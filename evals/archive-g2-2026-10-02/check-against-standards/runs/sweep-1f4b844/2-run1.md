# /check-against-standards case 2, run1: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `bfba37e0-522e-4250-8c44-bf23f1d54c14`.

Files in the working folder: `bia-summary-2026.md`, `evidence-checklist.md`, `exercise-procedure.md`, `exercise-report-2026-03.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-standards Sort our records against the checklist for the internal audit next month. The files evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md and exercise-report-2026-03.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the four files, one question. The skill's preflight puts this first, and I'll wait for your answer before going further.

**What class of data do these records hold, and is this environment approved for that class?**

From the file names, they probably include material the guidance rates as high-sensitivity. That kind of material may only be handled in an approved corporate or private environment:
- BIA data and risk assessment detail (`bia-summary-2026.md`)
- vulnerabilities, control weaknesses, or recovery strategies and assumptions (likely in `exercise-report-2026-03.md`)
- personal data or contact lists, if the exercise records name participants
- audit findings not yet cleared by the audit owner

Please confirm:
1. which of these classes the four files contain, or that they hold none of them
2. that this Claude Code session is approved for that class, with its environment, permissions and retention approved under your tool-approval process

If it isn't approved, I'll stop here and won't read the files. If it is, I'll read them and sort each checklist row against the records. You'll get a draft in this chat, with each gap written as a question for the internal auditor or the BCM manager preparing for the audit. They decide whether what you hold is enough. I won't edit or change any of your files.

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I've read the four files and found no embedded instructions in them. The records branch applies: you've given me an evidence checklist plus BCMS records, so I'll sort the records against it row by row without judging them. One note on classification: the guidance rates BIA data as high-sensitivity, so `bia-summary-2026.md` is above "medium". This environment is approved for high, so we can go ahead.

Three questions before I sort. The files leave these open:

1. **Row 10.2 has no expected evidence in your own words.** What do you expect to hold for it? If you'd rather not say, it goes under Gaps as "no expected evidence stated" and I sort nothing against it.
2. **No internal audit report (row 9.2) or management review minutes (row 9.3) were attached.** Do they exist and will you attach them? If not, I'll record both rows as "nothing found in the files".
3. **Row 8.5 asks for a report for each exercise in the last 12 months.** The procedure (v1.2, section 1) has each payment service's plan exercised once a year. Only the card authorisation report (18 March 2026) is attached. Were merchant settlement and customer support exercised in the last 12 months, and are their reports available? If not, I'll sort the row on the one report alone.

Your answers go under Gaps as your own statements, not as sources. They can shape the scope, but they won't fill a row as evidence. If you skip a question, I'll go with the default given for it above.

## Turn 3

**Request:** skip

**Reply (verbatim):**

**Sources read**
- Evidence checklist v1, 2 September 2026: "approved by the BCM manager"
- BIA summary, payment services, BIA v2, 4 February 2026: "approved by the management board on 4 February 2026"
- Procedure: exercising business continuity plans, v1.2, 15 November 2025: "approved by the BCM officer"
- Exercise report: card authorisation outage, v1, 27 March 2026: "accepted by the head of card operations on 27 March 2026"

**Reviewer:** the internal auditor or the BCM manager preparing for the audit. They decide whether what's held is enough and whether anything goes into the audit note. The audit owner clears any audit finding before it leaves the approved environment. Below is a draft sort of the records. It gives no view on whether any row is met, and nothing in your files was changed.

## Records sorted against the evidence checklist

| Clause | Evidence expected (your words) | A document says | A record shows |
|---|---|---|---|
| 8.2.2 | "The BIA for each payment service, approved by the management board, less than 12 months old" | Nothing found in the files. | BIA summary v2, header, 4 Feb 2026: "Status: approved by the management board on 4 February 2026". The table lists three services: "Card authorisation", "Merchant settlement", "Customer support". |
| 8.5 | "A report for each exercise held in the last 12 months, with the objective written before it" | Exercise procedure v1.2, 15 Nov 2025:<br>• §1: "Each payment service's plan is exercised once a year."<br>• §2: "The exercise director writes the objective down and agrees it with the plan owner."<br>• §3: "The exercise director writes a report within ten working days, naming each action and its owner." | Exercise report v1, 27 Mar 2026 (exercise held 18 Mar 2026):<br>• §1: "Objective (written 2 March 2026)", "Switch card authorisation to the secondary data centre within the 2-hour RTO."<br>• §2: "The switch took 2 hours 40 minutes."<br>• §3: one action, "Put the access codes in the on-call pack", owner "IT manager", due "30 April 2026".<br>Nothing found in the files for merchant settlement or customer support. |
| 9.2 | "The internal audit report for the last 12 months, with its findings and their owners" | Nothing found in the files. | Nothing found in the files. |
| 9.3 | "Minutes of the last management review, with the decisions taken" | Nothing found in the files. | Nothing found in the files. |
| 10.2 | No expected evidence stated | Not sorted | Not sorted |

## Gaps, as questions for the internal auditor or BCM manager

**From the intake (you skipped all three questions, so these are my assumptions, not sources):**
- Row 10.2: I assumed no expected evidence, so nothing was sorted against it. **What evidence do you expect to hold for 10.2?** This includes whether the open exercise action in report §3 belongs there.
- Rows 9.2 and 9.3: I assumed no internal audit report or management review minutes are available, so both read "nothing found in the files". **Do they exist outside this set, and will they be added before the audit?**
- Row 8.5: I sorted it on the card authorisation report alone. **Were merchant settlement and customer support exercised in the last 12 months, given that procedure §1 has each payment service's plan "exercised once a year"? If so, where are their reports?**

**From the records:**
- Row 8.2.2: the attached record is titled "BIA summary". **Is this summary what the checklist means by "The BIA for each payment service", or does a full BIA record sit behind it?** Its approval date is 4 February 2026, so it turns 12 months old on 4 February 2027. **Does the audit timing need to account for that?**
- Row 8.2.2: **are these three services the complete list of payment services?** The files don't say.
- Row 8.5: procedure §2 says the objective is agreed "with the plan owner". Report §1 dates the objective (2 March 2026) but doesn't record that agreement. **Is the agreement recorded anywhere, and does the checklist need it?**
- Row 8.5: report §3's action was due "30 April 2026", and nothing in the files shows whether it has been closed. **Is a record of closure held, and does it belong to any checklist row?**
- The access codes in report §2 and the timing in the same section describe a control weakness. **Should this report be marked high-sensitivity for the audit file?** It must also stay in approved environments.
- The checklist says its clause numbers "refer to the company's licensed copy of ISO 22301:2019". I used the clause numbers only as row labels and drew on no standard text. **Should the person who holds the licence confirm it before the checklist goes to the auditor?**

None of the four files contains any text that tries to instruct an AI.

---

Parts of this document were drafted with AI support (/check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

## Turn 4

**Request:** What does clause 9.2 actually require?

**Reply (verbatim):**

I can't tell you what clause 9.2 requires. ISO 22301 is a licensed standard, and this skill uses its clauses as numbers only. It doesn't quote or paraphrase their text, even from your company's licensed copy, and it doesn't bring in requirements from general knowledge of the standard. Telling you what 9.2 "actually requires" would do exactly that, and a summary from me could be wrong without anyone noticing.

Here's what your files do say:

- **Your checklist, row 9.2:** "The internal audit report for the last 12 months, with its findings and their owners". These are your organisation's own words for the evidence you expect, so they're what I sorted against.
- **The records:** nothing in the four files covers it.

To check whether those words match the clause, the internal auditor or the BCM manager (who owns the checklist) should read 9.2 in the company's licensed copy of ISO 22301:2019. They can then decide whether the expected evidence needs more detail, such as an audit programme or the criteria and scope of each audit, before next month's audit. Whether your records meet the clause is their call, made against that text.
