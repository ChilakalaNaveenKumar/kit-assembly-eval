"""Marks drawn over assemblies (landed vs expected rings, arrows, highlights) and the data behind the replay animation."""
import math
from collections.abc import Callable
from functools import lru_cache

import numpy as np
from svgelements import Path as SvgPath

from .annotate import check_spec, failed_points
from .geometry import apply, rotation_deg
from .grader import extract_svg, placements
from .kit import PART_STYLE, criteria, kit_svg, load_kit, load_task, reference_matrices, reference_svg
from .render import assembly_svg
from .templates import part_ids

RED, GREEN = "#d03b3b", "#0ca30c"
ASPECT = 3 / 2  # close-ups share one shape so card grids stay even
MIN_VIEW = 110.0
FIT_ASPECT = 3 / 2  # trial slider, replay and hero share one shape so their frames line up
SHEET_WIDTH = 1000.0
PAPER = "#F8F7F2"
ANGLE_KINDS = ("orient", "upright", "angle")
LIMIT = 1e6  # placements beyond this are hostile output, not geometry


@lru_cache(maxsize=None)
def part_boxes(name: str) -> dict[str, tuple[float, float, float, float]]:
    """Each part's bounding box in its own kit-local frame: (x0, y0, x1, y1)."""
    out = {}
    for part, spec in load_kit(name).items():
        boxes = [SvgPath(d).bbox() for d, _ in spec["paths"]]
        out[part] = (min(b[0] for b in boxes), min(b[1] for b in boxes), max(b[2] for b in boxes), max(b[3] for b in boxes))
    return out


def sanitised_placements(name: str, reply: str, condition: str) -> dict[str, np.ndarray]:
    """part -> the first finite 3x3 placement the reply gives it; anything unparseable yields none."""
    svg = extract_svg(reply)
    if svg is None:
        return {}
    try:
        raw = placements(svg)
    except Exception:  # noqa: BLE001 - untrusted model output
        return {}
    to_part = {v: k for k, v in part_ids(name, condition).items()}
    out = {}
    for pid, ms in raw.items():
        m = ms[0]
        if pid in to_part and np.all(np.isfinite(m)) and np.abs(m).max() < LIMIT:
            out[to_part[pid]] = m
    return out


def flat(m: np.ndarray) -> list[float]:
    """3x3 matrix as the six numbers of an SVG matrix()."""
    return [round(float(v), 6) for v in (m[0, 0], m[1, 0], m[0, 1], m[1, 1], m[0, 2], m[1, 2])]


Rect = tuple[float, float, float, float]


def aligned_reference(name: str, placed: dict[str, np.ndarray]) -> dict[str, np.ndarray]:
    """The correct assembly moved by model_base @ inv(ref_base), so it sits where the model put its base part."""
    ref = reference_matrices(load_kit(name))
    base = load_task(name).UPRIGHT[0]
    if base not in placed:
        return ref
    shift = placed[base] @ np.linalg.inv(ref[base])
    return {p: shift @ m for p, m in ref.items()}


def _corners(name: str, part: str, m: np.ndarray) -> list[list[float]]:
    x0, y0, x1, y1 = part_boxes(name)[part]
    return [[float(v) for v in (m @ np.array([x, y, 1.0]))[:2]] for x, y in ((x0, y0), (x1, y0), (x1, y1), (x0, y1))]


def _grow(x0: float, y0: float, x1: float, y1: float, aspect: float) -> Rect:
    """The smallest window of this aspect ratio that holds the rectangle, centred on it."""
    w, h = max(x1 - x0, 1.0), max(y1 - y0, 1.0)
    vw = max(w, h * aspect)
    vh = vw / aspect
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    return cx - vw / 2, cy - vh / 2, vw, vh


def fit_view(name: str, placed: dict[str, np.ndarray], aligned: dict[str, np.ndarray], extra: list[list[float]] | None = None) -> Rect:
    """One window around the model's parts, the aligned correct parts and any extra points, padded, in the shared shape."""
    w, h = load_task(name).CANVAS
    pts = [c for src in (placed, aligned) for p, m in src.items() for c in _corners(name, p, m)] + list(extra or [])
    xs = [min(max(p[0], -w), 2 * w) for p in pts]  # hostile placements must not blow the window up
    ys = [min(max(p[1], -h), 2 * h) for p in pts]
    pad = 0.04 * max(max(xs) - min(xs), max(ys) - min(ys)) + 12
    return _grow(min(xs) - pad, min(ys) - pad, max(xs) + pad, max(ys) + pad, FIT_ASPECT)


