# B · pulley · claude-sonnet-5-5 · trial 2

- Result: **PASS**, score 1.00, tags: pass
- Model version: `claude-sonnet-5-5`, response id: `msg_vrtx_011CgrVTEtSKjgMBn9igU7v9`
- Started 2026-11-08T20:32:05-0500, finished 2026-11-08T20:34:43-0500, 157.9 s, attempts 1
- Tokens: input 6,683, output 18,013 (thinking not reported separately by this provider)
- Settings: `{"provider": "anthropic", "route": "vertex", "max_tokens": 128000, "thinking": {"type": "adaptive", "display": "summarized"}, "output_config": {"effort": "high"}}`, prompt sha256 `0eb4a228ba7e95b6b6657247f40030cf1c9e960d98e122abe06db12d8d862842`

## Failed checks

- none

## Thinking summary (as returned by the provider)

````text
I'm identifying the components: p08 is the ceiling beam support that the hoist hangs from, hatched on top to indicate the mounting surface, while p01 appears to be an elongated rounded pulley block frame.

Looking at the corner coordinates, p01 forms a rotated rectangle about 230 by 146, tilted roughly 25 degrees, with two small mounting holes near the top edge and a line running down the middle that could be a center divider or load indicator — possibly suggesting p01 is actually a crate-like load rather than a housing piece.

Now I'm piecing together the rest of the assembly: this looks like a block-and-tackle hoist with two wheels (p04 and p05 as pulleys), a bracket piece (p02), a link plate (p03), a rope with a looped eye (p06), a U-shaped hook strap (p07), and possibly a crank handle or wrench-like part (p09) with a grip. Overall it's shaping up to be a ceiling-mounted pulley hoist system with a hanging bracket, upper and lower wheels, rope, and load.

Maybe p09 is a wall bracket with a pink round end holding a hole. I'm trying to piece together the hoist assembly: a beam, a fixed wheel bracket, a movable wheel with a hook sling, a crate load, and a rope path that loops and arcs through several points, likely wrapping around both pulley wheels before anchoring somewhere.

The arc radii line up nicely — the 57.5 radius matches the groove of the upper wheel p05, and the 45 radius matches the lower wheel p04, confirming the rope wraps around both pulleys as part of a block-and-tackle system. The rope's starting point near a small hole suggests it's anchored to a fixed point before running down and around the lower wheel.

Now I'm computing the tangent directions and arc centers for each segment to figure out exactly where the rope wraps around each pulley and how the geometry fits together.

Now I'm computing the upper wheel's arc center, trying the left-turn direction formula and checking it against both endpoints to verify the radius matches—first attempt gave inconsistent distances, so I'm correcting the perpendicular vector sign and recomputing.

Distance works out to 184, consistent with the hoist geometry. Tracing the rope path: the anchor end near (112,123) runs down to the lower wheel's right side, wraps under it, then crosses to the left side heading up toward the top wheel.

I'm figuring out where this rope ties off — likely anchored on the fixed bracket holding the top wheel, since standard two-pulley hoists fix one end there and run it down around the movable pulley before coming back over the top. I'm checking which piece (maybe p01, with two holes spaced 62.6 apart) would serve as that fixed anchor bracket.

Checking the geometry, the two holes sit symmetrically about the center line, roughly 62-63 px apart and 8-9 px from the line's top point, suggesting a crate hanging from two symmetric attachment eyes. I'm now looking at piece p07, which appears to be a U-shaped strap with holes at its two ends.

Tracing the strap's path, it forms a loop rising from the two crate holes rather than hanging below them, roughly 63 wide and 40 deep — possibly a hanger that the lower pulley's hub sits within. I'm now checking whether p02's bracket, with its larger hole, could actually be that wheel axle instead.

Going through parts again: wheels p04/p05, rope p06, crate p01, strap p07, brackets p02/p09/p03, base p08 — nine total. I'm working out how p03 connects, likely anchoring to the beam at one rounded end while its other end ties into the rope.

p02 looks like a bracket holding a wheel, with a hole 9 for the axle and hole 4 at the other end for a pin. p09 seems to be a longer arm with its own axle and pin holes, and I'm tracing out its actual polygon shape now to confirm the geometry.

I'm wondering if the pink coloring signals a pin or anchor point for the rope mechanism rather than just decoration. I'm also cross-checking wheel radii and rope segment geometry — comparing p05's larger radius against p04's smaller one, and tracing the distance and direction between their centers to understand how the rope wraps between them.

I'm now calculating the rope anchor point's position relative to both wheel centers, trying to pin down the exact distances so I can confirm how the rope is tangent to the lower wheel and where it terminates near the upper assembly.

