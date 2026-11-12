"""Rebuild every kit: kit.json, kit.svg, reference_solution.svg, reference.png and kit_marked.png."""
import sys
from pathlib import Path

from svgelements import Path as SvgPath

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from kitbench.grader import grade  # noqa: E402
from kitbench.kit import TASKS, build_kit, kit_names, kit_svg, reference_svg  # noqa: E402
from kitbench.render import assembly_svg, to_png  # noqa: E402
from kitbench.templates import CONDITIONS, part_ids  # noqa: E402


def marked_sheet(name: str, kit: dict) -> str:
    """All parts laid out in a grid with their attach points in red (for human review, never sent to models)."""
    defs = kit_svg(kit)
    defs = defs[defs.index("<defs>"):defs.index("</defs>") + 7]
    x = y = row = 0
    width, cells = 2000, []
    for part, v in kit.items():
        boxes = [SvgPath(d).bbox() for d, _ in v["paths"]]
        w, h = max(b[2] for b in boxes) + 10, max(b[3] for b in boxes) + 10
        if x + w > width and x > 0:
            x, y, row = 0, y + row + 50, 0
        dots = "".join(f'<circle cx="{a[0]}" cy="{a[1]}" r="5" fill="red"/>' for a in v["anchors"].values())
        cells.append(f'<g transform="translate({x + 10},{y + 40})"><use href="#kit-{part}"/>{dots}'
                     f'<text x="0" y="-12" font-size="22" font-family="Helvetica" fill="#c00">{part}</text></g>')
        x, row = x + w + 40, max(row, h)
    total = y + row + 60
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{total}" viewBox="0 0 {width} {total}">'
            f'<rect width="100%" height="100%" fill="white"/>{defs}{"".join(cells)}</svg>')


def main() -> None:
    """Rebuild every kit, check each reference passes, and write the figures."""
    for name in kit_names():
        kit = build_kit(name)
        for cond in CONDITIONS:
            ref = reference_svg(name, kit, ids=part_ids(name, cond))
            g = grade(name, ref, cond)
            if not g["pass"]:
                raise SystemExit(f"{name}/{cond}: reference fails its own checks: {g}")
        out = TASKS / name / "build"
        to_png(assembly_svg(name, reference_svg(name, kit), "A", f"{name}: correct assembly"), out / "reference.png")
        to_png(marked_sheet(name, kit), out / "kit_marked.png", width=1400)
        print(f"{name}: built, reference passes in {', '.join(CONDITIONS)}")


if __name__ == "__main__":
    main()
