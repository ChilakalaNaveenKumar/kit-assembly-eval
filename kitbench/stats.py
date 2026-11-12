"""Every reported number is computed here, so the summary, README and dashboard can never disagree."""
import json
import re
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path

from .kit import criteria, load_task
from .models import MODELS, PRICE_PER_MTOK

LADDER = ["B", "A", "C"]  # hardest first: unnamed parts, no recipe, full recipe
FAILURE_TYPES = ["wrong connection (far off)", "near miss (just outside tolerance)",
                 "missing / extra / mirrored / scaled part", "no answer before token cap", "unusable output"]


def load(root: Path) -> list[dict]:
    """All result files under root/<condition>/<kit>/<model>__t<k>.json."""
    return [json.loads(p.read_text()) for p in sorted(root.glob("*/*/*.json"))]


def ok(rows: list[dict]) -> list[dict]:
    """Trials that produced a model result (API errors excluded from every number)."""
    return [r for r in rows if r.get("status") == "ok"]


def failure_type(r: dict) -> str:
    """One label per failed trial."""
    g = r["grade"]
    if r.get("stop_reason") in ("max_tokens", "FinishReason.MAX_TOKENS") and "no <svg> in reply" in g["issues"]:
        return FAILURE_TYPES[3]
    if g["issues"] and not g["checks"]:
        return FAILURE_TYPES[4]
    if any(k in i for i in g["issues"] for k in ("missing", "used", "mirrored", "scaled", "unknown", "non-finite")):
        return FAILURE_TYPES[2]
    bad = [c for c in g["checks"] if not c["ok"]]
    if any(c.get("err") is None or c["err"] > 3 * c["tol"] for c in bad):
        return FAILURE_TYPES[0]
    return FAILURE_TYPES[1]


def cost(rows: list[dict], model: str) -> float | None:
    """List-price cost of these trials, or None when the price is unconfirmed."""
    price = PRICE_PER_MTOK.get(model)
    if price is None:
        return None
    return sum(r["input_tokens"] * price[0] + r["output_tokens"] * price[1] for r in rows) / 1e6


def model_table(rows: list[dict], condition: str) -> list[dict]:
    """Per-model stats for one condition."""
    out = []
    for m in MODELS:
        rs = [r for r in ok(rows) if r["condition"] == condition and r["model"] == m]
        if not rs:
            continue
        by_kit = defaultdict(list)
        for r in rs:
            by_kit[r["kit"]].append(r["grade"]["pass"])
        n, passes = len(rs), sum(r["grade"]["pass"] for r in rs)
        out.append({"model": m, "trials": n, "passes": passes, "pass_rate": passes / n,
                    "passk": sum(all(v) for v in by_kit.values()), "kits": len(by_kit),
                    "mean_score": sum(r["grade"]["score"] for r in rs) / n,
                    "mean_output_tokens": sum(r["output_tokens"] for r in rs) / n,
                    "mean_seconds": sum(r["seconds"] for r in rs) / n, "cost_usd": cost(rs, m)})
    return out


def kit_grid(rows: list[dict], condition: str) -> dict[str, dict[str, dict]]:
    """kit -> model -> {passes, trials, mean_score}."""
    cells: dict = defaultdict(lambda: defaultdict(list))
    for r in ok(rows):
        if r["condition"] == condition:
            cells[r["kit"]][r["model"]].append(r)
    return {k: {m: {"passes": sum(r["grade"]["pass"] for r in rs), "trials": len(rs),
                    "mean_score": sum(r["grade"]["score"] for r in rs) / len(rs)} for m, rs in v.items()}
            for k, v in sorted(cells.items())}


def failure_breakdown(rows: list[dict], condition: str | None = None) -> dict[str, dict[str, int]]:
    """model -> failure type -> count of failed trials."""
    out: dict = {m: Counter() for m in MODELS}
    for r in ok(rows):
        if (condition is None or r["condition"] == condition) and not r["grade"]["pass"]:
            out[r["model"]][failure_type(r)] += 1
    return {m: dict(c) for m, c in out.items() if c}


