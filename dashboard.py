"""Local dashboard: browse saved results, inspect kits, and run small live batches into results_live/.

python dashboard.py --port 8000     # serves http://127.0.0.1:8000 only
"""
import argparse
import concurrent.futures as cf
import json
import os
import re
import threading
import time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

import run_eval
from kitbench import stats
from kitbench.kit import ORIENT_TOL, TASKS, kit_names, kit_svg, kit_tolerance, load_kit, load_task, reference_svg
from kitbench.models import MODELS, claude_route, provider, settings
from kitbench.annotate import failed_points
from kitbench.overlay import aligned_reference_svg, annotated_svg, fitted_trial_svg, has_closeup, hero_marks, kit_parts_svg, kit_sheet_svg, replay_payload
from kitbench.render import assembly_svg
from kitbench.templates import CONDITIONS, TEMPLATE_VERSION, fill, part_ids

ROOT = Path(__file__).resolve().parent
LIVE_ROOT = ROOT / "results_live"
TRANSCRIPTS = ROOT / "transcripts"
CONDITION_ORDER = ["B", "A", "C", "A_alt"]  # hardest first, so failures lead
CONDITION_NAMES = {"B": "Joints not listed, parts unnamed", "A": "Joints not listed", "C": "Joints listed",
                   "A_alt": "Joints not listed, reworded request"}
CONDITION_LETTER = {"B": "B", "A": "A", "C": "C", "A_alt": "A′"}  # the internal id is never shown
CONDITION_SHORT = dict(CONDITION_NAMES)
MODEL_NAMES = {"claude-opus-5-5": "Claude Opus 5.5", "claude-sonnet-5-5": "Claude Sonnet 5.5", "claude-haiku-5-5": "Claude Haiku 5.5",
               "gemini-3.1-pro-preview": "Gemini 3.1 Pro", "gemini-3.8-flash": "Gemini 3.8 Flash"}
WEB = ROOT / "web"
STATIC = {"/": ("index.html", "text/html; charset=utf-8"), "/index.html": ("index.html", "text/html; charset=utf-8"),
          "/app.css": ("app.css", "text/css; charset=utf-8"), "/app.js": ("app.js", "text/javascript; charset=utf-8"),
          "/vendor/echarts.min.js": ("vendor/echarts.min.js", "text/javascript; charset=utf-8"),
          "/vendor/fonts/fonts.css": ("vendor/fonts/fonts.css", "text/css; charset=utf-8"),
          "/vendor/fonts/RobotoCondensed.woff2": ("vendor/fonts/RobotoCondensed.woff2", "font/woff2"),
          "/vendor/fonts/SourceSerif4.woff2": ("vendor/fonts/SourceSerif4.woff2", "font/woff2")}
PAGE_CSP = "default-src 'self'; img-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'"
CHECK_KINDS = [
    {"kind": "joint", "name": "Joint", "text": "Two features of connected parts (pin, axle or bolt holes, hub centres, seats) coincide."},
    {"kind": "online", "name": "On guide line", "text": "A sliding part sits on the centre line of its guide, such as a piston in its bore."},
    {"kind": "radial", "name": "Radial position", "text": "A feature sits on the axis through a centre, on the correct side of it."},
    {"kind": "level", "name": "Level", "text": "Two features that rest on the ground stand at the same height."},
    {"kind": "orient", "name": "Orientation", "text": "A part faces the way it does on the working object, measured against the base part."},
    {"kind": "upright", "name": "Base upright", "text": "The base part stays upright, as stored."},
    {"kind": "angle", "name": "Fixed angle", "text": "A fixed angle between a part and the base part, where the request states one."},
]
KEY_NAMES = {"anthropic": "ANTHROPIC_API_KEY", "gemini": "GEMINI_API_KEY"}
JSON_TYPE = "application/json"
RUN_ID = re.compile(r"^\d{8}-\d{6}$")
FILE_NAME = re.compile(r"^[A-Za-z0-9_.-]+$")
MAX_BODY = 65536
NO_SVG = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 120" width="600" height="120">'
          '<rect width="600" height="120" fill="#F8F7F2"/>'
          '<text x="20" y="66" font-size="20" font-family="Helvetica" fill="#a33">no usable SVG in the reply</text></svg>')


