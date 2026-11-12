# C · desk_lamp · claude-haiku-5-5 · trial 1

- Result: **FAIL**, score 0.67, tags: fail, wrong connection (far off), failed:joint, failed:orient
- Model version: `claude-haiku-5-5`, response id: `msg_vrtx_011CgrW8pXqoGtKbC7P8Axq7`
- Started 2026-11-08T20:41:00-0500, finished 2026-11-08T20:46:57-0500, 356.9 s, attempts 1
- Tokens: input 25,614, output 76,806 (thinking not reported separately by this provider)
- Settings: `{"provider": "anthropic", "route": "vertex", "max_tokens": 128000, "thinking": {"type": "adaptive", "display": "summarized"}, "output_config": {"effort": "high"}}`, prompt sha256 `689a4396384fecc622c40e22b79c109d3476055cadb95a2c4780b04cd6699670`

## Failed checks

- Lower arm: its bottom end hole on the l bracket's upright pin hole (within 6 px): error 73.77 (tolerance 6)
- Bulb: its screw cap on the shade's socket at narrow end of cone (within 6 px): error 104.5 (tolerance 6)
- L bracket faces the way it does on the working object (within 8 deg): error 90.0 (tolerance 8.0)

## Thinking summary (as returned by the provider)

````text
I'm starting to map out the geometry of each part, beginning with the kit-base plate and tracing its outline coordinates to understand its bounding box and shape.

Then I move to the kit-l_bracket, tracing its outline points to understand the foot and overall L-shape so I can figure out where to position and rotate it on the canvas.

Tracing the rest of the outline, it loops down to the bottom-left foot, curves around the base, then sweeps back up through the middle toward the right arm tip, forming a bent, angular shape like a wide V or boomerang rather than a clean L.

I'm mapping out the lower arm piece, which looks like a long strip from roughly (5,5) to (65,357), with mounting holes near the top (around 20,20) and near the bottom (around 52,345).

Now I'm checking the upper arm's hole positions, estimating centers around (20.6,20.7) and (328.4,164.7) based on the circle coordinates.

Moving to the elbow plate, I'm locating three holes: a larger radius hole near (89.5,23.9), a mid-size one around (68.6,86.9), and a third near (24.0,38.1) with radius 3.82.

I'm now figuring out which hole corresponds to "right" versus "bottom" based on their x/y positions — (89.5,23.9) appears rightmost, while (68.6,86.9) sits lowest, so I'm tentatively assigning those labels accordingly.

Looking at the head plate, I'm locating its three holes at approximately (58.9,96.2), (36.5,36.7), and (100.6,43.8), and trying to determine which one matches the "arm hole" where the upper arm's top end attaches versus the other labeled hole.

I'm also checking the shade for its single lug hole, found around (168.6,175.3) with radius 3.47, comparing it against the head plate's 3.58 radius holes to see which ones correspond to matching connection points.

Since the grader likely only checks positions and not pin radii, I should focus on geometric reasoning—orientation of the upper arm and shade shape—to determine the correct hole matches rather than relying on exact radius equality. I'm now tracing the shade's outline coordinates to figure out its narrow end and overall orientation.

There's also a narrow neck piece lower right with a circular element, suggesting a socket connector. So overall the shade forms a cone shape, wide at the left opening (~213 tall) and narrowing to about 80 units wide at the right end before continuing into the socket neck.

Now I'm examining the bulb shape separately — its outline spans roughly x 5-179, y 5-159, with a small circular feature near the upper left around (15.4, 18.7) that looks like the screw cap detail.

So the screw cap appears to be that tiny circle near (15.4,18.7) at the narrow end of the neck—likely the socket contact point the grader wants, though it's a bit ambiguous whether they mean the cap's center or the base of the bulb's neck.

Maybe that (150–185,150–193) piece is the socket, so the one circle there could be the lug hole, leaving the actual socket location to be inferred elsewhere, perhaps near the cone's narrow end around (130,113).

So the lug attaches to the head plate, and the bulb inserts from the narrow end of the shade. I'm trying to work out whether the bulb's cap (at its tapered left end) connects to the shade's socket near x≈130, with the globe extending toward the shade's wide opening.

Let me reconsider the shade's overall geometry by tracing through the actual path coordinates for both fill pieces, trying to figure out where the narrow neck versus wide opening actually sit based on the real outline points rather than assumptions.

Tracing the outline further, it tapers from the wide cone base near (5,5)-(14,227) rightward along a top edge through (9,6), (128,68.5), (215.9,65.9) to the cylinder end around (226.6,76), while the bottom edge runs (14.9,227)→(131.4,156)→(150,155), dips into a socket shape between (152,180) and (185,180), then back up through (185,154), (218,153) to (228.6,141) at the right end — confirming this is a lampshade-like form.

The narrow end sits at the right around x≈225 with an opening spanning y 72–150, versus the wide left opening spanning the full 5–227 range, so the cone tapers from a large mouth on the left down to a smaller cylindrical opening on the right. There's also a mounting lug hanging below the cone near x 152–185, y 153–193, with a hole around (168.6, 175.3) for attaching to a head plate.

Looking at the bulb geometry now, I'm figuring its cap inserts into that narrow right opening around (225,111) while its globe extends outward through the wide left mouth, with the globe spanning roughly x up to 179 and y 27–159.

Tracing the outline further, I see the neck tapers diagonally from the globe up to around (68,30) down to (37,67), then connects into the screw cap region in the upper-left corner of the shape.

I'm trying to pin down the overall axis: the globe looks centered around (115,95), while the cap occupies roughly x 5–70, y 5–70, and I need to figure out the cap's own center to understand the bulb's orientation.

Since the grader likely needs the screw cap's end-center placed into the shade's socket, I'm guessing at which marked point represents that cap position — possibly the small circle around (15.4,18.7) with radius 2.5, though it's unclear if that's actually the electrode tip or the cap itself.

That small circle at (15.4, 18.7) with radius 2.5 could be a screw-point hole rather than the main screw cap anchor itself.

