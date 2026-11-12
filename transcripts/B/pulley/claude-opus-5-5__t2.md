# B · pulley · claude-opus-5-5 · trial 2

- Result: **PASS**, score 1.00, tags: pass
- Model version: `claude-opus-5-5`, response id: `msg_vrtx_011CgrVTFarmcTqCfw878SoH`
- Started 2026-11-08T20:32:05-0500, finished 2026-11-08T20:34:44-0500, 159.7 s, attempts 1
- Tokens: input 6,683, output 15,562 (thinking not reported separately by this provider)
- Settings: `{"provider": "anthropic", "route": "vertex", "max_tokens": 128000, "thinking": {"type": "adaptive", "display": "summarized"}, "output_config": {"effort": "high"}}`, prompt sha256 `0eb4a228ba7e95b6b6657247f40030cf1c9e960d98e122abe06db12d8d862842`

## Failed checks

- none

## Thinking summary (as returned by the provider)

````text
I'm identifying the pieces: p08 looks like a ceiling beam with hatching marking it as fixed in place, serving as the anchor the hoist hangs from. Then p01 appears to be a rotated load or crate shape with corner protectors and hook features, which I need to examine further.

I'm measuring the two holes on the crate's top edge as lifting points and calculating the crate's rotation angle to figure out how it would look upright. Then I'm checking p02, which seems to be a bracket or hanger plate with mounting holes at either end, possibly serving as the ceiling mount given its matching color to another wheel piece, and starting to compare the color coding across pieces to figure out which parts belong together.

Now I'm tracing out p09's outline point by point, figuring out it's an inverted T-shape — a long crossbar with a stem — likely a hook or fork plate component with holes for a pulley connection.

Actually reconsidering: with stem vertical, rotating by +40° would put the crossbar at bottom, forming an inverted-T foot shape. That fits p08 as a ceiling mount with hatching above the line, meaning p09 could instead hang downward from the ceiling flange, stem descending with the crossbar bolted at top.

This confirms p09 is the ceiling flange with the 9-hole as the upper pulley axle, and the pad below with a 4-hole likely serving as the becket where the rope's dead end anchors to the fixed block in a two-pulley setup.

The midpoint comes to (134.6,155.75). The stem edges aren't parallel, suggesting the stem tapers wider toward the bottom, with the two sides angled at roughly 57° and 43° — averaging near 50°, matching the expected 140-90 configuration. I'm now tracing that axis from the pad hole up toward where it meets the crossbar's inner corners.

Measuring distances along the rotated axis, I find the flange top to 9-hole span is about 106 units, and to the pad hole about 180.5. I'm also checking the crossbar's outer flange edge coordinates to work out its thickness near the top corner.

Computing along the normal direction, the flange edge is about 14 units thick, with the pad sitting toward the smaller projection value. After applying the -140° rotation, that normal direction shifts to roughly -90°.

Looking at p06 next, it looks like a pink rope: a shank line from one point curving around a pulley-like arc of radius 45, then another arc of radius 57.5, extending down to a long endpoint — matching p09's pad color, with a thick stroke suggesting rope texture. Meanwhile p07, with its thick grey-lined stroke, looks like a U-shaped shackle with holes at both ends.

Continuing the line to (61.5,499.6) as the hauling end, then checking the rope's path logic: from the becket it runs down around the movable pulley (radius-45 wrap) and up over the fixed pulley (radius-57.5 wrap) before dropping to the free end. Applying the -35° rotation to the first segment gives roughly 65.7° instead of a clean vertical, so I'm second-guessing whether these angles are supposed to be exactly vertical or whether the anchor offset naturally produces slanted segments that the grader still accepts.

Now I'm working out the arc geometry precisely — computing the tangent direction at the start of the first pulley wrap and figuring out which side the arc center falls on given the sweep flag, since that determines whether the rope wraps clockwise or counterclockwise around the movable pulley.

So center C1 comes out to (49.75, 213.07), and I verify the distance to P2 checks out at 45. Now moving to the second arc from P3 to P4 with radius 57.5, I'm computing the incoming direction vector from P2 to P3, getting length 183.6 and unit vector (0.5165,-0.8561) to figure out the sweep direction.

Trying the perpendicular rotation for a counterclockwise sweep, I get C2 at (56.82, 2.94), but checking the distance from this center to P4 gives 171.7 instead of the required 57.5 — so this orientation is wrong and I need to try the opposite rotation direction.

