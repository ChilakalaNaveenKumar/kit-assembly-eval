# B · pulley · claude-opus-5-5 · trial 3

- Result: **PASS**, score 1.00, tags: pass
- Model version: `claude-opus-5-5`, response id: `msg_vrtx_011CgrVTFMTvuKLLjFQJdYJY`
- Started 2026-11-08T20:32:05-0500, finished 2026-11-08T20:34:16-0500, 131.7 s, attempts 1
- Tokens: input 6,683, output 12,585 (thinking not reported separately by this provider)
- Settings: `{"provider": "anthropic", "route": "vertex", "max_tokens": 128000, "thinking": {"type": "adaptive", "display": "summarized"}, "output_config": {"effort": "high"}}`, prompt sha256 `0eb4a228ba7e95b6b6657247f40030cf1c9e960d98e122abe06db12d8d862842`

## Failed checks

- none

## Thinking summary (as returned by the provider)

````text
I'm examining part p08, which looks like an overhead beam with hatching marks on top indicating a fixed ceiling support, with the hoist hanging below it—trying to work out if it represents the base structure.

Now I'm turning to p09, which appears to be a hanger or bracket: a stem ending in an axle hole (radius 9) with a small pink tab bearing a smaller hole (radius 4), attached to a crossbar-shaped foot that likely bolts to the underside of the beam. I'm working through the rotated coordinates to pin down the stem's direction and the foot's midpoint so I can understand how this piece connects the beam to the hanging mechanism.

I'm checking the foot thickness and where it meets the beam underside, trying to figure out the hatching direction. The hatch lines sit above the rect's top edge, which would normally indicate solid material above — suggesting this is a ceiling mount rather than ground, though I'm second-guessing since ground hatching usually goes below instead.

Now I'm concluding it's a ceiling-mounted beam, with the bracket part attaching to its bottom edge.

Looking at the other part now — a large rounded rectangle rotated 25°, with wedge-shaped corner notches, two semicircle notches on the long sides, a small rectangle notch, a center dividing line, and a pair of small holes. This looks like a crate or load component, roughly 220 units long based on its corner coordinates.

I'm measuring the second dimension now and getting about 146 units, giving a 220x146 rounded box. The small r4 holes sit near the top semicircle notch, suggesting they're lifting points like eyes for rigging the load — which makes me wonder if this load is meant to hang from the ceiling beam rather than sit on the ground.

Now I see another piece that looks like a hook, defined by a line segment and a large arc.

I'm tracing this path further and realizing with the pink-tinted thick stroke it's actually the rope — anchored at one of the lifting holes, wrapping down around a pulley wheel of radius 45 matching the groove on an earlier piece, then back up around a second wheel of radius 57.5 matching another piece's groove, before continuing on.

Now I'm looking at the other pieces: one is a gray U-shaped strap with two small holes at either end, likely a hanger connecting to a block, while another gray piece has a hole at one end and a rounded end at the other, roughly 80 units long — possibly a connecting link.

Piece p02 is a yellow strap with a larger axle hole at its rounded end and a smaller hole at the square end, matching the lower pulley's yellow color — this looks like the lower block's side strap holding the axle and the hook attachment. I'm also noting p09 as the upper block bracket housing the axle for the blue upper wheel, with p01 appearing green/blue as the load with notches, and now I'm tracing the rope path starting from its dead end hole.

The rope runs from its dead-end anchor down around the lower wheel's groove, back up over the upper wheel, then down as the free end — and I'm checking whether the pink tab with a hole near the bottom of p09's stem serves as the becket where the rope's dead end attaches, since its color matches the rope. I'm measuring distances between the tab hole, the axle hole, and the stem's foot edge to confirm the geometry fits.

Now I'm working through the actual arc geometry of the rope path in local coordinates, tracing the line segment that leads into the first arc and figuring out its direction vector and angle so I can determine where the arc's center sits, accounting for the sweep flag that dictates clockwise curvature in SVG's coordinate system.

Good, that confirms C1=(49.8,213.1). Now for the second arc from B to D, I'm computing the direction and using the sweep flag to find center C2=(155.3,62.3), verifying against endpoint E. Then I'm locating the dead-end anchor point at H=(112.56,123.37).

Looking at the p06 orientation stored at 35°, I check the vector between wheel centers C2-C1, which gives angle -55° rather than the expected -90° for vertical alignment, so I need to rotate p06 by -35° since the rope isn't part of the rotating assembly. I start setting up the rotation matrix to recompute positions after applying that -35° rotation.

