# B · desk_lamp · claude-haiku-5-5 · trial 3

- Result: **FAIL**, score 0.33, tags: fail, wrong connection (far off), failed:anyhole, failed:joint, failed:online, failed:orient
- Model version: `claude-haiku-5-5`, response id: `msg_vrtx_011CgrVRAcfET6fPK9RjSshS`
- Started 2026-11-08T20:31:35-0500, finished 2026-11-08T20:36:11-0500, 276.2 s, attempts 1
- Tokens: input 25,539, output 58,672 (thinking not reported separately by this provider)
- Settings: `{"provider": "anthropic", "route": "vertex", "max_tokens": 128000, "thinking": {"type": "adaptive", "display": "summarized"}, "output_config": {"effort": "high"}}`, prompt sha256 `f81a16ea17aa27fecb8df1abae6e081d3427d66fe40127ae72760a3cc73257f9`

## Failed checks

- Lower arm: its bottom end hole on the l bracket's upright pin hole (within 6 px): error 468.62 (tolerance 6)
- Bulb: its screw cap on the shade's socket at narrow end of cone (within 6 px): error 175.05 (tolerance 6)
- Lower arm: its top end hole on one of the elbow plate's three holes (within 6 px): error 325.23 (tolerance 6)
- Upper arm: its bottom end hole on one of the elbow plate's three holes (within 6 px): error 324.55 (tolerance 6)
- L bracket: the bottom edge of its foot stands on the base's flat top edge, anywhere along it with the whole foot on the slab (within 6 px): error 606.47 (tolerance 6)
- L bracket faces the way it does on the working object (within 8 deg): error 145.8 (tolerance 8.0)

## Thinking summary (as returned by the provider)

````text
I'm examining the parts to figure out how this desk lamp assembles, starting with p01 which looks like a long bent arm with rounded pivot-hole ends that I need to trace the outline of.

Now I'm looking at p02, a curved piece with a hole near one end — possibly the lamp shade or head component, trying to trace its curved outline through the coordinate path to understand its shape.

Tracing the inner rim coordinates, the open edge of the shade seems to run diagonally from around (172,121) down to (119,156), while the small hole at (15,18) sits separately in the tab near the narrow end — likely a pin or hinge point where the shade attaches to the lamp arm.

Looking at p03, it reads like a tall bracket piece (roughly 225 by 222 units) with a hole near (167,174) — possibly a pivot yoke connecting the shade to the arm. Then p04 looks like a flat elongated base plate (about 275 by 42 units) with a rounded hole near one end at (253,27).

Checking the base assumption again: p04's hinge hole at (253,27) is likely where the first arm attaches, with the plate resting flat on the ground along its bottom edge. Moving on to p05, it appears to be a long link piece (about 326 units) with pin holes at both ends, similar in function to p01 but longer — and p06 seems to be another arm-like link with a hole partway along its length.

p08 looks like a triangular bracket shape spanning roughly (105,20) to (8,40) to (60,100), with three holes at (89,24), (69,86), and (24,38).

Now I'm trying to piece together what the overall object is — likely a desk lamp with a jointed arm: a base with a hinge, lower and upper arm links connected by elbow and wrist joints, then a head yoke holding the shade, possibly with a counterweight or spring tension. I'm checking each part's pin hole positions to figure out how they connect, starting with the small circles near the ends of part p01.

I'm now measuring the hole-to-hole distances on parts p01 and p05 using their circle centers — p01's holes are about 340 units apart, while p05's are about 326 units apart, both with similar hole radii.

For p07, I'm computing centers for three circles by averaging their boundary points, finding them clustered around (58.4,96.2), (100.6,43.3), and (36.5,36.9) with slightly varying radii.

This looks like a triangular bent link with three holes — possibly a gusset connecting a lower arm, upper arm, and spring mount. I'm now moving to p08 and extracting its hole centers from the circle boundary points.

This triangular shape with three holes near each vertex might be a lamp head yoke, with one pivot connecting to the upper arm, another to the shade tilt, and a third possibly for a spring or counterweight. I'm now comparing this to p07, which also looks like a triangular bracket with three holes.

Checking the side lengths of both triangles, they're both roughly equilateral with sides near 65 units, though the hole diameters differ between the two parts—so they're similar triangular link shapes but distinguishable by hole sizing.

Thinking about the overall lamp assembly, this looks like a spring-counterbalanced desk lamp: a base, lower and upper arms, a head yoke/bracket, a shade, and a spring. I'm trying to map the individual parts to these roles, noting that one has a single bracket hole that could be a pivot point.

That lobe with the hole looks like a pivot point for the arm, so p03 might actually be a clamp or bracket piece. Meanwhile p04 has a flat bottom edge and a hole at its end, which fits the idea of an upright base plate that stands on the ground—so p04 is likely the base, leaving me to figure out whether p03 serves as the clamp or some kind of counterweight.

I'm working through a typical jointed desk lamp's parts: base, two arm links, a shade, a yoke bracket, and possibly tension brackets or triangular supports. Looking at the hole sizes and shapes, p01 and p05 seem like the long arm links, p02 is probably the shade, and p07/p08 look like triangular pieces, while p06 has a distinctive bent bar shape with rounded ends at both sides that I'm still trying to place.

Now I'm trying to map out where the base's pivot point connects to the rest of the structure, checking which link attaches at that hinge position near the base's right edge.

I'm comparing hole radii across pieces to find matches — p04's hole and p08's hole both measure about 3.82, suggesting p08 might be the bracket connecting at that base joint, even though its matching hole sits at one of its triangular tips.

Continuing through the parts list, I'm checking hole radii and computed centre coordinates for p02 through p04, cross-referencing the arc points against candidate pin positions.

Then for p05 I'm noting two larger holes (r4.35) at separate locations, while p06 appears to have no holes at all — its rounded ends might just be solid curved terminations rather than pin holes, so I'm tracing its outline points to confirm that.

Now I'm cataloging p07's three holes (r2.5, r3.58, r3.58) and p08's three holes (r4.11, r2.5, r3.82), then trying to match hole radii across pieces to the pin radii I found earlier — p01/p02/p07/p08 share r2.5 pins, p07's larger holes roughly match p03's hole, and p04's r3.82 pin lines up with p08's third hole.

I'm also reconsidering what object this actually is — likely an Anglepoise-style lamp with a base hinge, lower and upper arm links pivoting at an elbow and spring-loaded wrist, a yoke connecting to the head and shade, plus a counterbalance spring. I'm wondering if p06 could be the spring or a bulb holder, and noting that p07 and p08 each form near-equilateral triangular brackets with three holes, possibly tension or clamp brackets in this assembly.

I'm shifting to working out actual placement coordinates so the holes line up into a coherent lamp shape: positioning the base plate upright near the bottom of the canvas, then figuring out how the arm chain extends upward and to the side toward where the shade should sit.

Looking more closely, the p04 plate spans x 18 to 265 at its top edge, with a hole at (253,27), and there's a lip near x=276 that looks like it could be a hinge housing.

Comparing arm sizes across pieces: p01's center distance is 340.3, p05's is 326.2, while p07 and p08 have triangular sides around 65-66. p03 seems to be a bent arm or yoke-like piece, with a single hole near (167.5,175.4) and a quadrilateral body plus a second connected segment extending further out.

Looking more closely at p03, it seems like a bent plate made of a long flat blade section and a separate lobe with the hole, possibly forming part of a lamp head or housing rather than a simple arm, since p02 appears to be the curved shade already.

Reconsidering, maybe p05 is a long tapered link arm with pivots at each end and a foot-like lobe near the bottom, while p01 is another 340-length arm with pivot holes at both ends too — suggesting both p01 and p05 function as structural links in the assembly.

Pairing these as lower and upper arms seems plausible given their lengths are close to typical Anglepoise proportions. The remaining pieces — p02, p03, p06, p07, p08 — likely form the head/yoke, shade, and spring-bracket. I'm trying to match hinge radii across parts to figure out connections, but none of the arm end-holes match the base hinge's radius exactly, which makes me suspect the hole radii might just be incidental rather than meaningful for determining the assembly chain — the grader probably only cares about hole centers.

I need to work out orientation: the base hinge sits near the right end of the base plate, so the arm likely rises from there, with the lamp head projecting outward over the desk. I'm placing the shade's pivot hole near its apex as the connection point to the yoke, and considering whether the remaining triangular pieces act as the bracket linking the upper arm to the shade.

I'm comparing hole radii across all pieces to spot matching pivot pairs rather than relying on geometry alone, since several holes cluster around similar radii (~2.5, ~3.5-3.6, ~3.8, ~4.1). This suggests grouping p01, p02, p07, and p08 holes as one matching family, and p03/p04/p05/p07/p08 as others, though I should be cautious about over-relying on radius matching versus just working out link lengths directly from a physically plausible Anglepoise-style chain starting at the base hinge.

I'm now questioning whether p05's foot lobe serves as the base pivot bracket, and trying to reason out which of the 8 parts fills roles like lower arm, upper arm, yoke, shade, and possibly a spring or elbow bracket, since the connections need to mirror a real lamp-like assembly.

I'm trying to match hole distances across parts to figure out which pieces connect — p01's two holes are about 340 apart, p05's about 326 apart, and I'm now estimating the rounded end positions on p06 to see if its geometry lines up with any of the others.

Now I'm checking the inner boundary points of the rounded end, tracing coordinates like (24.87,96.2), (29.3,91.9), and (48.2,40.1) to see if they fit the same arc geometry.

Tracing the outline further, the top edge runs from the right point up and leftward through several coordinates toward the upper-left corner before continuing down.

Tracing more of the outline coordinates, continuing from the right end along the top edge then down to a lower-left point around (6,74.1).

Then the path curves along the bottom edge rightward and up to about (51.1,42.4), before another branch forms a separate loop near the right side closing back near (119.2,40.8) — overall shaping into a bent V-like silhouette.

Actually, looking more closely, this resembles a bell-crank or boomerang shape: two arms meeting at a corner near the top-left, one arm running down to the bottom-left lobe and the other extending rightward along the bottom edge toward the right-side closure.

That fill region near coordinates (39,18) to (17,78) looks like decorative shading rather than structural geometry, so I think the actual body boundary is defined elsewhere, with the cutout between the arms traced by a separate path near (112,54) and (51,39).

Stepping back, this is likely a generated desk lamp assembly: a base, lower and upper arm links, a triangular head yoke, and a shade, each built from a parametric template with pin holes connecting them.

Given the complexity, I'm trying a more systematic approach: extracting each part's hole positions and radii, computing distances between connection points, and matching parts whose hole spacing and radii correspond to plausible pivot joints.

I'm trying to pin down the right end lobe's center by triangulating these scattered coordinate points, estimating it lands around (115.5,47) with roughly a 4-unit radius.

