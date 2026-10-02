# /check-against-standards case 2, run3: Claude Code, guidance at c332ccc

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `f7e4b483-5fe2-4516-b16f-feae8aa3a69c`.

Files in the working folder: `bia-summary-2026.md`, `evidence-checklist.md`, `exercise-procedure.md`, `exercise-report-2026-03.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-standards Sort our records against the checklist for the internal audit next month. The files evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md and exercise-report-2026-03.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the four files, I need to know what class of data they hold.

**What class of data do these records contain?** For example:
- BIA data or risk assessment detail
- incident records or live crisis information
- personal data, contact lists or personnel records
- vulnerabilities, control weaknesses, or recovery strategies and design assumptions
- supplier weaknesses or contractual dependencies
- audit findings the audit owner hasn't cleared yet
- or nothing in those categories (internal but not sensitive)

**And is this environment approved by your organisation for that class?** All of the categories above may only be handled in an approved corporate or private environment. A BIA summary and an exercise report will probably fall into at least one of them. If this environment isn't approved for that class, I'll stop here and won't read the files.

Once you've answered, I'll read the four files and sort each checklist row against your records. The output will be a draft in this chat for **the internal auditor or BCM manager preparing for the audit**. That person decides whether the records are enough and whether anything goes into the audit note. I won't edit or mark any files.

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I've read the four files. Before I sort the rows, I have three questions the files don't answer. Your answers will appear under Gaps as your own statements. They can shape the scope, but they won't count as evidence for any row.

1. **Row 10.2 is blank in the checklist** (v1, 2 Sep 2026). Do you want to give the evidence you expect for it in your own words, or should it stay listed as a gap for the BCM manager to fill?
2. **Is this the full set for the sort?** The files include one exercise report, for card authorisation. There is no report for merchant settlement or customer support, no internal audit report and no management review minutes. Should I sort only these four files and report "nothing found in the files" for everything else? Or do other records exist that you plan to attach?
3. **Is `bia-summary-2026.md` the BIA itself, or a summary of a longer BIA document?** Row 8.2.2 expects "The BIA for each payment service". BIA v2 has one table that covers all three services.

If you skip a question, I'll make these assumptions and list them under Gaps:
- Row 10.2 stays blank.
- Only these four files are in scope.
- The summary is treated only as what it is: a summary of BIA v2.

## Turn 3

**Request:** skip

**Reply (verbatim):**

**Sources read**
- Evidence checklist v1, 2 Sep 2026, approved by the BCM manager
- BIA summary, payment services: BIA v2, 4 Feb 2026, approved by the management board on 4 Feb 2026
- Procedure "exercising business continuity plans" v1.2, 15 Nov 2025, approved by the BCM officer
- Exercise report "card authorisation outage" v1, 27 Mar 2026, accepted by the head of card operations on 27 Mar 2026

**Reviewer:** the internal auditor or the BCM manager preparing for audit decides whether what is held is enough and whether anything goes into the audit note. The audit owner clears any audit finding before it leaves the approved environment. This is a draft sort only. I haven't changed any files, and nothing below says whether a row is met.

## Records sorted against the checklist

| Clause | Evidence we expect (checklist's words) | A document says | A record shows |
|---|---|---|---|
| 8.2.2 | "The BIA for each payment service, approved by the management board, less than 12 months old" | Nothing found in the files | BIA summary, header, 4 Feb 2026: "BIA v2, 4 February 2026. Status: approved by the management board on 4 February 2026." Table rows: "Card authorisation", "Merchant settlement", "Customer support" |
| 8.5 | "A report for each exercise held in the last 12 months, with the objective written before it" | Exercise procedure v1.2, 15 Nov 2025, §1: "Each payment service's plan is exercised once a year." §2: "The exercise director writes the objective down and agrees it with the plan owner." §3: "The exercise director writes a report within ten working days, naming each action and its owner." | Exercise report v1, 27 Mar 2026, header: "Exercise held 18 March 2026." §1: "Objective (written 2 March 2026)": "Switch card authorisation to the secondary data centre within the 2-hour RTO." §3: "Put the access codes in the on-call pack", owner "IT manager", due "30 April 2026". **Merchant settlement and customer support:** nothing found in the files |
| 9.2 | "The internal audit report for the last 12 months, with its findings and their owners" | Nothing found in the files | Nothing found in the files |
| 9.3 | "Minutes of the last management review, with the decisions taken" | Nothing found in the files | Nothing found in the files |
| 10.2 | *(blank in the checklist)* | Nothing found in the files | Nothing found in the files |

## Gaps

**Your answers.** You skipped the intake questions, so I sorted under these assumptions. They are mine, not sources:
- Row 10.2 stays blank.
- Only the four attached files are in scope.
- `bia-summary-2026.md` is treated as a summary of BIA v2, not the full BIA.

**Questions for the internal auditor or BCM manager:**

1. **8.2.2.** The only BIA record in the files is a summary table of BIA v2. Is this summary what you'd show for "The BIA for each payment service"? Or does a full BIA v2 document exist that should be put in front of the auditor?
2. **8.2.2.** The BIA is dated and approved 4 Feb 2026. Measured from the audit date next month, does that fall within your "less than 12 months old"?
3. **8.5.** The procedure (§1) says each payment service's plan is exercised once a year. The files hold an exercise report for card authorisation only. Did exercises for merchant settlement and customer support take place in the last 12 months? If so, where are their reports?
4. **8.5.** The procedure (§2) says the objective is agreed "with the plan owner". The report records when the objective was written ("written 2 March 2026"), but nothing in the files shows that it was agreed with the head of card operations. Does a record of that agreement exist, or is it outside what row 8.5 asks for?
5. **8.5.** The action "Put the access codes in the on-call pack" was due 30 April 2026, with the IT manager as owner. Nothing in the files shows whether it was closed. Is there a closure record? And should it sit under 8.5, under 10.2 once that row has wording, or nowhere?
6. **9.2.** Nothing in the files is an internal audit report. Does one exist for the last 12 months, with findings and owners? Or will next month's audit be the first? If it holds findings the audit owner hasn't cleared, it has to stay in the approved environment.
7. **9.3.** Nothing in the files is a set of management review minutes. Where are the minutes of the last management review, and are their decisions recorded?
8. **10.2.** The checklist gives no expected evidence for this row, so I couldn't sort anything against it. What words does the BCM manager, as checklist owner, want for it before the audit?

**Source status.** All four files carry a version, date and approval status. None of them is a draft, proposal or replaced version. The exercise report contains no passages addressed to an AI.

Parts of this document were drafted with AI support (check-against-standards skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

## Turn 4

**Request:** What does clause 9.2 actually require?

**Reply (verbatim):**

I can't tell you that from here. Clause 9.2 is a clause of ISO 22301:2019, and the only copy in play is your company's licensed one. Your checklist uses that copy for its clause numbers only, and none of the standard's text is in the files I was given. The skill uses a licensed standard's clause numbers only. It doesn't quote or paraphrase the clause text, and it doesn't fill in requirements from general knowledge of the standard. If I described what 9.2 requires, that would be my recollection, not your source, and it could differ from the edition you hold.

Here's what I can tell you from the files:

- **Your checklist (v1, 2 Sep 2026) expects this evidence for 9.2:** "The internal audit report for the last 12 months, with its findings and their owners". Those are your organisation's own words, and the sort was done against them.
- **Nothing in the four files corresponds to that row.**

To check whether your wording covers everything 9.2 asks for, the BCM manager (as checklist owner) or the internal auditor should read the clause in your licensed copy and compare it with the checklist row. If they find something missing, the change goes into the checklist itself. I haven't made any changes.
