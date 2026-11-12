# Home page design: editorial (approved)

Approved mockups, the target to match (compare side by side in QA):
- wide desktop top: `../qa/mockups/edit_desk_top.png`
- wide desktop lower half: `../qa/mockups/edit_desk_bottom.png` (its content column is too narrow; use the 1280 px column below instead)
- original full page: `../qa/mockups/a_editorial_light_1.png`, section crops `../qa/mockups/crop_*.png`
- tablet: `../qa/mockups/edit_tablet.png`
The phone mockup is not a real phone layout; the phone layout is specified below.

Every word and number on the page comes from the API. The mockup's numbers are placeholders.

## Tokens
| Token | Light | Dark |
|---|---|---|
| page background | `#F4EAE2` warm paper, with a very faint radial lighter wash behind the hero | `#1B1614` warm charcoal |
| card surface | `#FBF3EE` → `#F8E5DD` soft top-to-bottom gradient | `#272020` → `#2E2523` |
| card shadow | `0 1px 0 rgba(255,255,255,.7) inset, 0 10px 30px rgba(120,60,40,.10)` | `0 10px 30px rgba(0,0,0,.45)` |
| ink | `#1F1918` | `#F4EAE2` |
| ink 2 | `#5B504C` | `#CBBFB8` |
| muted (≥4.5:1) | `#6E625D` | `#A89C96` |
| rule | `#E4D6CC` | `#3A302C` |
| accent coral | `#D9543F` (text and outlines), `#E8705C` fills | `#F07A63` |
| pass / fail | `#0ca30c` / `#d03b3b`, always with icon + label | same |
| ladder B / A / C | `#DE9481` / `#C9604B` / `#9F3A28` | `#A24A39` / `#D9725C` / `#F4B7A6` |
| failure types | `#e34948` wrong connection, `#6250d6` near miss, `#008300` missing/extra/mirrored/scaled, `#0a8fb0` no answer before token cap, `#b0701f` unusable output | `#e66767`, `#9085e9`, `#008300`, `#1a9ec2`, `#b8732a` |
| drawings | on their own cream canvas; in dark mode inside a card with an 8 px warm inset frame so no white block glares | |

Model colours (`--s1..--s5`) stay as they are for other pages.

## Type
Fonts are bundled: `web/vendor/fonts/fonts.css` (Source Serif 4 and Roboto Condensed, variable). Load that file from index.html.
- Display serif (Source Serif 4, 700): hero headline 64/70 desktop, 44/50 tablet, 32/38 phone; stat numbers 88/88 desktop, 64 tablet, 56 phone.
- Section titles (Roboto Condensed 700): 34/40 desktop, 28 tablet, 24 phone.
- Step titles and card titles (Roboto Condensed 700): 22/28.
- Body and sublines (Roboto Condensed 400): 22/32 hero subline, 17/26 body, 15/22 captions, 13/18 axis labels.
- Numbers in charts: tabular figures.

## Layout (desktop ≥ 1200 px: centred 1280 px column, 48 px side padding; tablet 768–1199; phone < 768)
1. **Nav** (72 px): left logo (gear-with-wrench mark in coral + "Kit Assembly" in Roboto Condensed 700, 26 px); right: tabs Overview · Failures · Results · Kits · Method separated by middle dots, then "Run live" as a coral outline pill, then the theme toggle (half-filled circle icon). Thin rule under the nav. Tablet: tabs in a horizontally scrollable row under the logo line. Phone: logo + hamburger that opens a full-width sheet with the tabs, Run live and theme toggle.
2. **Hero**: centred serif headline "Can AI build a working machine from a box of parts?" and one subline with the three numbers in bold: "Told exactly how, the best model gets **C%** right. Asked to work it out, **A%**. With unlabelled parts, **B%**." (best model per condition from the API; if the best models differ, keep the sentence true by naming the stat "the best model" generically). Below: the most striking failure as two large drawings side by side, the model's assembly (left) with the red landed ring, green expected ring and a curved coral arrow, caption in coral "<check in plain words> · <err> px off" plus a small grey "<model> · <condition short name>"; right: the correct assembly aligned to the model's base part, caption "Correct assembly". Drawings have no card frame on desktop light (they sit on the paper). Phone: one drawing with a toggle "Show the correct one" that cross-fades.
3. **How the test works**: section title, then 4 columns (2x2 tablet, 1 column phone). Each step: illustration on top, number + bold title, one-line caption.
   1. "The kit (loose parts)": the loose kit image of the same kit.
   2. "The instruction": a speech bubble "Assemble a working road bike." and the caption "No coordinates, no list of which hole goes where."
   3. "The model's answer": the model's assembly, small.
   4. "The verdict": a rotated stamp "FAIL" (coral, double border) or "PASS" (green), the caption "<n> of <m> connections wrong → fail", and three mini bars B / A / C with that model's full-pass rates.
4. **Results row** (desktop two columns 5/7; tablet and phone stacked): left, stat cards B and A side by side, C full width under them (big serif number, label "B · Unlabelled parts", coral progress bar, "best model <name> (<passes>/<trials>)" small); right, "Difficulty ladder": legend chips B · Unlabelled parts, A · Named parts, C · Full recipe, then ECharts grouped horizontal bars per model (labels on the left, value labels at bar ends "67% (6/9)", x axis 0–100% with light gridlines and axis name "Full-pass rate"). Bars clickable → Results.
5. **What goes wrong**: full width; ECharts stacked horizontal bars per model with the legend as an HTML list on the right (below on phone), axis name "Failed trials". Segments clickable → Failures.
6. **Most common mistakes**: 3 cards (1 column phone): rounded 16 px, shadow; inside, the annotated close-up in a framed window (1 px rule, 10 px radius); caption below "<short check> · <trials> trials · <err> px". "See all mistakes →" link to Failures.
7. **Footer**: rule, then centred "Graded by code at every visible hole · <trials> trials · <kits> kits · <models> models" from the API.

## Motion (all disabled by prefers-reduced-motion)
- Sections fade and rise 16 px on first scroll into view, 500 ms, 60 ms stagger between items.
- Hero: drawings fade in; then the red ring scales from 1.4 to 1 with an ease-out and the arrow draws (stroke-dashoffset) over 600 ms; the caption fades in last.
- Stat numbers count up over 900 ms when first visible; progress bars grow from 0.
- FAIL stamp: scale 1.3 → 1 and rotate −12° → −8° with a short settle when visible.
- Charts: ECharts grow-in animation on first view.
- Hover: cards lift 2 px with a deeper shadow; buttons darken; focus rings coral 2 px.

## Acceptance
- Side-by-side with the mockups at 1920 and 1440: same structure, hierarchy, type, colours, spacing feel.
- 1440, 1024, 390 px in light and dark: no overlap, no clipped text, no horizontal overflow, no console errors, no broken images.
- Every number matches `/api/overview`.