Stepping back, this is too detailed—let me think about the overall object type instead. Given the typical "jointed arm desk lamp" structure (base with hinge, lower arm, upper arm, head/shade with yoke, spring), the triangle-holed piece could be an elbow bracket joining three pivots: one to the base arm, one to the upper arm, and one to the spring.

Looking at the shade shape p02, its coordinates trace out a cone or dome-like form opening toward the lower right, with the apex at the upper-left where a tab holds a mounting hole—consistent with a lamp shade's inner cavity and highlight bands.

Tracing the outline further, the shell wraps around the open shade region, and I notice the top-left lobe stretching from around (5,21) to (40,5) is where the mounting hole sits — so the shade's narrow end tapers into that lobe.

This suggests the shade is a cone that opens toward the lower-right, with its pivot tab tucked at the upper-left back, and the rim spanning roughly from (172,121) to (120,156), putting the rim's center near (146,138) — which helps me figure out the cone's axis direction for positioning the bulb inside.

Now shifting to p03, I'm trying to piece together its shape: a flat plate-like blade on the left running diagonally, and a more complex piece on the right with a hole at (167,175) connected by an irregular outline forming an arm. It's not matching the base piece (that's p04), so I'm wondering if p03 might instead be some kind of spring component.

I'm thinking about the arm's joint structure overall: a base-to-lower-arm pivot, a lower-to-upper elbow pivot, an upper-arm-to-yoke pivot, and a yoke-to-shade pivot, plus a spring connection, giving roughly five or six hinge points total. Counting holes across pieces — p04 has one, p05 has two, p01 has two, p02 has one, p03 likely one, p06 appears to have none, and p07 and p08 each have three — I get a total of thirteen holes across all parts.

Looking at p07 and p08 more closely, both form roughly equilateral triangles with side lengths around 65-67mm, which makes me wonder if they're matching brackets (perhaps a head yoke and a spring bracket) that connect to each other, possibly as part of a parallelogram linkage like in a classic Anglepoise lamp design. I'm also trying to figure out where p03's hole fits into the connection scheme, but I don't have enough distance data yet to place it confidently.

Trying to identify the parts more concretely: p05 looks like a lower arm link with a wide foot at the bottom and a narrower top, while p01 appears to be a similar two-pin link with lobes at both ends, likely the upper arm. I'm comparing hole radii across parts to figure out which pins fit which brackets — p04's hole matches p08's radius almost exactly, while p07 and p03 share a close radius too, suggesting these are the mating pivot points in the linkage.

I'm now trying to trace a chain from the base hinge through the lower arm pivot candidates, and thinking about how the yoke connects the arm's wrist end to the shade's pivot point S, possibly through p03 or the p07/p08 triangle pieces with their ~65 unit pivot spacing.

Checking p03's outline, its corners look sharp rather than rounded, so it probably isn't a yoke piece with rounded pivot ends — that rules it out as the connector between the shade and the arm, so I need to look at p06 next.

Maybe p06 functions as a tension spring instead, with rounded eyes at each end connecting the lower arm to the upper elbow — but its shape reads more like a bent bell crank with lobes at two corners, so I'm measuring the distance between those lobe centers to see if it matches a plausible pivot span. Alternatively p06 could just be a bell crank with three pivot points, one at the top corner.

Thinking through a desk-lamp chain of parts — base, lower arm, upper arm, head yoke, shade — and trying to assign each labeled piece to its likely role in that sequence, including where a spring component might fit in.

I'm now examining the hole positions and lobe shapes on p05 to figure out which end attaches to the base joint versus the upper arm, comparing the foot-shaped lobe near one hole against the pin-like lobe near the other.

Looking at p01's end lobes, both appear similarly shaped, which makes me think more carefully about the overall lamp geometry: the base hinge sits at the right side of the base plate, so the lower arm likely rises from there, with the upper arm extending outward and the head angling down toward the shade.

Without clearer certainty, I need to settle this by satisfying natural constraints: the base stays flat at bottom, the lower arm rises from the base hinge, and the shade's opening should face downward toward the work surface rather than up or sideways.

Looking at p05's geometry, I'm checking which endpoint sits near the base hinge versus which extends toward the shade—the arm runs nearly vertically between its two lobes, so I need to figure out which lobe anchors to the base.

I'm computing p01's direction vector too, roughly 25° from horizontal, then trying to work out a global layout: placing the base with minimal rotation, finding the hinge position relative to the base's bottom edge, and figuring out how the lower arm's length and angle would position it going up from that hinge point.

The base stays upright with rotation 0, as required. Now I'm working out the lamp arm geometry from the hinge point—comparing lower arm lengths between variants (326 vs 340) and thinking through how an Anglepoise-style base and arm would connect.

Without exact knowledge of the intended orientation, I should try to deduce the structure by matching distances between holes across parts, since the generator likely created consistent hole placements across the base, lower arm, upper arm, yoke, and shade that I can use to infer the correct chain of connections.

Actually p02 looks curved like a shade with a rim, while p03 is a bent plate with a single hole — that single hole near H3 suggests p03 could be the yoke tip rather than a counterweight.

I keep going back and forth on identifying p03, so let me shift focus to p06, which is more plausibly a spring bracket connecting the lower and upper arms where a tension spring would anchor.

Thinking through classic Anglepoise geometry, the elbow pivot joins lower and upper arms, with spring anchors at each arm's end and the head yoke attaching to the upper arm's tip. Given the difficulty pinning down exact parts, I'll settle on a plausible chain starting from the base through the lower arm.

Continuing to check distances: the lower arm measures 326 units and upper arm 340, running from elbow to wrist, with the yoke bridging to the shade through various pivot points whose exact coordinates I'm still trying to match up.

Checking the shade's orientation relative to pivot S — the opening faces down-right, consistent with a desk lamp head pointing downward, so that part checks out. But matching p07 and p08's hole distances (around 65-66 units each) to figure out which is the elbow bracket versus the yoke is proving inconclusive, so I need to try a different approach to the geometry.

I'm trying radius-matching as a heuristic for pairing holes to pins across the components — comparing values like 3.82, 4.35, 4.11, and 3.58 across base, p05, p08, p07, and p03 to see which holes plausibly share the same pin size, though several of these are close but not exact matches.

Grouping the ~2.5 radius holes together (p01, p02, p07 A, p08 B) gives an uneven count that doesn't cleanly pair up, so the radii likely include some noise rather than being perfectly consistent identifiers.

Let me try a different interpretation: maybe the object is a desk lamp with a base, lower arm, upper arm, and clamp bracket, where each link's holes sit at the lobe ends. Looking at p03's hole H3, it falls in the tab lobe region at the bottom end of the piece, which could help identify where it connects.

Tracing p03's two pieces more carefully, the first forms a long flat quadrilateral-like plate with a left edge around 214px, and the second piece looks like a wider fan-shaped top section — together they might form a blade or bracket shape, but I'm not yet confident on how they combine.

Wondering if p03 is actually a clamp jaw rather than a blade, which would mean p04 (the stated base) plays a different structural role, possibly as the stable upright part the clamp attaches to.

Given the time pressure, I should just commit to a reasoned assembly rather than chase perfect geometric certainty — trying to find a configuration where link ends align cleanly, like placing the yoke pivot at the upper arm end and connecting the shade mount there.

Since the grader checks every connection the real object has, I need to correctly guess what this thing actually is: likely a jointed desk lamp with base, lower arm, upper arm, head bracket, shade, some spring/counterweight, and possibly a separate bulb socket piece. I'm now weighing whether p03 could be that bulb holder or instead the yoke/head bracket itself, given its bent shape and single hole.

Testing whether p03's hole pairs with the shade's attachment point as a pivot, but then the yoke would need a second hole to connect to the upper arm, and it only has one — so maybe the upper arm attaches elsewhere. I'm counting up the holes across all parts and considering whether p06's rounded ends function as pin connectors without holes, which changes how the joints pair up.

Or maybe its one real hole is fixed via a rigid joint with another part, like a counterbalance spring cover attached to the upper arm, with the rest being a fixed, non-articulated connection.

Tracing the chain again: base with one hole connects to the lower arm, which connects to the upper arm, which connects to a yoke needing two holes, and finally the shade. The triangular parts with three holes each could be the yoke plus a spring bracket, which makes me think there's a spring linking two points in the mechanism.

I'm wondering whether p06's rounded lobes represent spring eyes, or whether this is really an Anglepoise-style lamp with a base, lower arm, upper arm, spring-case bracket, head yoke, and shade as the core pieces.

Maybe p07 and p08 are the two triangular three-hole brackets — one acting as the spring holder on the lower arm, the other as the head yoke — with p01/p05 as the two arms, p02 as the shade, and p03 possibly the spring itself. I'm trying to mentally reconstruct a consistent layout: base at bottom-left hinging into the lower arm, rising to an elbow, then the upper arm extending right from there.

Since the grader likely only checks pin coincidences, arm rotation angles are free, but there's probably still an implied canonical orientation—like the shade opening facing down toward the desk—that determines which pivot assignment counts as "real."

I'm trying to match hole radii across parts: the shade's pivot radius (2.5) could correspond to either p07's A hole or p08's B hole, so I need another distinguishing clue to resolve which part is actually the yoke.

Trying both yoke assignments for the 2.5 radius hole leads to mismatches with the upper arm's ends either way, so the radii are likely just distractors rather than meaningful constraints. I should focus instead on the actual geometric features — rounded end centers, pin holes, axle holes, bolt holes, hub centers — rather than chasing radius matches that don't resolve cleanly.

Given the uncertainty, I'm picturing this as a jointed desk lamp viewed from the side, with a base, lower arm, upper arm, triangular head yoke, shade, spring, spring anchor bracket, and some kind of counterweight or bulb-clamp piece. I'm reconsidering whether p03's two blades (one about 120x215, close to the shade's size) might actually belong to a base clamp or a counterweight assembly attached near the lower arm's rear end, rather than being part of the shade itself.

Without a fully certain identification, I'm leaning toward a pragmatic assembly: base, lower arm, upper arm, yoke, shade as the main chain, with p03, p06, and the remaining triangular piece serving as spring and counterweight components whose holes dictate how they attach to the arms. I want to check p01's geometry more closely to firm up this reasoning before committing.

Tracing its outline, p01 looks like a straight elongated bar roughly 20px wide, running from around (34,18)/(25,33) at one end to (320,151)/(310,165) at the other, with small curved tabs at both ends—so it reads as a simple link or arm segment rather than a bent bracket.

Now checking p05's shape, which seems similar but larger, with rounded lobes near its top and bottom ends.

p06 looks like a bent link, bell-crank shaped.

Now sorting the pieces by hole count: p01 and p05 are two-hole links, p02 and p03 have one hole, p06 has rounded ends but no holes, and p07/p08 are triangular plates with three holes each.

I'm trying to pin down p06's shape as a bell crank or spring bracket by estimating the center and radius of its rounded lobes from the outline coordinates, fitting a circle to the left lobe's edge points.

