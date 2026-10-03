# /check-against-standards case 4, run1: Claude Code, guidance at 2f85a91

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `ef899c07-b666-4fd7-9ed3-f5d6cbd90d75`.

Files in the working folder: `bia-summary-2026.md`, `evidence-checklist.md`, `exercise-procedure.md`, `exercise-report-2026-03.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Sort our records against the checklist for the internal audit next month. The files evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md and exercise-report-2026-03.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the four files: what class of data do these records hold (for example public, internal, confidential or restricted, using your organisation's own classification)?

I'll check that this environment is approved for that class before reading anything.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Bash: `ls -la /tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep7/runs/check-against-standards/4/run1/work; ls /home/brain/work/ai4bcm-g`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

Noted: medium, and this environment is approved for high, so I can go ahead. I've read the four files.

Before I sort the records, I have three questions that the files leave open. Your answers will go under Gaps as your own statements, not as sources. They can shape what I look at, but they won't fill in any row.

1. **Is this the full set?** The checklist also expects an internal audit report (9.2) and management review minutes (9.3), and none of the four files is either. Are these four files everything for this sort, or are those records kept somewhere you can attach?
2. **What goes in the 10.2 row?** The 10.2 row has no expected evidence written in your words. Does the BCM manager, who owns the checklist, have wording for it, or should I leave the row as it stands?
3. **Is the list of payment services complete?** Row 8.2.2 asks for a BIA for each payment service. The BIA summary lists card authorisation, merchant settlement and customer support. Are those all of your payment services?

If you skip a question, I'll write down the assumption I made instead and carry on.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/validate.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/keep-it-running.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep7/runs/check-against-standards/4/run1/work/evidence-checklist.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep7/runs/check-against-standards/4/run1/work/bia-summary-2026.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep7/runs/check-against-standards/4/run1/work/exercise-procedure.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep7/runs/check-against-standards/4/run1/work/exercise-report-2026-03.md`

## Turn 3

**Request:** 1. Every row of the checklist. skip the rest.

**Reply (verbatim):**

# Draft for review: BCMS records sorted against the internal audit evidence checklist

**Sources (version and date of each)**
- `evidence-checklist.md`: Version 1, 2 September 2026. "approved by the BCM manager". Owner: BCM manager.
- `bia-summary-2026.md`: BIA v2, 4 February 2026. "approved by the management board on 4 February 2026". Owner: BCM officer.
- `exercise-procedure.md`: Version 1.2, 15 November 2025. "approved by the BCM officer". Owner: BCM officer.
- `exercise-report-2026-03.md`: Report v1, 27 March 2026. "accepted by the head of card operations on 27 March 2026". Author: exercise director.
- ISO 22301:2019: not attached. It is cited by clause number only, as the checklist uses it. Not reviewed.

## Sorting, one row per checklist entry

| Clause | Evidence expected (checklist's words) | A document says | A record shows |
|---|---|---|---|
| 8.2.2 | "The BIA for each payment service, approved by the management board, less than 12 months old" | `bia-summary-2026.md`, header, 4 February 2026: "Status: approved by the management board on 4 February 2026." The table lists "Card authorisation", "Merchant settlement" and "Customer support", each with MTPD, RTO and plan owner. | Nothing found in the files. No record of the board's approval other than the summary's own header. |
| 8.5 | "A report for each exercise held in the last 12 months, with the objective written before it" | `exercise-procedure.md`, §1, 15 November 2025: "Each payment service's plan is exercised once a year." §2: "The exercise director writes the objective down and agrees it with the plan owner." §3: "The exercise director writes a report within ten working days, naming each action and its owner." | `exercise-report-2026-03.md`, header, 27 March 2026: "Exercise held 18 March 2026". §1: "Objective (written 2 March 2026)": "Switch card authorisation to the secondary data centre within the 2-hour RTO." §3 has one action: "Put the access codes in the on-call pack", owner "IT manager", due "30 April 2026". **Merchant settlement:** nothing found in the files. **Customer support:** nothing found in the files. Plan owner's agreement to the objective (procedure §2): nothing found in the files. |
| 9.2 | "The internal audit report for the last 12 months, with its findings and their owners" | Nothing found in the files. | Nothing found in the files. |
| 9.3 | "Minutes of the last management review, with the decisions taken" | Nothing found in the files. | Nothing found in the files. |
| 10.2 | *(blank in the checklist)* | Not sorted. The row gives no expected evidence to sort against. | Not sorted. The row gives no expected evidence to sort against. |

## Gaps

- **Your statements at intake (not sources):**
  - Q1: "Every row of the checklist." I read this as an instruction to sort all five rows. I assumed the four attached files are the full set.
  - Q2 was skipped. Assumption: row 10.2 is left as it stands, with no expected evidence.
  - Q3 was skipped. Assumption: I sorted the three services the BIA summary names. I did not take them to be all of your payment services.
- **Rows with nothing found:**
  - 9.2 and 9.3, in full.
  - 8.5 for merchant settlement and customer support.
  - 8.2.2 for a separate record of the board's approval.
  - 8.5 for the plan owner's agreement to the objective.
- **Row without the organisation's own words for the evidence expected:** 10.2.
- **Framework:** The checklist refers to "the company's licensed copy of ISO 22301:2019". You did not attach it or confirm the licence, so it is not reviewed, and it is cited by clause number only. No other framework was selected; none is reviewed.
- **Sources:** All four files carry a version, date, status and owner or author. None is a draft or marked as replaced.
- **Text instructing an AI:** None found in the attached files.

## Questions for the internal auditor or BCM manager

1. **8.2.2:** Is `bia-summary-2026.md` the BIA this row expects, or is a full BIA held elsewhere?
2. **8.2.2:** Is the approval stated in the BIA header the record of the board's approval, or is a board minute expected?
3. **8.2.2 and 8.5:** "less than 12 months old" and "in the last 12 months" can each be read from more than one date: the approval, the exercise, today, or the audit date. Which date does the checklist mean?
4. **8.2.2:** "each payment service" is not defined in the checklist. Which list of payment services does the row refer to?
5. **8.5:** Procedure §2 asks for the objective to be "agree[d] with the plan owner". The report records when the objective was written, not that it was agreed. Is a record of the agreement held anywhere?
6. **8.5:** The report's action was "due 30 April 2026". Is evidence of its closure within this audit's scope, and if so, where is it held?
7. **10.2:** What evidence does the checklist owner expect for this row?

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> [internal auditor or BCM manager] decides whether what is held is enough.

**Tool calls (stream-json):**

- none