Breaking down the vector into axial and lateral components along the line between wheel centers, I find the anchor falls almost exactly on that axis — zero lateral offset — meaning it's attached somewhere along the straight line connecting the two wheels rather than offset to one side, likely fixed to a bracket at one end or the other.

Checking p02's hole distances to see if it matches the 75px measurement to the upper wheel, I'm recomputing hole centers more precisely by averaging the arc coordinate points for hole 9 and hole 4.

Checking that endpoint against the arc confirms the geometry works, but the anchor-to-upper-center distance of 74.5 doesn't quite match the expected 72, so I'm reconsidering whether this really is a single consistent assembly or if I'm misreading which bracket connects where. Maybe I should reconsider the overall structure as a two-wheel pulley hoist with a ceiling beam rather than forcing this particular distance to match.

Actually p09's hole 9 at the upper wheel axle and its pink hole 4 give exactly the 74.5 distance I need, so p09 is likely the upper bracket with the wheel mounted there and the rope end pinned at the pink hole.

I'm now checking how this bracket attaches to the beam, since its body shape extends away from that hole line toward other extents — trying to figure out which direction is "down" toward the anchor versus where the plate's arms extend relative to the wheel center.

Tracing the remaining edges, this looks like a triangular hanger plate — the apex points down with a rope anchor, while the shape widens upward to two feet that attach at the beam, with a wheel hole set in the middle.

The feet seem to rest against the beam's underside with no bolt holes, so p09 must be oriented by rotating the up-vector to align with screen-up. As for p03, it looks like a separate rounded piece with a single hole, maybe a bolt or clamp component.

Moving to the remaining parts: p04 is the lower wheel, with p02 serving as the bracket holding it via hole 9 for the axle and hole 4 positioned 72 units from the wheel center, likely toward a load hook. The rope anchor sits 74.5 below the upper wheel and 109 above the lower wheel, giving a total wheel separation of 184 based on the rope geometry.

Now I'm tracing where p02 connects to p07 — p02 is a link plate with hole 4 near one rounded end and the wheel hole at the other, but p07's strap holes (63 apart) don't match p02's hole directly, so I'm checking whether p07's loop attaches elsewhere or whether p03's hole 4 at (77,12) is the actual connection point instead.

Working through the full chain geometrically: the crate hangs below the lower wheel, so the sequence likely runs from the wheel hub through p02's hole, down to p03 (hole 4 at the top, rounded end 85 units below), then possibly into p07's strap loop before reaching the crate — trying to see if p03's rounded end center matches a feature on another part to confirm the link.

I'm working out p07's loop geometry, computing the hole centers from their corner points and tracing the path between them to find the direction vector and perpendicular for the strap's curve.

So the apex sits 57 units above the chord midpoint, meaning the strap loop rises well above the crate holes. I'm trying to figure out whether p03's rounded end actually corresponds to this apex, but the apex isn't a true endpoint of the curve, so maybe p03 connects to something else entirely, like the beam itself.

I keep testing connection chains instead: perhaps p02's holes link the wheel hub to p03, with p03's rounded end sitting some distance away from its own hole, rather than p03 touching the strap apex directly.

I'll settle on p03's round end seating at the strap apex. Now I'm trying to work out the full vertical stack of the assembly—beam, upper wheel, lower wheel, crate holes—adding up the offsets between each component to estimate total height.

Fits within canvas, I think, but now I need to double check whether the wheel axis between the two wheel centers runs truly vertical, since that determines how the rope path should be laid out in this configuration.

Checking if the rope could instead hang with the free end flipped: rotating so u points up by -35° works, and tracing the free end direction confirms it swings down-right from the top wheel's right side, consistent with the layout.

Checking the feet positions confirms the axis is vertical since they're symmetric at ±73 around it. Working through the anchor-to-wheel tangent geometry, the 24° tilt from vertical matches the asin(45/109) calculation, confirming the anchor sits on-axis rather than at the wheel's edge, and the p04 wheel radius checks out against the rope rim range. Now I'm moving on to computing the actual transforms.

Now I'm positioning the beam element, centering it horizontally on the 1376px canvas and picking a vertical offset so the bottom edge and hatching line up with the ceiling placement.

For the wheel geometry, I'm figuring out where the feet attach by checking the polygon edge between the two foot vertices—verifying it's perpendicular to the "up" direction, confirming this edge is the flat connecting line between both feet.

Now I'm tracing through the notch cuts in the polygon, trying to identify which edges form the thickness of the support plate between the two triangular leg sections.