That approach isn't converging well, so I'm wondering if the lobe isn't truly circular and considering it might instead be a lamp-arm style bracket with irregular rounded ends — it might be better to step back and look at the overall shape rather than force an exact circle fit.

I'm guessing this is a desk-lamp generator producing eight parts: base, lower arm, upper arm, yoke bracket, shade, spring, and two more pieces like an elbow bracket and a spring anchor. Since scoring seems strict, I should propose a consistent joint structure connecting the base hinge to the lower arm's lower lobe, though I'm unsure yet which end that is.

Tracing possible connections: the lower arm's top end likely links to the upper arm at an elbow joint, the upper arm's other end connects to a yoke pivot, and the yoke's remaining holes connect to the shade and a spring bracket. I'm unsure where part p03 fits — possibly a spring anchor or counterweight — and I'm examining the triangle piece p08's hole positions for geometric clues about how everything links together.

Without more definitive evidence, I'll just commit to a plausible configuration based on the shapes and hole placements I've inferred so far.

Continuing the grouping, I'm checking whether the base-to-lower joint pairing (p04 H4 to p05's 4.35 end) actually matches up under this radius hypothesis.

The mismatches don't resolve cleanly, so the radii likely aren't meaningful pairing cues — probably just arbitrary. I'm shifting to thinking about this as an Anglepoise-style lamp instead, considering whether p06's rounded-end shape suggests it's a spring link or lever rather than something tied to those radius values.

Trying to lay out a plausible chain: base p04 hinges to lower arm p05, which elbows into upper arm p01, which connects to a head yoke p08, which holds the shade p02, with a spring component (p06, p07, or p03) providing counterbalance tension somewhere along the arms. Without more certainty, I'll settle on a reasoned-but-guessed assembly rather than trying to force the triangle piece p07 into an unlikely geometric role.

Working through actual coordinates now: placing the base at a translation so it sits in the lower-right of the scene, then computing the global position of its hinge point, and from there figuring out the lower arm's orientation by connecting its bottom hole to that hinge and measuring the tilt angle needed for its top hole to point upward and slightly left.

Continuing the upper arm outward and down, placing the wrist around (1006, 500), then figuring out the yoke position next.

Arms likely aren't flagged as "turning parts" since those are reserved for wheels, gears, cranks, and similar rotating mechanisms, so the lamp's linked arms probably need fixed orientation. Since both ends are pinned, the arm's facing is dictated by where those pins sit, meaning the grader likely checks that the pin positions line up correctly rather than the arm's angle directly.

Given the ambiguity, I'll accept the answer will be imperfect and just aim to build a valid kinematic chain with a sensible pose, shade facing down, and hope the grading tolerance accommodates reasonable choices.

I'm working out pin coordinates and orientations for the shade and yoke components, calculating the shade's opening direction from its body center to rim so it faces downward toward a desk surface.

I'm trying to match pin radii between parts to find valid connections — the shade's 2.5 radius pivot pairs nicely with yoke pin B on p08, though the upper arm's matching 2.5 pin creates ambiguity about which piece it should actually attach to, possibly p07 instead.

Since the radius matching feels inconclusive, I'll just settle on the simplest chain: base to lower arm, lower arm to upper arm at the elbow, upper arm to yoke at the wrist, and yoke to shade.

I'm noting that the lower arm only has two holes at its ends, so it can't connect to anything else besides the base and elbow joints — any other bracket pieces must attach elsewhere in the chain, not to the lower arm itself.

Maybe the elbow pin is actually a triple connection joining lower arm, upper arm, and p07 together, or perhaps p07 anchors at the base hinge alongside the lower arm. I'm also reconsidering whether p06's rounded ends serve as the actual spring attachment points, since rounded ends might represent connection centers rather than fixed pins.

I'm now trying to trace a plausible chain through the whole mechanism: lower arm pivoting at the base, connecting to the upper arm at the elbow, the upper arm meeting the head yoke at the wrist, the yoke holding the shade, and then figuring out how p06 and p07 link into this chain via their remaining holes to complete the spring-loaded parallelogram linkage.

I still need to find roles for p03, p06, and p07. For p03 with its single hole H3 and flat rigid body, I'm thinking it could attach to something else at that hole point.

For p06 with its rounded ends, it's likely a link or spring connecting two holes, and p07's three holes suggest it's a bracket piece. Since both arm pieces already have their holes occupied at elbow and wrist, p03 would need to pin to something else entirely -- maybe the yoke, p07/p08's holes, the shade's hole, or the base's hole.

Thinking through the yoke's three holes, I wonder if p07 connects to p06's end and to p03, forming a secondary linkage alongside the main lower arm, upper arm, and base — mimicking the classic Anglepoise parallelogram mechanism.

Maybe p06's third end connects to base H4, making it a triple joint there, though that feels forced. I'm not landing on certainty here, so I'll just go with the simplest guess and move forward with it.

Let me try working out actual coordinates: placing the base with H4 near (548, 680), then extending the lower arm at roughly a 70° angle upward to an elbow point around (438, 373), tilting the lamp slightly left of the base so the shade ends up on that side.

Continuing the wrist calculation gives a low head position near the desk, which works for the lamp pose. Now I'm positioning the yoke pin relative to the wrist, using its known joint distances to place the shade so its opening faces downward, orienting B beneath the pivot.

Computing the rim position gives (1010, 823), which overshoots the 768-pixel canvas height, so this arrangement won't fit. I need a more compact layout instead, with the base bottom around y=700 and shorter arms, rethinking how the shade sits near the top.

Since exact facing direction isn't verifiable, I'll just pick a plausible downward-ish orientation for the shade opening, roughly 60° below horizontal, and go with that as the final pose without overanalyzing further.

Computing the shade rim position, I find it extends off-canvas near y=809, which is too low given the 768px height — so I need to shift the whole shade upward to keep it within bounds.

I'm reconsidering the lamp's proportions with a smaller overall height: placing the base mid around y=679.5, with the lower arm rising to an elbow near y=383, then adjusting the upper arm angle so the wrist and shade stay comfortably above the desk level.

I keep juggling angle options for the elbow, wrist, and yoke without landing on a clean fit, so I'll stop overthinking the exact geometry and just commit to a concrete set of numbers, accepting the grader likely cares more about overall pose plausibility than perfect precision.

I still need to place the remaining parts, p03, p06, and p07, and figure out how they connect. Thinking it through, the spring bracket probably shares a pin with the elbow joint rather than attaching separately, since the lower arm only has two holes already in use — so a triple-pin connection at the elbow (lower arm, upper arm, and spring bracket together) seems like the most realistic design choice.

Working through a tentative chain: the base connects to the lower arm, the elbow joins the lower and upper arms along with bracket p07, the wrist connects the upper arm to yoke p08, which then links to the shade on one side and to spring p06 on the other, with p06 anchoring into p07, and p07 possibly connecting further to p03 as some kind of counterweight — though I'm not fully convinced that placement makes sense structurally.

I'm now trying to pin down actual coordinates: setting a base transform, then computing the elbow point by projecting a direction vector from the base hole at some angle and multiplying by the arm length to get its position.

I'll keep going the same way for the upper arm, picking a slight downward-right angle so it extends past the elbow toward the lamp head, computing that endpoint, and then starting to position the yoke piece relative to that endpoint.

For the yoke, I'm calculating its local pivot points and their vectors to figure out the proper rotation needed to orient it so the shade points in the right direction, then computing where the shade's rim center lands globally based on that orientation.

Setting B equal to S and checking the vector from W to B gives roughly (x-952, -11), so I'm computing that distance to constrain x.

Solving for the angle gives ψ ≈ -9.5°, placing B to the right of W at about (1017.7, 470), which puts the shade rim at (1106, 623) — comfortably within the canvas. I'm now checking how this angle relates to the yoke orientation.

This is getting too arbitrary—let me reconsider how the spring connects to p07, maybe linking p08's C point to p07's A point instead, since p07 has three holes to work with.

I'm not confident I can pin this down with certainty, but I need to commit to something consistent where the pins all align without wild overlaps. Let me settle on pinning p07 at the elbow joint using its hole and work out the remaining connections from there, accepting some mismatch in pin radii as acceptable for now.

So p03 hangs from p07's C point at a single pin, which works fine as a rigid body attachment. Now I'm working out the actual geometry — placing p07's hole A at the elbow point and figuring out its rotation so that B and C land in sensible positions, checking the spring distance from B to the yoke location.

But I realize p06's fixed end-to-end length constrains this: since p07's A-B distance is fixed at roughly 63.5 and p06 has its own fixed internal spacing, I can't freely choose p07's rotation — the distance from B to the yoke depends entirely on how p07 is oriented about E, so I need to solve for that angle rather than assume it.

With E fixed, p07's rotation is the one free parameter determining B's position, while p06 being rigid with both ends fixed forces the distance between B and C to equal exactly d6. So yoke C's orientation relative to W must be chosen so |B-C|=d6 is satisfied, leaving a one-parameter family of solutions to search over.

This is turning into a multi-loop overdetermined system where I don't actually know which yoke ends are true pins versus just rounded tips, so I can't pin down exact distances confidently. Given the uncertainty, I might need to settle for an approximate fit that satisfies the clearer connections while treating the spring attachment as flexible, accepting the risk that the grader could penalize this if the true structure differs.

That doesn't look like a clean circle either, so the corner radius isn't consistent enough to pin down precisely. Trying the other end's arc near the bottom-left lobe gives similarly inconsistent distances, so this curve-fitting approach isn't converging on a clean geometric answer.

I'm struggling to nail down an exact coherent assembly here. Given time constraints, I'll settle for a plausible lamp structure—base, lower arm, upper arm, yoke, shade—and accept some risk that not every spring pin distance will be perfectly consistent, picking reasonable connection points like the spring at the yoke and elbow joints even if it means some approximation.

I don't actually know the real object's exact linkage geometry, so I should accept some approximation here rather than chase perfect correctness. I'll simplify to a realistic Anglepoise-style configuration where the spring connects the elbow bracket and yoke, letting the lower arm, upper arm, yoke, and p07 close out reasonably, and move on from trying to nail down every exact joint position.

I'm still unsure where p03 fits — all three holes on p07 and p08 seem already accounted for (lower arm, upper arm, spring; wrist, shade, spring), so p03 might be a separate attachment like a counterweight or bulb holder connecting elsewhere, maybe to the base.

I'm leaning toward H4 being a shared hinge point where both p03 and the lower arm's hole coincide, essentially treating it as a triple connection at the base. It's a bit forced, but I'll accept it as the working hypothesis and move forward to check p03's other side.

Now I'm mapping out the full linkage chain: base hinge connects to the lower arm and p03, the lower arm's other end meets the elbow knuckle p07, which has three holes for lower arm, upper arm, and spring. From there, the upper arm connects to the wrist piece p08, which links to the shade and to p06, with p06's far end tying back to p07's spring hole. I want to verify this whole chain is geometrically consistent by checking the distance constraint between p07's and p08's connection points.

