# A · pulley · claude-opus-5-5 · trial 1

- Result: **PASS**, score 1.00, tags: pass
- Model version: `claude-opus-5-5`, response id: `msg_vrtx_011CgrVTFh4ALSqGkiZNheXB`
- Started 2026-11-08T20:32:05-0500, finished 2026-11-08T20:33:43-0500, 98.7 s, attempts 1
- Tokens: input 6,671, output 9,862 (thinking not reported separately by this provider)
- Settings: `{"provider": "anthropic", "route": "vertex", "max_tokens": 128000, "thinking": {"type": "adaptive", "display": "summarized"}, "output_config": {"effort": "high"}}`, prompt sha256 `fb51e84f957061389e1cf34461222a2bdcfd9c392286360d6e86ad372bca9ca1`

## Failed checks

- none

## Thinking summary (as returned by the provider)

````text
I'm working out the geometry of the ceiling beam and the bracket hanging from it, figuring out the coordinates for the beam's hatched top edge and locating the center of the bracket's mounting hole from its surrounding points.

The larger hole center around (66.5, 74.5) sits along the bracket's diagonal stem connecting the small pink mounting tab to the main crossbar, confirming the bracket is a T-shaped hanger — a stem with a bolt hole running down to a flange where it attaches to something else, with the pink tab serving as the seat against the beam.

Now I'm checking the rotation convention for each part: beam at 0°, box 25°, bracket 140°, fixed wheel 70°, hook 55°, movable wheel 110°, rope 35°, shackle 160°, strap 125°. I'm figuring out whether these stored angles correspond directly to rotation parameters I'd need to reverse to get the canonical upright orientation, checking the bracket's stem angle to see if it matches.

For the box, I'm examining the lifting points and corner protectors to figure out where the lug attaches in its canonical (unrotated) orientation.

I confirm the other diagonal pair also averages to the same center, (148.8,130.9), so that's solid. Now I'm rotating one corner vector by -25° around that center to get its canonical position, working through the cosine/sine math to land on roughly (-120,-83).

Continuing the rotation for the opposite corner, I land on (120,-83), giving a top edge at y=-83 spanning the full width. Then I rotate the lug rectangle's center and find it sits at about (-61,-60), and I start rotating the hole coordinates too, getting the first hole to around (-31,-73).

Rotating the second hole, I get roughly (31,-73), so the two holes sit symmetrically at x=±31 just inside the top edge. Then I trace the arc endpoints and find they land at (-31,-83) and (31,-83) with a radius of 31, suggesting a semicircular lug centered at (0,-83) — I'm working out which way it bulges based on the sweep flag and hole placement before moving to the next line segment.

Rotating the leg direction by -160° brings it to roughly -90°, meaning the shackle's U bend arches upward above the pin holes, with the bow at top and pins at bottom going into the box. Now I'm checking the hook piece — it's a thin bar with a rounded end and a hole centered around (77.05,12.21), likely meant to catch onto the shackle's bow.

The strap has a big hole (r9, center ~83.5,67.9) and small hole (r4, center ~24.6,26.6), distance 72 apart, rotated so the big hole sits on top with the small hole below. This strap looks like the movable pulley's hanger — the wheel axle at top, with the small hole below connecting to the hook's own hole.

Now I'm checking the hook: it extends 80.7 down to a rounded end, which should seat into the shackle bow. I'm computing the midpoint of the shackle's bezier curve to find where that U-shaped arc sits, working out the coordinates at t=0.5.

I'll use the apex centerline as the reference point, then verify consistency against the rope geometry - checking the anchor hole position, the line to the movable wheel groove (radius between its inner and outer bounds), and the arc toward the fixed wheel.

This confirms a classic pulley setup: the rope's dead end fixes to the bracket tab, routes down and around the movable wheel, back up and over the fixed wheel, then down to the free pulling end. Now I'm calculating the arc centers by finding tangent directions from the line segments bordering each arc, starting with the segment leading into the first wheel's radius-45 arc.

Computing the radius vector gives (0.9825, 0.1863), so the center works out to (49.75, 213.07), and checking against P2 confirms a distance of 45, matching the radius. Now I'm moving to the second arc, computing the direction from the previous line segment to set up for finding its center next.

Rotating into canonical rope orientation, I find the movable wheel sits exactly 184 units directly below the fixed wheel center, and the anchor hole ends up about 74.5 units directly below it too — a nice simplification.

Now checking the bracket's axle hole to tab hole distance, I get sqrt(5549.5) ≈ 74.5, matching that same offset.

Next I'm working through the strap, hook, and shackle dimensions, confirming the shackle is about 57 tall and the box holes sit at y=-73 relative to center. Then I'm computing the free end of the rope's position relative to the fixed anchor.

