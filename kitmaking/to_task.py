"""Turn a combined machine (assemble_<m>.py + joints.json) into a kit task: kit-assembly-eval/tasks/<m>/task.py.

Each part keeps the author's vectorizer paths (background shapes dropped, embedded hole images replaced by drawn
holes), moved into the assembled position, and the whole machine fitted to the 1376 x 768 canvas the other kits use.
Anchors are the joint points from joints.json, so every joint sits on a feature both parts show.
usage: python to_task.py <machine>"""
import json, re, runpy, sys
from pathlib import Path
import numpy as np
import kitlib

CFG = {
    'hand_pump': dict(obj='hand water pump (side view)', base='base_plate', free_spin={}, free_rot=set(), swap=[]),
    'desk_lamp': dict(obj='desk lamp with a jointed arm (side view)', base='base', free_spin={}, free_rot=set(), swap=[]),
    'scale': dict(obj='balance scale (side view)', base='base', free_spin={}, free_rot=set(), swap=[('left_pan', 'right_pan'), ('left_stirrup', 'right_stirrup')]),
    'wheelbarrow': dict(obj='wheelbarrow (side view)', base='handle_frame', free_spin={'tyre': (332.49, 556.34), 'wheel_hub': (332.49, 556.34)}, free_rot=set(), swap=[]),
}
ROTS = [35, 70, 140, 110, 125, 55, 160, 25, 95, 145]
INK, PAPER = '#1F2A3A', '#F8F7F2'
CANVAS = (1376, 768)


def slug(t):
    t = re.sub(r'^p\d+\s+', '', t.strip().lower())
    return re.sub(r'[^a-z0-9]+', '_', t).strip('_')


def captured(machine):
    """Run assemble_<m>.py with kitlib.render captured: placements and part names."""
    got = {}
    real_render, real_sheet = kitlib.render, kitlib.sheet
    kitlib.render = lambda out, items, **k: got.setdefault('items', [tuple(it) + (1.0,) * (7 - len(it)) for it in items])
    kitlib.sheet = lambda out, parts, names, **k: got.setdefault('names', dict(names))
    try:
        runpy.run_path(str(kitlib.H / f'assemble_{machine}.py'), run_name='__main__')
    finally:
        kitlib.render, kitlib.sheet = real_render, real_sheet
    return got['items'], got['names']


def affine(X, Y, px, py, rot, s):
    """3x3 matrix: crop px -> world."""
    t = np.radians(rot); c, sn = np.cos(t) * s, np.sin(t) * s
    return np.array([[c, -sn, X - (c * px - sn * py)], [sn, c, Y - (sn * px + c * py)], [0, 0, 1]])


def mstr(m):
    return f'matrix({m[0,0]:.6f},{m[1,0]:.6f},{m[0,1]:.6f},{m[1,1]:.6f},{m[0,2]:.4f},{m[1,2]:.4f})'


def part_elements(p, M):
    """Vectorizer paths of part p, background dropped, holes as drawn circles; M maps crop px -> canvas."""
    raw = (kitlib.H / 'fsvg' / p['machine'] / f'p{p["n"]:02d}.svg').read_text()
    head = raw[:raw.index('>', raw.index('<svg')) + 1]
    s = head + p['body'] + '</svg>'                                      # the drawing exactly as combined (e.g. mirrored)
    mirror = 'scale(-1,1)' in p['body'][:200]
    vx, vy, vw, vh = [float(v) for v in re.search(r'viewBox="([^"]+)"', s).group(1).split()]
    S = np.array([[p['w'] / vw, 0, -vx * p['w'] / vw], [0, p['h'] / vh, -vy * p['h'] / vh], [0, 0, 1]])   # svg units -> crop px
    T = M @ S
    bgc = np.array(p['bg'])
    els = []
    import io
    from svgelements import SVG, Path as SP, Shape, Matrix
    doc = SVG.parse(io.StringIO(re.sub(r'<image[^>]*/>', '', s)), reify=True)      # applies every nested group transform
    Tm = Matrix(M[0, 0], M[1, 0], M[0, 1], M[1, 1], M[0, 2], M[1, 2])   # parser output is already in crop px
    for e in doc.elements():
        if not isinstance(e, Shape) or e.fill is None or e.fill.value is None: continue
        q = SP(e); q.reify()
        if len(q) == 0: continue
        x0, y0, x1, y1 = [v / f for v, f in zip(q.bbox(), (p["w"] / vw, p["h"] / vh) * 2)]
        rgb = np.array([e.fill.red, e.fill.green, e.fill.blue])
        touches_edge = x0 <= vx + 3 or y0 <= vy + 3 or x1 >= vx + vw - 3 or y1 >= vy + vh - 3
        if touches_edge and np.abs(rgb - bgc).sum() < 40: continue        # the crop's background
        q = q * Tm; q.reify()
        els.append(f'<path d="{q.d()}" fill="{e.fill.hex[:7]}" fill-rule="{e.values.get("fill-rule", "nonzero")}" stroke="none"/>')
    k = np.sqrt(abs(np.linalg.det(M[:2, :2])))                          # crop px -> canvas length factor
    for im in re.finditer(r'<image x="([-\d.]+)" y="([-\d.]+)" width="([-\d.]+)" height="([-\d.]+)"', s):
        x, y, w, h = [float(v) for v in im.groups()]
        cx = x + w / 2
        if mirror: cx = 2 * vx + vw - cx
        c = S @ np.array([cx, y + h / 2, 1])
        near = min(p['holes'], key=lambda q: (q[0] - c[0]) ** 2 + (q[1] - c[1]) ** 2, default=None)
        r = near[2] if near and np.hypot(near[0] - c[0], near[1] - c[1]) < 25 else w * p['w'] / vw * 0.08
        cc = M @ np.array([c[0], c[1], 1])
        els.append(f'<circle cx="{cc[0]:.2f}" cy="{cc[1]:.2f}" r="{max(r * k, 2.5):.2f}" fill="{PAPER}" stroke="{INK}" stroke-width="2.3"/>')
    return els