def _view(points: list[list[float]], aspect: float = ASPECT) -> Rect:
    """A window around the points with room for context; small errors get a tight window so the rings separate."""
    xs, ys = [p[0] for p in points], [p[1] for p in points]
    bw, bh = max(xs) - min(xs), max(ys) - min(ys)
    pad = 0.35 * max(bw, bh) + 30
    vw = max(MIN_VIEW, bw + 2 * pad, (bh + 2 * pad) * aspect)
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    return cx - vw / 2, cy - vw / aspect / 2, vw, vw / aspect


def _ring(p: list[float], r: float, sw: float, colour: str) -> str:
    return f'<circle cx="{p[0]:.2f}" cy="{p[1]:.2f}" r="{r:.2f}" fill="none" stroke="{colour}" stroke-width="{sw:.2f}"/>'


def _arrow(a: list[float], b: list[float], sw: float, head: float) -> str:
    d = math.hypot(b[0] - a[0], b[1] - a[1])
    if d < 1e-6:
        return ""
    ux, uy = (b[0] - a[0]) / d, (b[1] - a[1]) / d
    tip = (b[0] - ux * head * 0.2, b[1] - uy * head * 0.2)
    base = (tip[0] - ux * head, tip[1] - uy * head)
    left, right = (base[0] - uy * head * 0.45, base[1] + ux * head * 0.45), (base[0] + uy * head * 0.45, base[1] - ux * head * 0.45)
    return (f'<line x1="{a[0]:.2f}" y1="{a[1]:.2f}" x2="{base[0]:.2f}" y2="{base[1]:.2f}" stroke="{RED}" stroke-width="{sw:.2f}" stroke-linecap="round"/>'
            f'<polygon points="{tip[0]:.2f},{tip[1]:.2f} {left[0]:.2f},{left[1]:.2f} {right[0]:.2f},{right[1]:.2f}" fill="{RED}"/>')


def _sizes(vw: float, gap: float | None = None) -> tuple[float, float, float, float]:
    """Ring radius, stroke, arrow head and label size for a window; rings shrink so a small error still shows two rings."""
    r = max(vw / 40, 1.2)
    if gap is not None and gap > 0:
        r = max(min(r, gap / 2.6), vw / 90)
    return r, max(vw / 280, 0.5), max(vw / 28, 2.0), max(vw / 21, 3.0)


def _label_rect(centre: list[float], text: str, fs: float) -> Rect:
    w = len(text) * fs * 0.6 + fs * 0.9
    return centre[0] - w / 2, centre[1] - fs * 0.75, w, fs * 1.5


def _label_at(a: list[float], b: list[float], text: str, vw: float, gap: float | None) -> list[float]:
    """Where a label sits: beside the arrow's middle, clear of both rings, on the upper side."""
    r, _, _, fs = _sizes(vw, gap)
    d = math.hypot(b[0] - a[0], b[1] - a[1])
    nx, ny = (0.0, -1.0) if d < 1e-6 else (-(b[1] - a[1]) / d, (b[0] - a[0]) / d)
    if ny > 0 or (abs(ny) < 1e-9 and nx > 0):
        nx, ny = -nx, -ny
    half_w = len(text) * fs * 0.3 + fs * 0.45
    off = r * 1.2 + max(fs * 0.9, abs(nx) * half_w + abs(ny) * fs * 0.75) + fs * 0.2
    return [(a[0] + b[0]) / 2 + nx * off, (a[1] + b[1]) / 2 + ny * off]


def _label(centre: list[float], text: str, fs: float, sw: float) -> str:
    x, y, w, h = _label_rect(centre, text, fs)
    return (f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{fs * 0.35:.2f}" fill="#ffffff" stroke="{RED}" stroke-width="{sw * 0.7:.2f}"/>'
            f'<text x="{centre[0]:.2f}" y="{centre[1] + fs * 0.36:.2f}" font-size="{fs:.2f}" font-family="Helvetica,Arial,sans-serif" font-weight="700" '
            f'text-anchor="middle" fill="#a82424">{text}</text>')


def _error_text(err: float | None, kind: str) -> str:
    if err is None or not math.isfinite(err):
        return "n/a"
    return f"{err:.1f}°" if kind in ANGLE_KINDS else f"{err:.1f} pixels off"


def _gap(point: dict) -> float | None:
    return None if point["landed"] is None else _dist(point)


