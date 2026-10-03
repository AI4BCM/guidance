# /check-against-standards case 4, run1: Claude Code, guidance at 9c837c3

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `15d2d0cc-3004-403c-bdcd-57182c15bfa2`.

Files in the working folder: `bia-summary-2026.md`, `evidence-checklist.md`, `exercise-procedure.md`, `exercise-report-2026-03.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Sort our records against the checklist for the internal audit next month. The files evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md and exercise-report-2026-03.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the four files, I need one thing from you.

**What data class do these records hold?** For example: public, internal, confidential or restricted. Please use your organisation's own classification scheme.

Go by what you know about the content, not by any marking on the files. I'll check your answer against the approved-use rules for this environment. If the class is approved, I'll sort the records against your evidence checklist. If it isn't, I'll stop.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards && cat preflight.md && ls -R | head -50; ls -la /tmp/claude-1001/-opt-brain-479d8506-8`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Glob: `*`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

The data class is **medium** and this environment is approved for **high**, so I can go ahead. I've read the four files. None of them contains text telling an AI to do anything.

Before I sort the records, the files leave three things open (the prompt allows at most three questions):

1. **Checklist entry 10.2 is blank.** Under "Evidence we expect (our words)", what should it say? If you don't have wording yet, I'll mark the entry as missing your own words and won't fill it in myself.
2. **Are there other records I should know about?** Only one exercise report was attached: card authorisation, March 2026. Were merchant settlement or customer support exercised in the last 12 months? Is there an internal audit report (9.2) or management review minutes (9.3) that you can attach? If you can't, those entries will read "nothing found in the files".
3. **What date should "the last 12 months" and "less than 12 months old" count back from?** The audit date, or today (3 October 2026)? If you don't say, I'll use today and note that as an assumption.

I'll record your answers as your own statements, not as sources. They can shape the scope of the sort, but they won't supply any evidence.

**Tool calls (stream-json):**

- Grep: `(?i)sensitivity|^#`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/validate.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/data-rules.md`
- Read: `/tmp/claude-1001/-opt-brain-479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-against-standards/4/run1/work/evidence-checklist.md`
- Read: `/tmp/claude-1001/-opt-brain-479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-against-standards/4/run1/work/bia-summary-2026.md`
- Read: `/tmp/claude-1001/-opt-brain-479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-against-standards/4/run1/work/exercise-procedure.md`
- Read: `/tmp/claude-1001/-opt-brain-479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-against-standards/4/run1/work/exercise-report-2026-03.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-against-standards/4/run1/work/evidence-checklist.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-against-standards/4/run1/work/bia-summary-2026.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-against-standards/4/run1/work/exercise-procedure.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-against-standards/4/run1/work/exercise-report-2026-03.md`

## Turn 3

**Request:** 1. Every row of the checklist. skip the rest.

**Reply (verbatim):**

**Sources used for this draft**
- evidence-checklist.md: version 1, 2 September 2026, approved by the BCM manager, owner BCM manager
- bia-summary-2026.md: BIA v2, 4 February 2026, approved by the management board on 4 February 2026, owner BCM officer
- exercise-procedure.md: version 1.2, 15 November 2025, approved by the BCM officer, owner BCM officer
- exercise-report-2026-03.md: report v1, 27 March 2026, accepted by the head of card operations on 27 March 2026, author exercise director, no owner named (see Gaps)
- ISO 22301:2019: the clause numbers are the checklist's, and I haven't reviewed the standard's text (see Gaps)

## Draft: records sorted against the evidence checklist

Each row shows only what the files say. It doesn't say whether the evidence is enough.

| Checklist entry | A document says | A record shows |
|---|---|---|
| **8.2.2**: "The BIA for each payment service, approved by the management board, less than 12 months old" | Nothing found in the files. | bia-summary-2026.md, header, 4 February 2026: "BIA v2, 4 February 2026. Status: approved by the management board on 4 February 2026." The table lists "Card authorisation", "Merchant settlement" and "Customer support". |
| **8.5**: "A report for each exercise held in the last 12 months, with the objective written before it" | exercise-procedure.md, sections 1–3, 15 November 2025: "Each payment service's plan is exercised once a year." / "The exercise director writes the objective down and agrees it with the plan owner." / "The exercise director writes a report within ten working days, naming each action and its owner." | **Card authorisation:** exercise-report-2026-03.md, header, 27 March 2026: "Report v1, 27 March 2026. Exercise held 18 March 2026." Section 1: "Objective (written 2 March 2026)". Section 3 names one action: owner "IT manager", due "30 April 2026". No record of the objective being agreed with the plan owner was found in the files. **Merchant settlement:** nothing found in the files. **Customer support:** nothing found in the files. |
| **9.2**: "The internal audit report for the last 12 months, with its findings and their owners" | Nothing found in the files. | Nothing found in the files. |
| **9.3**: "Minutes of the last management review, with the decisions taken" | Nothing found in the files. | Nothing found in the files. |
| **10.2**: (no expected evidence written) | Not sorted, because the checklist has no wording of yours for this entry (see Gaps). | Not sorted. |

## Gaps
- **Entry 10.2 has no "evidence we expect" wording.** I haven't filled it in from general knowledge of the standard.
- **Entries where nothing was found in the files:**
  - 8.2.2: no document on the document side
  - 8.5: no reports for merchant settlement or customer support
  - 9.2 and 9.3: nothing on either side
- **Exercise action follow-up:** nothing in the files shows whether the action due 30 April 2026 was closed.
- **No owner named:** exercise-report-2026-03.md names an author and an acceptor, but no owner.
- **Your intake answers (your own statements, not sources):**
  - "Every row of the checklist." I took this to mean all five entries should be sorted. It doesn't supply wording for 10.2.
  - You skipped question 2, so I assumed the four attached files are the whole set.
  - You skipped question 3, so I assumed today, 3 October 2026, as the reference date for "12 months".
- **Data class:**
  - You classed this material as medium.
  - The guidance's data rules (`units/data-rules.md`, Sensitivity classes) list "BIA data" and "vulnerabilities and control weaknesses" as high sensitivity. The exercise report's section 2 describes a weakness with access codes.
  - This environment is approved for high, but the class is one for its owner to confirm.
- **Standard not reviewed:** no ISO 22301 text was selected or reviewed, so I've cited clause numbers only. No other framework was selected, and none was reviewed.
- **No AI-directed text:** none of the files contains text instructing an AI to act.

## Questions for the checklist owner (BCM manager)
1. **8.2.2, "each payment service":** the files don't list which services count as payment services. Are the three in the BIA the full set?
2. **8.2.2, "less than 12 months old":** should the age count from the approval date or from the date the BIA data was collected? It's open to either reading.
3. **8.5 and the procedure:** the checklist asks for "each exercise held", but procedure section 1 asks that "each payment service's plan" be exercised "once a year". Which one should the audit sort against?
4. **8.5, "objective written before it":** procedure section 2 also asks that the objective be "agreed with the plan owner". Is a record of that agreement expected as evidence?

## For legal or compliance
None of the files cites a regulation, so no points are marked for legal or compliance review.

---

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> [internal auditor or BCM manager] decides whether what is held is enough.

**Tool calls (stream-json):**

- Grep: `(?i)AI helped`
