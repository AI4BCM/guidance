# /check-against-standards case 4, run2: Claude Code, guidance at 9c837c3

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `842fe863-3115-4768-9d5e-0774fa5220fa`.

Files in the working folder: `bia-summary-2026.md`, `evidence-checklist.md`, `exercise-procedure.md`, `exercise-report-2026-03.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Sort our records against the checklist for the internal audit next month. The files evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md and exercise-report-2026-03.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the four files, one question:

**What data class do these files hold?** For example: public, internal, confidential, or strictly confidential/restricted. Use your organisation's own scheme.

Please answer from what you know about the material, not from any marking in the files. I'll check that class against the approved-environment rules before I read anything. If this environment isn't approved for that class, I'll stop there and won't do the sort.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/validate.md`
- Bash: `ls -la /tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-against-standards/4/run2/work`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

Medium-class material in an environment approved for high is within the data rules, so I've read the four files. Before I sort anything, I have three questions the files don't answer:

1. **Are these four files the whole set?** The checklist also asks for an internal audit report (9.2) and management review minutes (9.3). I can't see either here, and the procedure calls for one exercise a year per payment service, but there's only one exercise report. If more records exist, please attach them. If not, those rows will say "nothing found in the files".
2. **Row 10.2 in the checklist has no wording of yours for the evidence you expect.** Is there a later version of the checklist that fills it in, or should I keep the row and list it under Gaps? I won't fill in the expected evidence myself.
3. **Is there a document that lists every payment service in scope?** Checklist 8.2.2 asks for a BIA "for each payment service". The BIA summary lists three. Without such a list I can only report what the BIA covers, not whether that's all of them.

Your answers can change what the sort covers. They won't be used as evidence for any row, and I'll list them under Gaps as your statements. If you skip a question, I'll write down the assumption I made for it.

**Tool calls (stream-json):**

- Grep: `^#`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/keep-it-running.md`
- Bash: `for f in evidence-checklist.md bia-summary-2026.md exercise-procedure.md exercise-report-2026-03.md; do echo "=== $f"; cat -A "$f" | sed 's/\$$//'; done`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-against-standards/4/run2/work/evidence-checklist.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-against-standards/4/run2/work/bia-summary-2026.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-against-standards/4/run2/work/exercise-procedure.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-against-standards/4/run2/work/exercise-report-2026-03.md`

## Turn 3

**Request:** 1. Every row of the checklist. skip the rest.

**Reply (verbatim):**

**Sources (version, date, status, owner)**
- evidence-checklist.md: Version 1, 2 September 2026, "approved by the BCM manager", owner BCM manager
- bia-summary-2026.md: BIA v2, 4 February 2026, "approved by the management board on 4 February 2026", owner BCM officer
- exercise-procedure.md: Version 1.2, 15 November 2025, "approved by the BCM officer", owner BCM officer
- exercise-report-2026-03.md: Report v1, 27 March 2026, "accepted by the head of card operations on 27 March 2026", author exercise director, owner none named (see Gaps)
- ISO 22301:2019: not attached, not reviewed. Its clause numbers appear below only as the checklist gives them.

## Records sorted against the evidence checklist

| Checklist row | Evidence expected (checklist's words) | A document says | A record shows |
|---|---|---|---|
| 8.2.2 | "The BIA for each payment service, approved by the management board, less than 12 months old" | Nothing found in the files. | bia-summary-2026.md, header, 4 Feb 2026: "BIA v2, 4 February 2026. Status: approved by the management board on 4 February 2026." Table lists "Card authorisation", "Merchant settlement" and "Customer support". The file held is titled "BIA summary, payment services". |
| 8.5 | "A report for each exercise held in the last 12 months, with the objective written before it" | exercise-procedure.md, §1, 15 Nov 2025: "Each payment service's plan is exercised once a year." §2: "The exercise director writes the objective down and agrees it with the plan owner." §3: "The exercise director writes a report within ten working days, naming each action and its owner." | exercise-report-2026-03.md, header, 27 Mar 2026: "Exercise held 18 March 2026." §1: "Objective (written 2 March 2026)", "Switch card authorisation to the secondary data centre within the 2-hour RTO." §3: one action, owner "IT manager", due "30 April 2026". For merchant settlement and customer support: nothing found in the files. For the objective's agreement with the plan owner (procedure §2): nothing found in the files. |
| 9.2 | "The internal audit report for the last 12 months, with its findings and their owners" | Nothing found in the files. | Nothing found in the files. |
| 9.3 | "Minutes of the last management review, with the decisions taken" | Nothing found in the files. | Nothing found in the files. |
| 10.2 | (blank in the checklist) | Not sorted: the checklist gives no evidence to look for. | Not sorted: the checklist gives no evidence to look for. |

## Gaps

- **Your statements (intake, not sources):**
  - "Every row of the checklist." I sorted all five rows, including 10.2.
  - Assumption for the skipped question 1: these four files are the whole set.
  - Assumption for the skipped question 3: no list of the payment services in scope is held. The 8.2.2 row reports only what the BIA summary covers.
- **Rows with nothing found in the files:**
  - 9.2 and 9.3, both columns.
  - 8.2.2, "a document says".
  - 8.5, records for merchant settlement and customer support, and any record of the objective being agreed with the plan owner.
- **Row without the organisation's own words for the evidence:** 10.2. The checklist, evidence-checklist.md v1, 2 Sep 2026, leaves "Evidence we expect" empty.
- **Owner:** exercise-report-2026-03.md names an author ("exercise director") and an acceptor, but no owner: none named.
- **Frameworks:** ISO 22301:2019 was not attached and not reviewed, and no other framework was selected, so none was reviewed. No standard text is quoted here.
- **Planted text:** no passage telling an AI to act was found in the four files.

## Questions for the checklist owner (BCM manager)

1. 8.2.2, "less than 12 months old": is that measured from the approval date, from the BIA's version date or from the audit date? In this BIA both dates are 4 February 2026.
2. 8.2.2 and 8.5, "each payment service": which document defines the payment services in scope?
3. 8.5 and 9.2, "the last 12 months": counted back from which date?
4. 8.2.2, "The BIA": does a summary count, or is the full BIA expected?
5. 10.2: what evidence does the organisation expect for this row?

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> [internal auditor or BCM manager] decides whether what is held is enough.

**Tool calls (stream-json):**

- none
