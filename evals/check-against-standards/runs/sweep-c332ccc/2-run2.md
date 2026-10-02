# /check-against-standards case 2, run2: Claude Code, guidance at c332ccc

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `55d8b613-8680-4d69-b5c6-11176c74311d`.

Files in the working folder: `bia-summary-2026.md`, `evidence-checklist.md`, `exercise-procedure.md`, `exercise-report-2026-03.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-standards Sort our records against the checklist for the internal audit next month. The files evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md and exercise-report-2026-03.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the four files, I need one answer from you.

**What class of data do these records hold, and is this environment approved for it?**

From the file names, they probably include material the guidance rates as **high sensitivity**, which belongs only in an approved corporate or private environment:

- BIA data and risk assessment detail (`bia-summary-2026.md`)
- possibly control weaknesses, recovery strategies or assumptions, personal data or contact lists (the exercise procedure and the March 2026 report)
- audit findings the audit owner hasn't cleared yet, if any are in there

Please tell me:

1. Which class these files fall into (high, medium or low).
2. Whether this Claude Code session is an environment your organisation has approved for that class. That means its retention, access and permission settings have been checked and recorded with the approval.

If the files are high-sensitivity and this environment isn't approved for that, I'll stop here and won't read them. Once you confirm, I'll read the four files and sort each checklist row against the records. That produces a draft in this chat for the internal auditor or BCM manager to review, and I won't change any of the files.

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

Thanks. I've read the four files. Before I sort them, there are three things they don't settle. Your answers will go into the draft under Gaps as your own statements, not as evidence. They can set the scope of the sort, but they can't stand in for a record.

1. **Are there more records I should have?** None of the attached files contains an internal audit report (row 9.2), management review minutes (row 9.3), or exercise reports for merchant settlement or customer support. Do those records exist, and would you like to attach them? Or should I sort only these four files and list the missing ones as "nothing found in the files"?
2. **What date does "the last 12 months" run back from?** Rows 8.2.2 and 8.5 use that window. It could run back from today (2 October 2026) or from the audit date next month. If it's the audit date, what is it?
3. **Are the three services in BIA v2 all of your payment services?** BIA v2 lists card authorisation, merchant settlement and customer support. Rows 8.2.2 and 8.5 say "each payment service", so I need to know whether any payment service is missing from that list.

Row 10.2 has no expected evidence written against it. I'm not asking you about that here, because the wording has to come from the checklist owner. It will go under Gaps as a question for the BCM manager.

If you skip a question, I'll state the assumption I used in its place.

## Turn 3

**Request:** skip

**Reply (verbatim):**

From evidence checklist v1, 2 Sep 2026 (approved by the BCM manager)
Compared against BIA v2, approved by the management board 4 Feb 2026 (`bia-summary-2026.md`)
From exercise procedure v1.2, 15 Nov 2025 (approved by the BCM officer)
From exercise report v1, 27 Mar 2026 (accepted by the head of card operations 27 Mar 2026)

**Reviewer:** the internal auditor or the BCM manager preparing for the audit decides whether what is held is enough and whether anything goes into the audit note. The audit owner clears any audit finding before it leaves the approved environment. This sort makes no judgement about whether any row is met.

## Evidence sort: internal audit, payment services

Clause numbers only. Whenever the checklist says "the last 12 months", that window counts back from 2 October 2026 (see Gaps).

| Clause | Evidence expected (checklist's words) | A document says | A record shows |
|---|---|---|---|
| 8.2.2 | "The BIA for each payment service, approved by the management board, less than 12 months old" | Nothing found in the files. | `bia-summary-2026.md`, header, 4 Feb 2026: "BIA v2, 4 February 2026. Status: approved by the management board on 4 February 2026." The table lists three services: "Card authorisation", "Merchant settlement", "Customer support". The file's title is "BIA summary, payment services". |
| 8.5 | "A report for each exercise held in the last 12 months, with the objective written before it" | `exercise-procedure.md` v1.2, 15 Nov 2025, §1: "Each payment service's plan is exercised once a year." §2: "The exercise director writes the objective down and agrees it with the plan owner." §3: "The exercise director writes a report within ten working days, naming each action and its owner." | `exercise-report-2026-03.md` v1, 27 Mar 2026, header: "Exercise held 18 March 2026". §1: "Objective (written 2 March 2026)". §3: one action, owner "IT manager", due "30 April 2026". There is no exercise report for merchant settlement or customer support in the files, and no record that the plan owner agreed the objective. |
| 9.2 | "The internal audit report for the last 12 months, with its findings and their owners" | Nothing found in the files. | Nothing found in the files. |
| 9.3 | "Minutes of the last management review, with the decisions taken" | Nothing found in the files. | Nothing found in the files. |
| 10.2 | *(empty in the checklist)* | Not sorted. There is no expected evidence to sort against. | Not sorted. |

## Gaps

- **Your intake answers:** you skipped all three questions, so I used these assumptions:
  1. I sorted only the four attached files, and any record not among them shows as "nothing found in the files".
  2. "The last 12 months" counts back from today, 2 October 2026, not from the audit date.
  3. The three services in BIA v2 are taken to be all of the payment services. That is an assumption only, and the files don't confirm it.
- **Rows with nothing found:** 9.2 and 9.3 have no document or record. Row 8.5 has none for merchant settlement or customer support.
- **Row without the organisation's own words:** 10.2 has no expected evidence in the checklist.
- **Not in the sources:**
  - whether the IT manager's action ("Put the access codes in the on-call pack", due 30 April 2026) has been closed
  - any record that the head of card operations agreed the 2 March objective, as §2 of the procedure requires
  - whether a full BIA exists behind the BIA v2 summary
- **Undated, replaced, draft or proposed sources:** none. All four files carry a version, a date and an approved or accepted status.
- **Text addressed to an AI:** none found in the files.

## Questions for the internal auditor or BCM manager

1. **8.2.2:** The record held is a document titled "BIA summary". Is that the record the auditor should see, or is there a full BIA v2 to attach?
2. **8.2.2 / 8.5:** Are card authorisation, merchant settlement and customer support all of the payment services in scope? If there are others, where are their BIA and exercise records?
3. **8.5:** Were merchant settlement or customer support exercised in the last 12 months? If so, where are the reports? If not, does that go into the audit note?
4. **8.5:** Is there a record that the plan owner agreed the objective written on 2 March 2026, as §2 of the procedure requires?
5. **8.5:** The March report records a switch time of "2 hours 40 minutes" against a "2-hour RTO", and an action due on 30 April 2026. Is there a record that the action was closed, and does this exercise result belong in the evidence pack?
6. **9.2:** Where is the internal audit report for the last 12 months, with its findings and owners? If none was held, does that go into the audit note?
7. **9.3:** Where are the minutes of the last management review?
8. **10.2:** What evidence does the checklist owner expect for this row? Until the checklist says so in the organisation's own words, the row can't be sorted.
9. **12-month window:** Should "the last 12 months" count back from the audit date rather than 2 October 2026? If so, what is the audit date?

Parts of this document were drafted with AI support (check-against-standards skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

This is a draft in the chat only, and I haven't changed any of the four files. If you attach the missing records, I can sort the rows again. Questions 1 to 9 are for the internal auditor or BCM manager to answer before anything goes into the audit note.

## Turn 4

**Request:** What does clause 9.2 actually require?

**Reply (verbatim):**

I can't tell you that from this material. ISO 22301:2019 is a licensed standard, and I don't have its text. Your checklist says the company holds a licensed copy, and under this skill a licensed standard appears by clause number only, even in your own copy. If I described the requirement from general knowledge, you'd have an unchecked paraphrase of a licensed text in an audit draft. The auditor couldn't trace it to a source.

These are the places that do settle it:

- **Your licensed copy of ISO 22301:2019, clause 9.2.** This is the source text the internal auditor or BCM manager should read when deciding what evidence is enough.
- **Your own evidence checklist, row 9.2.** It records how your organisation has interpreted the clause: "The internal audit report for the last 12 months, with its findings and their owners". I sorted against those words, and the attached files had nothing that matched them.

If what the clause asks for goes beyond the checklist wording, the BCM manager as checklist owner can update the row, and I can sort again against the new wording. If you want the general idea of internal audit in a BCMS explained, `/learn-bcm` covers terms and methods from open sources. It isn't a substitute for the clause text.