I'm reasoning through the geometry: on the right side of the circle, moving downward corresponds to clockwise motion with the center to the left of travel, which matches arc 1's large-arc setting. For arc 2, the rope travels upward along the other side, so I need to check whether that direction is also consistent with clockwise motion or if it flips to counterclockwise.

Since the chord length is just under twice the radius, two valid circle centers exist symmetric about the midpoint, so I'm checking whether the sweep=0 flag actually corresponds to my assumed center or the reflected one instead.

That sweep angle would route the arc under the wheel and through the bottom, which seems like a rendering anomaly rather than intended geometry. Let me instead check tangency conditions directly at P4 for the outgoing rope line to verify the correct circle center.

Verifying this confirms the intended hub center is (155.27, 62.34), tangent to both rope lines, so the sweep flag must just be mis-set by the generator rather than reflecting true geometry. But checking the angles of the segments after applying the -35° rotation, none come out vertical as I'd expect, so something about my rotation assumption still isn't matching up.

Continuing the rotation, I find C2's y' close to -38, and the anchor A sits 74.5 units below fixed point C2, matching the hole spacing I noted earlier. Also A, C1, and C2 all land on the same x'=163 line, confirming vertical alignment, while the free end E lands off to the side at x'=337, which makes sense since the rope runs from the centerline out to the tangent point on the movable pulley before heading to the free end.

Now I'm mapping components to parts: the fixed block is p09 with a 9-hole axle and a becket pad hole 74.5 below it, matching the alignment; the movable pulley plate is p02/p04 with a 9-hole axle and a 4-hole 72 units away, and p07 is a shackle with two 4-holes while p03 is a small link connecting one 4-hole to a rounded end.

Checking the load piece p01, its two top holes are 62 apart, matching the distance between the stirrup p07's two end holes — confirming p07 connects the crate's top holes to the rest of the rig.

Rotating p07 upright, I find both legs curve upward from the crate holes, forming an inverted U shape, which likely hooks onto the movable block p02's hole plate above it.

Checking p02 upright, the 4-hole sits 72 units below the axle hole, suggesting this is a strap hanging from the axle down below the wheel, which then connects to p03. Working out p03's upright rotation, its hole-to-rounded-end direction also points downward, meaning p03 hangs below p02 as a link in the chain.

I'm trying to figure out where the bail piece p07 attaches, since its curved top edge doesn't have a hole — it must hook onto something, likely p03's rounded end, since that's described as a plain bar with a rounded free end rather than a hole. I'm computing the midpoint of p07's curve using the Bezier formula to see if it aligns with p03's end position.

I'm reconsidering whether p03 extends from p02's hole down to a rounded end where the bail hooks, versus being a tie-rod, versus being a pull handle at the rope's free end. I'm now trying to trace all the connection points systematically: p08 to p09's seat, p09 to p05's axle, and p09 to p06's becket hole where the rope anchors.

Following the chain further, I'm working out that p06 connects to p05's hub and p04's movable hub, p04 links to p02 via a nine-hole axle, and p02 connects to p03 which likely acts as a hook or link from the block down to the bail — with p03's rounded end seating somewhere on p07, possibly at the apex of its curved feature.

Checking the vertical measurements for plausibility, I'm tracing the stack from the movable axle at y=146 down through p02's four-hole offset to p03's rounded end, trying to verify the distances line up with where the bail apex should fall, while reconsidering whether p03's free end is actually a hook into the bail or just a handle on a rope's free end.

I also need to confirm the crate's bounding box doesn't overlap the rope's free endpoint, and double-check p02's hole orientation and p07's rotation geometry to make sure everything stays consistent.

The midpoint of the two holes matches the apex position, confirming t=0.5 is the curve's apex. Now I'm computing the upright crate rotation for p01: applying a -25 degree rotation to the two hole centers derived from their path coordinates, finding h1 at roughly (151.59,51.68) and h2 at (207.78,77.88), then transforming h1 into rotated coordinates.

Crate spans x 80 to 300 with center 190.2, confirming symmetric hole placement, and it hangs rather than resting on the ground. Now I'm computing the rotation for p02's upright orientation, applying a -125 degree transform to locate the 9-hole center from its arc path coordinates.

Working through the hole centers: the 9-hole lands at (83.53, 67.94) and the 4-hole at (24.55, 26.64) before rotation. After applying the transform, the 9-hole maps to roughly (7.75, -107.40) and the 4-hole to (7.74, -35.39), confirming the 4-hole sits below the 9-hole by 72 units as expected. Now I'm setting up the same rotation calculation for p03, using a -55 degree angle this time.