Checking the rope direction from H down to the lower wheel tangent point — it's not vertical, but the exact angle doesn't matter much since this is just a drawn rope following the fixed geometry anyway.

Now looking at the lower block and hook pieces, I'm checking hole spacings to match parts together. The two holes on the load piece are 62 units apart, matching the stirrup's hole spacing — so these likely connect.

I'm also considering p03, which has one hole and a rounded end, as a connecting link: its hole could mate with p02's hole, while its rounded end attaches to the stirrup's curved bight. I need to figure out exactly where that rounded end lines up on the curve.

Looking again at p01's geometry, the top-edge semicircle and the centerline running down to the bottom semicircle center suggests p01 might actually be the load itself rather than a supporting part—perhaps a crate with corner wedges and lifting lugs near the top center, including a small rectangular notch cut into one corner.

I'm now tracing how the load connects to p07's bail: the U-shaped bail's holes attach to the load's top holes, with the legs extending upward from those holes. Working out the rotation, p07 is stored at 160°, so I need to rotate by -160° to get the legs pointing straight up in the assembly's frame.

Looking at what hooks into the bail's apex, I'm considering p03's rounded end and whether it's a hook tip, but the apex isn't an actual listed feature, so I'm reconsidering whether p03 might instead be a handle on the rope's free end — though that end isn't a hole either. Stepping back, I'm thinking the lower block likely has side straps, with p02 providing the axle hole at its rounded end and another hole at its square end.

Checking the rotation convention against each piece: p02's stored 125° matches rotating its axle-to-hole direction (215°) down to vertical, and p07's stored 160° places its U-shape legs pointing up with holes at the bottom. Now verifying p01's stored 25° against its long edge angle to confirm the pattern holds consistently across parts.

Computing the second hole's rotated position gives (31,-73), symmetric with the first, confirming both holes sit at roughly (±31,-73) relative to center. Then I'm finding the top edge's distance from center, which works out to about -83, so the holes sit a bit inside the top edge.

Now I'm working through piece p07's holes after a -160° rotation, applying the standard rotation formulas with cos160 and sin160 to get the transformed hole coordinates.

H1 lands at roughly (-60.12, -31.46) and H2 at (1.87, -31.46), confirming the holes sit horizontally 62 units apart, which matches the expected spacing.

Now I'm computing the midpoint of the bight's cubic curve using the Bezier midpoint formula, averaging the start point, control points weighted by 3, and the endpoint, then dividing by 8 to get the midpoint coordinates around (57.71, 73.4).

I'm trying to figure out which rounded end connects where—maybe p03's r4 hole links to p02, while the bail's pin role stays unclear since p07 lacks a center feature at the bight. Let me count up all the connection points across parts: p09's two holes, p05 and p04 hubs, p02's two holes, and p03's hole, to see how the assembly links together.

I need to pin down the exact y-coordinate for the rod's resting point within 4px tolerance — testing values like the bight stroke center versus the bearing edge, landing somewhere around -87.5 that satisfies both constraints.

The proper semicircle control length would be bigger than what's here, so this curve is flatter than a true arc, putting the apex about 17 above the P0-P3 line. I'll settle on roughly -87.7 for the seat position, a small offset from the apex to account for bearing.

Switching to check the hook orientation — the hole sits up top with the rounded end hanging down, which matches how a load would hang. Now I need to work out the chain's vertical layout: setting the upper axle center at some Y2, with the lower axle 184.05 below it.

I'm computing the becket position by rotating the hook's axle and becket hole coordinates by -140 degrees, finding the axle midpoint lands near (-3.00, -99.82) after transformation, and now working out the corresponding becket hole midpoint from its listed corner points.

So the foot's top edge sits 106 units above the axle, centered at x=-3. Now I'm working out the canvas placement: with a 1376x768 canvas and a 588-wide beam positioned at tx=394 (spanning 399-977), I can set the beam's underside at y=88 and solve for the foot group's translation so its rotated top edge lines up there, centering it horizontally around the canvas middle.

Now I'm checking the axle position (688, 193.99) and becket (688, 268.49), then computing the rope's rotation and translation so its transformed endpoint H lands close to the becket — getting (688.02, 268.54), a good match. I'm now recalculating the C1 and C2 rope points more precisely using the direction vector and length from point H.

Computing C2 and verifying against point E confirms the 57.5 distance checks out. Now I'm rotating both centers and point H by -35 degrees to align them into a common coordinate frame, getting their transformed x' and y' values, and I'm about to compute the vector from C2 to H in this rotated frame.

