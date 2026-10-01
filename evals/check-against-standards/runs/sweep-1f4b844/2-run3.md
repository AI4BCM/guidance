# /check-against-standards case 2, run3: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `731b7e71-9080-4b02-8e28-3c45212b5609`.

Files in the working folder: `bia-summary-2026.md`, `evidence-checklist.md`, `exercise-procedure.md`, `exercise-report-2026-03.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-standards Sort our records against the checklist for the internal audit next month. The files evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md and exercise-report-2026-03.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the four files, I need to know one thing.

**What class of data do these records hold, and is this environment approved for that class?**

A BIA summary and an exercise report usually count as **high sensitivity** under the guidance's data rules. That covers BIA data and risk assessment detail, recovery strategies and design assumptions, control weaknesses, supplier dependencies, personal data such as names and contact details, and audit findings the audit owner hasn't cleared yet. High-sensitivity data may only be processed in an approved corporate or private environment. The guidance puts this task (an evidence-gap scan against a checklist) at medium to high sensitivity, in an approved corporate environment.

Please confirm:

1. The sensitivity class of `bia-summary-2026.md`, `exercise-report-2026-03.md`, `exercise-procedure.md` and `evidence-checklist.md` (low, medium or high).
2. That this Claude Code session is approved for that class under your organisation's rules.

If it isn't approved for what the files contain, I'll stop here and not read them. If it is, I'll read the four files and sort each checklist row against the records. The result will be a draft in this chat, and I won't change any of the files. The internal auditor or the BCM manager preparing for the audit will decide whether the evidence is enough.

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I've read the four files and the intake step for this task. Three things are still open, and I need your answers before I sort the rows:

1. **Checklist row 10.2 has no expected evidence.** In your organisation's words, what evidence do you expect for 10.2? If you'd rather leave it blank, I'll list the row under Gaps as "no expected evidence stated" and won't sort anything against it.
2. **The date the "12 months" counts back from.** Three rows say "less than 12 months old" or "in the last 12 months". Should those count back from the audit date (which date next month?), from today (1 October 2026), or from another date? If you don't say, I'll use the audit date and note that as an assumption under Gaps.
3. **Records for 9.2 and 9.3.** No internal audit report and no management review minutes were attached. Do they exist and will you attach them, or should I sort those rows on the four files alone? Either way I'll only use what's attached; anything else gets "nothing found in the files".

I'll list your answers under Gaps as your own statements, not as sources.

## Turn 3

**Request:** skip

**Reply (verbatim):**

Sources read, all from the files you attached:

- **Evidence checklist** v1, 2 September 2026, "approved by the BCM manager"
- **BIA summary, payment services** v2, 4 February 2026, "approved by the management board on 4 February 2026"
- **Procedure: exercising business continuity plans** v1.2, 15 November 2025, "approved by the BCM officer"
- **Exercise report: card authorisation outage** v1, 27 March 2026, "accepted by the head of card operations on 27 March 2026"

**Reviewer:** the internal auditor or the BCM manager preparing for the audit decides whether what's held is enough and whether anything goes into the audit note. The audit owner clears any audit finding before it leaves the approved environment. This is a draft for that person. I changed no files.

## Records sorted against the checklist

| Clause | Evidence we expect (your words) | A document says | A record shows |
|---|---|---|---|
| 8.2.2 | "The BIA for each payment service, approved by the management board, less than 12 months old" | Nothing found in the files. | BIA summary v2, header, 4 Feb 2026: "approved by the management board on 4 February 2026". Table, same date, lists three services: "Card authorisation", "Merchant settlement", "Customer support". |
| 8.5 | "A report for each exercise held in the last 12 months, with the objective written before it" | Exercise procedure v1.2, §1, 15 Nov 2025: "Each payment service's plan is exercised once a year." §2: "The exercise director writes the objective down and agrees it with the plan owner." §3: "a report within ten working days, naming each action and its owner." | Exercise report v1, 27 Mar 2026: "Exercise held 18 March 2026". §1: "Objective (written 2 March 2026)". §3: one action, "Put the access codes in the on-call pack", owner "IT manager", due "30 April 2026". No exercise report for merchant settlement or customer support in the files. |
| 9.2 | "The internal audit report for the last 12 months, with its findings and their owners" | Nothing found in the files. | Nothing found in the files. |
| 9.3 | "Minutes of the last management review, with the decisions taken" | Nothing found in the files. | Nothing found in the files. |
| 10.2 | No expected evidence stated (row is blank) | Not sorted | Not sorted |

## Gaps

- **Your intake answers:** you skipped all three questions, so I assumed the following:
  - Row 10.2 stays blank and unsorted.
  - "12 months" counts back from the audit date next month. The exact date isn't in the sources.
  - Rows 9.2 and 9.3 were sorted on the four attached files only.
- **Row 10.2 has no expected evidence in your own words.**
- **Rows 9.2 and 9.3:** nothing was found in the files.
- **Owners differ between documents.** The checklist's owner is "BCM manager". The BIA and the exercise procedure name "BCM officer". The sources don't say whether these are the same role.
- **Things the sources don't cover:**
  - Whether the three services in the BIA are all of your payment services.
  - Whether exercises other than the 18 March 2026 one were held.
  - Whether the 30 April 2026 action was closed.
  - Whether the plan owner agreed the objective, which procedure §2 asks for. The report records only when the objective was written.

## Questions for the internal auditor or BCM manager

1. **Row 10.2:** what evidence do you expect, in your own words? Until that's written, there's nothing to sort this row against.
2. **Row 8.2.2:** are "Card authorisation", "Merchant settlement" and "Customer support" all of your payment services? Does a BIA approved on 4 February 2026 cover what you expect, counting back from the audit date?
3. **Row 8.5:** the procedure says "each payment service's plan is exercised once a year", but the files hold one exercise report, for card authorisation. Were merchant settlement and customer support exercised? If so, where are their reports? If not, does anything about that go into the audit note?
4. **Row 8.5:** is there a record that the action "Put the access codes in the on-call pack" (IT manager, due 30 April 2026) was closed? Is there a record that the head of card operations, as plan owner, agreed the objective written on 2 March 2026?
5. **Rows 9.2 and 9.3:** do the internal audit report and the minutes of the last management review exist, and where are they held? Without them these rows show "nothing found in the files".
6. **Ownership:** are "BCM manager" (owner of the checklist) and "BCM officer" (owner of the BIA and the exercise procedure) the same role? If not, who answers for each record at the audit?

Parts of this document were drafted with AI support (check-against-standards skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

## Turn 4

**Request:** What does clause 9.2 actually require?

**Reply (verbatim):**

I can't tell you what clause 9.2 requires. This skill refers to a licensed standard by its clause number only, even when the organisation holds a licence. ISO 22301:2019 isn't among the sources that ship with the skill, and your licensed copy wasn't attached. Anything I said about 9.2's content would come from general knowledge of the standard, not from a source you can check, and the skill rules that out.

Here's what the sources do give:

- **Your checklist's own words for 9.2:** "The internal audit report for the last 12 months, with its findings and their owners". That's what the row was sorted against. The attached files held nothing for it.
- **The requirement itself:** read it in your organisation's licensed copy of ISO 22301:2019 (the checklist header points there). The internal auditor or BCM manager decides whether your checklist wording reflects it.

If it helps, I can check the openly licensed frameworks that ship with the skill (for example NIST CSF 2.0 or the UK Cabinet Office organisational resilience guidance) for passages on internal audit or independent review of continuity arrangements. Those are different texts from ISO 22301. I'd cite them on their own terms, not as a reading of 9.2.
