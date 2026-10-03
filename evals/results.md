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
| prepare-bia | Claude Code | job 1/3, never-alone 3/3, F2 2/3 at `836c32f` | job 2/3 accepted | baseline fails H1, H6, H7 | **not yet passed** at `836c32f` (fix round 4 dropped 'what you need back'; fixed `c976ac5`, re-sweep pending); passed at `23ab607` |
| prepare-bia | Codex | job 3/3, never-alone 3/3, F2 3/3 | job 3/3 accepted | baseline fails H1, H6, H7 | **pass** at `836c32f` |
| check-against-bia | Claude Code | job 3/3, never-alone 3/3, F2 3/3 | job 3/3 accepted | baseline fails H1, H6, H3 | **pass** at `836c32f` (`check-against-bia/runs/grades-sweep-836c32f.md`) |
| check-against-bia | Codex | job 3/3, never-alone 3/3, F2 2/3 | job 3/3 accepted | baseline fails H1, H3, H6 | **pass** at `836c32f` |
| ask-ai4bcm | Claude Code | job 3/3, never-alone 2/3, F2 2/3, new routes 3/3 | job 3/3 accepted | baseline guesses section and level | **pass** at `836c32f` (`ask-ai4bcm/runs/grades-sweep-836c32f.md`) |
| ask-ai4bcm | Codex | job 3/3, never-alone 3/3, F2 3/3, new routes 3/3 | job 3/3 accepted | baseline drafts the work itself | **pass** at `836c32f` |
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