def main(machine):
    cfg = CFG[machine]
    items, names = captured(machine)
    P = kitlib.load(machine)
    num_of = {id(it[0]): it[0]['n'] for it in items}
    place = {it[0]['n']: affine(*it[1:]) for it in items}
    # fit the assembled machine onto the canvas
    pts = []
    for n, A in place.items():
        b = P[n]['box']
        pts += [(A @ np.array([qx, qy, 1]))[:2] for qx, qy in ((b[0], b[1]), (b[2], b[1]), (b[0], b[3]), (b[2], b[3]))]
    pts = np.array(pts); lo, hi = pts.min(0), pts.max(0)
    k = min((CANVAS[0] - 120) / (hi[0] - lo[0]), (CANVAS[1] - 80) / (hi[1] - lo[1]))
    off = np.array(CANVAS) / 2 - k * (lo + hi) / 2
    F = np.array([[k, 0, off[0]], [0, k, off[1]], [0, 0, 1]])
    pname = {n: slug(names[n]) for n in place}
    joints = json.loads((kitlib.H / 'assembly' / f'{machine}_joints.json').read_text())
    by_name = {slug(v): n for n, v in names.items()}
    anchors = {n: {} for n in place}; JOINTS = []
    for j in joints:
        if 'joins_part' not in j or 'world_point' not in j: continue
        a, b = by_name[slug(j['part'])], by_name[slug(j['joins_part'])]
        w = F @ np.array([*j['world_point'], 1]); pt = (round(float(w[0]), 2), round(float(w[1]), 2))
        fa, fb = slug(j['feature']), slug(j['joins_feature'])
        anchors[a][fa] = pt; anchors[b][fb] = pt
        A, B = names[a].split(' ', 1)[-1] if names[a].startswith('p') and names[a][1:3].isdigit() else names[a], names[b]
        JOINTS.append((f"{pname[a].replace('_', ' ').capitalize()}: its {j['feature']} on the {pname[b].replace('_', ' ')}'s {j['joins_feature']}",
                       pname[a], fa, pname[b], fb, 6))
    parts = {}
    cap = {it[0]['n']: it[0] for it in items}
    for i, (n, A) in enumerate(place.items()):
        p = dict(cap[n]); p['machine'] = machine
        im = __import__('cv2').imread(str(kitlib.H / 'fcrops' / machine / f'p{n:02d}.png'))
        p['bg'] = [int(v) for v in np.median(im[:4, :4].reshape(-1, 3), 0)[::-1]]
        parts[pname[n]] = {'els': part_elements(p, F @ A), 'anchors': anchors[n]}
    order = [pname[it[0]['n']] for it in items]                         # back-to-front, as combined
    rot = {nm: (0 if nm == cfg['base'] else ROTS[i % len(ROTS)]) for i, nm in enumerate(order)}
    out = Path(kitlib.H).parent / 'kit-assembly-eval' / 'tasks' / machine; out.mkdir(parents=True, exist_ok=True)
    src = ['# Kit cut from the author\'s generated drawing: parts vectorized with the author\'s vectorizer, combined at their own joints.',
           f'PARTS = {json.dumps({nm: parts[nm] for nm in order}, indent=1)}',
           f'ROT = {json.dumps(rot)}', f'CANVAS = {CANVAS}', f'OBJECT = {cfg["obj"]!r}',
           f"UPRIGHT = ({cfg['base']!r}, 3, {('The ' + cfg['base'].replace('_', ' ') + ' upright: rotated at most 3 deg from how it is stored.')!r})",
           f'JOINTS = {json.dumps(JOINTS, indent=1)}', 'EXTRA = []',
           f'FREE_SPIN = {cfg["free_spin"]!r}', f'FREE_ROTATION = {cfg["free_rot"]!r}', f'INTERCHANGEABLE = {cfg["swap"]!r}']
    (out / 'task.py').write_text('\n'.join(src).replace(': null', ': None').replace(': true', ': True').replace(': false', ': False') + '\n')
    print(machine, 'parts', len(parts), 'joints', len(JOINTS), 'canvas scale', round(k, 3))


if __name__ == '__main__':
    main(sys.argv[1])
