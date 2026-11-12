# C · desk_lamp · claude-haiku-5-5 · trial 2

- Result: **FAIL**, score 0.67, tags: fail, wrong connection (far off), failed:joint, failed:orient
- Model version: `claude-haiku-5-5`, response id: `msg_vrtx_011CgrW8ozLo1cZQjtapLvpo`
- Started 2026-11-08T20:41:00-0500, finished 2026-11-08T20:46:44-0500, 343.3 s, attempts 1
- Tokens: input 25,614, output 74,433 (thinking not reported separately by this provider)
- Settings: `{"provider": "anthropic", "route": "vertex", "max_tokens": 128000, "thinking": {"type": "adaptive", "display": "summarized"}, "output_config": {"effort": "high"}}`, prompt sha256 `689a4396384fecc622c40e22b79c109d3476055cadb95a2c4780b04cd6699670`

## Failed checks

- Lower arm: its bottom end hole on the l bracket's upright pin hole (within 6 px): error 83.11 (tolerance 6)
- Bulb: its screw cap on the shade's socket at narrow end of cone (within 6 px): error 105.09 (tolerance 6)
- L bracket faces the way it does on the working object (within 8 deg): error 90.0 (tolerance 8.0)

## Thinking summary (as returned by the provider)

````text
I need to work out the geometry of each assembly part, starting with the kit base's flat outline and dimensions to understand its shape and boundaries.

So the base slab spans roughly y 5 to 47 and x 5 to 280, with a flat top edge and a small notch recess near the middle. Since it's stored upright, I'll keep it at identity rotation and just translate it into position on the canvas, placing the top around y=605 so the bottom lands near 647.

Now I need to figure out the overall lamp height combining the arm lengths, then move on to parsing the L-bracket piece's outline coordinates to understand its shape — the foot, bend, and tip points of the L.

No explicit arc paths in the l_bracket listing, so the holes must be the inner ring outlines instead — I'm scanning those coordinate loops to locate where the pin holes actually sit.

I'm also tracing the lower arm's two end holes (top near x≈21, y≈20 and bottom near x≈52, y≈345, roughly 325 units apart) and now trying to pin down the upper arm's hole positions near x≈330.

Comparing the upper arm's two end circles, roughly 20,20 and 329,164.5, giving a length near 341. Then I'm checking the elbow plate's three circles to figure out which is the left, right, and bottom mounting hole.

I'm trying to match hole radii between the upper arm and the head plate — since both have a 2.5 radius hole, that's likely the pivot pairing, with the small hole at (36.5,36.7) on the head plate being the match for the shade lug hole.

Now I'm examining the shade's geometry to figure out if it's a cone shape, tracing its outline points to identify which edge forms the narrow end versus the wide rim.

I'm now tracing the socket cylinder extending from the narrow end of the cone, and spotting what looks like a lug hole on a small rectangular tab near the shade's neck, possibly for attaching the head plate.

Averaging those four arc points gives a lug hole center around (168.6, 176.1). Now I'm checking the bulb's screw cap, a small circle near (15,19) with radius about 2.5, trying to figure out whether that's the contact rivet or the cap itself.

Tracing the bulb outline, I can see the rounded globe body spans roughly x=37 to 180 with the neck/cap tapering off to the left around x=5-65, matching the curve of a typical light bulb silhouette.

I'm tracing the bulb's neck running diagonally up-left toward the threaded base, with the small circle near (15,19) likely marking the screw cap contact point where the bulb connects to its socket.

Given the overall complexity, I'm stepping back to lay out the full assembly logically: base at bottom-left with an L bracket, lower arm hinged at the bracket's upright pin, an elbow plate connecting to the upper arm, a head plate holding the shade via hole A, and the bulb seated in the shade's socket.

Now I'm working through the specific hole-to-hole distances linking each component—bracket pin to lower arm, lower arm to elbow plate's three holes, elbow plate to upper arm, and upper arm to head plate—computing approximate separations to keep the chain geometrically consistent despite the tight pixel tolerance.

Beyond distances, I need to figure out rotation for each part so the lamp reads as upright and natural: base at the bottom, L-bracket vertical, arm angling upward, bulb facing down, shade opening downward, all oriented correctly relative to the base rather than arbitrary stored angles.

Tracing through the outline coordinates more carefully, it looks like a thick diagonal arm stretching from the upper-right down to a rounded foot shape at bottom-left, with the stroke widening near the base.

Actually it reads more like a triangular bracket shape — a long diagonal member running from top to bottom-left, with an arm extending right to connect near the top-right. The hole outlines don't look like simple circles, so I'm reconsidering whether there are any pin-hole arcs in this bracket at all.

I'm trying to locate the pin hole on the bracket's upright, tracing the diagonal strip from roughly (40,8) to (25,97) and checking the inner boundary path to see if the hole sits near the center of that strip's cross-section.

Looking more closely, I think the lower arm is actually a long tapered bar with holes at each end - one near the top around (21,20) and one near the bottom around (52,345), narrowing as it goes from top to bottom.

I need to figure out which end of the lower arm is "bottom" in the assembly sense—the arm connects the bracket at the bottom to the elbow plate at the top, so its bottom end should be whichever local hole attaches to the bracket's upright pin, but I'm unsure if that's the (52,345) or (21,20) hole depending on how the arm is oriented.

Since the bracket sits foot-down on the base with its upright rising up, I need to locate the pin hole in the bracket's local coordinates—likely near the top of the upright rather than the foot—by scanning through its fill subpaths for the small ring shapes that represent the holes.

Still writing path coordinates...

The foot's bottom edge seems slanted rather than flat, which means the bracket sits at a slight tilt on the base rather than square against it — I need to work out that rotation angle from the diagonal upright.

Looking at the outline points more closely, the bottom edge near the rounded corner seems roughly horizontal, suggesting the foot's bottom is meant to sit flat — so the foot is likely the bottom portion of the bracket resting on the base.

Thinking about orientation, the upright axis appears tilted about 11° from vertical, with the top leaning right relative to the bottom. Since the part should face upright on the working object like it would relative to the base, I need to rotate it so that axis becomes vertical, correcting for that rightward lean.

Actually, maybe the foot's bottom edge isn't purely horizontal—checking the outline coordinates, the upright direction runs roughly (-0.188, 0.982), so the perpendicular slope for the bottom edge would be about 0.19, meaning the foot naturally sits tilted relative to the leg rather than flat.

Confirming the measurements: both edges give roughly the same slope ratio, so the upright is indeed tilted about 20° from vertical, leaning toward the top-right.

I'm trying to pin down the exact bottom edge of the upright, but the candidate points are inconsistent and ambiguous. I think it's simpler to treat the bracket as a bent strip and figure out which arm is the upright versus the foot by looking at the overall shape instead.

Looking at the arm extending right from around (51,42) to (119,40-60), its top and bottom edges tilt down at roughly 20-24°, and I notice this direction (0.94, 0.35) is actually perpendicular to the upright's direction (-0.35, 0.94) — confirming this is indeed an L-shaped bracket with the arm meeting the upright at a right angle.

So the corner joint sits around (40,8), with the upright running down to a foot around (20,99), and the arm extending out to around (119,45), giving the L its characteristic perpendicular shape with foot and arm.

I'm guessing the bracket stands upright on the base with its foot flat on top, so the arm sticks out horizontally — but the role of that arm relative to the lamp's lower arm and elbow joint is still unclear; it might just be decorative rather than functional.

I'm tracing which leg is the arm versus the upright by testing how the bracket would sit if rotated—checking whether the corner at top-left with the foot extending toward (119,47) and the upright dropping toward (20,99) matches a plausible orientation.

Actually, that bottom point isn't really a flat foot resting on a base — it's just the leg's endpoint. I need the shape oriented so the horizontal segment sits at the bottom like a foot with the upright rising from it, which means rotating the corner to the bottom instead of the top.

Working out the rotation angle, I calculate that about 160° gets the upright leg pointing straight up and the arm leg pointing horizontally left, which positions the foot correctly at the bottom of the L-shape.

After rotation, the corner sits bottom-right, with the long upright (~95) pointing up and the shorter arm (~85) pointing left as the foot resting on the base. This matches an L-bracket shape, with the pin hole located on the upright near its top.

I need to figure out which edge of the arm ends up facing down after the 160° rotation, so I'm applying the rotation formula to the corner points and checking their resulting orientation.

The arm end's angle versus the corner suggests only a slight 5° tilt, so my perpendicularity assumption was rough rather than exact. Let me re-derive the upright's true axis by locating its actual top and bottom endpoints rather than relying on my earlier eyeballed 20° estimate.

Checking the edges directly: the left edge runs from about (27.6,14.8) to (6,74.1), and the right edge from (51.1,42.4) to (31.7,94.2) — both giving a consistent slope corresponding to roughly 20° from vertical, which matches better than my midpoint vector calculation of 9.7°, so I should trust the edge-based measurement over the midpoint approximation.

That gives a width around 31, which seems a bit wide compared to how the upright looks visually, but I'll keep checking against the top edge measurements to verify.

Checking the slopes confirms both the upright and arm are tilted 20° from vertical/horizontal respectively, and they're perpendicular to each other as expected for an L bracket shape — so the corner sits upper-left with the upright going down-left and the arm going down-right.

Working out the exact rotation angle needed: if I compute the upright direction's angle and rotate by 160°, it snaps the upright to point straight up and the arm to point left, which confirms the natural orientation of the L bracket is corner at bottom-right, foot extending left, upright extending up.

I should double check whether the L is actually meant with the arm vertical instead, since the test only requires parts to face within 8 degrees of their working orientation. Testing rotate(70) or rotate(-110): the foot would end up at the bottom with the upright rising vertically, or alternatively the arm could become vertical if I rotate differently, making the upright swing to lie horizontal on the left instead.

That configuration with corner top-right and upright horizontal doesn't fit since I need the upright pointing up. So comparing two options: rotate(160) makes the 85-length leg the foot with the 95-length upright rising at its right end, while rotate(-110) makes the 95-length leg the foot extending right with the vertical leg at its end.

I'm trying to figure out which leg is actually "upright" versus "foot" by checking for a pin hole feature, but the small contour segments near the arm's end and near the foot end just look like inner notches of the bent strip rather than actual circular holes.

Without a clear hole marker, I'll need to infer the pin hole's location geometrically—it should connect sensibly to the lower arm heading up toward the elbow plate, which in turn connects to the upper arm leading up-right to the head plate.

That dark strip might just be the upright's inner face rather than a hole. I can't definitively locate the pin hole, so I'll have to approximate using the upright's centerline, assuming the grader has specific local-frame coordinates for it.

Looking at the lower arm, it has holes at both ends with a tapered body, while the bracket may instead have its pin location right at the corner rather than a visible circle.

Given this ambiguity, I'll just estimate coordinates as best I can and accept some imprecision, prioritizing hole positions since those are likely graded, along with keeping orientation within the allowed tolerance for each part.

Now I'm working through the lower arm's geometry, averaging the arc endpoints from its circular hole path to pin down the center coordinates.

Top hole lands at roughly (20.7, 20.5), and doing the same averaging for the bottom circle's four points gives approximately (52.2, 345.2). That makes the distance between the two holes about 326.2 units, computed from the dx and dy offsets.

Now checking the tilt direction: the vector from top to bottom normalizes to roughly (0.097, 0.995), meaning the arm tilts about 5.5° off vertical. Moving to the upper arm, I'm averaging the four corner points for its two circles — one centers near (20.5, 20.7) and the other near (328.9, 164.6), giving a length of about 340.4 units between them.

Now I'm trying to figure out which end of the upper arm connects to the elbow versus the head, matching up the hole positions on each plate by averaging their corner coordinates to find precise centers.

Matching radii, the top hole on the upper arm (radius 2.5) lines up with the head plate's small hole at (36.8,36.9), so that becomes the arm hole. That leaves the bigger holes to sort out, trying to match the shade lug hole radius against the head plate's larger hole.

I'm still trying to figure out which of the two big head-plate holes (58.4,96.7) or (100.1,43.3) corresponds to "hole A" versus the shade lug, and I think I need the shade's hanging orientation relative to the head plate to resolve this. Now I'm mapping out the head plate's overall shape, which seems triangular with diagonal edges running between its corner points, before moving on to list out the elbow plate's holes.

Computing the elbow plate's three hole centers by averaging their corner coordinates, I get roughly (89.5,23.9) for the 4.11 hole on the right, (68.6,86.9) for the 2.5 hole at the bottom, and (24.0,38.1) for the 3.82 hole on the left. Checking the pairwise distances between these centers, they come out close to 66-67 units each, suggesting the three holes form a nearly equilateral triangle on the elbow plate.

Now I'm comparing distances between end holes on the lower and upper arm bars to figure out which arm connects to which elbow hole, noting that the radii don't need to match for the holes to be considered connected—only the center positions matter for identifying the correct end of each bar.

Thinking through the overall lamp structure: base, L-bracket, lower arm up to the elbow plate, upper arm from elbow to the head plate, and the shade hanging off the head. I need to figure out the elbow plate's orientation in world space so the lower arm's top hole lines up with the elbow's bottom hole, and the upper arm's bottom hole lines up with the elbow's right hole.

The grader checks that each part faces the correct way within 8°, which applies to the elbow plate too, so I can't just place it arbitrarily—I need to infer which orientation corresponds to the working lamp. I'm reasoning that if the plate's local "bottom" hole is meant to be the lowest point and "right" hole is meant to be on the right side, then the plate's local coordinates might already match the correct upright orientation without extra rotation.

So for each part, I need to infer the assembly rotation from its geometry relative to whatever counts as "correct" orientation. For the elbow plate, I'm trying to figure out which orientation is correct, since its hole triangle has the bottom hole pointing down locally.

If the stored orientation is arbitrary, the plate could be rotated by some angle and its "bottom" hole wouldn't actually face down. The real determining factor is the two connections: the lower arm attaches at the bottom hole and the upper arm attaches at the right hole, and these two connection points together fix the plate's rotation.