I'll settle on (15.4, 18.7) as the bulb's screw cap anchor, matching it with the shade's lug hole circle at (168.6, 175.3) with radius 3.47. For the socket at the narrow end of the cone, I'm considering placing it around (225-226, 111) as the center of the right opening where the bulb cap would sit.

Checking proportions, the bulb's full extent fits comfortably within the shade cone's length, so the sizing works out fine. Now I need to work out the overall lamp geometry: how the head plate connects to the shade lug, how the upper arm attaches to the head plate, and the shade's orientation so the bulb points outward through its mouth.

I'm tracing the lower arm's pivot holes and how its bottom end should attach to the L-bracket's upright pin, but I need to find where that pin hole actually is in the L-bracket's path data before I can place it correctly.

Checking the other colored paths, I'm spotting two small blob shapes: one around (94,45) near the top-right of the upright, possibly a pin hole, and another around (27,75) near the foot of the bracket. These look like the two pin-ish features I should account for in the L bracket's geometry.

Still tracing shape coordinates...

Tracing the outer boundary coordinates more carefully, I see one limb angling from the lower-left foot diagonally up to the right past (100,60), suggesting the two arms meet at a sharper angle than a simple right-angle L, more like a diagonal brace shape.

I'm tracing the inner cutout boundary of the triangular frame, including the flat foot section at the bottom of the shape around y=99.

I'm trying to figure out which limb of the triangle is the horizontal foot versus the slanted upright, since neither diagonal edge seems to form a clean right angle—maybe the bottom isn't actually flat and I need to reconsider the shape's orientation entirely.

Looking at the overall vertex layout, it seems like this is a triangular bracket plate rather than a cleanly-aligned L shape, so I need to identify which edge actually functions as the flat "foot" that sits on the base's top edge, since the rotation stored is arbitrary.

Let me try viewing it as a V-shape instead, with the apex at the bottom-left point and two limbs extending up to the other corners, and I'm calculating the angle between those two limb vectors.

I'm trying to figure out which ring hole the lower arm's bottom pivot connects to on the L bracket — comparing the (27,75) ring near the apex versus the (94,45) ring near the triangle's right vertex, since the lower arm leans upward from the base toward the upper-left.

I'm checking whether the two limbs actually meet at a right angle to confirm this is a true L-shape, measuring the tilt of each segment relative to horizontal and vertical to see if the geometry matches, since the stem and foot angles don't seem to line up as expected.

Tracing the rest of the right limb outward and back to the inner edge, I'm seeing this forms a thick chevron or "V" shape — left limb descending from the top apex, right limb rising back up, with an inner boundary cutting through the middle of the band.

I'm trying to figure out which limb forms the "foot" versus the upright of the L-shape, but the angle between the candidate edges comes out to roughly 50° rather than 90°, which doesn't match a clean L bracket. I'm wondering if I should step back and consider whether this puzzle has a canonical shape definition I'm missing rather than trying to reverse-engineer it purely from coordinates.

So the foot's bottom is roughly horizontal with rounding in local coordinates, meaning the bracket stands upright with one limb leaning left toward (40,5) and the other leaning right toward (119,45).

This isn't a typical L bracket—it's more like a triangular shape standing on a narrow apex, with a steep left limb and a shallower right limb. Maybe the upright is actually the steep left limb going from the foot up to the top point, and the shallow right limb represents something else entirely.

Looking at the pin locations, ring A near the bottom of the steep limb could be where the lower arm pivots, while ring B sits further up on the right limb near the top—this suggests the lower arm attaches low on the bracket and extends upward toward the elbow joint connecting to the upper arm and lamp head.

Rather than guessing orientation, I should work out distances: the lower arm spans about 326.3 units between its holes, and the upper arm spans roughly 339.8. For the elbow plate, I'm checking the distance between its top-right hole and bottom hole, which comes out to about 66.4 units, to see which arm pieces could plausibly connect there.

Now I'm looking at the head plate's hole positions and radii, and comparing them to the two end holes of the upper arm piece to figure out which end attaches to the elbow and which attaches to the head, since both ends look geometrically similar and I need another way to distinguish them.

Hole A is likely one of those two coordinates. Thinking about the shade lug position relative to the socket piece — the head plate sits on top, with the shade hanging below it, cone opening facing down, narrow end to the right.

The shade axis runs roughly horizontal from the narrow end to the wide mouth on the left, so the lug sitting below that axis suggests it's positioned on the shade's underside, connecting upward to the head plate above it.

But for a desk lamp, the shade's mouth needs to point down toward the desk, not left — so I need to rotate the shade roughly 90 degrees from its stored orientation, which means figuring out where the lug ends up relative to the shade center after that rotation maps the leftward mouth direction to a downward one.

This isn't quite realistic but geometrically works. For the bulb, I need to figure out how it maps into the shade—its cap-to-globe axis should align with the shade's narrow-end-to-mouth axis, though there's enough freedom here that the grader likely just checks key landmark positions like the lug hole and cap location.

Beyond that, I realize each part—shade, bulb, head plate, elbow, upper arm, lower arm—has an implied correct orientation relative to the base that I need to infer, with an 8-degree tolerance. The chain of constraints starts from the fixed base: the L bracket's foot sits on the base top, the lower arm connects from the bracket's pin hole to the elbow's hole, and that hole-to-hole distance must match the known 326px separation, which in turn determines the elbow's position based on the lower arm's rotation.

Working forward, the elbow's remaining hole fixes the upper arm, which then fixes the head plate, which then fixes the shade's lug placement — but the shade's rotation about that lug still needs to match some intended "facing" direction within the allowed tolerance.

While hole positions constrain things, orientation still traces back to the reference solution's angles, so our arm chain needs to match that reference's up-right geometry, leaving freedom mainly in the base placement.

Now I'm working out the lower arm's geometry from its hole positions: the axis from bottom to top hole runs nearly vertical, tilted about 5.5° to the left, with the top hole sitting toward the upper-left.

I'm checking the elbow plate's three holes and how they connect to the upper arm, then computing the vector and length between the upper arm's two mounting holes to figure out its angle and span.

The third distance comes out around 67, so the three head holes form a roughly equilateral triangle, which makes it ambiguous which one corresponds to the shade's lug hole. I need to figure out the correct head plate hole by reasoning about how the shade should hang — the head plate's orientation must put the shade's mouth facing down, so I should check each candidate hole against that constraint.

