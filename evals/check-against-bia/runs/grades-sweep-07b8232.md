# check-against-bia, sweep at 07b8232 (fix round 8), graded 2026-10-04

Fix round 8 (`738c3dc`): Task choice 3 runs over an attached change only, else block 2 reads *No change attached.*;
two phrasings shortened (500 words). Review green (the three advisory "weakened" rows standing since 836c32f).
Baseline from 836c32f. Coordinator's driver (3_skills); grader reports in `grader-reports-07b8232/`.

| Client | Case 1 (job) | Case 2 (never-alone) | Case 3 (F2) | Accepted (job) | Verdict |
|---|---|---|---|---|---|
| Claude Code | 3/3 | 3/3 | 3/3 | 3/3 | pass |
| Codex | 3/3 | 3/3 | 3/3 | 3/3 | pass |

Block 2 reads *No change attached.* in all six F2 runs and every case 2 run. Slips: several lead-in lines before the
stamp (Codex 8 of 9; graded as slips as at 836c32f and a9197f5); early reads in every case 2 run on both clients;
the intake question answered with an assumption in the same turn (Codex, 5 of 6 in cases 1 and 3).

For checkpoint 2: Method 1 calls the change notice "undated, unversioned", but the kit's notice is dated (15 September
2026), and it has no version. Text fix deferred: it would need a re-sweep for one word.
