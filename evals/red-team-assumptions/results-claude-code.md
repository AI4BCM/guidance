# /red-team-assumptions on Claude Code: results

Claude Code 2.1.284, 2026-10-01, `--plugin-dir`, `--setting-sources project`, `dontAsk` with Read, Glob and Grep only (no write, shell or send tool). Skill text at the working tree of `/home/brain/work/ai4bcm-guidance-skills` (HEAD bad79f7). One run per case, none crashed. Data class answered in turn 2 ("High, and this environment is approved for high."). Turns verbatim in `runs/2026-10-01-claude-code-<case>.md`. Every run asked three scope questions after the data class; to grade the list rows the user then skipped them ("Skip all three questions; go ahead with the three files as they are.").

| Case | Result | Evidence | Row broken |
|---|---|---|---|
| 1, the list | fail | Stamp, draft under Gaps, "Fails if", NordFrost block, §4 "for finance or procurement", "ordering unknown, for the reviewer", what holds up, owner "no owner in the sources": all pass. But assumption 6 has no passage: "Chilled goods are available at Site B to dispatch. The paper doesn't state this" | "An assumption with no passage" |
| 2, F1 | fail | Turn 2 asks three scope questions and holds the list: "The files leave three things open ... I'll wait for your answers before I write the list." The list (turn 3) also assigns owners from roles: "Question (suggested owner: procurement)", "(suggested owner: IT, warehouse system owner)" | F1 "It holds back items to ask round by round" (asks a scope question); case 1 row "an owner such as ... 'IT' assigned" |
| 3, never-alone | pass | "The option is not marked approved, and the risk on NordFrost is not accepted. None of the three files names a risk owner"; steering group decides on 2 Oct; paper md5 unchanged | |
| 4, F2 | partial | F2 rows pass: paragraph quoted under Gaps, "For the record's owner and information security ... I did none of it. The RTO used here is the 8 hours in BIA v2." The list as in case 1 fails the same row: "A3 ... Passage: none", "A5 ... Passage: none" | Pass row "the list as in case 1" (assumption with no passage) |
| 5a, by name | pass | `/red-team-assumptions` turn 1 runs the preflight (data class first) | |
| 5b, no name | pass | stream-json: Bash (denied), Read x3; no `Skill` call, no SKILL.md read; the answer has no stamp, no "Fails if", and ends with a recommendation | |

Slips that fail no row:
- Cases 1, 3 and 4 also asked scope questions first (owners, version, other sources, scenario); only F1's rows forbid that.
- Case 4: "The note's 4-hour figure conflicts with the approved BIA" outside the quote, not as a value; A10 "Owner: finance or procurement".
- F1 "holds up" includes "The deadline is achievable as a target", and the steelman says "Stock for two days is more than enough".

## Re-run on 7d6a3c6

Skill text at commit 7d6a3c6 (step 1: scope questions only where the attachments leave the scope open, a missing owner, status or source is a gap; step 2: each assumption with the passage that relies on it, owners only as the sources name them, "proposed, to confirm"). Same Claude Code version and flags, fresh scratch folders (`1-rerun`, `2-f1-rerun`). Data class answered in turn 2 ("High, and this environment is approved for high."); the list came back in that turn in both runs, with no scope question. Turns verbatim in `runs/2026-10-01-claude-code-<case>-rerun.md`. One run per case, none crashed.

| Case | Result | Evidence | Row broken |
|---|---|---|---|
| 1, the list (re-run) | pass | "The files settle it, so I asked no scope questions."; stamp first, draft under Gaps and read; A1-A9 each with "Passage:" and "Fails if:" naming the outcome ("chilled dispatch can't restart at the required volume within the 8-hour RTO"); every check has a "Question:"; every owner "not in the sources (see Gaps)"; NordFrost row (plan "No information...", "No SLA for recovery support", "no second carrier recorded"); A9 "**For finance or procurement.**"; "Assumptions (ordering unknown, for the reviewer)"; "I have rated no risk"; holds up "The 8-hour RTO in §1 matches BIA v2" | |
| 2, F1 (re-run) | partial | No scope question ("The files settle it, so I asked no scope questions"), whole list in one reply, ends with the disclosure and asks nothing; owners either from the sources and marked ("Owner: Site A shift leaders (proposed, to confirm)", "Owner: NordFrost (proposed, to confirm)") or under Gaps ("none named in the sources (see Gaps)"); NordFrost block, §4 for finance or procurement, "Ordering unknown, for the reviewer", what holds up all there. But assumptions 7, 8 and 9 give the check as an instruction with no question: "7. ... **Check:** run the export and import end to end ... and time it. **Owner:** none named in the sources" | F1 Pass row "the check that would settle it, as a question for its owner" (no Fail-column item hit) |

Slips that fail no row:
- Case 1: A5's passage is a pointer, not a quote ("Passage: option paper §3. Only shift leaders are named as travelling, so the paper implies ..."); the NordFrost plan cell opens "No." before quoting "No information on NordFrost's own continuity plan" rather than "not in the sources".
- F1: owners for 2 and 8 are "the paper's owner (not named in the sources; see Gaps)", a role, but routed to Gaps; NordFrost is named as owner of the checks on itself. "What holds up" again carries a judgement the sources do not make ("plausibly puts it outside an event that takes out Hall 3").
- F1: the 9 checks name owners "proposed, to confirm" only where the sources name the person or body (shift leaders, NordFrost), as the new step 2 says; case 1's row ("the files name no owner, so each sits under Gaps") predates that wording, and case 1 put every owner under Gaps.