Since the arms themselves rotate freely at their joints, the plate's world orientation ultimately depends on the pose the lamp is configured in, and since the elbow plate isn't listed as a free-moving part, I'd expect the grader to require its rotation to match the expected pose within the tolerance.

So rotation is fully determined once those two pin positions are fixed, no freedom there. Same logic applies to the elbow plate: its orientation locks in once the lower arm's top hole and upper arm's bottom hole positions are set.

So each joint contributes its own rotational degree of freedom—lower arm angle sets the elbow position, elbow rotation feeds into the upper arm's placement, and upper arm angle determines where the head plate attaches—forming a chain of rigid bodies each with their own 2D pose to solve for.

Maybe the intended solution isn't fully determined by distances alone, but combined with the ±8° orientation requirement it narrows to a unique pose — so I need to figure out what orientation each part should have based on how it visually "faces" in the reference image.

I realize the base's stored drawing being "upright exactly as stored" suggests its canonical frame matches its drawing, while other parts' drawings may already be rotated arbitrarily from their true canonical upright orientation — so I can't just assume each part's drawing-as-stored equals its intended pose.

I'm stuck trying to infer the exact canonical-to-world rotation transform the designer used for each part, since the random rotations applied to the stored drawings aren't directly recoverable — I may need to just infer the final working pose by consistency across parts rather than solving for the exact angles.

Looking at each part's natural "up" direction, I trace the bulb's axis from its neck to the globe center, since the screw cap end (neck) should attach at the top of the shade's socket while the globe hangs below in the working orientation.

Checking the shade geometry, I'm measuring the wide opening edge versus the narrow end to confirm which side flares out and which tapers down to the socket.

Beyond the cone shape I'm also tracing a rectangular socket section (roughly x 130-228) and noticing a lug tab hanging below it with what looks like a mounting hole around (168.6, 176).

So the shade's local axis runs from the wide opening near x≈12 to the socket at x≈228, meaning the whole shade needs to be rotated roughly -90° in world space so the opening faces down and the socket points up. I'm now working out where the lug tab lands after applying that rotation.

Testing the opposite rotation of +90 puts the socket pointing down, which seems wrong, so I'm sticking with -90 for socket-up orientation. Now I need to work out where the opening maps to under that same transform, applying (x,y)→(y,-x) to the opening's local coordinates to check it lands on the correct side.

So the tab extends from the socket's bottom side, which maps to the right side in world coordinates. Tracing the cone shape, the narrow end sits at one local coordinate and the wide opening at another, which I'm converting into world-space y positions to figure out how the socket and cone align spatially.

Working through this, the socket sits at the top with the cone narrowing upward and widening at the bottom, matching a lamp shade shape. Now I'm checking the lug hole position relative to the socket's edges — it sits roughly 24 pixels to the right of the socket's right boundary, and I'm converting the lug tab's local coordinates into world y-values to pin down its exact placement.

Now I'm tracing how the head plate connects: hole A attaches to this lug, placing the head plate near the top-right of the shade's socket, which fits a typical desk lamp where the head sits above a hanging shade. I'm mapping out the head plate's three holes — a small one and two larger ones — to figure out how the upper arm attaches at hole A.

Measuring the triangle formed by these three holes, I find the sides are roughly equal in length, around 64-68 units, suggesting a near-equilateral layout. But I still don't know the head plate's actual orientation in the assembled object, so I need another way to pin down the exact pose expected by the scoring.

The grader likely checks each non-moving part's world rotation against whatever the generator assembled, meaning the plates' fixed orientations in the "working" lamp determine the correct joint angles rather than the other way around — so I need to work backward from the plates' expected orientations to figure out what angle each joint should be set to.

So to pass, I need to find the rotation that counteracts the stored random rotation R_i and aligns the canonical frame with its expected working orientation — essentially solving T_i as the inverse of R_i composed with the target angle.

The problem is I don't actually know R_i for each piece. The base was explicitly generated upright (R≈0), but for others like the elbow plate, orientation is random, so the stored drawing's hole positions alone don't reveal what the canonical "nice" orientation should be without more assumptions.

That's roughly a 12° offset from a natural canonical orientation, which seems plausible as a small random rotation. I'm now cross-checking other elements' stored tilts—the L bracket at ~20°, lower arm at 5.5°, upper arm at 25°—to see if a consistent rotation pattern emerges across the whole drawing.

The stored rotations don't seem to follow multiples of 90°, so they appear essentially random and can't be inferred from canonical axes. I'd rather assume each part sits in its natural working pose—bracket upright, arm vertical-ish, shade axis up, bulb hanging down—and reconstruct the intended configuration from there, since the grader's tight tolerances mean the puzzle must have a solvable, well-defined target pose.

The task phrase "assemble into one complete, working desk lamp" suggests orientation is actually pinned down by functional constraints rather than arbitrary rotation—each part's "facing" direction is determined by its features (shade opening down, bulb cap up, foot down), though for the plates this is less obvious. I'm also noting that arms aren't classified among the explicitly "moving" parts like wheels or cranks, so they're likely treated as fixed once placed.

Since the arm angles are set by the hole positions connecting the base, elbow, and head, the whole pose becomes geometrically determined once the plates' orientations are fixed. I'm trying to infer that canonical orientation by imagining the lamp in its natural working stance—lower arm rising from the bracket, elbow bending, upper arm reaching to the head, shade angled downward—and wondering if the original part drawings were already stored in this working pose before any rotation was applied.

I'm now questioning whether "arbitrary rotation" actually excludes the base, since the base is explicitly said to be stored upright. That makes me reconsider the L bracket: if it's stored tilted at 20°, maybe rotating it back by -20° would restore its "natural" upright configuration, with one leg horizontal and the other vertical — which could serve as the reference orientation for assembling the rest of the parts.

Rotation 160 makes more sense: the corner sits bottom-right, the foot extends left with its flat bottom edge resting on base, and the upright leg rises from the right end — that's the natural L-bracket orientation, unlike the hanging-bracket feel of the other rotation.

Tracing the outline coordinates of that bracket region to pin down the exact shape of the arm and notch near the corner.

I'm weighing two possible geometry interpretations for the lamp's lower arm to see which produces a plausible structure connecting the vertical leg to the elbow joint.

I'm now actually placing coordinates: fixing the canvas size, base dimensions, and choosing a world-space position for the base's top edge to anchor the rest of the figure.

With the arms each around 330 units long plus the base and head plate, the lamp would total nearly 760 units if fully extended vertically—too tall for a 768-high canvas once the base is accounted for—so I'm realizing the pose needs to bend the arms rather than stand straight up.

So I'm working out a bent pose: the lower arm angled up at roughly 60° from horizontal, an elbow joint, then the upper arm extending toward the head with the shade hanging below it. I'm calculating the base's position by translating its local coordinates so it centers around x=500 with its top around y=680, figuring out the offset values needed to place it correctly on the canvas.

Still computing coordinates...

Checking the outer edge points, I find y'≈10 consistently, confirming the arm's bottom face sits around y'=10 while the top face is near y'=-22, giving an arm width of roughly 32px. Now I'm shifting to check the upright's outer edge coordinates for option A to see where that corner lands after rotation.

Actually the arm extends left to x'≈-127, so the foot shape points left of the upright which spans x' -31 to -62, with the top of the upright reaching y'≈-84.5.

The foot's bottom face sits at y'=+10 with its top at y'=-22, giving thickness 32, and the upright attaches at that right end with its inner edge at x'=-62. The pin hole position on the upright is still uncertain, maybe around y'=-60 to -70, so I should also check whether rotating by -110 degrees fits better.

I'm now transforming the local edge coordinates through that -110 degree rotation to see where the upright's outer edges land in world space.

Checking whether the foot sits at the bottom near y'=-31 to -62 while the arm extends upward to -127, trying to verify the orientation makes sense as an L-shape with the corner correctly placed.

Tracing the arm's span from x'≈-10 to 22, rising up to y'=-127, while the foot spans x'=-10 to 67 along the bottom band — so the corner sits bottom-left with the foot extending right and the arm rising up, matching option B. Both candidate orientations seem to form valid L shapes.

Thinking about real lamp designs: the upright, where the arm pivots, is typically the longer leg compared to the flat foot. Option A has the upright as the 95-length leg with an 87-length foot, while option B flips that — so I'm weighing which one matches realistic lamp proportions, since both seem plausible at first glance.

Given I can't verify the exact pin location against the hidden grader, I'm instead focusing on getting the rounded foot's curve shape right at the bottom of the 95-leg, since that flared, rounded profile looks like the natural base of the lamp.

Checking option B too: the foot's bottom face there is also flat, around length 63. Both options give a flat-bottomed foot, so I'm leaning toward option A, with the foot being the arm and the upright being the 95-length leg, and now I need to check where that leg's far end lands.

Going with a 160° rotation for option A: the upright stands vertical, the foot extends left from its base, and the lamp arm rises from the right end of the foot up through the elbow and into the upper arm.

Now I'm working out the world coordinates by applying the rotation and translation to the foot's boundary points, making sure the outer bottom edge of the foot rests flush on the base's top surface.

I'm setting ty = Y_b - 10.7 so the foot sits at the right world height, and working out the base's top y-offset similarly, picking Y_b = 690 as a trial value. Now I'm figuring out where the pin hole on the upright should sit in the rotated frame, somewhere near the top of that -62 to -31 x-range.

I'm guessing the pin sits about 12 units from the upright's top end, then tracing how the lower arm connects from that pin up to the elbow's bottom hole, comparing the arm's stored top and bottom hole coordinates to figure out its orientation and rotation.

Good, so the vector points downward as expected for the pose. Now I need to pick the elbow position and pose angle — placing the lower arm's bottom end P and computing the elbow bottom hole by extending along a world angle φ above horizontal, then working out where the elbow's right hole and the plate orientation fall relative to it.

I'm trying to figure out the designer's canonical orientation for each piece by cross-referencing stored rotations: the lower arm's stored tilt is small (5.5°), the L-bracket's is larger (20°), and the shade sits horizontal — checking whether these suggest a consistent baseline rotation convention I can apply to the elbow plate and head plate too.

Maybe the shade's 90° offset is actually canonical since it could rest horizontally, and the rest are canonical plus small random perturbations within roughly ±25°. I want to test that hypothesis more carefully.

That coincidence theory seems to break down for the bulb and shade, so maybe rotations really are random and the near-axis alignments for elbow and arms are just chance. If so, the orientation must instead be inferable from each part's own labeled features — the bulb's cap pointing up, the shade's opening down, the bracket's foot down — and for plates, perhaps from named holes like "bottom," "right," or "left" indicating which way they face.

So the simplest hypothesis is that the stored elbow plate drawing is approximately the canonical orientation with only a small rotation offset, so bottom/right/left roughly match their labels. I'm now checking the left hole's position relative to the centroid to verify this.

This confirms the triangle is equilateral with the bottom vertex pointing straight down (90°) in canonical form, and the stored data reflects a consistent +12° rotation offset applied to bring it to that natural orientation. So the elbow plate's working rotation equals the stored value plus 12°, and I expect the head plate triangle to follow the same pattern.

I'm trying to figure out the canonical orientation by testing whether a vertex points down (rotation -10°, giving 90/208/326) versus pointing up (rotation 170°), and considering which hole corresponds to the arm versus the shade attachment based on how the head plate connects to the rest of the object.

Looking at the plate's actual vertex coordinates, I can see it forms a triangle-like shape with corners roughly at upper-left (~25,30), upper-right (~110,35), and bottom (~60,110). The small arm hole sits near the upper-left corner, the second hole near the upper-right corner, and the main hole near the bottom vertex — so in canonical form, the bottom-pointing corner holds the main hole, suggesting a rotation that places that hole near 90°.

I'm now reasoning about how the shade would hang from this head plate: the shade's lug tab extends sideways from the socket rather than straight down, so if the plate's bottom corner holds the attachment hole, the shade would hang off to the side rather than directly beneath — I need to work out how that geometry resolves.

I'm weighing two possible arrangements, one where the attachment hole sits at the bottom corner and the shade hangs there, versus one where it sits at the upper-right corner, and picturing the overall lamp silhouette — base, arm rising to an elbow, second arm reaching the head, shade angled downward at the end — to decide which configuration reads as a natural desk-lamp shape.

Since I can't pin down exact geometry from the clues, I'm settling on a reasonable working pose: placing the base around x=500–775, positioning the bracket's upright near x=480 with its foot extending left, and starting to sketch out coordinates for the arm segments to carry forward with calculations.

So the foot spans roughly x=399 to 496 at the bottom, meaning the base needs to extend wider than that range, say from 380 to 660, to properly support it.

Working out base translation: setting base x from 370 to 645 means a translation offset of 365, giving a base center around 507.5, with the base top at y≈690 and bottom at y≈731.8, fitting within the 768 canvas height. Then checking the pin position, it lands at roughly (480, 609.3) after applying its own offset.

Now I'm figuring out the lower arm angle from the pin to the elbow bottom hole—testing 60° and 70° tilts to see where the elbow lands, since that determines how high the upper arm and head will sit. I'm leaning toward picking the angle after also working out the lower arm's rotation based on the local vector between its two end holes.

Comparing local versus world vector angles gives a 35.6° rotation for the lower arm, but I'm worried this orientation needs to match whatever pose the grader expects within 8°, which means I need to guess what "rest" pose a lamp generator would typically use—likely with the lower arm tilted rather than vertical.

So if the lower arm were stored vertical with just a 5.5° tilt, the total lamp height would stack up from the base bracket through to the upper arm, which would then extend from that point.

Working through it, the elbow would sit around height 284 if the base pin is near 610, with the upper arm then projecting 340 units outward to reach the head position.

But I'm second-guessing this tall-lamp interpretation since the canvas is wide (1376x768), suggesting the layout might spread horizontally rather than vertically, with the base around 275 wide and both arms roughly 340 each.

