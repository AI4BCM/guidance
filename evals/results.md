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
| prepare-bia | Claude Code | job 3/3 (case 1 only; kit proof, ticket 62) | job 1/3: run 2 and run 3 break the analysis order (suppliers before IT and seats, NordFrost dependency filed under suppliers); run 2 cites the organiser's typed answer as a source; run 3 names no reviewer and drops Method 4 | not run | not yet passed: pre-rebuild skill at `ef3bca9`, kit `85ebae8`; ticket 64 replaces this row |
| prepare-bia | Codex | job 1/1 (case 1 only, one run; kit proof, ticket 62) | job 1/1 accepted, but the case row on NordFrost fails ("no second carrier recorded" never reaches the owner), so the run fails | not run | not yet passed: pre-rebuild skill at `85ebae8`, kit `85ebae8`; ticket 64 replaces this row |
| check-against-bia | Claude Code | | | | |
| check-against-bia | Codex | | | | |
| ask-ai4bcm | Claude Code | | | | |
| ask-ai4bcm | Codex | | | | |
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
