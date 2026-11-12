"""Where a failed connection went wrong: the landed and the expected position of each failed check, for drawing error close-ups."""
from .geometry import apply
from .grader import _assignments, _evaluate, extract_svg, placements
from .kit import criteria, load_kit, load_task, reference_matrices
from .templates import part_ids


def check_spec(task, condition: str, checks: list[dict], i: int) -> dict | None:
    """The task's spec for stored check i: by position (the grader emits checks in task order), else by text.

    Positional matching survives wording edits to a task after results were stored; the kind must agree.
    """
    specs = criteria(task, condition)
    if len(specs) == len(checks) and specs[i]["kind"] == checks[i]["kind"]:
        return specs[i]
    return {c["text"].lower(): c for c in specs}.get(checks[i]["text"].lower())


def best_role(name: str, condition: str, reply: str) -> dict[str, str]:
    """The interchangeable-part assignment the grader scored best, so close-ups mark the check that actually failed."""
    task, kit, ids = load_task(name), load_kit(name), part_ids(name, condition)
    groups = [g for g in getattr(task, "INTERCHANGEABLE", []) if len(g) > 1]
    best, role = None, {}
    for perm in _assignments(groups):
        r = _evaluate(task, kit, ids, condition, reply, perm)
        if best is None or (r["pass"], r["score"]) > (best["pass"], best["score"]):
            best, role = r, perm
    return role


def failed_points(name: str, reply: str, condition: str, grade: dict) -> list[dict]:
    """For each failed point check: where the moving part's feature landed and where it should be, in canvas coordinates."""
    task, kit = load_task(name), load_kit(name)
    ref = reference_matrices(kit)
    svg = extract_svg(reply)
    if svg is None:
        return []
    try:
        raw = placements(svg)
    except Exception:  # noqa: BLE001 - untrusted model output; an unparseable reply simply has no close-ups
        return []
    to_part = {v: k for k, v in part_ids(name, condition).items()}
    by_actual = {to_part[pid]: ms[0] for pid, ms in raw.items() if pid in to_part}
    role = best_role(name, condition, reply)
    placed = {r: by_actual[role.get(r, r)] for r in set(by_actual) | set(role) if role.get(r, r) in by_actual}
    checks = grade.get("checks", [])
    out = []
    for i, g in enumerate(checks):
        c = check_spec(task, condition, checks, i)
        if g["ok"] or c is None or c["kind"] not in ("joint", "anyhole", "level", "online", "radial"):
            continue
        part, feat = c["a"], c["an"]
        expected_part, expected_feat = (c["b"], c["bn"]) if "bn" in c else (c["a"], c["an"])
        anchor = kit[part]["anchors"][feat]
        landed = apply(placed[part], kit[role.get(part, part)]["anchors"][feat]) if part in placed else None
        if expected_part in placed and expected_part != part:
            target = apply(placed[expected_part], kit[role.get(expected_part, expected_part)]["anchors"][expected_feat])
        else:
            target = apply(ref[part], anchor)  # where it sits in the correct assembly
        if c["kind"] == "online" and part in placed and c["b"] in placed:
            actual_b = role.get(c["b"], c["b"])
            q1 = apply(placed[c["b"]], kit[actual_b]["anchors"][c["b1"]])
            q2 = apply(placed[c["b"]], kit[actual_b]["anchors"][c["b2"]])
            d = q2 - q1
            t = 0.0 if float(d @ d) < 1e-12 else min(1.0, max(0.0, float((landed - q1) @ d / (d @ d))))
            target = q1 + t * d  # nearest point on the guide line
        if c["kind"] == "level" and landed is not None:
            target = [landed[0], target[1]]  # only height is compared
        out.append({"index": i, "text": g["text"], "kind": c["kind"], "err": g.get("err"), "tol": g["tol"],
                    "part": part, "feature": [part, feat], "landed": None if landed is None else [float(landed[0]), float(landed[1])],
                    "expected": [float(target[0]), float(target[1])]})
    return out