def _point_extent(point: dict, vw: float | None = None) -> list[list[float]]:
    """The points a close-up must show: both positions and the label beside them, sized for a window of width vw."""
    pts = [point["expected"]] + ([point["landed"]] if point["landed"] is not None else [])
    if point["landed"] is not None:
        text = _error_text(point["err"], point["kind"])
        vw = vw or _view(pts)[2]
        c = _label_at(point["landed"], point["expected"], text, vw, _gap(point))
        x, y, w, h = _label_rect(c, text, _sizes(vw, _gap(point))[3])
        pts += [[x, y], [x + w, y + h]]
    return pts


def _marks(point: dict | None, view: Rect, both: bool = True) -> str:
    """Rings, arrow and error label for one failed point, sized relative to the window."""
    if point is None:
        return ""
    r, sw, head, fs = _sizes(view[2], _gap(point) if both else None)
    out = ""
    if both and point["landed"] is not None and _dist(point) > 1.5 * r:
        out += _arrow(point["landed"], point["expected"], sw, head)
    out += _ring(point["expected"], r, sw * 1.2, GREEN)
    if both and point["landed"] is not None:
        out += _ring(point["landed"], r, sw * 1.2, RED)
        text = _error_text(point["err"], point["kind"])
        out += _label(_label_at(point["landed"], point["expected"], text, view[2], _gap(point)), text, fs, sw)
    elif both:
        out += _label([point["expected"][0], point["expected"][1] - r * 2.2 - fs], "part missing", fs, sw)
    return out


def _dist(point: dict) -> float:
    return math.hypot(point["landed"][0] - point["expected"][0], point["landed"][1] - point["expected"][1])


def _outline(name: str, part: str, m: np.ndarray, colour: str, sw: float, dashed: bool = False) -> str:
    """A part's drawn outline under a placement, in one colour with no fill."""
    dash = f' stroke-dasharray="{sw * 3:.1f} {sw * 2:.1f}"' if dashed else ""
    paths = "".join(f'<path d="{d}"/>' for d, _ in load_kit(name)[part]["paths"])
    return (f'<g transform="matrix({m[0, 0]:.6f},{m[1, 0]:.6f},{m[0, 1]:.6f},{m[1, 1]:.6f},{m[0, 2]:.4f},{m[1, 2]:.4f})" fill="none" '
            f'stroke="{colour}" stroke-width="{sw:.2f}" stroke-linejoin="round"{dash}>{paths}</g>')


def _orientation(name: str, part: str, kind: str, err: float | None, placed: dict, aligned: dict) -> tuple[list[list[float]], Callable[[Rect], str]] | None:
    """The part's outline as placed (red), turned to the correct angle in place (green), and a function drawing them with the angle error."""
    if part not in placed or part not in part_boxes(name):
        return None
    m = placed[part]
    want = reference_matrices(load_kit(name))[part] if kind == "upright" else aligned[part]
    x0, y0, x1, y1 = part_boxes(name)[part]
    c_local = np.array([(x0 + x1) / 2, (y0 + y1) / 2, 1.0])
    c = (m @ c_local)[:2]
    g = want.copy()
    g[:2, 2] = c - want[:2, :2] @ c_local[:2]
    red, green = _corners(name, part, m), _corners(name, part, g)
    pts = red + green
    a0, a1 = math.radians(rotation_deg(m)), math.radians(rotation_deg(g))

    def draw(view: Rect) -> str:
        _, sw, _, fs = _sizes(view[2])
        rad = 1.1 * max(math.hypot(p[0] - c[0], p[1] - c[1]) for p in red)
        d = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
        p0 = (c[0] + rad * math.cos(a0), c[1] + rad * math.sin(a0))
        p1 = (c[0] + rad * math.cos(a0 + d), c[1] + rad * math.sin(a0 + d))
        arc = (f'<path d="M{p0[0]:.2f} {p0[1]:.2f} A{rad:.2f} {rad:.2f} 0 0 {1 if d > 0 else 0} {p1[0]:.2f} {p1[1]:.2f}" fill="none" '
               f'stroke="{RED}" stroke-width="{sw * 2.4:.2f}" stroke-linecap="round"/>')
        text = _error_text(err, kind)
        spot = [c[0], c[1] - rad - fs * 1.3]
        return (_outline(name, part, g, GREEN, sw * 1.8) + _outline(name, part, m, RED, sw * 1.8, dashed=True) + arc + _label(spot, text, fs, sw))

    rad0 = 1.1 * max(math.hypot(p[0] - c[0], p[1] - c[1]) for p in red)
    span = max(_bounds(pts)[2] - _bounds(pts)[0], _bounds(pts)[3] - _bounds(pts)[1])
    return pts + [[float(c[0]), float(c[1] - rad0 - 0.2 * span)]], draw