def check_label(text: str) -> str:
    """A failed check's text without its tolerance suffix, for grouping."""
    return re.sub(r"\s*\(within [^)]*\)\s*$", "", text)


@lru_cache(maxsize=None)
def _specs(kit: str, condition: str) -> dict[str, dict]:
    """The grader's check specs of a kit in a condition, keyed by check text."""
    return {c["text"]: c for c in criteria(load_task(kit), condition)}


def mistake_key(kit: str, condition: str, text: str) -> tuple:
    """What a check physically tests, so differently worded checks of one joint group together."""
    spec = _specs(kit, condition).get(text)
    if spec is None:
        return (kit, check_label(text))
    if spec["kind"] == "joint":
        return (kit, "joint", spec["b"], spec["bn"])  # parts sharing one pin fail together, so they count once
    if "a" in spec and "an" in spec:
        return (kit, spec["kind"], spec["a"], spec["an"])
    return (kit, spec["kind"], spec.get("part"))


def top_mistakes(rows: list[dict], limit: int = 12) -> list[dict]:
    """The most frequently failed checks, one entry per physical joint, with trial counts and one example trial."""
    groups: dict = defaultdict(dict)
    for r in ok(rows):
        for c in r["grade"]["checks"]:
            if c["ok"]:
                continue
            trial = (r["condition"], r["kit"], r["model"], r["trial"])
            hit = groups[mistake_key(r["kit"], r["condition"], c["text"])]
            if trial not in hit or (c.get("err") or 0) > (hit[trial][1].get("err") or 0):
                hit[trial] = (r, c)
    merged: dict = {}
    for key, by_trial in groups.items():
        sig = frozenset(by_trial) if len(by_trial) >= 5 else frozenset((t, round((c.get("err") or 0) / 10)) for t, (_, c) in by_trial.items())
        merged.setdefault((key[0], sig), {}).update(by_trial)  # same trials failing together is one displaced part
    out = []
    for key, by_trial in sorted(((sig[0], v) for sig, v in merged.items()), key=lambda kv: (-len(kv[1]), str(kv[0])))[:limit]:
        hits = list(by_trial.values())
        errs = [c["err"] for _, c in hits if c.get("err") is not None]
        ex, ex_check = max(hits, key=lambda h: h[1].get("err") or 0)
        label = Counter(check_label(c["text"]) for _, c in hits).most_common(1)[0][0]
        out.append({"kit": key, "check": label, "trials": len(hits),
                    "models": dict(Counter(r["model"] for r, _ in hits)),
                    "conditions": dict(Counter(r["condition"] for r, _ in hits)),
                    "median_err": sorted(errs)[len(errs) // 2] if errs else None, "max_err": max(errs) if errs else None,
                    "example": {"cond": ex["condition"], "kit": ex["kit"], "model": ex["model"], "trial": ex["trial"],
                                "label": check_label(ex_check["text"])}})
    return out


def ladder(rows: list[dict]) -> dict[str, dict[str, float]]:
    """model -> condition -> full-pass rate, for the conditions on the difficulty ladder."""
    out: dict = defaultdict(dict)
    for cond in LADDER:
        for t in model_table(rows, cond):
            out[t["model"]][cond] = t["pass_rate"]
    return dict(out)


def condition_summary(rows: list[dict], condition: str) -> dict:
    """Headline numbers for one condition: trial counts, best model, and the mean of the per-model pass rates."""
    table = model_table(rows, condition)
    best = max(table, key=lambda t: t["pass_rate"], default=None)
    return {"condition": condition, "models": len(table), "trials": sum(t["trials"] for t in table),
            "passes": sum(t["passes"] for t in table),
            "mean_rate": sum(t["pass_rate"] for t in table) / len(table) if table else None,
            "best_model": best["model"] if best else None, "best_rate": best["pass_rate"] if best else None,
            "best_trials": best["trials"] if best else 0}


def failed_trials(rows: list[dict]) -> list[dict]:
    """Every failed trial with its failure type, newest first."""
    out = [{"cond": r["condition"], "kit": r["kit"], "model": r["model"], "trial": r["trial"],
            "score": r["grade"]["score"], "date": r.get("date") or "", "failure_type": failure_type(r),
            "failed_checks": sum(not c["ok"] for c in r["grade"]["checks"]), "checks": len(r["grade"]["checks"]),
            "token_limit": (r.get("settings") or {}).get("max_tokens") or (r.get("settings") or {}).get("max_output_tokens")}
           for r in ok(rows) if not r["grade"]["pass"]]
    return sorted(out, key=lambda f: (f["date"], f["cond"], f["kit"], f["model"], f["trial"]), reverse=True)


def check_kinds(rows: list[dict]) -> dict[tuple[str, str], str]:
    """(kit, check label) -> check kind, so a mistake's error can be shown in px or degrees."""
    return {(r["kit"], check_label(c["text"])): c["kind"] for r in ok(rows) for c in r["grade"]["checks"]}


POINT_KINDS = ("joint", "online", "radial", "level")


def story_example(rows: list[dict], conditions: tuple[str, ...] = ("A", "B", "C", "A_alt")) -> dict | None:
    """A trial where a strong model gets only a few connections wrong and one is far off, for the how-it-works strip."""
    for cond in conditions:
        pool = [r for r in ok(rows) if r["condition"] == cond and r["grade"]["checks"] and not r["grade"]["pass"]]
        if not pool:
            continue

        def key(r: dict) -> tuple:
            bad = [c for c in r["grade"]["checks"] if not c["ok"]]
            far = max((c.get("err") or 0 for c in bad if c["kind"] in POINT_KINDS), default=0)
            return (len(bad) <= 3 and far >= 80, -MODELS.index(r["model"]), -len(bad), far)

        r = max(pool, key=key)
        checks = r["grade"]["checks"]
        return {"cond": cond, "kit": r["kit"], "model": r["model"], "trial": r["trial"], "checks": len(checks),
                "failed": sum(not c["ok"] for c in checks)}
    return None


def ladder_matched(rows: list[dict]) -> dict[str, dict]:
    """Per model, B/A/C pass rates over only the kits it has finished in all three, so the conditions compare like with like."""
    out = {}
    for m in MODELS:
        mine = [r for r in ok(rows) if r["model"] == m and r["condition"] in LADDER]
        counts = {(r["kit"], r["condition"]) for r in mine}
        per_kit = {k: [sum(1 for r in mine if r["kit"] == k and r["condition"] == c) for c in LADDER] for k, _ in counts}
        # a kit is compared only when every condition has the same number of finished trials
        kits = sorted(k for k, n in per_kit.items() if min(n) > 0 and len(set(n)) == 1)
        if not kits:
            continue
        per = {}
        for c in LADDER:
            rs = [r for r in mine if r["condition"] == c and r["kit"] in kits]
            per[c] = {"rate": sum(r["grade"]["pass"] for r in rs) / len(rs), "passes": sum(r["grade"]["pass"] for r in rs), "trials": len(rs)}
        out[m] = {"kits": kits, "conditions": per}
    return out


def check_index(row: dict, label: str) -> int | None:
    """Index of the first failed check of a trial whose grouped label matches, so a close-up can target it."""
    for i, c in enumerate(row["grade"]["checks"]):
        if not c["ok"] and check_label(c["text"]) == label:
            return i
    return None


def top_mistakes_indexed(rows: list[dict], limit: int = 12) -> list[dict]:
    """top_mistakes with the failed-check index of each example, for annotated close-ups."""
    by_key = {(r["condition"], r["kit"], r["model"], r["trial"]): r for r in ok(rows)}
    out = []
    for m in top_mistakes(rows, limit):
        ex = m["example"]
        row = by_key.get((ex["cond"], ex["kit"], ex["model"], ex["trial"]))
        out.append({**m, "example": {**ex, "index": None if row is None else check_index(row, ex["label"])}})
    return out
