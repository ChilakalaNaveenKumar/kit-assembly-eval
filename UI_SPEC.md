# Dashboard UI spec

The dashboard is how judges and readers see the results. Every element below is checked in QA (screenshots at 1440, 1024 and 390 px wide, light and dark, plus scripted clicks). Zero display defects is the bar.

## Principles
1. **Failures first.** The first thing on every page is what went wrong, then how much help fixes it.
2. **Show the mistake, not just the number.** Every failure is shown as an annotated close-up: a red ring where the part landed, a green ring where it belongs, an arrow between them and the error in px.
3. **Everything is interactive.** Charts are Apache ECharts (vendored at `web/vendor/echarts.min.js`): hover tooltips, clickable legends that toggle series, click a bar or cell to drill into the trials behind it.
4. **One source of numbers.** The page only formats what the JSON endpoints return; every endpoint serialises `kitbench.stats`. No statistics are computed in JavaScript.
5. **Calm, modern, professional.** Light theme by default with a dark toggle; system font stack; generous whitespace; no heavy borders; subtle shadows; motion that explains (never decorative loops).

## Files
- `web/index.html`, `web/app.css`, `web/app.js`, `web/vendor/echarts.min.js`. `dashboard.py` serves them as static files and keeps all JSON and SVG endpoints. No inline script blocks in Python strings.

## Formats (used everywhere, no exceptions)
| Value | Format | Example |
|---|---|---|
| pass rate | integer percent, with counts where space allows | `67%` · `67% (2/3)` |
| score | two decimals | `0.81` |
| position error | one decimal + px | `122.3 px` |
| angle error | one decimal + ° | `15.0°` |
| tolerance | as stored + unit | `8 px`, `8°` |
| tokens | thousands separator | `37,981` |
| seconds | integer + s | `304 s` |
| cost | `$` + two decimals, `n/a` when unpriced | `$0.28` |
| model | display name, id in tooltips and tables | `Claude Opus 5.5` (`claude-opus-5-5`) |
| condition | letter + short name | `B · Unnamed parts`, `A · Named parts`, `C · Full recipe` |
| kit | title case | `Truss bridge` |

Model display names: claude-opus-5-5 → Claude Opus 5.5; claude-sonnet-5-5 → Claude Sonnet 5.5; claude-haiku-5-5 → Claude Haiku 5.5; gemini-3.1-pro-preview → Gemini 3.1 Pro; gemini-3.8-flash → Gemini 3.8 Flash.
Condition order is always B, A, C (hardest first), then A_alt where shown.

## Colour
- Models: categorical slots 1-5 from the dataviz palette in `kitbench.models.MODELS` order (blue, orange, aqua, yellow, magenta; dark-mode steps for dark). A model's colour never changes.
- Conditions: ordinal blue ramp B dark → C light (light: `#184f95`, `#3987e5`, `#86b6ef`; dark: `#cde2fb`, `#5598e7`, `#1c5cab`).
- Failure types: `#e34948` wrong connection, `#6250d6` near miss, `#008300` missing/extra/mirrored/scaled, `#0a8fb0` no answer before token cap, `#b0701f` unusable output (dark: `#e66767`, `#9085e9`, `#008300`, `#1a9ec2`, `#b8732a`).
- Status: pass `#0ca30c`, fail `#d03b3b`, always with an icon and a label.

## Pages (hash routes: `#overview`, `#failures`, `#results`, `#kits`, `#method`, `#run`; back/forward and direct links work)

### Overview
1. **Hero.** Title "Can AI assemble a working machine from a kit of parts?" and one generated sentence with the headline numbers. Beside it, the most striking failure (largest error among the most common mistake): the model's assembly and the correct one side by side, each with its annotated close-up, and a "Replay assembly" button.
2. **Three stat tiles,** B, A, C: best model's full-pass rate (counts up on load), all-model mean, trials. Clicking a tile opens Results filtered to that condition.
3. **Difficulty ladder** (ECharts horizontal grouped bar): one group per model, bars B/A/C on matched kits (`ladder_matched`), value labels on bars, legend toggles conditions, tooltip shows passes/trials and kits compared, clicking a bar opens that model's trials in that condition.
4. **What goes wrong** (ECharts horizontal stacked bar): failure types per model, condition selector, legend toggles types, click a segment to open the Failures gallery filtered to that model and type.
5. **Most common mistakes:** cards with the check in plain words, kit, trials, median error, which models, and the annotated close-up of the worst example; click opens the trial.
6. **Per-kit heatmap** (ECharts heatmap): kits × models, full-pass rate, `passes/trials` in each cell, condition selector, click a cell to open its trials.

### Failures
Filter row (condition, model, kit, failure type) and a grid of cards: annotated close-up of the first failed check, model, kit, condition, score, failure type, number of failed checks. "Show more" paging. Click opens the trial.

### Trial view (drawer or page, reachable from everywhere, with its own hash `#trial/<cond>/<kit>/<model>/<trial>`)
- Header: PASS/FAIL with icon, score, failure type, condition, model, kit, tokens, seconds.
- **Before/after slider** between the model's assembly and the correct one.
- **Replay:** parts start where the kit stores them and move to where the model placed them (about 1.5 s, eased); on arrival the failed joints pulse red and the correct positions show as green ghosts.
- Failed checks table: check text, error vs tolerance with a small bar, and each row's annotated close-up.
- Raw reply, collapsed, rendered as text only.

### Results, Kits, Method, Run live
Same data and guarantees as today, restyled to the same system. Results tables use the formats above and do not repeat the condition name under the heading.

## Motion
- Charts: ECharts entry animation (bars grow, about 600 ms), re-animate on filter change.
- Stat tiles count up once on first view.
- Replay animation as above; respects `prefers-reduced-motion` (show end state, no movement).
- No continuous or looping animation.

## Empty and loading states
Every chart and list has a loading skeleton and a written empty state ("No finished trials for this condition yet").

## Accessibility
Keyboard reachable controls, visible focus, `aria-label` on charts, table view for every chart, contrast of text ≥ 4.5:1.

## Security (unchanged)
127.0.0.1 only; model output only ever as `<img src>` of a server-sanitised SVG or as text; keys only in memory; live runs in `results_live/`.