Now I'm working through the overall lamp geometry: base at the bottom, an L-bracket on the base, the lower arm rising diagonally, an elbow joint, the upper arm extending out, and the head with the shade hanging down at the end. I'm chaining together the positions — base pin, lower arm top (326 units away), elbow pin offset by 66.4, then the upper arm hole 340 units further — building up the full pose step by step with unknown but plausible angles, since I don't know exactly what the grader expects.

Maybe the "facing" check is about each part's orientation vector relative to the base within that tolerance—like the shade opening pointing down, the bulb aligned with the shade, and so on—meaning my pose would need to closely match whatever reference orientation was used originally, which is hard to guess exactly.

Actually, since each part's rotation in the kit is randomized, the reference orientation must just be whatever makes the pin-hole alignment consistent regardless of absolute angle, so I should focus on reconstructing relative transforms rather than assuming a "nice" canonical pose.

Arms likely count as "connecting rods" and can sit at any angle, but the elbow plate and head plate probably don't qualify, so their facing still needs to match within 8 degrees. The tricky part is that the head plate's correct orientation depends on which hole aligns with the shade lug, making its reference rotation harder to pin down.

The base stays exactly upright as stored, so its reference rotation is essentially 0 — but other parts seem to be stored at arbitrary rotations, so I need to figure out what counts as their proper reference orientation.

For the shade, I'm guessing its natural design orientation has the mouth pointing down, so I'll use that as the reference despite the arbitrary stored rotation. Then I'm thinking through the lower and upper arm orientations—the lower arm's stored tilt versus a plausible vertical design pose, and the upper arm's stored diagonal placement versus how it would naturally extend in the design.

Now I'm sketching out the actual lamp layout: positioning the base near the bottom of the canvas, figuring translate offsets so the base sits around y=680-722, and placing it horizontally around x=300-575 so the arms can extend rightward from an L-bracket near x~380.

I'm also working out the L bracket's rotation—its stored shape has a V-like form with a foot at roughly (20, 99.6) and limbs rising to (40,5) and (119,45), and I'm reasoning that keeping it at zero rotation makes it stand naturally on that foot as the upright support.

Maybe the stored geometry has the foot angled in its canonical orientation, so I'd need to rotate the bracket to get the foot's bottom edge flat against the base — but the grader likely checks this against the base's flat top edge specifically.

So I'm tracing the outer boundary coordinates near the bottom of the bracket to identify a straight segment of roughly 20-30 units that could serve as the flat foot.

Trying to identify which limbs form the L-shape's upright and foot by checking edge slopes and angles between segments, but none of the candidate pairs seem to form a clean right angle or straight line yet.

Actually tracing the coordinates again, I think the right limb forms a strip with a top edge running from (45,5) through (106,27) to (119,41), and a bottom edge running from (51,42) through (100,60) to (115,56) — so it's a parallel pair of boundaries forming a diagonal arm rather than a hollow triangle.

Trying to map which limb is the "upright" versus "foot" — the stem seems to be the vertical limb with a pin hole near its bottom ring, while the horizontal arm extending from the top likely holds the other pin, consistent with an L-bracket's upright-and-foot design.

Tracing the shape's orientation: the corner sits at top-left with the stem descending and the arm extending rightward, rather than the standard bottom-left corner configuration. I need to figure out the right rotation so the foot becomes horizontal at the bottom and the stem points upward from it.

Rotation preserves handedness, so I can't just rotate to match—maybe I should swap which segment I'm calling the foot versus the stem, trying the arm as the stem-direction-part instead and checking if that orientation works out correctly.

Checking the end cap angle against the stem direction, it's not quite perpendicular, so that geometric match is shaky. I'm reconsidering: maybe the stem (foot) runs from the corner down to the bottom point, while the upright is the shorter arm toward the other end, closer to typical lamp bracket proportions.

Looking at the grader's requirement that the foot's flat bottom edge rests anywhere along the base's top edge with the whole foot on the slab, I realize the foot must have a long flat outer face, and I'm checking which limb's outer edge — likely the one running roughly 82 units in length — could serve as that flat base.

So the stem forms a band roughly 20-25 units wide between these two nearly-parallel edges, with a bottom end cap closing it off. Now I'm tracing the arm similarly, looking at its outer and inner faces running toward point (119,45) to see if it forms a matching band shape.

Checking directions, the top and bottom faces of the arm are parallel at a 20° angle, giving a band width around 33 units — wider than the stem's. So this confirms an L-shape: a thicker arm extending right at about 20° downward from the corner, and a narrower stem extending down-left at roughly -20°, meeting at that corner point.

Taking the dot product between the arm direction and the stem direction gives nearly a right angle, about 94°, which confirms this is a true L-shape rather than the skewed one I'd estimated earlier. The corner sits near the top-left, with the stem running down about 95 units and the arm extending right about 85 units to roughly (119,45).

Now I'm trying to figure out which segment serves as the flat "foot" resting on the base — comparing the lengths and orientations of the arm's top/bottom edges versus the stem's outer face to see which one forms a long, flat bottom edge.

Testing rotations, I realize rotating by -20° to make the arm's bottom edge horizontal makes the stem point downward into the base instead of upward, which doesn't work. So I need to try a 180° rotation instead, checking whether that orientation puts the arm flat on the base while the stem rises vertically as expected for a standing L shape.

So rotating by 160° gives arm angle 180 and stem angle -86°, pointing up as desired. Now I need to work out where the foot's bottom edge lands after this rotation.

So after the rotation, the arm's original outer top face becomes the bottom face, which checks out with the stem rising from the corner. I'm now tracing where the stem ends up — it was positioned on the side near the bottom face originally, and after rotating it lands pointing upward, confirming the foot's orientation makes sense.

So the arm extends left from the corner, with the stem rising at the right end, forming an "⅃" shape, and the foot rests entirely on the slab. Now I need to figure out which pin hole belongs to the upright stem versus the arm — ring A near (27,75) seems to sit on the stem, while ring B at (94.4,45.5) sits on the arm, so I'm checking whether ring A is truly the upright's pin hole given its position near the stem's far end.

