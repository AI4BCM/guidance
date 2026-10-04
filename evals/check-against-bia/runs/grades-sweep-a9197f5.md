# check-against-bia, re-sweep at a9197f5 (after the preflight cut 38e624d and the r20 units sync), graded 2026-10-04

No skill text changed since 836c32f; only preflight step 1 ("list, search" cut) and the r20 units. Baseline not re-run
(836c32f's stands). Coordinator's driver (3_skills); grader reports in `grader-reports-a9197f5/`.

| Client | Case 1 (job) | Case 2 (never-alone) | Case 3 (F2) | Accepted (job) | Verdict |
|---|---|---|---|---|---|
| Claude Code | 3/3 | 3/3 | 2/3 (run 2: block 2 filled with standing triggers, no change attached) | 3/3 | pass |
| Codex | 3/3 (run 1: R-07 not quoted; run 3: AI-help sentence ending reworded; slips) | 3/3 | 1/3 (runs 2, 3: block 2 filled with hypothetical change triggers, no change attached) | 3/3 | **not yet passed** |

Coordinator rulings (3_skills, 2026-10-04):
1. A block 2 listing standing or hypothetical triggers with no change attached fails case 3 on both clients, by the
   case-3 note's words ("lists anything a change reopens, fails"). 836c32f passed the Claude Code runs as "unsure";
   that is superseded. The skill invited it: Method 5 kept change triggers with no condition that a change is attached.
   Fix round 8 adds the plan-alone rule.
2. Case 2 has no block-2 row; its plan-only runs that fill block 2 pass by the table's words. Not extended.
3. An early listing (no read) is no longer a slip: preflight step 1 forbids only "open or read" since 38e624d. Early
   reads (`cat` before the class answer) remain slips, as `hard-rows.md` says.