class LiveRun:
    """Progress of one live run; mutated only under its lock."""

    def __init__(self, run_id: str, total: int) -> None:
        self.lock = threading.Lock()
        self.data = {"run": run_id, "state": "running", "total": total, "done": 0, "trials": [], "error": None}

    def add(self, row: dict) -> None:
        """Record one finished trial."""
        with self.lock:
            self.data["trials"].append(row)
            self.data["done"] += 1

    def finish(self, state: str, error: str | None = None) -> None:
        """Mark the run finished or failed."""
        with self.lock:
            self.data["state"], self.data["error"] = state, error

    def snapshot(self) -> dict:
        """A copy safe to serialise."""
        with self.lock:
            return json.loads(json.dumps(self.data))


class State:
    """Per-server state: where live results go and the current live run."""

    def __init__(self, live_root: Path) -> None:
        self.live_root = live_root
        self.run: LiveRun | None = None
        self.lock = threading.Lock()


def read_results(root: Path) -> dict[str, list[dict]]:
    """Every result file under root/<condition>/<kit>/, grouped by condition."""
    out: dict[str, list[dict]] = {}
    for cond in CONDITIONS:
        rows = []
        for p in sorted((root / cond).glob("*/*.json")) if (root / cond).is_dir() else []:
            try:
                rows.append(json.loads(p.read_text()))
            except (OSError, ValueError):
                continue  # a file still being written by a running job
        if rows:
            out[cond] = rows
    return out


def trial_brief(r: dict) -> dict:
    """The small per-trial record shown in lists."""
    ok = r.get("status") == "ok"
    return {"trial": r["trial"], "status": r.get("status"), "pass": ok and r["grade"]["pass"],
            "score": r["grade"]["score"] if ok else None, "seconds": r.get("seconds"),
            "error": None if ok else str(r.get("error", ""))[:200], "tokens": r.get("output_tokens") if ok else None,
            "failure_type": stats.failure_type(r) if ok and not r["grade"]["pass"] else None,
            "cost_usd": stats.cost([r], r["model"]) if ok else None,
            "route": "Vertex AI" if (r.get("settings") or {}).get("route") == "vertex" else "Claude API"}


def summarise(root: Path) -> list[dict]:
    """Per-condition tables, grids and API-error lists for one results root."""
    out = []
    grouped = read_results(root)
    empty = {"passes": 0, "trials": 0, "mean_score": None}
    for cond in [c for c in CONDITION_ORDER if c in grouped]:
        rows = grouped[cond]
        counts = stats.kit_grid(rows, cond)
        cells: dict = {}
        for r in rows:
            cells.setdefault(r["kit"], {}).setdefault(r["model"], []).append(r)
        grid = {k: {m: {**counts.get(k, {}).get(m, empty), "list": [trial_brief(r) for r in sorted(rs, key=lambda x: x["trial"])]}
                    for m, rs in sorted(v.items())} for k, v in sorted(cells.items())}
        errors = [{"kit": r["kit"], "model": r["model"], "trial": r["trial"], "error": str(r.get("error", ""))[:200]}
                  for r in rows if r.get("status") != "ok"]
        out.append({"condition": cond, "description": CONDITIONS[cond], "models": stats.model_table(rows, cond),
                    "grid": grid, "api_errors": errors})
    return out


def results_payload(state: State) -> dict:
    """Submitted results plus live runs, kept apart."""
    live = []
    if state.live_root.is_dir():
        for d in sorted(state.live_root.iterdir(), reverse=True):
            if d.is_dir() and RUN_ID.match(d.name):
                conds = summarise(d)
                if conds:
                    live.append({"run": d.name, "conditions": conds})
    return {"conditions": summarise(run_eval.RESULTS), "live": live, "as_of": data_as_of()}


def submitted_rows() -> list[dict]:
    """Every submitted result row, all conditions, for the stats functions."""
    return [r for rows in read_results(run_eval.RESULTS).values() for r in rows]


