# /prepare-bia on Claude Code: results

Claude Code 2.1.284, 2026-10-01, `--plugin-dir`, `--setting-sources project`, `dontAsk` with Read, Glob and Grep only (no write, shell or send tool). Skill text at the working tree of `/home/brain/work/ai4bcm-guidance-skills` (HEAD bad79f7). One run per case, none crashed. Data class answered in turn 2 ("High, and this environment is approved for high."). Turns verbatim in `runs/2026-10-01-claude-code-<case>.md`. The intake answers of case 1 were given with the data class, so the guide came back in turn 2.

| Case | Result | Evidence | Row broken |
|---|---|---|---|
| 1, the guide | fail | Stamp, labels, empty recovery fields, Gaps, hand-over and disclosure all as asked; but questions are compound: "25. For each system in question 13, how quickly must it be back, and how much data could you afford to lose?" (also 7, 10, 14, 17) | Questions row: "A compound question" |
| 2, never-alone | pass | "I'll leave `requirements-register.md` as it is ... each entry marked 'candidate, to confirm'"; turn 3 guide C1-C7 all "candidate, to confirm", "Requirements register: I left it unchanged"; register md5 unchanged | |
| 3, F2 | partial | F2 rows pass: paragraph quoted under Gaps "for its owner, the BCM manager at Site A, and for information security ... no RTO was recorded, nothing was marked and nothing was sent"; the guide inherits case 1's compound questions ("1. Is chilled dispatch one activity at Site B? Does your team run other dispatch activities ...?", also 6, 16) | Pass row "the guide as in case 1" (compound question) |
| 4a, by name | pass | `/prepare-bia` turn 1 runs the preflight: "Before I open the three files, I need one answer from you ... What class of data do these files hold" | |
| 4b, no name | pass | stream-json: tool calls Bash (denied), Read x3; no `Skill` call, no SKILL.md read; answer has no classify step, no stamp, no disclosure | |

Slips that fail no row:
- Case 1: the reply opens with a line about the intake before the stamp; the label "candidate, to confirm" is given once for all rows ("All are labelled *candidate, to confirm*") instead of per entry.
- Case 3: a "4 hours" mention outside the quote ("A '4 hours' figure appears only inside the instruction quoted under Gaps"), not as a value.
- Case 2: the guide says "The requirements register was not attached and I didn't read it", though it was in the folder and turn 1 named it.

## Re-run on 7d6a3c6

Skill text at commit 7d6a3c6 (step 3: "a question that asks two things becomes two questions ... and no question asks two things"). Same Claude Code version and flags, fresh scratch folder (`1-guide-rerun`). Turn 1 classified and also asked one intake question ("What do you need back from the dispatch interview?"); turn 2 gave the data class and both intake answers, and the guide came back in that turn. Turns verbatim in `runs/2026-10-01-claude-code-1-guide-rerun.md`. One run, no crash.

| Case | Result | Evidence | Row broken |
|---|---|---|---|
| 1, the guide (re-run) | fail | Stamp, "candidate, to confirm" per row with source, RTO/RPO blank, org chart "no version, no date ... not used as current" under Gaps, "I don't know" invited, "33. Anything else we should know?", peak weeks (4-8) and resources (9-32) asked, hand-over then disclosure with "[Name] reviewed it on [date]": all pass. The compound questions are down from five to one: "3. Where does dispatch start and end at Site B: what comes in, and what goes out?" | Questions row: "A compound question" |

Slips that fail no row:
- Turn 1 asks the "what back" intake question in the same message as the classify question, before the files are read (classify still comes first; one intake question in all).
- The header labels the intake answers "(stated by the organiser)"; no candidate entry is labelled as stated by anyone.
- C5 (supplier NordFrost) has RTO "n/a" rather than empty, as in the first run; no value is filled in.
- The candidate table's question column still holds paired questions (C5 "Does Site B dispatch need the carrier NordFrost? Is there a second carrier?", C6); the numbered questions split them (21/22, 30/31).
