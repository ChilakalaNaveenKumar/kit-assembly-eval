# A · pulley · claude-sonnet-5-5 · trial 1

- Result: **PASS**, score 1.00, tags: pass
- Model version: `claude-sonnet-5-5`, response id: `msg_vrtx_011CgrVTFFmRJWYBZ52oQDg8`
- Started 2026-11-08T20:32:05-0500, finished 2026-11-08T20:34:25-0500, 140.5 s, attempts 1
- Tokens: input 6,671, output 17,661 (thinking not reported separately by this provider)
- Settings: `{"provider": "anthropic", "route": "vertex", "max_tokens": 128000, "thinking": {"type": "adaptive", "display": "summarized"}, "output_config": {"effort": "high"}}`, prompt sha256 `fb51e84f957061389e1cf34461222a2bdcfd9c392286360d6e86ad372bca9ca1`

## Failed checks

- none

## Thinking summary (as returned by the provider)

````text
I'm mapping out the geometry of each component: the horizontal beam, the pulley block housing with its sheave cutouts, the angled mounting bracket with its holes, plus the fixed wheel, hook, movable wheel, and rope that connect them.

I'm working through the geometry, converting the hole positions into the box's local rotated coordinate frame to figure out exactly where they sit relative to the box's long and short axes.

I'm trying to figure out what this box actually represents—maybe a pulley block housing with two wheel axles, but the spacing doesn't quite match the wheel radii I calculated. The corner wedge shapes and semicircle cutouts are confusing me; they could be bolt holes or some kind of bracket detail rather than functional wheel mounts.

Reconsidering the whole assembly: perhaps this is a load crate hanging from a hook, with the two top holes serving as attachment points, connected to a beam-mounted bracket that holds a fixed pulley wheel via a pin at one end.

That big hole likely houses the fixed wheel axle, matching its hub radius exactly. The strap component has its own holes sized to grip the movable wheel on one end and connect to the hook/shackle assembly on the other, so I'm mapping how these pieces chain together mechanically.

The rope seems to end at a mounting point, and I'm trying to reconstruct the whole pulley system: rope tied off at a fixed support, running down around the movable wheel, back up over the fixed wheel, and down to the pulling end, with the load hanging from the movable wheel through the strap, hook, and down to the box. The beam itself has no holes and appears to be a ceiling support with hatching on top, so the bracket's rounded pink ends with their small holes are probably what actually fasten to the beam.

I'm trying to trace the bracket's actual geometry from these vertex coordinates, figuring out whether it's a simple bar shape or more of an L/V-shaped piece connecting the pink bolted end to the far hole.

Looking closer, it seems to resolve into a triangular gusset with three corners: the pink end, a right-side point around (183,105), and a bottom point near (76,200), with a small hole positioned along the left edge near the pink end.

Leg 2 has no hole, but there's a larger r=9 hole near the pink end on leg 1 — maybe for a wheel axle, with the pink end itself serving as a hinge pin to the beam. I'm unsure how the bracket actually connects to the beam though, since the beam itself shows no distinguishing feature — the grader might define that connection point in coordinates I can't see.

I'm also noting the rope's hole at its starting point, which seems to mark the beginning of its path before it stretches down to a free tail further below.

Tracing the path, the rope dips down and loops around the movable wheel at a radius matching the groove's midpoint, then rises up and over the fixed wheel's groove radius before dropping to its trailing end—confirming both wheels are threaded correctly along the rope's route.

Now I'm working backward from the arc endpoints and radius to pin down the fixed wheel's actual center coordinates, using the chord length and the known radius to compute the perpendicular offset from the midpoint.

Confirming the tail direction perpendicular check works out, I move to the movable wheel: solving for its center using the arc radius of 45 between the two given points, verifying the perpendicular distance matches, and arriving at a candidate center around (49.75,213.07) for the larger arc that wraps around the bottom.

I'm checking whether that rope hole at (113,123) actually matches the pink bracket's hole, since the rope's pink color (#FEB8A7) seems to tie directly to the bracket's pink end — suggesting the bracket's hole is the rope's anchor point, and its other hole holds the fixed wheel's hub.

Computing the vector between the bracket's two holes versus the vector between the rope's two anchor points, I get matching lengths (~73.7 vs ~74.0), confirming these correspond to the same physical connection, just rotated differently between the two local coordinate systems.

Now I'm trying to figure out how the bracket actually mounts to the beam and orients the fixed wheel—its L-shape has one leg against the beam but no obvious hole there, so the beam attachment might just be a flat seated contact rather than a bolted joint.