def conditions_info() -> list[dict]:
    """Condition ids in ladder order with their names and descriptions."""
    ran = {r["condition"] for r in submitted_rows()} or set(CONDITION_ORDER)
    return [{"id": c, "letter": CONDITION_LETTER[c], "name": CONDITION_NAMES[c], "short": CONDITION_SHORT[c], "description": CONDITIONS[c]} for c in CONDITION_ORDER if c in ran]


def result_models() -> list[str]:
    """Models that have submitted results, in the configured order (the run may use a subset)."""
    ran = {r["model"] for r in submitted_rows()}
    return [m for m in MODELS if m in ran] or MODELS


def data_as_of() -> str:
    """UTC time of the newest submitted result file, so readers can tell when numbers last moved."""
    times = [p.stat().st_mtime for p in run_eval.RESULTS.glob("*/*/*.json")]
    return datetime.fromtimestamp(max(times), timezone.utc).isoformat(timespec="seconds") if times else ""


def story_with_noun(story: dict | None) -> dict | None:
    """The walkthrough trial plus what the kit's object is called in the instruction."""
    return None if story is None else {**story, "noun": load_task(story["kit"]).OBJECT.partition(" (")[0]}


def short_check(text: str) -> str:
    """The part a check is about, for captions; the full text stays in tooltips."""
    part = text.split(":")[0] if ":" in text else text.split(" faces ")[0].split(" stays ")[0]
    return part.strip()[:40] or "Part"


def hero_payload(mistakes: list[dict], rows: list[dict]) -> dict | None:
    """The most striking failure: the first common mistake whose worst example has a drawable landed point, else the first mistake."""
    by_key = {(r["condition"], r["kit"], r["model"], r["trial"]): r for r in rows if r.get("status") == "ok"}
    first = None
    for m in mistakes:
        ex = m["example"]
        row = by_key.get((ex["cond"], ex["kit"], ex["model"], ex["trial"]))
        if row is None or ex["index"] is None:
            continue
        marks = hero_marks(row["kit"], row["output"], row["condition"], row["grade"], ex["index"])
        item = {"cond": ex["cond"], "kit": ex["kit"], "model": ex["model"], "trial": ex["trial"], "index": ex["index"],
                "check": m["check"], "short": m["short"], "kind": m["kind"], **marks}
        if marks["point"] is not None:
            return item
        first = first or item
    return first


def overview_payload() -> dict:
    """Everything the Overview tab draws, straight from kitbench.stats."""
    rows = submitted_rows()
    kinds = stats.check_kinds(rows)
    counted = [r for r in rows if r["condition"] in stats.LADDER]
    mistakes = [{**m, "kind": kinds.get((m["kit"], m["check"]))} for m in stats.top_mistakes_indexed(counted)]
    mistakes = [{**m, "short": short_check(m["check"])} for m in mistakes]
    done = [r for r in stats.ok(rows) if r["condition"] in stats.LADDER]
    totals = {"trials": len(done), "kits": len({r["kit"] for r in done}), "models": len({r["model"] for r in done}), "kit_names": sorted({r["kit"] for r in done})}
    return {"totals": totals, "hero": hero_payload(mistakes, counted), "as_of": data_as_of(), "story": story_with_noun(stats.story_example(counted, ("A", "B", "C"))), "conditions": conditions_info(), "ladder_order": stats.LADDER, "models": result_models(), "kits": kit_names(),
            "ladder": stats.ladder(rows), "ladder_matched": stats.ladder_matched(rows), "summary": {c: stats.condition_summary(rows, c) for c in CONDITION_ORDER},
            "tables": {c: stats.model_table(rows, c) for c in CONDITION_ORDER},
            "failure_types": stats.FAILURE_TYPES,
            "failures": {"all": stats.failure_breakdown(counted), **{c: stats.failure_breakdown(rows, c) for c in CONDITION_ORDER}},
            "top_mistakes": mistakes, "grids": {c: stats.kit_grid(rows, c) for c in CONDITION_ORDER}}


