"""Run kits x models x trials for one condition and save every result.

python run_eval.py --condition A --kits all --models all --trials 5
python run_eval.py --oracle          # reference solutions through the full grading path, no keys needed
"""
import argparse
import concurrent.futures as cf
import hashlib
import json
import os
import sys
import time
from pathlib import Path

from kitbench.grader import grade
from kitbench.kit import kit_names, reference_svg
from kitbench.models import MODELS, PRICE_PER_MTOK, RUN_MODELS, ApiError, call, settings
from kitbench.templates import CONDITIONS, TEMPLATE_VERSION, fill, part_ids

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
RAW = ROOT / "results_raw"


def load_env() -> None:
    """Read KEY=value lines from .env into the environment, without overriding existing variables."""
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


def raw_root_for(root: Path) -> Path:
    """Where raw provider responses go for a results root: results -> results_raw, a live run dir -> a sibling _raw dir."""
    return RAW if root == RESULTS else root.parent / (root.name + "_raw")


def result_path(condition: str, kit: str, model: str, trial: int, root: Path = RESULTS) -> Path:
    """Where one trial's result is stored."""
    return root / condition / kit / f"{model}__t{trial}.json"


def tags(g: dict, stop_reason: str) -> list[str]:
    """Searchable labels for a trial: outcome, failure type and the kinds of checks that failed."""
    from kitbench.stats import failure_type
    out = ["pass" if g["pass"] else "fail"]
    if not g["pass"]:
        out.append(failure_type({"grade": g, "stop_reason": stop_reason}))
        out += sorted({f"failed:{c['kind']}" for c in g["checks"] if not c["ok"]})
    return out


def is_done(path: Path, prompt: str) -> bool:
    """A stored result is reused only if it succeeded with exactly this prompt."""
    if not path.exists():
        return False
    done = json.loads(path.read_text())
    return done.get("status") == "ok" and done.get("prompt_sha256") == hashlib.sha256(prompt.encode()).hexdigest()


def estimate_cost(jobs: list[tuple]) -> str:
    """Upper-bound cost: prompt tokens estimated at 4 characters each, output at the token cap."""
    total, unknown = 0.0, set()
    for cond, kit, model, _ in jobs:
        price = PRICE_PER_MTOK.get(model)
        if price is None:
            unknown.add(model)
            continue
        cap = settings(model).get("max_tokens") or settings(model)["max_output_tokens"]
        total += (len(fill(kit, cond)) / 4 * price[0] + cap * price[1]) / 1e6
    note = f" (no price for {', '.join(sorted(unknown))})" if unknown else ""
    return f"upper-bound cost ${total:,.2f}{note}"


def run_trial(condition: str, kit: str, model: str, trial: int, root: Path = RESULTS) -> dict:
    """One fresh single-turn call, graded and saved; completed trials are reused."""
    path = result_path(condition, kit, model, trial, root)
    prompt = fill(kit, condition)
    if is_done(path, prompt):
        return json.loads(path.read_text())
    record = {"condition": condition, "kit": kit, "model": model, "trial": trial,
              "template_version": TEMPLATE_VERSION, "settings": settings(model),
              "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
              "date": time.strftime("%Y-%m-%d %H:%M:%S %Z")}
    try:
        out = call(model, prompt)
        g = grade(kit, out["text"], condition)
        raw_path = result_path(condition, kit, model, trial, raw_root_for(root))
        raw_path.parent.mkdir(parents=True, exist_ok=True)
        # the provider's response exactly as returned, kept apart so the graded record stays readable
        raw_path.write_text(json.dumps(out["raw"], indent=1, ensure_ascii=False))
        record.update(status="ok", prompt=prompt, output=out["text"], thinking=out["thinking"], stop_reason=out["stop_reason"],
                      input_tokens=out["input_tokens"], output_tokens=out["output_tokens"], thinking_tokens=out["thinking_tokens"],
                      response_id=out["response_id"], model_version=out["model_version"], usage=out["usage"],
                      started=out["started"], finished=out["finished"], seconds=out["seconds"], attempts=out["attempts"],
                      grade=g, tags=tags(g, out["stop_reason"]), raw_response_file=str(raw_path.relative_to(root.parent) if root != RESULTS else raw_path.relative_to(ROOT)))
    except ApiError as e:
        record.update(status="api_error", error=str(e))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, indent=1))
    return record


def oracle() -> None:
    """Grade every reference solution in every condition through the same path as model output."""
    bad = 0
    for kit in kit_names():
        for cond in CONDITIONS:
            g = grade(kit, reference_svg(kit, ids=part_ids(kit, cond)), cond)
            bad += not g["pass"]
            print(f"oracle {kit:13s} {cond:5s} {'PASS' if g['pass'] else 'FAIL'} {g['score']}")
    sys.exit(1 if bad else 0)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--condition", choices=sorted(CONDITIONS), help="prompt condition to run")
    ap.add_argument("--kits", default="all", help="comma-separated kit names, or 'all'")
    ap.add_argument("--models", default="all", help=f"comma-separated model ids, or 'all' = {', '.join(RUN_MODELS)} (also available: {', '.join(m for m in MODELS if m not in RUN_MODELS)})")
    ap.add_argument("--trials", type=int, default=5, help="trials per kit and model")
    ap.add_argument("--workers", type=int, default=6, help="parallel API calls")
    ap.add_argument("--dry-run", action="store_true", help="print the plan without calling any model")
    ap.add_argument("--oracle", action="store_true", help="grade the reference solutions instead of calling models")
    a = ap.parse_args()
    if a.oracle:
        oracle()
    if not a.condition:
        ap.error("--condition is required unless --oracle is given")
    kits = kit_names() if a.kits == "all" else a.kits.split(",")
    models = RUN_MODELS if a.models == "all" else a.models.split(",")
    unknown = [k for k in kits if k not in kit_names()] + [m for m in models if m not in MODELS]
    if unknown:
        ap.error(f"unknown kit or model: {', '.join(unknown)}")
    jobs = [(a.condition, k, m, t) for k in kits for m in models for t in range(1, a.trials + 1)]
    todo = [j for j in jobs if not is_done(result_path(*j), fill(j[1], j[0]))]
    print(f"condition {a.condition} ({CONDITIONS[a.condition]}): {len(jobs)} trials, {len(todo)} still to run, "
          f"{estimate_cost(todo)}", flush=True)
    if a.dry_run:
        return
    load_env()
    with cf.ThreadPoolExecutor(a.workers) as ex:
        for r in ex.map(lambda j: run_trial(*j), todo):
            if r["status"] == "ok":
                g = r["grade"]
                print(f"{r['kit']:13s} {r['model']:24s} t{r['trial']} {'PASS' if g['pass'] else 'FAIL'} "
                      f"score {g['score']:.2f} {r['seconds']}s", flush=True)
            else:
                print(f"{r['kit']:13s} {r['model']:24s} t{r['trial']} API_ERROR {r['error'][:80]}", flush=True)


if __name__ == "__main__":
    main()