I'm working through the degrees of freedom — the lower arm angle gives the elbow position, then the upper arm angle gives the wrist position, but I realize p07's own rotation isn't actually free since its two connection points are fixed by the lower and upper arm positions, making it a rigid triangle whose shape must satisfy both constraints simultaneously.

I likely can't pin down the exact pose from description alone, so I'll go with plausibility — shade facing down, lamp in a natural resting pose. Then I need to double check the spring component, p06.

Its length depends on where its ends actually land. Testing a few candidate endpoint pairs — the lobe near (19,86) against the corner at (37,14), or against the far end near (115,47) — gives distances around 74 or 104, compared to p07's sides near 63-68 and p08's near 66, so I'm leaning toward the shorter span of about 74 as the better fit, though the corner's rounding radius still needs checking.

Given the geometry won't fully resolve, I'll just commit to a plausible overall structure — base, lower arm, upper arm, head yoke, shade, spring, bulb, counterweight — and start assigning placements: base part at origin, then the lower arm's anchor point computed from the base's joint, with its direction angle still to be chosen.

Good, that confirms the rotation angle checks out. Now I'm setting up the transform for p05.

Now I'm working out the knuckle placement at p07, pinning joint A to the elbow point E and computing the local vectors to B and C so I can figure out the rotation that keeps the upper arm extending naturally to the right and downward toward the wrist.

Continuing the kinematic chain, I pick the upper arm rotation so the elbow-to-wrist vector points at roughly 10°, computing the wrist position from the elbow point. Now I'm working out the yoke segment starting at the wrist, trying to orient it so the shade hangs down sensibly.

But checking the spring constraint (p06) between knuckle C and the yoke C point, the distance comes out around 360, way beyond the spring's expected 74-104 length range — so my arbitrary pose choices clearly violate the spring geometry, meaning I need to actually solve for a consistent pose using the spring as a real constraint rather than guessing angles freely.

Since it's likely all-or-nothing grading, I should still try to make the assembly internally consistent by actually solving for the spring constraint rather than guessing — picking the yoke pose so the knuckle-to-yoke distance matches whichever spring length I settle on.

Actually, if the knuckle and yoke end up close together, that suggests a folded pose where the upper arm lies back against the lower arm, like a closed Anglepoise lamp. That's a plausible rest position, so a short spring length isn't necessarily wrong.

Since |B-W| is fixed at 340 (the upper arm link length), and knuckle C sits within about 68 of B while yoke C sits within about 66 of W, the minimum possible distance between the two centers is roughly 340 minus those two radii — around 206, not something that can shrink to zero.

But p06's actual extent only spans about 104, far short of 206, so it can't be the spring in that configuration — meaning my assumed structure (knuckle at elbow connecting to a yoke spring) must be incorrect, and I need to reconsider how the spring attaches across the mechanism.

Given the amount of uncertainty here, I think the best path forward is to accept I can't fully verify the exact geometric relationships and instead produce a plausible, internally consistent SVG that captures the overall Anglepoise-style design intent, being honest about the approximation involved.

Let me simplify: treat p07's A pin as a triple point coinciding with elbow E, shared with the lower arm's A5 and upper arm's B1, leaving p07 free to rotate while its B and C pins connect onward to p06 and p03.

Now I'm verifying the upper arm's transform - confirming the local angle at B1 toward A1 is about 25°, so the rotation needed is -15° to align with the 10° wrist direction, then computing the wrist position W by extending from E along that angle by the arm length, landing around (995.1, 432.2).

Next I'm placing the yoke piece with its pivot A at W, picking an orientation angle of 60° so the shade points downward, which gives the shade-pin B position and the required yoke rotation of about -48.6°. But when I compute point C from this transform, it ends up around (963, 491), which puts it roughly 325 units from E - way too far for a spring piece that's only 104 units long, so this configuration isn't going to work.

I'll just place p06 and p07 somewhere separate instead of trying to connect them to the yoke. For the shade itself, I'm setting S equal to the yoke's B point, choosing an opening angle of 60° globally which requires a shade rotation of about 17.6°, and checking that the rim position lands around (1116, 643) which fits comfortably within the canvas. Now I need to figure out how p07, p03, and p06 attach to the base - maybe p07 sits at the elbow with its A pin, and p06 connects between p07's points and something else, though the base only has H4 to work with so I'm still puzzling out how p03's H3 pin fits in.

Even forcing p06 between p07 B and p08 C won't work since it can't physically span both points with rounded ends matching. Let me reconsider whether p07 B should instead connect to p08 C directly without the spring in between.

Checking the geometry: the distance between B and C can't get small enough since B is pinned near E and C near W, and |E-W| is 340 while their individual radii only total around 130, so the gap stays at least 210 — too far for p06 to bridge. That means the spring must attach somewhere else, perhaps between p07's C point and another component instead.

Checking p06's pin placement at the elbow knuckle and wrist yoke seems too far apart, so maybe my assumption about which triangles sit at the elbow versus wrist is wrong — perhaps the upper arm actually connects elsewhere entirely.

Testing another hypothesis: maybe there's a triple-pin wrist assembly where the upper arm, yoke p08, and spring bracket p07 all meet, with p06 forming the short spring link between p07 and p08's pins. That distance range would fit much better than my earlier guess.

Actually this resembles an Anglepoise-style counterbalance, where the spring links the end of the upper arm to another pivoting lever at the same axis.

I'm trying different joint assignments—maybe the elbow connects the lower and upper arms, with the spring stretching from that joint to a point on the base, but the base only has one hinge available. Let me try having the wrist share the upper arm's pivot along with two other parts, leaving a free pin for the shade and another for the spring to attach to the lower arm segment.

Simplifying further, I want a chain: base hinges to lower arm, lower arm elbow-joins to upper arm, upper arm wrist-joins to two more parts, one of which carries the shade. The spring then connects between two of these free pins, and since both parts can rotate freely about the wrist, I can adjust their rotation to make the spring's two endpoints land at the right separation distance.

I work out the distance constraint around 67 units from the wrist, giving a valid spring-length range of about 3.5 to 130. Checking the spring's own pin pairs, several fall within that range, but since I don't actually know which two pins are the true spring endpoints, I'm forced to guess — picking the longest pair as the most plausible spring attachment points, while recognizing this guess could be wrong.

I then estimate the right lobe's rounded end center around (113,47), giving an L–R spring distance of about 101.8, and proceed to compute the yoke and shade poses from there — placing the wrist point, then deriving the shade's B and C coordinates from the chosen rotation angles, checking that C lands roughly where expected relative to the wrist.

Now I set up the spring geometry: with the yoke's A, B, C positions established, I verify the distance from W to C matches the expected 67, forming a triangle between W, B, and C with sides 63.5, 101.8, and 67 to solve for the spring's orientation angle.

The upper-left option feels more natural for a counterbalance spring pulling toward the lower arm, so I'll go with that placement.

Working out the rotation math for point p07: computing the angle from A to B gives about 69.8°, and since I want it at 221.7°, that means rotating by roughly 151.9°, which then shifts the A-to-C angle to about 157.9° for placing point C.

Checking the arithmetic for p07's rotated B position, I get coordinates around (947.8, 389.8), and verifying the distance from B to C comes out to about 102 — I'm trying to decide whether to pin p03's H3 joint to this p07 C point.

Now I'm computing p06's transform: the local L→R vector has length 101.8 at -22.5°, while the desired global vector from B to C is at 81.7°, giving a rotation of about 104.2°, which checks out within tolerance. I'm now moving on to figure out where p03's H3 joint should map in global space.

Recomputing p07's C point more precisely, I subtract pin A from local C to get a vector, apply the 151.9° rotation using cosine and sine values, then add back the global anchor W to land on roughly (935.5, 456.7) — confirming p03's H3 pin location matches this point.

Now I'm figuring out p03's orientation and placement. With H3 anchored at (935.5, 456.7), trying rotation 0 pushes the body into an awkward overlap with the upper arm and yoke, spanning roughly x 773-998 and y 286-509; flipping to 180° instead shifts things toward (1095, 623), which still risks overlapping the shade. I'll just pick something reasonable and move forward rather than over-optimizing this placement.

Switching to the shade component, I'm computing its rotation using the yoke's B pin location, derived from W plus a 66.2-unit offset at 60°, giving roughly (1028.2, 489.5). I'm verifying the yoke's local pin distances (A to B) check out to about 66.1, matching expectations, then setting up the yoke's transform chain with translate, rotate(-48.6°), and a translate back to re-center on pin A before confirming the B pin maps correctly under that transform.

Now I'm checking that the C pin also maps correctly under the same yoke transform, landing around (962.4, 490.7), and then building the shade's transform using the computed B position with a 17.6° rotation, verifying its facing direction lines up with the intended 60° global opening. I'm tracing through the shade's rim geometry to figure out its actual extents in global coordinates, working out the transformed positions of the rim's corner points to estimate how far the shade extends.

I'm also confirming the base sits flat with its top-left corner, hinge point, and bottom edge all landing where expected, then checking that everything stays within canvas bounds — the arms, yoke, shade, and other reference points. Finally I'm verifying the p01 arm's rotation transform by recomputing where its endpoint lands, confirming it matches the target W position, and starting the same check for p05's local B5 point.

Now computing p03's placement using the offset from p07's C coordinate, landing the body roughly in the 768–1000 x-range and 281–510 y-range.

Noticing the arm would overlap physically, though that's acceptable here—I'm weighing whether to rotate p03 180° about H3 so the body extends away instead, and tracking the local blade offsets to figure out where each piece would land.

Deciding to leave the placement as is and confirming the base sits level at the ground line. Now I'm writing the SVG, placing each kit piece with translate and rotate transforms to position the limbs and body parts...

In my reply, I should be upfront about which joints I'm confident about and which ones (like the spring, p03, p06) remain a bit ambiguous, then give the final SVG with a brief explanation.


````

## Answer

````text
I identified the parts from their drawings, but parts p03, p06 and p07 are uncertain, so this assembly may not pass every connection check.

**Identification**
- **p04**: flat base plate with a hinge hole near its right end. It stands upright on its bottom edge.
- **p05** and **p01**: straight links with pin holes at both ends (lower arm and upper arm).
- **p08**: triangular three-hole yoke. Its hole B matches the shade's pivot.
- **p02**: cone-shaped shade with a pivot tab at its top-left.
- **p07**: three-hole bracket pinned at the wrist.
- **p06**: bent link with rounded ends, used here as the spring between p07 and the yoke.
- **p03**: bent bracket with one lobe hole, pinned to p07.

**Assumed joints**
- Base hinge → lower arm (bottom end).
- Lower arm top → upper arm (elbow).
- Upper arm far end → yoke → shade pivot, with the shade opening downward.
- Wrist bracket p07 and yoke joined through the spring p06.
- p03 hung from p07.

