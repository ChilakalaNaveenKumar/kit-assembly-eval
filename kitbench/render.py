"""Draw an assembly (reference or model output) to PNG with rsvg-convert."""
import re
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import quoteattr

from .grader import extract_svg
from .kit import kit_svg, load_kit, load_task
from .templates import part_ids


def _emit(e: ET.Element) -> str:
    """Re-emit only <g> and <use href="#kit-..."> elements with their placement attributes; drop everything else."""
    tag = e.tag.split("}")[-1]
    kids = "".join(_emit(c) for c in e)
    tr = e.get("transform")
    tr_attr = f" transform={quoteattr(tr)}" if tr is not None else ""
    if tag == "g":
        return f"<g{tr_attr}>{kids}</g>"
    if tag == "use":
        ref = e.get("href") or ""
        if not ref.startswith("#kit-"):
            return ""
        xy = "".join(f" {k}={quoteattr(e.get(k))}" for k in ("x", "y") if e.get(k) is not None)
        return f"<use href={quoteattr(ref)}{tr_attr}{xy}/>"
    return ""


def assembly_svg(name: str, reply: str, condition: str, title: str = "") -> str | None:
    """A standalone SVG: the reply's placements (<g>/<use> only) plus the kit defs, on paper background."""
    svg = extract_svg(reply)
    if svg is None:
        return None
    try:
        root = ET.fromstring(re.sub(r'\sxmlns(:\w+)?="[^"]*"', "", svg).replace("xlink:href", "href"))
        body = "".join(_emit(c) for c in root)
    except ET.ParseError:
        return None
    task = load_task(name)
    w, h = task.CANVAS
    kit = kit_svg(load_kit(name), part_ids(name, condition))
    defs = kit[kit.index("<defs>"):kit.index("</defs>") + 7]
    head = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><rect width="{w}" height="{h}" fill="#F8F7F2"/>'
    label = f'<text x="16" y="34" font-size="26" font-family="Helvetica" fill="#c00">{title}</text>' if title else ""
    return head + defs + body + label + "</svg>"


def to_png(svg: str, png: Path, width: int = 1100) -> None:
    """Rasterise an SVG string to PNG."""
    png.parent.mkdir(parents=True, exist_ok=True)
    src = png.with_suffix(".svg")
    src.write_text(svg)
    subprocess.run(["rsvg-convert", "-w", str(width), str(src), "-o", str(png)], check=True)