Working through the stem geometry: ring A at (27,75) falls about two-thirds down the stem toward its free end, which after rotation becomes the top — matching the expected "upright pin hole near top" position. Ring B on the arm sits closer to the arm's free end too, suggesting it's a separate fastener hole rather than the upright's pin, possibly for a base mount. Now I'm working out the L-bracket's local coordinate points, starting with pinpointing the exact corner location.

Solving the system gives s≈-15.13 and t≈-13.9, putting the intersection point around (32.7, 0.6), which seems off so I should double-check that corner calculation.

I'll approximate that sharp corner near (34,2) with a rounding radius of about 10. Rather than chase the exact corner, I think it's better to set up local coordinates for the foot and stem pieces and numerically compute the transform, starting with the arm top face line from (45.8,5.3) to (105.8,27.1) and its outward normal direction.

Checking the perpendicular options, the outward normal (away from the body, upward) comes out to (0.34,-0.94). After rotating by 160°, that normal's angle of -70° shifts to 90°, giving (0,1) — pointing straight down, which confirms this becomes the bottom face in the final orientation, letting me place the arm top face line at the correct y-coordinate in screen space.

I'm now setting up a translate+rotate(160°) transform and computing where a reference point on the arm's top face edge (the midpoint of that line segment) lands after rotation, applying the rotation matrix numerically to get its transformed coordinates for positioning in the SVG.

Checking the corner point near local (35,2), its image lands at roughly x' ≈ -33.6, confirming the junction location relative to the foot's span.

The bottom face stretches from this corner out to about x' ≈ -109, matching the free-end position, while the rounded transition sits between there and the top face's start. I'm now tracing the stem geometry by transforming ring A's local coordinates into image space.

That puts ring A roughly 14px below the stem's top end, which seems plausible. Checking the stem's position relative to the foot, it sits at x' around -51 to -53 while the corner is near -34, so the stem leans up-left from the corner at about 14° off vertical, consistent with the foot extending left from that same corner.

Checking the second point confirms both lie on x'≈-30.97, verifying the stem's outer face is vertical there. Now I'm working out the inner face position by plugging in a few more candidate points to see where they land.

Let me recompute the band boundaries at y=75: outer face lands around x≈6 and inner face around x≈39, giving a width of 33 centered near 22.5, which confirms ring A at x=27 sits close to the stem's middle. So the upright pin lands at x'=-51, y'=-61.

Now I need to work out the L bracket transform: translating by (X,Y) and rotating 160°, with Y set so the foot sits flush, and X picked so the foot's x-range (-109 to -45) lines up with the base. That puts ring A at X-51 horizontally and Y-71 vertically relative to the top point.

I'm also locating the lower arm's bottom hole (around local coordinates 52.2, 345.2) which attaches at ring A, with the top hole near (20.7, 20.5) near the elbow C. The arm runs upward from ring A to the elbow, pivoting on the same pin as the stem — I need to confirm the arm sits properly on that upright pin without interference.

Now I'm laying out the overall lamp within the canvas, choosing ring A's position and the lower arm's tilt angle to determine where the elbow lands, working out the reach of both arms (326 and 340 units) relative to the base width to keep the whole composition balanced.

Now I need to figure out the elbow plate's orientation, since C is its bottom hole at local coordinates (68.6, 86.9), and I still need to locate the other hole B on the right side of that plate.

I still need to fix the elbow orientation freely, then figure which upper arm hole is the shoulder end versus the head end. I'm now working out the shade geometry, estimating the narrow end center and the mouth opening center from the hole coordinates to position it correctly.

Locating the lug hole at (168.6,175.3) relative to the narrow end, I find it sits about 59px toward the mouth and 62px below the axis. Now I need to figure out the rotation angle that reorients the shade so its mouth faces downward on screen, since the axis currently points at roughly 179.2° and needs to end up at 90°.

The shade extends downward from the narrow end to the mouth, with the narrow end sitting at top like a neck. The lug sits on the right side of that narrow end, roughly 59 units below its center, suggesting the yoke attaches near the socket side rather than dead center on top.

Now I'm tracing the bulb's orientation: the cap should sit at the narrow end with the globe pointing down toward the mouth. Looking at the bulb's local coordinates, the cap tip sits near the top-left while the globe spans a wider region toward the bottom-right, giving me a rough center point for the globe to work with when mapping it onto the shade's axis.

Tracing back along the neck's axis from the junction point, I can estimate the cap center landing around (24,26), with the cap tip slightly beyond that toward (15,19).

Checking the projection confirms that the tip point (15.4, 18.7) lands precisely on the axis line passing through the junction, roughly 46 pixels away. That matches up neatly with the small circle marking the axis point at the cap tip — I'll treat this as the anchor point and continue tracing the bulb's axis from there toward the globe.

Now I need to rotate the bulb so its axis (currently pointing at about 39.3°) aligns with the shade's downward axis at 90°, meaning a rotation of roughly 50.7°. I'm setting up the transform as a translate-rotate-translate sequence anchored at the cap tip, making sure the bulb's globe ends up positioned correctly near the shade's mouth opening.

Working through the shade's own placement transform now, matching its lug point to the head's socket hole and computing where the narrow end lands after rotation by solving the vector math for the rotated offset.

I need to figure out the mouth opening width after rotation — the local perpendicular span of 9.5 to 222 becomes a horizontal span once rotated back into the actual coordinate frame.

That gives a mouth opening of roughly 213 px, much wider than the cone's narrow end around 80 px, confirming the shade's proportions. Now I'm tracing how the shade connects to the head plate through the lug hole and arm hole relationships.

Tracing the outline further, I'm mapping the three lobes with their holes, and following the body contour from the left-top arm around to the bottom lobe, trying to reconstruct the Y-shaped head plate geometry point by point.

Checking the side lengths confirms it's roughly equilateral, around 63-67 units each. Now I need to figure out which vertex hole corresponds to the arm connection versus the shade lug, given the arm comes in from the upper-left elbow direction.