The spring and p03 placements are guesses rather than deductions, and the spring length was estimated from p06's rounded-end positions. The shade faces down-right at about 60° below horizontal.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1376 768">
<use href="#kit-p04" transform="translate(295,652.9)"/>
<use href="#kit-p05" transform="translate(548.4,679.5) rotate(25.5) translate(-52.2,-345.2)"/>
<use href="#kit-p01" transform="translate(659.9,373.1) rotate(-15) translate(-20.5,-20.7)"/>
<use href="#kit-p08" transform="translate(995.1,432.2) rotate(-48.6) translate(-89.5,-23.9)"/>
<use href="#kit-p02" transform="translate(1028.2,489.5) rotate(17.6) translate(-15.36,-18.85)"/>
<use href="#kit-p07" transform="translate(995.1,432.2) rotate(151.9) translate(-36.5,-36.6)"/>
<use href="#kit-p06" transform="translate(947.6,390.1) rotate(104.2) translate(-19,-86)"/>
<use href="#kit-p03" transform="translate(768,281.3)"/>
</svg>
````

## Prompt

````text
Below is a kit of 8 SVG parts for a desk lamp with a jointed arm (side view). Each part is a <g id="kit-..."> drawn in its own local coordinate system, stored at an arbitrary rotation. The parts are unlabelled (ids p01 to p08); work out what each one is from its drawing.

Assemble the parts into one complete, working desk lamp with a jointed arm (side view) on a 1376 x 768 canvas. Parts are rigid: translate and rotate only, no scaling and no mirroring. Use every part exactly once. The base part, kit-p04, stays upright exactly as stored (at most 3 degrees of rotation).

Nobody will tell you which part connects to which, at which hole or feature, or which way round a part goes. Work that out from the parts, as a practitioner who knows this object would.

Grading is done by code on where the parts land:
- every connection the real object has must be made: the matching features of the two connected parts (pin holes, axle holes, bolt holes, hub centres, the centres of rounded ends, seats) must coincide within 6 px;
- a part that slides along a guide (such as a piston in its bore) must sit on the guide's centre line, within 6 px;
- every part must face the way it does on the working object, relative to the base part, within 8 degrees; parts that turn in use (wheels, gears, sprockets, cranks, connecting rods, pedals, rotors) may sit at any angle;
- anything that stands on the ground must stand level, within 6 px;
- a missing, duplicated, scaled, skewed or mirrored part fails the assembly.

Reply with one <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1376 768"> that contains exactly one <use href="#kit-ID" transform="..."/> per part. You may wrap <use> elements in <g transform="..."> groups. Do not copy the part drawings: the kit's <defs> are inserted automatically.

KIT:
<svg xmlns="http://www.w3.org/2000/svg"><defs>
<g id="kit-p01" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 340.934844818,168.967806972 L 341.693855258,164.328420897 L 340.650176157,159.706653494 L 338.957694111,156.810879931 L 335.684663063,153.958290273 L 331.301274431,152.148344388 L 325.551530773,152.431977721 L 320.040510997,151.032456008 L 34.4151399053,17.9991993064 L 29.5007572784,11.8065550088 L 26.791886912,9.91922320504 L 21.3661996168,8.16938967726 L 16.3854836173,8.81162649669 L 11.3543273696,12.2390842735 L 9.32189583693,15.4264377313 L 8.13553277227,19.4764430003 L 8.68380032962,24.4913610141 L 10.7867065471,28.5147657216 L 14.0597375953,31.3673553796 L 18.4089242124,33.0833320024 L 25.2607337819,32.611415036 L 309.877663115,164.628283417 L 316.337702512,168.342834667 L 319.824927536,173.245819638 L 323.508037647,176.055570501 L 328.44660507,177.3441945 L 333.170978517,176.582423185 L 338.116802283,173.505277223 Z M 336.960499921,163.603612471 L 336.551456186,167.157861087 L 335.441443712,169.370974801 L 333.656372842,171.191283013 L 330.085540883,172.490959558 L 327.137946635,172.2867828 L 324.608723121,171.185407107 L 322.856818937,169.588274761 L 321.180920235,164.983780919 L 321.957204237,160.976614445 L 323.91294007,158.455682603 L 328.004748806,156.54071491 L 333.037285491,157.795136894 L 334.977128199,159.323865211 Z M 28.2898643084,19.5901106369 L 27.5564191016,24.0073561733 L 26.0276907843,25.9471988813 L 21.5344397664,28.2211151704 L 17.1513962443,27.5816392257 L 15.1859883029,26.2750514469 L 13.8099611674,24.5411110436 L 12.8181027517,21.8160024433 L 13.0392079622,18.3301578561 L 14.5762279511,15.5359550085 L 16.6774086218,13.707010015 L 19.30854796,12.7493536137 L 21.9058303932,12.8681978905 L 25.5630301614,14.7296193516 L 26.9988245447,16.3353884785 Z" fill="#dbeddc" stroke="none"/>
  <path d="M 343.250909683,171.530197172 L 344.778602673,166.078944644 L 344.247263568,160.525776291 L 342.127083788,155.870151982 L 336.802967208,150.89081642 L 331.437047161,149.012811616 L 324.57660081,149.168618782 L 318.279279814,146.778273981 L 36.2427044614,15.4185002164 L 31.8496437211,9.78103471034 L 26.2781664783,6.16874439348 L 20.425471668,5 L 15.9232387598,5.78733654834 L 10.6526684118,8.55700949059 L 6.64722748479,13.6330751896 L 5,19.340670271 L 5.90756126252,25.9275005067 L 8.92493997667,31.0014955496 L 14.2231462141,35.0325017101 L 19.512025452,36.4064581895 L 25.7658174347,36.045784047 L 297.155540064,162.128766448 L 311.96364088,169.189938463 L 314.091422112,170.650262752 L 318.843431448,176.68917054 L 323.697011499,179.498576293 L 330.113521882,180.462108601 L 335.452841368,179.050844123 L 340.330261106,175.785759637 Z M 340.934844818,168.967806972 L 338.424275303,173.180530641 L 335.14433302,175.864180884 L 330.027154073,177.301010595 L 323.508037647,176.055570501 L 319.824927536,173.245819638 L 316.337702512,168.342834667 L 309.877663115,164.628283417 L 25.2607337819,32.611415036 L 18.4089242124,33.0833320024 L 14.0597375953,31.3673553796 L 10.7867065471,28.5147657216 L 8.68380032962,24.4913610141 L 8.13553277227,19.4764430003 L 9.32189583693,15.4264377313 L 11.3543273696,12.2390842735 L 16.3854836173,8.81162649669 L 21.3661996168,8.16938967726 L 26.791886912,9.91922320504 L 29.5007572784,11.8065550088 L 34.4151399053,17.9991993064 L 320.040510997,151.032456008 L 325.551530773,152.431977721 L 331.301274431,152.148344388 L 335.684663063,153.958290273 L 338.957694111,156.810879931 L 340.650176157,159.706653494 L 341.693855258,164.328420897 Z" fill="#13243b" stroke="none"/>
  <path d="M 336.062610767,160.844301857 L 332.199853804,157.248594883 L 328.004748806,156.54071491 L 324.809793895,157.703583397 L 322.076738733,160.720271893 L 321.368168541,162.57443701 L 321.215122249,165.077750181 L 322.395264299,168.904924693 L 326.018607162,171.842846832 L 328.915070943,172.491304667 L 333.656372842,171.191283013 L 335.381676465,169.499146077 L 336.773251615,166.01295638 L 336.960499921,163.603612471 Z M 333.868151053,165.048388745 L 332.399535093,168.030530117 L 329.366953473,169.347135114 L 325.786794514,167.989761978 L 324.299179446,164.487334047 L 326.280135402,160.573791726 L 328.75753823,159.778508616 L 332.175323898,160.982145242 L 333.252169686,162.186472087 Z" fill="#15243c" stroke="none"/>
  <path d="M 27.4261771692,16.9247692844 L 24.8195677364,14.1488753266 L 22.606454023,13.0388628529 L 19.30854796,12.7493536137 L 16.6774086218,13.707010015 L 14.5762279511,15.5359550085 L 13.0392079622,18.3301578561 L 12.8181027517,21.8160024433 L 13.8099611674,24.5411110436 L 15.4765328701,26.4885552044 L 18.4928762562,28.0511404268 L 21.5344397664,28.2211151704 L 25.3529774973,26.7248633207 L 27.9319510406,22.7000781758 L 28.2556622941,19.4961413748 Z M 25.1460398646,20.3086980472 L 23.9082012237,23.632514453 L 22.1058567917,24.8206030644 L 19.9956942308,25.1629683171 L 17.5604399789,24.0273906099 L 16.3381493532,22.1310769158 L 15.9615820862,19.9269450928 L 17.4986020751,17.1327422451 L 20.2492759088,15.918743291 L 22.5732873367,16.4563034114 L 24.4191607827,18.019233743 Z" fill="#15233c" stroke="none"/>
  <path d="M 332.175323898,160.982145242 L 328.75753823,159.778508616 L 325.511452853,161.38565818 L 324.299179446,164.487334047 L 325.786794514,167.989761978 L 329.366953473,169.347135114 L 332.399535093,168.030530117 L 333.816675477,164.322199882 Z" fill="#ecf4e9" stroke="none"/>
  <path d="M 24.4191607827,18.019233743 L 21.3599786013,16.0465694581 L 18.1477501288,16.5772183442 L 16.9776252979,17.7480333938 L 15.8593211526,20.8155072467 L 16.8169775539,23.4466465849 L 19.9956942308,25.1629683171 L 22.1058567917,24.8206030644 L 23.9082012237,23.632514453 L 25.1460398646,20.3086980472 Z" fill="#e4f0e3" stroke="none"/>
  <path d="M 329.770365592,166.976173566 A 2.5,2.5 70 0,1 326.566083682,165.481992372 A 2.5,2.5 70 0,1 328.060264876,162.277710462 A 2.5,2.5 70 0,1 331.264546786,163.771891656 A 2.5,2.5 70 0,1 329.770365592,166.976173566 Z" fill="#F8F7F2" stroke="#1F2A3A" stroke-width="2.3"/>
  <path d="M 21.3731390288,23.0121438639 A 2.5,2.5 70 0,1 18.1688571185,21.5179626702 A 2.5,2.5 70 0,1 19.6630383122,18.31368076 A 2.5,2.5 70 0,1 22.8673202225,19.8078619536 A 2.5,2.5 70 0,1 21.3731390288,23.0121438639 Z" fill="#F8F7F2" stroke="#1F2A3A" stroke-width="2.3"/>