Rotating both flange edge points by -140° relative to the axle gives me a consistent top edge at y=-106 with width spanning ±74, confirming symmetry. Checking the tab hole position against this same rotation to verify it lines up correctly.

Now I'm figuring out the global layout: given the beam's underside sits at y=68, the axle needs to be at beam-frame y=174. I'm positioning the beam centered on the 1376x768 canvas with some translation offsets, then working out where the fixed axle lands at (688,194) and computing where the movable axle should go.

Continuing down the chain, I'm placing the strap hole, hook end, and shackle apex each a fixed distance below, then verifying the shackle's canonical hole geometry stays horizontal by checking the angle between its two holes equals zero after rotation. I'm also confirming the apex sits perpendicular above the hole midpoint by checking that angle comes out to -90, then using that to compute the final shackle hole positions at y=587.95, x=688±31, before moving on to the box holes.

Now I'm working out the box's final position, confirming it fits within the vertical limit, and checking the rope's free end location—there's no ground constraint since everything hangs. I'm now setting up the transform formula for each part: translating a chosen feature point to its target location, then rotating around that point by negating the angle, and I'm starting to apply this to the beam, bracket, and fixed wheel using their local coordinate points.

Still computing wheel centers...

Tracing the rope path clockwise around the movable wheel from right to bottom to left, I'm computing P2's position relative to the fixed wheel and checking whether the dead-end line from the anchor crosses the fixed wheel's rope path, verifying the tangent conditions hold at each wrap point.

Now I'm working out the strap and hook geometry — placing the big and small holes, rotating the strap piece by -125 degrees, then rotating the hook piece by -55 degrees and verifying its length by computing the arc endpoints and center of the semicircular cap.

For the shackle, I'm mapping the apex point to the hook's end position with a -160 degree rotation, then computing the two hole centers and their midpoint to check the apex-to-midpoint distance against the expected geometry.

I'm reconsidering whether to map the shackle holes directly to the box holes instead of using the apex as the reference point, then working out which shackle hole corresponds to the left side after rotation.

For the box, I'm computing precise hole centers from the given points, then using the midpoint between the two holes as a more reliable anchor than the box center, verifying the hole-line angle comes out to 25 degrees as expected.

The box bottom edge checks out at 744, and the bracket and fixed-wheel don't collide, so this looks good to finalize.


````

## Answer

````text
The hoist is assembled in the classic one-fixed, one-movable pulley arrangement. All placements were found by matching hole spacings and the rope's arc centres between parts.

**How the parts connect (all in the upright, unrotated orientation):**
- **Bracket:** Its flange's top edge is 106 px above its axle hole, so it bolts flat under the beam with the stem hanging down. The wheel axle is at (688,194). The small hole in its bottom tab sits 74.5 px lower, at (688,268.5).
- **Fixed wheel:** Its hub sits on the bracket's axle at (688,194).
- **Rope:**
  - Its wrap of radius 57.5 sits on the fixed wheel at (688,194).
  - Its wrap of radius 45 lies 184 px straight below, at (688,378), which places the movable wheel.
  - Its dead-end hole is 74.5 px below the fixed-wheel centre. This lands exactly on the bracket's tab hole at (688,268.5).
- **Movable wheel:** Its hub sits at (688,378).
- **Strap:** Its large hole is the movable wheel's axle at (688,378). Its small hole is 72 px below, at (688,450).
- **Hook:** Its eye pins to the strap's small hole at (688,450). Its rounded end is 80.75 px below, at (688,530.75).
- **Shackle:** The hook's rounded end sits in the top of the shackle's bow at (688,530.75). The shackle's pin holes are 62 px apart, 57.25 px below the bow, at y = 588.
- **Box:** Its two lifting holes are also 62 px apart, just under its top edge. They take the shackle pins at (688±31, 588), so the box hangs level with its bottom at y = 744.

The hook-to-shackle contact is the least certain match. I placed the hook's rounded-end centre on the centre line of the bow's apex, since the shackle has no explicit hole there.