Working through the geometry: the elbow sits near the top of the lower arm, and the upper arm connects it to the head's arm hole across a 340-unit span. I'm trying to place the shade below the head plate so its narrow end attaches near the head and its mouth hangs roughly 100-200 units above the base, keeping the bulb clear of the table surface.

Now I'm figuring out the head plate's orientation using its two holes — the main hole and the arm hole, 65 apart — and testing a roughly horizontal-rightward upper arm with the elbow offset right of the lower arm's top point to see if the resulting pose looks like a plausible desk lamp.

Working out the base translate so its local coordinates map to x 350–625, y 680–722, keeping rotation at zero for an upright stand. Now positioning the L-bracket foot relative to that same X reference point.

For the lower arm, I need it tilted 20° to the right from vertical, so I'm computing the local bottom-to-top vector's angle and finding the rotation offset needed to match that target direction, landing on roughly 25.5° rotation applied at the pin point (486, 608).

Now I'm computing where the top hole lands after that rotation, getting approximately (597.6, 301.3) as the new world position for point C, then moving on to work out the elbow transform using the local coordinates for C, B, and A.

For the elbow, I'm figuring out the direction from C to B (about -71.6°) and comparing it to the lower arm's segment direction (-70°) to decide how to orient the elbow plate so the arm bends naturally.

Checking the span fits the canvas, I estimate the lamp reaching from base around x=350 to shade around x=1100, which stays within the 1376 width. Trying a simpler horizontal upper arm (α=0) to keep the head positioned more centrally rather than stretching too far right.

I'm figuring out the head plate orientation — picking which hole pairs work well together, noting arm hole P1 at r2.5 matches the upper arm pins nicely, while P2 and P3 at r3.58 are close enough to the shade lug's r3.47 to be a reasonable match.

But checking the lower arm and elbow radii, the pin sizes don't line up consistently (lower arm 4.35 vs ring 5, elbow C 2.5 vs lower arm 4.35), so I'm realizing radius matching is too unreliable to use as the deciding factor — I need a geometric approach instead.

Looking at the head plate's hole positions in the stored frame, I'm trying to reason about which vertex sits at top versus bottom to figure out which hole should be the arm hole and which should be hole A, but without a clear reference orientation this is still ambiguous.

I'm trying to pin down a plausible physical configuration instead of relying on exact stored orientation data — maybe just assume the upper arm points horizontally to the right with the arm hole at the top-left vertex, and work out the head plate position from there.

Checking two possible hole candidates for where the shade attaches to the head plate, comparing the angles each would produce, and then working through how the shade's lug and narrow end position relative to the head plate depend on the unknown head rotation.

I'm checking whether the shade's narrow end overlaps with the upper arm near the head attachment point — tracing the coordinates shows the arm's end sits right at H while the shade's cone opening spans a region just above and to the side, so they seem to clear each other without colliding.

So the head plate should sit to the upper-right of the shade, with the arm coming in from the left toward the arm hole H. I'm testing Option 2, pairing P1 as H and P3 as the pivot, and trying to pick an angle so the arm sits horizontal with the elbow on the left side.

Checking the x-ranges, the shade's narrow top overlaps the head plate region, and the lug at Q sits just right of the cylinder's edge, below its bottom—placing it near the socket piece at the shade's lower-right corner, which seems geometrically sound overall.

Now I'm working out the arm's orientation: picking which local hole corresponds to the elbow versus the head determines the direction from B to H, though both choices give the same 340-length arm just mirrored, so I need to resolve that ambiguity by checking which configuration keeps the head plate roughly horizontal under the lamp.

I need to figure out which end of the arm connects to the elbow versus the head, so I'm computing the angles between the two end points to decide the orientation—checking whether E1 should map to the bottom (elbow) and E2 to the top (head), or vice versa, based on which direction matches the expected elbow angle.

For the head placement, I'm picking an arm angle of around -10° so the arm points rightward and slightly upward, then computing the head position from the elbow point using that rotation, followed by placing the shading and mouth relative to the head position. I still need to verify that this arm path doesn't visually cross or overlap the elbow joint.

I'm also reconsidering the head plate orientation, putting P1's arm hole top-left and P3's hole on the right, then working out the elbow angle γ so that point B lands near the desired position relative to C.

Now I'm computing the elbow's rotation angle by comparing the local C→B vector's direction to the target γ, confirming the segment length checks out, then setting up the transform for the elbow piece using the right translate/rotate/translate sequence.

For the upper arm, I'm solving the rotation ζ needed to make the E1→E2 segment horizontal when placed at B, then verifying H lands at the correct position by rotating the local vector and adding it to B.

Now moving to the head plate: arm hole H corresponds to point P1 at (36.5, 36.7) on the plate, and hole A corresponds to P3 at (100.6, 43.8). I need the head plate's rotation angle, computing the local vector from P1 to P3.

I'm continuing to work out the geometry: locating point Q as the rotated P3 position, then deriving the shade's narrow-end center N by offsetting from Q, and from there computing the mouth position and width bounds.

After rotation the cylinder neck spans y 220–316 around x=1002±40, and the cone expands from there down to the mouth at y=434 with half-width 107. Checking the lug hole's local coordinates relative to N, transforming by the rotation gives (61.2, 59.05), so the lug lands at (1063.5, 279.2), matching what I expected.

This lug sits outside the cylinder body (which spans x 962–1042), so it's actually anchored on the lower-right via the connecting socket piece—I'm working through the local coordinate ranges for that socket (x 152–185, y 153–193) and translating them through the same rotation to find where it lands on screen.

Working out the rotation gives a clean approximation: screen x ≈ local dy offset, screen y ≈ -local dx offset. Checking this against the lug's known position confirms it matches, so I can now apply this simplified mapping to locate the mouth at local x=5, which puts it at screen y = N_y + 221.

Applying the same mapping to the cylinder and socket pieces, I find the cylinder spans from N_y to N_y+96, and the socket sits at screen x from N_x+40 to N_x+80 with y from N_y+41 to N_y+74 — placing the lug hole correctly inside it on the right side of the shade's cylinder.

