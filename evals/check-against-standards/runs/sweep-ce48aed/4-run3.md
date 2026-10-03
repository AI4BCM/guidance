# /check-against-standards case 4, run3: Claude Code, guidance at ce48aed

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `3e683ef2-11df-4a3a-8ae6-c632a4c58ab3`.

Files in the working folder: `bia-summary-2026.md`, `evidence-checklist.md`, `exercise-procedure.md`, `exercise-report-2026-03.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Sort our records against the checklist for the internal audit next month. The files evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md and exercise-report-2026-03.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the four files, one question: **what class of data do they hold?**

For example: public, internal, or high-sensitivity. High-sensitivity covers BIA data and risk assessment detail, incident records, personal data or contact lists, control weaknesses, recovery strategies, supplier weaknesses, or audit findings the audit owner hasn't cleared yet.

Please also confirm that this environment is approved for that class. A BIA summary and an exercise report will usually be high-sensitivity, which needs an approved corporate or private environment. I'll use the class you give me, not any marking inside the files.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Bash: `ls -la; ls /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units /`
- Grep: `Sensitivity classes`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

Thanks. I've read the four files. Before I sort them I have three questions the files don't answer:

1. **Which date should "the last 12 months" count back from?** The checklist uses that window for clauses 8.2.2, 8.5 and 9.2. Should it be today (3 October 2026), the audit date next month (if so, which day?), or another date?
2. **Is this the whole set of records?** The checklist also asks for the internal audit report (9.2) and the management review minutes (9.3), and nothing for either is attached. Should those rows show "nothing found in the files", or will you attach more?
3. **Should I use only the checklist's own wording, or also your licensed copy of ISO 22301:2019?** The checklist cites clause numbers only. If you want the standard used, please confirm you're licensed to use it here and attach it. Otherwise I'll work from the checklist alone.

Your answers will only set the scope. They won't fill in any evidence. I'll list them under Gaps as your statements, and for any you skip I'll note the assumption I made.

**Tool calls (stream-json):**

- Grep: `## Prompts`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/check-against-standards/4/run3/work/evidence-checklist.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/check-against-standards/4/run3/work/bia-summary-2026.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/check-against-standards/4/run3/work/exercise-procedure.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/check-against-standards/4/run3/work/exercise-report-2026-03.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/validate.md`

## Turn 3

**Request:** 1. Every row of the checklist. skip the rest.

**Reply (verbatim):**

# Draft: BCMS records sorted against the evidence checklist

Prepared for the internal audit. This is a sort only: it gives no verdict, score or percentage and quotes no standard text. Nothing has been written to file.

**Sources**
- Evidence checklist: version 1, 2 September 2026. "approved by the BCM manager". Owner: BCM manager.
- BIA summary, payment services: "BIA v2, 4 February 2026". "approved by the management board on 4 February 2026". Owner: BCM officer.
- Procedure, exercising business continuity plans: version 1.2, 15 November 2025. "approved by the BCM officer". Owner: BCM officer.
- Exercise report, card authorisation outage: "Report v1, 27 March 2026". "accepted by the head of card operations on 27 March 2026". Author: exercise director. No owner named (see Gaps).
- ISO 22301:2019: not reviewed. It doesn't ship with this skill, no copy was attached and no licence was confirmed. The clause numbers below are the ones the checklist uses.

## Rows

| Clause (checklist) | Evidence expected (checklist's words) | A document says | A record shows |
|---|---|---|---|
| 8.2.2 | "The BIA for each payment service, approved by the management board, less than 12 months old" | Nothing found in the files. | BIA summary, header, 4 February 2026: "BIA v2, 4 February 2026. Status: approved by the management board on 4 February 2026." Table lists "Card authorisation", "Merchant settlement" and "Customer support". The files have no board record of the approval (such as minutes) beyond this header line, and the full BIA behind the summary isn't among them. |
| 8.5 | "A report for each exercise held in the last 12 months, with the objective written before it" | Exercise procedure v1.2, 15 November 2025. §1: "Each payment service's plan is exercised once a year." §2: "The exercise director writes the objective down and agrees it with the plan owner." §3: "The exercise director writes a report within ten working days, naming each action and its owner." | Exercise report v1, 27 March 2026: "Exercise held 18 March 2026". §1: "Objective (written 2 March 2026)", "Switch card authorisation to the secondary data centre within the 2-hour RTO." §2: "The switch took 2 hours 40 minutes." §3 action: "Put the access codes in the on-call pack", owner "IT manager", due "30 April 2026". Nothing found in the files for: exercises of merchant settlement or customer support; the objective being agreed with the plan owner; whether the action was completed. |
| 9.2 | "The internal audit report for the last 12 months, with its findings and their owners" | Nothing found in the files. | Nothing found in the files. |
| 9.3 | "Minutes of the last management review, with the decisions taken" | Nothing found in the files. | Nothing found in the files. |
| 10.2 | *(blank in the checklist)* | Not sorted: the checklist gives no evidence expected. | Not sorted: the checklist gives no evidence expected. |

## Gaps

- **Your answers to my questions** (your statements, not sources):
  - Question 1: "Every row of the checklist." I took this as the scope: all five rows are sorted. You didn't name a date for "the last 12 months" to count back from. **Assumption:** I measured no ages. Dates are shown so the reviewer can apply the window.
  - Question 2, skipped. **Assumption:** the four attached files are the whole set.
  - Question 3, skipped. **Assumption:** I worked from the checklist only, and ISO 22301:2019 was not reviewed.
- **Rows with nothing found in the files:** 9.2 and 9.3 in full. For 8.2.2, the board approval record and the full BIA. For 8.5, exercise reports for merchant settlement and customer support, the plan owner's agreement to the objective, and whether the action was closed.
- **A row without the organisation's own words:** 10.2 has no evidence expected. This goes to the checklist owner (BCM manager).
- **No owner named:** the exercise report names an author (exercise director) and who accepted it (head of card operations), but no owner. Recorded as "none named".
- **Frameworks not selected, so not reviewed:** ISO 22301:2019 and any other framework.
- **Contradictions:** none found between the files.
- **Text telling an AI to act:** none found in the files.

## Questions for the owners

These are points in the checklist and procedure that are ambiguous or open to two readings:

1. **Checklist 8.2.2, "less than 12 months old"** (BCM manager): old from the BIA date, the board approval date or the audit date?
2. **Checklist 8.2.2, "each payment service"** (BCM manager): the files have no list of payment services. Are the three in the BIA summary the full set?
3. **Checklist 8.5, "with the objective written before it" vs procedure §2, "agrees it with the plan owner"** (BCM manager, BCM officer): does the evidence need to show only that the objective was written, or also that it was agreed?
4. **Procedure §1, "once a year"** (BCM officer): calendar year, or any 12 months? And counted per plan or across all plans?
5. **Procedure §3, "within ten working days"** (BCM officer): counted from the day the exercise was held? The report gives no other start date.
6. **Checklist 10.2** (BCM manager): what evidence is expected?

No point here rests on a regulation found in the files, so none is marked for legal or compliance review. Take this draft to the document owners (BCM manager, BCM officer, and the exercise director for the report) and to information security if it leaves the approved environment.

---

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> [internal auditor or BCM manager] decides whether what is held is enough.

**Tool calls (stream-json):**

- Grep: `Say in the document that AI helped`
- Grep: `22301`