**Transforms:** Each transform moves a part's matching feature to its target point and undoes the part's stored rotation. The beam stays unrotated.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1376 768">
  <use href="#kit-beam" transform="translate(394,20)"/>
  <use href="#kit-bracket" transform="translate(688,194) rotate(-140) translate(-66.46,-74.54)"/>
  <use href="#kit-fixed_wheel" transform="translate(688,194) rotate(-70) translate(-68.94,-68.94)"/>
  <use href="#kit-movable_wheel" transform="translate(688,378) rotate(-110) translate(-56.95,-56.95)"/>
  <use href="#kit-rope" transform="translate(688,194) rotate(-35) translate(-155.28,-62.34)"/>
  <use href="#kit-strap" transform="translate(688,378) rotate(-125) translate(-83.53,-67.94)"/>
  <use href="#kit-hook" transform="translate(688,450) rotate(-55) translate(-77.05,-12.21)"/>
  <use href="#kit-shackle" transform="translate(688,530.75) rotate(-160) translate(-57.71,-73.4)"/>
  <use href="#kit-box" transform="translate(688,588) rotate(-25) translate(-179.685,-64.78)"/>
</svg>
```
````

## Prompt

````text
Below is a kit of 9 SVG parts for a two-wheel pulley hoist (side view). Each part is a <g id="kit-..."> drawn in its own local coordinate system, stored at an arbitrary rotation. Each part's id names the part.

Assemble the parts into one complete, working two-wheel pulley hoist (side view) on a 1376 x 768 canvas. Parts are rigid: translate and rotate only, no scaling and no mirroring. Use every part exactly once. The base part, kit-beam, stays upright exactly as stored (at most 3 degrees of rotation).

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
<g id="kit-beam" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
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
<g id="kit-box" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
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
<g id="kit-bracket" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 191.286436542,108.171411568 L 77.9118589606,203.303977802 L 72.7695580831,197.175622257 Q 68.912832425,192.579355598 74.2751435269,188.07984233 L 101.086699036,165.582275991 L 13.5615703486,30.1594128986 L 31.9466369834,14.7325102662 L 150.113543396,124.443868971 L 176.925098905,101.946302632 Q 182.287410007,97.4467893646 186.144135665,102.043056023 Z" fill="#EBE3F7" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 59.5692611366,80.3220722017 A 9,9 140 0,1 60.6785726375,67.6425837264 A 9,9 140 0,1 73.3580611127,68.7518952273 A 9,9 140 0,1 72.2487496119,81.4313837026 A 9,9 140 0,1 59.5692611366,80.3220722017 Z" fill="#F8F7F2"/>
  <path d="M 30.0315258756,16.3394792904 L 15.4766814564,28.5524438744 A 6,6 140 0,1 7.02368913952,27.8129028738 L 6.38090152984,27.0468584307 A 6,6 140 0,1 7.12044253043,18.5938661139 L 21.6752869497,6.38090152984 A 6,6 140 0,1 30.1282792665,7.12044253043 L 30.7710668762,7.88648697355 A 6,6 140 0,1 30.0315258756,16.3394792904 Z" fill="#FEB8A7" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 15.5118064305,20.0378231409 A 4,4 140 0,1 16.0048337643,14.4024949297 A 4,4 140 0,1 21.6401619755,14.8955222634 A 4,4 140 0,1 21.1471346418,20.5308504746 A 4,4 140 0,1 15.5118064305,20.0378231409 Z" fill="#F8F7F2"/>
</g>
<g id="kit-fixed_wheel" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 90.8283753541,129.079413912 A 64,64 70 0,1 8.79875845094,90.8283753541 A 64,64 70 0,1 47.0497970084,8.79875845094 A 64,64 70 0,1 129.079413912,47.0497970084 A 64,64 70 0,1 90.8283753541,129.079413912 Z" fill="#DBEAF7" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 86.0400933475,115.923717221 A 50,50 70 0,1 21.9544551419,86.0400933475 A 50,50 70 0,1 51.838079015,21.9544551419 A 50,50 70 0,1 115.923717221,51.838079015 A 50,50 70 0,1 86.0400933475,115.923717221 Z" fill="#DBEAF7" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 72.0172674712,77.3963197683 A 9,9 70 0,1 60.4818525942,72.0172674712 A 9,9 70 0,1 65.8609048913,60.4818525942 A 9,9 70 0,1 77.3963197683,65.8609048913 A 9,9 70 0,1 72.0172674712,77.3963197683 Z" fill="#F8F7F2"/>
</g>
<g id="kit-hook" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 76.8905236535,5 L 7.46738789997,53.6106029808 A 6,6 55 0,0 14.3503051362,63.4404275122 L 83.7734408897,14.8298245315 Z" fill="#ECEAE4" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 79.3496798398,15.4858261883 A 4,4 55 0,1 73.7787659173,14.5035237565 A 4,4 55 0,1 74.761068349,8.93260983398 A 4,4 55 0,1 80.3319822716,9.91491226573 A 4,4 55 0,1 79.3496798398,15.4858261883 Z" fill="#F8F7F2"/>
</g>
<g id="kit-movable_wheel" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 39.1654600693,105.814523803 A 52,52 110 0,1 8.08649124139,39.1654600693 A 52,52 110 0,1 74.7355549752,8.08649124139 A 52,52 110 0,1 105.814523803,74.7355549752 A 52,52 110 0,1 39.1654600693,105.814523803 Z" fill="#FDF1C9" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 43.9537420759,92.6588271121 A 38,38 110 0,1 21.2421879324,43.9537420759 A 38,38 110 0,1 69.9472729686,21.2421879324 A 38,38 110 0,1 92.6588271121,69.9472729686 A 38,38 110 0,1 43.9537420759,92.6588271121 Z" fill="#FDF1C9" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 53.8723262323,65.4077411093 A 9,9 110 0,1 48.4932739352,53.8723262323 A 9,9 110 0,1 60.0286888122,48.4932739352 A 9,9 110 0,1 65.4077411093,60.0286888122 A 9,9 110 0,1 53.8723262323,65.4077411093 Z" fill="#F8F7F2"/>
</g>
<g id="kit-rope" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 112.55585817,123.366588224 L 93.9612808915,221.445558043 A 45,45 35 1,1 11.2191650428,189.816597186 L 106.054617793,32.6350093851 A 57.5,57.5 35 0,1 209.491978553,81.5248742758 L 61.5062666074,499.632703096" fill="none" stroke="#1F2A3A" stroke-width="17"/>
  <path d="M 112.55585817,123.366588224 L 93.9612808915,221.445558043 A 45,45 35 1,1 11.2191650428,189.816597186 L 106.054617793,32.6350093851 A 57.5,57.5 35 0,1 209.491978553,81.5248742758 L 61.5062666074,499.632703096" fill="none" stroke="#FEB8A7" stroke-width="9"/>
  <path d="M 115.832466347,125.660893969 A 4,4 35 0,1 110.261552424,126.643196401 A 4,4 35 0,1 109.279249992,121.072282478 A 4,4 35 0,1 114.850163915,120.089980047 A 4,4 35 0,1 115.832466347,125.660893969 Z" fill="#F8F7F2"/>
</g>
<g id="kit-shackle" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 67.2571353751,8.99619288633 L 80.9379411081,46.5838977178 C 88.8044044046,68.1968279958 30.5434619158,89.402076882 22.6769986194,67.789146604 L 8.99619288633,30.2014417725" fill="none" stroke="#1F2A3A" stroke-width="17"/>
  <path d="M 67.2571353751,8.99619288633 L 80.9379411081,46.5838977178 C 88.8044044046,68.1968279958 30.5434619158,89.402076882 22.6769986194,67.789146604 L 8.99619288633,30.2014417725" fill="none" stroke="#ECEAE4" stroke-width="9"/>
  <path d="M 63.4983648919,10.3642734596 A 4,4 160 0,1 65.8890548018,5.23742240318 A 4,4 160 0,1 71.0159058582,7.62811231302 A 4,4 160 0,1 68.6252159484,12.7549633695 A 4,4 160 0,1 63.4983648919,10.3642734596 Z" fill="#F8F7F2"/>
  <path d="M 5.23742240318,31.5695223458 A 4,4 160 0,1 7.62811231302,26.4426712894 A 4,4 160 0,1 12.7549633695,28.8333611992 A 4,4 160 0,1 10.3642734596,33.9602122557 A 4,4 160 0,1 5.23742240318,31.5695223458 Z" fill="#F8F7F2"/>
</g>
<g id="kit-strap" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 31.3960668461,6.40597930804 L 95.2899263006,51.1449413434 A 20.5,20.5 125 0,1 71.7732924102,84.7301751593 L 7.87943295567,39.9912131239 Q 2.96452068993,36.5497545058 6.40597930804,31.63484224 L 23.0396959622,7.87943295567 Q 26.4811545803,2.96452068993 31.3960668461,6.40597930804 Z" fill="#FDF1C9" stroke="#1F2A3A" stroke-width="4"/>
  <path d="M 78.3694214282,75.3099266499 A 9,9 125 0,1 76.1592409568,62.7753703242 A 9,9 125 0,1 88.6937972826,60.5651898527 A 9,9 125 0,1 90.903977754,73.0997461785 A 9,9 125 0,1 78.3694214282,75.3099266499 Z" fill="#F8F7F2"/>
  <path d="M 22.2583564212,29.9166630112 A 4,4 125 0,1 21.2760539894,24.3457490887 A 4,4 125 0,1 26.846967912,23.3634466569 A 4,4 125 0,1 27.8292703438,28.9343605795 A 4,4 125 0,1 22.2583564212,29.9166630112 Z" fill="#F8F7F2"/>
</g>
</defs></svg>
````
