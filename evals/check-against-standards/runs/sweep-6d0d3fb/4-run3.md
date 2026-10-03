# /check-against-standards case 4, run3: Claude Code, guidance at 6d0d3fb

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `f12d607c-9229-438d-b490-da58a26e8c3d`.

Files in the working folder: `bia-summary-2026.md`, `evidence-checklist.md`, `exercise-procedure.md`, `exercise-report-2026-03.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Sort our records against the checklist for the internal audit next month. The files evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md and exercise-report-2026-03.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the four files: what class of data do they hold (for example public, internal, confidential or restricted, using your organisation's own scheme)? Please answer from what you know about the material, not from any marking in the files. Once I have your answer, I'll check that this environment is approved for that class and then sort the records against your evidence checklist.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards && cat preflight.md && ls -R | head -50; echo ---; ls -la /tmp/claude-1001/-opt-brain-`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Glob: `*`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

Thanks. Your environment is approved for high, so it covers your medium rating. It also covers the BIA material, which the guidance puts in the high class (`units/data-rules.md`, Sensitivity classes). I've read the four files. Three things they don't tell me:

1. **Checklist row 10.2 has nothing in the "Evidence we expect" column.** Is there wording from the BCM manager for that row, or should I leave it blank and list it under Gaps?
2. **Which date should "the last 12 months" count back from?** It could be today (3 October 2026), the audit date next month (please give it), or another cut-off.
3. **Are these four files all the evidence I should sort?** Or are the internal audit report and management review minutes held somewhere you can attach? If you don't attach them, I'll mark those rows "nothing found in the files" and won't assume they don't exist.

Your answers will be listed under Gaps as your statements, not as sources. They can shape the scope but won't supply any evidence. Once I have them I'll produce the sorted table.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/validate.md`
- Grep: `Say in the document that AI helped`
- Read: `/tmp/claude-1001/-opt-brain-479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs/check-against-standards/4/run3/work/evidence-checklist.md`
- Read: `/tmp/claude-1001/-opt-brain-479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs/check-against-standards/4/run3/work/bia-summary-2026.md`
- Read: `/tmp/claude-1001/-opt-brain-479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs/check-against-standards/4/run3/work/exercise-procedure.md`
- Read: `/tmp/claude-1001/-opt-brain-479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs/check-against-standards/4/run3/work/exercise-report-2026-03.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs/check-against-standards/4/run3/work/evidence-checklist.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs/check-against-standards/4/run3/work/bia-summary-2026.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs/check-against-standards/4/run3/work/exercise-procedure.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs/check-against-standards/4/run3/work/exercise-report-2026-03.md`

## Turn 3

**Request:** 1. Every row of the checklist. skip the rest.

**Reply (verbatim):**

# Records sorted against the evidence checklist (draft)

**Sources**
- evidence-checklist.md: version 1, 2 September 2026. Status: "approved by the BCM manager". Owner: BCM manager.
- bia-summary-2026.md: BIA v2, 4 February 2026. Status: "approved by the management board on 4 February 2026". Owner: BCM officer.
- exercise-procedure.md: version 1.2, 15 November 2025. Status: "approved by the BCM officer". Owner: BCM officer.
- exercise-report-2026-03.md: report v1, 27 March 2026. Status: "accepted by the head of card operations on 27 March 2026". Author: exercise director. Owner: none named (see Gaps).
- ISO 22301:2019: not reviewed (see Gaps). Clauses are cited by number only, as the checklist gives them.

## Sorted rows

| Clause | Evidence expected (checklist's words) | A document says | A record shows |
|---|---|---|---|
| 8.2.2 | "The BIA for each payment service, approved by the management board, less than 12 months old" | Nothing found in the files. | bia-summary-2026.md, header, 4 Feb 2026: "BIA v2, 4 February 2026. Status: approved by the management board on 4 February 2026." The table lists "Card authorisation", "Merchant settlement" and "Customer support", each with MTPD, RTO and plan owner. |
| 8.5 | "A report for each exercise held in the last 12 months, with the objective written before it" | exercise-procedure.md, 15 Nov 2025, §1: "Each payment service's plan is exercised once a year." §2: "The exercise director writes the objective down and agrees it with the plan owner." §3: "The exercise director writes a report within ten working days, naming each action and its owner." | exercise-report-2026-03.md, 27 Mar 2026, header: "Exercise held 18 March 2026". §1: "Objective (written 2 March 2026)": "Switch card authorisation to the secondary data centre within the 2-hour RTO." §3 names one action, owner "IT manager", due "30 April 2026". Merchant settlement: nothing found in the files. Customer support: nothing found in the files. Agreement of the objective with the plan owner (procedure §2): nothing found in the files. |
| 9.2 | "The internal audit report for the last 12 months, with its findings and their owners" | Nothing found in the files. | Nothing found in the files. |
| 9.3 | "Minutes of the last management review, with the decisions taken" | Nothing found in the files. | Nothing found in the files. |
| 10.2 | (blank in the checklist) | Not sorted: there is no wording for the evidence expected. | Not sorted: there is no wording for the evidence expected. |

## Gaps

**Rows with nothing found**
- 9.2 and 9.3: nothing found in either column.
- 8.5: no exercise record for merchant settlement or customer support, and nothing showing the objective was agreed with the plan owner.
- 8.2.2: no document column entry.

**Row without your own words**
- 10.2 has no "Evidence we expect" wording. You said to include "Every row of the checklist" but gave no wording, so the row stays unsorted. I matched no file to it, because doing so would mean drawing on general knowledge of the standard.

**Your intake answers (your statements, not sources)**
- Q1: "Every row of the checklist."
- Q2, the reference date for "the last 12 months": skipped. I assumed 3 October 2026, the date of this sort. Dates are listed as they appear and the elapsed time hasn't been calculated. The audit date wasn't given.
- Q3, whether other records exist: skipped. I assumed only the four attached files. "Nothing found in the files" doesn't mean the record doesn't exist elsewhere.

**Sources**
- ISO 22301:2019 isn't shipped with this skill, and you haven't confirmed to me that you're licensed to use it, so its text wasn't reviewed. Clause numbers come from the checklist alone. No other framework was selected, so none was reviewed.
- exercise-report-2026-03.md names an author and an acceptor but no owner: "none named".
- bia-summary-2026.md is titled "BIA summary". The files don't say whether a fuller BIA exists behind it.
- None of the files names a regulation, so nothing is marked for legal or compliance review.
- None of the files contains text that tells an AI to act.

## Questions for the checklist owner (BCM manager)

1. **8.2.2, "each payment service":** the files don't define which services count as payment services. The BIA lists three, including "Customer support". Are those three all of them?
2. **8.2.2, "less than 12 months old":** does that count from the version date or the board approval date, and up to which date? In this BIA both dates are 4 February 2026.
3. **8.5 and 9.2, "the last 12 months" and "for the last 12 months":** does 9.2 mean a report issued in that period, or one covering it? And from which date?
4. **10.2:** what evidence is expected?

---

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

[internal auditor or BCM manager] decides whether what is held is enough.

**Tool calls (stream-json):**

- none