</g>
<g id="kit-p02" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 172.359131198,121.20019804 L 174.936126478,112.361131612 L 175.93624382,103.117768301 L 175.256638193,92.9807995134 L 172.305155972,81.5637616883 L 167.203451626,71.6818280331 L 160.767202163,63.7153549834 L 152.289194674,56.3415236168 L 143.926734528,51.5593420745 L 132.997053063,47.7868014089 L 125.004199275,46.7077794824 L 111.477736976,46.1378517032 L 100.995590336,44.0083912487 L 86.7003558064,38.2251162475 L 73.6790831883,29.9464412688 L 68.3023077296,29.6459655342 L 65.5298844062,31.3322836881 L 37.8227460084,65.1954566316 L 37.1587710424,67.092595858 L 37.4494728158,69.5452459511 L 39.3292667798,72.849239694 L 51.0826846128,83.8468380338 L 60.0998338222,96.2166003652 L 64.0834331921,104.473775188 L 69.5740413916,122.040027538 L 75.2801136152,132.755471522 L 83.6379308099,142.280013072 L 92.399556829,148.57238222 L 100.018649367,152.345899003 L 109.987546966,155.339405418 L 119.502802613,156.466308239 L 130.129079993,155.68385758 L 142.331259195,151.995114877 L 150.666850544,147.606730566 L 160.427129731,139.689853012 L 167.692008939,130.499013547 Z" fill="#fdeec6" stroke="none"/>
  <path d="M 168.575352396,134.993421666 L 174.794436028,123.549515043 L 178.047620527,113.260356156 L 179.143499658,100.972189127 L 178.161954121,91.246112407 L 176.474171792,83.5078056923 L 171.003349147,71.5780068851 L 165.056408277,63.508688804 L 156.970971477,55.7662271962 L 148.904344114,50.3496302029 L 138.947172709,46.1478760909 L 131.195675625,44.078022725 L 110.71555993,42.8033223286 L 103.157538656,41.2650393822 L 90.0466113755,36.2546915049 L 75.980031239,27.3782438334 L 71.2977663782,26.2982457902 L 66.2112046347,26.7951256848 L 60.6822390755,22.5618598245 L 59.3584440365,19.9584838058 L 56.5188423232,19.1860447403 L 53.8294784772,15.7252179454 L 48.2042630712,12.881461339 L 46.8804680322,10.2780853203 L 44.312758655,9.63243173334 L 42.348929097,8.16499401164 L 40.293980702,5 L 30.8998914652,5.03297592335 L 25.4212470917,7.55378052293 L 15.7252179454,7.99764851363 L 12.7837473173,10.0464897823 L 8.27858912083,15.448669863 L 5,21.5331462889 L 6.55537778225,30.9751164199 L 5.35470138694,36.1527970004 L 5.72430774473,39.8559566162 L 7.33831649896,43.2566882641 L 11.7074033141,47.611120535 L 12.584151586,50.2267108064 L 14.8738615007,50.5220555313 L 18.209366992,53.0704674128 L 19.4002694262,55.722212384 L 22.5056563492,56.3979135444 L 24.0585938399,57.5634113566 L 25.6059122625,60.1606802489 L 28.7718823908,61.4163207814 L 33.5213256415,64.9550760439 L 34.9611560813,71.8053963506 L 36.7864739664,74.7529741051 L 51.0357798352,88.6798288202 L 58.1313613128,99.4915226512 L 62.7198166184,110.237502267 L 67.0373557046,124.167285332 L 71.6675847781,133.167339706 L 77.5600495688,140.880241798 L 85.9474262787,148.211811339 L 95.9957165204,154.111121741 L 107.78333682,158.173388063 L 118.694208848,159.620064114 L 129.501747785,158.922137108 L 140.254322586,156.21249965 L 150.462624656,151.593996771 L 159.280929414,145.223949581 Z M 172.359131198,121.20019804 L 166.230678344,132.686366488 L 160.427129731,139.689853012 L 151.373575395,147.274255025 L 142.288997369,152.085745656 L 130.974804575,155.52653647 L 119.502802613,156.466308239 L 109.987546966,155.339405418 L 98.659187686,151.71197161 L 92.399556829,148.57238222 L 83.6379308099,142.280013072 L 74.6696386114,131.698437809 L 69.4834106129,121.997765711 L 64.0834331921,104.473775188 L 60.0998338222,96.2166003652 L 50.8530541029,83.6294217766 L 38.7248989024,72.0157293649 L 37.4494728158,69.5452459511 L 37.1587710424,67.092595858 L 37.8227460084,65.1954566316 L 65.5298844062,31.3322836881 L 68.3023077296,29.6459655342 L 73.6790831883,29.9464412688 L 86.7003558064,38.2251162475 L 100.995590336,44.0083912487 L 110.758797872,46.0232804774 L 128.278633502,47.0209575281 L 136.694593611,48.8489661313 L 143.473580635,51.3480329436 L 152.289194674,56.3415236168 L 160.767202163,63.7153549834 L 167.203451626,71.6818280331 L 172.305155972,81.5637616883 L 175.256638193,92.9807995134 L 175.93624382,103.117768301 L 174.936126478,112.361131612 Z M 62.9917345442,28.4936580914 L 61.9412960162,30.9829509426 L 36.0396899495,62.1572480985 L 35.1455964152,62.1816766039 L 29.2902624409,57.4652092765 L 51.9098629786,20.7883273001 L 54.2601560986,21.663611397 L 56.0972001781,23.4029414548 L 47.323597538,37.9588301846 L 46.7864080504,39.5840770749 L 47.257883323,40.4659563565 L 49.1005464706,40.7735153342 L 58.0615177944,26.5256736403 L 59.6078601004,25.8123536051 Z M 46.2113620564,15.2622900907 L 49.6074507529,18.3906413442 L 26.365649017,55.2187373047 L 23.3565119407,53.1535268902 L 22.8789295418,52.048124225 L 44.0010447843,17.8727493524 Z M 39.5887200263,10.2983589327 L 42.8274876126,12.5809856044 L 42.9486540231,13.7408643485 L 20.0087921967,50.1580682415 L 16.1717638594,47.2654546243 L 37.7164973637,12.1837719647 Z M 35.7700130681,8.0763154662 L 36.1931193881,8.82530214294 L 13.6880900763,44.7832450161 L 9.7360024548,40.9542760384 L 8.57514759409,37.7648535213 L 8.76154016123,34.7623116297 L 10.5487511132,31.4028656913 L 27.8203972225,10.2172516885 L 30.3270353361,8.62767143972 Z M 22.9150970364,10.7986552355 L 9.46020565218,27.5851348497 L 8.22093426547,24.8004972736 L 8.06312509686,22.2994782281 L 9.71133631765,18.7648778586 L 13.4736149638,14.0093274815 L 17.3631671467,10.6371792321 Z" fill="#13233b" stroke="none"/>
  <path d="M 62.9011037655,28.4513962652 L 58.6653976135,25.7038895056 L 49.7105334161,40.1752545831 L 48.3877144936,40.8824674919 L 47.257883323,40.4659563565 L 47.0277647548,38.5932456355 L 56.1878309568,23.445203281 L 52.7555875604,20.6310061898 L 51.9098629786,20.7883273001 L 29.2057387886,57.646470834 L 35.9067973446,62.205617051 L 62.3338667045,30.6143207014 Z" fill="#fcedc2" stroke="none"/>
  <path d="M 36.2654287878,8.19699381836 L 32.3265315357,8.12566053536 L 27.7781353963,10.3078824672 L 10.5487511132,31.4028656913 L 8.76154016123,34.7623116297 L 8.57514759409,37.7648535213 L 9.7360024548,40.9542760384 L 13.6880900763,44.7832450161 Z" fill="#fdeec2" stroke="none"/>
  <path d="M 39.2745658641,10.2622042329 L 16.8479530782,45.8153621651 L 16.2685017645,47.5312398341 L 20.0087921967,50.1580682415 L 42.773499592,13.8798640797 L 42.8274876126,12.5809856044 Z" fill="#fff2cd" stroke="none"/>
  <path d="M 45.9878386728,15.2683972171 L 22.9634531941,51.8668626676 L 23.265881162,53.111265064 L 26.365649017,55.2187373047 L 49.6919744053,18.2093797868 Z" fill="#fff2cd" stroke="none"/>
  <path d="M 22.7822044316,10.847024188 L 17.3631671467,10.6371792321 L 13.4736149638,14.0093274815 L 8.72710006293,20.4023390016 L 8.06312509686,22.2994782281 L 8.91642097995,27.3315638927 L 10.0279307715,27.0775048773 Z" fill="#fcedc2" stroke="none"/>
  <path d="M 17.629902151,19.9085627555 A 2.5,2.5 25 0,1 14.307587029,21.1177865687 A 2.5,2.5 25 0,1 13.0983632158,17.7954714468 A 2.5,2.5 25 0,1 16.4206783377,16.5862476335 A 2.5,2.5 25 0,1 17.629902151,19.9085627555 Z" fill="#F8F7F2" stroke="#1F2A3A" stroke-width="2.3"/>
