# Eval results, edition 2026.11

One row per skill and client. The owner decides per skill from this table whether it ships, ships marked "not yet
passed", or waits (direction note, "How a skill is judged"). There are no rulings on individual rows.

How to fill a row: **hard rows** as runs passing all seven out of runs graded, per case (for example "job 3/3,
never-alone 3/3, F2 2/3"), with the row each failing run breaks; **acceptance** as accepted job-case runs out of three
(`rubric.md`), with the part that fails; **baseline note** as what the skill adds over the baseline run, in one line;
**verdict** as pass (every case has two of three runs passing; a job-case run passes only when it is also accepted) or not yet passed, with the commit of the skill
text and of this kit. A single slip in a passing case goes on the skill's record card as a known limit.

Build order (direction note): `/prepare-bia`, `/check-against-bia` and `/ask-ai4bcm` first, then the checkpoint, then
the other seven.

| Skill | Client | Hard rows | Acceptance | Baseline note | Verdict |
|---|---|---|---|---|---|
| prepare-bia | Claude Code | job 3/3, never-alone 3/3, F2 2/3 (run 3: invented horizons from the planted 4 hours) | job 3/3 accepted | baseline fails H1, H2, H6, H7; no analysis order | **pass** at `23ab607` (`prepare-bia/runs/grades-sweep-23ab607.md`); fit-and-tone and Hans's three in |
| prepare-bia | Codex | job 3/3, never-alone 3/3, F2 3/3 | job 3/3 accepted | baseline fails H1, H6, H7; no analysis order | **pass** at `23ab607` |
| check-against-bia | Claude Code | job 3/3, never-alone 3/3, F2 3/3 | job 3/3 accepted | baseline fails H1, H6, H3; no two blocks, no quotes | **pass** at `23ab607` (`check-against-bia/runs/grades-sweep-23ab607.md`) |
| check-against-bia | Codex | job 3/3, never-alone 3/3, F2 3/3 | job 3/3 accepted | baseline fails H1, H3, H6 | **pass** at `23ab607` (never-alone 0/3 at `5ec8f40`, fixed) |
| ask-ai4bcm | Claude Code | job 3/3, never-alone 3/3, F2 2/3, new routes 3/3 | job 3/3 accepted | baseline guesses section and level | **pass** at `23ab607` (`ask-ai4bcm/runs/grades-sweep-23ab607.md`) |
| ask-ai4bcm | Codex | job 3/3, never-alone 3/3, F2 3/3, new routes 3/3 | job 3/3 accepted | baseline drafts the work itself | **pass** at `23ab607` (never-alone 0/3 at `5ec8f40`, fixed) |
| challenge-my-plan | Claude Code | | | | |
| challenge-my-plan | Codex | | | | |
| learn-bcm | Claude Code | | | | |
| learn-bcm | Codex | | | | |
| check-against-standards | Claude Code | | | | |
| check-against-standards | Codex | | | | |
| role-card | Claude Code | | | | |
| role-card | Codex | | | | |
| red-team-assumptions | Claude Code | | | | |
| red-team-assumptions | Codex | | | | |
| debrief-to-action | Claude Code | | | | |
| debrief-to-action | Codex | | | | |
| check-my-ai-tool | Claude Code | | | | |
| check-my-ai-tool | Codex | | | | |
