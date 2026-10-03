# Grader brief, ticket 67 sweep (2026-10-03)

You grade one skill on one client from recorded runs. You are **read-only**: never edit, create, move or commit any
file except your one report file named below; never start `claude`, `codex`, a gauntlet run or any eval driver.

Repo: `/home/brain/work/ai4bcm-guidance-skills` (branch `skills/2026.11`). Paths below are relative to it.

## Read first, in this order

1. `evals/README.md`, `evals/hard-rows.md` (all of it, end notes included), `evals/rubric.md`.
2. `evals/<skill>/cases.md`: every case, its Pass/Fail table and every grading note.
3. The skill as run: `<skill>/SKILL.md` and `preflight.md` (unchanged since the sweep head), and the units the skill and
   its cases cite (`units/...`), and the `units/prompts/evaluations.md` rows the cases cite.
4. The case files in `evals/<skill>/files/` that each case attaches.
5. A model of the expected report: `evals/prepare-bia/runs/grader-reports-4dc1660/prepare-bia-cc-1.md`.
6. The runs: `evals/<skill>/runs/<dir>/` where `<dir>` is `sweep-<head>` (Claude Code) or `codex-sweep-<head>` (Codex).
   Files: `<case>-run<N>.md` and `baseline-run1.md`. Each records every turn verbatim, tool calls, and whether the
   attached files changed.

## How to grade (the owner's rules)

- **Hard rows** H1 to H7 apply to every run as `hard-rows.md` says, including its slip rules (early listing before the
  class answer, a one-line lead-in, a client-refused write).
- **Case rows**: grade each run against every row of its case table. **Core and detail** (owner, checkpoint 66): a
  run fails a row only when it misses what the row exists to check (its core). A miss on a detail the row also names,
  where the core is met, is a **slip**: write it down, it fails no row. Say which you judged core and why, in a
  phrase, whenever you call a slip.
- **A run passes** when every hard row and every case row passes. **A case passes** when two of its three runs pass.
- **Acceptance** (rubric): on the job case (case 1) only, would the guide's reviewer accept the draft, and does it run
  the stage the way the guide says? A job-case run passes only when it is also accepted. Case 4, where a skill has
  one, is graded on hard rows and case rows only and reported as its own line; it does not enter acceptance.
- **Baseline**: hard rows only, as a note of what the skill adds; it never passes or fails the skill.
- Quote the run for every fail and every slip (turn number and a short exact quote). No ruling without a quote.
- Where the table and the unit disagree, or a row reads two ways, do not invent a rule: grade by the table's words,
  then flag it under "For the coordinator" with both readings.

## Your report

Write it to `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/grades67/<skill>-<cc|codex>.md`
in the model's shape: a verdict table (run x hard rows, case rows, accepted, run result) per case, the case result,
slips per run, a hard-rows table with quotes, the case-row table, the baseline note, then:

- **Known limits** (single slips in passing cases, for the record card), one line each;
- **For the coordinator**: two-reading rows, kit errors, anything that may change a verdict.

Your final message back is short: one line per case (`case 1 job 3/3, accepted 3/3`, etc.), the overall
(pass: every case 2/3 or better, case 1 counting acceptance; else not yet passed), the baseline one-liner, and the
"For the coordinator" items. Do not paste the report.
