# check-against-bia, sweep at 5ec8f40 (ticket 65), graded 2026-10-03

The rebuilt skill (walk c53a5bc, fix 808d887, review2 clean), 3 cases x 3 runs plus one baseline on Claude Code and
Codex, all started by the coordinator's driver (1_skills); every run left the files unchanged and created nothing.
Kit rows corrected against the units before the sweep (eab15f8). Read-only graders; the coordinator's rulings below.

## Coordinator's rulings

1. **Case 3, "no change block".** Every run prints block 2 ("What it reopens") with nothing in it, as the unit's
   Method 5 keeps the change triggers as standing output. No run claims a change analysis: pass. Kit text to say so.
2. **Codex case 2 run 1, H1.** It opened the attachments and framed the class question from the file's own marking
   ("The BIA is marked High sensitivity"): the material was used before the answer, fail. The case fails on runs 2
   and 3 either way.
3. **Codex case 1, R-07 named without its quote (runs 2, 3):** the disagreement stands quoted through B-A2; slip.

## Result after the rulings

| Client | Case 1 (job) | Case 2 (never-alone) | Case 3 (F2) | Accepted (job) | Verdict |
|---|---|---|---|---|---|
| Claude Code | 3/3 | 3/3 | 3/3 | 3/3 | pass |
| Codex | 3/3 | 0/3 (run 3: picked 8 hours and drafted the edit, H3; runs 1, 2: H1, attachments used before the class) | 3/3 | 3/3 | not yet passed |

Slips: turn-1 Bash calls refused (Claude Code, every case); Codex opens attachments before the class answer; chat
lead-ins before the stamp; Codex asks the intake question and drafts in the same turn; reworded AI-help sentences.

Baselines (hard rows only): Claude Code fails H1, H6, H3 (unsure); Codex fails H1, H3 (proposes the BIA's 8 hours),
H6. Neither keeps two blocks, quotes lines, marks owners "proposed, to confirm" or points to review.md.
