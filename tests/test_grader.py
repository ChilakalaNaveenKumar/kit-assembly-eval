"""Grader tests: right answers pass, every kind of wrong answer fails, malformed output fails cleanly. No network."""
import hashlib
import itertools
import re
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from kitbench.geometry import apply, mat, rotate, translate  # noqa: E402
from kitbench.grader import grade  # noqa: E402
from kitbench.kit import TASKS, build_kit, kit_names, load_kit, load_task, m2s, reference_matrices, reference_svg  # noqa: E402
from kitbench.templates import CONDITIONS, TEMPLATES, fill, part_ids  # noqa: E402

KITS = kit_names()
NO_RECIPE = ["A", "A_alt", "B"]


def svg_from(name: str, cond: str, mats: dict) -> str:
    ids = part_ids(name, cond)
    w, h = load_task(name).CANVAS
    uses = "".join(f'<use href="#kit-{ids[p]}" transform="{m2s(m)}"/>' for p, m in mats.items())
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">{uses}</svg>'


def first_anchor(name: str, part: str) -> tuple:
    kit = load_kit(name)
    a = next(iter(kit[part]["anchors"].values()))
    return tuple(apply(reference_matrices(kit)[part], a))


def spin_groups(name: str) -> list[tuple]:
    out = []
    for k, centre in getattr(load_task(name), "FREE_SPIN", {}).items():
        out.append((k if isinstance(k, tuple) else (k,), centre))
    return out


@pytest.mark.parametrize("name", KITS)
@pytest.mark.parametrize("cond", list(CONDITIONS))
def test_reference_passes(name, cond):
    assert grade(name, reference_svg(name, ids=part_ids(name, cond)), cond)["pass"]


@pytest.mark.parametrize("name", KITS)
@pytest.mark.parametrize("cond", ["A", "C"])
def test_each_part_shifted_fails(name, cond):
    ref = reference_matrices(load_kit(name))
    tol = max(c[5] for c in load_task(name).JOINTS)
    for part in ref:
        # diagonal, so parts that may slide along an edge or a centre line still leave it
        mats = {**ref, part: translate(2 * tol + 2, 2 * tol + 2) @ ref[part]}
        assert not grade(name, svg_from(name, cond, mats), cond)["pass"], part


@pytest.mark.parametrize("name", KITS)
def test_parts_with_two_attach_points_fail_when_rotated_or_reversed(name):
    kit = load_kit(name)
    ref = reference_matrices(kit)
    spinning = {p for g, _ in spin_groups(name) for p in g}
    for part, v in kit.items():
        if len(v["anchors"]) < 2 or part in spinning:
            continue
        pts = [apply(ref[part], a) for a in v["anchors"].values()]
        mid = tuple((pts[0] + pts[1]) / 2)
        half = max(float(np.linalg.norm(p - np.array(mid))) for p in pts)
        tol = max(c[5] for c in load_task(name).JOINTS)
        small = float(np.degrees(2 * np.arcsin(min(1.0, 3 * tol / (2 * half)))))  # moves the far hole 3x the tolerance
        for deg in (small, 180):  # small rotation, and end-for-end reversal
            mats = {**ref, part: rotate(deg, *mid) @ ref[part]}
            assert not grade(name, svg_from(name, "A", mats), "A")["pass"], (part, deg)


@pytest.mark.parametrize("name", KITS)
def test_mirrored_scaled_missing_duplicated_fail(name):
    ref = reference_matrices(load_kit(name))
    part = sorted(ref)[0]
    c = first_anchor(name, part)
    mirror = translate(*c) @ mat(-1, 0, 0, 1, 0, 0) @ translate(-c[0], -c[1])
    scale = translate(*c) @ mat(1.05, 0, 0, 1.05, 0, 0) @ translate(-c[0], -c[1])
    for mats in ({**ref, part: mirror @ ref[part]}, {**ref, part: scale @ ref[part]}, {k: m for k, m in ref.items() if k != part}):
        assert not grade(name, svg_from(name, "A", mats), "A")["pass"]
    dup = svg_from(name, "A", ref).replace("</svg>", f'<use href="#kit-{part}" transform="{m2s(ref[part])}"/></svg>')
    assert not grade(name, dup, "A")["pass"]


@pytest.mark.parametrize("name", KITS)
def test_swapping_any_two_parts_fails(name):
    ref = reference_matrices(load_kit(name))
    allowed = {frozenset(g) for g in getattr(load_task(name), "INTERCHANGEABLE", [])}
    for a, b in itertools.combinations(sorted(ref), 2):
        if frozenset((a, b)) in allowed:
            continue
        mats = {**ref, a: ref[b], b: ref[a]}
        assert not grade(name, svg_from(name, "A", mats), "A")["pass"], (a, b)


