# How the four new kits were made

Designed and built by Naveen Kumar Chilakala.

The hand pump, desk lamp, balance scale and wheelbarrow kits were made in five steps. The bike and pulley kits come from Naveen Kumar Chilakala's earlier drawings and are described in the main README.

1. **Drawing.** `generate_images.py` asks an image model for each machine twice, using the same flat-line style prompt as the bike drawing: first every part alone in its own box (`source_images/<m>_parts.jpg`), then the assembled machine built from those parts (`source_images/<m>_full.jpg`). Running it needs `GOOGLE_CLOUD_PROJECT` set.
2. **Cropping.** `crop_parts.py` finds each box and crops the part inside it.
3. **Vectorizing.** Each crop was converted to SVG with Naveen Kumar Chilakala's own vectorizer (a separate project, not included here). The resulting part SVGs are in `part_svgs/<m>/`.
4. **Combining.** `kitlib.py` clips each part SVG to its own outline, so no box background shows. `assemble_<m>.py` places every part at its own joint features (a hole on a hole, a hook in an eye, an edge flush on an edge). The image model drew some parts at inconsistent sizes, so a part may be resized evenly once, never stretched or redrawn. The combined machine, not the image model's full picture, is the ground truth.
5. **Task.** `to_task.py` turns the combined machine into `tasks/<m>/task.py`. It keeps every vectorized shape in its assembled position, fits the machine to the 1376 x 768 canvas, and uses the joint points as the grader's anchors.

These scripts read the crops and part SVGs from a working folder, which is not included because it is large. They are here to show exactly how each kit was built.
