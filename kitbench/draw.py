"""Drawing helpers used by task files. All coordinates are in the assembled (global) frame."""
import math

PAL = {"blue": "#DBEAF7", "lilac": "#EBE3F7", "cream": "#FDF1C9", "coral": "#FEB8A7", "mint": "#DFF1E3",
       "grey": "#ECEAE4", "pink": "#FBE1DC", "ink": "#1F2A3A", "paper": "#F8F7F2"}
Point = tuple[float, float]


def f(v: float) -> str:
    """Format a coordinate with 2 decimals."""
    return f"{v:.2f}"


def _attrs(kw: dict[str, str | float]) -> str:
    return "".join(f' {k.replace("_", "-")}="{v}"' for k, v in kw.items())


def circle(c: Point, r: float, fill: str = PAL["grey"], **kw: str | float) -> str:
    """Filled circle."""
    return f'<circle cx="{f(c[0])}" cy="{f(c[1])}" r="{f(r)}" fill="{fill}"{_attrs(kw)}/>'


def hole(c: Point, r: float = 5) -> str:
    """Pin hole: a circle filled with the paper colour."""
    return circle(c, r, fill=PAL["paper"])


def bar(p1: Point, p2: Point, w: float, fill: str = PAL["blue"], holes: bool = True, hole_r: float | None = None) -> list[str]:
    """Rounded link bar between two pin centres, with a pin hole at each end."""
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    length = math.hypot(dx, dy)
    nx, ny = -dy / length * w / 2, dx / length * w / 2
    r = w / 2
    d = (f"M{f(p1[0]+nx)} {f(p1[1]+ny)} L{f(p2[0]+nx)} {f(p2[1]+ny)} A{f(r)} {f(r)} 0 0 0 {f(p2[0]-nx)} {f(p2[1]-ny)} "
         f"L{f(p1[0]-nx)} {f(p1[1]-ny)} A{f(r)} {f(r)} 0 0 0 {f(p1[0]+nx)} {f(p1[1]+ny)} Z")
    out = [f'<path d="{d}" fill="{fill}"/>']
    if holes:
        out += [hole(p1, hole_r or w * 0.22), hole(p2, hole_r or w * 0.22)]
    return out


def poly(pts: list[Point], fill: str = PAL["lilac"]) -> str:
    """Closed polygon."""
    return '<path d="M' + " L".join(f"{f(x)} {f(y)}" for x, y in pts) + f' Z" fill="{fill}"/>'


def rect(x: float, y: float, w: float, h: float, fill: str = PAL["grey"], rx: float = 0) -> str:
    """Rectangle, optionally with rounded corners."""
    return f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" rx="{f(rx)}" fill="{fill}"/>'


def line(p1: Point, p2: Point, **kw: str | float) -> str:
    """Straight line."""
    return f'<line x1="{f(p1[0])}" y1="{f(p1[1])}" x2="{f(p2[0])}" y2="{f(p2[1])}"{_attrs(kw)}/>'


def rot_pt(p: Point, c: Point, deg: float) -> Point:
    """Rotate point p about c by deg (SVG sense, y down)."""
    a = math.radians(deg)
    x, y = p[0] - c[0], p[1] - c[1]
    return (c[0] + x * math.cos(a) - y * math.sin(a), c[1] + x * math.sin(a) + y * math.cos(a))
