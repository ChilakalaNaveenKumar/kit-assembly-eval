"""The fixed prompt templates. Per kit only the {slots} change; every model receives the same bytes."""
from .kit import ORIENT_TOL, anon_ids, criteria, kit_svg, kit_tolerance, load_kit, load_task

TEMPLATE_VERSION = "v2"

_FRAME = """Below is a kit of {n_parts} SVG parts for a {object}. Each part is a <g id="kit-..."> drawn in its own local coordinate system, stored at an arbitrary rotation. {naming}

Assemble the parts into one complete, working {object} on a {w} x {h} canvas. Parts are rigid: translate and rotate only, no scaling and no mirroring. Use every part exactly once. The base part, {base}, stays upright exactly as stored (at most {upright_tol} degrees of rotation).
"""

_TURNING = "parts that turn in use (wheels, gears, sprockets, cranks, connecting rods, pedals, rotors) may sit at any angle"

_NO_RECIPE = """
Nobody will tell you which part connects to which, at which hole or feature, or which way round a part goes. Work that out from the parts, as a practitioner who knows this object would.

Grading is done by code on where the parts land:
- every connection the real object has must be made: the matching features of the two connected parts (pin holes, axle holes, bolt holes, hub centres, the centres of rounded ends, seats) must coincide within {tol} px;
- a part that slides along a guide (such as a piston in its bore) must sit on the guide's centre line, within {tol} px;
- every part must face the way it does on the working object, relative to the base part, within {orient_tol} degrees; """ + _TURNING + """;
- anything that stands on the ground must stand level, within {tol} px;
- a missing, duplicated, scaled, skewed or mirrored part fails the assembly.
"""

_NO_RECIPE_ALT = """
You are not given a list of which parts join, at which holes, or in which orientation. Decide that yourself from the drawings, the way someone who builds this object for a living would.

How it is scored (automatically, from the final position of every part):
- each joint that exists on the real object has to be made, meaning the corresponding features on the two parts (pin, axle or bolt holes, hub centres, centres of rounded ends, seats) line up within {tol} px;
- a sliding part (for example a piston in its bore) has to lie on the centre line of its guide, within {tol} px;
- each part has to point the same way as on the real, working object, measured relative to the base part, within {orient_tol} degrees; parts that rotate in use (wheels, gears, sprockets, cranks, connecting rods, pedals, rotors) can be at any angle;
- if the object rests on the ground, it has to rest level, within {tol} px;
- the assembly fails if any part is missing, used twice, scaled, skewed or mirrored.
"""

_WITH_RECIPE = """
Grading is done by code on where the parts land:
{checks}
- every other part must face the way it does on the working object, relative to the base part, within {orient_tol} degrees; """ + _TURNING + """;
- a missing, duplicated, scaled, skewed or mirrored part fails the assembly.
"""

_OUTPUT = """
Reply with one <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}"> that contains exactly one <use href="#kit-ID" transform="..."/> per part. You may wrap <use> elements in <g transform="..."> groups. Do not copy the part drawings: the kit's <defs> are inserted automatically.

KIT:
{kit}"""

TEMPLATES = {
    "A": _FRAME + _NO_RECIPE + _OUTPUT,
    "A_alt": _FRAME + _NO_RECIPE_ALT + _OUTPUT,
    "B": _FRAME + _NO_RECIPE + _OUTPUT,
    "C": _FRAME + _WITH_RECIPE + _OUTPUT,
}
CONDITIONS = {
    "A": "named parts, no recipe",
    "A_alt": "named parts, no recipe, reworded template",
    "B": "unnamed parts, no recipe",
    "C": "named parts, full recipe (control)",
}
NAMED = "Each part's id names the part."
UNNAMED = "The parts are unlabelled (ids p01 to p{last}); work out what each one is from its drawing."


def part_ids(name: str, condition: str) -> dict[str, str]:
    """Part name -> id shown to the model in this condition."""
    if condition == "B":
        return anon_ids(name)
    return {p: p for p in load_task(name).PARTS}


def fill(name: str, condition: str) -> str:
    """The prompt for one kit in one condition."""
    task = load_task(name)
    kit = load_kit(name)
    ids = part_ids(name, condition)
    recipe = [c for c in criteria(task, "C") if c["kind"] != "orient"]
    w, h = task.CANVAS
    slots = {
        "n_parts": len(task.PARTS),
        "object": task.OBJECT,
        "naming": UNNAMED.format(last=f"{len(task.PARTS):02d}") if condition == "B" else NAMED,
        "w": w,
        "h": h,
        "base": f"kit-{ids[task.UPRIGHT[0]]}",
        "upright_tol": task.UPRIGHT[1],
        "tol": f"{kit_tolerance(task):g}",
        "orient_tol": f"{ORIENT_TOL:g}",
        "checks": "\n".join(f"- {c['text']}" for c in recipe),
        # parts listed in id order so the authoring order cannot hint at the assembly in condition B
        "kit": kit_svg(kit, ids, order=sorted(kit, key=lambda p: ids[p])),
    }
    return TEMPLATES[condition].format(**slots)
