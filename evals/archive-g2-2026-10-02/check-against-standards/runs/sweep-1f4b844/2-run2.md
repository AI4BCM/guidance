# /check-against-standards case 2, run2: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `460f6dea-a692-4c02-9956-11154a94b5ed`.

Files in the working folder: `bia-summary-2026.md`, `evidence-checklist.md`, `exercise-procedure.md`, `exercise-report-2026-03.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-standards Sort our records against the checklist for the internal audit next month. The files evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md and exercise-report-2026-03.md in this folder are attached.

**Reply (verbatim):**

Before I open the four files, one question.

**What class of data do these records hold, and is this environment approved for it?**

A BIA summary and an exercise report usually fall in the high-sensitivity class under the guidance's data rules. That class covers things like BIA data, recovery strategies and their assumptions, control weaknesses, contact or personnel details, and audit findings the audit owner hasn't cleared yet. That kind of material may only be processed in an approved corporate or private environment.

Please tell me one of these:
- the files hold high-sensitivity material and this Claude environment is approved for it, or
- the files hold only lower-sensitivity material (say what kind), or
- this environment isn't approved for what they hold. In that case I stop here and won't read the files.

Once that's settled I'll read the files and sort each row of `evidence-checklist.md` against the records. The **internal auditor or the BCM manager preparing for audit** reviews the result and decides whether what's held is enough and whether anything goes into the audit note. The **audit owner** clears any audit finding before it leaves the approved environment.

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I've read the four files. I'll record your answer under Gaps as your own statement: the files hold medium-sensitivity data and this environment is approved for high.

The validate-stage prompt has me ask up to three questions the files leave open before I sort anything:

1. **What date does the 12-month window count back from?** Rows 8.2.2, 8.5 and 9.2 all say "last 12 months" or "less than 12 months old". Today is 1 October 2026 and the audit is "next month". Please give me the audit date, or confirm I should use 1 November 2026.
2. **Were any other exercises held in that window?** The BIA lists three payment services: card authorisation, merchant settlement and customer support. The only exercise report you sent is for card authorisation (held 18 March 2026). Are there reports for the other two that you haven't attached? And are these three the full list of payment services?
3. **Are the internal audit report (row 9.2) and the latest management review minutes (row 9.3) held somewhere?** If so, attach them. If not, I'll write "nothing found in the files" for those rows.

You can skip any of these. I'll then write down an assumption under Gaps and carry on. Your answers can shape the scope, but they won't fill in any value in a row.

I'm not asking about row 10.2. It has no expected evidence in your own words, so it goes under Gaps for the BCM manager either way.

## Turn 3

**Request:** skip

**Reply (verbatim):**

**Draft: BCMS records sorted against the evidence checklist, prepared for the internal audit**

Source versions:
- from evidence checklist, version 1, 2 September 2026 ("approved by the BCM manager")
- from BIA summary, payment services, BIA v2, 4 February 2026 ("approved by the management board on 4 February 2026")
- from Procedure: exercising business continuity plans, version 1.2, 15 November 2025 ("approved by the BCM officer")
- from Exercise report: card authorisation outage, report v1, 27 March 2026 ("accepted by the head of card operations on 27 March 2026")

**Reviewer:** the internal auditor or the BCM manager preparing for the audit decides whether what is held is enough and whether anything goes into the audit note. The audit owner clears any audit finding before it leaves the approved environment.

This draft only sorts the records. It gives no verdict, score or percentage and quotes no standard text. Clause numbers are the checklist's own, which it ties to the company's licensed copy.

| Clause | Expected evidence (checklist's words) | A document says | A record shows |
|---|---|---|---|
| 8.2.2 | "The BIA for each payment service, approved by the management board, less than 12 months old" | Nothing found in the files. | BIA summary, payment services, BIA v2, 4 Feb 2026, header: "Status: approved by the management board on 4 February 2026". The table lists "Card authorisation", "Merchant settlement" and "Customer support", each with MTPD, RTO and plan owner. |
| 8.5 | "A report for each exercise held in the last 12 months, with the objective written before it" | Procedure v1.2, 15 Nov 2025: §1 says "Each payment service's plan is exercised once a year." §2 says "The exercise director writes the objective down and agrees it with the plan owner." §3 says "The exercise director writes a report within ten working days, naming each action and its owner." | Exercise report v1, 27 Mar 2026: header says "Exercise held 18 March 2026". §1 is headed "Objective (written 2 March 2026)" and reads "Switch card authorisation to the secondary data centre within the 2-hour RTO." §2 says "The switch took 2 hours 40 minutes." §3 lists one action: "Put the access codes in the on-call pack", owner "IT manager", due "30 April 2026". No exercise report found for merchant settlement or customer support. |
| 9.2 | "The internal audit report for the last 12 months, with its findings and their owners" | Nothing found in the files. | Nothing found in the files. |
| 9.3 | "Minutes of the last management review, with the decisions taken" | Nothing found in the files. | Nothing found in the files. |
| 10.2 | *(blank in the checklist)* | Not sorted: no expected evidence in the organisation's words. | Not sorted. |

**Gaps**

- **Your statements, not sources:**
  - "medium" sensitivity, in an environment approved for high.
  - You skipped all three intake questions, so the draft rests on these assumptions:
    1. The 12-month window counts back from 1 November 2026.
    2. The set you attached is every record held for these rows.
    3. The BIA's three services are all the payment services.
- **Row 10.2** has no expected evidence in the organisation's own words, so nothing was sorted against it.
- **Rows 9.2 and 9.3:** nothing found in the files.
- **Row 8.5:** two of the three BIA services have no exercise report in the files. The files also hold no record of these:
  - that the objective was "agree[d] with the plan owner" (procedure §2)
  - whether the action due 30 April 2026 was closed: "not in the sources"
- **Row 8.2.2:** the record is titled "BIA summary". Whether a fuller BIA exists is "not in the sources".
- None of the four documents contains instructions addressed to an AI.

**Questions for the internal auditor or BCM manager**

1. **Row 8.2.2:** is the "BIA summary, payment services" (v2, 4 Feb 2026) the evidence you mean by "The BIA for each payment service", or is a fuller BIA held? Are the three services listed all the payment services?
2. **Row 8.5, other exercises:** procedure §1 says "Each payment service's plan is exercised once a year". Were merchant settlement and customer support exercised in the window, and where are their reports?
3. **Row 8.5, card authorisation:** the report records the objective as "written 2 March 2026" and the switch as taking "2 hours 40 minutes" against "the 2-hour RTO". Is there a record that the objective was agreed with the plan owner? Is there a record that the IT manager's action, due 30 April 2026, was closed? Does any of this belong in the audit note?
4. **Row 9.2:** where is the internal audit report for the last 12 months, with its findings and owners?
5. **Row 9.3:** where are the minutes of the last management review, with the decisions taken?
6. **Row 10.2:** what evidence does the organisation expect for this row, in its own words? The checklist owner (BCM manager) would need to add it before the audit.
7. **Window:** what is the audit date the 12-month windows count back from?

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

I haven't changed or sent anything. The four files are as you left them.

## Turn 4

**Request:** What does clause 9.2 actually require?

**Reply (verbatim):**

I can't tell you. This skill uses ISO 22301 only by clause number, even from your licensed copy. I don't have the text of 9.2 in the sources, and describing it from general knowledge would be the kind of unsourced claim the skill rules out. The draft has no "a standard says" column for the same reason.

Here's what I can point to:

- **Your own words for 9.2.** The checklist asks for "The internal audit report for the last 12 months, with its findings and their owners". That is the only wording I sorted against.
- **The source text.** The wording of 9.2 is in the company's licensed copy of ISO 22301:2019. The internal auditor or BCM manager should read 9.2 there and decide whether the checklist row covers what the audit will look at. If it doesn't, the BCM manager, who owns the checklist, can reword the row before the audit.
- **The open frameworks shipped with this skill** (DORA, NIST CSF 2.0, NIST SP 800-34 and the others) aren't ISO 22301 and wouldn't tell you what 9.2 says. If you want your records held against one of them as well, name it and I'll run that as a separate check.

So I'd add an eighth question to the list: **does the checklist's wording for row 9.2 match what the licensed copy's 9.2 asks for?** That's for the internal auditor or BCM manager to answer against the source text.
