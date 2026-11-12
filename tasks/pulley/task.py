# Ported from the author's pulley drawing (art/pulley_hairline.svg); pins re-centred, movable wheel shrunk and rope recomputed so every attach point is exact.
import math
from kitbench.draw import hole

INK = '#1F2A3A'
def S(tag, fill='none', sw='4', stroke=INK, **geo):
    a = ' '.join(f'{k.replace("_", "-")}="{v}"' for k, v in geo.items())
    st = '' if stroke is None else f' stroke="{stroke}" stroke-width="{sw}"'
    return f'<{tag} {a} fill="{fill}"{st}/>'
def thick(d, inner): return [S('path', d=d, sw='17'), S('path', d=d, sw='9', stroke=inner)]

F = (688.0, 194.0); M = (688.0, 378.0)          # fixed / movable wheel axles
R1, R2 = 57.5, 45.0                              # rope radius in each wheel groove
D = (688.0, 268.5)                               # rope dead end: eye hole at the centre of the bracket collar
E = (862.0, 606.0)                               # rope free end

def _cw_dir(t): return (-math.sin(t), math.cos(t))       # travel direction going clockwise (screen) at angle t
def _on(c, r, t): return (c[0]+r*math.cos(t), c[1]+r*math.sin(t))
def _tan_from(P, c, r, leaving):
    """angle t on circle c where a line through P is tangent with clockwise travel (arriving from P, or leaving towards P)"""
    dx, dy = P[0]-c[0], P[1]-c[1]; d = math.hypot(dx, dy); base = math.atan2(dy, dx); off = math.acos(r/d)
    for t in (base+off, base-off):
        T = _on(c, r, t); u = _cw_dir(t); v = (P[0]-T[0], P[1]-T[1]) if leaving else (T[0]-P[0], T[1]-P[1])
        if u[0]*v[0]+u[1]*v[1] > 0: return t
t1 = _tan_from(D, M, R2, leaving=False)                   # dead end -> right side of movable wheel
s = (R1-R2)/math.hypot(F[0]-M[0], F[1]-M[1]); t2 = math.pi - math.asin(s)   # left run, common tangent of both wheels
t4 = _tan_from(E, F, R1, leaving=True)                    # over the fixed wheel -> free end
T1, T2, T3, T4 = _on(M, R2, t1), _on(M, R2, t2), _on(F, R1, t2), _on(F, R1, t4)
def _large(a, b): return 1 if ((b-a) % (2*math.pi)) > math.pi else 0
def g(p): return f'{p[0]:.3f} {p[1]:.3f}'
ROPE_D = (f'M{g(D)} L{g(T1)} A{R2} {R2} 0 {_large(t1, t2)} 1 {g(T2)} L{g(T3)} '
          f'A{R1} {R1} 0 {_large(t2, t4)} 1 {g(T4)} L{g(E)}')

HOOK_D = 'M682 446 V530.75 A6 6 0 0 0 694 530.75 V446 Z'   # hook turned 90 deg to the shackle, so seen edge-on
SHACKLE_D = 'M657 571 V531 C657 508 719 508 719 531 V571'   # crown centreline top at (688, 513.75)
CURL_IN = (688.0, 530.75-8.5)    # inner edge of the hook curl's low point (rope-like stroke is 17 wide)
CROWN_IN = (688.0, 513.75+8.5)   # inner edge of the shackle bow's top