@pytest.mark.parametrize("name", KITS)
@pytest.mark.parametrize("cond", NO_RECIPE + ["C"])
def test_valid_alternatives_pass(name, cond):
    ref = reference_matrices(load_kit(name))
    moved = {k: translate(-23, 17) @ m for k, m in ref.items()}
    assert grade(name, svg_from(name, cond, moved), cond)["pass"]
    for group, centre in spin_groups(name):
        spun = {k: (rotate(37, *centre) @ m if k in group else m) for k, m in ref.items()}
        assert grade(name, svg_from(name, cond, spun), cond)["pass"], group


@pytest.mark.parametrize("name", KITS)
def test_equivalent_transform_encodings_pass(name):
    ref = reference_matrices(load_kit(name))
    ids = part_ids(name, "A")
    uses = []
    for p, m in ref.items():
        ang = np.degrees(np.arctan2(m[1, 0], m[0, 0]))
        uses.append(f'<g transform="translate({m[0, 2] + 7:.6f} {m[1, 2]:.6f})"><use href="#kit-{ids[p]}" '
                    f'transform="translate(-7 0) rotate({ang:.8f})"/></g>')
    svg = '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">' + "".join(uses) + "</svg>"
    assert grade(name, svg, "A")["pass"]
    xlink = svg_from(name, "A", ref).replace('href="#', 'xlink:href="#')
    assert grade(name, "Here is my answer:\n```svg\n" + xlink + "\n```", "A")["pass"]


@pytest.mark.parametrize("bad", [
    "", "no svg here", "<svg><use href='#kit-x'", "<svg><use href=\"#kit-nope\"/></svg>",
    '<svg><use href="#kit-frame" transform="matrix(nan,0,0,1,0,0)"/></svg>',
    '<svg><use href="#kit-frame" transform="matrix(1,2)"/></svg>',
    '<svg><use href="#kit-frame" transform="translate(1e308 1e308) scale(1e308)"/></svg>',
])
def test_malformed_output_fails_cleanly(bad):
    for name in KITS:
        g = grade(name, bad, "A")
        assert g["pass"] is False and isinstance(g["issues"], list)


@pytest.mark.parametrize("name", KITS)
def test_condition_b_uses_anonymous_ids_and_rejects_names(name):
    ids = part_ids(name, "B")
    assert sorted(ids.values()) == [f"p{i + 1:02d}" for i in range(len(ids))]
    named = reference_svg(name, ids=part_ids(name, "A"))
    assert not grade(name, named, "B")["pass"]


def test_templates_differ_only_in_slots():
    for cond in CONDITIONS:
        pieces = re.split(r"\{\w+\}", TEMPLATES[cond])
        pattern = "(.*?)".join(re.escape(p) for p in pieces)
        for name in KITS:
            assert re.fullmatch(pattern, fill(name, cond), flags=re.S), (cond, name)


def test_no_recipe_prompts_contain_no_recipe():
    for name in KITS:
        task = load_task(name)
        hints = [j[0] for j in task.JOINTS] + [x[1] for x in getattr(task, "EXTRA", [])]
        for cond in NO_RECIPE:
            head = fill(name, cond).split("KIT:")[0]
            assert not [h for h in hints if h in head], (name, cond)


def test_kit_build_is_deterministic():
    def digest() -> str:
        h = hashlib.sha256()
        for name in KITS:
            for f in ("kit.json", "kit.svg", "reference_solution.svg"):
                h.update((TASKS / name / "build" / f).read_bytes())
        return h.hexdigest()
    before = digest()
    for name in KITS:
        build_kit(name)
    assert digest() == before


@pytest.mark.parametrize("name", KITS)
@pytest.mark.parametrize("cond", list(CONDITIONS))
def test_part_turned_about_its_own_joint_fails_unless_it_turns_in_use(name, cond):
    from kitbench.kit import free_rotation
    task = load_task(name)
    kit = load_kit(name)
    ref = reference_matrices(kit)
    free = free_rotation(task)
    for part, v in kit.items():
        if part == task.UPRIGHT[0] or part in free:
            continue
        pivot = tuple(apply(ref[part], next(iter(v["anchors"].values()))))
        for deg in (180, 30):
            mats = {**ref, part: rotate(deg, *pivot) @ ref[part]}
            assert not grade(name, svg_from(name, cond, mats), cond)["pass"], (part, deg)


def test_bike_drivetrain_turned_together_still_passes():
    ref = reference_matrices(load_kit("bike"))
    bb = first_anchor("bike", "chainring")
    mats = {k: (rotate(75, *bb) @ m if k in ("chainring", "crank", "pedal") else m) for k, m in ref.items()}
    for cond in CONDITIONS:
        assert grade("bike", svg_from("bike", cond, mats), cond)["pass"], cond


@pytest.mark.parametrize("name", KITS)
def test_every_part_mirrored_scaled_or_skewed_fails(name):
    ref = reference_matrices(load_kit(name))
    for part in ref:
        c = first_anchor(name, part)
        around = lambda t: translate(*c) @ t @ translate(-c[0], -c[1])  # noqa: E731
        for t in (mat(-1, 0, 0, 1, 0, 0), mat(1.05, 0, 0, 1.05, 0, 0), mat(1, 0, 0.2, 1, 0, 0), mat(0, 0, 0, 0, 0, 0)):
            assert not grade(name, svg_from(name, "A", {**ref, part: around(t) @ ref[part]}), "A")["pass"], part


