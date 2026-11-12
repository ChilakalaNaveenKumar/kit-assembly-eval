# Road bike kit cut from the author's own bike illustration (art/bike_hairline.svg).
import xml.etree.ElementTree as ET
from pathlib import Path
SRC=Path(__file__).parent/'art'/'bike_hairline.svg'
ns='{http://www.w3.org/2000/svg}'; KEEP=('fill','stroke','stroke-width','stroke-dasharray','stroke-dashoffset','opacity')
_root=ET.parse(SRC).getroot(); _g={x.get('id'):x for x in _root.iter(ns+'g') if x.get('id')}
def _els(e, inh=None, skip=()):
    inh=dict(inh or {}); inh.update({k:v for k,v in e.attrib.items() if k in KEEP}); out=[]
    for c in e:
        if c.get('id') in skip: continue
        t=c.tag.replace(ns,'')
        if t=='g': out+=_els(c,inh,skip)
        elif t in('path','circle','line','rect','ellipse'):
            a=dict(inh); a.update({k:v for k,v in c.attrib.items() if k in KEEP})
            geo={k:v for k,v in c.attrib.items() if k not in KEEP and k!='id'}
            out.append(f'<{t} '+' '.join(f'{k}="{v}"' for k,v in {**geo,**a}.items())+'/>')
    return out
_fp=list(_g['frame'].iter(ns+'path'))
def _fr(idx): return [_els(ET.fromstring(f'<g xmlns="http://www.w3.org/2000/svg">{ET.tostring(_fp[i]).decode()}</g>'))[0] for i in idx]
RA=(316.5,488.5); FA=(1058.8,488.6); BB=(627.5,536.5); PE=(756.5,539.5)
CROWN=(942.0,235.4); STEM=(909.8,137.5); SEAT=(521.0,179.2)
PARTS={
 'frame':{'els':_fr([2,3,7,8,9,10,12,13,14,16])+_els(_g['derailleur']),'anchors':{'rear_eyelet':(317.0,489.3),'head_bottom':CROWN,'head_top':STEM,'seat_top':SEAT}},
 'handlebar':{'els':_fr([5,11,15,17]),'anchors':{'spacer_bottom':STEM}},
 'saddle':{'els':_fr([6]),'anchors':{'post_bottom':SEAT}},
 'rear_wheel':{'els':_els(_g['rear_wheel']),'anchors':{'hub':RA}},
 'front_wheel':{'els':_els(_g['front_wheel']),'anchors':{'hub':FA}},
 'fork':{'els':_fr([4]),'anchors':{'crown':CROWN,'tip':FA}},
 'cassette':{'els':_els(_g['cassette']),'anchors':{'centre':RA}},
 'chain':{'els':_els(_g['chain']),'anchors':{'front_centre':BB,'rear_centre':RA}},
 'chainring':{'els':_els(_g['chainring']),'anchors':{'centre':BB}},
 'crank':{'els':_els(_g['crank_arm'],skip=('pedal',)),'anchors':{'spindle':BB,'outer_end':PE}},
 'pedal':{'els':_els(_g['pedal']),'anchors':{'axle':PE}},
}
ROT={'fork':21.3,'crank':-91.3,'pedal':108.3,'chainring':-36.0,'handlebar':30.0,'saddle':-25.0,'chain':15.0,'cassette':10.0}
CANVAS=(1376,768); OBJECT='road bike (side view)'
UPRIGHT=('frame',3,'Frame upright: rotated at most 3 deg from how it is stored.')
JOINTS=[
 ("Rear wheel: its hub centre (the common centre of its tyre/rim circles) on the centre of the frame's small round rear-dropout eyelet",'rear_wheel','hub','frame','rear_eyelet',4),
 ("Cassette: concentric with the rear wheel hub",'cassette','centre','rear_wheel','hub',4),
 ("Chain: its small rear round end concentric with the cassette",'chain','rear_centre','cassette','centre',5),
 ("Chain: its large front round end concentric with the chainring",'chain','front_centre','chainring','centre',5),
 ("Crank arm: the centre of its large round spindle eye on the chainring centre",'crank','spindle','chainring','centre',4),
 ("Pedal: the centre of its round axle on the centre of the crank arm's rounded outer end",'pedal','axle','crank','outer_end',6),
 ("Fork: the centre of its top (crown) edge at the centre of the bottom end of the frame's head tube",'fork','crown','frame','head_bottom',6),
 ("Front wheel: its hub centre at the fork's bottom tip (the tip wraps around the hub)",'front_wheel','hub','fork','tip',6),
 ("Handlebar: the centre of the bottom edge of its green headset spacer on the centre of the top edge of the frame's head tube",'handlebar','spacer_bottom','frame','head_top',6),
 ("Saddle: the bottom edge of its seatpost collar sits on the top edge of the frame's seat tube, centred on it",'saddle','post_bottom','frame','seat_top',8),
]
EXTRA=[('level','Both wheels stand on level ground: front and rear hub centres at the same height','front_wheel','hub','rear_wheel','hub',4),
       ('angle',"Saddle: the collar's bottom edge lies flush along the seat tube's top edge (saddle orientation relative to the frame)",'saddle',6),
       ('angle',"Handlebar: the spacer's bottom edge lies flush along the head tube's top edge (handlebar orientation relative to the frame)",'handlebar',6)]
FREE_SPIN={'rear_wheel':RA,'front_wheel':FA,'cassette':RA}
FREE_ROTATION = {'chainring', 'crank', 'pedal'}  # turn with the pedalling, so any angle is a working bike
INTERCHANGEABLE = [('rear_wheel', 'front_wheel')]  # the two wheels differ only in a hub detail, so swapping them still builds a working bike
