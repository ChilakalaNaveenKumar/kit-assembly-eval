"""Desk lamp: every part placed by its own pin holes and edges (kitlib)."""
import json, math, sys
import kitlib
from kitlib import world as W

PLATE_ROT, SHADE_HOLE, SHADE_ROT, BULB_DEPTH = (float(sys.argv[1]), sys.argv[2], float(sys.argv[3]), float(sys.argv[4])) if len(sys.argv) > 4 else (170.0, 'A', 245.0, -16.0)
OUT = sys.argv[5] if len(sys.argv) > 5 else str(kitlib.H / 'assembly/desk_lamp_combined')
P = kitlib.load('desk_lamp')
names = {1: 'base', 2: 'L bracket', 3: 'lower arm', 4: 'elbow plate', 5: 'upper arm', 6: 'head plate', 7: 'shade', 8: 'bulb'}

# joint features, crop px
BASE_TOP = 106                                   # top edge of the base slab
BRK_FOOT, BRK_HOLE = (23, 191), (59.1, 66.6)     # bracket bottom-left corner, upright pin hole
ARM1 = {'low': (50.4, 424.4), 'high': (460.8, 51.2)}
ELB = {'A': (56.0, 56.4), 'B': (153.5, 113.8), 'C': (56.2, 170.4)}
ARM2 = {'low': (49.8, 460.3), 'high': (459.9, 51.7)}
HEAD = {'A': (55.3, 55.7), 'B': (153.5, 101.3), 'C': (69.3, 170.0)}
LUG = (426.2, 218.2)
SHADE_NECK, SHADE_MOUTH = (303, 189), (164, 335)  # mids of the cone's narrow end and of the mouth
BULB_TIP, BULB_GLASS = (40, 282), (215, 120)      # screw cap centre, glass centre

ang = lambda a, b: math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
dist = lambda a, b: math.hypot(b[0] - a[0], b[1] - a[1])

items, joints = [], []
def put(n, X, Y, px, py, rot):
    items.append((n, X, Y, px, py, rot)); return lambda q: tuple(round(float(v), 1) for v in W(px, py, X, Y, rot, *q))
def joint(a, fa, pa, b, fb, pb, w):
    joints.append(dict(part=names[a], feature=fa, joins_part=names[b], joins_feature=fb, part_point=list(pa), world_point=list(w)))

base = put(1, 0, 0, 0, 0, 0)
brk = put(2, 24 + 49, BASE_TOP + 3, *BRK_FOOT, 0)            # foot flush on the slab top (strokes merged)
joint(2, 'bottom edge of foot', BRK_FOOT, 1, 'top edge of slab', (24 + 49, BASE_TOP), brk(BRK_FOOT))
h1 = brk(BRK_HOLE)

rot3 = -130.6 - ang(ARM1['low'], ARM1['high'])                # lower arm leans up-left as in the reference
arm1 = put(3, *h1, *ARM1['low'], rot3)
joint(3, 'bottom end hole', ARM1['low'], 2, 'upright pin hole', BRK_HOLE, h1)
e1 = arm1(ARM1['high'])
joint(3, 'top end hole', ARM1['high'], 4, 'bottom hole', ELB['C'], e1)

elb = put(4, *e1, *ELB['C'], -47)
e2 = elb(ELB['B'])
rot5 = -44.8 - ang(ARM2['low'], ARM2['high'])
arm2 = put(5, *e2, *ARM2['low'], rot5)
joint(5, 'bottom end hole', ARM2['low'], 4, 'right hole', ELB['B'], e2)
u = arm2(ARM2['high'])
joint(5, 'top end hole', ARM2['high'], 6, 'arm hole', HEAD['C'], u)

head = put(6, *u, *HEAD['C'], PLATE_ROT)
s = head(HEAD[SHADE_HOLE])
shade = put(7, *s, *LUG, SHADE_ROT)
joint(7, 'lug hole', LUG, 6, f'hole {SHADE_HOLE}', HEAD[SHADE_HOLE], s)

ax = ang(SHADE_NECK, SHADE_MOUTH) + SHADE_ROT                  # shade axis in the world
neck = shade(SHADE_NECK)
tip = (neck[0] - BULB_DEPTH * math.cos(math.radians(ax)), neck[1] - BULB_DEPTH * math.sin(math.radians(ax)))  # cap starts just inside the cone, at its narrow end
bulb = put(8, *tip, *BULB_TIP, ax - ang(BULB_TIP, BULB_GLASS))
joint(8, 'screw cap', BULB_TIP, 7, 'socket at narrow end of cone', SHADE_NECK, bulb(BULB_TIP))

# back to front: arms behind bracket and plates; shade lug over the head plate; bulb in front, cap seated inside the cone
order = [3, 5, 1, 2, 4, 6, 7, 8]
by = {it[0]: it for it in items}
kitlib.render(OUT, [(P[n],) + by[n][1:] for n in order])
kitlib.sheet(str(kitlib.H / 'assembly/desk_lamp_parts'), P, names)
(kitlib.H / 'assembly/desk_lamp_joints.json').write_text(json.dumps(joints, indent=1))
