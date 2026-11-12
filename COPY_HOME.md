# Home page copy (use these words exactly; {braces} are filled from the API)

Rules: plain English a newcomer understands without help; no jargon ("recipe", "condition", "pass^k", "tolerance", "px") on the home page; every sentence stays true whatever the final numbers are; numbers always say what they count. {models}, {kits} and {trials} are counted from the submitted results (settings B, A and C only), not from the configured lists.

## Names used everywhere on the home page
| Internal | Shown to readers |
|---|---|
| condition C | **Joints listed** (we name every connection to make) |
| condition A | **Joints not listed** (part names given) |
| condition B | **Joints not listed, parts unnamed** |
| full pass | **built correctly** (every check passed: every joint made, every part facing the right way, nothing missing or mirrored) |
| trial | **build** |
| kit | **kit** |
| failure: wrong connection (far off) | **Part in the wrong place or turned wrong** |
| failure: near miss | **Almost right** (every miss small, at least one just outside the allowed margin) |
| failure: missing / extra / mirrored / scaled part | **Part missing, doubled, mirrored or resized** |
| failure: no answer before token cap | **Hit the length limit before answering** |
| failure: unusable output | **Answer could not be read** |

## Nav
Kit Assembly · Overview · Failures · Results · Kits · Method · [Run it yourself]

## Hero
- Eyebrow: **AN AI BENCHMARK**
- Headline: **Can AI put a machine together from its parts?**
- Subline (desktop): We gave {models} AI models the loose parts of {kits} kits, from a road bike to a wheelbarrow, and asked them to put each one together. When we listed every joint, the best model built **{C}%** correctly. When we didn't, the best managed **{A}%**. With the part names hidden too, **{B}%**.
- Subline (phone): {models} AI models, {kits} kits of loose parts. Best result: **{C}%** built correctly with the joints listed, **{A}%** without, **{B}%** with the part names hidden too.
- Left drawing caption (coral): **{Part} in the wrong place · {err} pixels off** (angle checks: **{Part} turned {err}° wrong**)
- Left drawing note (grey): {Model display name}, {setting name}
- Right drawing caption: **A correct assembly**
- Phone toggle: **Show a correct assembly**

## How the test works
- Title: **How the test works**
- Intro: Every build follows the same four steps.
- 1 **The parts**: Every part arrives on its own, most of them turned away from how they sit in the finished machine.
- 2 **The request**: bubble: "Assemble a working {object}." Caption when the story's setting is A or B: The request also explains how the build will be checked, but gives no positions and no list of which part joins which. Caption when it is C: The request lists every connection to make, but gives no positions or angles.
- 3 **The AI's assembly**: The model replies with one picture that places each part: moved and turned, never redrawn.
- 4 **The check**: Code checks every joint, the way each part faces, and that nothing is missing or mirrored. Stamp: **FAIL** or **PASS**. Caption: {n} of {m} checks failed. Mini bars title: This model's builds of the {object}, by setting:

## Results
- Card labels: **Joints listed** / **Joints not listed** / **Joints not listed, parts unnamed**
- Card number: the best model's share built correctly, e.g. **{86}%**
- Card note: Best model: {Model}, {passes} of {trials} builds correct (ties: Top score, shared by {Model} and {Model2})
- Chart title: **Each model in all three settings**
- Chart intro: Share of builds assembled correctly. Each model is shown only on kits it built the same number of times in all three settings, so these figures can differ from the cards above.
- Axis: Share built correctly
- Value labels: {67}% ({6} of {9})

## How models fail
- Title: **How models fail**
- Intro: Every failed build, grouped by its main problem. Use the selector to see one setting.
- Axis: Failed builds
- Legend: the five reader names from the table above.

## The mistakes models make most
- Title: **The mistakes models make most**
- Intro: Counted across all settings. Each picture shows the worst case. Red: where the model put the part. Green: where it belongs.
- Card caption: **{Part} in the wrong place** · in {trials} builds · typically {median} pixels off (degrees for angle mistakes; full check text as tooltip)
- Link: **See every failed build →**

## Footer
Every build is checked by code: each joint, the way each part faces, and that nothing is missing · {trials} builds · {kits} kits · {models} AI models
