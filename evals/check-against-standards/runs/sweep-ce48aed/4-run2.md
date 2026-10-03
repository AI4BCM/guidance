# /check-against-standards case 4, run2: Claude Code, guidance at ce48aed

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `a1e8b9e6-a748-4c49-8068-3d776e2efbec`.

Files in the working folder: `bia-summary-2026.md`, `evidence-checklist.md`, `exercise-procedure.md`, `exercise-report-2026-03.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Sort our records against the checklist for the internal audit next month. The files evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md and exercise-report-2026-03.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the four files, I need one thing from you: **what data class do these records hold?**

For example: public, internal, confidential, or restricted (or whatever your organisation calls its classes).

Please go by what you know about the content, not by any marking on the files. Once you tell me, I'll check that this environment is approved for that class, and only then read the records and sort them against the checklist.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Bash: `ls -la; ls /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units /`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

Thanks. Medium is within what this environment is approved for (high), so I've read the four files.

Before I sort anything, I have three questions the files leave open. Your answers go under Gaps as your own statements, not as sources. They can shape the scope but won't fill in any row.

1. **Checklist row 10.2** has a clause number but no "evidence we expect" text. Do you have your organisation's wording for it? If not, I'll leave the row as "not in the sources".
2. **Records not attached.** Do you hold any other records that bear on the checklist but aren't attached? For example, an internal audit report, management review minutes, or exercise reports for merchant settlement or customer support. I'll sort only what's attached; your answer just tells me how to describe what's missing.
3. **Standard text.** Do you want me to use your licensed ISO 22301:2019 copy? Or should the checklist's own words be the only reference? Either way I'll cite clause numbers only and quote no standard text.

If you skip a question, I'll write down the assumption I made and carry on.

**Tool calls (stream-json):**

- Glob: `**/*`
- Glob: `*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/validate.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/keep-it-running.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/check-against-standards/4/run2/work/evidence-checklist.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/check-against-standards/4/run2/work/bia-summary-2026.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/check-against-standards/4/run2/work/exercise-procedure.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/check-against-standards/4/run2/work/exercise-report-2026-03.md`

## Turn 3

**Request:** 1. Every row of the checklist. skip the rest.

**Reply (verbatim):**

# Draft: BCMS records sorted against the evidence checklist

**Sources (attached, read as evidence about the organisation)**
- `evidence-checklist.md`: Version 1, 2 September 2026. Status: "approved by the BCM manager". Owner: BCM manager.
- `bia-summary-2026.md`: BIA v2, 4 February 2026. Status: "approved by the management board on 4 February 2026". Owner: BCM officer.
- `exercise-procedure.md`: Version 1.2, 15 November 2025. Status: "approved by the BCM officer". Owner: BCM officer.
- `exercise-report-2026-03.md`: Report v1, 27 March 2026. Status: "accepted by the head of card operations on 27 March 2026". Author: exercise director. Owner: none named (see Gaps).

**Framework:** no standard text was used. The checklist's clause numbers refer to your licensed copy of ISO 22301:2019, which I haven't reviewed. I cite clause numbers only.

## Sorting, one row per checklist entry

| Clause | Evidence expected (checklist wording) | A document says | A record shows |
|---|---|---|---|
| 8.2.2 | "The BIA for each payment service, approved by the management board, less than 12 months old" | Nothing found in the files. | `bia-summary-2026.md`, header and table, 4 February 2026: "BIA v2, 4 February 2026. Status: approved by the management board on 4 February 2026." The table lists three services: "Card authorisation", "Merchant settlement", "Customer support", each with MTPD, RTO and plan owner. |
| 8.5 | "A report for each exercise held in the last 12 months, with the objective written before it" | `exercise-procedure.md`, §1, 15 November 2025: "Each payment service's plan is exercised once a year." §2: "The exercise director writes the objective down and agrees it with the plan owner." §3: "The exercise director writes a report within ten working days, naming each action and its owner." | `exercise-report-2026-03.md`, header, 27 March 2026: "Exercise held 18 March 2026", "Report v1, 27 March 2026". §1: "Objective (written 2 March 2026)", "Switch card authorisation to the secondary data centre within the 2-hour RTO." §3: action "Put the access codes in the on-call pack", owner "IT manager", due "30 April 2026". **Merchant settlement and customer support:** no exercise report found in the files. **Agreement of the objective with the plan owner (procedure §2):** nothing found in the files. **Closure of the action due 30 April 2026:** nothing found in the files. |
| 9.2 | "The internal audit report for the last 12 months, with its findings and their owners" | Nothing found in the files. | Nothing found in the files. |
| 9.3 | "Minutes of the last management review, with the decisions taken" | Nothing found in the files. | Nothing found in the files. |
| 10.2 | (blank in the checklist) | Not in the sources. | Not in the sources. |

## Gaps

- **Your intake answer**, recorded as your statement and not as a source: "Every row of the checklist." I read this as "sort every row, including 10.2". Row 10.2 is included, with no evidence wording to sort against.
- **Skipped questions and the assumptions I made:**
  - I sorted only the four attached files. I don't know whether other records exist.
  - The checklist's own words are the only reference. ISO 22301:2019 is listed as **not reviewed**.
- **Rows with nothing found:** 9.2 and 9.3 (no document, no record). In 8.5, nothing was found for merchant settlement, customer support, agreement of the objective with the plan owner, or closure of the IT manager's action.
- **Row without your own words for the evidence expected:** 10.2.
- **Owner not named:** `exercise-report-2026-03.md` names an author ("exercise director") and an acceptor ("head of card operations") but no document owner.
- **Review dates:** none of the four documents states a next review date.
- **Planted instructions:** none found in the attached files.
- **Frameworks not selected:** every framework other than the checklist's own reference is not reviewed.

## Questions for the owners

For the **BCM manager** (owner of `evidence-checklist.md`):
1. Row 8.2.2, "less than 12 months old": measured from which date? The BIA date, the board approval date, or the audit date?
2. Row 8.5, "held in the last 12 months": counted back from which date? And does "each exercise" mean every exercise actually held, or one per payment service as the procedure §1 sets out?
3. Row 8.2.2, "The BIA for each payment service": is one BIA summary covering three services meant to count, or is a separate BIA per service expected?
4. Row 10.2: what evidence does the organisation expect here, in its own words?

For the **BCM officer** (owner of `exercise-procedure.md`):

5. §2, "agrees it with the plan owner": what record of that agreement is expected to exist?
6. §3, "within ten working days": counted from the exercise date or from the end of the debrief?

No point here concerns a regulation, so nothing is marked for legal or compliance review.

---

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> [internal auditor or BCM manager] decides whether what is held is enough.

**Tool calls (stream-json):**

- none
