"""Grade a model's assembly by where each part actually lands. Model output is untrusted input."""
import itertools
import math
import re
import xml.etree.ElementTree as ET
from types import ModuleType

import numpy as np

from .geometry import angle_diff, apply, parse_transform, rotation_deg, translate
from .kit import criteria, load_kit, load_task, reference_matrices
from .templates import part_ids

NOT_RENDERED = {"defs", "symbol", "clipPath", "mask", "pattern", "marker", "metadata", "title", "desc"}
_SVG_BLOCK = re.compile(r"<svg\b[\s\S]*?</svg>")


def extract_svg(text: str) -> str | None:
    """The last <svg>...</svg> block in the reply that parses as XML, if any."""
    blocks = _SVG_BLOCK.findall(text or "")
    for block in reversed(blocks):
        try:
            ET.fromstring(_clean(block))
            return block
        except ET.ParseError:
            continue
    return blocks[-1] if blocks else None


def _clean(svg: str) -> str:
    return re.sub(r'\sxmlns(:\w+)?="[^"]*"', "", svg).replace("xlink:href", "href")


def _length(v: str | None) -> float:
    if not v:
        return 0.0
    m = re.fullmatch(r"\s*([-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?)\s*(px)?\s*", v)
    if not m:
        raise ValueError(f"bad length {v!r}")
    return float(m.group(1))


def placements(svg: str) -> dict[str, list[np.ndarray]]:
    """Map each referenced kit id to the matrices of every rendered <use> that places it."""
    root = ET.fromstring(_clean(svg))
    found: dict[str, list[np.ndarray]] = {}
    stack = [(root, np.eye(3))]
    # iterative walk so hostile, deeply nested output cannot exhaust the recursion limit
    while stack:
        e, parent = stack.pop()
        tag = e.tag.split("}")[-1]
        if tag in NOT_RENDERED or e.get("display") == "none" or e.get("visibility") == "hidden":
            continue
        m = parent @ parse_transform(e.get("transform"))
        if tag == "use":
            ref = (e.get("href") or "").lstrip("#")
            ref = ref[4:] if ref.startswith("kit-") else ref
            found.setdefault(ref, []).append(m @ translate(_length(e.get("x")), _length(e.get("y"))))
        stack.extend((child, m) for child in e)
    return found


def _fail(reason: str) -> dict:
    return {"pass": False, "score": 0.0, "checks": [], "issues": [reason]}


def _distance_to_line(p: np.ndarray, q: np.ndarray, d: np.ndarray) -> float:
    n = float(np.linalg.norm(d))
    if n < 1e-9:
        return float("inf")
    return abs(float(d[0] * (p - q)[1] - d[1] * (p - q)[0])) / n


def evaluate(task: ModuleType, kit: dict, ids: dict[str, str], condition: str, text: str) -> dict:
    """Pure grading; parts declared INTERCHANGEABLE are graded under whichever assignment scores best."""
    groups = [g for g in getattr(task, "INTERCHANGEABLE", []) if len(g) > 1]
    best = None
    for perm in _assignments(groups):
        result = _evaluate(task, kit, ids, condition, text, perm)
        if best is None or (result["pass"], result["score"]) > (best["pass"], best["score"]):
            best = result
    return best


def _assignments(groups: list[tuple]) -> list[dict[str, str]]:
    out = [{}]
    for g in groups:
        out = [{**a, **dict(zip(g, p))} for a in out for p in itertools.permutations(g)]
    return out


