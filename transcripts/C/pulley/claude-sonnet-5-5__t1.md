# C · pulley · claude-sonnet-5-5 · trial 1

- Result: **PASS**, score 1.00, tags: pass
- Model version: `claude-sonnet-5-5`, response id: `msg_vrtx_011CgrXzJttnmcneXe9D83Fj`
- Started 2026-11-08T21:05:20-0500, finished 2026-11-08T21:07:13-0500, 113.2 s, attempts 1
- Tokens: input 7,202, output 14,399 (thinking not reported separately by this provider)
- Settings: `{"provider": "anthropic", "route": "vertex", "max_tokens": 128000, "thinking": {"type": "adaptive", "display": "summarized"}, "output_config": {"effort": "high"}}`, prompt sha256 `76f5e071749cea91c1dade657f51f7d3e1a95596fc5850212d1d23e075b5f3c4`

## Failed checks

- none

## Thinking summary (as returned by the provider)

````text
I'm working out the positioning math for each piece - placing the beam upright with a specific translation so its underside and edges land correctly on the canvas, then figuring out the rotation and local coordinates needed for the other parts.

Now I'm tracing out the bracket shape's path points to identify its structure: a wide top plate connected to a vertical arm, with a pink collar near one end and an axle hole partway along. I'm measuring edge lengths to figure out which segment forms the plate's width versus its thickness, and locating the plate's center and orientation.

Next I'm figuring out which direction is "outward" from the plate versus "toward the body," then computing the rotation needed so that the hanging arm points straight down in world coordinates.

Applying the rotation matrix to the plate's local top-edge coordinate, I'm computing the transformed point to around (-3.0, -205.8), then checking where that needs to land in world space once the translation is added.

Now I'm placing the bracket at x=600 along the beam, giving a translation around (603.0, 313.82) so the underside sits flush with the beam at y=108. I'm also working out the center of the axle hole by trying to locate it from the four arc endpoints of the radius-9 circle.

Averaging opposite points gives the axle hole's local center at (66.46, 74.54), and rotating/translating into world coordinates lands it at (600.0, 214.0) — nicely directly below the plate center. Now I'm moving on to work out the collar hole's position from its own set of corner points.

Now I'm tracing the rope path itself: it starts at the dead end hole, runs down to a small 45-radius arc under the movable wheel, then back up over a larger 57.5-radius arc, and finally down along the long tail end — trying to map which arc goes under versus over the wheel.

I'm now checking that the large arc's center lines up concentrically with the fixed wheel hub, and working out its actual center coordinates from the chord geometry between the two known arc endpoints.

Rethinking the geometry instead: the dead-end hole at the collar near the fixed wheel likely drops vertically down to a small arc beneath the movable wheel, then wraps back up around the large arc over the fixed wheel before heading to the tail — so I need to work out where the movable wheel center sits relative to the fixed wheel's radius bounds.

I'm realizing the rope's rotation should be uniquely determined by matching its large arc center to the fixed hub and its dead-end hole to the collar point, since that distance constraint fixes both rotation and translation together. So I need to compute the large arc's center from the chord endpoints in the rope's local coordinates, then use that alongside the hole position to solve for the correct orientation.

That matches - distance 74.5, confirming C1=(155.29,62.34) as the correct center. Working out the rotation needed to map the vector from C1 to H onto the expected world position, I get about -35°, which aligns nicely with the arc parameter. Now I'm checking how the dead-end segment's direction transforms under this same rotation.

Rotating the other direction, I get nearly vertical (-0.068,-0.997), so that strand climbs almost straight up to the fixed wheel — roughly 4° off, which fits the -35° rotation plausibly despite the slanted dead strand. Now checking the tail direction (-148,418.1) normalized to (-0.334,0.943) and rotating that too.

Finishing those rotated coordinates, A lands left of center and B lands right and slightly above, confirming the large arc sweeps over the top correctly. Now I'm moving to the small arc with center C2, radius 45, computing the chord between its endpoints to find the perpendicular offset for the center.

Checking C2=(49.75,213.07) confirms the tangent direction matches smoothly for clockwise motion. Now I'm computing the rotated offset between C2 and C1 to verify the arc centers align correctly.

Checking that length matches, then computing the upward strand from Q to A, which comes out nearly vertical on the left side around x=555 to x=542 — consistent with the geometry.