Now checking the head plate: it extends from H(999,279) to Q(1063,279), with the triangle dropping down to about (1028,336). Comparing this to the shade cylinder's bounds (x 962–1042, y 220–316), the two regions overlap — so the head plate is actually colliding with the shade geometrically, which is physically awkward even if the grader likely won't penalize it.

Let me try A = P2 with arm at P3, orienting the plate so its body extends away from the shade — toward the right/down-right of the lug, away from the cylinder region.

Testing A=P1 as the lug with P3 as the arm hole: the direction from P1 to P3 is about 6.3°, and the body centroid direction relative to that comes out to roughly -43.9°, so I'm checking whether this geometry fits the expected triangle configuration.

Let me parametrize by the plate's rotation angle ρ, computing the hole and arm positions as functions of ρ using the known vector lengths and directions, then check that the body sits away from the shade and the arm meets the upper arm horizontally at H.

Testing ρ=0 leads to the arm passing right through the lug region near Q, so I'd need a different orientation where H ends up as the top-right vertex to avoid that collision. Given this is turning into a complex geometric puzzle and the grader likely only checks hole positions rather than collisions, I'll shift focus to just getting the holes correct.

Let me check the alternative where the lug sits below the body, so the plate's body is above it—then I need to verify whether that body region overlaps the shade's narrow-end cylinder, checking the x and y ranges of both shapes against the offset Q position to see how much they intersect.

Maybe the head sits upper-right with the lug below-left, so I'm testing an orientation where P3→P2 points down-left at roughly 128.5° and checking the corresponding P3→P1 vector to see if the arm geometry still holds up.

That 135° option seems to risk collision since the arm likely arrives from that same left side. Trying 45° instead (down-right), giving ρ ≈ -83.5°, places the cylinder more centered near H but close to where the arm itself ends, which could still cause overlap issues near the top of the cylinder region.

Testing a 0° direction (straight right) still puts the arm's endpoint H within the cylinder's bounding box, so that fails too. I'm now setting up the general condition: for the lug direction angle giving offset (dx,dy) from H to Q, H stays clear of the cylinder only if dx<21, dx>101, dy>59, or dy<-37 — narrowing down which directions actually avoid the collision.

With Q at H+(0,62), that places it right-and-down from N, and I'm checking the socket piece's bounding box falls within N+40..80 horizontally and N+41..74 vertically, translating to H-21..H+19 and roughly H+44 in the shared coordinate frame.

Now I'm working out the head plate shape, rotating P1 relative to P3 so that P3-to-P2 points straight down, which fixes the rotation angle at -38.5°, and that gives me P1's position at roughly H+(-55, 34) — forming a triangle with H at top-right, P1 at left-middle, and Q at the bottom, sitting left of the shade cylinder's footprint.

I notice this placement overlaps with the shade region, but I'm deciding not to over-engineer against that collision since the grader likely focuses on explicitly described constraints like orientation rather than aesthetic overlaps, so I'll prioritize matching the plate's rotational relationships over avoiding this geometric overlap.

My best guess is the puzzle was generated by taking a canonical lamp with each part at a defined working transform, then randomly rotating each part for the question, so the facing constraints just mean matching back to those original canonical orientations.

Since arm angle is free, head plate orientation relative to base becomes ambiguous, so maybe the grader's canonical reference simply uses each part's stored rest orientation rather than some globally consistent assembled pose — meaning parts like the elbow and head plate might just need to stay at rotation zero relative to their own default.

The grader probably checks each non-turning part's angle against the reference within a tolerance, so the holes and base orientation must fully pin down head plate and shade placement for this to be solvable—but since the arm angle is free to rotate, the head plate's orientation seems ambiguous unless "facing" is judged independently of the arm's swing.

Without certainty, I'll aim for a natural desk-lamp pose: head plate oriented so the shade hangs below it with the arm attaching from above, like a classic Anglepoise yoke setup.

I'm trying different hole-pair assignments for H and Q, checking which pairs give roughly the right ~62 vertical separation, then computing where the third hole would fall relative to that arm-lug axis using the angle offsets between pairs.

No overlap there with a ~6px gap, but the socket piece does overlap the plate's body near the lug—which makes sense since that's where they're joined together. This all checks out physically: arm hole at top, lug at bottom, shade hanging left, socket attached at the lug. Now I need to figure out where the upper arm comes from above—tracing from elbow B down to H to determine the upper arm's position and length.

Actually checking the geometry, the arm at y≈279 with its width would clip the cylinder's top edge near x 899-979 since the cylinder starts at y=282 — too close. I need to angle the arm so it approaches H from the upper-left instead of straight horizontal, avoiding that overlap.

But the elbow position is constrained: B must sit within 66 units of the fixed joint C at (597.6, 301.3), so I can't just pick B freely from the angle — I need to find B on that circle around C that also gives a clean approach angle into H.

The arm grazes the rim at that angle, so I'm tilting it upward instead: setting δ=-15° gives H≈(972.5,166) and the narrow end N≈(911.5,169), which should clear the shade opening better.

Checking the trajectory though, the arm still dips to y≈182.5 near x=911, which falls inside the shade cylinder below the rim—still a collision. Trying δ=+15° instead, approaching from the upper-left, the arm sits at y≈325 near that x, which is also inside the shade region since the rim there sits around y=367.

Revisiting with H_y=342 and rim at 345, the arm's path through x=883..963 stays around y=306-327, clearing the rim by roughly 18 units even after accounting for arm thickness—that configuration works. So I'm settling on B=(644,254), δ=+15°, H=(972.5,342), verifying the elbow geometry checks out at length 66.3, then computing the lug position Q, the N point, and the resulting shade cylinder bounds and mouth opening from there.

Checking the arm clearance again at x=911 confirms a 10px margin above the rim, so the head plate geometry built from P1=H, P2=Q, and P3 offset from H should hold, along with the plate rotation matching the P1→P2 angle. I'm now working out the shade socket placement relative to the lug and starting to re-derive the upper arm's local-to-world transform using elbow and head endpoints.

Solving for the required rotation offset ζ, I find H lands at roughly B+(328.1, 89.0). I'm now setting up the elbow's own rotation so its C→B direction matches the desired -45° angle, factoring in how the lower arm approaches C from the pin below.

