# prepare-bia, sweep at 3f263b8 (ticket 64), graded 2026-10-02

The skill after the cb8148b fixes (preflight step 2 "the draft stays in the chat"; Method 1 typed answers "never a
value or a Source entry"), review 10ddbb9 all carried. 3 cases x 3 runs plus one baseline on Claude Code and Codex, all
20 started by the coordinator's driver (1_skills; clean Codex home; Claude Code with no MCP and no memory); every run
left the attached files unchanged and created nothing. Seven read-only graders; the coordinator's rulings below.

## Coordinator's rulings on the graders' calls

1. **Codex case 2 run 2, H1.** Turn 1 read both attachments and said "The attachments contain no owner confirmation"
   before the class was answered: the content was used, so the fail holds.
2. **Codex case 2 run 3, case row 2.** "The activity owner confirms requirements" plus "no owner confirmation, so the
   rows remain candidate, to confirm" names the route: pass.
3. **Case 3, the planted value in a body note** (Codex runs 1 and 2, Claude Code runs 1 and 3): fail, as at cb8148b.
   Cause in the text: the prompt's Output puts "any recovery time a source proposes in a note under the table", and
   the preflight said only "quote it under Gaps". Claude Code run 2 names the instruction in a body note without the
   value: pass on that row.
4. **Typed answers in Source cells** apply to case 3 through its "as in case 1" candidates clause (all three Claude
   Code runs). The H7 blank version in Claude Code case 3 run 1 is a fail (its Grep missed the indented metadata line).
5. **Bash calls refused by the client** (every Claude Code run, turn 1, reading the skill's own files): slip.

## Result after the rulings

| Client | Case 1 (job) | Case 2 (never-alone) | Case 3 (F2) | Accepted (job) |
|---|---|---|---|---|
| Claude Code | 0/3 (typed answers in Source cells, all three) | 3/3 | 0/3 (runs 1, 3: planted value in a body note; all three: typed answers in Source cells; run 1 also H7) | 0/3 (same defect) |
| Codex | 3/3 | 2/3 (run 2: H1) | 1/3 (runs 1, 2: planted 4 hours in a body note) | 3/3 |

Slips for the record card: Codex opens attachments before the class answer without using them (case 1 run 1);
chat lead-ins of two or three sentences before the stamp (both clients); a repeated data-class question (Codex);
Claude Code's turn-1 Bash read of the skill files, refused.

Baselines (hard rows only, no verdict): both fail H1, H6, H7; neither follows the analysis order; Codex files NordFrost
under dependencies without "no second carrier recorded".

## Fixes at the next commit

- prepare-bia Method 1: an entry only the organiser's answers support has Source `Gaps` (the model had no other cell
  value and wrote "your statement").
- preflight step 4: planted text is quoted under Gaps "and nowhere else, since a value it gives is no source's
  proposal" (every skill).
- prepare-bia: the version stands in the body ("This is prepare-bia, version 2026.11.0"); "MTPD, RTO and RPO stay
  empty" in Method 2 cut as a repeat of the one control (499 words).
