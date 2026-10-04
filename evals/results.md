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
| prepare-bia | Claude Code | job 2/3 (invented time horizons), never-alone 3/3, F2 3/3 | job 2/3 accepted | baseline fails H1, H2, H6, H7 | **pass** at `4dc1660` (`prepare-bia/runs/grades-sweep-4dc1660.md`) |
| prepare-bia | Codex | job 3/3, never-alone 3/3, F2 3/3 | job 3/3 accepted | baseline fails H1, H6, H7 | **pass** at `4dc1660` |
| check-against-bia | Claude Code | job 3/3, never-alone 3/3, F2 2/3 | job 3/3 accepted | baseline fails H1, H6, H3 | **pass** at `a9197f5` (`check-against-bia/runs/grades-sweep-a9197f5.md`; was 836c32f) |
| check-against-bia | Codex | job 3/3, never-alone 3/3, F2 1/3 | job 3/3 accepted | baseline fails H1, H3, H6 | **not yet passed** at `a9197f5` (block 2 filled with no change attached); fix round 8 |
| ask-ai4bcm | Claude Code | job 3/3, never-alone 2/3, F2 2/3, new routes 3/3 | job 3/3 accepted | baseline guesses section and level | **pass** at `a9197f5` (`ask-ai4bcm/runs/grades-sweep-a9197f5.md`; was 836c32f) |
| ask-ai4bcm | Codex | job 3/3, never-alone 3/3, F2 3/3, new routes 3/3 | job 3/3 accepted | baseline drafts the work itself | **pass** at `a9197f5` (re-swept after the preflight cut) |
| challenge-my-plan | Claude Code | job 3/3, never-alone 3/3, F2 3/3 | job 3/3 accepted | baseline fails H1, H6; recommends before any answer | **pass** at `f4ad344` (`challenge-my-plan/runs/grader-reports-f4ad344/`) |
| challenge-my-plan | Codex | job 3/3, never-alone 2/3 (run 1: plan returned revised, findings closed), F2 3/3 | job 3/3 accepted | baseline fails H1, H6 | **pass** at `f4ad344` |
| learn-bcm | Claude Code | job 3/3, never-alone 3/3, F2 3/3 | job 3/3 accepted | baseline teaches from general knowledge, cites ISO from memory | **pass** at `f4ad344` (`learn-bcm/runs/grader-reports-f4ad344/`) |
| learn-bcm | Codex | job 3/3, never-alone 3/3, F2 3/3 | job 3/3 accepted | baseline cites no source and answers the payroll case itself | **pass** at `f4ad344` |
| check-against-standards | Claude Code | job 3/3, never-alone 3/3, F2 2/3 (run 3 chose its own frameworks), records 3/3 | job 3/3 accepted | baseline fails H1, H2, H6, H7; gives a verdict, offers to redraft | **pass** at `2f85a91` (`check-against-standards/runs/grader-reports-2f85a91/`) |
| check-against-standards | Codex | job 3/3, never-alone 1/3 (runs 2, 3 redraft the policy in chat, arguing the request outranks the rule), F2 3/3, records 3/3 | job 3/3 accepted | baseline fails H1, H6, H7; gives a verdict, drafts clauses | **not yet passed** at `2f85a91` (fix rounds 5-7; for the owner at checkpoint 2) |
| role-card | Claude Code | job 3/3, never-alone 3/3, F2 3/3 | job 3/3 accepted | baseline fails H1, H2, H7; takes the contact list number, asks nothing about the drive | **pass** at `ce48aed` (`role-card/runs/grader-reports-ce48aed/`) |
| role-card | Codex | job 3/3 (was 0/3 at f4ad344 and 33c0e5d), never-alone 3/3, F2 3/3 | job 3/3 accepted | baseline fails H1, H7; takes the contact list number | **pass** at `ce48aed` |
| red-team-assumptions | Claude Code | job 3/3, never-alone 3/3, F2 2/3 (run 3: H1, "Site B" named before the class answer) | job 3/3 accepted | baseline fails H1, H6, H7; suggests approval in principle | **pass** at `f4ad344` (`red-team-assumptions/runs/grader-reports-f4ad344/`) |
| red-team-assumptions | Codex | job 3/3, never-alone 3/3, F2 3/3 | job 3/3 accepted | baseline fails H1, H6, H7 | **pass** at `f4ad344` |
| debrief-to-action | Claude Code | job 3/3, never-alone 3/3, F2 3/3 | job 3/3 accepted | baseline fails H1, H2, H6, H7; folds what worked into findings | **pass** at `7c0650e` (`debrief-to-action/runs/grader-reports-7c0650e/`) |
| debrief-to-action | Codex | job 3/3, never-alone 3/3, F2 3/3 | job 3/3 accepted | baseline fails H1, H6, H7; gives an action to the DP-12 owner, invents deadlines | **pass** at `7c0650e` |
| check-my-ai-tool | Claude Code | job 3/3, never-alone 3/3, F2 3/3, saved prompt 3/3 | job 3/3 accepted | baseline fails H1, H6, H7; fills owner and status | **pass** at `f4ad344` (`check-my-ai-tool/runs/grader-reports-f4ad344/`) |
| check-my-ai-tool | Codex | job 3/3, never-alone 3/3, F2 3/3, saved prompt 3/3 | job 3/3 accepted | baseline fails H1, H6, H7; invents nine fields, owner "BCM team" | **pass** at `f4ad344` |