def _evaluate(task: ModuleType, kit: dict, ids: dict[str, str], condition: str, text: str, role: dict[str, str]) -> dict:
    """Grade with role[part] = the actual part placed in that part's role (identity when absent)."""
    ref = reference_matrices(kit)
    to_part = {v: k for k, v in ids.items()}
    svg = extract_svg(text)
    if svg is None:
        return _fail("no <svg> in reply")
    try:
        raw = placements(svg)
    except (ET.ParseError, ValueError, IndexError, OverflowError) as e:
        return _fail(f"unparseable svg: {type(e).__name__}")

    issues, placed = [], {}
    for pid, ms in raw.items():
        part = to_part.get(pid)
        if part is None:
            issues.append(f"unknown part id {pid}")
            continue
        if len(ms) > 1:
            issues.append(f"{pid} used {len(ms)} times")
        m = ms[0]
        lin = m[:2, :2]
        with np.errstate(all="ignore"):
            if not np.all(np.isfinite(m)) or not np.isfinite(np.linalg.det(lin)):
                issues.append(f"{pid} has a non-finite transform")
                continue
            if np.linalg.det(lin) < 0:
                issues.append(f"{pid} mirrored")
                continue
            if np.abs(lin.T @ lin - np.eye(2)).max() > 0.02:
                issues.append(f"{pid} scaled or skewed")
                continue
        placed[part] = m
    by_actual, placed = placed, {}
    for r in set(by_actual) | set(role):
        if role.get(r, r) in by_actual:
            placed[r] = by_actual[role.get(r, r)]
    for part, pid in ids.items():
        if pid not in raw:
            issues.append(f"{pid} missing")

    def anchor(part: str, feature: str) -> np.ndarray:
        actual = role.get(part, part)
        return apply(placed[part], kit[actual]["anchors"][feature])

    base = task.UPRIGHT[0]
    checks = []
    for c in criteria(task, condition):
        r = {"kind": c["kind"], "text": c["text"], "tol": c["tol"]}
        needed = [c[k] for k in ("a", "b", "part") if k in c]
        if c["kind"] in ("angle", "orient"):
            needed.append(base)
        if any(p not in placed for p in needed):
            r.update(ok=False, err=None, why="part missing or invalid")
            checks.append(r)
            continue
        if c["kind"] == "joint":
            e = float(np.linalg.norm(anchor(c["a"], c["an"]) - anchor(c["b"], c["bn"])))
        elif c["kind"] == "anyhole":
            e = min(float(np.linalg.norm(anchor(c["a"], c["an"]) - anchor(c["b"], h))) for h in c["bns"])
        elif c["kind"] == "level":
            e = abs(float(anchor(c["a"], c["an"])[1] - anchor(c["b"], c["bn"])[1]))
        elif c["kind"] == "upright":
            e = angle_diff(rotation_deg(placed[c["part"]]), rotation_deg(ref[c["part"]]))
        elif c["kind"] in ("angle", "orient"):
            want = rotation_deg(ref[c["part"]]) - rotation_deg(ref[base])
            got = rotation_deg(placed[c["part"]]) - rotation_deg(placed[base])
            e = angle_diff(got, want)
        elif c["kind"] == "online":
            p, q1, q2 = anchor(c["a"], c["an"]), anchor(c["b"], c["b1"]), anchor(c["b"], c["b2"])
            d = q2 - q1
            dd = float(np.dot(d, d))
            t = float(np.dot(p - q1, d) / dd) if dd > 1e-12 else 0.0
            e = _distance_to_line(p, q1, d)
            if not 0.0 <= t <= 1.0:
                e = max(e, float(np.linalg.norm(p - (q1 if t < 0 else q2))))
        elif c["kind"] == "radial":
            p, o = anchor(c["a"], c["an"]), anchor(c["b"], c["bn"])
            d = (anchor(c["a"], c["a1"]) + anchor(c["a"], c["a2"])) / 2 - o
            e = _distance_to_line(p, o, d)
            if float(np.dot(p - o, d)) < 0:
                e = max(e, float(np.linalg.norm(p - o)))
        else:
            raise ValueError(c["kind"])
        e = e if math.isfinite(e) else float("inf")
        r.update(ok=e <= c["tol"], err=round(e, 2) if math.isfinite(e) else None)
        checks.append(r)

    n_ok = sum(1 for r in checks if r["ok"])
    return {"pass": n_ok == len(checks) and not issues, "score": round(n_ok / len(checks), 4), "checks": checks, "issues": issues}


def grade(name: str, text: str, condition: str) -> dict:
    """Load the kit and grade one model reply: {pass, score, checks, issues}."""
    return evaluate(load_task(name), load_kit(name), part_ids(name, condition), condition, text)
