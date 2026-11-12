# C · pulley · claude-sonnet-5-5 · trial 2

- Result: **PASS**, score 1.00, tags: pass
- Model version: `claude-sonnet-5-5`, response id: `msg_vrtx_011CgrXzKuARQDPV26qUteMJ`
- Started 2026-11-08T21:05:20-0500, finished 2026-11-08T21:07:13-0500, 113.0 s, attempts 1
- Tokens: input 7,202, output 14,534 (thinking not reported separately by this provider)
- Settings: `{"provider": "anthropic", "route": "vertex", "max_tokens": 128000, "thinking": {"type": "adaptive", "display": "summarized"}, "output_config": {"effort": "high"}}`, prompt sha256 `76f5e071749cea91c1dade657f51f7d3e1a95596fc5850212d1d23e075b5f3c4`

## Failed checks

- none

## Thinking summary (as returned by the provider)

````text
I'm working out the positioning and rotation for each component, placing the beam at a translated location spanning its width and figuring out the bracket's plate geometry to fit beneath it.

Tracing the plate as a thin strip (thickness ~8) along that long edge, with its center around (134.6,155.74), and the arm extending from the plate toward the collar region in the direction roughly (-115.8,-138.3) — establishing the bracket's local "down" orientation.

Now checking the ordering along the arm: plate center at (134.6,155.7), axle hole at (66.5,74.5), and collar at (18.8,17.5), which suggests the arm runs from the plate down through the axle to the collar at the very bottom, where the fixed wheel sits at the axle and the rope's dead end attaches at the collar below it.

I'm computing the rotation needed: the local "up" direction (from collar to plate) is at roughly 50.1° in local coordinates, and I need to rotate it to point to -90° to match the target orientation.

The stored rotation of 140° in the arc flags tells me the undo rotation should be -140°, which I verify by applying that transform to the up vector and confirming it lands correctly, then I start applying it to the plate's center point.

Checking the other reference points—axle and collar hole—against this same rotation, all x' values consistently converge to -3.0, confirming the rotation axis. I'm now locating the plate's outer edge along this rotated axis and seeing that it sits at y' ≈ -205.8, matching the line endpoint, with the plate body extending toward values greater than that.

Now I'm working out the translation needed to place this rotated plate at the beam underside in world coordinates, picking x=600 as the beam position and solving for the offsets, which puts the axle around (600, 214) and the collar around (600, 288.5). With the fixed wheel centered at (600,214) with radius 64, I'm checking that the rope path over the wheel and down to its dead end lines up properly.

So the dead end goes from the collar down to the movable wheel, wraps under it with radius 45, then up to the fixed wheel, wraps over it with radius 57.5, and continues as a long free tail hanging down to the other side. That accounts for both wheels in the pulley path.

Now I'm working out the center of the fixed arc given its endpoints and radius 57.5, computing the chord length and perpendicular offset to pin down the exact center coordinates.

Let me double check this by computing the circle center from a different tangent line, using the rope segment direction and perpendicular offset to confirm consistency with the arc geometry.

But I'm noticing the rotation doesn't line up cleanly — the tail direction angle comes out around 109.5° when I'd expect something closer to 90°, and the straight segments at the dead end aren't actually parallel to each other, which is throwing off my assumptions about the rotation value.

Let me try fixing the rotation by actual constraints instead: anchoring the large arc center to the fixed wheel and the dead end hole to the collar should pin down both rotation and translation simultaneously, so I'm computing the vector between those two points in local coordinates to solve for it.

Good, tail slants to the right as expected. Now I'm working out the arc center for the smaller arc from the two endpoints with radius 45, computing the chord midpoint and perpendicular offset, then determining which side the center falls on based on the large-arc and sweep flags.

Cross-checking using the tangent direction at the arrival point confirms the center at approximately (49.75, 213.07), matching both methods.

Now computing the vector between big center (155.3, 62.33) and small center, rotating by -35 degrees gives a clean vertical offset of 184, placing the movable wheel center at (600, 398), which looks right. Then I'm working out the rope transform by rotating about the origin and translating so the big center maps to (600, 214).

Now I'm locating the movable wheel's hub hole center by averaging the four corner points of the hole outline.

Working out the translation for the fixed wheel, I get (531.06,145.06). Now I need the precise axle position on the bracket, averaging the hole coordinates to find the local center and rotating it to determine the exact translation offset.

Checking the beam underside aligns with ty=313.8 by working through the plate's top edge midpoint rotation, confirming ty≈313.82 and the plate's x-range fits within the beam. Now starting to work out the strap geometry, locating its rounded top-end hole coordinates.

Solving for the rotation angle, I get -125°, which checks out correctly against the target vector of length 72 pointing straight down. Now I'm applying that same rotation to the strap's top hole coordinates to find its new local position.

For the bottom hole and the hook component, I'm placing the bottom hole at world coordinates (600, 470.4), then working out the hook's geometry by averaging its mounting hole corner points to get a center around (77, 12.2), and computing the angle from that hole to the hook's curl tip to figure out how much rotation is needed to point it downward.

So the hook body appears to just be a straight bar roughly 12 wide and 85 long with a rounded end, rather than a true curled hook shape. I'm thinking the shackle bow's inner top edge should rest somewhere along that lowest rounded portion of the bar.