So it's just a solid triangle shape with corners slightly notched, apex pointing toward the pink end, flush against the beam bottom with the top edge centered at length 148. Now I'm figuring out the wheel center position, placing W1 at (688,185) with radius 64, checking how it sits relative to the triangle.

Then I'm computing the beam bottom position at y=78, placing the anchor point 74.5 below the upper wheel at (688,259.5), and the lower wheel 109.4 further down at (688,369), confirming the separation matches the rope length of 184. I'm setting up a rotation transform of -35° to map the upper wheel's local center to its position in the scene, and verifying the anchor point maps correctly under that rotation.

Now I'm double-checking the precise angle by recomputing the lower center using the direction vector of the segment, working through the normalized components to pin down the exact coordinates.

The axis from lower to upper gives an angle of exactly -55°, confirming the -35° rotation. Now I'm moving to hole p09's transform, needing to figure out the rotation that maps its up vector to point straight down, starting by locating the center point for that hole.

The rotation checks out at -140°, placing the anchor roughly 74 units below the wheel center. I'm now working out the transform chain: translate to the wheel position, rotate by -140°, then translate back by the wheel's original center, so the rope anchor lands close to the pink hole location around y≈259.

I'm also verifying that the beam's top edge sits at y=78.1, matching the expected 78, and computing hole 9's center by averaging its four corner points, landing on (68.94, 68.94).

For the wheel pieces, I'm translating p05's hole center to position (619.06, 116.06), and p04's hole center to (631.05, 312.05), then confirming the rope length checks out at 184 units by verifying it reaches y=369 when rotated straight down. Now I'm working out how to rotate p02 so that hole 9 aligns with point L while hole 4 lands directly 72 units below it.

Computing hole 9's center from its four corner points gives (83.53, 67.94), and hole 4's center comes out to (24.55, 26.64). The vector between them has length 72 as expected, with an angle of 215° from hole 9 to hole 4, so I need to figure out the rotation needed to point that vector straight down.

Moving to p03, I'm computing the hole center from its four points and the rounded end center from its bounding arc, getting a vector of length ~80.75 at 145°, meaning I need a -55° rotation to orient it downward—matching the given parameter.

I'm now checking whether this length is consistent with the overall strap geometry relative to the crate above, then starting to compute the crate's own hole centers from their point sets to find its local rotation.

Checking the down direction confirms the crate's top edge is where the holes sit, with the divider line running from holes midpoint to center about 73px — roughly half the crate's height, so the holes appear very close to the top edge rather than centered.

Working through the perpendicular distance, I get about 83 for the half-height, placing holes roughly 10 below the top edge. That puts the crate's vertical extent at around 166 total, with the bottom edge about 156 below the holes.

Checking against the 768 boundary, this fits but it's tight, so I decide to shift everything by -10 to tighten the layout further, repositioning the beam, hatches, and strap elements accordingly. I'm now recalculating the shifted coordinates for each component including the apex point for p07.

Verifying the apex calculation: using the chord midpoint and perpendicular direction vector, I confirm the dot product checks out at 57.3 units from the chord midpoint with zero lateral deviation, so the apex geometry is correct given the 17-stroke strap thickness.

So the crate hole midpoint should land at (688, 569.05) when offset below the apex, which seems reasonable for p03's endpoint placement. For p07, I'm working out the transform that maps the chord midpoint to this new position, rotating the direction vector to align it vertically — translating, rotating by -160°, then translating back — and spot-checking that the first hole lands at the expected relative coordinates.

Crate rotation checks out correctly. Now I'm recalculating the beam, rope, and crate positions with the shift adjustment applied, working through translate and rotate coordinates for each element.


````

## Answer

````text
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1376 768">
<use href="#kit-p08" transform="translate(394,0)"/>
<use href="#kit-p09" transform="translate(688,175) rotate(-140) translate(-66.464,-74.037)"/>
<use href="#kit-p05" transform="translate(619.06,106.06)"/>
<use href="#kit-p06" transform="translate(688,175) rotate(-35) translate(-155.26,-62.34)"/>
<use href="#kit-p04" transform="translate(631.05,302.05)"/>
<use href="#kit-p02" transform="translate(688,359) rotate(-125) translate(-83.5315,-67.9375)"/>
<use href="#kit-p03" transform="translate(688,431) rotate(-55) translate(-77.055,-12.21)"/>
<use href="#kit-p07" transform="translate(688,569.05) rotate(-160) translate(-38.127,-19.599)"/>
<use href="#kit-p01" transform="translate(688,569.05) rotate(-25) translate(-179.686,-64.777)"/>
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