def _set_view(svg: str, name: str, view: Rect | None, paper: bool = True) -> str:
    """Point the drawing's window at the view and extend the paper behind it (or drop the paper for a transparent drawing)."""
    w, h = load_task(name).CANVAS
    old, rect = f'viewBox="0 0 {w} {h}" width="{w}" height="{h}"', f'<rect width="{w}" height="{h}" fill="{PAPER}"/>'
    if view is not None and old in svg:
        svg = svg.replace(old, f'viewBox="{view[0]:.2f} {view[1]:.2f} {view[2]:.2f} {view[3]:.2f}" width="{view[2]:.0f}" height="{view[3]:.0f}"', 1)
        rect_new = f'<rect x="{view[0]:.2f}" y="{view[1]:.2f}" width="{view[2]:.2f}" height="{view[3]:.2f}" fill="{PAPER}"/>'
        svg = svg.replace(rect, rect_new if paper else "", 1)
    elif not paper:
        svg = svg.replace(rect, "", 1)
    return svg


def trial_view(name: str, reply: str, condition: str) -> tuple[dict, dict, Rect]:
    """The model's placements, the correct assembly aligned to them, and the window both are drawn in."""
    placed = sanitised_placements(name, reply, condition)
    aligned = aligned_reference(name, placed)
    return placed, aligned, fit_view(name, placed, aligned)


def fitted_trial_svg(name: str, reply: str, condition: str, title: str = "", paper: bool = True) -> str | None:
    """The model's assembly in the shared window, so it lines up with the aligned correct assembly."""
    svg = assembly_svg(name, reply, condition, title)
    return None if svg is None else _set_view(svg, name, trial_view(name, reply, condition)[2], paper)


def aligned_reference_svg(name: str, reply: str, condition: str, title: str = "", paper: bool = True) -> str | None:
    """The correct assembly placed on the model's base part, in the same window as the model's drawing."""
    placed, aligned, view = trial_view(name, reply, condition)
    svg = assembly_svg(name, reference_svg(name, ids=part_ids(name, condition), modify=lambda p, m: aligned[p]), condition, title)
    return None if svg is None else _set_view(svg, name, view, paper)


def hero_marks(name: str, reply: str, condition: str, grade: dict, index: int | None) -> dict | None:
    """The shared window plus where one failed point landed and belongs, with ring sizes, for an overlay drawn by the page."""
    placed, aligned, view = trial_view(name, reply, condition)
    point = next((p for p in failed_points(name, reply, condition, grade) if p["index"] == index), None)
    out = {"view": [round(v, 2) for v in view], "point": None}
    if point is not None and point["landed"] is not None:
        gap = _dist(point)
        r = max(min(view[2] / 24, gap / 2.6), view[2] / 90)
        out["point"] = {"landed": [round(v, 2) for v in point["landed"]], "expected": [round(v, 2) for v in point["expected"]],
                        "err": point["err"], "kind": point["kind"], "radius": round(r, 2), "stroke": round(view[2] / 230, 2)}
    return out


def _spec_for(name: str, condition: str, checks: list[dict], i: int) -> dict | None:
    """The grader's spec for stored check i (see check_spec)."""
    return check_spec(load_task(name), condition, checks, i)


def _check_target(name: str, condition: str, grade: dict, index: int | None) -> tuple[int | None, dict | None]:
    """The failed check a close-up is about: the one asked for, else the first failed one."""
    checks = grade.get("checks", [])
    if index is None:
        index = next((i for i, c in enumerate(checks) if not c["ok"]), None)
    if index is None or not 0 <= index < len(checks) or checks[index]["ok"]:
        return None, None
    return index, _spec_for(name, condition, checks, index)