Computing the angles more precisely, it looks like the triangle has a narrow ~14° tip at pink point A, with the base angles at B and C both around 83° — so it's an isosceles shape with its apex at the pink corner.

This suggests the base BC (length ~148) sits flush against the beam while the pink apex points downward, away from it. The wheel hole near (66,74) would then sit close to the apex, roughly 73 units from it along the perpendicular distance from A to line BC, which I'm calculating using the line's direction and normal vectors.

I'm now working out how far the wheel hole sits below the beam — about 100 units from the base — with the rope and pink eye positioned at the apex. Now I need to figure out the rotation needed to orient the bracket correctly, since the vector from the base to apex needs to point straight down (90°) but currently points at roughly -130°, so I'm computing the rotation angle to align it.

Checking the bracket's stored rotation of 140° confirms the un-rotation is correct, and rotating the hole vector by -140° places the wheel above the pink eye by about 73.7 units — consistent with the apex pointing down and the wheel hanging above it.

Working out the rope's rotation (-35°) to align the fixed wheel center correctly, then checking the tail direction angle of roughly 74.5° — this seems off from vertical, so I'm reconsidering the tangent point geometry where the rope meets the wheel's edge.

Working through the rotation confirms the fixed wheel center lands directly vertical from the rope hole, and the movable wheel center also ends up exactly below it by 109.5 units—so the whole rope assembly aligns vertically, with the rope continuing down toward the other anchor point.

Now I'm setting up the beam's position, placing its bottom edge against the bracket base and preparing to translate it with offsets tx, ty at zero rotation.

Calculating the tail's end point based on its rotation angle, I get it landing about 512 below the beam bottom, so with the beam placed around y=100 the tail reaches roughly y=612 — fits within the 768 canvas. Now I'm turning to the movable assembly, starting with the strap holes that will hold the wheel hub.

The strap has a big hole for the wheel hub and a small hole at its narrow end, which should connect to a shackle rather than directly to the load. Checking the shackle's two hole positions, their spacing matches the spacing between the box's top holes almost exactly, so the shackle must bolt onto the box as a U-shaped bracket, forming the link between the strap and the load.

I need to check which features align within a few pixels: the hook hole matching the strap's small hole, and the hook's rounded tip matching some other part's center. I'm also considering whether the box's top holes (accounting for its 25° rotation) connect to the shackle ends instead, and trying to figure out what the hook ultimately attaches to among the nine parts.

Looking at the hook geometry more closely, it's really just a straight bar about 85 long with a rounded end (r=6) on one side and a hole (r=4) on the other — so it's actually a link bar rather than a traditional curved hook, with the hole end likely connecting into the shackle.

Now I'm wondering about the box: it has small holes at two points and blue wedges at the rounded corners plus some midpoint cap windows, which makes it look more like a crate with corner reinforcements rather than a pulley block housing.

The shackle's hole spacing (62.7) nearly matches the box's hole spacing (62.0), which suggests the shackle's two ends bolt directly onto the box as a lifting lug, rather than connecting through the hook or strap. That reframes the chain of connections — the strap and hook link elsewhere, while the shackle's U-shape spans across the box's two mounting points.

Computing the midpoint of the bezier curve gives roughly (57.7, 73.4) for the bottom of the U-loop—this could be where the hook's rounded end center sits when it hangs through the shackle eye.

Now I'm trying to reason through the actual part connections: the hook likely has a pin hole with radius 4 at one end and a rounded end with no hole at the other, while the strap has a large axle hole and small pin hole. I'm working out whether the hook's pin hole connects to the strap's pin hole, and whether the hook's rounded end connects to the shackle, with the shackle and box each having two small holes forming additional links in the chain.

I'm second-guessing the hole connections again—maybe the shackle links to the strap's small hole while the hook goes to the box, or the hook's round end could even sit over a box hole like a pin head. It's genuinely ambiguous, so I'm trying to recall the typical generator layout for a two-wheel pulley hoist: beam, bracket, fixed wheel, movable wheel, strap/yoke, and how these pieces normally stack together.

Now I'm working out the orientation of the shackle relative to the box—figuring out which way the U-shaped loop bulges so it extends upward away from the box when hanging, and calculating the rotation angle needed based on the hole and bulge coordinates.

I'm also considering where the hook tip should actually rest within the shackle's loop—whether it bears against the top of the bulge curve or somewhere in the middle of the eye—since that determines the physical contact point for hanging the hook through the shackle.

Now I'm working out the positioning transforms, placing the beam so it spans a specific horizontal range and sits at a chosen height, then figuring out where the movable components need to align relative to the beam's bottom edge.