The geometry seems plausible enough even if the exact orientation isn't perfectly satisfied — I'll move forward and lock in final numbers, including shifting the whole assembly left by about 150 units to better center it within the current extent bounds.

So vertical span is 230–722, with canvas height 768 giving center 476 versus canvas center 384 — meaning I should shift the whole thing up by about 90 units to center it properly.

Deciding to keep things simple and skip the shift, I'll now pin down the base's exact coordinates — the top edge sits at local y≈5.2, which translates to screen y=680 after applying the translate transform.

Working through the L bracket's position, I'm centering the foot over the base to compute X_L, then using that to derive the ring and elbow positions along the lower arm — settling on X_L=537 gives a cleaner alignment with ring A near x=486.

Verifying the rotation math for ring A's local coordinates under a 160° rotation to confirm it lands at approximately (486, 608), and double-checking the sign convention of SVG's rotation matrix against the computed values.

Now I'm pinning down the lower arm's hole centers more precisely by averaging the arc endpoint coordinates from the path data for the bottom circle.

Now I'm computing the lower arm's vector and angle, finding it points at roughly -95.54° while the desired screen direction is -70°, giving a rotation of 25.54° for that segment before I move on to building its transform.

Applying this rotation to find the elbow's top endpoint, I get C at approximately (597.37, 301.45), which closes out the lower arm calculation. Now I'm shifting to refine the elbow hole centers, locating the small circle points for the bottom hole.

That gives (24.02, 38.09) for the left circle center. Computing the vector from center C to B: (20.85, -63.01), with length 66.37 and angle roughly -71.7° using atan2.

To achieve a desired γ of -45°, I need ψ_e = 26.7°, so I'm setting up the elbow transform as a translate-rotate-translate sequence, then recomputing B's position using rotation matrix components (cos=0.8933, sin=0.4494), arriving at B = (644.31, 254.53). Now I'm moving to refine the upper arm circle centers.

Averaging the marker point coordinates gives E1 = (20.52, 20.66) and E2 = (328.92, 164.63), so the vector E1→E2 has length 340.4 and angle 25.02°. With B=E1 as the elbow end and H=E2 as the head end, I'm now working out the desired δ angle for this segment.

Setting the target angle to 15° means a rotation offset ζ = -10.02°, which I apply via a translate-rotate-translate transform to compute the new head position H ≈ (973.05, 342.66). Now I need to double-check that the upper arm's end circle extends slightly past E2 before moving on to refining the head plate's hole coordinates, starting with the arm hole P1.

Now I'm averaging the circle marker coordinates to get the centers of P1, P2, and P3 on the head plate, getting roughly P1=(36.76,36.90), P2=(58.36,96.74), and P3=(100.12,43.34), then starting to compute the distance between P1 and P2.

The length from P1 to P2 comes out to about 63.62 units at an angle of 70.2°, so the needed head rotation would be around 19.8° to vertically align H with Q. I'm questioning whether straight vertical alignment is actually the right approach here, and I'm now recomputing the lug hole center using refined coordinates, averaging to around (168.55, 176).

Next I'm trying to pin down the narrow end center by examining the rim points on the right side of the cylinder, looking for the top and bottom edges of the opening to estimate its center around (227.6, 108.6), though the exact point selection is still uncertain.

The cylinder bottom curves into around (218,153), so the rim spans roughly y 76 to 141, putting its center near y≈108.5 rather than the 113 I used earlier.

Checking the left mouth endpoints gives a center around (12.3,116.1), and comparing to the right opening center suggests the axis isn't perfectly horizontal but tilted slightly, around -2°.

I'm recomputing the lug's position relative to the narrow-end center, and I'm getting numbers that differ by a few pixels from my earlier estimate, so I need to pin down which measurement for the narrow-end center is actually more trustworthy.

Taking the cylinder's narrow end centered around (130,112) and the mouth rim centered at (227,110), I'm estimating the axis running nearly horizontal, from mouth to narrow end at roughly -1.63°, meaning narrow-to-mouth is about 178.37°. Given the tight 6px tolerance required, I need to pin down these edge coordinates more precisely before finalizing the angle.

Verifying the mouth direction image confirms it points downward as intended, so the transformation checks out. Now I need to work out the head placement next.

Good, the transform checks out for N. Now I'm refining the bulb's anchor point by averaging four nearby coordinate points, landing on roughly (15.36, 18.85), and starting to work out the bulb's axis direction from that anchor toward the globe, estimated around 39.3°.

Let me verify this axis passes through the correct junction point using the perpendicular bisector between two reference points — the cross product check confirms the anchor sits almost exactly on that line, so the 39.3° angle holds. Now I want to double-check whether this same axis also runs through the globe's center.

Checking more points' perpendicular offsets from the axis to map out the globe's actual boundary shape, and the values seem inconsistent, suggesting the globe isn't a simple circle in this projection.

I'll accept this and move to the bulb transform: rotating it 50.7° so its axis aligns with the shade's narrow-to-mouth direction, with the anchor mapping to point N and the cap at the narrow end so the globe extends downward correctly.

Now I'm recalculating the head transform precisely, recomputing H as the rotated offset from B using the refined angle and upper arm endpoint E2 to get the correct translation point.

With H confirmed at (973.02, 342.64), I'm deriving the lug point Q by offsetting downward, then backing out N by subtracting the head-to-neck offset, landing N near (908.7, 345.9) to verify against the shade mouth center.

Working out the other mouth corner gives (1015.1, 559.8), so the mouth spans roughly x 802–1015, which checks out.

Now I'm checking the shade's rim position relative to the head and arm — tracing the arm's line from B to H to find its y-coordinate near the rim and estimating the arm's width to see if it clears the shade.

Then I work out the head plate's geometry by rotating point P3 relative to P1 and translating it against H, locating the plate's extent and the lug position, and comparing that against the shade's socket dimensions near the rim.

Computing the socket's rotated bounding box now: it works out to roughly x 950–990, y 388–421, and confirms lug (973,406) falls within it.

Checking the plate body—triangle with vertices near (973,343), (1030,370), (973,406)—and confirming P1 connects correctly to arm endpoint H. Now verifying the head plate's stored rotation angle around 19.8 degrees.

