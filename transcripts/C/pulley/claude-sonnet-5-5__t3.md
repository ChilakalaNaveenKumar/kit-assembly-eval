# C · pulley · claude-sonnet-5-5 · trial 3

- Result: **PASS**, score 1.00, tags: pass
- Model version: `claude-sonnet-5-5`, response id: `msg_vrtx_011CgrXzKwdsfU7MPZ2BqkrV`
- Started 2026-11-08T21:05:20-0500, finished 2026-11-08T21:07:21-0500, 121.3 s, attempts 1
- Tokens: input 7,202, output 15,310 (thinking not reported separately by this provider)
- Settings: `{"provider": "anthropic", "route": "vertex", "max_tokens": 128000, "thinking": {"type": "adaptive", "display": "summarized"}, "output_config": {"effort": "high"}}`, prompt sha256 `76f5e071749cea91c1dade657f51f7d3e1a95596fc5850212d1d23e075b5f3c4`

## Failed checks

- none

## Thinking summary (as returned by the provider)

````text
I'm working out the positioning for each piece, figuring out where to translate the beam so its underside lines up, then starting to analyze the bracket's path vertices and plate structure.

Looking at the coordinates, I can identify the pink collar and its hole location around (18.3,17.5), and the axle hole center computed from the arc points to roughly (66.5,74.5). I'm also tracing the wide top plate's long edge between its two corner points to understand how the plate is oriented before figuring out where the shorter connecting edges go.

I'm computing the plate edge's direction vector and comparing it against the arm's direction toward the collar point to figure out which normal vector points toward the bracket body, using dot products to determine orientation.

Now I'm working out the rotation needed so the body-facing direction aligns with screen-down, finding the angle between the computed normal and (0,1), then deriving a rotation of about -140° and verifying it also brings the plate edge to horizontal.

Applying this rotation, I compute the upper edge's center and the axle hole position, finding the axle lands almost directly below the edge center, confirming the alignment is correct.

Now checking the collar hole similarly, it lands at nearly the same x-coordinate as the axle but about 75px below—which, given the wheel's radius of 64, puts it just beneath the wheel itself, suggesting the collar sits right at the base of the fixed wheel.

For bracket placement, I'm computing the translation needed so the rotated upper edge center aligns with the beam's underside, then working out where the axle hole and collar hole land after applying that transform—getting the axle at roughly (594, 204) and the collar just below it.

Now I'm finding the fixed wheel's hub hole center by averaging its corner points, confirming it sits at (68.94, 68.94), symmetric so orientation doesn't matter, and computing the translation needed to shift it onto the axle position, checking that the wheel's top edge clears the beam underside properly.

Then I'm tracing out the rope's path geometry—starting from a hole whose center I calculate at roughly (112.56, 123.37), following line segments and arcs (one with radius 45, large-arc and sweep flags set, another radius 57.5) through several waypoints down to a far endpoint near (61.51, 499.63), working out how the rope threads from its starting hole through each bend.

