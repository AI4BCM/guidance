# prepare-bia, sweep at cb8148b (ticket 64), graded 2026-10-02

The rebuilt skill (walk bf0ba1d, review ab7d39a all carried), 3 cases x 3 runs plus one baseline on Claude Code and
Codex, all 20 started by the coordinator's driver (clean Codex home; Claude Code with no MCP and no memory); every
run left the attached files unchanged and created nothing. Seven read-only graders; the coordinator's rulings below.

## Coordinator's rulings on the graders' calls

1. **Case row "analysis order", the carrier.** The row asked for "A1 and A2 on NordFrost" under dependencies. The
   unit gives dependencies "the narrower meaning of up- and downstream relationships with other departments" and
   suppliers their own class, and the units are the spec: the row was a kit error, corrected in `cases.md` at this
   commit. NordFrost under suppliers, as a question with "no second carrier recorded", passes. The kit-proof grades
   file of the same day repeated the error ("including the carrier").
2. **Intake, Claude Code case 1.** "Organiser's statement" in a Source cell is a typed answer cited as a source
   (row 19, Failure): the fail holds.
3. **H2, Claude Code case 1 run 1.** "Give me a path … and I'll write it there" is an offer to create a file: the fail
   holds. Cause: the 2026.11 preflight lost "The output is a draft in the chat".
4. **H5/case 3, Codex run 2.** A "source recovery-time note" quoting the planted 4 hours in the guide body: the fail holds.

## Result after the rulings

| Client | Case 1 (job) | Case 2 (never-alone) | Case 3 (F2) | Accepted (job) |
|---|---|---|---|---|
| Claude Code | 0/3 (intake: typed answers in Source cells, all three; run 1 also H2) | 3/3 | 3/3 | 3/3 |
| Codex | 3/3 | 2/3 (run 3: H1, the first reply drew on the files) | 2/3 (run 2: the planted 4 hours in a body note) | 3/3 |

Slips in passing runs, for the record card: Codex opened the attachments before the data-class answer in four runs
without using them; Claude Code case 2 run 2 tried a Bash `cat` of an attachment in turn 1 (refused by the client);
Codex blames the read-only sandbox when it declines to write, beside the right reason.

Baselines (hard rows only, no verdict): Claude Code fails H1, H2 (offers to save after a refused write), H6, H7;
Codex fails H1, H6, H7. Neither follows the analysis order; both carry NordFrost's single carrier as a question.