Cross-checking with the p09 reference transform, I calculate the axle position by rotating point A through 140 degrees using precise sine/cosine values, landing on axle coordinates around (687.997, 193.979), which lets me derive the rope translation offset.

Now I'm locating the hub centers for the lower and upper wheels from their hole points, then translating each wheel so its hub lands exactly at the corresponding axle position (688, 377.98) and (688, 193.98), confirming the rope groove radius lines up with the wheel radii.

For part p02, I'm rotating it -125° about axle C1: computing the axle hole center and a reference hole center, applying the rotation matrix, and verifying the two rotated points fall 72 units apart as expected before working out the final translation offset.

Now moving to p03, rotating it -55°: finding the hole center and the rounded-end arc's midpoint (confirming the two arc endpoints are diametrically opposed at radius 6), then applying the same rotation matrix to these coordinates.

Translating p03 so the computed hole/end positions land at the target bail location, yielding an end point around (688.0, 530.73). Then for p07, I'm working out the seat position relative to the bail's hole line using the earlier rotated local coordinates, solving for the translation offsets to place the seat correctly.

Now I'm working through p01's rotation, computing the midpoints of its two hole pairs and applying the -25° rotation matrix to find their transformed positions, getting hole1 near (159.2, -17...).

Continuing the translation, hole2 lands at x=719.01, matching the target exactly, which confirms the 62.0 separation is correct. I then check that the load bottom clears the 768 boundary and verify the rope's free end position translates to roughly (862, 606), which looks fine.

Checking C2 y-coordinate puts it at 136 with beam bottom at 88, both within range, and foot widths for p09 look fine too. Ready to output.


````

## Answer

````text
This assembles the kit as a two-wheel hoist hanging from a ceiling beam:

- **kit-p08** is the base: an overhead beam. The hatching above it marks the fixed ceiling.
- **kit-p09** is the upper bracket. Its foot bolts to the underside of the beam. It carries the upper wheel's axle and a rope anchor (becket) below the axle.
- **kit-p05** is the upper wheel (groove radius about 57) and **kit-p04** is the lower wheel (groove radius about 45).
- **kit-p06** is the rope:
  - its dead end is pinned at the becket on p09;
  - it runs under the lower wheel and over the upper wheel;
  - its free end hangs down.
- **kit-p02** is the lower block strap. Its large hole is the lower axle, and its small hole carries the hook link.
- **kit-p03** is the hook link. Its rounded end sits in the bight of the bail.
- **kit-p07** is the bail, pinned to the two lifting holes on the load.
- **kit-p01** is the load.

The rope's geometry fixes the layout:
- The upper and lower wheel centres are 184 px apart, one directly above the other.
- The rope's anchor point is 74.5 px below the upper axle. This matches the distance from the axle to the becket on p09.

One placement is a judgement call. The bail p07 has no marked feature at its bight. I placed the rounded end of p03 about 1 px below the centre line of the bail's apex, near where it would bear on the inside of the bend. This puts it within tolerance of either reading of that contact point.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1376 768">
  <use href="#kit-p08" transform="translate(394,20)"/>
  <use href="#kit-p09" transform="translate(691,293.8) rotate(-140)"/>
  <use href="#kit-p05" transform="translate(619.06,125.04)"/>
  <use href="#kit-p06" transform="translate(525.04,231.98) rotate(-35)"/>
  <use href="#kit-p04" transform="translate(631.05,321.03)"/>
  <use href="#kit-p02" transform="translate(680.26,485.37) rotate(-125)"/>
  <use href="#kit-p03" transform="translate(633.80,506.10) rotate(-55)"/>
  <use href="#kit-p07" transform="translate(717.13,618.43) rotate(-160)"/>
  <use href="#kit-p01" transform="translate(497.78,604.20) rotate(-25)"/>
