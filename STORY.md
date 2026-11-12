# The story: what this eval tests and why

By Naveen Kumar Chilakala.

## The job
People who make technical pictures keep libraries of reusable drawn parts and build new pictures by
assembling them. They do this every day:
- instruction-manual and repair-guide writers;
- technical illustrators (service manuals, spare-parts catalogues, patent drawings);
- teams building product configurators for shopping sites;
- engineering and science teachers and e-learning teams;
- game and animation artists with modular kits.
Wheels, frames, cylinders, gears and pulleys are each drawn once and reused.

The obvious thing to hand to AI is the assembly step itself: "here are the parts, build me a working
hand pump". A human practitioner does this by recognising each part, knowing how the real machine goes
together, and lining up the holes.

## The question
Given only a kit of SVG parts and the name of the object, can a frontier model assemble a working object,
where every real connection is made at the right holes and every part faces the right way?

Nobody tells the model which hole goes on which hole, and nobody gives it positions or angles.
It must work that out from the parts, as a practitioner would.

## Why it matters
A wrong assembly is a wrong technical picture: a pump handle pinned to the wrong hole, a wheel off its axle,
a chain that misses the sprocket. It looks plausible at a glance and teaches the wrong thing. If the
assembly cannot be trusted, every picture needs a human to check every joint, which defeats the purpose.

## What we measure
- Input: one fixed prompt template + the kit (parts stored at arbitrary rotations) + the object's name.
- Output: one SVG placing every part.
- Pass: every connection the real object has is made (matching holes or features coincide within a stated
  tolerance), the object stands level where it stands on the ground, and nothing is missing, mirrored or scaled.
- Score: the fraction of connections made. Reliability: pass^k over repeated trials.

## Conditions
| Condition | The model gets | Purpose |
|---|---|---|
| A: named parts, no recipe | Part ids that name the part, plus "assemble a working X" | Headline |
| B: unnamed parts, no recipe | Part ids p01..pNN, plus "assemble a working X" | Raw parts, as they come out of a vectorizer |
| C: full recipe (control) | Every connection spelled out | Shows the model can place parts when told how |

If models pass C but fail A and B, the limitation is not drawing or arithmetic: it is knowing how the
object goes together and recognising which part is which.

## The kits
Six objects with 6 to 11 parts each: road bike, pulley hoist, hand water pump, desk lamp, balance scale,
wheelbarrow. All six are in one flat line-art style:
- the bike and pulley come from Naveen Kumar Chilakala's own illustration work;
- the other four were drawn for this eval by an image model, part by part, vectorized with Naveen Kumar
  Chilakala's vectorizer, and combined at their own holes and edges (`kitmaking/`).

## Models
claude-opus-5-5, claude-sonnet-5-5, claude-haiku-5-5, all through Google Vertex AI with the same settings
(max 128,000 output tokens, adaptive thinking, effort high).