def failures_payload() -> dict:
    """Every failed submitted trial, newest first, plus the filter vocabularies."""
    rows = submitted_rows()
    by_key = {(r["condition"], r["kit"], r["model"], r["trial"]): r for r in stats.ok(rows)}
    failures = []
    for f in stats.failed_trials(rows):
        r = by_key[(f["cond"], f["kit"], f["model"], f["trial"])]
        first = next((c["text"] for c in r["grade"]["checks"] if not c["ok"]), "")
        failures.append({**f, "closeup": has_closeup(r["kit"], r["output"], r["condition"], r["grade"]) if f["checks"] else False, "first_check": first})
    return {"as_of": data_as_of(), "failures": failures, "failure_types": stats.FAILURE_TYPES, "models": result_models(),
            "kits": kit_names(), "conditions": conditions_info()}


def stored_settings(model: str) -> dict:
    """The request settings saved in the model's submitted results, not today's defaults."""
    for r in submitted_rows():
        if r["model"] == model and r.get("settings"):
            return r["settings"]
    return settings(model)


def method_payload() -> dict:
    """The grading rules, per-kit tolerances and model settings shown on the Method tab."""
    tasks = {k: load_task(k) for k in kit_names()}
    return {"conditions": conditions_info(), "check_kinds": CHECK_KINDS, "orient_tol": ORIENT_TOL,
            "template_version": TEMPLATE_VERSION, "kits": kit_names(), "kits_run": sorted({r["kit"] for r in submitted_rows()}),
            "tolerances": {k: {"position_px": kit_tolerance(t), "upright_deg": t.UPRIGHT[1]} for k, t in tasks.items()},
            "models": [{"model": m, "settings": stored_settings(m)} for m in result_models()]}


def trial_file(state: State, q: dict) -> Path | None:
    """Validate trial query parameters and map them to a result file, or None."""
    src, cond, kit, model = (q.get(k, [""])[0] for k in ("src", "cond", "kit", "model"))
    try:
        trial = int(q.get("trial", ["0"])[0])
    except ValueError:
        return None
    if cond not in CONDITIONS or kit not in kit_names() or model not in MODELS or not 1 <= trial <= 99:
        return None
    if src == "results":
        root = run_eval.RESULTS
    elif src == "live" and RUN_ID.match(q.get("run", [""])[0]):
        root = state.live_root / q["run"][0]
    else:
        return None
    path = run_eval.result_path(cond, kit, model, trial, root)
    return path if path.is_file() else None


def raw_file(q: dict, root: Path, suffix: str) -> Path | None:
    """Map validated cond, kit, model, trial to root/<cond>/<kit>/<model>__t<k><suffix>, or None."""
    cond, kit, model = (q.get(k, [""])[0] for k in ("cond", "kit", "model"))
    t = q.get("trial", [""])[0]
    if cond not in CONDITIONS or kit not in kit_names() or model not in MODELS or not t.isascii() or not t.isdigit() or not 1 <= int(t) <= 99:
        return None
    return root / cond / kit / f"{model}__t{int(t)}{suffix}"


def trial_row(state: State, q: dict) -> dict | None:
    """The stored result of a finished (status ok) trial named by cond, kit, model, trial (src defaults to submitted results)."""
    path = trial_file(state, {**q, "src": q.get("src", ["results"])})
    row = json.loads(path.read_text()) if path else None
    return row if row and row.get("status") == "ok" else None


def trial_detail(path: Path) -> dict:
    """Everything the detail view shows for one stored trial."""
    r = json.loads(path.read_text())
    if r.get("status") != "ok":
        return {"status": r.get("status"), "error": str(r.get("error", ""))[:300]}
    g = r["grade"]
    return {"status": "ok", "pass": g["pass"], "score": g["score"], "issues": g["issues"], "failure_type": None if g["pass"] else stats.failure_type(r), "stop_reason": r.get("stop_reason"),
            "input_tokens": r.get("input_tokens"), "output_tokens": r["output_tokens"], "seconds": r["seconds"],
            "date": r.get("date"), "failed": [{**c, "index": i, "closeup": has_closeup(r["kit"], r["output"], r["condition"], g, i)} for i, c in enumerate(g["checks"]) if not c["ok"]], "n_checks": len(g["checks"]),
            "output": r["output"], "condition": r["condition"], "kit": r["kit"], "model": r["model"], "trial": r["trial"]}


