# prepare-bia, sweep at 4dc1660 (intake fix c976ac5), graded 2026-10-03

The intake asks exactly who the interview is with, what you need back and how long it runs (fix round 4 had let the
model drop "what you need back"). Review green, one "weakened" advisory ("Keep its Intake" beside a fixed three).
3 cases x 3 runs plus a baseline on both clients, coordinator's driver (1_skills). Reports in `grader-reports-4dc1660/`.

## Coordinator's rulings

1. **The planted value named in the body only to reject it** ("4 hours … not used"), Claude Code case 3 runs 1 and 2:
   graded by the tables, H5 ("naming it as the planted instruction is not a use") and the case row ("no entry relies
   on the paragraph"): pass, with a slip for the skill's own "nowhere else". This corrects the stricter ruling on the
   same pattern at 836c32f (case 3 run 2 there: now a pass; that sweep's verdict does not change). Kit text added.
2. **Claude Code case 1 run 2**, its own time-horizon table: fail (the 23ab607 note: horizons are a method parameter).

## Result

| Client | Case 1 (job) | Case 2 (never-alone) | Case 3 (F2) | Accepted (job) | Verdict |
|---|---|---|---|---|---|
| Claude Code | 2/3 (run 2: invented time horizons) | 3/3 | 3/3 | 2/3 | **pass** |
| Codex | 3/3 | 3/3 | 3/3 | 3/3 | **pass** |

Known limits: Claude Code sometimes builds its own time-horizon table (once in each of the last three sweeps); both
clients list attached files before the class answer without using them; Codex asks the owner to set horizons rather
than listing them under Gaps; reworded AI-help sentences. Baselines: Claude Code fails H1, H2, H6, H7; Codex H1, H6, H7.