PARTS = {
 'beam': {'els': [S('rect', fill='#ECEAE4', stroke=None, x=399, y=41, width=578, height=47),
                  S('line', x1=399, y1=41, x2=977, y2=41), S('line', x1=399, y1=88, x2=977, y2=88)] +
                 [S('line', sw='3', x1=x, y1=41, x2=x+16, y2=25) for x in range(405, 966, 34)],
          'anchors': {'underside_left': (473.0, 88.0), 'underside_right': (903.0, 88.0)}},
 'rope': {'els': thick(ROPE_D, '#FEB8A7') + [hole(D, 4)],
          'anchors': {'upper_arc_centre': F, 'lower_arc_centre': M, 'dead_end': D}},
 'fixed_wheel': {'els': [S('circle', fill='#DBEAF7', cx=688, cy=194, r=64), S('circle', fill='#DBEAF7', cx=688, cy=194, r=50),
                         hole(F, 9)],
                 'anchors': {'axle': F}},
 'bracket': {'els': [S('path', fill='#EBE3F7', d='M614 88 H762 V96 Q762 102 755 102 H720 L700 262 H676 L656 102 H621 Q614 102 614 96 Z'),
                     hole(F, 9),   # was cx=688 cy=191 in the original: moved 3 px to be concentric with the wheel
                     S('rect', fill='#FEB8A7', x=672.5, y=262, width=31, height=13, rx=6), hole(D, 4)],
             'anchors': {'top_centre': (688.0, 88.0), 'pin': F, 'collar_bottom': D}},
 'movable_wheel': {'els': [S('circle', fill='#FDF1C9', cx=688, cy=378, r=52), S('circle', fill='#FDF1C9', cx=688, cy=378, r=38),
                           hole(M, 9)],
                   'anchors': {'axle': M}},
 'box': {'els': [S('rect', fill='#DFF1E3', x=568, y=561, width=240, height=166, rx=10),
                 S('path', fill='#DBEAF7', d='M568 561 H599 A31 31 0 0 1 568 592 Z'),
                 S('path', fill='#DBEAF7', d='M808 561 H777 A31 31 0 0 0 808 592 Z'),
                 S('path', fill='#DBEAF7', d='M568 727 H599 A31 31 0 0 0 568 696 Z'),
                 S('path', fill='#DBEAF7', d='M808 727 H777 A31 31 0 0 1 808 696 Z'),
                 S('path', fill='#DBEAF7', d='M657 561 A31 31 0 0 0 719 561 Z'),
                 S('path', fill='#DBEAF7', d='M657 727 A31 31 0 0 1 719 727 Z'),
                 S('rect', fill='#DBEAF7', x=614, y=561, width=26, height=46),
                 S('line', x1=688, y1=561, x2=688, y2=727), hole((657.0, 571.0), 4), hole((719.0, 571.0), 4)],
         'anchors': {'lug_left_hole': (657.0, 571.0), 'lug_right_hole': (719.0, 571.0)}},
 'shackle': {'els': thick(SHACKLE_D, '#ECEAE4') + [hole((657.0, 571.0), 4), hole((719.0, 571.0), 4)],
             'anchors': {'crown_inner_top': CROWN_IN, 'leg_a_hole': (657.0, 571.0), 'leg_b_hole': (719.0, 571.0)}},
 'hook': {'els': [S('path', fill='#ECEAE4', d=HOOK_D)] + [hole((688.0, 450.0), 4)], 'anchors': {'eye_top': (688.0, 450.0), 'curl_inner_bottom': CURL_IN, 'visible_bottom': (688.0, 539.25)}},
 'strap': {'els': [S('path', fill='#FDF1C9', d='M667.5 456 V378 A20.5 20.5 0 0 1 708.5 378 V456 Q708.5 462 702.5 462 H673.5 Q667.5 462 667.5 456 Z'),
                   hole(M, 9), hole((688.0, 450.0), 4)],   # was cx=688 cy=381 in the original: moved 3 px to be concentric with the wheel
           'anchors': {'pin': M, 'hook_hole': (688.0, 450.0)}},
}
ROT = {'beam': 0, 'rope': 35, 'fixed_wheel': 70, 'bracket': 140, 'movable_wheel': 110, 'strap': 125, 'hook': 55, 'shackle': 160, 'box': 25}
CANVAS = (1376, 768); OBJECT = 'two-wheel pulley hoist (side view)'
UPRIGHT = ('beam', 3, 'Ceiling beam upright, hatching on top: rotated at most 3 deg from how it is stored.')
JOINTS = [
 ("Fixed (larger, blue) pulley wheel: its hub hole on the bracket's axle hole", 'fixed_wheel', 'axle', 'bracket', 'pin', 4),
 ("Rope: its larger wrap arc (the one that goes over the top) concentric with the fixed wheel's hub", 'rope', 'upper_arc_centre', 'fixed_wheel', 'axle', 4),
 ("Rope: the hole in its short dead end (the end next to the smaller arc) on the hole in the bracket's pink collar", 'rope', 'dead_end', 'bracket', 'collar_bottom', 4),
 ("Movable (smaller, cream) pulley wheel: its hub hole concentric with the rope's smaller wrap arc, which goes under it", 'movable_wheel', 'axle', 'rope', 'lower_arc_centre', 4),
 ("Strap: the hole in its rounded top end on the movable wheel's hub hole", 'strap', 'pin', 'movable_wheel', 'axle', 4),
 ("Hook: the hole in its straight top end on the small hole near the strap's bottom", 'hook', 'eye_top', 'strap', 'hook_hole', 4),
 ("Box: one of the two small holes flanking the blue half-disc on its lid under the hole at one shackle leg end", 'box', 'lug_left_hole', 'shackle', 'leg_a_hole', 4),
 ("Box: the other small lid hole under the hole at the other shackle leg end", 'box', 'lug_right_hole', 'shackle', 'leg_b_hole', 4),
]
EXTRA = [
 ('online', "Shackle: the inner edge of its bow's top rests on the hook's lowest part (anywhere from the inside of the hook's curl down to its visible bottom), so the bow hangs on the hook", 'shackle', 'crown_inner_top', 'hook', 'curl_inner_bottom', 'visible_bottom', 4),
 ('online', "Bracket: the centre of its wide top plate's upper edge on the beam's underside, anywhere along it with the whole plate under the beam", 'bracket', 'top_centre', 'beam', 'underside_left', 'underside_right', 4),
 ('angle', 'Bracket: hangs straight down from the beam, top plate flat against the beam (orientation relative to the beam)', 'bracket', 6),
 ('angle', 'Strap: hangs straight down below the movable wheel hub, rounded end up (orientation relative to the beam)', 'strap', 6),
 ('angle', 'Hook: hangs straight down from the strap, curl at the bottom (orientation relative to the beam)', 'hook', 6),
 ('angle', 'Shackle: hangs straight down, bow up, legs vertical (orientation relative to the beam)', 'shackle', 6),
 ('angle', 'Box: hangs level and right way up, the small blue label strip at the top (orientation relative to the beam)', 'box', 6),
]
FREE_SPIN = {'fixed_wheel': F, 'movable_wheel': M}