Trying ty=10 instead: box bottom lands near 715, which works better. Now I need to pick a horizontal position for the beam and bracket — shifting the beam over with tx=100 gives a center around 394, and I'll center the bracket's base roughly there too, though the exact beam-bracket connection point is still uncertain.

Since the bracket's only real anchor points are those two holes, and the pink hole radius matches the rope hole radius, I'll treat the pink eye as the rope attachment and just seat the bracket against the beam. Now I'm computing the bracket's world transform — rotating it -140 degrees locally then translating so its pink hole lands at the target world coordinates.

I'm averaging arc endpoint coordinates to pin down the pink hole center at roughly (18.58, 17.47) and the wheel hole center at roughly (66.46, 74.54), then checking that the vector between them has length and angle matching the known rope dimensions (74.5 length, 50° angle — confirmed). Now I'm setting up the base line equation so I can solve for the translation that places the bracket's base flush against the beam's bottom edge.

So the pink point sits 106 below the beam bottom. Checking the foot projection along the base, I find it lands exactly at the midpoint between the two endpoints, confirming symmetric isosceles geometry. Now I'm setting up the rotation matrix for a -140° world rotation to verify how the base normal transforms.

Verifying the rotation confirms the normal points straight down, which checks out. Next I'm placing the pink point's world coordinates based on the beam's vertical offset, then stacking the hanging components downward—strap hole, hook end, and shackle holes—to trace the full chain length from that anchor point.

Setting ty=0 instead gives a bit more margin, so I'm placing the beam at translate(100,0) with the bottom edge at y=68, which puts the pink anchor point at (394, 248.5). From there I'm constructing the bracket's transform as a translate-rotate-translate sequence centered on that anchor, then working out the rope's rotation around its hole's local center point.

I'm now verifying the rope hole position by averaging its four corner coordinates, then checking my rotation math against the fixed wheel location — confirming the rotated vector lands the bracket hole at world coordinates (394, 174), which matches the fixed wheel's position, and now locating that wheel's hub center from its four corner points.

Next I'm computing the movable wheel's center position at (394, 358) and finding its local hub center from the four corner points, to figure out the translate offset needed to place it correctly.

Then I'm locating the strap's two hole centers from their corner coordinates and computing the vector and angle between them, which I'll use to determine the correct rotation so the small hole aligns properly.

Now I'm working out the hook geometry, finding the hole center and the round end's center from its arc, treating the chord as the diameter to pinpoint the center location.

Then I'm computing the needed rotation so the hook hangs vertically below the strap hole, confirming the wheel-strap-hook chain lines up collinearly, and setting the transform accordingly.

Next I'm moving on to the shackle component, locating its hole centers from the coordinate pairs to establish its own positioning.

Computing hole2 position as 62 units right of hole1, giving world coordinates (363,568.05) and (425,568.05), then verifying the transform translate-rotate-translate maps the bulge and hole midpoint correctly back to the hook end point.

Now checking the box's hole positions from averaged corner points: hole1 at roughly (151.6,51.7) and hole2 at (207.8,77.9), giving the same 62-unit spacing but at a 25° angle, which I need to correct so hole2 sits directly to the right of hole1 horizontally.

I'm rotating the box by -25° so its body hangs below the hole line on the +v side, confirming the box transform is translate to world position, rotate -25°, then translate back by the hole1 local coordinates, and computing where hole2 lands under that rotation.

Checking the box spans within the canvas bounds (roughly y 568 to 708, x 289 to 509), then tracking where the rope's tail end lands, starting from the tangent point off the fixed wheel and heading down-right at its slope angle.


````

## Answer

````text
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1376 768">
<use href="#kit-beam" transform="translate(100,0)"/>
<use href="#kit-bracket" transform="translate(394,248.5) rotate(-140) translate(-18.58,-17.47)"/>
<use href="#kit-fixed_wheel" transform="translate(325.06,105.06)"/>
<use href="#kit-movable_wheel" transform="translate(337.05,301.05)"/>
<use href="#kit-rope" transform="translate(394,248.5) rotate(-35) translate(-112.55,-123.37)"/>
<use href="#kit-strap" transform="translate(394,358) rotate(-125) translate(-83.53,-67.94)"/>
<use href="#kit-hook" transform="translate(394,430) rotate(-55) translate(-77.05,-12.21)"/>
<use href="#kit-shackle" transform="translate(394,510.75) rotate(-160) translate(-57.7,-73.4)"/>
<use href="#kit-box" transform="translate(363,568.05) rotate(-25) translate(-151.59,-51.68)"/>
</svg>
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