I'm checking whether the dead-end segment and the segment connecting to the fixed wheel are parallel by computing direction angles between the points, and finding they don't line up as expected (~100.7° versus ~-58.9°, not matching the ~-79.3° I'd expect for parallel lines)—suggesting the rope might be rotated by some offset I need to account for.

Working through the geometry of the large arc: with radius 57.5 connecting the two points, I'm computing the chord length and using it to find how far the arc's center sits from the chord's midpoint, since the chord is nearly twice the radius (close to a semicircle).

Since sweep=0 means the arc goes counterclockwise visually, passing from left to right through the bottom, the arc should bulge toward the perpendicular direction (-0.427,0.904), meaning it curves downward from the chord.

Checking the free-end direction from P2 to the far point gives roughly (-0.334, 0.943), which seems to point the same way as the bulge rather than opposite, so something's off with my sweep assumption — I should verify by checking that the radial vector at P2 is actually perpendicular to the tangent line.

Correcting my radial assumption, I find the center should instead satisfy the perpendicularity condition with the opposite sign, giving center (155.3, 62.3), which checks out against the distance to P2. Recomputing the chord length and offset from this corrected center, I get a midpoint around (157.77, ...) with a small perpendicular offset of about 5.87.

Working through the geometry, I confirm the arc bulges clockwise from P1 to P2, with the center positioned so the bulge direction is roughly (0.427,-0.904) — establishing that local "up" for the wrap corresponds to that same direction.

I'm checking rotation angles: the local up direction gives roughly -64.7°, needing about -25° rotation to align with vertical, but when I check against the tangent line direction at P1 (-58.9°) instead, I get a different rotation estimate of about -31.1°. These two methods aren't agreeing, so I need to figure out which reference is actually correct for aligning the dead-end line vertically.

Rotating by -35° doesn't make things line up vertically either, so that theory seems off. Checking the free end's direction against line 1, there's an 11.6° slant mismatch between them, so they're not parallel.

I need to pin down rotation using consistency between the rope's big arc center and the dead-end hole. The big arc center in local coordinates is (155.3,62.3) and the hole is (112.56,123.37), giving a vector of length 74.5 which matches my earlier calculation. Since the world target vector should point straight down, I need to find the rotation angle that takes the local vector's 125° angle to 90°.

That gives roughly 41 over 91, about 65.7° from horizontal, or 24° off vertical — consistent with a slanted dead end. Now I'm working out the small arc's center by finding the radius vector perpendicular to the tangent direction at the start point, testing which sign matches the sweep flag.

Tracing the clockwise sweep: moving south along the path, clockwise visually means turning toward west, so the center sits to the west of the start point. Computing it gives C2=(49.81,213.08), and checking the distance to the endpoint confirms it lands right at radius 45, so that center checks out.

Converting C2 into local coordinates relative to C1 and rotating shows C2 sits directly below C1 by 184 units, placing the movable wheel hub at roughly (594.07, 388.0) — consistent with the wheel radius plus rope fitting the groove. Now I'm working out the rope's world-to-local translation so C1 maps correctly to (593.97,204.0).

I verify by checking the hole position too: transforming it through the same rotation and translation gives (593.98, 278.54), which matches the collar position (594.15, 278.67) closely enough to confirm the transform is correct.

Now I'm checking the rope's orientation — rotating the free end direction from P2 gives roughly (118.6, 427.4), meaning the rope extends down and to the right at about 15° from vertical, consistent with how the movable wheel should hang. I'm now computing P2's world position by applying the same rotation matrix.

Next I'm figuring out where the free end lands relative to the box, which hangs below the movable wheel — tracking hub position, radius, and strap length to make sure nothing overlaps awkwardly within the 768px canvas. I'm also working out the strap's top hole geometry from its corner coordinates to pin down its exact center.

Working out the vector angle, I find the rotation needed is -125°, and verifying against the stored coordinates confirms this undoes the 125° rotation correctly, matching the expected length of 72.0.

Now I'm computing the strap's translate transform by working backward from the movable hub position at (594.07, 388.0), applying the inverse rotation to find the strap's origin offset, which lands at (586.32, 495.40), placing the small hole at world coordinates (594.07, 460.0). Then I shift to analyzing the hook shape, locating its hole center around (77.05, 12.20) and tracing the straight top edge from (76.89, 5) to (7.47, 53.61).

Verifying the -55° rotation checks out against the coordinates, confirming the hook is a simple bar roughly 12 wide without an inner curl. Now I'm positioning the hook's top hole relative to the strap's small hole to solve for the translation offset.

With T computed as approximately (539.89, 516.12), I'm now tracking the hook's bottom edge in world coordinates — landing around y=540.8 with the arc radius extending the visible bottom to roughly 547. So the hook's bar spans about x±6 around 594, from y≈455 down to y≈547, and I'm treating the shackle's bow as resting somewhere in that lowest region of the hook.

Now I'm working through the shackle's orientation — legs pointing down with holes at top, bow curving at the bottom in a U shape — trying to pin down exactly how it drapes over the hook.

I'm computing the second hole center at (9.0,30.2) confirming E2, then measuring the leg vectors from each hole to the bow curve — getting a length of 40 at roughly 70° angle. I need to figure out the rotation so the legs point straight up and the bow sits above, using the end-to-end separation (length 62, angle -20°) to solve for the correct orientation.

Applying a rotation of -160°, I'm transforming E1 and E2 into the new coordinate frame to check their positions, finding E1 lands near (-60.12,-31.46) and E2 near (1.87,-31.48).

Correcting my earlier mix-up, I confirm E1 is on the left and E2 on the right, giving a leg separation around 62 units. Now I'm applying the same rotation to the bow endpoint B1, placing it at roughly (-60.13,-71.45), so the legs run vertically from about y=-31.5 to y=-71.5, a span of 40.

Transforming B2 and the two bezier control points, I get the bow's curve running from (-60.13,-71.45) through controls at (-60.13,-94.46) and (1.87,-94.46) to (1.87,-71.46), and I'm now evaluating the cubic at its midpoint to check the curve's peak height.

Working through the midpoint gives y'≈-88.71 for the bow centerline at the top, so with a stroke width of 17 (half-width 8.5), the inner surface of the arch sits around -80.2 -- that's the resting point where the hook's lowest part should contact the bow.

Now I need to figure out the hook's actual lowest point after rotation, tracing through the rounded end geometry with its radius-6 arc to find where that bottom edge lands.

Solving for Ty gives 621.2, then Tx comes from centering the bow x-coordinate at 594.07, yielding 623.2. From there I compute the leg end positions, landing around y=589.7 with the legs 62 apart horizontally, then I need to find the small lid holes flanking the blue half-disc on the box to align them underneath those leg ends.

Averaging the hole marker points gives hole 1 around (151.6, 51.7) and hole 2 around (207.8, 77.9), separated by exactly 62.0 units — matching the shackle span nicely. Now I'm checking whether the blue half-disc's chord lies along the lid edge connecting these two holes.

Checking the chord endpoints (155.8,42.6) and (212.0,68.8) against the box's top edge running from (84.2,9.2) to (283.6,102.2): plugging in x=155.8 to that line's equation gives y=42.6, confirming the chord sits exactly on that edge, with the arc bulging inward into the box.

The two small holes sit near the chord's ends rather than strictly flanking it, and I'm noticing a blue parallelogram strip near the same top edge plus a diagonal line running from (183.9,55.7) to (113.8,206.2) that looks like the box's center divider. This suggests the top edge (84,9)-(283,102) is the lid, with similar small blue half-discs likely marking other edges/corners of the box.

Measuring the box dimensions: the top edge length comes out to about 220, and the side length (from roughly (283.6,102.2) to (226.7,247.8)) is about 156, giving a box of roughly 220×156 with rounded corners. The top edge's rotation angle is about 25°, so I'd need to rotate by -25° to level it before placing the lid properly.

Applying this rotation to both holes confirms they land 62 apart at a consistent height, matching the shackle spacing, so I translate the local hole positions to align hole1 with E1, giving a box offset of about (403.87, 606.92), and verify hole2 lands at 625.09, matching E2.

Checking the box extents now: computing the rotated corners gives a height of roughly 166 and width extending from about x=474 to x=714 in world coordinates, with the bottom edge around y=745.7, which fits under the 768 limit but is tight with stroke width considered.

The free rope end lands around (768,616), staying clear of the box's right edge at 714 and not overlapping the wheel, so no collisions there. For the beam, I'm placing it with its underside at y=98 (accounting for stroke), putting the bracket plate's edge center at (594,98).

I'm confirming the bracket top plate stays within the beam's x range (520-668 fits inside 305-883), checking the fixed wheel sits comfortably at y=140, and making sure everything stacks vertically within the 768 bounds. Now I'm working through the rotation values assigned to each element—strap, hook, shackle, box, bracket, rope—then computing the movable wheel's hub center from its four corner points.

Calculating the hub center more precisely: radius checks out at about 52, and after applying the translation I land on center coordinates around (537.12, 331.05), then refining the rope endpoint calculation to get (594.03, 388.03), which adjusts the movable wheel's translate to (537.08, 331.08).

Now I'm working through the strap, hook, shackle, and leg positions in sequence—each piece's translation derived from the previous anchor point—ending with the box translate at roughly (403.81, 606.80). I'm noting the drawing order should start with the beam.


````

## Answer

````text
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1376 768">
<use href="#kit-beam" transform="translate(300,30)"/>
<use href="#kit-bracket" transform="translate(596.96,303.84) rotate(-140)"/>
<use href="#kit-fixed_wheel" transform="translate(525.03,135.06)"/>
<use href="#kit-movable_wheel" transform="translate(537.08,331.08)"/>
<use href="#kit-rope" transform="translate(431.01,242.04) rotate(-35)"/>
<use href="#kit-strap" transform="translate(586.28,495.43) rotate(-125)"/>
<use href="#kit-hook" transform="translate(539.85,516.15) rotate(-55)"/>
<use href="#kit-shackle" transform="translate(623.16,621.04) rotate(-160)"/>
<use href="#kit-box" transform="translate(403.81,606.80) rotate(-25)"/>
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