I'm now wondering whether the generator defines joint angles randomly and the validation checks against that specific chosen pose, which would make inferring the canonical orientation nearly impossible except through directional cues.

Since arms aren't in the explicit "moving parts" list, their orientation might still be checked tightly since the grader expects them to connect naturally to the elbow plate, head plate, and shade—all of which should have inferable canonical orientations based on how a lamp physically assembles together.

I need to check the shade's stored axis orientation by looking at its geometry—specifically the cone's wide edge coordinates to determine the midpoint and angle.

Continuing the calculation, the narrow edge midpoint and socket endpoint both confirm the axis is horizontal within about 2 degrees of tilt, so the shade's local axis aligns roughly with the x-direction. This means to get the socket pointing up and opening pointing down in world space, I need to rotate by -90 degrees, since that transformation maps local +x to world up.

I wonder if the stored rotation follows a pattern like canonical plus a multiple of 90 plus small noise, which would mean the random angles aren't truly uniform—unless there's some other explanation. Let me check the base's tilt too, since it's supposed to stay upright within about 3 degrees, by looking at its top edge coordinates.

Checking the actual edges, the base comes out flat at exactly 0 degrees, while the L bracket tilts 20 degrees, the lower arm tilts 5.5 degrees, and the elbow triangle sits 12 degrees off from equilateral—so there's no clean 90-degree pattern across parts. This makes me reconsider the generator: maybe each part is drawn canonically in its own frame, with the base's canonical orientation matching its stored orientation exactly, while other parts carry their own small or arbitrary rotation offsets. I want to test whether the lower arm is actually drawn along the vertical in its canonical form.

The bulb axis at 36° doesn't fit neatly either way, so that hypothesis is shaky. But if the shade's canonical orientation really is horizontal, that would mean the lamp head points sideways rather than downward, which is plausible for some Anglepoise-style poses.

When the bulb is inserted into the shade's socket, its axis must align with the shade's horizontal axis, with the neck/cap pointing rightward toward the socket. I'm working out that the bulb's stored neck direction, computed from globe to neck, gives roughly a 216° angle, so I need to figure out the rotation needed to align that with the shade's rightward direction.

Since I can't fully resolve the canonical orientation, I'll accept some uncertainty and just aim for a physically plausible lamp assembly — shade opening downward, bulb cap seated into the socket, bracket upright, arms and elbow plate positioned sensibly — even if it doesn't perfectly match whatever pose the grader expects. I'll try to reconstruct the most natural working pose and fit the holes precisely based on how the generator likely computed joint positions.

The orientation constraint on the elbow plate fixes its rotation, but its translation still seems only pinned by its own holes connecting to the lower arm and base — so I need the lower arm's length plus the elbow plate's hole geometry to actually pin down its position uniquely, rather than leaving it floating.

Given time constraints, I'll just pick a plausible "natural" canonical pose for each part—L bracket upright vertical, lower arm with a slight vertical tilt—and derive the rotations from undoing the stored transforms to match that assumed resting posture.

If the bottom vertex is lowest, the other two vertices sit above it — the lower arm attaches from below at the bottom vertex, upper arm at the right vertex. With the equilateral triangle (side 66, circumradius ~38.1), I'm placing bottom at 90°, right at 330°, left at 210° relative to the centroid, applying the stored angular correction to get actual screen positions.

Computing the right vertex relative to the bottom: the difference comes out to (33, -57.2), length 66, at angle -60°. Comparing to stored coordinates gives an angle of -71.6°, a discrepancy of 11.6° that matches the known -12° rotation offset — confirming the canonical model lines up correctly, so I can place E_r as E_b plus 66.4 at angle -60° relative to E_b.

Now I need to figure out which end of the upper arm attaches to the elbow at (481.6, 228) versus which end connects up to the head, since the upper arm has two possible endpoints and I need to determine orientation before placing the head plate.

Shade lands around y~300, fitting the canvas. Let me try computing the upper arm's rotation instead, checking how the local elbow-to-head vector maps to this world orientation.

Taking elbow as U1 and head as U2, if the world direction from elbow to head sits around -30° (up-right), the needed rotation comes out to roughly -55° relative to the stored orientation.

Rather than work through the symmetric case, I'll just commit to a natural lamp pose: vertical bracket from the base up to the pin, lower arm leaning up-right at about 60° giving an elbow position around (643, 327), with a rotation near 35.6° for that segment.

Pushing through, I compute the elbow plate position and then direct the upper arm from there up toward the head, placing the head around (971, 99) — so the whole arm rises from the base, bends at the elbow, and extends up and out toward the head, which reads as a plausible desk-lamp silhouette even if not perfectly standard.

Now I'm fixing the head plate's canonical orientation: taking bigA as the bottom corner, small as upper-left, and big2 as upper-right, then checking that rotating by -10° lines each point up correctly (bigA near 90°, small near 210°, big2 near 330°), confirming the orientation works.

Then I'm reasoning about which corner serves as the arm hole versus the shade socket hole — if small (upper-left) is the arm hole where the upper arm attaches, that leaves bigA (bottom) as the shade mounting point, meaning the shade would hang below the head plate with its lug tab at that bottom corner, which seems geometrically consistent with how the shade socket would sit relative to the head.

Computing the offset between lug and socket center, the tab points essentially horizontally (+x) from the socket, meaning hole A should be positioned horizontally relative to the socket too, not above or below it.

After applying the -90 rotation, I recalculate the cone's world coordinates: the narrow top edge sits around world y=-128 and the wide bottom opening around y=-12, while the x-span works out to roughly 72-153 at the narrow end but a much wider 9.5-223 at the open end, so the cone flares out considerably wider than I expected.

The socket sits above the narrow end, centered near x≈112, and the lug extends right from the socket's edge toward x=193, putting hole A at roughly (176,-169) — offset about (+64,+11) from the socket center. So the head plate hole ends up positioned about 64px to the right of the shade's central axis, at roughly the same height as the socket.