Computing p05 hub center similarly, then noting wheels can be placed at any rotation since only translation matters. For p09, I'm applying a -140° rotation transform to locate the 9-hole center and pad hole center using the same formula pattern.

I'm transforming the flange top midpoint and edge endpoints through the same rotation, confirming the flange sits above and aligns horizontally, then starting to lay out the world coordinate frame by placing the ceiling piece p08 with a translation and checking its span.

Now I'm picking a world x-coordinate for the fixed block flange and solving for the translation needed in p09's transform so its rotated local flange point lands there, then propagating that to find the fixed axle and becket world positions. I'm continuing into the rope piece p06, solving its translation similarly by matching a rotated local point to the target world position.

I'm verifying by checking the other rope anchor point maps close to the becket coordinate as expected, then computing the remaining joint points. Now I'm recalculating the C2 control point more carefully, finding the unit vector along P2→P3, normalizing it, taking the perpendicular, and using it to offset from P3 by 57.5 units.

Computing the translation offset so the fixed axle lands at the correct world position, then checking that point A and C1 land consistently—confirms translate(437, 252) roughly, giving C1 world coordinates near (600, 398), matching the target anchor point.

Now I'm working out the translations for the remaining upright parts (p04, p05) to align their centers with the fixed world coordinate, then recomputing the 9-hole and 4-hole positions on the p02 upright using the rotation matrix to verify they both land near x=7.74.

For p03, I'm computing the upright-to-world translation using its rotated hole and center coordinates, checking the math against the known endpoint (600, 469.99) to solve for tx and ty.

For p07, I'm working out the apex point's translation using the Bezier control points to find the precise world-space apex coordinates for (600, 550.74).

Now I'm computing the hole centers for this piece by averaging the extreme points and applying the rotation transform to get their world-space positions.

Computing h2's transformed position confirms the translation offsets align both holes to the crate, placing the bottom around y=764 against a 768 canvas height—tight but workable, with the rope end at (774,626) also fitting within range. I'm now considering nudging the whole composition upward by about 30 units to give more breathing room near the ceiling hatch.

Writing out the final transform values...

Verifying the axle alignment between p09, p05, and p06 — the computed hub and connector midpoints all converge on the same world coordinate, confirming the placements are consistent.


````

## Answer

````text
The assembly hangs from the ceiling beam. I identified the parts from their drawings as follows:

| Part | What it is |
|---|---|
| p08 | Ceiling beam (base), hatched on top, kept upright |
| p09 | Fixed pulley block. Its flange seats on the beam's underside, a 9 px hole carries the upper axle, and a pad hole 74.5 px lower is the rope anchor (becket). |
| p05 | Upper fixed pulley wheel (radius 64). The rope wraps its groove at radius 57.5. |
| p06 | The rope. It is tied off at the becket, runs down and around the lower wheel, up and over the upper wheel, then out to the free hauling end. Its curves fix the relative positions of the becket and both wheel centres, all on one vertical line. |
| p04 | Lower movable pulley wheel (radius 52). The rope wraps it at radius 45. |
| p02 | Movable block side plate: an axle hole with a link hole 72 px directly below it. |
| p03 | Hanging link from the plate's lower hole, ending in a rounded end. |
| p07 | U-shaped bail. Its top curve hangs on the link's rounded end, and its two leg holes (62 px apart) pin to the crate. |
| p01 | Load crate, with two lifting holes on its top, 62 px apart. |

Placement:
- Every non-wheel part is rotated back to its working orientation by undoing its stored angle.
- The two wheels are only translated, since they may sit at any angle.
- Each part is positioned so its matching features coincide with its neighbour's.
- The upper axle, becket and lower axle all lie on x = 600.
- The bail is pinned to the crate holes at x ≈ 569 and x ≈ 631.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1376 768">
  <use href="#kit-p08" transform="translate(394,10)"/>
  <use href="#kit-p09" transform="translate(602.99,283.81) rotate(-140)"/>
  <use href="#kit-p05" transform="translate(531.06,115.05)"/>
  <use href="#kit-p06" transform="translate(437.04,221.99) rotate(-35)"/>
  <use href="#kit-p04" transform="translate(543.05,311.04)"/>
  <use href="#kit-p02" transform="translate(592.26,475.38) rotate(-125)"/>
  <use href="#kit-p03" transform="translate(545.80,496.11) rotate(-55)"/>
  <use href="#kit-p07" transform="translate(629.12,609.45) rotate(-160)"/>
  <use href="#kit-p01" transform="translate(409.77,595.22) rotate(-25)"/>
</svg>
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
