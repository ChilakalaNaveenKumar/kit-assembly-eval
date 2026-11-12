"""Balance scale combined from its kit parts (fcrops/scale + fsvg/scale) via kitlib; joints measured in crop pixels."""
import json, subprocess
import kitlib
from kitlib import world

P = kitlib.load('scale')
names = {1: 'base', 2: 'pillar', 3: 'beam', 4: 'pointer', 5: 'left stirrup', 6: 'right stirrup', 7: 'left pan', 8: 'right pan'}

# crop-pixel features
BEAM_HOLE = (269.6, 62.6)                     # centre pivot hole (kitlib hole)
EYE_DX, EYE_DY = 232.0, 40.0                  # beam end-curl eye centre, mirrored: +-EYE_DX from the pivot, EYE_DY below it
PILLAR_PIVOT = (87.5, 120)                    # top collar centre, just under the knob
PILLAR_FOOT = (87.5, 526)                     # foot bottom edge
BASE_TAB = (270, 27)                          # top edge of the centre tab
POINTER_TIP = (58, 25)                        # narrow top tip of the needle
POINTER_HUB = (58.3, 391.7)                   # hub pin hole
ROD = (122.5, 60)                             # stirrup: rod centre just under the hook's neck (identical on p05/p06)
CRADLE = (122.5, 495)                         # stirrup U: inner bottom where the rod meets it
PAN_FOOT = (259.0, 110)                       # pan: bottom edge of the centre foot (same on p07/p08)
SC = {1: 0.8, 2: 1.0, 3: 1.0, 4: 0.70, 5: 0.55, 6: 0.55, 7: 0.61, 8: 0.61}
HOOK_OFF = (0.0, 0.0)                           # stirrup rod offset from the eye centre so the hook threads the curl

joints, items = [], {}
def place(n, local, W, rot=0.0):
    items[n] = (P[n], W[0], W[1], local[0], local[1], rot, SC[n])
def at(n, q):
    _, X, Y, px, py, rot, s = items[n]; return world(px, py, X, Y, rot, *q, s)
def joint(a, fa, qa, b, fb):
    w = at(a, qa); joints.append(dict(part=names[a], scale=SC[a], feature=fa, joins_part=names[b], joins_feature=fb,
                                      part_point=[float(qa[0]), float(qa[1])], world_point=[round(float(w[0]), 1), round(float(w[1]), 1)]))

place(3, BEAM_HOLE, (0, 0))                                   # beam pivot is the world origin
place(2, PILLAR_PIVOT, (0, 0))
joint(3, 'centre pivot hole', BEAM_HOLE, 2, 'top collar centre under the knob')
place(1, BASE_TAB, at(2, PILLAR_FOOT))
joint(2, 'foot bottom edge', PILLAR_FOOT, 1, 'top edge of the centre tab')
place(4, POINTER_TIP, (0, 30))                              # rot 0: needle tip under the beam pivot, hub lower in front of the pillar
joint(4, 'narrow top tip', POINTER_TIP, 3, 'centre pivot hole (just below it)')
for s, pan, sg in ((5, 7, -1), (6, 8, 1)):
    place(s, ROD, (sg * EYE_DX, EYE_DY + HOOK_OFF[1]))
    joint(s, 'rod under the hook neck', ROD, 3, f'{"left" if sg < 0 else "right"} end curl eye (hook threads through it)')
    place(pan, PAN_FOOT, at(s, CRADLE))
    joint(pan, 'foot bottom edge under the centre tab', PAN_FOOT, s, 'U cradle inner bottom')

# back to front: pans, stirrups (U in front of the pans), base, pillar, pointer, beam in front of the hooks
ORDER = [7, 8, 1, 2, 4, 3, 5, 6]
kitlib.render(str(kitlib.H / 'assembly/scale_combined'), [items[n] for n in ORDER])
kitlib.sheet(str(kitlib.H / 'assembly/scale_parts'), P, names)
(kitlib.H / 'assembly/scale_joints.json').write_text(json.dumps(joints, indent=1))
A = kitlib.H / 'assembly'
subprocess.run(['magick', str(kitlib.H / 'flat/scale_full.png'), '-resize', 'x1000', '+repage', '(', str(A / 'scale_combined.png'), '-resize', 'x1000', ')',
                '-background', 'white', '-splice', '20x0', '+append', '+repage', str(A / 'scale_side.png')], check=True)
