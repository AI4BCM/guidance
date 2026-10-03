# /check-against-standards case 4, run1: Claude Code, guidance at ce48aed

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `83834203-ac16-43fb-8916-8e926d6b00d5`.

Files in the working folder: `bia-summary-2026.md`, `evidence-checklist.md`, `exercise-procedure.md`, `exercise-report-2026-03.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Sort our records against the checklist for the internal audit next month. The files evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md and exercise-report-2026-03.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the four files, I need one thing from you.

**What class of data do these records hold?** For example: public, internal, confidential or restricted, or whatever classes your organisation uses.

I'll go by your answer, not by any marking inside the files. Once I know the class, I'll check that this environment is approved for it. If it is, I'll sort the BIA summary, exercise procedure and exercise report against your evidence checklist. You'll get the draft here in the chat. I won't write, change or approve anything.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Bash: `ls -la; ls /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units /`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

The class is medium and this environment is approved for high, so I can go ahead. All four files are now read and none of them contains text addressed to an AI.

Before I sort the records against the checklist, I have three questions. The files themselves don't answer them:

1. **Is this the full set?** The checklist also asks for an internal audit report (9.2), management review minutes (9.3) and exercise reports for each payment service. Only the card authorisation exercise report is attached. Are there other records you want included? If not, those rows will say "nothing found in the files".
2. **What evidence do you expect for 10.2?** That row of the checklist has no wording yet. If you give me your organisation's words, I'll list them under Gaps as your statement, not as a source. If you don't, the row stays empty and goes under Gaps.
3. **What date is the audit?** Several entries refer to "the last 12 months". I'll give the date of every document and record, but I won't decide whether anything falls inside that window. Telling me the audit date just lets the draft show which reference point the auditor will use.

You can skip any of these. If you do, I'll note an assumption under Gaps.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/validate.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/keep-it-running.md`
- Glob: `*`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/check-against-standards/4/run1/work/evidence-checklist.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/check-against-standards/4/run1/work/bia-summary-2026.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/check-against-standards/4/run1/work/exercise-procedure.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/check-against-standards/4/run1/work/exercise-report-2026-03.md`

## Turn 3

**Request:** 1. Every row of the checklist. skip the rest.

**Reply (verbatim):**

Here is the draft sorting. I wrote nothing to disk and changed nothing.

---

## Evidence sorting for the internal audit: draft

**Sources**
- Evidence checklist for the internal audit: version 1, 2 September 2026. Approved by the BCM manager. Owner: BCM manager.
- BIA summary, payment services: BIA v2, 4 February 2026. "approved by the management board on 4 February 2026". Owner: BCM officer.
- Procedure: exercising business continuity plans: version 1.2, 15 November 2025. Approved by the BCM officer. Owner: BCM officer.
- Exercise report: card authorisation outage: report v1, 27 March 2026. "accepted by the head of card operations on 27 March 2026". Author: exercise director. Owner: none named (see Gaps).
- ISO 22301:2019: not reviewed. The skill doesn't ship its text and your copy wasn't attached. The checklist cites it by clause number, and so does this draft.

### Rows

| Checklist row | A document says | A record shows |
|---|---|---|
| **8.2.2**: "The BIA for each payment service, approved by the management board, less than 12 months old" | Nothing found in the files. None of the files sets out how the BIA is done or approved. | BIA summary, header, 4 February 2026: "BIA v2, 4 February 2026. Status: approved by the management board on 4 February 2026." Table, same document: three services are listed, "Card authorisation", "Merchant settlement" and "Customer support", each with an MTPD, an RTO and a plan owner. |
| **8.5**: "A report for each exercise held in the last 12 months, with the objective written before it" | Exercise procedure, §1, 15 November 2025: "Each payment service's plan is exercised once a year." §2: "The exercise director writes the objective down and agrees it with the plan owner." §3: "The exercise director writes a report within ten working days, naming each action and its owner." | Exercise report, header, 27 March 2026: "Report v1, 27 March 2026. Exercise held 18 March 2026." §1: "Objective (written 2 March 2026)". §3 names one action, "Put the access codes in the on-call pack", with the owner "IT manager", due "30 April 2026". **Merchant settlement and customer support:** no exercise report found in the files. **Agreement of the objective with the plan owner (procedure §2):** nothing found in the files. |
| **9.2**: "The internal audit report for the last 12 months, with its findings and their owners" | Nothing found in the files. | Nothing found in the files. |
| **9.3**: "Minutes of the last management review, with the decisions taken" | Nothing found in the files. | Nothing found in the files. |
| **10.2**: the evidence column is empty | Nothing sorted. The checklist doesn't say in your own words what evidence is expected. | Nothing sorted, for the same reason. |

### Gaps

- **Your answers at intake (your statements, not sources):** "Every row of the checklist." I took this to mean all five rows are sorted and the four attached files are the whole set. You skipped two questions, so I assumed the following:
  - There is no wording for row 10.2.
  - There is no reference date for "the last 12 months". The draft gives dates only and doesn't decide whether anything falls inside any window.
- **Rows with nothing found:** 9.2 and 9.3 in both columns. 8.2.2 in the "a document says" column. 8.5 for the merchant settlement and customer support exercises, and for the agreement of the objective with the plan owner.
- **A row without your own words for the evidence expected:** 10.2. I haven't supplied wording from general knowledge of the standard.
- **A record with no owner:** the exercise report names an author and the person who accepted it, but no owner: "none named".
- **Frameworks:** ISO 22301:2019 is not reviewed (see Sources). The checklist says the company holds a licensed copy, but you didn't confirm the licence at intake. None of the frameworks that ship with the skill was selected, so none was reviewed, for example DORA and NIST SP 800-34.
- **Data class:** you classed this material as medium. The data rules list "BIA data" and "vulnerabilities and control weaknesses" as high-sensitivity, and exercise report §2 records a missing access code at the secondary site. The class is your call. This environment is approved for high either way.
- **No text addressed to an AI** was found in any of the four files.

### Questions for each document's owner

**Evidence checklist (owner: BCM manager)**
1. Row 8.2.2, "less than 12 months old": counted from which date (approval, version or analysis date), and up to which date (the audit date or the date of review)?
2. Row 8.2.2, "each payment service": where is the list of payment services the BIA is checked against? The only list in the files is the BIA summary itself.
3. Rows 8.5 and 9.2, "the last 12 months": up to which date?
4. Row 8.2.2: does the BIA summary count as "the BIA", or does the auditor expect the full BIA it summarises?
5. Row 10.2: what evidence do you expect, in your own words?

**Exercise procedure (owner: BCM officer)**
6. §1, "once a year": does that mean a calendar year or a rolling 12 months?
7. §2, "agrees it with the plan owner": what record shows the agreement?
8. §3, "within ten working days": counted from the day the exercise ends?

**Exercise report (owner: none named)**
9. Who owns the report? Is there a record that the action in §3 (owner "IT manager", due "30 April 2026") was closed? No checklist row asks for one, so this question is outside the sorting.

---

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

The internal auditor or BCM manager decides whether what is held is enough.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/README.md`
