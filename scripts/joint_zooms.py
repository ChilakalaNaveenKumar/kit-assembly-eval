"""Draw a close-up of every graded connection on each kit's correct assembly, for human review: review/joints/<kit>.png."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from kitbench.geometry import apply  # noqa: E402
from kitbench.kit import criteria, kit_names, kit_svg, load_kit, load_task, reference_matrices, reference_svg  # noqa: E402
from kitbench.render import to_png  # noqa: E402

CELL, ZOOM_HALF, COLS = 300, 45, 4


def joint_points(name: str) -> list[dict]:
    """Every point-based check of the kit with the global positions of the features it compares."""
    task, kit = load_task(name), load_kit(name)
    ref = reference_matrices(kit)
    out = []
    for i, c in enumerate(criteria(task, "C")):
        if c["kind"] in ("upright", "angle", "orient"):
            continue
        keys = [("a", "an"), ("b", "bn"), ("b", "b1"), ("b", "b2"), ("a", "a1"), ("a", "a2")]
        pts = [tuple(apply(ref[c[p]], kit[c[p]]["anchors"][c[f]])) for p, f in keys if p in c and f in c]
        out.append({"n": i + 1, "text": c["text"], "points": pts})
    return out


def scene(name: str) -> tuple[str, str]:
    """The shared <defs> block and the placed parts of the correct assembly, as SVG fragments."""
    body = reference_svg(name)
    uses = body[body.index(">") + 1:body.rindex("</svg>")]
    kit = kit_svg(load_kit(name))
    return kit[kit.index("<defs>"):kit.index("</defs>") + 7], uses


def view(j: dict) -> tuple[float, float, float]:
    """Centre and half-width of the square close-up that holds every point of one connection."""
    cx = sum(p[0] for p in j["points"]) / len(j["points"])
    cy = sum(p[1] for p in j["points"]) / len(j["points"])
    half = max(ZOOM_HALF, max(abs(p[0] - cx) for p in j["points"]) + 15, max(abs(p[1] - cy) for p in j["points"]) + 15)
    return cx, cy, half


def marks(j: dict, half: float) -> str:
    """Red rings around each compared feature, sized to the close-up."""
    return "".join(f'<circle cx="{p[0]:.2f}" cy="{p[1]:.2f}" r="{half / 30:.2f}" fill="none" stroke="#d03b3b" stroke-width="{half / 90:.2f}"/>'
                   for p in j["points"])


def joint_svg(name: str, n: int) -> str:
    """Standalone SVG close-up of connection n of a kit; raises KeyError for an unknown n."""
    j = next((x for x in joint_points(name) if x["n"] == n), None)
    if j is None:
        raise KeyError(n)
    defs, uses = scene(name)
    cx, cy, half = view(j)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{CELL}" height="{CELL}" viewBox="{cx - half:.2f} {cy - half:.2f} {2 * half:.2f} {2 * half:.2f}">'
            f'<rect x="{cx - half:.2f}" y="{cy - half:.2f}" width="{2 * half:.2f}" height="{2 * half:.2f}" fill="#F8F7F2"/>{defs}{uses}{marks(j, half)}</svg>')


def sheet(name: str) -> str:
    """One SVG: a grid of zoomed views of the reference assembly, one per connection, with both features marked."""
    defs, uses = scene(name)
    joints = joint_points(name)
    rows = (len(joints) + COLS - 1) // COLS
    w, h = COLS * CELL, rows * (CELL + 110) + 10
    cells = []
    for i, j in enumerate(joints):
        x, y = (i % COLS) * CELL, (i // COLS) * (CELL + 110) + 10
        cx, cy, half = view(j)
        words = j["text"].split()
        lines, cur = [], ""
        for word in words:
            if len(cur) + len(word) > 44:
                lines.append(cur)
                cur = word
            else:
                cur = f"{cur} {word}".strip()
        lines.append(cur)
        caption = "".join(f'<text x="{x + 6}" y="{y + CELL + 16 + k * 14}" font-size="12" font-family="Helvetica" fill="#222">{t.replace("&", "&amp;").replace("<", "&lt;")}</text>'
                          for k, t in enumerate([f"{j['n']}. " + lines[0]] + lines[1:7]))
        cells.append(f'<rect x="{x + 2}" y="{y}" width="{CELL - 4}" height="{CELL}" fill="#F8F7F2" stroke="#999"/>'
                     f'<svg x="{x + 2}" y="{y}" width="{CELL - 4}" height="{CELL}" viewBox="{cx - half:.2f} {cy - half:.2f} {2 * half:.2f} {2 * half:.2f}">'
                     f'{uses}{marks(j, half)}</svg>{caption}')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<rect width="100%" height="100%" fill="white"/>{defs}{"".join(cells)}</svg>')


def main() -> None:
    """Write review/joints/<kit>.png for every kit."""
    for name in kit_names():
        to_png(sheet(name), ROOT / "review" / "joints" / f"{name}.png", width=COLS * CELL)
        print(f"{name}: {len(joint_points(name))} connections drawn")


if __name__ == "__main__":
    main()