Given the shade must open downward (lamp shades don't open upward), rotation has to be -90 rather than +90, which maps the shade's axis vertically with the socket pointing down. I'm now working out where hole A lands in world coordinates by applying that -90 rotation transform to the shade's local coordinates plus its translation.

With that lug position established, I'm turning to the head plate's own rotation: I'm testing a value around -10 degrees so that the geometry between the arm hole and hole A lines up correctly, computing the vector between those points in local coordinates and checking the resulting angle after rotation to see if it matches the expected direction toward the arm.

But I need to decide which hole is "A" — could also be big2, the upper-right one after rotation, instead of bigA at the bottom. I'll go with hole A being bigA, the bottom hole.

Taking that as the hanging point, the lug sits at hole A directly below the arm hole, placing the shade socket to the left of the lug by 64 units horizontally and 11 up, giving the socket center as roughly H_a plus (-32.4, 44.1) — so down-left of the arm hole. From there, the shade cone extends downward from the socket's narrow end.

Checking the shade dimensions, the cone bottom sits 168 below the socket center and spans about 213 wide, centered near the socket, which places the big shade opening right beneath the head plate — a sensible proportion. Now I'm verifying this socket position against the lug coordinates to confirm consistency.

Using the lug's local-to-world transform, the offset between the lug and socket center comes out to about (65.1, 11.4), so the socket center equals the head anchor minus that offset, giving roughly (-33.5, 43.7) relative to the head. From there I derive the shade's translation by comparing against its local socket position.

Next I need to figure out where the bulb's screw cap sits so it inserts correctly into the socket, with the bulb's globe hanging down into the cone.

Rechecking the globe's bounding box, with rightmost x around 179 and bottom y around 159, I'm estimating the radius to be roughly 70, which places the center a bit differently than I first guessed.

Testing distances from a candidate center near (110,90) against points on the globe edge confirms a radius close to 70, with the neck junction sitting slightly farther out. So the globe center lands around (110,92) with radius ~70, and the neck axis runs from there toward roughly (20,30), giving an angle of about -145.5° — meaning in canonical orientation the cap points upward toward the socket while the globe hangs below.

So I'm working out the bulb's rotation relative to the shade's vertical axis: since the cap needs to point at -90° but currently sits at -145.5°, the bulb needs roughly +55.5° of rotation to align coaxially with the shade. Now I need to pin down where the screw cap center actually sits by tracing the neck outline's coordinates to find the midpoint of that upper region.

I'm checking the neck's parallel edges to figure out the axis direction, tracing from one edge's coordinates to the next to estimate the angle of the cylinder.

Checking the dot product confirms that edge is roughly perpendicular to the axis, so it's a cross-section of the neck — likely the face where the neck transitions into the globe.

So I'm thinking this shoulder edge marks the neck-globe boundary, with the cap (screw end) extending further upper-left beyond it toward another edge near the tip. I'm trying to estimate the cap's center by averaging the shoulder's midpoint with the end-face's approximate midpoint, landing somewhere around (33,30).

Getting precise placement within a few pixels seems unrealistic here, so I'm approximating the bulb's screw cap position relative to the socket's narrow end, reasoning that the cap should insert at that narrow opening rather than the socket's overall center.

Calculating the cap-to-globe distance gives roughly 107 units, so the bulb's total length from cap to globe bottom is about 177. Comparing that to the shade's socket-to-cone span of about 216, the bulb bottom would land near the shade's opening if the cap sits around y -170 to -190 in world coordinates — which seems plausible for the socket placement.

I'm second-guessing whether the socket anchor should be the socket's center or the narrow-end point of the cone itself, since those two candidates differ by about 52 pixels and would change where the bulb cap needs to sit.

Checking the math, if the cap sits at the socket's narrow end, the globe would extend about 60px beyond the cone opening, which seems off given the bulb is roughly 177 long against a cone+socket height of about 216 — I'm trying different anchor placements to see which keeps the bulb properly nested in the shade.

I suspect the generator just treats the socket and bulb cap as coincident point anchors placed coaxially, rather than trying to reason about exact lengths, so the cap's tip anchor likely sits somewhere around local coordinates (15,18).

Actually, I'm noticing a small circle at (15.36,18.86) that's probably the designed "contact tip" anchor marking the bulb's screw cap, similar to how the shade's lug hole and the plates' holes are also drawn as circles—so that's likely the true bulb anchor point.

From that anchor to the globe center at roughly (110,92), I get a direction vector giving an axis angle around -142.3°, revising my earlier estimate of -145.5°. Converting to canonical orientation where cap-up equals -90°, that yields a rotation ρ_b of about 52.3°, though I'm still unsure whether this anchor point is truly the right reference.

Checking whether the anchor sits on the actual bulb axis — the neck tip region spans a few nearby coordinates, and the circle point looks close enough to the axis to be reasonable. Now I need to figure out where the bulb's cap anchors onto the shade's socket at the narrow end of the cone, taking the midpoint there as the socket anchor and placing the bulb's tip there, with the globe extending downward from that point.

Placing the bulb this way means its globe sticks out of the shade's opening by a noticeable margin, which seems physically odd since the socket cylinder continues above the narrow end — but since the generator's placement seems arbitrary anyway, I'll just go with the narrow-end anchor and accept the slightly awkward overlap, since the grader likely only checks anchor positions.

In real lamps, the screw cap goes into the socket while the glass globe sits inside the shade, with the socket itself extending above the shade. Given the socket's dimensions here, I'm leaning toward anchoring the bulb's tip closer to the socket's inner end rather than its outer edge.

That's the bulb's cap anchor placed at the socket point — but physically the cap's base (where threads end and the neck begins) should align there, not the tip, since the screw base needs to sit in the socket while the globe pokes out beyond the cone's narrow end.

Actually, maybe the generator only draws circles at hole anchors, so the bulb's single circle at (15.36,18.86) is likely its designated cap anchor, while the socket, lacking a circle, uses its narrow cone tip as the anchor instead.

Actually checking the measurements, the cap-to-globe-bottom length of 172 doesn't fit within the cone length of 116 if the cap sits at the narrow end — but if the cap sits at the socket's far end instead, the globe bottom lands around -56, which fits neatly inside the cone's opening. That confirms the socket's far end is the right anchor point.

But I'm second-guessing this since the generator's phrasing about "narrow end of cone" might mean the anchor is the cone's narrow end itself rather than the socket's far end, so I'm testing an alternative placement where the bulb's cap sits near -128 and the globe center lands around -28, checking whether that span still makes geometric sense.

I'll settle on the far end of the socket (228,111) → world (111,-228) as the anchor, since that's where a bulb typically screws in, even though "narrow end of cone" could describe either end loosely.

Now I'll move to computing actual numbers, starting with fixing the base translation pose parameters.

Working out the L bracket's rotation matrix at 160 degrees and applying it to the local foot coordinates to find where the flat bottom edge lands, so I can align it against the y=690 baseline.

Then I'm locating the upright's centerline by checking x' values on both outer and inner edges, confirming they average to about -46.5, and solving the inverse rotation to find which local point maps to a chosen pin location on that centerline.

Checking the left and right edge x-values at that y confirms the center falls right at x≈19.8, so the pin location sits correctly on the upright's centerline. Now I can compute the pin's world coordinates by applying the rotation and translation to this local point.

Solving for tx so the pin lands at world x=480 gives the transform translate(526.5, 679.29) rotate(160). I'm verifying the foot's extent reaches from world x 398 to 496, comfortably within the base's 370–645 range, and confirming the whole foot sits on the slab before moving on to the lower arm.

Now I'm placing the lower arm pin at (480, 609.3) and testing angle options—60° puts the elbow around (643,327), near the base's right edge, while 75° gives a more vertical elbow at (564,294) with the right hole around (598,236). I'm weighing which angle gives the lamp a more natural-looking pose.

Recomputing the mouth position relative to the lug: the mouth sits at world (111,-228) while the lug is at (176.1,-168.6), giving a relative offset of (65.1, 59.4), so the mouth equals H_A minus that offset, which simplifies to H_a plus (-33.5, -4.3).

Tracking the bulb and shade geometry from that mouth point: the bulb extends downward about 190 units, putting the globe bottom around y=354 near x=884, while the cone's opening sits around y=380 spanning roughly ±107 in x from a center of 884.

Now I'm working out the shade's coordinate transform, computing the -90° rotation mapping from local shade coordinates to world coordinates so I can pin down the translation offset from the mouth point.

Then I turn to the head plate, trying to verify its rotation transform against the three hole positions by checking that the small-to-bigA vector rotated by -10° matches the expected world-space offset.

That gives t_h = H_a - (42.65, 29.95). Now for the upper arm, I need to figure out which local endpoint (U1 or U2) maps to the elbow versus the head, then compute the rotation needed so the local elbow-to-head vector aligns with the desired world-space direction from E_r to H_a — comparing their angles to get the rotation offset.

Picking a pose angle β of -20° puts H_a around (917.4, 120.4), which checks out against the shade and bulb positions, keeping everything within canvas bounds. The exact angle is somewhat arbitrary, but I want the shade to land near the middle-right of the canvas with the lamp leaning naturally from the base.

Testing a lower arm angle of 70° instead: elbow point lands around (591.6, 302.8), which I'm comparing against the 60° and 75° alternatives to see which gives the most balanced overall span across the canvas.

The local angle checks out at 84.42°, and the world-frame angle needed is atan2(306.54, -111.56), which equals 180 - 70 = 110°, so the rotation α works out to roughly 110 - 84.42 = 25.58°.

Now I'm computing the lower arm's transform: solving for the translation vector by subtracting the rotated local point from the target endpoint, which requires finding cos and sin of 25.58° via interpolation from known values at 25°.

Then I verify by applying the same rotation and translation to point B, confirming it lands close to the expected target P=(480, 609.3).

Now I'll settle P at (479.96, 609.28) for consistency. For the elbow plate, I need its bottom hole position and rotation so the bottom vertex points straight down—computing the centroid of its three holes and the angle to the bottom hole gives about 78°, so I need roughly a 12° rotation to align it to 90°.

I'm computing the full rigid transform for the elbow piece: applying a 12° rotation to the local bottom hole coordinates and solving for the translation that places it exactly at the target world point, then using that same transform to find where the right hole lands in world space so I can check it against the ear piece's connecting hole.

Now I'm transforming the left hole as well to confirm the triangle orientation looks correct with the apex pointing down, then turning to the upper arm piece to figure out which end connects to the elbow and what rotation angle that requires.

Computing H_a at roughly (945.0, 129.1) with the upper arm at -20°. Now I'm working out the composite rotation for the upper arm transform, combining the -20° angle with the -25.04° local offset to get γ ≈ -45.04°, and starting the cosine/sine calculations for that rotation.

Good, this confirms the result matches H_a (944.88, 128.98) against the expected (945, 129.1). Now for the head plate, I compute the translation using the head's -10° rotation: t_h = H_a - (42.65, 29.95) = (902.25, 99.05), consistent with my earlier calculation.

With the head transform set at translate(902.25, 99.05) rotate(-10), I work out hole A's world position from its local coordinates, getting H_A = (976.52, 184.19), which checks out against H_a + (31.65, 55.15). Now I'm using this to solve for the shade's translation by mapping its lug position through a -90° rotation back to H_A.

I'm verifying the socket/mouth position and shade bounds against earlier estimates, then tracing where the shade's lug tab sticks out relative to the socket, landing it around world x 953-996, y 167-198.

Now I'm working through the head plate's vertex positions, rotating points to locate each corner (976,184), (945,129), and (1008,124), forming the triangle that defines the head plate shape.

Checking the shade socket and cone geometry, I'm recalculating the narrow end's local coordinates against the world frame to pin down where the socket sits relative to the head plate, since the tab region appears to run underneath it.

There's a slight overlap between the plate's edge and the socket corner, but it's minor and acceptable since the lug hole sits on the socket's side while the plate is on the right. Now I'm positioning the bulb with its tip at the socket mouth, pointing downward from the socket, and working out the rotation angle needed to go from the canonical upward-pointing orientation to this new direction, landing around +52.3°.

Now applying the same rotation to the globe center to find its world position, continuing to work out the bulb's placement in world coordinates.

Checking that the globe at center (911,244) with radius 70 fits within the lamp shade's opening at y=341 — the span looks roughly correct, though I should double check the socket relationship.

Now I'm verifying the bulb's transform: the axis from globe center to tip points straight down, matching the rotation after translating to (916.9, 101.06) and rotating 52.3°. For the shade, I'm confirming the local-to-global mapping places the socket mouth at (911.4, 124.75), and checking the axis tilt against the stored socket direction.

Next I'm checking the overall lamp structure—lower arm from the base pivot to the elbow, upper arm from elbow to head—and verifying the rotation signs produce the correct downward orientation on screen for both arm transforms.

I'm then working through the remaining placements: elbow plate, head plate, shade, bulb, L bracket, and base, confirming each transform lands its connection point at the right coordinate and that the base's top edge aligns with the L bracket's foot.

Checking the orientation of the L bracket next — verifying the foot extends left while the upright sits on the right, and that the lower arm's pivot point lines up correctly with the upright's centerline.

Confirming the chain of connections: lower arm to elbow, elbow to upper arm, upper arm to head, head to shade lug, and bulb cap at the socket mouth all line up as expected, then tallying the final rotation angles for each part — base at 0, bracket at 160, lower arm at 25.6, elbow at 12, upper arm at -45, head at -10, shade at -90, bulb at +52 — to make sure every piece faces the way it should on the working lamp.

Writing SVG placement code...

Then I'm verifying the base's flat top notch and top edge alignment look correct.

I'll keep y=690 for the foot contact point, confirming it aligns with the base's top outline. I'll finalize the SVG now with brief notes, keeping the explanation concise given the measurement uncertainty.


````

## Answer

````text
This is a best-effort assembly. I read the hole centres and edge angles from the path data, but I could not confirm the L-bracket pin hole or the bulb cap anchor from the drawings, and the joint angles are a plausible pose rather than a verified one.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1376 768">
<use href="#kit-base" transform="translate(365 684.8)"/>
<use href="#kit-l_bracket" transform="translate(526.5 679.29) rotate(160)"/>
<use href="#kit-lower_arm" transform="translate(581.77 275.3) rotate(25.58)"/>
<use href="#kit-elbow_plate" transform="translate(542.48 203.5) rotate(12)"/>
<use href="#kit-upper_arm" transform="translate(595.96 245.39) rotate(-45.04)"/>
<use href="#kit-head_plate" transform="translate(902.25 99.05) rotate(-10)"/>
<use href="#kit-shade" transform="translate(800.4 352.75) rotate(-90)"/>
<use href="#kit-bulb" transform="translate(916.9 101.06) rotate(52.3)"/>
</svg>

**Assumptions behind the placement:**
- **Base:** kept unrotated, with its flat top at y ≈ 690.
- **L bracket:** rotated 160° so its upright is vertical and its foot lies flat on the base. The pin is taken on the upright's centreline (no circle is drawn there, so its position is estimated).
- **Lower arm:** runs from the pin up to the elbow plate's bottom hole.
- **Elbow plate:** rotated 12° so its bottom hole points straight down.
- **Upper arm:** runs from the elbow plate's right hole to the head plate's small arm hole.
- **Head plate:** rotated −10° so its bottom corner (the large hole) points down; hole A is taken as that bottom corner.
- **Shade:** rotated −90° so the socket is up and the opening is down; its lug hole sits on head hole A.
- **Bulb:** rotated 52.3° so it hangs straight down with its cap at the socket mouth. I used the socket's far end as the anchor, since that keeps the bulb inside the shade; the grader may define the anchor at the narrow end instead.
````

## Prompt

````text
Below is a kit of 8 SVG parts for a desk lamp with a jointed arm (side view). Each part is a <g id="kit-..."> drawn in its own local coordinate system, stored at an arbitrary rotation. Each part's id names the part.

Assemble the parts into one complete, working desk lamp with a jointed arm (side view) on a 1376 x 768 canvas. Parts are rigid: translate and rotate only, no scaling and no mirroring. Use every part exactly once. The base part, kit-base, stays upright exactly as stored (at most 3 degrees of rotation).

Grading is done by code on where the parts land:
- The base upright: rotated at most 3 deg from how it is stored.
- Lower arm: its bottom end hole on the l bracket's upright pin hole (within 6 px)
- Lower arm: its top end hole on the elbow plate's bottom hole (within 6 px)
- Upper arm: its bottom end hole on the elbow plate's right hole (within 6 px)
- Upper arm: its top end hole on the head plate's arm hole (within 6 px)
- Shade: its lug hole on the head plate's hole A (within 6 px)
- Bulb: its screw cap on the shade's socket at narrow end of cone (within 6 px)
- L bracket: the bottom edge of its foot stands on the base's flat top edge, anywhere along it with the whole foot on the slab (within 6 px)
- every other part must face the way it does on the working object, relative to the base part, within 8 degrees; parts that turn in use (wheels, gears, sprockets, cranks, connecting rods, pedals, rotors) may sit at any angle;
- a missing, duplicated, scaled, skewed or mirrored part fails the assembly.

Reply with one <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1376 768"> that contains exactly one <use href="#kit-ID" transform="..."/> per part. You may wrap <use> elements in <g transform="..."> groups. Do not copy the part drawings: the kit's <defs> are inserted automatically.

KIT:
<svg xmlns="http://www.w3.org/2000/svg"><defs>
<g id="kit-base" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 8,21.3 L 8,43.1 L 8.5,44 L 268.4,44.1 L 276.9,43.6 L 276.4,16.7 L 274.7,13.5 L 272.1,10.8 L 268.6,9 L 265.7,8.4 L 18.9,8.4 L 15.3,9.4 L 11.9,11.6 L 9,15.6 Z M 253.3,19 L 256.1,19.4 L 258.3,20.7 L 260.5,24 L 260.9,26.4 L 260.2,29.8 L 259,31.5 L 256.9,33.3 L 253.6,34.1 L 249,32.7 L 246.6,29.9 L 245.9,26.5 L 246.8,22.9 L 248.5,20.7 L 250.6,19.4 Z" fill="#dbe8f5" stroke="none"/>
  <path d="M 271,6.6 L 274.9,9.2 L 277.2,11.9 L 279.3,15.8 L 279.8,18.7 L 279.8,44.3 L 279.1,45.9 L 276.6,47.1 L 9,47.1 L 6.6,46.5 L 5,44.3 L 5,18.7 L 5.6,15.6 L 7,12.7 L 9.8,9.4 L 12.6,7.2 L 16.9,5.4 L 200.6,5.2 L 200.6,6.2 L 248.6,6.2 L 248.6,5 L 266,5.1 Z M 8,43.3 L 8.4,44 L 276.4,44.1 L 276.9,19.6 L 276.4,16.7 L 274.6,13.4 L 270.2,9.7 L 265.6,8.4 L 18.9,8.4 L 15.3,9.4 L 11.9,11.6 L 8.4,17.2 Z" fill="#1a2942" stroke="none"/>
  <path d="M 252.4,19 L 250.1,19.6 L 247.3,21.9 L 245.9,26.7 L 246.7,29.9 L 249.8,33.2 L 253.4,34.1 L 258.2,32.3 L 260.2,29.7 L 260.9,26.4 L 260.2,23.3 L 258.1,20.5 L 254.8,19.1 Z M 253.2,22.3 L 256.4,23.3 L 257.8,26.7 L 256.7,29.7 L 253.5,31.1 L 250.2,29.8 L 249.2,27.2 L 249.8,24 Z" fill="#14233b" stroke="none"/>
  <path d="M 253.2,22.3 L 249.8,24 L 249.2,27.1 L 250.2,29.8 L 253.5,31.1 L 256.7,29.7 L 257.8,26.7 L 256.4,23.3 Z" fill="#f3f3ed" stroke="none"/>
  <path d="M 257.2,26.62 A 3.82,3.82 0 0,1 253.38,30.44 A 3.82,3.82 0 0,1 249.56,26.62 A 3.82,3.82 0 0,1 253.38,22.8 A 3.82,3.82 0 0,1 257.2,26.62 Z" fill="#F8F7F2" stroke="#1F2A3A" stroke-width="2.3"/>
</g>
<g id="kit-bulb" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 172.359131198,121.20019804 L 174.936126478,112.361131612 L 175.93624382,103.117768301 L 175.256638193,92.9807995134 L 172.305155972,81.5637616883 L 167.203451626,71.6818280331 L 160.767202163,63.7153549834 L 152.289194674,56.3415236168 L 143.926734528,51.5593420745 L 132.997053063,47.7868014089 L 125.004199275,46.7077794824 L 111.477736976,46.1378517032 L 100.995590336,44.0083912487 L 86.7003558064,38.2251162475 L 73.6790831883,29.9464412688 L 68.3023077296,29.6459655342 L 65.5298844062,31.3322836881 L 37.8227460084,65.1954566316 L 37.1587710424,67.092595858 L 37.4494728158,69.5452459511 L 39.3292667798,72.849239694 L 51.0826846128,83.8468380338 L 60.0998338222,96.2166003652 L 64.0834331921,104.473775188 L 69.5740413916,122.040027538 L 75.2801136152,132.755471522 L 83.6379308099,142.280013072 L 92.399556829,148.57238222 L 100.018649367,152.345899003 L 109.987546966,155.339405418 L 119.502802613,156.466308239 L 130.129079993,155.68385758 L 142.331259195,151.995114877 L 150.666850544,147.606730566 L 160.427129731,139.689853012 L 167.692008939,130.499013547 Z" fill="#fdeec6" stroke="none"/>
  <path d="M 168.575352396,134.993421666 L 174.794436028,123.549515043 L 178.047620527,113.260356156 L 179.143499658,100.972189127 L 178.161954121,91.246112407 L 176.474171792,83.5078056923 L 171.003349147,71.5780068851 L 165.056408277,63.508688804 L 156.970971477,55.7662271962 L 148.904344114,50.3496302029 L 138.947172709,46.1478760909 L 131.195675625,44.078022725 L 110.71555993,42.8033223286 L 103.157538656,41.2650393822 L 90.0466113755,36.2546915049 L 75.980031239,27.3782438334 L 71.2977663782,26.2982457902 L 66.2112046347,26.7951256848 L 60.6822390755,22.5618598245 L 59.3584440365,19.9584838058 L 56.5188423232,19.1860447403 L 53.8294784772,15.7252179454 L 48.2042630712,12.881461339 L 46.8804680322,10.2780853203 L 44.312758655,9.63243173334 L 42.348929097,8.16499401164 L 40.293980702,5 L 30.8998914652,5.03297592335 L 25.4212470917,7.55378052293 L 15.7252179454,7.99764851363 L 12.7837473173,10.0464897823 L 8.27858912083,15.448669863 L 5,21.5331462889 L 6.55537778225,30.9751164199 L 5.35470138694,36.1527970004 L 5.72430774473,39.8559566162 L 7.33831649896,43.2566882641 L 11.7074033141,47.611120535 L 12.584151586,50.2267108064 L 14.8738615007,50.5220555313 L 18.209366992,53.0704674128 L 19.4002694262,55.722212384 L 22.5056563492,56.3979135444 L 24.0585938399,57.5634113566 L 25.6059122625,60.1606802489 L 28.7718823908,61.4163207814 L 33.5213256415,64.9550760439 L 34.9611560813,71.8053963506 L 36.7864739664,74.7529741051 L 51.0357798352,88.6798288202 L 58.1313613128,99.4915226512 L 62.7198166184,110.237502267 L 67.0373557046,124.167285332 L 71.6675847781,133.167339706 L 77.5600495688,140.880241798 L 85.9474262787,148.211811339 L 95.9957165204,154.111121741 L 107.78333682,158.173388063 L 118.694208848,159.620064114 L 129.501747785,158.922137108 L 140.254322586,156.21249965 L 150.462624656,151.593996771 L 159.280929414,145.223949581 Z M 172.359131198,121.20019804 L 166.230678344,132.686366488 L 160.427129731,139.689853012 L 151.373575395,147.274255025 L 142.288997369,152.085745656 L 130.974804575,155.52653647 L 119.502802613,156.466308239 L 109.987546966,155.339405418 L 98.659187686,151.71197161 L 92.399556829,148.57238222 L 83.6379308099,142.280013072 L 74.6696386114,131.698437809 L 69.4834106129,121.997765711 L 64.0834331921,104.473775188 L 60.0998338222,96.2166003652 L 50.8530541029,83.6294217766 L 38.7248989024,72.0157293649 L 37.4494728158,69.5452459511 L 37.1587710424,67.092595858 L 37.8227460084,65.1954566316 L 65.5298844062,31.3322836881 L 68.3023077296,29.6459655342 L 73.6790831883,29.9464412688 L 86.7003558064,38.2251162475 L 100.995590336,44.0083912487 L 110.758797872,46.0232804774 L 128.278633502,47.0209575281 L 136.694593611,48.8489661313 L 143.473580635,51.3480329436 L 152.289194674,56.3415236168 L 160.767202163,63.7153549834 L 167.203451626,71.6818280331 L 172.305155972,81.5637616883 L 175.256638193,92.9807995134 L 175.93624382,103.117768301 L 174.936126478,112.361131612 Z M 62.9917345442,28.4936580914 L 61.9412960162,30.9829509426 L 36.0396899495,62.1572480985 L 35.1455964152,62.1816766039 L 29.2902624409,57.4652092765 L 51.9098629786,20.7883273001 L 54.2601560986,21.663611397 L 56.0972001781,23.4029414548 L 47.323597538,37.9588301846 L 46.7864080504,39.5840770749 L 47.257883323,40.4659563565 L 49.1005464706,40.7735153342 L 58.0615177944,26.5256736403 L 59.6078601004,25.8123536051 Z M 46.2113620564,15.2622900907 L 49.6074507529,18.3906413442 L 26.365649017,55.2187373047 L 23.3565119407,53.1535268902 L 22.8789295418,52.048124225 L 44.0010447843,17.8727493524 Z M 39.5887200263,10.2983589327 L 42.8274876126,12.5809856044 L 42.9486540231,13.7408643485 L 20.0087921967,50.1580682415 L 16.1717638594,47.2654546243 L 37.7164973637,12.1837719647 Z M 35.7700130681,8.0763154662 L 36.1931193881,8.82530214294 L 13.6880900763,44.7832450161 L 9.7360024548,40.9542760384 L 8.57514759409,37.7648535213 L 8.76154016123,34.7623116297 L 10.5487511132,31.4028656913 L 27.8203972225,10.2172516885 L 30.3270353361,8.62767143972 Z M 22.9150970364,10.7986552355 L 9.46020565218,27.5851348497 L 8.22093426547,24.8004972736 L 8.06312509686,22.2994782281 L 9.71133631765,18.7648778586 L 13.4736149638,14.0093274815 L 17.3631671467,10.6371792321 Z" fill="#13233b" stroke="none"/>
  <path d="M 62.9011037655,28.4513962652 L 58.6653976135,25.7038895056 L 49.7105334161,40.1752545831 L 48.3877144936,40.8824674919 L 47.257883323,40.4659563565 L 47.0277647548,38.5932456355 L 56.1878309568,23.445203281 L 52.7555875604,20.6310061898 L 51.9098629786,20.7883273001 L 29.2057387886,57.646470834 L 35.9067973446,62.205617051 L 62.3338667045,30.6143207014 Z" fill="#fcedc2" stroke="none"/>
  <path d="M 36.2654287878,8.19699381836 L 32.3265315357,8.12566053536 L 27.7781353963,10.3078824672 L 10.5487511132,31.4028656913 L 8.76154016123,34.7623116297 L 8.57514759409,37.7648535213 L 9.7360024548,40.9542760384 L 13.6880900763,44.7832450161 Z" fill="#fdeec2" stroke="none"/>
  <path d="M 39.2745658641,10.2622042329 L 16.8479530782,45.8153621651 L 16.2685017645,47.5312398341 L 20.0087921967,50.1580682415 L 42.773499592,13.8798640797 L 42.8274876126,12.5809856044 Z" fill="#fff2cd" stroke="none"/>
  <path d="M 45.9878386728,15.2683972171 L 22.9634531941,51.8668626676 L 23.265881162,53.111265064 L 26.365649017,55.2187373047 L 49.6919744053,18.2093797868 Z" fill="#fff2cd" stroke="none"/>
  <path d="M 22.7822044316,10.847024188 L 17.3631671467,10.6371792321 L 13.4736149638,14.0093274815 L 8.72710006293,20.4023390016 L 8.06312509686,22.2994782281 L 8.91642097995,27.3315638927 L 10.0279307715,27.0775048773 Z" fill="#fcedc2" stroke="none"/>
  <path d="M 17.629902151,19.9085627555 A 2.5,2.5 25 0,1 14.307587029,21.1177865687 A 2.5,2.5 25 0,1 13.0983632158,17.7954714468 A 2.5,2.5 25 0,1 16.4206783377,16.5862476335 A 2.5,2.5 25 0,1 17.629902151,19.9085627555 Z" fill="#F8F7F2" stroke="#1F2A3A" stroke-width="2.3"/>
</g>
<g id="kit-elbow_plate" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 104.9566923,20.6411316362 L 103.720231727,16.479261233 L 100.050702577,11.9565899186 L 93.9396923228,8.6542341432 L 89.0407550851,8.15382037319 L 18.0931777662,23.1768451211 L 12.9971000207,26.4448707655 L 10.6864792366,29.2217451941 L 8.67054918195,33.6698937994 L 8.10487525695,36.5698960426 L 8.49745621895,41.2395727111 L 11.8307420183,48.334585451 L 57.9382095095,99.2972329641 L 60.3956656424,101.017962273 L 65.2370752311,102.820946797 L 71.8483292504,102.445020885 L 75.0844048388,101.659008934 L 78.5418384849,99.6851415164 L 80.9261319514,97.3260856321 L 83.5482685199,93.0582524797 L 104.291768099,30.3079757855 L 105.382073345,25.0896202522 Z M 97.2800306068,23.9333748307 L 96.9109871735,26.7269043087 L 95.3868883561,29.0778876763 L 91.1429327431,31.4776461549 L 88.7835368481,31.5346637878 L 86.5225412016,30.9281172633 L 83.6309514858,28.781326888 L 81.886684648,23.7755768744 L 82.3048432029,21.2605930925 L 83.9764573904,18.5245912635 L 88.8594196,16.0839601854 L 92.7834469013,16.756276881 L 95.404733443,18.5917214773 Z M 76.0366272733,87.9206221133 L 75.0203347212,91.1154850914 L 73.2832903734,93.0732074757 L 71.235070252,94.0805774843 L 67.0896848929,94.5961162556 L 65.189150147,93.9978122531 L 62.1665301051,91.515118538 L 60.7746516512,85.6574163973 L 62.2087627475,82.3888807368 L 64.1669951478,80.4639584354 L 70.0492548493,79.2113528296 L 74.7266640238,82.1202776162 L 75.9632946016,85.0614924697 Z M 31.632894031,38.8834069177 L 31.0017899456,41.0051297161 L 28.7157267223,43.9212769927 L 25.4631660899,45.4282107446 L 22.0797451368,45.3785856069 L 19.9908224212,44.5262934691 L 17.467936128,42.0272847153 L 16.3379483208,38.0620448038 L 16.5266763011,35.8747218397 L 19.4273585657,31.5577735658 L 25.9731824247,30.4035682085 L 30.3966034639,33.5008809647 Z" fill="#febca6" stroke="none"/>
  <path d="M 107.300113167,17.6430691552 L 104.998754937,12.7355493847 L 100.493588698,8.36022343507 L 95.7505793583,5.89367475341 L 90.6386965901,5 L 17.356280937,20.2193152289 L 11.5966390341,23.3889406248 L 6.5246088334,30.4582057665 L 5,36.4711557834 L 6.02300502594,43.9017318523 L 7.92302975586,48.162002504 L 11.395928414,52.7911465837 L 56.3813106093,101.869404384 L 59.305700408,103.795006707 L 64.6140436625,105.802864245 L 72.4950683531,105.705654034 L 80.2290876897,102.331495635 L 84.0390797251,98.2850205405 L 86.5301859675,93.6812840483 L 107.740789218,29.9152248182 L 108.552548767,24.7459844064 Z M 104.9566923,20.6411316362 L 105.382073345,25.0896202522 L 104.16881029,30.832267095 L 83.5482685199,93.0582524797 L 80.9261319514,97.3260856321 L 75.8954843664,101.372390721 L 71.9302444549,102.502378528 L 65.2370752311,102.820946797 L 60.3956656424,101.017962273 L 57.9382095095,99.2972329641 L 11.8307420183,48.334585451 L 8.49745621895,41.2395727111 L 8.10487525695,36.5698960426 L 8.8508646349,33.0636872855 L 10.8011945238,29.0579147852 L 12.9971000207,26.4448707655 L 18.0931777662,23.1768451211 L 89.0407550851,8.15382037319 L 93.9396923228,8.6542341432 L 100.050702577,11.9565899186 L 103.720231727,16.479261233 Z" fill="#15243c" stroke="none"/>
  <path d="M 74.7266640238,82.1202776162 L 70.0492548493,79.2113528296 L 64.0850799433,80.4066007918 L 62.2087627475,82.3888807368 L 60.9549671042,85.0512098835 L 62.1665301051,91.515118538 L 65.189150147,93.9978122531 L 67.0896848929,94.5961162556 L 71.235070252,94.0805774843 L 73.2832903734,93.0732074757 L 75.0203347212,91.1154850914 L 76.2251852483,86.9539546989 Z M 72.5465635496,88.8950220337 L 69.8837243869,91.3031930397 L 66.4757458731,91.114295054 L 64.1331750328,88.0090797863 L 64.6907764411,84.248882894 L 67.3944882033,82.4797184847 L 71.2038002173,83.3158655891 L 72.9236794996,86.9616872049 Z" fill="#14233b" stroke="none"/>
  <path d="M 96.5759338604,20.754656886 L 95.4866486474,18.649079121 L 92.7834469013,16.756276881 L 87.2700606277,16.4360085586 L 84.4598761003,18.0085424761 L 82.3048432029,21.2605930925 L 82.2468055379,26.2251304959 L 83.6309514858,28.781326888 L 86.1375227402,30.7806018931 L 91.1429327431,31.4776461549 L 94.0267899529,30.3229307815 L 96.9109871735,26.7269043087 Z M 94.1914703886,24.3343683201 L 92.6508865271,27.4062734889 L 88.8822771073,28.4297885309 L 86.6295239829,27.4627811058 L 85.4500810434,25.6603065976 L 85.0982026755,22.8502920755 L 86.9664473547,20.0078174813 L 91.2756631226,19.6069939973 L 93.0532400593,20.7295893092 Z" fill="#13223a" stroke="none"/>
  <path d="M 30.0198275246,32.9929046941 L 26.4974737341,30.5265260178 L 24.8672421623,30.2395677942 L 19.0012974995,31.9919071487 L 17.3133682733,34.2281752291 L 16.3626758869,36.9806621022 L 17.7873544237,42.6171761904 L 22.0797451368,45.3785856069 L 25.4631660899,45.4282107446 L 28.7157267223,43.9212769927 L 30.7969169319,41.4720633819 L 31.5755363873,38.9653221221 L 31.0026399724,34.9018519674 Z M 28.5690613789,38.2030177054 L 27.7986844455,40.3492980646 L 25.9306097717,41.9711171091 L 24.2019779513,42.3477230431 L 21.6624366087,41.7902916401 L 19.5410538209,38.7178764553 L 20.6557466215,34.8594493198 L 22.4582211296,33.6800063803 L 24.629229055,33.369000612 L 27.5373038149,34.7948691862 Z" fill="#13223b" stroke="none"/>
  <path d="M 93.5610463246,21.5734689196 L 91.2756631226,19.6069939973 L 86.5403862885,20.4419510643 L 85.2539605677,22.1048127136 L 84.9587598221,24.0955051861 L 86.6295239829,27.4627811058 L 88.8003619029,28.3724308872 L 92.060995052,27.7256917845 L 94.1258702229,24.7767444251 Z" fill="#f9f5eb" stroke="none"/>
  <path d="M 28.5690613789,38.2030177054 L 27.373473406,34.6801538989 L 24.629229055,33.369000612 L 22.4582211296,33.6800063803 L 20.6557466215,34.8594493198 L 19.5410538209,38.7178764553 L 21.5805214042,41.7329339965 L 24.2019779513,42.3477230431 L 25.9306097717,41.9711171091 L 27.7986844455,40.3492980646 Z" fill="#faf9f3" stroke="none"/>
  <path d="M 71.531461035,83.5452961637 L 68.5332285486,82.4225308464 L 65.2315527946,83.6509189022 L 63.9531995906,86.1739752007 L 64.1331750328,88.0090797863 L 65.4927634199,90.4260033304 L 68.1305350057,91.5405261256 L 71.7107564559,90.2630229482 L 72.8908794168,87.1828752574 Z" fill="#fcfaf5" stroke="none"/>
  <path d="M 87.1366590008,27.2441168115 A 4.11,4.11 125 0,1 86.1273432522,21.520002756 A 4.11,4.11 125 0,1 91.8514573076,20.5106870074 A 4.11,4.11 125 0,1 92.8607730562,26.2348010629 A 4.11,4.11 125 0,1 87.1366590008,27.2441168115 Z" fill="#F8F7F2" stroke="#1F2A3A" stroke-width="2.3"/>
  <path d="M 67.2051652043,88.9393358729 A 2.5,2.5 125 0,1 66.5912261844,85.4575146713 A 2.5,2.5 125 0,1 70.073047386,84.8435756515 A 2.5,2.5 125 0,1 70.6869864059,88.3253968531 A 2.5,2.5 125 0,1 67.2051652043,88.9393358729 Z" fill="#F8F7F2" stroke="#1F2A3A" stroke-width="2.3"/>
  <path d="M 21.8280005246,41.2225869724 A 3.82,3.82 125 0,1 20.8899017023,35.9023641764 A 3.82,3.82 125 0,1 26.2101244983,34.964265354 A 3.82,3.82 125 0,1 27.1482233206,40.2844881501 A 3.82,3.82 125 0,1 21.8280005246,41.2225869724 Z" fill="#F8F7F2" stroke="#1F2A3A" stroke-width="2.3"/>
</g>
<g id="kit-head_plate" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 49.6754019339,109.670043919 L 55.5578316408,112.143305074 L 62.594976721,111.73270902 L 66.2730884036,110.011809706 L 73.2600983301,102.555826049 L 114.001354907,49.8571542202 L 115.45076101,45.3020228336 L 115.007534878,39.2643452506 L 113.827411917,36.1841975598 L 110.795699327,32.2031526257 L 105.617706377,28.9924846249 L 101.685266548,28.0836848702 L 40.4550085432,21.8824346237 L 32.6150264574,22.3668733657 L 25.7995794457,26.4066359863 L 21.7043292403,32.9364848172 L 21.1316028307,38.2206105216 L 21.7956770042,41.7841769223 L 45.4639063931,105.050162393 Z M 51.3205885017,99.1181075486 L 51.0171452341,96.7669541756 L 52.1471330413,92.8017142641 L 55.8741898402,89.5816137039 L 59.3312834756,89.1141700221 L 62.1249829589,89.9657821385 L 66.0333752428,94.6758213905 L 66.1566730628,97.6414237994 L 65.3296185072,100.295850435 L 62.5118714791,103.245477815 L 60.7260520204,104.007612227 L 55.753272095,103.705188991 L 52.6808569102,101.583806204 Z M 32.8227895621,43.5849513769 L 29.397815988,39.3909609123 L 29.3480208451,34.7868844095 L 32.4195860031,30.8049894486 L 35.4423760503,29.5429512833 L 38.7193242381,29.6899566373 L 41.7834969009,31.4508785245 L 43.7090992237,34.3752683232 L 44.1191852619,37.7504467542 L 43.5050762367,40.0116124061 L 41.7604693882,42.5760513202 L 39.0818252029,44.3295807121 L 35.3707434321,44.6086364243 Z M 93.0202699711,45.8704168442 L 92.6185964603,44.0763548635 L 93.4372384885,39.8408117779 L 94.5675663065,38.3168829659 L 97.9588897709,36.1864076294 L 100.391958348,35.8256067181 L 103.488761089,36.5870611081 L 107.593783864,41.4035731253 L 107.135772742,46.8515292385 L 102.42573349,50.7599215224 L 96.9777773766,50.3019104001 Z" fill="#eaddf6" stroke="none"/>
  <path d="M 64.2420333477,114.607983697 L 68.1085329999,112.633096247 L 71.6717593899,109.527710974 L 116.066230078,52.8061015796 L 117.966254808,48.5458309279 L 118.621066427,44.4250031297 L 117.497621089,36.5441484443 L 115.670249009,33.0626672534 L 111.860256974,29.0161921589 L 104.89627456,25.3470030198 L 47.2215104386,19.341873249 L 42.8956396212,16.9994724141 L 29.3521832387,5.85161211643 L 26.5584837554,5 L 5.28644820748,29.5389588949 L 5,31.5706939723 L 19.8382946307,45.9625323696 L 41.0315628105,102.90439205 L 44.6452643648,109.285705479 L 49.6513543891,113.471283416 L 53.6821944663,115.043647328 L 59.6872419718,115.599888694 Z M 49.6754019339,109.670043919 L 46.3242710476,106.27889046 L 43.9150800096,101.617796324 L 21.7956770042,41.7841769223 L 21.1316028307,38.2206105216 L 21.7043292403,32.9364848172 L 25.7995794457,26.4066359863 L 31.3206982253,22.7848619152 L 39.1769953498,21.8006894246 L 101.685266548,28.0836848702 L 105.617706377,28.9924846249 L 111.049687462,32.3915405953 L 114.442030959,37.5849985572 L 115.360093268,41.3369529275 L 115.45076101,45.3020228336 L 114.001354907,49.8571542202 L 73.2600983301,102.555826049 L 66.2730884036,110.011809706 L 62.594976721,111.73270902 L 59.6130592734,112.355740589 L 55.0007402485,112.045074831 Z M 8.42429355262,30.8820622379 L 27.0587275201,8.67828168795 L 39.5943038779,18.2123954578 L 39.5206311955,18.630214002 L 35.4982036458,18.6389665401 L 30.5829513694,19.6391140587 L 24.6768141284,23.4084034999 L 21.4494910782,26.6448190989 L 19.3363508125,30.0776951843 L 17.9935874802,35.6568516289 L 18.0514551399,39.4007334825 Z" fill="#14233b" stroke="none"/>
  <path d="M 8.65372412716,31.2097230557 L 17.9121822918,39.3761759217 L 18.2800356877,33.6251165515 L 19.680326669,29.3485308611 L 25.9792148772,22.1302203012 L 32.4015709109,19.0981676999 L 39.5451887563,18.4909411539 L 27.361830777,8.58812396147 L 8.4734086742,30.6035165418 Z" fill="#e9dbf6" stroke="none"/>
  <path d="M 53.6722518908,102.47663093 L 56.1465330784,103.918134522 L 59.4562813491,104.286327928 L 62.1268530178,103.392993186 L 64.7644545982,101.057814841 L 66.0912429025,98.4197032441 L 66.0333752428,94.6758213905 L 62.7722320777,90.3671156386 L 59.3312834756,89.1141700221 L 55.9561050446,89.5242560602 L 52.9498000415,91.5072160267 L 51.2216782371,94.7925767419 L 51.3205885017,99.1181075486 Z M 54.5482515626,98.3230030491 L 54.375838621,95.6359463363 L 57.054312801,92.6617613947 L 60.3558185497,92.6694939007 L 62.6827543726,94.9466345806 L 62.5685491014,98.444770821 L 60.2340507778,100.689791439 L 57.3258060126,100.895004464 Z" fill="#14223b" stroke="none"/>
  <path d="M 32.3148132914,43.2081754376 L 36.869944678,44.6575815405 L 39.8518621256,44.0345499719 L 41.7604693882,42.5760513202 L 44.1191852619,37.7504467542 L 44.0286875247,35.0060323978 L 41.7834969009,31.4508785245 L 39.2518580696,29.9274597286 L 35.4423760503,29.5429512833 L 31.1663003759,31.8046269512 L 29.1678753975,35.4013334454 L 29.0863002037,37.9000021885 L 30.0124350293,40.7917619097 Z M 32.6910792146,39.0382325178 L 32.2974782205,36.3839758878 L 34.8857946741,33.1066876893 L 36.8191295029,32.7295717393 L 38.9983799503,33.4010384081 L 40.5961514501,35.3342032316 L 40.5884189441,38.6357089802 L 37.7624293939,41.2248754605 L 34.6493116149,40.9631548192 Z" fill="#14233b" stroke="none"/>
  <path d="M 96.9204197329,50.2199951956 L 100.238410526,50.9486495028 L 103.031940004,50.5796060695 L 107.455191037,46.2616377634 L 107.618341425,41.2643002772 L 105.438750967,38.1515225089 L 103.234772953,36.3986731384 L 99.7529517516,35.7847341186 L 97.352683257,36.3667230823 L 93.0113474277,40.6273337447 L 93.0202699711,45.8704168442 Z M 96.6248789767,45.7879916237 L 96.0427200076,42.1670675794 L 98.0658725522,39.6517437869 L 100.744686743,39.1188699447 L 103.866217049,40.9617070363 L 104.669394065,43.3291754481 L 103.383648366,46.5489359976 L 99.5825788742,47.7455440026 Z" fill="#15233c" stroke="none"/>
  <path d="M 55.9493925707,100.149695107 L 58.6611768496,101.058664867 L 60.2340507778,100.689791439 L 62.2491308057,99.034662296 L 62.953227552,95.8559443514 L 61.3389710082,93.2018577268 L 58.4059986768,92.3256880496 L 55.6617543258,93.6368413365 L 54.2121782175,96.9713171733 Z" fill="#f6f0ee" stroke="none"/>
  <path d="M 97.7064316837,46.9839196073 L 98.7469417858,47.5981986379 L 102.236835504,47.3519430085 L 103.383648366,46.5489359976 L 104.595551378,42.5263384425 L 102.448761002,39.6347487267 L 99.3847583451,39.0944823893 L 96.5177261901,41.1019999165 L 96.1577753055,44.7722090877 Z" fill="#f7f3f1" stroke="none"/>
  <path d="M 34.8459421066,41.0696275844 L 37.7624293939,41.2248754605 L 40.5884189441,38.6357089802 L 40.8010244638,35.8011368974 L 38.4084884752,33.0816201125 L 35.0496250829,32.991972402 L 32.4776236681,35.769526852 L 32.8303520627,39.0627900786 Z" fill="#f3eeec" stroke="none"/>
  <path d="M 60.4133209716,99.6730996486 A 3.58,3.58 55 0,1 55.4273530109,98.7939389721 A 3.58,3.58 55 0,1 56.3065136873,93.8079710114 A 3.58,3.58 55 0,1 61.292481648,94.6871316879 A 3.58,3.58 55 0,1 60.4133209716,99.6730996486 Z" fill="#F8F7F2" stroke="#1F2A3A" stroke-width="2.3"/>
  <path d="M 38.1930279606,38.9457122644 A 2.5,2.5 55 0,1 34.711206759,38.3317732446 A 2.5,2.5 55 0,1 35.3251457788,34.849952043 A 2.5,2.5 55 0,1 38.8069669804,35.4638910628 A 2.5,2.5 55 0,1 38.1930279606,38.9457122644 Z" fill="#F8F7F2" stroke="#1F2A3A" stroke-width="2.3"/>
  <path d="M 102.176061848,46.2713845591 A 3.58,3.58 55 0,1 97.1900938872,45.3922238827 A 3.58,3.58 55 0,1 98.0692545636,40.406255922 A 3.58,3.58 55 0,1 103.055222524,41.2854165984 A 3.58,3.58 55 0,1 102.176061848,46.2713845591 Z" fill="#F8F7F2" stroke="#1F2A3A" stroke-width="2.3"/>
</g>
<g id="kit-l_bracket" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 119.19646597,40.8202254905 L 114.892533914,33.9328334693 L 110.570638077,30.0186009296 L 105.77855082,27.1038282584 L 45.8261616141,5.28294311427 L 42.4173578365,5 L 38.4699586105,5.90445527842 L 32.052758009,9.20892746629 L 27.5657280066,14.812190958 L 5.98425696276,74.1067953296 L 5,80.0272039499 L 6.30451712277,89.0154315325 L 7.73893106868,92.0915421663 L 10.190078445,95.0056246188 L 20.4240912306,99.0497539816 L 22.8759288256,99.6228965537 L 25.071768977,99.1451036811 L 29.7716125184,96.1733246369 L 31.6603247595,94.2003152426 L 51.1378542579,42.4405253991 L 100.224011077,60.2000076187 L 106.691306818,60.8512263284 L 112.655244452,59.0844643481 L 115.637730933,56.4453784476 L 119.570617472,46.8093832488 L 119.938893067,43.7508912861 Z M 116.180467693,41.2123407726 L 116.734611157,45.2450724798 L 115.57174267,48.4400273904 L 113.343080941,44.3299097644 L 110.575823764,41.407190531 L 103.563021341,36.4071303136 L 41.577510384,13.739831592 L 39.0057931842,14.0808164073 L 37.2880910146,15.5839794912 L 14.4753474548,78.2614772976 L 14.1312566554,86.2239895596 L 15.9059651979,94.2127572736 L 11.993458205,92.6823034096 L 9.3802826473,88.7514875267 L 8.04121840085,81.0276991464 L 8.7777695917,74.9107152211 L 30.4618466785,15.3342030632 L 32.9147196015,12.3959358147 L 38.1614502628,9.09111851752 L 42.3651920416,8.0671287436 L 46.2780441439,8.42711266746 L 103.693263274,29.3245434247 L 107.187054423,31.128268294 L 112.038563818,35.3416821818 Z M 112.801724618,54.8810676786 L 111.400132249,56.3928675434 L 108.52059692,57.5795757174 L 102.010462385,57.3384360704 L 51.4207973722,39.0317216216 L 42.3710679478,17.1147784646 L 97.4798943211,36.7470798008 L 104.441911387,40.1323890011 L 108.097730717,42.9528473008 L 112.410644664,48.3536595813 L 113.503383576,51.1989928957 Z M 22.013967233,96.4358882053 L 19.3234057564,94.1795905873 L 17.6585596005,90.2746850473 L 16.9769350792,83.9607807075 L 17.3714661268,78.7834894029 L 39.3205225473,18.771332949 L 48.1653849951,40.0816217382 L 29.3200750978,91.8586851435 L 24.8675922191,96.197509433 Z" fill="#14233b" stroke="none"/>
  <path d="M 116.180467693,41.2123407726 L 112.038563818,35.3416821818 L 107.187054423,31.128268294 L 103.693263274,29.3245434247 L 46.2780441439,8.42711266746 L 42.3651920416,8.0671287436 L 38.1614502628,9.09111851752 L 32.9147196015,12.3959358147 L 30.3934426499,15.5221415874 L 10.2570929889,70.5539271511 L 8.7777695917,74.9107152211 L 8.04121840085,81.0276991464 L 9.3802826473,88.7514875267 L 11.993458205,92.6823034096 L 15.9059651979,94.2127572736 L 14.1312566554,86.2239895596 L 14.4753474548,78.2614772976 L 37.2880910146,15.5839794912 L 39.0057931842,14.0808164073 L 41.577510384,13.739831592 L 103.563021341,36.4071303136 L 111.31894108,41.9969164462 L 115.57174267,48.4400273904 L 116.734611157,45.2450724798 Z" fill="#eeeae4" stroke="none"/>
  <path d="M 112.177796688,55.7181542564 L 113.571442495,52.1815243117 L 112.410644664,48.3536595813 L 108.131932732,42.8588780387 L 104.441911387,40.1323890011 L 96.4462324382,36.3708576432 L 43.3535993638,17.0467195453 L 42.3368659335,17.2087477267 L 51.4207973722,39.0317216216 L 101.916493123,57.3042340561 L 107.819973291,57.7502406798 Z M 101.201701915,47.5728891578 L 99.0393735593,50.2976526487 L 96.4676563595,50.638637464 L 93.2298626536,49.8858480393 L 88.198706406,46.4583902625 L 87.2255019895,43.8693995009 L 88.4139357103,40.8965851287 L 90.8833919764,39.6670381595 L 96.393721534,40.608456327 L 100.177712141,43.369147379 L 101.441461125,45.744634383 Z" fill="#eee9e3" stroke="none"/>
  <path d="M 39.3205225473,18.771332949 L 17.4056681411,78.6895201408 L 16.9769350792,83.9607807075 L 17.6585596005,90.2746850473 L 19.4429402519,94.4359331402 L 22.013967233,96.4358882053 L 24.8675922191,96.197509433 L 29.3200750978,91.8586851435 L 48.1653849951,40.0816217382 Z M 26.5289782343,82.8614756707 L 22.4627347315,81.1686485159 L 21.805985225,77.417824595 L 25.1574375202,69.3793068515 L 26.9691089518,67.9103457819 L 29.5066241373,67.6633302287 L 31.6160964796,70.3466353617 L 32.0251402142,73.9008839776 L 29.5967971966,80.5727015852 Z" fill="#ede9e3" stroke="none"/>
  <path d="M 101.201701915,47.5728891578 L 101.432824344,46.0607441836 L 100.177712141,43.369147379 L 95.4540289133,40.2664361836 L 90.4391108994,39.7181686263 L 88.4139357103,40.8965851287 L 87.5505936804,42.3914565411 L 87.2852692373,43.9975707773 L 88.1047371439,46.4241882482 L 91.0088023781,48.9710304333 L 93.0419241295,49.8174440107 L 97.9884381146,50.5536500922 L 100.039178537,49.5973741282 Z M 98.2458159955,46.9227057761 L 97.3144150463,47.4350457724 L 94.6660021462,47.1096089722 L 91.2748170398,45.0239763166 L 90.5320448335,43.2637804612 L 92.8816214948,42.9483608793 L 97.750749561,45.3590852258 Z" fill="#132135" stroke="none"/>
  <path d="M 30.2241762196,68.0309156054 L 27.0972802282,67.8505785341 L 24.2429650235,70.4298971868 L 21.805985225,77.417824595 L 21.873699035,79.5708259512 L 22.9837115087,81.7839396645 L 26.5289782343,82.8614756707 L 27.9046602605,82.2980052076 L 29.8617765303,80.1370572891 L 32.0251402142,73.9008839776 L 31.9149327183,70.9874917438 Z M 25.4704413367,79.9221730941 L 25.0527608212,76.6840342789 L 26.8139920046,72.4298522519 L 28.2667148404,71.3623334641 L 28.9493746897,74.1648279833 L 27.0855374632,78.7009177965 Z" fill="#15233a" stroke="none"/>
  <path d="M 98.2458159955,46.9227057761 L 97.750749561,45.3590852258 L 92.8816214948,42.9483608793 L 90.5320448335,43.2637804612 L 91.2748170398,45.0239763166 L 94.6660021462,47.1096089722 L 97.3144150463,47.4350457724 Z" fill="#f2ede5" stroke="none"/>
  <path d="M 28.1727455783,71.3281314497 L 25.6428318457,74.770447023 L 24.898679202,77.6921309283 L 25.1885335505,79.8195670511 L 26.0086916758,79.9052446417 L 27.649698145,77.7356599423 L 29.0606175136,73.5668103965 Z" fill="#f5f1eb" stroke="none"/>
</g>
<g id="kit-lower_arm" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 18.6914817686,8.15382037319 L 14.2428231473,9.79985696777 L 10.4738737168,13.2646831092 L 8.44162862346,17.2130979659 L 8.01505754117,21.309198198 L 8.85825713021,25.6840141317 L 13.3302832749,32.7218392333 L 42.8380132827,334.039452176 L 42.3951271617,337.63581866 L 40.5677550821,341.117299851 L 39.8871958645,345.401788053 L 41.07437131,350.505768309 L 44.9568459903,355.421700607 L 49.4049945956,357.437630662 L 54.197459068,357.74141394 L 59.2032090816,355.997147103 L 61.9725210095,353.785606588 L 64.7421729481,349.132754975 L 65.1280414362,343.176992596 L 63.3755320764,338.531703483 L 60.2957243963,334.910269423 L 47.0505343304,204.412970829 L 30.124940247,29.8322895817 L 32.4850161635,24.8926497498 L 33.1166302648,19.1089603021 L 31.5361938359,14.2179255758 L 28.2106405425,10.4244185845 L 23.3774734759,8.2609731598 Z M 15.9134173027,14.3877884372 L 19.3052507831,12.8562971245 L 23.2375206064,13.1681529195 L 27.1366503362,16.1425078665 L 28.5206262787,19.9193598083 L 28.4874861852,22.5818589603 L 26.7174717492,25.9814249468 L 25.0460275671,27.496771226 L 21.465806117,28.7742744034 L 18.6968341998,28.5445038181 L 14.0522251081,25.414390979 L 12.7175342925,20.6954291836 L 13.692954245,16.8615596088 Z M 48.7359080016,338.169202518 L 51.8900683855,337.325832924 L 55.347162021,337.793276606 L 59.2708493115,340.906904401 L 60.2126191544,343.397500627 L 60.1137088898,347.723031434 L 56.6313776722,351.998937103 L 54.3619694983,352.973507029 L 50.7819180535,353.030354656 L 46.3011393707,350.014957104 L 44.9415509836,347.59803356 L 44.7864731128,343.460890723 L 45.5568500462,341.314610364 Z" fill="#e3f1e3" stroke="none"/>
  <path d="M 20.2894232737,5 L 13.4813687573,6.70305422752 L 9.90097730187,9.20121295458 L 5.7629844381,15.459568574 L 5,23.3486657814 L 6.47396366367,28.043070016 L 10.0533350871,32.8688445874 L 29.033011739,223.170872622 L 39.6182527332,335.325197876 L 37.0859338805,341.731238871 L 36.8723083286,346.220600086 L 37.3306594617,349.2272451 L 39.1487689872,353.430158108 L 43.7521654686,358.36257545 L 49.6912727977,360.690021289 L 54.9343558972,360.698943832 L 61.0625312174,358.397755608 L 65.2575417141,354.498795883 L 67.9700060144,348.707203924 L 68.3476319804,343.111902446 L 66.5870501039,337.606418684 L 63.228866733,332.813444196 L 33.5162637114,31.9627649182 L 33.4018884349,29.6852842276 L 35.9094797214,24.3606259344 L 36.1069602399,18.1508754205 L 34.0187175456,12.4159610837 L 29.3579634206,7.56545894623 L 26.0648701993,5.99207500194 Z M 18.6914817686,8.15382037319 L 23.3774734759,8.2609731598 L 28.2106405425,10.4244185845 L 31.5361938359,14.2179255758 L 33.1166302648,19.1089603021 L 32.4850161635,24.8926497498 L 30.124940247,29.8322895817 L 47.0505343304,204.412970829 L 60.2957243963,334.910269423 L 63.3755320764,338.531703483 L 65.1280414362,343.176992596 L 64.7421729481,349.132754975 L 61.9725210095,353.785606588 L 59.2032090816,355.997147103 L 54.197459068,357.74141394 L 49.4049945956,357.437630662 L 44.9568459903,355.421700607 L 41.07437131,350.505768309 L 39.8871958645,345.401788053 L 40.5677550821,341.117299851 L 42.3951271617,337.63581866 L 42.8380132827,334.039452176 L 13.3302832749,32.7218392333 L 8.85825713021,25.6840141317 L 8.01505754117,21.309198198 L 8.44162862346,17.2130979659 L 10.4738737168,13.2646831092 L 14.2428231473,9.79985696777 Z" fill="#14243b" stroke="none"/>
  <path d="M 44.7864731128,343.460890723 L 44.9415509836,347.59803356 L 46.3011393707,350.014957104 L 50.7819180535,353.030354656 L 54.3619694983,352.973507029 L 56.3773895369,352.187325072 L 60.1710665335,347.641116229 L 60.5236249227,345.568508552 L 59.5902676072,341.496795876 L 58.0012486455,339.407533149 L 55.347162021,337.793276606 L 50.9151584491,337.497735849 L 48.817823206,338.226560162 L 45.5568500462,341.314610364 Z M 49.6038351568,341.46263575 L 53.9212934468,340.701351366 L 56.2231616928,341.946904487 L 57.0090036382,346.403635625 L 54.5263099232,349.426255667 L 51.2739192961,349.712533869 L 48.841020724,348.131077408 L 47.8994208865,344.419825632 Z" fill="#15233a" stroke="none"/>
  <path d="M 15.094095253,15.0348675506 L 13.373365944,17.4923236834 L 12.7175342925,20.6954291836 L 14.0522251081,25.414390979 L 17.0748451499,27.897084694 L 21.465806117,28.7742744034 L 24.2595056003,27.9226622869 L 26.7174717492,25.9814249468 L 28.4874861852,22.5818589603 L 28.5206262787,19.9193598083 L 27.7509293667,17.1830179686 L 25.5148312917,14.2744331927 L 20.6651791809,12.8319095691 L 18.2156255594,13.1920304589 Z M 16.7157442922,18.1235977741 L 18.7804494577,16.3953059644 L 22.4178585461,16.2565431324 L 25.1045752482,18.8702671735 L 24.7516768482,23.3841859498 L 21.4007159673,25.5546838591 L 18.7710168982,25.3003557131 L 16.1990154834,22.5228012632 L 15.9618524029,19.5489563322 Z" fill="#15223a" stroke="none"/>
  <path d="M 15.9618524029,19.5489563322 L 16.1990154834,22.5228012632 L 18.7710168982,25.3003557131 L 21.4007159673,25.5546838591 L 24.7516768482,23.3841859498 L 25.1045752482,18.8702671735 L 22.4178585461,16.2565431324 L 20.0912627339,16.0923727128 L 17.9939274909,16.8211970253 Z" fill="#f9f5ee" stroke="none"/>
  <path d="M 48.2026941488,343.289327808 L 48.4970448676,347.401913085 L 50.6677127823,349.532218416 L 54.5263099232,349.426255667 L 56.7958881024,347.231030191 L 57.1730040524,345.297695362 L 56.4852223449,342.618711166 L 54.6667728087,340.857109258 L 50.2510842755,341.06130225 Z" fill="#f7f3eb" stroke="none"/>
  <path d="M 24.2519941012,23.0343043236 A 4.35,4.35 35 0,1 18.1936252104,24.1025582182 A 4.35,4.35 35 0,1 17.1253713159,18.0441893274 A 4.35,4.35 35 0,1 23.1837402067,16.9759354328 A 4.35,4.35 35 0,1 24.2519941012,23.0343043236 Z" fill="#F8F7F2" stroke="#1F2A3A" stroke-width="2.3"/>
  <path d="M 55.7562192531,347.687197577 A 4.35,4.35 35 0,1 49.6978503623,348.755451471 A 4.35,4.35 35 0,1 48.6295964677,342.69708258 A 4.35,4.35 35 0,1 54.6879653585,341.628828686 A 4.35,4.35 35 0,1 55.7562192531,347.687197577 Z" fill="#F8F7F2" stroke="#1F2A3A" stroke-width="2.3"/>
</g>
<g id="kit-shade" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 8.3842738722,9.4590490036 L 16.2986983202,222.712939673 L 129.05353019,153.579243909 L 126.654230641,71.5530690523 L 30.0966951619,20.2859027359 Z" fill="#ebe9e4" stroke="none"/>
  <path d="M 221.975326012,72.9346541266 L 218.189609858,69.8429954776 L 212.601894382,69.1098953802 L 137.034723593,71.7123363589 L 129.875441004,72.5089999069 L 132.701402959,152.783615689 L 216.487428562,149.956618407 L 220.041332068,149.195192201 L 222.92846885,147.186600355 L 224.756033406,144.605901265 L 225.387217679,141.077217883 L 223.737592524,80.7002459741 L 223.120920938,75.4973894361 Z" fill="#ece9e4" stroke="none"/>
  <path d="M 225.119150456,72.2160667163 L 221.726239803,68.4493496709 L 215.898765117,65.8879947987 L 128.310785126,68.5025236518 L 9.2375986838,5.95593085459 L 6.01638832103,5 L 5,6.00844175879 L 13.1472724234,226.626827103 L 14.8732662645,227.275630048 L 131.369595056,156.141634109 L 150.045638523,155.409923497 L 150.985676253,156.238373294 L 152.129191475,180.723927666 L 154.429018107,186.165508086 L 160.240254559,191.606053178 L 167.101391128,193.791185892 L 173.158607806,193.182805978 L 177.814232115,191.062626198 L 182.802204458,186.054619419 L 185.166984025,179.979438961 L 185.065422357,154.263302291 L 218.402051146,152.877957203 L 224.245073847,150.219181975 L 227.430701758,146.399263807 L 228.642284947,140.956648059 L 226.915618982,80.0756278259 L 226.589837072,76.2567449856 Z M 221.09505553,71.9780330533 L 222.915708852,74.9335738637 L 223.488851424,77.3854114586 L 225.186846171,127.954342769 L 225.191332593,143.170451991 L 222.92846885,147.186600355 L 220.605147641,148.989980115 L 217.495525211,149.802536788 L 132.735604973,152.877584951 L 129.944190142,73.8674083712 L 130.968870135,72.0046064728 L 214.370381909,68.9983074469 L 218.189609858,69.8429954776 Z M 9.27283602616,9.56130993726 L 126.654230641,71.5530690523 L 129.147499452,153.545041895 L 16.008153753,222.499435915 L 8.33314340538,9.90333008058 Z M 180.887590921,154.187641918 L 181.562649318,154.580447419 L 182.235628011,176.896071983 L 181.741251795,180.800632414 L 180.247070601,184.004914324 L 176.061982822,188.295023912 L 170.458029111,190.441114034 L 165.61377606,190.288757962 L 162.41813093,189.110686569 L 157.427397713,184.754933827 L 155.409823976,180.381217304 L 154.595886866,172.589715114 L 154.530942979,155.160837287 Z" fill="#14243b" stroke="none"/>
  <path d="M 180.887590921,154.187641918 L 154.530942979,155.160837287 L 154.595886866,172.589715114 L 155.409823976,180.381217304 L 157.427397713,184.754933827 L 162.41813093,189.110686569 L 165.61377606,190.288757962 L 170.458029111,190.441114034 L 176.061982822,188.295023912 L 180.247070601,184.004914324 L 181.741251795,180.800632414 L 182.235628011,176.896071983 L 181.562649318,154.580447419 Z M 174.997924174,172.506807446 L 175.666071337,178.435852847 L 174.342555105,180.939511127 L 171.523822352,183.136041497 L 168.567936433,183.786224879 L 165.996219233,183.445240064 L 162.210503079,180.353581415 L 161.192389211,175.509673473 L 163.03653711,171.220254103 L 165.146354562,169.70741891 L 167.845897929,168.937701033 L 172.169174203,169.705348254 Z" fill="#eceae5" stroke="none"/>
  <path d="M 173.00660589,170.251890265 L 170.571351638,169.116312558 L 167.845897929,168.937701033 L 165.146354562,169.70741891 L 161.943453089,172.895117478 L 161.064217935,175.449906225 L 161.475332325,178.91847725 L 163.031006314,181.438373765 L 165.19298956,182.992667315 L 167.269295216,183.726802741 L 170.866037518,183.375455598 L 174.342555105,180.939511127 L 175.666071337,178.435852847 L 175.75036849,174.574131211 L 174.895318131,172.224899659 Z M 172.196119874,174.165087477 L 172.709150089,175.574626408 L 172.308398026,178.274514884 L 171.112707962,179.667470472 L 168.447366609,180.531157611 L 166.217324443,179.959395477 L 165.012307379,178.695301384 L 164.388034341,176.687744866 L 164.712090703,174.654278005 L 166.898603855,172.475021197 L 170.281842399,172.414218621 Z" fill="#15243b" stroke="none"/>
  <path d="M 171.247445363,173.020527879 L 168.692656616,172.141292725 L 166.898603855,172.475021197 L 164.712090703,174.654278005 L 164.644722003,177.977749301 L 166.217324443,179.959395477 L 170.053480845,180.265833168 L 172.57303225,177.53968924 L 172.529503236,174.788670297 Z" fill="#f9f7f3" stroke="none"/>
  <path d="M 165.293835545,177.305178406 A 3.47,3.47 160 0,1 167.367759042,172.857635115 A 3.47,3.47 160 0,1 171.815302334,174.931558612 A 3.47,3.47 160 0,1 169.741378837,179.379101903 A 3.47,3.47 160 0,1 165.293835545,177.305178406 Z" fill="#F8F7F2" stroke="#1F2A3A" stroke-width="2.3"/>
</g>
<g id="kit-upper_arm" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 340.934844818,168.967806972 L 341.693855258,164.328420897 L 340.650176157,159.706653494 L 338.957694111,156.810879931 L 335.684663063,153.958290273 L 331.301274431,152.148344388 L 325.551530773,152.431977721 L 320.040510997,151.032456008 L 34.4151399053,17.9991993064 L 29.5007572784,11.8065550088 L 26.791886912,9.91922320504 L 21.3661996168,8.16938967726 L 16.3854836173,8.81162649669 L 11.3543273696,12.2390842735 L 9.32189583693,15.4264377313 L 8.13553277227,19.4764430003 L 8.68380032962,24.4913610141 L 10.7867065471,28.5147657216 L 14.0597375953,31.3673553796 L 18.4089242124,33.0833320024 L 25.2607337819,32.611415036 L 309.877663115,164.628283417 L 316.337702512,168.342834667 L 319.824927536,173.245819638 L 323.508037647,176.055570501 L 328.44660507,177.3441945 L 333.170978517,176.582423185 L 338.116802283,173.505277223 Z M 336.960499921,163.603612471 L 336.551456186,167.157861087 L 335.441443712,169.370974801 L 333.656372842,171.191283013 L 330.085540883,172.490959558 L 327.137946635,172.2867828 L 324.608723121,171.185407107 L 322.856818937,169.588274761 L 321.180920235,164.983780919 L 321.957204237,160.976614445 L 323.91294007,158.455682603 L 328.004748806,156.54071491 L 333.037285491,157.795136894 L 334.977128199,159.323865211 Z M 28.2898643084,19.5901106369 L 27.5564191016,24.0073561733 L 26.0276907843,25.9471988813 L 21.5344397664,28.2211151704 L 17.1513962443,27.5816392257 L 15.1859883029,26.2750514469 L 13.8099611674,24.5411110436 L 12.8181027517,21.8160024433 L 13.0392079622,18.3301578561 L 14.5762279511,15.5359550085 L 16.6774086218,13.707010015 L 19.30854796,12.7493536137 L 21.9058303932,12.8681978905 L 25.5630301614,14.7296193516 L 26.9988245447,16.3353884785 Z" fill="#dbeddc" stroke="none"/>
  <path d="M 343.250909683,171.530197172 L 344.778602673,166.078944644 L 344.247263568,160.525776291 L 342.127083788,155.870151982 L 336.802967208,150.89081642 L 331.437047161,149.012811616 L 324.57660081,149.168618782 L 318.279279814,146.778273981 L 36.2427044614,15.4185002164 L 31.8496437211,9.78103471034 L 26.2781664783,6.16874439348 L 20.425471668,5 L 15.9232387598,5.78733654834 L 10.6526684118,8.55700949059 L 6.64722748479,13.6330751896 L 5,19.340670271 L 5.90756126252,25.9275005067 L 8.92493997667,31.0014955496 L 14.2231462141,35.0325017101 L 19.512025452,36.4064581895 L 25.7658174347,36.045784047 L 297.155540064,162.128766448 L 311.96364088,169.189938463 L 314.091422112,170.650262752 L 318.843431448,176.68917054 L 323.697011499,179.498576293 L 330.113521882,180.462108601 L 335.452841368,179.050844123 L 340.330261106,175.785759637 Z M 340.934844818,168.967806972 L 338.424275303,173.180530641 L 335.14433302,175.864180884 L 330.027154073,177.301010595 L 323.508037647,176.055570501 L 319.824927536,173.245819638 L 316.337702512,168.342834667 L 309.877663115,164.628283417 L 25.2607337819,32.611415036 L 18.4089242124,33.0833320024 L 14.0597375953,31.3673553796 L 10.7867065471,28.5147657216 L 8.68380032962,24.4913610141 L 8.13553277227,19.4764430003 L 9.32189583693,15.4264377313 L 11.3543273696,12.2390842735 L 16.3854836173,8.81162649669 L 21.3661996168,8.16938967726 L 26.791886912,9.91922320504 L 29.5007572784,11.8065550088 L 34.4151399053,17.9991993064 L 320.040510997,151.032456008 L 325.551530773,152.431977721 L 331.301274431,152.148344388 L 335.684663063,153.958290273 L 338.957694111,156.810879931 L 340.650176157,159.706653494 L 341.693855258,164.328420897 Z" fill="#13243b" stroke="none"/>
  <path d="M 336.062610767,160.844301857 L 332.199853804,157.248594883 L 328.004748806,156.54071491 L 324.809793895,157.703583397 L 322.076738733,160.720271893 L 321.368168541,162.57443701 L 321.215122249,165.077750181 L 322.395264299,168.904924693 L 326.018607162,171.842846832 L 328.915070943,172.491304667 L 333.656372842,171.191283013 L 335.381676465,169.499146077 L 336.773251615,166.01295638 L 336.960499921,163.603612471 Z M 333.868151053,165.048388745 L 332.399535093,168.030530117 L 329.366953473,169.347135114 L 325.786794514,167.989761978 L 324.299179446,164.487334047 L 326.280135402,160.573791726 L 328.75753823,159.778508616 L 332.175323898,160.982145242 L 333.252169686,162.186472087 Z" fill="#15243c" stroke="none"/>
  <path d="M 27.4261771692,16.9247692844 L 24.8195677364,14.1488753266 L 22.606454023,13.0388628529 L 19.30854796,12.7493536137 L 16.6774086218,13.707010015 L 14.5762279511,15.5359550085 L 13.0392079622,18.3301578561 L 12.8181027517,21.8160024433 L 13.8099611674,24.5411110436 L 15.4765328701,26.4885552044 L 18.4928762562,28.0511404268 L 21.5344397664,28.2211151704 L 25.3529774973,26.7248633207 L 27.9319510406,22.7000781758 L 28.2556622941,19.4961413748 Z M 25.1460398646,20.3086980472 L 23.9082012237,23.632514453 L 22.1058567917,24.8206030644 L 19.9956942308,25.1629683171 L 17.5604399789,24.0273906099 L 16.3381493532,22.1310769158 L 15.9615820862,19.9269450928 L 17.4986020751,17.1327422451 L 20.2492759088,15.918743291 L 22.5732873367,16.4563034114 L 24.4191607827,18.019233743 Z" fill="#15233c" stroke="none"/>
  <path d="M 332.175323898,160.982145242 L 328.75753823,159.778508616 L 325.511452853,161.38565818 L 324.299179446,164.487334047 L 325.786794514,167.989761978 L 329.366953473,169.347135114 L 332.399535093,168.030530117 L 333.816675477,164.322199882 Z" fill="#ecf4e9" stroke="none"/>
  <path d="M 24.4191607827,18.019233743 L 21.3599786013,16.0465694581 L 18.1477501288,16.5772183442 L 16.9776252979,17.7480333938 L 15.8593211526,20.8155072467 L 16.8169775539,23.4466465849 L 19.9956942308,25.1629683171 L 22.1058567917,24.8206030644 L 23.9082012237,23.632514453 L 25.1460398646,20.3086980472 Z" fill="#e4f0e3" stroke="none"/>
  <path d="M 329.770365592,166.976173566 A 2.5,2.5 70 0,1 326.566083682,165.481992372 A 2.5,2.5 70 0,1 328.060264876,162.277710462 A 2.5,2.5 70 0,1 331.264546786,163.771891656 A 2.5,2.5 70 0,1 329.770365592,166.976173566 Z" fill="#F8F7F2" stroke="#1F2A3A" stroke-width="2.3"/>
  <path d="M 21.3731390288,23.0121438639 A 2.5,2.5 70 0,1 18.1688571185,21.5179626702 A 2.5,2.5 70 0,1 19.6630383122,18.31368076 A 2.5,2.5 70 0,1 22.8673202225,19.8078619536 A 2.5,2.5 70 0,1 21.3731390288,23.0121438639 Z" fill="#F8F7F2" stroke="#1F2A3A" stroke-width="2.3"/>
</g>
</defs></svg>
````