</g>
<g id="kit-p03" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 8.3842738722,9.4590490036 L 16.2986983202,222.712939673 L 129.05353019,153.579243909 L 126.654230641,71.5530690523 L 30.0966951619,20.2859027359 Z" fill="#ebe9e4" stroke="none"/>
  <path d="M 221.975326012,72.9346541266 L 218.189609858,69.8429954776 L 212.601894382,69.1098953802 L 137.034723593,71.7123363589 L 129.875441004,72.5089999069 L 132.701402959,152.783615689 L 216.487428562,149.956618407 L 220.041332068,149.195192201 L 222.92846885,147.186600355 L 224.756033406,144.605901265 L 225.387217679,141.077217883 L 223.737592524,80.7002459741 L 223.120920938,75.4973894361 Z" fill="#ece9e4" stroke="none"/>
  <path d="M 225.119150456,72.2160667163 L 221.726239803,68.4493496709 L 215.898765117,65.8879947987 L 128.310785126,68.5025236518 L 9.2375986838,5.95593085459 L 6.01638832103,5 L 5,6.00844175879 L 13.1472724234,226.626827103 L 14.8732662645,227.275630048 L 131.369595056,156.141634109 L 150.045638523,155.409923497 L 150.985676253,156.238373294 L 152.129191475,180.723927666 L 154.429018107,186.165508086 L 160.240254559,191.606053178 L 167.101391128,193.791185892 L 173.158607806,193.182805978 L 177.814232115,191.062626198 L 182.802204458,186.054619419 L 185.166984025,179.979438961 L 185.065422357,154.263302291 L 218.402051146,152.877957203 L 224.245073847,150.219181975 L 227.430701758,146.399263807 L 228.642284947,140.956648059 L 226.915618982,80.0756278259 L 226.589837072,76.2567449856 Z M 221.09505553,71.9780330533 L 222.915708852,74.9335738637 L 223.488851424,77.3854114586 L 225.186846171,127.954342769 L 225.191332593,143.170451991 L 222.92846885,147.186600355 L 220.605147641,148.989980115 L 217.495525211,149.802536788 L 132.735604973,152.877584951 L 129.944190142,73.8674083712 L 130.968870135,72.0046064728 L 214.370381909,68.9983074469 L 218.189609858,69.8429954776 Z M 9.27283602616,9.56130993726 L 126.654230641,71.5530690523 L 129.147499452,153.545041895 L 16.008153753,222.499435915 L 8.33314340538,9.90333008058 Z M 180.887590921,154.187641918 L 181.562649318,154.580447419 L 182.235628011,176.896071983 L 181.741251795,180.800632414 L 180.247070601,184.004914324 L 176.061982822,188.295023912 L 170.458029111,190.441114034 L 165.61377606,190.288757962 L 162.41813093,189.110686569 L 157.427397713,184.754933827 L 155.409823976,180.381217304 L 154.595886866,172.589715114 L 154.530942979,155.160837287 Z" fill="#14243b" stroke="none"/>
  <path d="M 180.887590921,154.187641918 L 154.530942979,155.160837287 L 154.595886866,172.589715114 L 155.409823976,180.381217304 L 157.427397713,184.754933827 L 162.41813093,189.110686569 L 165.61377606,190.288757962 L 170.458029111,190.441114034 L 176.061982822,188.295023912 L 180.247070601,184.004914324 L 181.741251795,180.800632414 L 182.235628011,176.896071983 L 181.562649318,154.580447419 Z M 174.997924174,172.506807446 L 175.666071337,178.435852847 L 174.342555105,180.939511127 L 171.523822352,183.136041497 L 168.567936433,183.786224879 L 165.996219233,183.445240064 L 162.210503079,180.353581415 L 161.192389211,175.509673473 L 163.03653711,171.220254103 L 165.146354562,169.70741891 L 167.845897929,168.937701033 L 172.169174203,169.705348254 Z" fill="#eceae5" stroke="none"/>
  <path d="M 173.00660589,170.251890265 L 170.571351638,169.116312558 L 167.845897929,168.937701033 L 165.146354562,169.70741891 L 161.943453089,172.895117478 L 161.064217935,175.449906225 L 161.475332325,178.91847725 L 163.031006314,181.438373765 L 165.19298956,182.992667315 L 167.269295216,183.726802741 L 170.866037518,183.375455598 L 174.342555105,180.939511127 L 175.666071337,178.435852847 L 175.75036849,174.574131211 L 174.895318131,172.224899659 Z M 172.196119874,174.165087477 L 172.709150089,175.574626408 L 172.308398026,178.274514884 L 171.112707962,179.667470472 L 168.447366609,180.531157611 L 166.217324443,179.959395477 L 165.012307379,178.695301384 L 164.388034341,176.687744866 L 164.712090703,174.654278005 L 166.898603855,172.475021197 L 170.281842399,172.414218621 Z" fill="#15243b" stroke="none"/>
  <path d="M 171.247445363,173.020527879 L 168.692656616,172.141292725 L 166.898603855,172.475021197 L 164.712090703,174.654278005 L 164.644722003,177.977749301 L 166.217324443,179.959395477 L 170.053480845,180.265833168 L 172.57303225,177.53968924 L 172.529503236,174.788670297 Z" fill="#f9f7f3" stroke="none"/>
  <path d="M 165.293835545,177.305178406 A 3.47,3.47 160 0,1 167.367759042,172.857635115 A 3.47,3.47 160 0,1 171.815302334,174.931558612 A 3.47,3.47 160 0,1 169.741378837,179.379101903 A 3.47,3.47 160 0,1 165.293835545,177.305178406 Z" fill="#F8F7F2" stroke="#1F2A3A" stroke-width="2.3"/>
</g>
<g id="kit-p04" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 8,21.3 L 8,43.1 L 8.5,44 L 268.4,44.1 L 276.9,43.6 L 276.4,16.7 L 274.7,13.5 L 272.1,10.8 L 268.6,9 L 265.7,8.4 L 18.9,8.4 L 15.3,9.4 L 11.9,11.6 L 9,15.6 Z M 253.3,19 L 256.1,19.4 L 258.3,20.7 L 260.5,24 L 260.9,26.4 L 260.2,29.8 L 259,31.5 L 256.9,33.3 L 253.6,34.1 L 249,32.7 L 246.6,29.9 L 245.9,26.5 L 246.8,22.9 L 248.5,20.7 L 250.6,19.4 Z" fill="#dbe8f5" stroke="none"/>
  <path d="M 271,6.6 L 274.9,9.2 L 277.2,11.9 L 279.3,15.8 L 279.8,18.7 L 279.8,44.3 L 279.1,45.9 L 276.6,47.1 L 9,47.1 L 6.6,46.5 L 5,44.3 L 5,18.7 L 5.6,15.6 L 7,12.7 L 9.8,9.4 L 12.6,7.2 L 16.9,5.4 L 200.6,5.2 L 200.6,6.2 L 248.6,6.2 L 248.6,5 L 266,5.1 Z M 8,43.3 L 8.4,44 L 276.4,44.1 L 276.9,19.6 L 276.4,16.7 L 274.6,13.4 L 270.2,9.7 L 265.6,8.4 L 18.9,8.4 L 15.3,9.4 L 11.9,11.6 L 8.4,17.2 Z" fill="#1a2942" stroke="none"/>
  <path d="M 252.4,19 L 250.1,19.6 L 247.3,21.9 L 245.9,26.7 L 246.7,29.9 L 249.8,33.2 L 253.4,34.1 L 258.2,32.3 L 260.2,29.7 L 260.9,26.4 L 260.2,23.3 L 258.1,20.5 L 254.8,19.1 Z M 253.2,22.3 L 256.4,23.3 L 257.8,26.7 L 256.7,29.7 L 253.5,31.1 L 250.2,29.8 L 249.2,27.2 L 249.8,24 Z" fill="#14233b" stroke="none"/>
  <path d="M 253.2,22.3 L 249.8,24 L 249.2,27.1 L 250.2,29.8 L 253.5,31.1 L 256.7,29.7 L 257.8,26.7 L 256.4,23.3 Z" fill="#f3f3ed" stroke="none"/>
  <path d="M 257.2,26.62 A 3.82,3.82 0 0,1 253.38,30.44 A 3.82,3.82 0 0,1 249.56,26.62 A 3.82,3.82 0 0,1 253.38,22.8 A 3.82,3.82 0 0,1 257.2,26.62 Z" fill="#F8F7F2" stroke="#1F2A3A" stroke-width="2.3"/>
</g>
<g id="kit-p05" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 18.6914817686,8.15382037319 L 14.2428231473,9.79985696777 L 10.4738737168,13.2646831092 L 8.44162862346,17.2130979659 L 8.01505754117,21.309198198 L 8.85825713021,25.6840141317 L 13.3302832749,32.7218392333 L 42.8380132827,334.039452176 L 42.3951271617,337.63581866 L 40.5677550821,341.117299851 L 39.8871958645,345.401788053 L 41.07437131,350.505768309 L 44.9568459903,355.421700607 L 49.4049945956,357.437630662 L 54.197459068,357.74141394 L 59.2032090816,355.997147103 L 61.9725210095,353.785606588 L 64.7421729481,349.132754975 L 65.1280414362,343.176992596 L 63.3755320764,338.531703483 L 60.2957243963,334.910269423 L 47.0505343304,204.412970829 L 30.124940247,29.8322895817 L 32.4850161635,24.8926497498 L 33.1166302648,19.1089603021 L 31.5361938359,14.2179255758 L 28.2106405425,10.4244185845 L 23.3774734759,8.2609731598 Z M 15.9134173027,14.3877884372 L 19.3052507831,12.8562971245 L 23.2375206064,13.1681529195 L 27.1366503362,16.1425078665 L 28.5206262787,19.9193598083 L 28.4874861852,22.5818589603 L 26.7174717492,25.9814249468 L 25.0460275671,27.496771226 L 21.465806117,28.7742744034 L 18.6968341998,28.5445038181 L 14.0522251081,25.414390979 L 12.7175342925,20.6954291836 L 13.692954245,16.8615596088 Z M 48.7359080016,338.169202518 L 51.8900683855,337.325832924 L 55.347162021,337.793276606 L 59.2708493115,340.906904401 L 60.2126191544,343.397500627 L 60.1137088898,347.723031434 L 56.6313776722,351.998937103 L 54.3619694983,352.973507029 L 50.7819180535,353.030354656 L 46.3011393707,350.014957104 L 44.9415509836,347.59803356 L 44.7864731128,343.460890723 L 45.5568500462,341.314610364 Z" fill="#e3f1e3" stroke="none"/>
  <path d="M 20.2894232737,5 L 13.4813687573,6.70305422752 L 9.90097730187,9.20121295458 L 5.7629844381,15.459568574 L 5,23.3486657814 L 6.47396366367,28.043070016 L 10.0533350871,32.8688445874 L 29.033011739,223.170872622 L 39.6182527332,335.325197876 L 37.0859338805,341.731238871 L 36.8723083286,346.220600086 L 37.3306594617,349.2272451 L 39.1487689872,353.430158108 L 43.7521654686,358.36257545 L 49.6912727977,360.690021289 L 54.9343558972,360.698943832 L 61.0625312174,358.397755608 L 65.2575417141,354.498795883 L 67.9700060144,348.707203924 L 68.3476319804,343.111902446 L 66.5870501039,337.606418684 L 63.228866733,332.813444196 L 33.5162637114,31.9627649182 L 33.4018884349,29.6852842276 L 35.9094797214,24.3606259344 L 36.1069602399,18.1508754205 L 34.0187175456,12.4159610837 L 29.3579634206,7.56545894623 L 26.0648701993,5.99207500194 Z M 18.6914817686,8.15382037319 L 23.3774734759,8.2609731598 L 28.2106405425,10.4244185845 L 31.5361938359,14.2179255758 L 33.1166302648,19.1089603021 L 32.4850161635,24.8926497498 L 30.124940247,29.8322895817 L 47.0505343304,204.412970829 L 60.2957243963,334.910269423 L 63.3755320764,338.531703483 L 65.1280414362,343.176992596 L 64.7421729481,349.132754975 L 61.9725210095,353.785606588 L 59.2032090816,355.997147103 L 54.197459068,357.74141394 L 49.4049945956,357.437630662 L 44.9568459903,355.421700607 L 41.07437131,350.505768309 L 39.8871958645,345.401788053 L 40.5677550821,341.117299851 L 42.3951271617,337.63581866 L 42.8380132827,334.039452176 L 13.3302832749,32.7218392333 L 8.85825713021,25.6840141317 L 8.01505754117,21.309198198 L 8.44162862346,17.2130979659 L 10.4738737168,13.2646831092 L 14.2428231473,9.79985696777 Z" fill="#14243b" stroke="none"/>
  <path d="M 44.7864731128,343.460890723 L 44.9415509836,347.59803356 L 46.3011393707,350.014957104 L 50.7819180535,353.030354656 L 54.3619694983,352.973507029 L 56.3773895369,352.187325072 L 60.1710665335,347.641116229 L 60.5236249227,345.568508552 L 59.5902676072,341.496795876 L 58.0012486455,339.407533149 L 55.347162021,337.793276606 L 50.9151584491,337.497735849 L 48.817823206,338.226560162 L 45.5568500462,341.314610364 Z M 49.6038351568,341.46263575 L 53.9212934468,340.701351366 L 56.2231616928,341.946904487 L 57.0090036382,346.403635625 L 54.5263099232,349.426255667 L 51.2739192961,349.712533869 L 48.841020724,348.131077408 L 47.8994208865,344.419825632 Z" fill="#15233a" stroke="none"/>
  <path d="M 15.094095253,15.0348675506 L 13.373365944,17.4923236834 L 12.7175342925,20.6954291836 L 14.0522251081,25.414390979 L 17.0748451499,27.897084694 L 21.465806117,28.7742744034 L 24.2595056003,27.9226622869 L 26.7174717492,25.9814249468 L 28.4874861852,22.5818589603 L 28.5206262787,19.9193598083 L 27.7509293667,17.1830179686 L 25.5148312917,14.2744331927 L 20.6651791809,12.8319095691 L 18.2156255594,13.1920304589 Z M 16.7157442922,18.1235977741 L 18.7804494577,16.3953059644 L 22.4178585461,16.2565431324 L 25.1045752482,18.8702671735 L 24.7516768482,23.3841859498 L 21.4007159673,25.5546838591 L 18.7710168982,25.3003557131 L 16.1990154834,22.5228012632 L 15.9618524029,19.5489563322 Z" fill="#15223a" stroke="none"/>
  <path d="M 15.9618524029,19.5489563322 L 16.1990154834,22.5228012632 L 18.7710168982,25.3003557131 L 21.4007159673,25.5546838591 L 24.7516768482,23.3841859498 L 25.1045752482,18.8702671735 L 22.4178585461,16.2565431324 L 20.0912627339,16.0923727128 L 17.9939274909,16.8211970253 Z" fill="#f9f5ee" stroke="none"/>
  <path d="M 48.2026941488,343.289327808 L 48.4970448676,347.401913085 L 50.6677127823,349.532218416 L 54.5263099232,349.426255667 L 56.7958881024,347.231030191 L 57.1730040524,345.297695362 L 56.4852223449,342.618711166 L 54.6667728087,340.857109258 L 50.2510842755,341.06130225 Z" fill="#f7f3eb" stroke="none"/>
  <path d="M 24.2519941012,23.0343043236 A 4.35,4.35 35 0,1 18.1936252104,24.1025582182 A 4.35,4.35 35 0,1 17.1253713159,18.0441893274 A 4.35,4.35 35 0,1 23.1837402067,16.9759354328 A 4.35,4.35 35 0,1 24.2519941012,23.0343043236 Z" fill="#F8F7F2" stroke="#1F2A3A" stroke-width="2.3"/>
  <path d="M 55.7562192531,347.687197577 A 4.35,4.35 35 0,1 49.6978503623,348.755451471 A 4.35,4.35 35 0,1 48.6295964677,342.69708258 A 4.35,4.35 35 0,1 54.6879653585,341.628828686 A 4.35,4.35 35 0,1 55.7562192531,347.687197577 Z" fill="#F8F7F2" stroke="#1F2A3A" stroke-width="2.3"/>