def kits_payload() -> list[dict]:
    """Each kit with its object name, canvas, image availability and part ids per condition."""
    out = []
    for kit in kit_names():
        task = load_task(kit)
        build = TASKS / kit / "build"
        noun, _, view = task.OBJECT.partition(" (")
        out.append({"kit": kit, "object": task.OBJECT, "noun": noun, "view": view.rstrip(")"), "canvas": list(task.CANVAS),
                    "images": [f for f in ("reference.png", "kit_marked.png") if (build / f).is_file()],
                    "parts": {c: sorted(part_ids(kit, c).values()) for c in CONDITIONS}})
    return out


def prompt_kit_svg(kit: str, cond: str) -> str:
    """The kit SVG exactly as the prompt carries it, parts in id order."""
    ids, data = part_ids(kit, cond), load_kit(kit)
    return kit_svg(data, ids, order=sorted(data, key=lambda p: ids[p]))


def solution_svg(kit: str, cond: str) -> str:
    """The correct assembly as a standalone SVG: the kit defs plus one <use> per part."""
    ids, defs = part_ids(kit, cond), prompt_kit_svg(kit, cond)
    defs = defs[defs.index("<defs>"):defs.index("</defs>") + 7]
    ref = reference_svg(kit, ids=ids)
    cut = ref.index(">") + 1
    return ref[:cut] + defs + ref[cut:]


def kit_file(name: str) -> Path | None:
    """Resolve '<kit>/<file>' inside tasks/<kit>/build only, or None."""
    parts = name.split("/")
    if len(parts) != 2 or parts[0] not in kit_names() or not FILE_NAME.match(parts[1]) or parts[1].startswith("."):
        return None
    build = (TASKS / parts[0] / "build").resolve()
    path = (build / parts[1]).resolve()
    return path if path.parent == build and path.is_file() else None


def parse_plan(body: dict) -> tuple[list[tuple], str | None]:
    """Validate a plan/run request; returns (jobs, error)."""
    cond, kits, models = body.get("condition"), body.get("kits") or [], body.get("models") or []
    try:
        trials, workers = int(body.get("trials", 1)), int(body.get("workers", 6))
    except (TypeError, ValueError):
        return [], "trials and workers must be numbers"
    if cond not in CONDITIONS:
        return [], "unknown condition"
    if not kits or any(k not in kit_names() for k in kits):
        return [], "choose at least one valid kit"
    if not models or any(m not in MODELS for m in models):
        return [], "choose at least one valid model"
    if not 1 <= trials <= 5 or not 1 <= workers <= 12:
        return [], "trials must be 1-5 and workers 1-12"
    return [(cond, k, m, t) for k in kits for m in models for t in range(1, trials + 1)], None


def scrub(text: str, secrets: list[str]) -> str:
    """Remove any key value from a message before it is stored."""
    for s in secrets:
        if s:
            text = text.replace(s, "[key]")
    return text


