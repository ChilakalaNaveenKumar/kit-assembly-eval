# Rules: checked file by file before submission

Each rule says how it is checked. All must hold; any failure blocks submission.

## Prompts
- R1 One template per condition (A, B, C; an A_alt rewording exists in the code but is not part of the submitted run), as string constants in one file. Per kit only the slots
  change: part count, object name, canvas size, base part id, tolerances ({upright_tol} is a slot), kit SVG.
  Condition C also fills a per-kit {checks} slot (the recipe).
  Check: read templates.py; diff two kits' prompts and confirm only slot values differ.
- R2 Every model gets the same prompt bytes for the same kit and condition.
  Check: the prompt SHA-256 stored in each result is identical across models.
- R3 Conditions A and B contain no recipe: no list of connections, no positions, no angles, no
  orientation hints. Check: read the filled A and B prompts for every kit.

## Kits
- R4 Every attach point is a visible feature (hole, axle, hub centre, drawn edge, the centre of a drawn circular arc such as a chain's rounded end) on both mating parts.
  Check: kit images with attach points marked, one per kit.
- R5 Congruent parts (the scale's two pans and two stirrups, the bike's two wheels) are declared INTERCHANGEABLE and graded as swappable; no other two parts in a kit are congruent. Check: the kit files and tests/test_grader.py.
- R6 The correct assembly is unique up to the freedoms a working object really has: moving the whole object, wheels spinning on their axles, jointed parts in any pose their pins allow (the desk lamp's arm, the pump's handle stroke), a part that may sit anywhere along an edge or centre line (the lamp and pulley brackets, the pump's piston rod), and the scale's stirrups hung by their hook or pinned through their rod hole.
  Check: tests cover valid alternatives (must pass) and wrong folds or swaps (must fail).
- R7 Kit build is deterministic: rebuilding gives byte-identical kit and reference files.
  Check: rebuild and compare hashes.
- R8 Kit artwork lives inside the project. No task file reads from a path outside the project.

## Grader
- R9 The reference solution passes every check in every condition.
- R10 Wrong answers fail: each part shifted, rotated, reversed end-for-end, mirrored, scaled, duplicated,
  missing, or swapped with another part. Check: tests/test_grader.py, run with pytest, all green.
- R11 Valid alternatives pass: whole object moved, wheels spun on their axles, other equivalent
  transform encodings (nested groups, rotate-about-point, matrix).
- R12 The grader judges only where the parts land, never how the transforms were written.
- R13 Everything the grader checks is stated in the prompt (the connection principle and tolerances).

## Runs
- R14 Models exactly: claude-opus-5-5, claude-sonnet-5-5, claude-haiku-5-5, all through Google Vertex AI, with the same settings for every call (max 128,000 output tokens, adaptive thinking, effort high), recorded in every result file. The harness also supports Gemini models, which are not part of the submitted run.
- R15 Every trial is a fresh single-turn call with no shared history.
- R16 Every result file stores: model id, condition, kit, trial, date, settings, prompt hash, full output,
  grade, tokens, seconds.
- R17 A failed API call is retried and never recorded as a model failure.

## Numbers
- R18 Every number in the README, description and video comes from summarize.py output. None typed by hand.
- R19 Re-grading the saved outputs with no API keys reproduces the summary exactly.

## Safety and cleanliness
- R20 No secrets anywhere: no keys, no .env file in the package. Check: grep for key prefixes.
- R21 No machine details: no home-directory paths, machine user names, cloud project ids, employer names. The author's name appears only as the author credit.
- R22 No tool signatures: no "generated with", co-author lines or assistant names in code, comments or commits.
- R23 Comments are at most 2 lines and explain why, not what.
- R24 requirements.txt pins the versions actually installed and used.

## Package
- R25 ZIP under 50 MB, no videos, no .env. Contains README, tasks, reference solutions, grader,
  harness, tests, results, transcripts, requirements.txt, .env.example.
- R26 README covers every section the guide lists: what it tests, who relies on it, tasks, grading and
  grader validation, how to run, results with models, settings and dates, cost and runtime, provenance,
  transcripts, main failure mode, AI use. (The guide requires the AI-use section; the author writes it.)
- R27 Representative transcripts: at least one failing transcript per kit for every model that failed it.
- R28 Prior work cited and the difference stated.

## Final check
- R29 After the build, every file is read line by line against R1-R28, and the result is recorded in
  CHECK_REPORT.md with pass/fail per rule and the evidence.
