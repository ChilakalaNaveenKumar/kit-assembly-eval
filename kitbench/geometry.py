"""2D affine transforms as 3x3 matrices, and SVG transform-attribute parsing."""
import math
import re

import numpy as np

_TRANSFORM = re.compile(r"(matrix|translate|scale|rotate|skewX|skewY)\s*\(([^)]*)\)")
_NUMBER = re.compile(r"[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?")


def mat(a: float, b: float, c: float, d: float, e: float, f: float) -> np.ndarray:
    """Matrix for SVG matrix(a b c d e f)."""
    return np.array([[a, c, e], [b, d, f], [0.0, 0.0, 1.0]])


def translate(dx: float, dy: float) -> np.ndarray:
    """Translation matrix."""
    return mat(1, 0, 0, 1, dx, dy)


def rotate(deg: float, cx: float = 0.0, cy: float = 0.0) -> np.ndarray:
    """Rotation by deg (SVG sense, y down) about (cx, cy)."""
    r = math.radians(deg)
    c, s = math.cos(r), math.sin(r)
    return translate(cx, cy) @ mat(c, s, -s, c, 0, 0) @ translate(-cx, -cy)


_ARITY = {"matrix": {6}, "translate": {1, 2}, "scale": {1, 2}, "rotate": {1, 3}, "skewX": {1}, "skewY": {1}}


def parse_transform(text: str | None) -> np.ndarray:
    """Parse an SVG transform attribute into one matrix; anything malformed raises ValueError."""
    m = np.eye(3)
    text = text or ""
    if _TRANSFORM.sub("", text).strip(" ,\t\n"):
        raise ValueError(f"unrecognised transform text: {text[:60]!r}")
    for name, args in _TRANSFORM.findall(text):
        v = [float(x) for x in _NUMBER.findall(args)]
        if len(v) not in _ARITY[name]:
            raise ValueError(f"{name}() with {len(v)} numbers")
        if name == "matrix":
            t = mat(*v)
        elif name == "translate":
            t = translate(v[0], v[1] if len(v) > 1 else 0.0)
        elif name == "scale":
            t = mat(v[0], 0, 0, v[1] if len(v) > 1 else v[0], 0, 0)
        elif name == "rotate":
            t = rotate(v[0], v[1], v[2]) if len(v) == 3 else rotate(v[0])
        elif name == "skewX":
            t = mat(1, 0, math.tan(math.radians(v[0])), 1, 0, 0)
        else:
            t = mat(1, math.tan(math.radians(v[0])), 0, 1, 0, 0)
        m = m @ t
    return m


def apply(m: np.ndarray, p: tuple[float, float]) -> np.ndarray:
    """Apply matrix m to point p; returns a length-2 array."""
    return (m @ np.array([p[0], p[1], 1.0]))[:2]


def rotation_deg(m: np.ndarray) -> float:
    """Rotation angle of the linear part of m, in degrees."""
    return math.degrees(math.atan2(m[1, 0], m[0, 0]))


def angle_diff(a: float, b: float) -> float:
    """Smallest absolute difference between two angles in degrees."""
    return abs((a - b + 180.0) % 360.0 - 180.0)