def annotated_svg(name: str, reply: str, condition: str, grade: dict, index: int | None = None, zoom: bool = True,
                  reference: bool = False, every: bool = False, fit: bool = False) -> str | None:
    """The assembly (model's, or the correct one) with failure marks, cropped around one failed check; None when there is nothing to draw."""
    placed, aligned, whole = trial_view(name, reply, condition)
    pts = failed_points(name, reply, condition, grade)
    if reference:
        base = assembly_svg(name, reference_svg(name, ids=part_ids(name, condition), modify=lambda p, m: aligned[p]), condition)
    else:
        base = assembly_svg(name, reply, condition)
    if base is None:
        return None
    canvas = load_task(name).CANVAS
    if not fit:
        whole = (0.0, 0.0, float(canvas[0]), float(canvas[1]))
    if every and index is None and pts:
        extent = [q for p in pts for q in _point_extent(p, whole[2])]
        x0, y0, x1, y1 = _bounds(extent + [[whole[0], whole[1]], [whole[0] + whole[2], whole[1] + whole[3]]])
        pad = 0.03 * (x1 - x0)
        view = _grow(x0 - pad, y0 - pad, x1 + pad, y1 + pad, FIT_ASPECT) if fit else whole
        marks = "".join(_marks({**p, "expected": _aligned_expected(name, condition, p, aligned) if reference else p["expected"]}, view, both=not reference) for p in pts)
        return _set_view(base, name, view)[:-6] + marks + "</svg>"
    idx, spec = _check_target(name, condition, grade, index)
    point = next((p for p in pts if p["index"] == idx), None)
    if point is None:
        found = _orientation(name, (spec or {}).get("part") or (spec or {}).get("a"), (spec or {}).get("kind", ""), (grade["checks"][idx]["err"] if idx is not None else None), placed, aligned) if spec else None
        if found is None:
            return _set_view(base, name, whole if fit else None)
        extent, draw = found
        view = _view(extent) if zoom else whole
        return _set_view(base, name, view)[:-6] + ("" if reference else draw(view)) + "</svg>"
    view = _view(_point_extent(point)) if zoom else whole
    if reference:
        point = {**point, "landed": None, "expected": _aligned_expected(name, condition, point, aligned)}
    return _set_view(base, name, view if (zoom or fit) else None)[:-6] + _marks(point, view, both=not reference) + "</svg>"


def has_closeup(name: str, reply: str, condition: str, grade: dict, index: int | None = None) -> bool:
    """True when the close-up for this failed check carries rings or an orientation outline, not just the bare drawing."""
    idx, spec = _check_target(name, condition, grade, index)
    if idx is None:
        return False
    if any(p["index"] == idx for p in failed_points(name, reply, condition, grade)):
        return True
    placed, aligned, _ = trial_view(name, reply, condition)
    part = (spec or {}).get("part") or (spec or {}).get("a")
    return bool(spec) and _orientation(name, part, spec["kind"], grade["checks"][idx]["err"], placed, aligned) is not None


def _bounds(points: list[list[float]]) -> Rect:
    xs, ys = [p[0] for p in points], [p[1] for p in points]
    return min(xs), min(ys), max(xs), max(ys)


def _aligned_expected(name: str, condition: str, point: dict, aligned: dict[str, np.ndarray]) -> list[float]:
    """Where the failed check's moving feature sits in the aligned correct assembly."""
    part, feat = point["feature"]
    if part not in aligned:
        return point["expected"]
    p = apply(aligned[part], load_kit(name)[part]["anchors"][feat])
    return [float(p[0]), float(p[1])]


def kit_sheet_svg(name: str, condition: str) -> str:
    """The loose parts as the model receives them, captioned with their ids (B) or names, without attach points."""
    boxes, ids = part_boxes(name), part_ids(name, condition)
    fs = 34.0
    caption = {p: ids[p] if condition == "B" else ids[p].replace("_", " ").capitalize() for p in boxes}
    for step in range(30):
        s, x, y, row_h, cells = 1.0 - step * 0.03, 10.0, 10.0, 0.0, []
        for part, (x0, y0, x1, y1) in boxes.items():
            w, h = (x1 - x0) * s, (y1 - y0) * s
            cell_w = max(w, len(caption[part]) * fs * 0.56) + 22
            if x + cell_w > SHEET_WIDTH - 10 and x > 10:
                x, y, row_h = 10.0, y + row_h + 22, 0.0
            cells.append((part, x + (cell_w - w) / 2 - x0 * s, y - y0 * s, s, x + cell_w / 2, y + h + fs + 4))
            x, row_h = x + cell_w, max(row_h, h + fs + 14)
        total = y + row_h + 10
        if total <= SHEET_WIDTH / FIT_ASPECT:
            break
    kit = kit_svg(load_kit(name), ids)
    body = "".join(f'<g transform="translate({tx:.2f},{ty:.2f}) scale({sc:.4f})"><use href="#kit-{ids[p]}"/></g>'
                   f'<text x="{cx:.2f}" y="{cy:.2f}" font-size="{fs}" font-family="Helvetica,Arial,sans-serif" text-anchor="middle" fill="#1F2A3A">{caption[p]}</text>'
                   for p, tx, ty, sc, cx, cy in cells)
    h = max(total, SHEET_WIDTH / FIT_ASPECT)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SHEET_WIDTH:.0f} {h:.0f}" width="{SHEET_WIDTH:.0f}" height="{h:.0f}">'
            f'<rect width="{SHEET_WIDTH:.0f}" height="{h:.0f}" fill="{PAPER}"/>{kit[kit.index("<defs>"):kit.index("</defs>") + 7]}{body}</svg>')