Working through the rotation math, I get the bottom edge of the hook landing at roughly world y=551, with the x-coordinates of the two corner points coming out close together around x=594 and x=600, confirming the bottom is fairly narrow and flat.

Now I'm figuring out the shackle shape — a thick U-shaped bar outlined with a path through several curve points, with small holes at each leg end. I'm averaging the hole coordinates to pin down their centers, finding one centered near (67.26, 9.0) matching the path's starting point, and now locating the other hole's center on the opposite leg.

With both hole positions identified, I'm working out that the legs sit near the top of the local coordinate space while the bow curves out at the bottom, meaning I need roughly 180 degrees of rotation to flip the bow upward as it would hang from a hook — accounting for the stored rotation value of 160 already applied.

Computing the rotation angle to align the leg axis vertically (-160°), then applying that cosine/sine transform to find the rotated coordinates of the first hole.

Continuing the bow point calc, I get x≈57.7, giving local bow coordinate (57.7,73.4). Now I need to account for stroke width 17, meaning the inner edge of the bow sits about 8.5 units from the centerline — and since the hook's lowest point rests against that inner edge, I need to figure out exactly where that inner surface is relative to the centerline top of the bow.

Since the rotation isn't a perfect 180 degrees, I need to actually trace the curve to find the true topmost world point rather than assuming it's the local midpoint, so I'm computing the rotated y-coordinate at several parameter values along the bow.

Checking t=.6 confirms the slope continues toward -88, so t=.5 does look like the extreme at about -88.70, with center x' around -29.12. Now I need to account for the stroke width to find the inner edge of the top of the bow - since the visible outer stroke is 17px with the cream fill at 9px, I'm figuring out how much of that is outline versus fill to offset the centerline y-coordinate correctly.

Splitting the difference between 4.5 and 8.5 offsets, I pick 6.5 as the inner edge offset, giving y' around -82.2. From there I work out the shackle's translation by placing this inner edge at the world y=549 position, getting ty≈631.2, then solve for tx so the bow center lands at x=600, yielding tx≈629.12. Finally I compute the world positions of the two shackle holes to confirm the legs are properly spaced and roughly symmetric about x=600.

Now I'm turning to the box geometry, examining its rounded rectangle corners after a 25° rotation to figure out the local coordinates of the lid holes flanking the blue half-disc, and estimating the box's long side length from the corner positions.

That gives a box roughly 240 by 166 with rounded corners, so now I'm figuring out which edge represents the lid by tracing the half-disc shapes positioned along the corners and edges.

I verify that midpoint lies exactly on the top edge line, confirming this half-disc bulges inward from the top edge. The next half-disc runs from (85.66,193.06) to (141.85,219.26), likely sitting on another edge similarly.

Now I'm locating the small holes on the lid: I'm averaging the quadrilateral corner points to find each hole's center, getting approximately (151.59, 51.68) for the first hole and around (207.78, 77.x) for the second.

Checking the distance confirms a length of 62.0, matching the half-disc's diameter span. I can see these holes sit 10 pixels inward from the half-disc's edge endpoints, offset along the perpendicular normal direction into the shape.

Now I'm noticing there's also a bottom half-disc without holes, plus a center dividing line, and a small rectangle near the top-left that looks like a blue label strip positioned along the top edge.

Applying the -25 degree rotation confirms the box sits upright with the lid at top, so I'm transforming the hole coordinates through this rotation to find their actual positions on the upright box.

Now I'm computing the translation needed to align the box's hole1 with the shackle's left hole at (569.0, 599.7), checking that the resulting box dimensions (height 166, width 240) fit within canvas bounds without clipping the bottom edge.

I'm verifying the box's lowest corner stays under y=768 after rotation and translation, confirming the lid holes line up with the shackle holes at y=599.7, then moving on to check the vertical layout of the shackle bow against the hook and strap positions.

Checking the strap hole placements, I confirm the hook's rotated top hole lands exactly at (600, 470.4) matching the strap's bottom hole, and verifying the hook's rotation by -55 degrees correctly points its straight end downward using the axis direction vector math.

Now I'm tracing the rope's tail position through its -35 degree rotation to confirm it lands around (773.9, 626.0), comfortably within the canvas, and checking that the beam spans x 305-883 and y 45-108 so the bracket plate sits properly inside its bounds before finalizing the transform attributes.

The rope-under-movable sits at wheel radius 45 against a 52 outer with a 38 groove radius, which checks out fine.


````

## Answer

````text
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1376 768">
<use href="#kit-beam" transform="translate(300,40)"/>
<use href="#kit-bracket" transform="translate(603,313.82) rotate(-140)"/>
<use href="#kit-fixed_wheel" transform="translate(531.06,145.06)"/>
<use href="#kit-rope" transform="translate(437.02,252.09) rotate(-35)"/>
<use href="#kit-movable_wheel" transform="translate(543.05,341.05)"/>
<use href="#kit-strap" transform="translate(592.26,505.39) rotate(-125)"/>
<use href="#kit-hook" transform="translate(545.81,526.52) rotate(-55)"/>
<use href="#kit-shackle" transform="translate(629.12,631.2) rotate(-160)"/>
<use href="#kit-box" transform="translate(409.78,616.93) rotate(-25)"/>
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