def test_hostile_structure_fails_cleanly():
    deep = "<svg>" + "<g>" * 5000 + '<use href="#kit-frame"/>' + "</g>" * 5000 + "</svg>"
    assert grade("bike", deep, "A")["pass"] is False
    for t in ("rotate(30 5)", "translate(1 2 3)", "scale()", "matrix(1,0,0,1,0)", "rotate(10) garbage(1)"):
        assert grade("bike", f'<svg><use href="#kit-frame" transform="{t}"/></svg>', "A")["issues"]


@pytest.mark.parametrize("name", KITS)
def test_hidden_or_defs_placements_do_not_count(name):
    ref_svg = reference_svg(name)
    hidden = ref_svg.replace("<use ", '<defs><use ', 1).replace("/>", "/></defs>", 1)
    assert not grade(name, hidden, "A")["pass"]
    nonedisp = ref_svg.replace("<use ", '<use display="none" ', 1)
    assert not grade(name, nonedisp, "A")["pass"]


def test_last_parseable_svg_block_is_graded():
    good = reference_svg("pulley")
    assert grade("pulley", "draft: <svg><use href='#kit-beam'/></svg>\nfinal:\n" + good, "A")["pass"]
    assert grade("pulley", good + "\n<svg><broken", "A")["pass"]


@pytest.mark.parametrize("name", KITS)
def test_anonymous_ids_round_trip(name):
    ids = part_ids(name, "B")
    assert len(set(ids.values())) == len(ids)
    assert grade(name, reference_svg(name, ids=ids), "B")["pass"]
    prompt = fill(name, "B")
    assert not [p for p in ids if f'id="kit-{p}"' in prompt]


def test_swapped_bike_wheels_pass_but_misplaced_wheel_fails():
    ref = reference_matrices(load_kit("bike"))
    ra, fa = first_anchor("bike", "rear_wheel"), first_anchor("bike", "front_wheel")
    swapped = {**ref, "rear_wheel": translate(ra[0] - fa[0], ra[1] - fa[1]) @ ref["front_wheel"],
               "front_wheel": translate(fa[0] - ra[0], fa[1] - ra[1]) @ ref["rear_wheel"]}
    for cond in CONDITIONS:
        assert grade("bike", svg_from("bike", cond, swapped), cond)["pass"], cond
    both_rear = {**ref, "front_wheel": translate(ra[0] - fa[0], ra[1] - fa[1]) @ ref["front_wheel"]}
    assert not grade("bike", svg_from("bike", "A", both_rear), "A")["pass"]



def _slide(kit_name, chain, dx):
    def mod(part, m):
        if part in chain:
            t = np.eye(3)
            t[0, 2] = dx
            return t @ m
        return m
    return grade(kit_name, reference_svg(kit_name, load_kit(kit_name), modify=mod), "C")


def test_brackets_may_sit_anywhere_along_their_edge_but_not_off_it():
    lamp = ["l_bracket", "lower_arm", "elbow_plate", "upper_arm", "head_plate", "shade", "bulb"]
    pulley = ["bracket", "fixed_wheel", "rope", "movable_wheel", "strap", "hook", "shackle", "box"]
    assert _slide("desk_lamp", lamp, 120)["pass"] and not _slide("desk_lamp", lamp, 400)["pass"]
    assert _slide("pulley", pulley, -150)["pass"] and not _slide("pulley", pulley, 400)["pass"]


def test_jointed_lamp_passes_in_another_pose():
    pin = load_task("desk_lamp").PARTS["upper_arm"]["anchors"]["bottom_end_hole"]
    for deg in (15, -20):
        turn = translate(*pin) @ rotate(deg) @ translate(-pin[0], -pin[1])
        moved = lambda p, m: turn @ m if p in ("upper_arm", "head_plate", "shade", "bulb") else m  # noqa: E731
        assert grade("desk_lamp", reference_svg("desk_lamp", load_kit("desk_lamp"), modify=moved), "A")["pass"]


def test_scale_stirrup_may_hang_by_its_hook_or_by_the_hole_in_its_rod():
    task = load_task("scale")
    for side in ("left", "right"):
        a = task.PARTS[f"{side}_stirrup"]["anchors"]
        dx, dy = a["hook_curl_centre"][0] - a["rod_hole"][0], a["hook_curl_centre"][1] - a["rod_hole"][1]
        lowered = lambda p, m: translate(dx, dy) @ m if p in (f"{side}_stirrup", f"{side}_pan") else m  # noqa: E731
        assert grade("scale", reference_svg("scale", load_kit("scale"), modify=lowered), "C")["pass"], side
        too_far = lambda p, m: translate(2 * dx, 2 * dy) @ m if p in (f"{side}_stirrup", f"{side}_pan") else m  # noqa: E731
        assert not grade("scale", reference_svg("scale", load_kit("scale"), modify=too_far), "C")["pass"], side