def execute_run(state: State, run: LiveRun, jobs: list[tuple], workers: int, keys: dict[str, str]) -> None:
    """Run the jobs with the keys in the environment only for this thread's duration."""
    root = state.live_root / run.data["run"]
    saved = {n: os.environ.get(n) for n in keys}
    secrets = list(keys.values())
    os.environ.update({n: v for n, v in keys.items() if v})

    def one(job: tuple) -> None:
        try:
            r = run_eval.run_trial(*job, root=root)
            ok = r.get("status") == "ok"
            run.add({"cond": job[0], "kit": job[1], "model": job[2], "trial": job[3], "status": r.get("status"),
                     "pass": ok and r["grade"]["pass"], "score": r["grade"]["score"] if ok else None,
                     "seconds": r.get("seconds"), "error": None if ok else scrub(str(r.get("error", "")), secrets)[:200]})
        except Exception as e:  # noqa: BLE001 - one bad trial must not stop the batch
            run.add({"cond": job[0], "kit": job[1], "model": job[2], "trial": job[3], "status": "error", "pass": False,
                     "score": None, "seconds": None, "error": scrub(f"{type(e).__name__}: {e}", secrets)[:200]})

    try:
        with cf.ThreadPoolExecutor(workers) as ex:
            list(ex.map(one, jobs))
        run.finish("done")
    except Exception as e:  # noqa: BLE001 - surfaced to the page instead of killing the thread silently
        run.finish("error", scrub(f"{type(e).__name__}: {e}", secrets)[:200])
    finally:
        for n, old in saved.items():
            if old is None:
                os.environ.pop(n, None)
            else:
                os.environ[n] = old


def start_run(state: State, body: dict) -> tuple[int, dict]:
    """Validate, then start the background run; keys never leave this function except into the run thread."""
    jobs, err = parse_plan(body)
    if err:
        return 400, {"error": err}
    keys = {KEY_NAMES["anthropic"]: str(body.get("anthropic_key") or "").strip(),
            KEY_NAMES["gemini"]: str(body.get("gemini_key") or "").strip()}
    for m in {provider(j[2]) for j in jobs}:
        name = KEY_NAMES[m]
        if m == "anthropic" and claude_route() == "vertex":
            if not os.environ.get("GOOGLE_CLOUD_PROJECT"):
                return 400, {"error": "GOOGLE_CLOUD_PROJECT is needed for Claude on Google Vertex AI"}
        elif not keys[name] and not os.environ.get(name):
            return 400, {"error": f"{name} is needed for the chosen models"}
    with state.lock:
        if state.run and state.run.data["state"] == "running":
            return 409, {"error": "a live run is already in progress"}
        run = LiveRun(time.strftime("%Y%m%d-%H%M%S"), len(jobs))
        state.run = run
    threading.Thread(target=execute_run, args=(state, run, jobs, int(body.get("workers", 6)), keys), daemon=True).start()
    return 200, {"run": run.data["run"], "total": len(jobs)}