</g>
<g id="kit-p06" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M 119.19646597,40.8202254905 L 114.892533914,33.9328334693 L 110.570638077,30.0186009296 L 105.77855082,27.1038282584 L 45.8261616141,5.28294311427 L 42.4173578365,5 L 38.4699586105,5.90445527842 L 32.052758009,9.20892746629 L 27.5657280066,14.812190958 L 5.98425696276,74.1067953296 L 5,80.0272039499 L 6.30451712277,89.0154315325 L 7.73893106868,92.0915421663 L 10.190078445,95.0056246188 L 20.4240912306,99.0497539816 L 22.8759288256,99.6228965537 L 25.071768977,99.1451036811 L 29.7716125184,96.1733246369 L 31.6603247595,94.2003152426 L 51.1378542579,42.4405253991 L 100.224011077,60.2000076187 L 106.691306818,60.8512263284 L 112.655244452,59.0844643481 L 115.637730933,56.4453784476 L 119.570617472,46.8093832488 L 119.938893067,43.7508912861 Z M 116.180467693,41.2123407726 L 116.734611157,45.2450724798 L 115.57174267,48.4400273904 L 113.343080941,44.3299097644 L 110.575823764,41.407190531 L 103.563021341,36.4071303136 L 41.577510384,13.739831592 L 39.0057931842,14.0808164073 L 37.2880910146,15.5839794912 L 14.4753474548,78.2614772976 L 14.1312566554,86.2239895596 L 15.9059651979,94.2127572736 L 11.993458205,92.6823034096 L 9.3802826473,88.7514875267 L 8.04121840085,81.0276991464 L 8.7777695917,74.9107152211 L 30.4618466785,15.3342030632 L 32.9147196015,12.3959358147 L 38.1614502628,9.09111851752 L 42.3651920416,8.0671287436 L 46.2780441439,8.42711266746 L 103.693263274,29.3245434247 L 107.187054423,31.128268294 L 112.038563818,35.3416821818 Z M 112.801724618,54.8810676786 L 111.400132249,56.3928675434 L 108.52059692,57.5795757174 L 102.010462385,57.3384360704 L 51.4207973722,39.0317216216 L 42.3710679478,17.1147784646 L 97.4798943211,36.7470798008 L 104.441911387,40.1323890011 L 108.097730717,42.9528473008 L 112.410644664,48.3536595813 L 113.503383576,51.1989928957 Z M 22.013967233,96.4358882053 L 19.3234057564,94.1795905873 L 17.6585596005,90.2746850473 L 16.9769350792,83.9607807075 L 17.3714661268,78.7834894029 L 39.3205225473,18.771332949 L 48.1653849951,40.0816217382 L 29.3200750978,91.8586851435 L 24.8675922191,96.197509433 Z" fill="#14233b" stroke="none"/>
  <path d="M 116.180467693,41.2123407726 L 112.038563818,35.3416821818 L 107.187054423,31.128268294 L 103.693263274,29.3245434247 L 46.2780441439,8.42711266746 L 42.3651920416,8.0671287436 L 38.1614502628,9.09111851752 L 32.9147196015,12.3959358147 L 30.3934426499,15.5221415874 L 10.2570929889,70.5539271511 L 8.7777695917,74.9107152211 L 8.04121840085,81.0276991464 L 9.3802826473,88.7514875267 L 11.993458205,92.6823034096 L 15.9059651979,94.2127572736 L 14.1312566554,86.2239895596 L 14.4753474548,78.2614772976 L 37.2880910146,15.5839794912 L 39.0057931842,14.0808164073 L 41.577510384,13.739831592 L 103.563021341,36.4071303136 L 111.31894108,41.9969164462 L 115.57174267,48.4400273904 L 116.734611157,45.2450724798 Z" fill="#eeeae4" stroke="none"/>
  <path d="M 112.177796688,55.7181542564 L 113.571442495,52.1815243117 L 112.410644664,48.3536595813 L 108.131932732,42.8588780387 L 104.441911387,40.1323890011 L 96.4462324382,36.3708576432 L 43.3535993638,17.0467195453 L 42.3368659335,17.2087477267 L 51.4207973722,39.0317216216 L 101.916493123,57.3042340561 L 107.819973291,57.7502406798 Z M 101.201701915,47.5728891578 L 99.0393735593,50.2976526487 L 96.4676563595,50.638637464 L 93.2298626536,49.8858480393 L 88.198706406,46.4583902625 L 87.2255019895,43.8693995009 L 88.4139357103,40.8965851287 L 90.8833919764,39.6670381595 L 96.393721534,40.608456327 L 100.177712141,43.369147379 L 101.441461125,45.744634383 Z" fill="#eee9e3" stroke="none"/>
  <path d="M 39.3205225473,18.771332949 L 17.4056681411,78.6895201408 L 16.9769350792,83.9607807075 L 17.6585596005,90.2746850473 L 19.4429402519,94.4359331402 L 22.013967233,96.4358882053 L 24.8675922191,96.197509433 L 29.3200750978,91.8586851435 L 48.1653849951,40.0816217382 Z M 26.5289782343,82.8614756707 L 22.4627347315,81.1686485159 L 21.805985225,77.417824595 L 25.1574375202,69.3793068515 L 26.9691089518,67.9103457819 L 29.5066241373,67.6633302287 L 31.6160964796,70.3466353617 L 32.0251402142,73.9008839776 L 29.5967971966,80.5727015852 Z" fill="#ede9e3" stroke="none"/>
  <path d="M 101.201701915,47.5728891578 L 101.432824344,46.0607441836 L 100.177712141,43.369147379 L 95.4540289133,40.2664361836 L 90.4391108994,39.7181686263 L 88.4139357103,40.8965851287 L 87.5505936804,42.3914565411 L 87.2852692373,43.9975707773 L 88.1047371439,46.4241882482 L 91.0088023781,48.9710304333 L 93.0419241295,49.8174440107 L 97.9884381146,50.5536500922 L 100.039178537,49.5973741282 Z M 98.2458159955,46.9227057761 L 97.3144150463,47.4350457724 L 94.6660021462,47.1096089722 L 91.2748170398,45.0239763166 L 90.5320448335,43.2637804612 L 92.8816214948,42.9483608793 L 97.750749561,45.3590852258 Z" fill="#132135" stroke="none"/>
  <path d="M 30.2241762196,68.0309156054 L 27.0972802282,67.8505785341 L 24.2429650235,70.4298971868 L 21.805985225,77.417824595 L 21.873699035,79.5708259512 L 22.9837115087,81.7839396645 L 26.5289782343,82.8614756707 L 27.9046602605,82.2980052076 L 29.8617765303,80.1370572891 L 32.0251402142,73.9008839776 L 31.9149327183,70.9874917438 Z M 25.4704413367,79.9221730941 L 25.0527608212,76.6840342789 L 26.8139920046,72.4298522519 L 28.2667148404,71.3623334641 L 28.9493746897,74.1648279833 L 27.0855374632,78.7009177965 Z" fill="#15233a" stroke="none"/>
  <path d="M 98.2458159955,46.9227057761 L 97.750749561,45.3590852258 L 92.8816214948,42.9483608793 L 90.5320448335,43.2637804612 L 91.2748170398,45.0239763166 L 94.6660021462,47.1096089722 L 97.3144150463,47.4350457724 Z" fill="#f2ede5" stroke="none"/>
  <path d="M 28.1727455783,71.3281314497 L 25.6428318457,74.770447023 L 24.898679202,77.6921309283 L 25.1885335505,79.8195670511 L 26.0086916758,79.9052446417 L 27.649698145,77.7356599423 L 29.0606175136,73.5668103965 Z" fill="#f5f1eb" stroke="none"/>
</g>
<g id="kit-p07" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
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
<g id="kit-p08" fill="none" stroke="#1F2A3A" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
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
</defs></svg>
````