Now verifying the strand crossing near the movable wheel region at (600,398) with radius 52, checking whether the rope passes inside or outside the wheel edge there. I'm recalculating the rotation and translation needed to map C1 onto its target position at (600,214), then double-checking the hole position under that same transform.

For the movable wheel, I'm locating its hub center from the circle points and averaging opposite corners to get roughly (57,57) local, with overall wheel radius 52. Since rotation doesn't matter for this wheel, I'm just computing the translation needed to place it at (600,398), landing on (543.05, 341.06).

Now for the fixed wheel, I'm doing the same calculation: averaging opposite circle points gives a local center around (68.94,68.94), so translating to position (600,214) requires an offset of (531.06,145.06).

Next I'm working out the strap's geometry, which hangs below the movable hub with a rounded top end — I'm averaging its corner points to find the hole center for proper alignment.

For the strap's bottom hole, I'm computing the vector between the top and bottom hole centers, finding its angle (around -145°), and figuring out the rotation needed (-125°) to orient the strap so it points straight down from the hub.

Verifying the rotation math against the known 72-unit length, then placing the rotated top hole relative to the hub position at (600,398), giving a local offset of about (7.74,-107.39), so the strap's world position becomes (592.26,505.39) with the bottom hole landing near (600,470).

Now I'm locating the hook's geometry from the circle-hole centers: the top end center sits around (80.33,9.91) and the bottom curl center around (10.91,58.53), establishing the hook as a straight bar running down-left between these two points.

I need to rotate this vector by roughly -55° to align it to 90°, since the hook appears to be a simple bar with just a rounded bottom rather than a pronounced curl -- so I should treat the shackle bow as resting flush against that rounded bottom edge, and I'm now checking where the hook's top hole lines up with the strap's bottom hole.

Computing the hook bar's world position and dimensions, I get a rod about 12 units wide centered at x=600, extending down to roughly y=557. Now I'm working out the shackle shape's leg endpoints and hole positions using the stroke geometry.

The leg direction from bow points down-ish at angle -110°, but I need it pointing up to vertical (90°), so I'm computing a rotation of 200° and verifying it zeroes out the x-component correctly.

Checking the other leg's separation confirms the rotated coordinates line up with 62 units apart horizontally and zero vertically, so the two legs end up level with each other as expected.

Now I need to find where the bow's top curve sits relative to the hook — I'm computing the midpoint of the bezier curve defining the bow by averaging its control points to estimate where the bow's outer edge reaches toward the hook's base.

I'm working out where the hook meets the bow — since the hook sits inside the bow's U shape, its bottom edge should touch the inner edge of the bow's top, which is the centerline offset inward by half the stroke width (8.5) toward the cream interior.

Estimating the hook's visible bottom at roughly y≈553 with a few pixels of tolerance, so the bow's centerline top comes out to about y≈544.5, assuming the bezier curve is symmetric at its midpoint.

Now I'm rotating the local bow-top coordinate by 200 degrees to find its world position, solving for the translation offset that places this point at x=600, y≈544.5 — working out t_x≈629.13 and t_y≈633.2.

Continuing, I compute the rotated world positions of the two leg endpoints, finding they both land at y≈601.7, with x-values near 569 and 631 — so the legs touch down symmetrically around x=600. Now I'm checking the box lid beneath them, which has two small holes flanking a blue half-disc, and noting the box itself is also rotated.

I estimate the box's rectangle corners from the rounded shape, getting roughly a 220x146 rectangle tilted about 25° based on the edge direction, so I'll need to rotate by -25° to level it. I'm also trying to figure out which side is the lid, given the small blue label strip visible at the top.

Looking closer, there are half-disc shapes at the four corners that look like rivet decorations, plus a larger blue half-disc centered on the long top edge midpoint, roughly radius 31, which seems to be the lid's distinguishing feature.

That long diagonal line seems to split the box into two halves, running perpendicular to the half-discs on the top and bottom edges. I'm also noting two cream dots flanking the half-disc on the top edge, trying to figure out how the arc's chord and bulge align with the box geometry.

Checking distance between hole1 and hole2 gives 62, matching the shackle end separation. This suggests the top long edge with the half-disc and holes is the lid, and I'm trying to figure out where the dividing line between lid and body falls relative to the blue label strip near the top.