Moving to the L bracket's stem geometry: it spans x from about 475 to 506, running from y=680 up to y≈583, and ring A at (486,608) falls nicely within that stem range, confirming the connection is valid.

The lower arm's bottom pivots at ring A and angles up-right at 20°, which means it crosses over the stem's right edge near y≈583-600 — this overlap is acceptable since the arm is pin-mounted and rotates in front of the stem's face.

Checking the L bracket's stem rise: the transformed top end lands around (484, 583) with the stem spanning x≈475-506, center near 490 — matching the earlier calculation.

Now I'm working out the elbow plate's position at C (597,301) with B at (644,254), computing the transformed location of the elbow's left hole A relative to the local coordinate frame.

After rotating by 26.7°, A lands at roughly (579.4, 237.8), sitting above B as expected, which confirms the upper arm starts at B (644, 254.5) heading right-down at 15°. The overall lamp shape checks out: base at bottom-left-center, L rising up, lower arm angling up-right into the elbow, then the upper arm extending right-down toward the head and shade.

I'm verifying the upper arm's transform — confirming that local points E1 and E2 correctly map onto B and H, and that the bottom end hole of the upper arm aligns with the elbow plate's right hole as intended.

Now I'm second-guessing which hole is which on the head plate — I'd assigned the arm hole to P1 and hole A to P2, but I'm not fully certain that matches the grader's labeling convention. It's possible "hole A" actually refers to whichever circle appears first in the path's drawing order rather than by logical position, so I'm going back through the head plate's path definition to check the sequence the circles were drawn in.

The arm hole is likely at the apex with the lug hole at the lower position, equidistant — looking at the head plate's lobe structure, P2 and P3 both sit at r3.58 on bottom and right lobes respectively, leaving P1 as the remaining vertex.

Checking radius matches: P1's r2.5 lines up with the arm's own r2.5 holes at both ends, which strongly suggests the head's arm hole is P1, and the elbow's bottom hole C also at r2.5 matches the lower arm's top hole. But elbow's right hole at r4.11 doesn't match the upper arm's r2.5, and the lug's r3.47 only loosely corresponds to the head's r3.58 — so I'm still working through which pairings are genuine matches versus coincidences.

Since P2 and P3 both sit near r3.58 and have similar distances from P1 (63.6 vs 64.5), I need to pick between them for the lug position by working out the rotation geometry — testing the P3 configuration by rotating the plate so P1→P3 becomes vertical, then calculating where P2 would land relative to H under that rotation.

Checking that layout, P2 ends up to the left-down of H, right where the shade cylinder would be, causing a collision — whereas making P2 the lug instead pushes the free vertex P3 to the right-down, away from the shade. That physical reasoning favors P2 as the lug, since designers would want the unused hole clear of the shade geometry.

For the arm orientation, I don't think it matters which end sits at the elbow since both ends look symmetric, so I'll keep it consistent and move on to checking the lower arm and the L-bracket's upright pin against ring A versus ring B.

Confirming: after rotation the stem is vertical, so ring A sits on it correctly as the upright pin, while ring B belongs to the foot — consistent with the arm being horizontal and flush against the base. Now I'm checking the foot's bottom face geometry to make sure it still lies flat.

The base stays upright at rotation 0 since it's within tolerance. Now I'm locking in the transforms: the base at (345,675), the L-bracket at (537,669.3) rotated 160 degrees, and starting the lower arm transform at (485.98,608.05)...

Writing transform chains...

Confirming the lower arm's C matches elbow C correctly, then moving to check the head transform, verifying P1 maps to H and starting to verify P2 using the rotation formula.

Refining the angle estimate to 19.9° using linear interpolation between known tangent values, then recomputing the rotated positions for P2 and P3 with this adjusted rotation.

Setting up the shade transform with the computed center point and rotation angle, then double-checking φ by recalculating the mouth center from its local endpoints and the vector from N to that center—confirming φ ≈ -88.35°.

Moving to the bulb, I compute its screen position by applying the rotation offset to get N at (908.63, 345.89), then derive the bulb's rotation angle ψ_b ≈ 50.7° from the anchor-to-globe direction vector. I pause to verify my assumption that the bulb's anchor point is the screw cap circle sitting at the shade's narrow-end socket.

Confirming the shade transform correctly maps the lug point to Q, and checking all eight parts (base, bulb, elbow_plate, head_plate, l_bracket, lower_arm, shade, upper_arm) are each used once before assembling the full SVG markup. Writing SVG code...

Good, the math checks out. Now verifying the shade's mouth position relative to the bulb and base placement to make sure everything lines up visually.

That looks clear of the elbow plate too. I'm reasonably confident in the geometry now, so I'll finalize the SVG with a brief note on my key assumptions.


````

## Answer

````text
I placed the parts by matching their hole positions, with the L bracket's foot on the base and the shade mouth pointing down. I computed the transforms by hand from the drawings and did not render the result, so the hole positions are estimates. Two choices were judgement calls: which head-plate hole takes the lug (I chose the bottom one) and which bracket hole is the upright pin (the one on the upright).

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1376 768">
  <use href="#kit-base" transform="translate(345 675)"/>
  <use href="#kit-l_bracket" transform="translate(537 669.3) rotate(160)"/>
  <use href="#kit-lower_arm" transform="translate(485.98 608.05) rotate(25.54) translate(-52.19 -345.19)"/>
  <use href="#kit-elbow_plate" transform="translate(597.37 301.45) rotate(26.7) translate(-68.64 -86.89)"/>
  <use href="#kit-upper_arm" transform="translate(644.31 254.53) rotate(-10.02) translate(-20.52 -20.66)"/>
  <use href="#kit-head_plate" transform="translate(973.02 342.64) rotate(19.9) translate(-36.76 -36.9)"/>
  <use href="#kit-shade" transform="translate(972.99 406.26) rotate(-88.35) translate(-168.55 -176.12)"/>
  <use href="#kit-bulb" transform="translate(908.63 345.89) rotate(50.7) translate(-15.36 -18.85)"/>
</svg>
```
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