def kit_parts_svg(name: str, condition: str) -> str:
    """The loose parts packed in one window with no captions, attach points or background, cropped to what is drawn."""
    ids, boxes = part_ids(name, condition), part_boxes(name)
    offsets, scale = _layout(name, (SHEET_WIDTH, SHEET_WIDTH / FIT_ASPECT))
    cells = []
    for part, (x0, y0, x1, y1) in boxes.items():
        ox, oy = offsets[part]
        cells.append((part, ox, oy, [ox + x0 * scale, oy + y0 * scale, ox + x1 * scale, oy + y1 * scale]))
    left, top = min(c[3][0] for c in cells), min(c[3][1] for c in cells)
    right, bottom = max(c[3][2] for c in cells), max(c[3][3] for c in cells)
    pad = 12.0
    x, y, w, h = _grow(left - pad, top - pad, right + pad, bottom + pad, FIT_ASPECT)
    kit = kit_svg(load_kit(name), ids)
    body = "".join(f'<g transform="translate({ox:.2f},{oy:.2f}) scale({scale:.4f})"><use href="#kit-{ids[p]}"/></g>' for p, ox, oy, _ in cells)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x:.2f} {y:.2f} {w:.2f} {h:.2f}" width="{w:.0f}" height="{h:.0f}">'
            f'{kit[kit.index("<defs>"):kit.index("</defs>") + 7]}{body}</svg>')


def _layout(name: str, size: tuple[float, float]) -> tuple[dict[str, tuple[float, float]], float]:
    """Shelf-pack the parts as the kit sheet stores them, shrunk until they fit the window; returns offsets and the scale."""
    boxes = part_boxes(name)
    for step in range(20):
        s, gap, x, y, row_h, out = 1.0 - step * 0.05, 24.0, 12.0, 12.0, 0.0, {}
        for part, (x0, y0, x1, y1) in boxes.items():
            w, h = (x1 - x0) * s, (y1 - y0) * s
            if x + w > size[0] - 12 and x > 12:
                x, y, row_h = 12.0, y + row_h + gap, 0.0
            out[part] = (x - x0 * s, y - y0 * s)
            x, row_h = x + w + gap, max(row_h, h)
        if y + row_h + 12 <= size[1]:
            break
    return out, s


def replay_payload(name: str, reply: str, condition: str, grade: dict) -> dict:
    """Per part: kit-sheet start matrix, the model's end matrix (or None), the correct matrix aligned to the model; plus the failed points."""
    task, kit = load_task(name), load_kit(name)
    ids, placed = part_ids(name, condition), sanitised_placements(name, reply, condition)
    aligned = aligned_reference(name, placed)
    view = fit_view(name, placed, aligned)
    offsets, scale = _layout(name, (view[2], view[3]))
    boxes = part_boxes(name)
    failed_parts = []
    for i, g in enumerate(grade.get("checks", [])):
        spec = _spec_for(name, condition, grade["checks"], i)
        part = None if spec is None or g["ok"] else spec.get("part") or spec.get("a")
        if part is not None and part not in failed_parts:
            failed_parts.append(part)
    parts = [{"part": p, "id": ids[p], "paths": [{"d": d, "style": s} for d, s in kit[p]["paths"]],
              "box": list(boxes[p]), "start": [round(scale, 4), 0.0, 0.0, round(scale, 4), round(offsets[p][0] + view[0], 3), round(offsets[p][1] + view[1], 3)],
              "end": flat(placed[p]) if p in placed else None, "ref": flat(aligned[p])} for p in task.PARTS]
    return {"kit": name, "canvas": list(task.CANVAS), "view": [round(v, 3) for v in view], "part_style": PART_STYLE, "parts": parts,
            "failed_parts": failed_parts, "failed_points": failed_points(name, reply, condition, grade)}
