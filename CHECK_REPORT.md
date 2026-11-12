# Final check against RULES.md

Checked on 2026-11-08 after the final run (162 builds) and the final regrade. Each rule lists the result and the evidence.

| Rule | Result | Evidence |
|---|---|---|
| R1 One template per condition, only slots change | Pass | `kitbench/templates.py` holds the A, B and C templates as constants; per kit only the listed slots are filled (`fill()`). |
| R2 Same prompt bytes for every model | Pass | Across the 18 kit/condition pairs, every stored `prompt_sha256` is identical for the three models (0 pairs with more than one prompt). |
| R3 No recipe in A and B | Pass | The A and B templates state only the grading principle; the joint list (`{checks}`) is filled only in C. |
| R4 Attach points on visible features | Pass | `review/joints/<kit>.png` circles every graded point; AI review plus Naveen Kumar Chilakala's manual review (`review/zoom_review.md`). |
| R5 Congruent parts declared interchangeable | Pass | The bike's wheels and the scale's pans and stirrups are `INTERCHANGEABLE`; tests swap them. |
| R6 Unique up to real freedoms | Pass | Free poses, edge and centre-line contacts, any-hole plates and the scale stirrups each have passing and failing tests in `tests/test_grader.py`. |
| R7 Deterministic kit build | Pass | Rebuilding every kit gives byte-identical `kit.json` (hash compared). |
| R8 Artwork inside the project | Pass | Every `tasks/<kit>/task.py` holds its own shapes or reads `tasks/<kit>/art/`; no outside paths. |
| R9 Reference passes every check | Pass | `python run_eval.py --oracle`: every kit passes in A, B and C. |
| R10 Wrong answers fail | Pass | `python -m pytest -q tests`: 187 passed (shifted, rotated, reversed, mirrored, scaled, duplicated, missing and swapped parts all fail). |
| R11 Valid alternatives pass | Pass | Tests: moved whole object, spun wheels, re-posed lamp, slid brackets, stirrup hung either way, nested groups and matrix encodings. |
| R12 Grader judges placement only | Pass | `kitbench/grader.py` composes every transform to world positions before checking. |
| R13 Everything checked is stated in the prompt | Pass | The A/B text states the grading principle and tolerances; C lists every check. The upright limit uses its own 3-degree value in every condition. |
| R14 Models and settings | Pass | All 162 results have the same settings: Claude Opus/Sonnet/Haiku 5.5, Google Vertex AI, max 128,000 tokens, adaptive thinking, effort high. |
| R15 Fresh single-turn calls | Pass | `run_eval.py` sends one user message per build with no history. |
| R16 Result fields | Pass | Every result stores model, condition, kit, trial, date, settings, prompt hash, output, grade, tokens and seconds. |
| R17 API errors never recorded as model failures | Pass | API errors are retried and excluded; the final summary shows 0 API errors. |
| R18 Numbers from summarize.py | Pass | README numbers come from `results/summary.md`; `python scripts/summarize.py --check` matches. |
| R19 Regrade reproduces the summary with no keys | Pass | `python scripts/regrade.py`: 162 re-graded, 0 differ. |
| R20 No secrets | Pass | Scan for key prefixes finds none outside model thinking signatures; no `.env` in the package. |
| R21 No machine details | Pass | No home paths, machine user names or project ids in shipped files (only in the scanners' own patterns). The author's name appears only as credit. |
| R22 No tool signatures | Pass | No "generated with" or co-author lines in code or docs (matches are the rule text and the models' own words in transcripts). |
| R23 Comments at most 2 lines | Pass | Scan of every `.py` file: no comment block over 2 lines. |
| R24 Pinned requirements | Pass | `requirements.txt` pins the installed versions, including Vertex, OpenCV and Pillow for `kitmaking/`. |
| R25 ZIP contents and size | Pass | `python scripts/make_zip.py`: README, tasks, reference solutions, grader, harness, tests, results, raw replies, transcripts, requirements, `.env.example`; under 50 MB; no videos, no `.env`. |
| R26 README sections | Pass | README covers what it tests, who relies on it, tasks, grading and validation, how to run, results with models/settings/dates, cost and runtime, provenance, transcripts, main failure modes and AI use. |
| R27 Representative transcripts | Pass | All 162 builds have a transcript in `transcripts/`, including every failing one. |
| R28 Prior work cited with the difference | Pass | README "Prior work": 8 works with arXiv ids and one line on the difference each. |
| R29 This report | Pass | This file. |
