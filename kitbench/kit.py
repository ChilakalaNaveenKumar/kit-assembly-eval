"""Turn an assembled object (tasks/<kit>/task.py) into a kit of parts, each baked into its own rotated local frame."""
import importlib.util
import io
import json
import math
import random
import xml.etree.ElementTree as ET
from functools import lru_cache
from pathlib import Path
from types import ModuleType

import numpy as np
from svgelements import SVG, Matrix, Path as SvgPath, Shape

from .geometry import mat

ROOT = Path(__file__).resolve().parent.parent
TASKS = ROOT / "tasks"
PART_STYLE = {"fill": "none", "stroke": "#1F2A3A", "stroke-width": "2.3", "stroke-linecap": "round", "stroke-linejoin": "round"}
_STYLE_KEYS = ("fill", "stroke", "stroke-width", "opacity", "stroke-dasharray", "stroke-dashoffset", "stroke-linecap", "stroke-linejoin")


def kit_names() -> list[str]:
    """All kits, sorted."""
    return sorted(p.name for p in TASKS.iterdir() if (p / "task.py").exists())


@lru_cache(maxsize=None)
def load_task(name: str) -> ModuleType:
    """Import tasks/<name>/task.py."""
    spec = importlib.util.spec_from_file_location(f"task_{name}", TASKS / name / "task.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ORIENT_TOL = 8.0
RECIPE_CONDITIONS = {"C"}


def free_rotation(task: ModuleType) -> set[str]:
    """Parts that may sit at any angle: everything that turns in use (FREE_SPIN groups plus FREE_ROTATION)."""
    out = set(getattr(task, "FREE_ROTATION", ()))
    for key in getattr(task, "FREE_SPIN", {}):
        out.update(key if isinstance(key, tuple) else (key,))
    return out


def kit_tolerance(task: ModuleType) -> float:
    """The single position tolerance stated in the no-recipe prompts: the loosest per-joint tolerance of the kit."""
    return max([j[5] for j in task.JOINTS] + [x[-1] for x in getattr(task, "EXTRA", []) if x[0] != "angle"])


def criteria(task: ModuleType, condition: str = "C") -> list[dict]:
    """Every check the grader runs for a task in a condition, in a fixed order."""
    recipe = condition in RECIPE_CONDITIONS
    out = _recipe_criteria(task)
    if not recipe:
        tol = kit_tolerance(task)
        # the upright limit is in degrees and keeps its own value; only distance checks get the kit-wide margin
        out = [c if c["kind"] == "upright" else dict(c, tol=tol) for c in out if c["kind"] != "angle"]
        for c in out:
            if c["kind"] != "upright":
                c["text"] = c["text"].rsplit(" (within", 1)[0] + f" (within {tol} px)"
    base = task.UPRIGHT[0]
    free = free_rotation(task)
    for part in task.PARTS:
        if part != base and part not in free:
            out.append({"kind": "orient", "part": part, "tol": ORIENT_TOL,
                        "text": f"{part.replace('_', ' ').capitalize()} faces the way it does on the working object (within {ORIENT_TOL:g} deg)"})
    return out


def _recipe_criteria(task: ModuleType) -> list[dict]:
    out = []
    part, tol, text = task.UPRIGHT
    out.append({"kind": "upright", "part": part, "tol": tol, "text": text})
    for text, a, an, b, bn, tol in task.JOINTS:
        out.append({"kind": "joint", "a": a, "an": an, "b": b, "bn": bn, "tol": tol, "text": f"{text} (within {tol} px)"})
    for x in getattr(task, "EXTRA", []):
        kind = x[0]
        if kind == "level":
            _, text, a, an, b, bn, tol = x
            out.append({"kind": kind, "a": a, "an": an, "b": b, "bn": bn, "tol": tol, "text": f"{text} (within {tol} px)"})
        elif kind == "angle":
            _, text, p, tol = x
            out.append({"kind": kind, "part": p, "tol": tol, "text": f"{text} (within {tol} deg)"})
        elif kind == "anyhole":
            # a plate with several equivalent holes: any of them makes the joint
            _, text, a, an, b, bns, tol = x
            out.append({"kind": kind, "a": a, "an": an, "b": b, "bn": bns[0], "bns": list(bns), "tol": tol, "text": f"{text} (within {tol} px)"})
        elif kind == "online":
            _, text, a, an, b, b1, b2, tol = x
            out.append({"kind": kind, "a": a, "an": an, "b": b, "b1": b1, "b2": b2, "tol": tol, "text": f"{text} (within {tol} px)"})
        elif kind == "radial":
            _, text, a, an, a1, a2, b, bn, tol = x
            out.append({"kind": kind, "a": a, "an": an, "a1": a1, "a2": a2, "b": b, "bn": bn, "tol": tol, "text": f"{text} (within {tol} px)"})
        else:
            raise ValueError(f"unknown check kind {kind}")
    return out


def _to_paths(elements: list[str]) -> list[tuple[SvgPath, dict]]:
    out = []
    for s in elements:
        e = ET.fromstring(s)
        style = {k: v for k, v in e.attrib.items() if k in _STYLE_KEYS}
        geo = "".join(f' {k}="{v}"' for k, v in e.attrib.items() if k not in style)
        tag = e.tag.split("}")[-1]
        doc = SVG.parse(io.StringIO(f'<svg xmlns="http://www.w3.org/2000/svg"><{tag}{geo}/></svg>'))
        shapes = [x for x in doc.elements() if isinstance(x, Shape)]
        if not shapes:
            raise ValueError(f"unparseable element: {s[:80]}")
        out.append((SvgPath(shapes[0]), style))
    return out


def _sample(path: SvgPath, n: int = 8) -> list[tuple[float, float]]:
    p = SvgPath(path)
    p.reify()
    return [(float(q.x), float(q.y)) for seg in p for q in (seg.point(t / n) for t in range(n + 1))]


def build_kit(name: str) -> dict:
    """Bake every part into a rotated local frame; return {part: {matrix, paths, anchors}} and write build files."""
    task = load_task(name)
    kit = {}
    for part, spec in task.PARTS.items():
        items = _to_paths(spec["els"])
        th = math.radians(task.ROT.get(part, 0.0))
        c, s = math.cos(th), math.sin(th)
        # rotation is baked into the coordinates, so a model cannot simply invert a wrapper transform
        rotated = [q for p, _ in items for q in _sample(SvgPath(p) * Matrix(c, s, -s, c, 0, 0))]
        tx = -min(x for x, _ in rotated) + 5
        ty = -min(y for _, y in rotated) + 5
        m = Matrix(c, s, -s, c, tx, ty)
        paths = []
        for p, style in items:
            q = SvgPath(p) * m
            q.reify()
            paths.append((q.d(), style))
        kit[part] = {
            "matrix": [float(m.a), float(m.b), float(m.c), float(m.d), float(m.e), float(m.f)],
            "paths": paths,
            "anchors": {k: [round(float(v), 4) for v in m.point_in_matrix_space(pt)] for k, pt in spec["anchors"].items()},
        }
    out = TASKS / name / "build"
    out.mkdir(exist_ok=True)
    (out / "kit.json").write_text(json.dumps(kit, indent=1))
    (out / "kit.svg").write_text(kit_svg(kit))
    (out / "reference_solution.svg").write_text(reference_svg(name, kit))
    return kit


def kit_svg(kit: dict, ids: dict[str, str] | None = None, order: list[str] | None = None) -> str:
    """The kit as the model sees it: one <g id="kit-ID"> per part inside <defs>, no anchors."""
    lines = ['<svg xmlns="http://www.w3.org/2000/svg"><defs>']
    for part in order or list(kit):
        v = kit[part]
        pid = (ids or {}).get(part, part)
        lines.append(f'<g id="kit-{pid}" ' + " ".join(f'{a}="{b}"' for a, b in PART_STYLE.items()) + ">")
        lines += ["  <path " + f'd="{d}" ' + " ".join(f'{k}="{v}"' for k, v in style.items()) + "/>" for d, style in v["paths"]]
        lines.append("</g>")
    lines.append("</defs></svg>")
    return "\n".join(lines)


def load_kit(name: str) -> dict:
    """Read the built kit for a task."""
    return json.loads((TASKS / name / "build" / "kit.json").read_text())


def reference_matrices(kit: dict) -> dict[str, np.ndarray]:
    """Where each part belongs: the inverse of its baking matrix."""
    return {k: np.linalg.inv(mat(*v["matrix"])) for k, v in kit.items()}


def m2s(m: np.ndarray) -> str:
    """Matrix as an SVG matrix() string."""
    return f"matrix({m[0,0]:.6f},{m[1,0]:.6f},{m[0,1]:.6f},{m[1,1]:.6f},{m[0,2]:.4f},{m[1,2]:.4f})"


def reference_svg(name: str, kit: dict | None = None, modify=None, ids: dict | None = None) -> str:
    """The correct assembly as <use> elements; modify(part, matrix) can alter or drop (None) a part for tests."""
    task = load_task(name)
    kit = kit or load_kit(name)
    w, h = task.CANVAS
    uses = []
    for part, m in reference_matrices(kit).items():
        if modify:
            m = modify(part, m)
        if m is not None:
            uses.append(f'<use href="#kit-{(ids or {}).get(part, part)}" transform="{m2s(m)}"/>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">' + "".join(uses) + "</svg>"


def anon_ids(name: str) -> dict[str, str]:
    """Deterministic shuffled ids p01..pNN for condition B, seeded by the kit name."""
    parts = sorted(load_task(name).PARTS)
    ids = [f"p{i + 1:02d}" for i in range(len(parts))]
    random.Random(sum(map(ord, name))).shuffle(ids)
    return dict(zip(parts, ids))