I'm now tracing the line from (183.9,55.7) to (113.8,206.2), which spans across the box's short dimension—essentially a vertical centerline once the box is leveled. That means the lid is the top edge with the handle cutout and holes, and after rotating by -25° that edge should become horizontal at the top, so I need to determine which side of that edge faces the box's interior.

Good, confirmed rotate(-25) keeps orientation correct. Now I'm computing the hole centers from their corner points and figuring out which leg end aligns with which hole after applying the rotation.

Checking the box extents against the shackle placement: the lid top and bottom fall within the 768 height limit, and the shackle legs, bow, and hook all land within their expected vertical ranges without overlap issues.

Now I'm verifying the beam-bracket alignment -- confirming the beam's hatching sits on top, the bracket plate is centered under the beam within its x-range, and the plate thickness extends downward correctly into the body.

Checking the bracket's transform (translate 603.0,313.82 rotate 220) against expected coordinates confirms it matches. I'm also re-verifying the rope's transform (translate 437.03,252.0 rotate -35) by recomputing its y-component precisely, which checks out at -38.00, before moving on to the shackle.


````

## Answer

````text
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1376 768">
<use href="#kit-beam" transform="translate(390,40)"/>
<use href="#kit-bracket" transform="translate(603.01,313.82) rotate(220)"/>
<use href="#kit-fixed_wheel" transform="translate(531.06,145.06)"/>
<use href="#kit-rope" transform="translate(437.03,252.0) rotate(-35)"/>
<use href="#kit-movable_wheel" transform="translate(543.05,341.06)"/>
<use href="#kit-strap" transform="translate(592.26,505.39) rotate(-125)"/>
<use href="#kit-hook" transform="translate(545.81,526.11) rotate(-55)"/>
<use href="#kit-shackle" transform="translate(629.13,633.2) rotate(200)"/>
<use href="#kit-box" transform="translate(409.78,618.92) rotate(-25)"/>
</svg>
````

## Prompt

````text
Below is a kit of 9 SVG parts for a two-wheel pulley hoist (side view). Each part is a <g id="kit-..."> drawn in its own local coordinate system, stored at an arbitrary rotation. Each part's id names the part.

Assemble the parts into one complete, working two-wheel pulley hoist (side view) on a 1376 x 768 canvas. Parts are rigid: translate and rotate only, no scaling and no mirroring. Use every part exactly once. The base part, kit-beam, stays upright exactly as stored (at most 3 degrees of rotation).

Grading is done by code on where the parts land:
- Ceiling beam upright, hatching on top: rotated at most 3 deg from how it is stored.
- Fixed (larger, blue) pulley wheel: its hub hole on the bracket's axle hole (within 4 px)
- Rope: its larger wrap arc (the one that goes over the top) concentric with the fixed wheel's hub (within 4 px)
- Rope: the hole in its short dead end (the end next to the smaller arc) on the hole in the bracket's pink collar (within 4 px)
- Movable (smaller, cream) pulley wheel: its hub hole concentric with the rope's smaller wrap arc, which goes under it (within 4 px)
- Strap: the hole in its rounded top end on the movable wheel's hub hole (within 4 px)
- Hook: the hole in its straight top end on the small hole near the strap's bottom (within 4 px)
- Box: one of the two small holes flanking the blue half-disc on its lid under the hole at one shackle leg end (within 4 px)
- Box: the other small lid hole under the hole at the other shackle leg end (within 4 px)
- Shackle: the inner edge of its bow's top rests on the hook's lowest part (anywhere from the inside of the hook's curl down to its visible bottom), so the bow hangs on the hook (within 4 px)
- Bracket: the centre of its wide top plate's upper edge on the beam's underside, anywhere along it with the whole plate under the beam (within 4 px)
- Bracket: hangs straight down from the beam, top plate flat against the beam (orientation relative to the beam) (within 6 deg)
- Strap: hangs straight down below the movable wheel hub, rounded end up (orientation relative to the beam) (within 6 deg)
- Hook: hangs straight down from the strap, curl at the bottom (orientation relative to the beam) (within 6 deg)
- Shackle: hangs straight down, bow up, legs vertical (orientation relative to the beam) (within 6 deg)
- Box: hangs level and right way up, the small blue label strip at the top (orientation relative to the beam) (within 6 deg)
- every other part must face the way it does on the working object, relative to the base part, within 8 degrees; parts that turn in use (wheels, gears, sprockets, cranks, connecting rods, pedals, rotors) may sit at any angle;
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
