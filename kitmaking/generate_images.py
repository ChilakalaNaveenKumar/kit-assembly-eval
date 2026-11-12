"""Same image model and same style prompt as the bike drawing, two steps per machine:
1) every part alone in its own box; 2) the full machine in one box, built from exactly those parts."""
import os, threading; threading.stack_size(64 * 1024 * 1024)
import concurrent.futures as cf, io, pathlib
from google import genai
from google.genai import types
from PIL import Image
D = pathlib.Path(__file__).resolve().parent / 'flat'; D.mkdir(exist_ok=True)
G = genai.Client(vertexai=True, project=os.environ["GOOGLE_CLOUD_PROJECT"], location="global")
STYLE = ("Hairline technical line-art: every part outlined with ONE thin, even, dark navy line (#1F2A3A, about 3 px, round ends), "
         "every part a closed outline filled with ONE flat pale colour from this palette only: pale blue #DBEAF7, pale green #DFF1E3, "
         "pale yellow #FDF1C9, pale coral #FBE1DC, pale lavender #EBE3F7, pale grey #ECEAE4; background plain warm white #FAF8F3. "
         "No shading, no gradients, no shadows, no texture, no hatching, no thick or varying lines, no text, letters or numbers. "
         "Every separate part is its own complete closed shape; parts that move are drawn whole and in front, never hidden behind other parts.")
SUBJECTS = {
 "scale": "An old balance scale, strict flat side view: a base, a vertical pillar, a beam pivoting on a pin through the pillar top, a pointer hanging from the pivot, and at each beam end a hanger: a rigid stirrup bar hooked into the beam end that holds a round pan by its rim (left pan, right pan).",
 "wheelbarrow": "A wheelbarrow, strict flat side view: a steel tray, one handle frame running from the grip to the wheel, a wheel with its hub, the wheel fork holding the axle, one leg stand under the tray, bolted together at visible bolt holes.",
 "hand_pump": "A cast-iron hand water pump, strict flat side view: a base plate, the pump body, a spout coming out of the body, a cap on top, a long curved handle lever, a short link bar joining the handle to the cap, and the piston rod hanging from the handle, all joined at visible pin holes.",
 "desk_lamp": "A desk lamp with an arm linkage, strict flat side view: a round base, a base bracket, a lower arm, an upper arm, an elbow joint plate joining them, a head bracket, a cone lamp shade and a bulb, all joined at visible pin holes.",
}
CFG = types.GenerateContentConfig(response_modalities=["IMAGE"], image_config=types.ImageConfig(aspect_ratio="16:9", image_size="2K"))
def img(r): return next(p.inline_data.data for p in r.candidates[0].content.parts if p.inline_data and p.inline_data.data)
def one(k):
    parts = ("Parts sheet. " + SUBJECTS[k] + " Draw every one of these parts separately: a grid of boxes with thin grey borders, each box holding exactly one part, "
             "alone and centred, drawn exactly as it sits in the working machine (same flat side view, same orientation). One box per part, one box per copy. "
             "Do not draw the assembled machine.\n" + STYLE)
    a = img(G.models.generate_content(model="gemini-nano-banana-2.1", contents=parts, config=CFG))
    Image.open(io.BytesIO(a)).convert("RGB").save(D / f"{k}_parts.png")
    full = ("The attached picture shows every part of the machine, one part per box. Draw the assembled machine, large and centred, built from exactly "
            "these parts and nothing else: every part used once (twice only if it has two boxes), each with exactly the same shape, size and colour as in "
            "its box, joined at its pin holes, hooks and edges. " + SUBJECTS[k] + "\n" + STYLE)
    b = img(G.models.generate_content(model="gemini-nano-banana-2.1", contents=[types.Part.from_bytes(data=a, mime_type="image/png"), full], config=CFG))
    Image.open(io.BytesIO(b)).convert("RGB").save(D / f"{k}_full.png"); return k
with cf.ThreadPoolExecutor(4) as ex:
    for k in ex.map(one, SUBJECTS): print(k, flush=True)
