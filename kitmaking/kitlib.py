"""Shared helpers to combine a machine from its vectorized parts.

Each part = its crop PNG (fcrops/<m>/pNN.png) + the author's vectorizer SVG (fsvg/<m>/pNN.svg).
The SVG is clipped to the part's own outline (traced from the crop) so box backgrounds never show.
Placement: part-local point (px, py) goes to world (X, Y), turned by `rot` degrees about that point.
"""
import re, subprocess
from pathlib import Path
import cv2, numpy as np

H = Path(__file__).resolve().parent
NS = 'xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"'


def load(machine, cuts=None):
    """All parts of a machine. cuts: {num: [(x0, y0, x1, y1), ...]} crop-pixel boxes to remove from a part's outline."""
    parts = {}
    for svg in sorted((H / 'fsvg' / machine).glob('p*.svg')):
        n = int(svg.stem[1:]); im = cv2.imread(str(H / 'fcrops' / machine / f'{svg.stem}.png')); h, w = im.shape[:2]
        bg = np.median(np.concatenate([im[:4, :4], im[:4, -4:], im[-4:, :4], im[-4:, -4:]]).reshape(-1, 3), 0)
        diff = np.abs(im.astype(int) - bg).sum(2)
        ink = cv2.morphologyEx((diff > 45).astype(np.uint8), cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
        outer, _ = cv2.findContours(ink, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        fg = np.zeros_like(ink); cv2.drawContours(fg, [c for c in outer if cv2.contourArea(c) > 40], -1, 1, -1)   # solid part, pale fills included
        for (a, b, c, d) in (cuts or {}).get(n, []): fg[b:d, a:c] = 0
        # holes: near-background islands inside the solid part, roughly round (pin holes, eyes)
        isl = ((diff < 14) & (fg > 0)).astype(np.uint8)
        hc, _ = cv2.findContours(isl, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        holes, hole_cs = [], []
        for c in hc:
            a = cv2.contourArea(c)
            if a < 25 or a > 0.05 * w * h: continue
            (x, y), r = cv2.minEnclosingCircle(c)
            if a / (np.pi * r * r) > 0.55: holes.append((round(x, 1), round(y, 1), round(r, 1))); hole_cs.append(c)
        outs, _ = cv2.findContours(fg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        clip = ' '.join('M' + ' L'.join(f'{x} {y}' for x, y in c.reshape(-1, 2)) + ' Z' for c in list(outs) + hole_cs if cv2.contourArea(c) > 20)
        s = svg.read_text(); vb = re.search(r'viewBox="([^"]+)"', s).group(1)
        body = s[s.index('>', s.index('<svg')) + 1:s.rindex('</svg>')]
        ys, xs = np.where(fg)
        parts[n] = dict(n=n, w=w, h=h, vb=vb, body=body, clip=clip, holes=holes, fg=fg, box=(int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())))
    return parts


def svg_of(p, X=0.0, Y=0.0, px=0.0, py=0.0, rot=0.0, uid='', s=1.0):
    """Part p drawn so its local point (px, py) lands on (X, Y), turned rot degrees about it, evenly resized by s."""
    t = f'translate({X:.2f},{Y:.2f}) rotate({rot:.3f}) scale({s:.4f}) translate({-px:.2f},{-py:.2f})'
    cid = f'clip{p["n"]}{uid}'
    return (f'<g transform="{t}"><clipPath id="{cid}" clipPathUnits="userSpaceOnUse"><path clip-rule="evenodd" d="{p["clip"]}"/></clipPath>'
            f'<g clip-path="url(#{cid})"><svg x="0" y="0" width="{p["w"]}" height="{p["h"]}" viewBox="{p["vb"]}" preserveAspectRatio="none">{p["body"]}</svg></g></g>')


def world(px, py, X, Y, rot, qx, qy, s=1.0):
    """Where part-local point (qx, qy) ends up, for a part placed with (px, py) -> (X, Y), rot, even resize s."""
    t = np.radians(rot); dx, dy = (qx - px) * s, (qy - py) * s
    return X + dx * np.cos(t) - dy * np.sin(t), Y + dx * np.sin(t) + dy * np.cos(t)


def render(out, items, pad=60, width=1400):
    """items: list of (part, X, Y, px, py, rot[, s]) in draw order (back to front). Writes out.svg and out.png fitted to content."""
    items = [tuple(it) + (1.0,) * (7 - len(it)) for it in items]
    pts = []
    for p, X, Y, px, py, rot, s in items:
        b = p['box']
        pts += [world(px, py, X, Y, rot, qx, qy, s) for qx, qy in ((b[0], b[1]), (b[2], b[1]), (b[0], b[3]), (b[2], b[3]))]
    xs, ys = [q[0] for q in pts], [q[1] for q in pts]
    x0, y0, x1, y1 = min(xs) - pad, min(ys) - pad, max(xs) + pad, max(ys) + pad
    body = ''.join(svg_of(p, X, Y, px, py, rot, uid=f'_{i}', s=s) for i, (p, X, Y, px, py, rot, s) in enumerate(items))
    svg = (f'<svg {NS} width="{x1 - x0:.0f}" height="{y1 - y0:.0f}" viewBox="{x0:.0f} {y0:.0f} {x1 - x0:.0f} {y1 - y0:.0f}">'
           f'<rect x="{x0:.0f}" y="{y0:.0f}" width="{x1 - x0:.0f}" height="{y1 - y0:.0f}" fill="#FFFFFF"/>{body}</svg>')
    Path(f'{out}.svg').write_text(svg)
    subprocess.run(['rsvg-convert', '-w', str(width), f'{out}.svg', '-o', f'{out}.png'], check=True)


def sheet(out, parts, names, cols_w=2600):
    """Every part upright, alone, labelled - for review."""
    x = y = 40; row = 0; cells = []
    for n, name in names.items():
        p = parts[n]
        if x + p['w'] > cols_w: x = 40; y += row + 90; row = 0
        cells.append(svg_of(p, x, y, uid='_s') + f'<text x="{x}" y="{y + p["h"] + 50}" font-size="40" font-family="Helvetica" fill="#333">{n}. {name}</text>')
        x += p['w'] + 60; row = max(row, p['h'])
    hgt = y + row + 90
    Path(f'{out}.svg').write_text(f'<svg {NS} width="{cols_w + 40}" height="{hgt}" viewBox="0 0 {cols_w + 40} {hgt}"><rect width="100%" height="100%" fill="#FFFFFF"/>{"".join(cells)}</svg>')
    subprocess.run(['rsvg-convert', '-w', '1600', f'{out}.svg', '-o', f'{out}.png'], check=True)
