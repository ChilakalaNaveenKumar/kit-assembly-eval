"""Wheelbarrow: parts sheet + assembly, each part placed by its own holes and edges (kitlib)."""
import json, re, subprocess
import numpy as np
import kitlib
from kitlib import world

P = kitlib.load('wheelbarrow')
NAMES = {1: 'tray', 2: 'handle frame', 3: 'leg stand', 4: 'tyre', 5: 'wheel hub', 6: 'wheel fork'}
OUT = kitlib.H / 'assembly'


def mirrored(p):
    """Part p flipped left-right (same size); crop-pixel x -> w-1-x."""
    w = p['w']; vx, vy, vw, vh = map(float, p['vb'].split())
    q = dict(p)
    q['body'] = f'<g transform="translate({2 * vx + vw},0) scale(-1,1)">{p["body"]}</g>'
    q['clip'] = re.sub(r'([ML])(-?[\d.]+) (-?[\d.]+)', lambda m: f'{m[1]}{w - 1 - float(m[2]):g} {m[3]}', p['clip'])
    q['fg'] = p['fg'][:, ::-1].copy()
    b = p['box']; q['box'] = (w - 1 - b[2], b[1], w - 1 - b[0], b[3])
    return q


# tray faces the other way in the reference (long slope toward the wheel, deep end toward the grips)
P[1] = mirrored(P[1])
TW1 = P[1]['w']
mx = lambda q: (TW1 - 1 - q[0], q[1])

# joint features, crop px (holes found as ink rings in the crops)
H_END = (49.7, 277.3)                      # handle: bolt hole at the front end (on the tube centre line)
H_TAB2 = (289.0, 197.5)                    # handle: hole in the middle under-tab
H_TAB3 = (518.4, 146.0)                    # handle: hole in the rear under-tab
T_REAR = mx((157.0, 256.0))                # tray (mirrored): rear hole of the bolt strip
T_FRONT = mx((415.0, 284.0))               # tray (mirrored): front hole of the bolt strip
L_HOLE1 = (43.0, 50.0)                     # leg: front hole of the bolt bracket
F_AXLE = (231.1, 268.0)                    # fork: axle hole at the bottom of the triangle (r 9)
F_SOCK = (397.5, 127.5)                    # fork: centre of the socket at the bar's rear end
HUB_C = (142.6, 143.0)                     # hub axle bore
TYRE_C = (232.5, 232.0)                    # tyre centre (box 24..441 x 24..440)
TYRE_R = 208.5


S_H, S_W, S_F = 2.2, 1.05, 1.2            # even resize: handle frame, tyre + hub, wheel fork
R_H = 6.0                                 # handle turn (degrees, clockwise on screen)
F_TAB = (92.3, 47.8)                      # fork: bolt hole in the tab above the bar
FORK_BAR = 3.9                            # fork bar slopes this much down to the right in its crop
TUBE_FRONT = -27.9                        # handle front run slope in its crop (rising to the right)


def tube_edges(x):
    ys = np.where(P[2]['fg'][:, int(round(x))])[0]
    return float(ys.min()), float(ys.min() + 40)          # tube is 40 px thick; tabs hang below it


def ang(a, b):
    return np.degrees(np.arctan2(b[1] - a[1], b[0] - a[0]))


def leg_top_tip():
    """Leg: middle of the flat top lip of the rear strut."""
    x = 408; return float(x), float(np.where(P[3]['fg'][:, x])[0].min())


def lowest(n, X, Y, px, py, rot, s):
    ys, xs = np.where(P[n]['fg'][::2, ::2]); wx, wy = world(px, py, X, Y, rot, xs * 2.0, ys * 2.0, s)
    i = np.argmax(wy); return float(wx[i]), float(wy[i])


def root(f, lo, hi):
    flo = f(lo); assert flo * f(hi) < 0, (lo, hi, flo, f(hi))
    for _ in range(60):
        m = (lo + hi) / 2
        if f(m) * flo > 0: lo = m
        else: hi = m
    return (lo + hi) / 2