</svg>
```
````

## Prompt

````text
Below is a kit of 9 SVG parts for a two-wheel pulley hoist (side view). Each part is a <g id="kit-..."> drawn in its own local coordinate system, stored at an arbitrary rotation. The parts are unlabelled (ids p01 to p09); work out what each one is from its drawing.

Assemble the parts into one complete, working two-wheel pulley hoist (side view) on a 1376 x 768 canvas. Parts are rigid: translate and rotate only, no scaling and no mirroring. Use every part exactly once. The base part, kit-p08, stays upright exactly as stored (at most 3 degrees of rotation).

Nobody will tell you which part connects to which, at which hole or feature, or which way round a part goes. Work that out from the parts, as a practitioner who knows this object would.

Grading is done by code on where the parts land:
- every connection the real object has must be made: the matching features of the two connected parts (pin holes, axle holes, bolt holes, hub centres, the centres of rounded ends, seats) must coincide within 4 px;
- a part that slides along a guide (such as a piston in its bore) must sit on the guide's centre line, within 4 px;
- every part must face the way it does on the working object, relative to the base part, within 8 degrees; parts that turn in use (wheels, gears, sprockets, cranks, connecting rods, pedals, rotors) may sit at any angle;
- anything that stands on the ground must stand level, within 4 px;
- a missing, duplicated, scaled, skewed or mirrored part fails the assembly.

Reply with one <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1376 768"> that contains exactly one <use href="#kit-ID" transform="..."/> per part. You may wrap <use> elements in <g transform="..."> groups. Do not copy the part drawings: the kit's <defs> are inserted automatically.

KIT:
<svg xmlns="http://www.w3.org/2000/svg"><defs>
<g id="kit-p01" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 84.2177093193,9.22618261741 L 283.605422467,102.2022002 A 10,10 25 0,1 288.44231772,115.491460688 L 226.740051506,247.812397595 A 10,10 25 0,1 213.450791018,252.649292848 L 14.0630778704,159.673275265 A 10,10 25 0,1 9.22618261741,146.384014778 L 70.9284488315,14.0630778704 A 10,10 25 0,1 84.2177093193,9.22618261741 Z" fill="#DFF1E3" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 75.154631449,5 L 103.250172847,18.101166114 A 31,31 25 0,1 62.053465335,33.0955413981 Z" fill="#DBEAF7" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 292.668500338,106.428382818 L 264.57295894,93.3272167038 A 31,31 25 0,0 279.567334224,134.523924216 Z" fill="#DBEAF7" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 5,155.447092648 L 33.0955413981,168.548258762 A 31,31 25 0,0 18.101166114,127.35155125 Z" fill="#DBEAF7" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 222.513868889,256.875475466 L 194.418327491,243.774309352 A 31,31 25 0,1 235.615035003,228.779934068 Z" fill="#DBEAF7" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 155.816024495,42.6130252949 A 31,31 25 0,0 212.007107291,68.8153575228 Z" fill="#DBEAF7" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 85.6613930463,193.060117943 A 31,31 25 0,1 141.852475843,219.262450171 Z" fill="#DBEAF7" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 116.844789653,24.4404400401 L 140.408792116,35.4285148453 L 120.968352076,77.118673049 L 97.4043496126,66.1305982438 Z" fill="#DBEAF7" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 183.911565893,55.7141914089 L 113.756934444,206.161284057" fill="none" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 155.215073026,53.3665762123 A 4,4 25 0,1 149.899368831,55.3013343134 A 4,4 25 0,1 147.96461073,49.9856301183 A 4,4 25 0,1 153.280314925,48.0508720171 A 4,4 25 0,1 155.215073026,53.3665762123 Z" fill="#F8F7F2"/>
  <path d="M 211.406155822,79.5689084402 A 4,4 25 0,1 206.090451627,81.5036665414 A 4,4 25 0,1 204.155693526,76.1879623462 A 4,4 25 0,1 209.471397721,74.2532042451 A 4,4 25 0,1 211.406155822,79.5689084402 Z" fill="#F8F7F2"/>
</g>
<g id="kit-p02" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 31.3960668461,6.40597930804 L 95.2899263006,51.1449413434 A 20.5,20.5 125 0,1 71.7732924102,84.7301751593 L 7.87943295567,39.9912131239 Q 2.96452068993,36.5497545058 6.40597930804,31.63484224 L 23.0396959622,7.87943295567 Q 26.4811545803,2.96452068993 31.3960668461,6.40597930804 Z" fill="#FDF1C9" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 78.3694214282,75.3099266499 A 9,9 125 0,1 76.1592409568,62.7753703242 A 9,9 125 0,1 88.6937972826,60.5651898527 A 9,9 125 0,1 90.903977754,73.0997461785 A 9,9 125 0,1 78.3694214282,75.3099266499 Z" fill="#F8F7F2"/>
  <path d="M 22.2583564212,29.9166630112 A 4,4 125 0,1 21.2760539894,24.3457490887 A 4,4 125 0,1 26.846967912,23.3634466569 A 4,4 125 0,1 27.8292703438,28.9343605795 A 4,4 125 0,1 22.2583564212,29.9166630112 Z" fill="#F8F7F2"/>
</g>
<g id="kit-p03" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 76.8905236535,5 L 7.46738789997,53.6106029808 A 6,6 55 0,0 14.3503051362,63.4404275122 L 83.7734408897,14.8298245315 Z" fill="#ECEAE4" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 79.3496798398,15.4858261883 A 4,4 55 0,1 73.7787659173,14.5035237565 A 4,4 55 0,1 74.761068349,8.93260983398 A 4,4 55 0,1 80.3319822716,9.91491226573 A 4,4 55 0,1 79.3496798398,15.4858261883 Z" fill="#F8F7F2"/>
</g>
<g id="kit-p04" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 39.1654600693,105.814523803 A 52,52 110 0,1 8.08649124139,39.1654600693 A 52,52 110 0,1 74.7355549752,8.08649124139 A 52,52 110 0,1 105.814523803,74.7355549752 A 52,52 110 0,1 39.1654600693,105.814523803 Z" fill="#FDF1C9" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 43.9537420759,92.6588271121 A 38,38 110 0,1 21.2421879324,43.9537420759 A 38,38 110 0,1 69.9472729686,21.2421879324 A 38,38 110 0,1 92.6588271121,69.9472729686 A 38,38 110 0,1 43.9537420759,92.6588271121 Z" fill="#FDF1C9" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 53.8723262323,65.4077411093 A 9,9 110 0,1 48.4932739352,53.8723262323 A 9,9 110 0,1 60.0286888122,48.4932739352 A 9,9 110 0,1 65.4077411093,60.0286888122 A 9,9 110 0,1 53.8723262323,65.4077411093 Z" fill="#F8F7F2"/>
</g>
<g id="kit-p05" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 90.8283753541,129.079413912 A 64,64 70 0,1 8.79875845094,90.8283753541 A 64,64 70 0,1 47.0497970084,8.79875845094 A 64,64 70 0,1 129.079413912,47.0497970084 A 64,64 70 0,1 90.8283753541,129.079413912 Z" fill="#DBEAF7" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 86.0400933475,115.923717221 A 50,50 70 0,1 21.9544551419,86.0400933475 A 50,50 70 0,1 51.838079015,21.9544551419 A 50,50 70 0,1 115.923717221,51.838079015 A 50,50 70 0,1 86.0400933475,115.923717221 Z" fill="#DBEAF7" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 72.0172674712,77.3963197683 A 9,9 70 0,1 60.4818525942,72.0172674712 A 9,9 70 0,1 65.8609048913,60.4818525942 A 9,9 70 0,1 77.3963197683,65.8609048913 A 9,9 70 0,1 72.0172674712,77.3963197683 Z" fill="#F8F7F2"/>
</g>
<g id="kit-p06" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 112.55585817,123.366588224 L 93.9612808915,221.445558043 A 45,45 35 1,1 11.2191650428,189.816597186 L 106.054617793,32.6350093851 A 57.5,57.5 35 0,1 209.491978553,81.5248742758 L 61.5062666074,499.632703096" fill="none" stroke="#1F2A3A" stroke-width="17"/>
  <path d="M 112.55585817,123.366588224 L 93.9612808915,221.445558043 A 45,45 35 1,1 11.2191650428,189.816597186 L 106.054617793,32.6350093851 A 57.5,57.5 35 0,1 209.491978553,81.5248742758 L 61.5062666074,499.632703096" fill="none" stroke="#FEB8A7" stroke-width="9"/>
  <path d="M 115.832466347,125.660893969 A 4,4 35 0,1 110.261552424,126.643196401 A 4,4 35 0,1 109.279249992,121.072282478 A 4,4 35 0,1 114.850163915,120.089980047 A 4,4 35 0,1 115.832466347,125.660893969 Z" fill="#F8F7F2"/>
</g>
<g id="kit-p07" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 67.2571353751,8.99619288633 L 80.9379411081,46.5838977178 C 88.8044044046,68.1968279958 30.5434619158,89.402076882 22.6769986194,67.789146604 L 8.99619288633,30.2014417725" fill="none" stroke="#1F2A3A" stroke-width="17"/>
  <path d="M 67.2571353751,8.99619288633 L 80.9379411081,46.5838977178 C 88.8044044046,68.1968279958 30.5434619158,89.402076882 22.6769986194,67.789146604 L 8.99619288633,30.2014417725" fill="none" stroke="#ECEAE4" stroke-width="9"/>
  <path d="M 63.4983648919,10.3642734596 A 4,4 160 0,1 65.8890548018,5.23742240318 A 4,4 160 0,1 71.0159058582,7.62811231302 A 4,4 160 0,1 68.6252159484,12.7549633695 A 4,4 160 0,1 63.4983648919,10.3642734596 Z" fill="#F8F7F2"/>
  <path d="M 5.23742240318,31.5695223458 A 4,4 160 0,1 7.62811231302,26.4426712894 A 4,4 160 0,1 12.7549633695,28.8333611992 A 4,4 160 0,1 10.3642734596,33.9602122557 A 4,4 160 0,1 5.23742240318,31.5695223458 Z" fill="#F8F7F2"/>
</g>
<g id="kit-p08" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 5,21 L 583,21 L 583,68 L 5,68 Z" fill="#ECEAE4"/>
  <path d="M 5,21 L 583,21" fill="none" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 5,68 L 583,68" fill="none" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 11,21 L 27,5" fill="none" stroke="#1F2A3A" stroke-width="3"/>
  <path d="M 45,21 L 61,5" fill="none" stroke="#1F2A3A" stroke-width="3"/>
  <path d="M 79,21 L 95,5" fill="none" stroke="#1F2A3A" stroke-width="3"/>
  <path d="M 113,21 L 129,5" fill="none" stroke="#1F2A3A" stroke-width="3"/>
  <path d="M 147,21 L 163,5" fill="none" stroke="#1F2A3A" stroke-width="3"/>
  <path d="M 181,21 L 197,5" fill="none" stroke="#1F2A3A" stroke-width="3"/>
  <path d="M 215,21 L 231,5" fill="none" stroke="#1F2A3A" stroke-width="3"/>
  <path d="M 249,21 L 265,5" fill="none" stroke="#1F2A3A" stroke-width="3"/>
  <path d="M 283,21 L 299,5" fill="none" stroke="#1F2A3A" stroke-width="3"/>
  <path d="M 317,21 L 333,5" fill="none" stroke="#1F2A3A" stroke-width="3"/>
  <path d="M 351,21 L 367,5" fill="none" stroke="#1F2A3A" stroke-width="3"/>
  <path d="M 385,21 L 401,5" fill="none" stroke="#1F2A3A" stroke-width="3"/>
  <path d="M 419,21 L 435,5" fill="none" stroke="#1F2A3A" stroke-width="3"/>
  <path d="M 453,21 L 469,5" fill="none" stroke="#1F2A3A" stroke-width="3"/>
  <path d="M 487,21 L 503,5" fill="none" stroke="#1F2A3A" stroke-width="3"/>
  <path d="M 521,21 L 537,5" fill="none" stroke="#1F2A3A" stroke-width="3"/>
  <path d="M 555,21 L 571,5" fill="none" stroke="#1F2A3A" stroke-width="3"/>
</g>
<g id="kit-p09" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 191.286436542,108.171411568 L 77.9118589606,203.303977802 L 72.7695580831,197.175622257 Q 68.912832425,192.579355598 74.2751435269,188.07984233 L 101.086699036,165.582275991 L 13.5615703486,30.1594128986 L 31.9466369834,14.7325102662 L 150.113543396,124.443868971 L 176.925098905,101.946302632 Q 182.287410007,97.4467893646 186.144135665,102.043056023 Z" fill="#EBE3F7" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 59.5692611366,80.3220722017 A 9,9 140 0,1 60.6785726375,67.6425837264 A 9,9 140 0,1 73.3580611127,68.7518952273 A 9,9 140 0,1 72.2487496119,81.4313837026 A 9,9 140 0,1 59.5692611366,80.3220722017 Z" fill="#F8F7F2"/>
  <path d="M 30.0315258756,16.3394792904 L 15.4766814564,28.5524438744 A 6,6 140 0,1 7.02368913952,27.8129028738 L 6.38090152984,27.0468584307 A 6,6 140 0,1 7.12044253043,18.5938661139 L 21.6752869497,6.38090152984 A 6,6 140 0,1 30.1282792665,7.12044253043 L 30.7710668762,7.88648697355 A 6,6 140 0,1 30.0315258756,16.3394792904 Z" fill="#FEB8A7" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 15.5118064305,20.0378231409 A 4,4 140 0,1 16.0048337643,14.4024949297 A 4,4 140 0,1 21.6401619755,14.8955222634 A 4,4 140 0,1 21.1471346418,20.5308504746 A 4,4 140 0,1 15.5118064305,20.0378231409 Z" fill="#F8F7F2"/>
</g>
</defs></svg>
````
