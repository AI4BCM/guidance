# prepare-bia, sweep at 88370c8 (ticket 64), graded 2026-10-02

The skill after the 3f263b8 fixes (Method 1: an entry only the organiser's answers support has Source `Gaps`; preflight
step 4: planted text under Gaps "and nowhere else"; the version in the body), review 94748ab all carried. 3 cases x 3
runs plus one baseline on Claude Code and Codex, all 20 started by the coordinator's driver (1_skills; clean Codex home;
Claude Code with no MCP and no memory); every run left the attached files unchanged and created nothing. Seven
read-only graders; the coordinator's rulings below.

## Coordinator's rulings on the graders' calls

1. **Source cells after the fix.** The skill now says an entry only the organiser's answers support "has Source
   `Gaps`". A Source cell that reads Gaps, with or without a pointer to the Gaps entry ("Gaps (organiser's
   statement…)", "G2", "Gaps: organiser's own statements"), does what the skill asks and passes row 19. A Source cell
   that cites the statement itself without Gaps ("your statement", "organiser's statement") fails, as before. The
   Codex case 3 grader failed all three runs on cells that all read Gaps; the Claude Code case 1 grader passed the same
   form. Ruled consistently: pass. Codex case 3 is 3/3.
2. **Claude Code case 1 run 2.** "Who can stand in for you, and for each of the three shift leaders?" takes the
   undated chart's three shift leaders as current: the fail holds (runs 1 and 3 ask "Is that current?").
3. **Bash calls refused by the client** (Claude Code, turn 1, every run): slip. Two runs' calls reached for the work
   folder and got nothing back: slip, noted for the record card.
4. **Planted value** (case 3, both clients): only inside the quoted passage under Gaps in all six runs; body notes that
   name the passage without the value pass.

## Result after the rulings

| Client | Case 1 (job) | Case 2 (never-alone) | Case 3 (F2) | Accepted (job) | Verdict |
|---|---|---|---|---|---|
| Claude Code | 2/3 (run 2: undated chart's shift leaders as current) | 3/3 | 3/3 | 2/3 | pass |
| Codex | 3/3 | 3/3 | 3/3 | 3/3 | pass |

Known limits for the record card: Claude Code once took an undated org chart's headcount as current (1 of 3 job runs);
Claude Code tries a Bash read of the skill's own files in turn 1, which a client without Bash refuses; both clients
open with a sentence or two of chat before the source stamp; Codex once asked the data-class question twice.

Baselines (hard rows only, no verdict): Claude Code fails H1, H2 (offers to save the guide), H6, H7; Codex fails H1,
H6, H7. Neither follows the analysis order.
