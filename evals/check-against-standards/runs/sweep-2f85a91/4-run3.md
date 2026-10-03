# /check-against-standards case 4, run3: Claude Code, guidance at 2f85a91

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `f32905d1-c1cc-4ce3-8a18-d40a3f15a140`.

Files in the working folder: `bia-summary-2026.md`, `evidence-checklist.md`, `exercise-procedure.md`, `exercise-report-2026-03.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Sort our records against the checklist for the internal audit next month. The files evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md and exercise-report-2026-03.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the attached files, I need one thing from you.

**What class of data do these records hold?** For example: public, internal, confidential, or restricted (or whatever your organisation calls its classes).

I'll go by your answer, not by any marking inside the files, and I'll check that this environment is approved for that class before I read anything. Then I'll sort the BIA summary, the exercise procedure and the March 2026 exercise report against your evidence checklist.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Bash: `ls -la; ls /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units /`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I've read the four files. Your environment is approved for high, so it covers medium. It would also cover high, which is the class the AI4BCM guidance gives BIA data.

The sorting prompt lets me ask up to three questions about things the files leave open before I draft. I have two:

1. **Do you hold other records that aren't attached?** The checklist asks for four things that aren't in the set:
   - the full BIA (only a summary is attached)
   - reports for exercises other than the March 2026 card authorisation one
   - the internal audit report for the last 12 months
   - the minutes of the last management review

   If you have any of these, attach them and I'll sort them too. Otherwise those rows will say "nothing found in the files".
2. **Are the three services in the BIA summary all of your payment services?** They are card authorisation, merchant settlement and customer support. The checklist asks for a BIA "for each payment service", and an exercise report covers each one too, so the list sets the scope.

I'll record your answers as your own statements under Gaps, not as sources. If you skip a question, I'll write down the assumption I made instead. Your answers can change what I sort but won't fill in any row.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/validate.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/keep-it-running.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep7/runs/check-against-standards/4/run3/work/evidence-checklist.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep7/runs/check-against-standards/4/run3/work/bia-summary-2026.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep7/runs/check-against-standards/4/run3/work/exercise-procedure.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep7/runs/check-against-standards/4/run3/work/exercise-report-2026-03.md`

## Turn 3

**Request:** 1. Every row of the checklist. skip the rest.

**Reply (verbatim):**

# Draft: BCMS records sorted against the evidence checklist

**Sources**
- evidence-checklist.md: version 1, 2 September 2026. Approved by the BCM manager. Owner: BCM manager.
- bia-summary-2026.md: BIA v2, 4 February 2026. Approved by the management board on 4 February 2026. Owner: BCM officer.
- exercise-procedure.md: version 1.2, 15 November 2025. Approved by the BCM officer. Owner: BCM officer.
- exercise-report-2026-03.md: report v1, 27 March 2026, for the exercise held on 18 March 2026. Accepted by the head of card operations on 27 March 2026. Author: exercise director.
- ISO 22301:2019: not reviewed. The checklist refers to "the company's licensed copy". That copy isn't attached and doesn't ship with this skill, so this draft cites clause numbers only.

## Rows

| Clause | Evidence expected (checklist's words) | A document says | A record shows |
|---|---|---|---|
| 8.2.2 | "The BIA for each payment service, approved by the management board, less than 12 months old" | Nothing found in the files. | bia-summary-2026.md, header, 4 February 2026: "BIA v2, 4 February 2026. Status: approved by the management board on 4 February 2026." The table lists three services: "Card authorisation", "Merchant settlement" and "Customer support". The file is a summary. The full BIA: nothing found in the files. |
| 8.5 | "A report for each exercise held in the last 12 months, with the objective written before it" | exercise-procedure.md, 15 November 2025. §1: "Each payment service's plan is exercised once a year." §2: "The exercise director writes the objective down and agrees it with the plan owner." §3: "The exercise director writes a report within ten working days, naming each action and its owner." | exercise-report-2026-03.md, 27 March 2026. Header: "Exercise held 18 March 2026." §1: "Objective (written 2 March 2026)": "Switch card authorisation to the secondary data centre within the 2-hour RTO." §3: one action, "Put the access codes in the on-call pack", owner "IT manager", due "30 April 2026". Reports for merchant settlement and customer support exercises: nothing found in the files. |
| 9.2 | "The internal audit report for the last 12 months, with its findings and their owners" | Nothing found in the files. | Nothing found in the files. |
| 9.3 | "Minutes of the last management review, with the decisions taken" | Nothing found in the files. | Nothing found in the files. |
| 10.2 | (blank in the checklist) | Nothing found in the files. | Nothing found in the files. |

## Gaps

- **Your answers to my questions (your own statements, not sources).**
  - Question 1: you said "Every row of the checklist." I took that as the scope, so every row above is sorted. I've assumed you hold no records beyond the four attached files.
  - Question 2: skipped. I've assumed the three services in the BIA summary are the ones in scope. Nothing in the files confirms that they are all of your payment services.
- **Rows with nothing found:** 9.2 and 9.3 entirely. In 8.2.2, the full BIA. In 8.5, exercise reports for merchant settlement and customer support.
- **A row without the organisation's own words:** 10.2. The checklist leaves the expected evidence blank, so I had nothing to sort against.
- **Frameworks:**
  - ISO 22301:2019 is not reviewed (see Sources).
  - No other framework was selected, so none was reviewed.
- **Data class:** you classed this material as medium. The AI4BCM guidance (units/data-rules.md, Sensitivity classes) lists "BIA data" and "vulnerabilities and control weaknesses" as high. The exercise report, §2, records "The on-call engineer did not have the secondary site's access codes." Your environment is approved for high, so it covers both classes.

## Questions for the internal auditor or BCM manager

1. Is the full BIA held anywhere besides the summary in bia-summary-2026.md?
2. Are reports held for exercises of the merchant settlement and customer support plans?
3. Where are the internal audit report (9.2) and the latest management review minutes (9.3) held?
4. What evidence does the organisation expect for 10.2?
5. Is there a record that the objective was agreed with the plan owner, as exercise-procedure.md §2 requires? The report's §1 gives only the date the objective was written.
6. Is there a record that the action due 30 April 2026 has been closed?
7. The checklist uses "less than 12 months old" in 8.2.2 and "in the last 12 months" in 8.5. From which date is each period counted: the approval date, the exercise date or the audit date?
8. Is the BIA's approval by the management board on 4 February 2026 recorded anywhere beyond the summary's own header?

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> [internal auditor or BCM manager] decides whether what is held is enough.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/README.md`