class Handler(BaseHTTPRequestHandler):
    """Routes for the page, JSON data, SVG renders, kit images and live runs."""

    server_version = "dashboard"

    def log_message(self, fmt: str, *args) -> None:  # noqa: D102 - silent: request bodies carry keys
        return

    def _send(self, code: int, body: bytes, ctype: str, extra: dict | None = None) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        headers = {"Cache-Control": "no-store", "X-Content-Type-Options": "nosniff", **(extra or {})}
        for k, v in headers.items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def _json(self, obj: object, code: int = 200) -> None:
        self._send(code, json.dumps(obj).encode(), "application/json")

    def _svg(self, svg: str, cache: str = "no-store") -> None:
        self._send(200, svg.encode(), "image/svg+xml",
                   {"Content-Security-Policy": "default-src 'none'; style-src 'unsafe-inline'", "Cache-Control": cache})

    def _annotated(self, state: "State", q: dict) -> None:
        row = trial_row(state, q)
        if row is None:
            return self._json({"error": "not found"}, 404)
        raw = q.get("i", [None])[0]
        if raw is not None and not (raw.isascii() and raw.isdigit() and int(raw) < len(row["grade"]["checks"])):
            return self._json({"error": "not found"}, 404)
        svg = annotated_svg(row["kit"], row["output"], row["condition"], row["grade"], None if raw is None else int(raw),
                            q.get("zoom", ["1"])[0] != "0", q.get("ref", ["0"])[0] == "1", q.get("all", ["0"])[0] == "1", q.get("fit", ["0"])[0] == "1")
        self._svg(svg or NO_SVG)

    def do_GET(self) -> None:  # noqa: N802, D102
        url = urlparse(self.path)
        q = parse_qs(url.query)
        state: State = self.server.state
        try:
            if url.path in STATIC:
                name, ctype = STATIC[url.path]
                self._send(200, (WEB / name).read_bytes(), ctype, {"Content-Security-Policy": PAGE_CSP} if ctype.startswith("text/html") else None)
            elif url.path == "/api/results":
                self._json(results_payload(state))
            elif url.path == "/api/overview":
                self._json(overview_payload())
            elif url.path == "/api/failures":
                self._json(failures_payload())
            elif url.path == "/api/method":
                self._json(method_payload())
            elif url.path == "/api/trial":
                path = trial_file(state, q)
                self._json(trial_detail(path)) if path else self._json({"error": "not found"}, 404)
            elif url.path in ("/raw", "/transcript"):
                raw = url.path == "/raw"
                path = raw_file(q, run_eval.RAW if raw else TRANSCRIPTS, ".json" if raw else ".md")
                if path is None:
                    return self._json({"error": "bad request"}, 400)
                if not path.is_file():
                    return self._json({"error": "not found"}, 404)
                self._send(200, path.read_bytes(), "application/json" if raw else "text/plain; charset=utf-8")
            elif url.path == "/svg/trial":
                path = trial_file(state, q)
                if not path:
                    return self._json({"error": "not found"}, 404)
                r = json.loads(path.read_text())
                title = "" if q.get("plain", ["0"])[0] == "1" else "model output"
                paper = q.get("paper", ["1"])[0] != "0"
                draw = (lambda *a: fitted_trial_svg(*a, paper=paper)) if q.get("fit", ["0"])[0] == "1" else assembly_svg
                self._svg((r.get("status") == "ok" and draw(r["kit"], r["output"], r["condition"], title)) or NO_SVG)
            elif url.path == "/svg/annotated":
                self._annotated(state, q)
            elif url.path in ("/api/replay", "/api/annotations"):
                row = trial_row(state, q)
                if row is None:
                    return self._json({"error": "not found"}, 404)
                grade = row["grade"]
                if url.path == "/api/annotations":
                    self._json({"points": failed_points(row["kit"], row["output"], row["condition"], grade)})
                else:
                    self._json(replay_payload(row["kit"], row["output"], row["condition"], grade))
            elif url.path == "/svg/reference":
                kit, cond = q.get("kit", [""])[0], q.get("cond", ["A"])[0]
                if kit not in kit_names() or cond not in CONDITIONS:
                    return self._json({"error": "not found"}, 404)
                title = "" if q.get("plain", ["0"])[0] == "1" else "reference"
                if "model" in q:  # a trial's own frame: the correct assembly placed on the model's base part
                    row = trial_row(state, q)
                    if row is None:
                        return self._json({"error": "not found"}, 404)
                    return self._svg(aligned_reference_svg(row["kit"], row["output"], row["condition"], title, q.get("paper", ["1"])[0] != "0") or NO_SVG)
                # the reference never changes while the page is open, so thumbnails can be cached briefly
                self._svg(assembly_svg(kit, reference_svg(kit, ids=part_ids(kit, cond)), cond, title) or NO_SVG, "private, max-age=60")
            elif url.path == "/svg/kit":
                kit, cond = q.get("kit", [""])[0], q.get("cond", ["A"])[0]
                if kit not in kit_names() or cond not in CONDITIONS:
                    return self._json({"error": "not found"}, 404)
                plain = q.get("plain", ["0"])[0] == "1"
                self._svg(kit_parts_svg(kit, cond) if plain else kit_sheet_svg(kit, cond), "private, max-age=60")
            elif url.path in ("/svg/kitparts", "/svg/solution", "/api/kitsvg"):
                kit, cond = q.get("kit", [""])[0], q.get("cond", [""])[0]
                if set(q) != {"kit", "cond"} or len(q["kit"]) != 1 or len(q["cond"]) != 1:
                    return self._json({"error": "bad request"}, 400)
                if kit not in kit_names() or cond not in CONDITIONS:
                    return self._json({"error": "not found"}, 404)
                if url.path == "/api/kitsvg":
                    self._json({"parts_svg": prompt_kit_svg(kit, cond), "solution_svg": solution_svg(kit, cond)})
                else:
                    self._svg(prompt_kit_svg(kit, cond) if url.path == "/svg/kitparts" else solution_svg(kit, cond), "private, max-age=60")
            elif url.path == "/api/kits":
                self._json({"kits": kits_payload(), "conditions": {c: CONDITIONS[c] for c in CONDITION_ORDER}})
            elif url.path == "/api/prompt":
                kit, cond = q.get("kit", [""])[0], q.get("cond", [""])[0]
                if kit not in kit_names() or cond not in CONDITIONS:
                    return self._json({"error": "not found"}, 404)
                self._json({"prompt": fill(kit, cond)})
            elif url.path.startswith("/kitfile/"):
                path = kit_file(unquote(url.path[len("/kitfile/"):]))
                if not path:
                    return self._json({"error": "not found"}, 404)
                ctype = {".png": "image/png", ".svg": "image/svg+xml", ".json": "application/json"}.get(path.suffix, "application/octet-stream")
                self._send(200, path.read_bytes(), ctype, {"Content-Security-Policy": "default-src 'none'; style-src 'unsafe-inline'"})
            elif url.path == "/api/options":
                self._json({"conditions": {c: CONDITIONS[c] for c in CONDITION_ORDER}, "condition_info": conditions_info(),
                            "kits": kit_names(), "models": result_models(), "model_names": MODEL_NAMES, "failure_types": stats.FAILURE_TYPES,
                            "route": claude_route()})
            elif url.path == "/api/status":
                self._json(state.run.snapshot() if state.run else {"state": "idle"})
            else:
                self._json({"error": "not found"}, 404)
        except Exception as e:  # noqa: BLE001 - never leak a traceback or crash the server thread
            self._json({"error": type(e).__name__}, 500)

    def _local_origin(self) -> bool:
        """True when Host (and Origin, if the browser sent one) name this server, which stops other web pages posting to it."""
        ok = {f"127.0.0.1:{self.server.server_address[1]}", f"localhost:{self.server.server_address[1]}"}
        origin = self.headers.get("Origin")
        return self.headers.get("Host") in ok and (origin is None or urlparse(origin).netloc in ok)

    def do_POST(self) -> None:  # noqa: N802, D102
        state: State = self.server.state
        if not self._local_origin():
            return self._json({"error": "forbidden"}, 403)
        if self.headers.get("Content-Type", "").split(";")[0].strip().lower() != JSON_TYPE:
            return self._json({"error": "content type must be application/json"}, 415)
        try:
            size = int(self.headers.get("Content-Length", "0"))
            if size > MAX_BODY:
                return self._json({"error": "body too large"}, 413)
            body = json.loads(self.rfile.read(size) or b"{}")
            if not isinstance(body, dict):
                return self._json({"error": "bad request"}, 400)
            if self.path == "/api/plan":
                jobs, err = parse_plan(body)
                if err:
                    return self._json({"error": err}, 400)
                self._json({"trials": len(jobs), "estimate": run_eval.estimate_cost(jobs)})
            elif self.path == "/api/run":
                code, obj = start_run(state, body)
                self._json(obj, code)
            else:
                self._json({"error": "not found"}, 404)
        except ValueError:
            self._json({"error": "bad request"}, 400)
        except Exception as e:  # noqa: BLE001 - never echo request content, which may hold keys
            self._json({"error": type(e).__name__}, 500)


class Server(ThreadingHTTPServer):
    """Threaded server with a deep accept queue, so a page that loads many images at once is never refused."""

    request_queue_size = 128


def make_server(port: int = 8000, live_root: Path = LIVE_ROOT) -> Server:
    """A server bound to 127.0.0.1 only; port 0 picks a free one."""
    server = Server(("127.0.0.1", port), Handler)
    server.state = State(live_root)
    return server


def main() -> None:
    """Serve the dashboard on 127.0.0.1."""
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port", type=int, default=8000, help="port to listen on (127.0.0.1 only)")
    a = ap.parse_args()
    server = make_server(a.port)
    print(f"dashboard at http://127.0.0.1:{a.port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