def layout():
    pl, J = {}, []
    R = R_H
    pl[2] = (0.0, 0.0, *H_END, R, S_H)
    hw = lambda q: world(*H_END, 0.0, 0.0, R, *q, S_H)

    def to_handle(W):                                      # world point -> handle crop px
        t = np.radians(-R); dx, dy = W[0], W[1]
        return H_END[0] + (dx * np.cos(t) - dy * np.sin(t)) / S_H, H_END[1] + (dx * np.sin(t) + dy * np.cos(t)) / S_H

    # fork: tab hole on the handle's front end hole; bar turned to run along the front run of the tube
    RF = R + TUBE_FRONT - FORK_BAR
    pl[6] = (0.0, 0.0, *F_TAB, RF, S_F)
    J.append(('wheel fork', 'bolt hole in the tab above the bar', 'handle frame', 'bolt hole at the front end of the tube', F_TAB, (0.0, 0.0), H_END, S_F))
    AX = world(*F_TAB, 0.0, 0.0, RF, *F_AXLE, S_F)
    pl[5] = (*AX, *HUB_C, 0.0, S_W); pl[4] = (*AX, *TYRE_C, 0.0, S_W)
    J.append(('wheel hub', 'axle bore', 'wheel fork', 'axle hole at the bottom of the triangle', HUB_C, AX, F_AXLE, S_W))
    J.append(('tyre', 'centre of the inner rim', 'wheel hub', 'axle bore (concentric)', TYRE_C, AX, HUB_C, S_W))

    # tray: bolt strip holes on both holed under-tabs (size and turn set by the two holes)
    T3, T2 = hw(H_TAB3), hw(H_TAB2)
    st = np.hypot(*np.subtract(T3, T2)) / np.hypot(*np.subtract(T_REAR, T_FRONT))
    rt = ang(T2, T3) - ang(T_FRONT, T_REAR)
    pl[1] = (*T2, *T_FRONT, rt, st)
    J.append(('tray', 'rear hole of the bolt strip', 'handle frame', 'hole in the rear under-tab', T_REAR, T3, H_TAB3, st))
    J.append(('tray', 'front hole of the bolt strip', 'handle frame', 'hole in the middle under-tab', T_FRONT, T2, H_TAB2, st))

    # leg: bracket hole on the middle tab hole; size + turn so the top lip meets the tube and the foot is on the ground
    ground = AX[1] + TYRE_R * S_W
    tip = leg_top_tip()
    def tipmiss(sl, L):
        q = to_handle(world(*L_HOLE1, *T2, L, *tip, sl)); return q[1] - tube_edges(q[0])[1] + 3
    best = None
    for sl in np.arange(1.0, 2.2, 0.01):
        try: L = root(lambda L: tipmiss(sl, L), -40, 40)
        except AssertionError: continue
        d = lowest(3, *T2, *L_HOLE1, L, sl)[1] - ground
        if best is None or abs(d) < abs(best[0]): best = (d, sl, L)
    d, sl, L = best
    pl[3] = (*T2, *L_HOLE1, L, sl)
    J.append(('leg stand', 'front hole of the bolt bracket', 'handle frame', 'hole in the middle under-tab (shared with the tray strip)', L_HOLE1, T2, H_TAB2, sl))
    tipW = world(*L_HOLE1, *T2, L, *tip, sl); tq = to_handle(tipW)
    J.append(('leg stand', 'flat top lip of the rear strut', 'handle frame', 'underside of the rear tube', tip, tipW, (float(tq[0]), tube_edges(tq[0])[1]), sl))
    return pl, J, (ground, lowest(3, *pl[3]))


pl, J, ground = layout()
R = R_H


if __name__ == '__main__':
    ORDER = [4, 5, 6, 1, 2, 3]          # back to front: tyre, hub, fork, tray, handle frame, leg (bracket flat on the tabs)
    kitlib.render(str(OUT / 'wheelbarrow_combined'), [(P[n], *pl[n]) for n in ORDER])
    kitlib.sheet(str(OUT / 'wheelbarrow_parts'), kitlib.load('wheelbarrow'), NAMES)
    js = []
    for j in J:
        d = dict(part=j[0], feature=j[1], joins_part=j[2], joins_feature=j[3], scale=round(float(j[7]), 3),
                 part_point=[round(float(v), 1) for v in j[4]], world_point=[round(float(v), 1) for v in j[5]],
                 joins_part_point=[round(float(v), 1) for v in j[6]])
        js.append(d)
    js.append(dict(part='handle frame', feature='whole part', scale=S_H, turn_degrees=R_H))
    (OUT / 'wheelbarrow_joints.json').write_text(json.dumps(js, indent=1))
    print('ground', ground, 'scales', S_H, S_W, S_F)
    for n in ORDER: print(NAMES[n], ['%.2f' % v for v in pl[n]])
    subprocess.run(['magick', str(kitlib.H / 'flat/wheelbarrow_full.png'), '-resize', 'x900',
                    '(', str(OUT / 'wheelbarrow_combined.png'), '-resize', 'x900', ')',
                    '+append', str(OUT / 'wheelbarrow_side.png')], check=True)
