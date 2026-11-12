"""Hand water pump: each part placed by its own holes and edges (kitlib parts, never scaled)."""
import json, subprocess
import numpy as np
import kitlib

M = 'hand_pump'
P = kitlib.load(M)
names = {1: 'base plate', 2: 'pump body', 3: 'spout', 4: 'cap', 5: 'handle lever', 6: 'link bar', 7: 'piston rod'}
out = kitlib.H / 'assembly'


def hole(n, near):
    """Detected hole of part n closest to an approximate crop point."""
    return min(P[n]['holes'], key=lambda h: (h[0] - near[0]) ** 2 + (h[1] - near[1]) ** 2)[:2]


def rows(n, x0, x1):
    """Top and bottom ink rows of part n within columns x0..x1."""
    ys = np.where(P[n]['fg'][:, x0:x1 + 1].any(1))[0]; return ys.min(), ys.max()


def cols(n, y0, y1):
    xs = np.where(P[n]['fg'][y0:y1 + 1].any(0))[0]; return xs.min(), xs.max()


place, joints = {}, []
def joint(a, fa, b, fb, pa, w):
    joints.append(dict(part=f'p{a:02d} {names[a]}', feature=fa, joins_part=f'p{b:02d} {names[b]}', joins_feature=fb,
                       part_point=[round(float(pa[0]), 1), round(float(pa[1]), 1)], world_point=[round(float(w[0]), 1), round(float(w[1]), 1)]))
def W(n, q):
    X, Y, px, py, rot = place[n]; return kitlib.world(px, py, X, Y, rot, *q)

# base plate at the origin; pedestal top centre
place[1] = (0, 0, 0, 0, 0)
bx0, bx1 = cols(1, 30, 60); ped = ((bx0 + bx1) / 2, rows(1, int(bx0) + 20, int(bx1) - 20)[0])

# body: bottom flange edge flush on the pedestal top, centred
fx0, fx1 = cols(2, 590, 605); body_bot = ((fx0 + fx1) / 2, rows(2, int(fx0) + 30, int(fx1) - 30)[1])
place[2] = (ped[0], ped[1], body_bot[0], body_bot[1], 0)
joint(2, 'bottom flange underside', 1, 'pedestal top face', body_bot, ped)
body_top = (body_bot[0], rows(2, int(fx0) + 30, int(fx1) - 30)[0])

# cap: skirt underside flush on the body's top flange, skirt centred on the body
sx0, sx1 = np.where(P[4]['fg'][260:291, :380].any(0))[0][[0, -1]];   # skirt only, lug excluded
skirt = ((sx0 + sx1) / 2, rows(4, int(sx0) + 10, int(sx1) - 10)[1])
place[4] = (*W(2, body_top), *skirt, 0)
joint(4, 'skirt underside', 2, 'top flange face', skirt, W(2, body_top))

# spout: flange face flush on the widest point of the upper bulge, just under the top flange (above the piston)
lx = cols(2, 70, 275)[0]
st = [y for y in range(70, 276) if cols(2, y, y)[0] == lx]
fl_x = P[3]['box'][2]; f0, f1 = rows(3, fl_x - 30, fl_x)
sp = (fl_x, (f0 + f1) / 2); bw = (lx, (st[0] + st[-1]) / 2)
# outlines meet stroke on stroke (vector stroke sits ~3 px inside the mask edge)
place[3] = (W(2, bw)[0] + 3, W(2, bw)[1], *sp, 0)
joint(3, 'flange face (right edge)', 2, 'widest point of upper bulge', sp, W(3, sp))

# link bar: lower eye on the cap lug's upper hole
lug_up = hole(4, (433, 192)); l_lo = hole(6, (64, 336)); l_hi = hole(6, (104, 64))
A = W(4, lug_up)
# handle: big end hole straight above the body centre (rod hangs there), small hole on the link's top eye
h_big = hole(5, (67, 116)); h_small = hole(5, (373, 116))
Lk = np.hypot(l_hi[0] - l_lo[0], l_hi[1] - l_lo[1]); Hd = h_small[0] - h_big[0]
rod_x = W(2, body_top)[0]
# keep the handle's hole line level: small hole at (rod_x + Hd, y), link length fixes y
Sx = rod_x + Hd; Sy = A[1] - np.sqrt(Lk ** 2 - (Sx - A[0]) ** 2)
link_rot = np.degrees(np.arctan2(Sy - A[1], Sx - A[0]) - np.arctan2(l_hi[1] - l_lo[1], l_hi[0] - l_lo[0]))
place[6] = (*A, *l_lo, link_rot)
joint(6, 'lower eye hole', 4, 'lug upper hole', l_lo, A)
hang = np.degrees(np.arctan2(h_small[1] - h_big[1], h_small[0] - h_big[0]))
place[5] = (rod_x, Sy, *h_big, -hang)
joint(5, 'small middle hole', 6, 'upper eye hole', h_small, W(5, h_small))
joint(6, 'upper eye hole', 5, 'small middle hole', l_hi, W(6, l_hi))

# piston rod: top eye on the handle's end hole, hanging straight down into the body
r_eye = hole(7, (71, 56))
place[7] = (*W(5, h_big), *r_eye, 0)
joint(7, 'top eye hole', 5, 'end hole (left)', r_eye, W(5, h_big))
rb = (r_eye[0], P[7]['box'][3])
joints.append(dict(part='p07 piston rod', feature='bottom piston (hidden inside)', joins_part='p02 pump body', joins_feature='bore, behind the body wall',
                   part_point=[float(rb[0]), float(rb[1])], world_point=[round(float(v), 1) for v in W(7, rb)]))

# back to front: handle, rod (behind cap and body), base, body, spout, cap, link on top of lug and handle
order = [5, 7, 1, 2, 3, 4, 6]
kitlib.render(str(out / 'hand_pump_combined'), [(P[n], *place[n]) for n in order])
kitlib.sheet(str(out / 'hand_pump_parts'), P, names)
(out / 'hand_pump_joints.json').write_text(json.dumps(joints, indent=1))
ref = kitlib.H / 'flat' / 'hand_pump_full.png'
subprocess.run(['magick', str(ref), '-resize', 'x1100', '(', str(out / 'hand_pump_combined.png'), '-resize', 'x1100', ')',
                '-background', 'white', '-splice', '20x0', '+append', str(out / 'hand_pump_side.png')], check=True)
for n in order: print(n, names[n], [round(float(v), 1) for v in place[n]])
