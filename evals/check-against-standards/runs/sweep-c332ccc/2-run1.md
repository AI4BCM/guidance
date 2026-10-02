# /check-against-standards case 2, run1: Claude Code, guidance at c332ccc

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `5acff0d0-8738-4b8e-8655-be8b8497df0a`.

Files in the working folder: `bia-summary-2026.md`, `evidence-checklist.md`, `exercise-procedure.md`, `exercise-report-2026-03.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-standards Sort our records against the checklist for the internal audit next month. The files evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md and exercise-report-2026-03.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the four files, I need one answer from you.

**What class of data do these files hold, and is this environment approved for it?**

From their names, the files probably include material the guidance classes as high-sensitivity. That class may only be handled in an approved corporate or private environment. It includes:

- BIA data and risk assessment detail (likely in `bia-summary-2026.md`)
- vulnerabilities, control weaknesses and recovery assumptions (an exercise report often records these)
- personal data or contact lists, such as participants and call trees
- audit findings the audit owner hasn't cleared yet

Please tell me:
1. Which of these classes, if any, the four files contain.
2. Whether this Claude Code session runs in an environment your organisation has approved for that class.

If any file contains passwords, keys or access tokens, remove them first. Those go into no tool, approved or not.

**What happens next:** once you confirm, I'll read the four files. I'll sort each row of `evidence-checklist.md` against the records, quoting your organisation's own words where the evidence exists. Anything missing, out of date or contradictory goes under Gaps as a question.

**Who reviews the result:** the internal auditor, or the BCM manager preparing for the audit, decides whether the evidence held is enough and what goes into the audit note. The audit owner clears any audit finding before it leaves the approved environment. I'll give you a draft in this chat only. I won't edit, mark or send anything, and I won't say whether you're ready for the audit.

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I've read the four files. Before I sort the checklist, I have three questions the files leave open:

1. **Row 10.2 is empty in the checklist.** What evidence do you expect there, in your organisation's own words? If you'd rather leave it open, I'll sort it as a row with no expected evidence stated and list it under Gaps.
2. **Should only these four files count?** Rows 9.2 (internal audit report) and 9.3 (management review minutes) have no matching file. The exercise procedure plans one exercise a year for each payment service, but I have only the March 2026 card authorisation report. If more records exist, such as exercise reports for merchant settlement or customer support, or an update on the April access-codes action, please attach them. Otherwise I'll treat the four files as everything there is.
3. **Can you confirm your organisation holds a licence for ISO 22301:2019?** The checklist says it refers to your licensed copy. I'll use only its clause numbers and quote none of its text.

Whatever you answer will go under Gaps as your own statements, not as sources. It can change what I look at, but it won't fill in any evidence.

## Turn 3

**Request:** skip

**Reply (verbatim):**

**Draft: evidence sort for the internal audit (November 2026)**

Sources read:
- Evidence checklist v1, 2 September 2026, approved by the BCM manager
- BIA summary v2, 4 February 2026, approved by the management board on 4 February 2026
- Exercise procedure v1.2, 15 November 2025, approved by the BCM officer
- Exercise report v1, 27 March 2026 (exercise held 18 March 2026), accepted by the head of card operations on 27 March 2026

**Reviewer:** the internal auditor or the BCM manager preparing for audit decides whether what is held is enough and whether anything goes into the audit note. The audit owner clears any audit finding before it leaves the approved environment. This draft sorts the records only. It gives no verdict on any row.

| Clause | Evidence we expect (your words) | A document says | A record shows |
|---|---|---|---|
| 8.2.2 | "The BIA for each payment service, approved by the management board, less than 12 months old" | BIA summary v2, header, 4 Feb 2026: "BIA v2, 4 February 2026. Status: approved by the management board on 4 February 2026." The table lists "Card authorisation", "Merchant settlement" and "Customer support". | Nothing found in the files apart from the status line in the summary. There are no board minutes or other approval record, and no full BIA for any single service. |
| 8.5 | "A report for each exercise held in the last 12 months, with the objective written before it" | Exercise procedure v1.2: §1 says "Each payment service's plan is exercised once a year." §2 says "The exercise director writes the objective down and agrees it with the plan owner." §3 says "The exercise director writes a report within ten working days, naming each action and its owner." | Exercise report v1, 27 Mar 2026, card authorisation only. Header: "Exercise held 18 March 2026." §1: "Objective (written 2 March 2026)", "Switch card authorisation to the secondary data centre within the 2-hour RTO." §2: "The switch took 2 hours 40 minutes." §3: one action, "Put the access codes in the on-call pack", owner "IT manager", due "30 April 2026". For merchant settlement and customer support, nothing found in the files. |
| 9.2 | "The internal audit report for the last 12 months, with its findings and their owners" | Nothing found in the files | Nothing found in the files |
| 9.3 | "Minutes of the last management review, with the decisions taken" | Nothing found in the files | Nothing found in the files |
| 10.2 | *(no expected evidence stated)* | Not sorted: there's no expected evidence in your words | Not sorted |

**Gaps** (each one is a question for the internal auditor or the BCM manager)

*Your answers to the intake questions:* you skipped all three. I made these assumptions:
- Row 10.2 stays without expected evidence.
- The four attached files are all the records there are.
- The ISO 22301:2019 licence was not confirmed by you. The clause numbers appear only as the checklist's own row labels, and I quoted no standard text.

1. **10.2: no expected evidence.** The checklist row is blank, so nothing could be sorted against it. What evidence do you expect for 10.2, in your own words, before the audit?
2. **9.2: nothing found.** No internal audit report is in the files. Is there one for the last 12 months, and where is it held?
3. **9.3: nothing found.** No management review minutes are in the files. Is there a record of the last management review and its decisions, and where is it held?
4. **8.2.2: approval record and scope.** The board approval appears only as a status line inside the BIA summary itself. Is a separate approval record, such as board minutes of 4 February 2026, held for the audit? Is the one-page summary the BIA you expect to show, or is there a full BIA for each payment service? Are the three listed services all of your payment services?
5. **8.2.2: age against the audit date.** The BIA is dated 4 February 2026 and the audit is in November 2026. Which date does your checklist measure "less than 12 months old" from: the approval date or the audit date?
6. **8.5: exercises for two services.** The procedure (§1) has each payment service's plan exercised once a year. The files hold an exercise report for card authorisation only. Were merchant settlement and customer support exercised in the last 12 months, and are their reports held?
7. **8.5: objective agreed with the plan owner.** The report shows the objective was written on 2 March 2026, before the 18 March exercise. The procedure (§2) also has the objective "agree[d] with the plan owner". Nothing in the files records that agreement. Is it recorded anywhere?
8. **8.5: open action.** The action "Put the access codes in the on-call pack" (IT manager, due 30 April 2026) has no closure record in the files. Is there a record that the action was closed, and by whom? This row records a control weakness, so it stays in the approved environment. Whether it enters the audit note is your decision, and the audit owner clears it first.
9. **8.5: result against the objective.** The report records "The switch took 2 hours 40 minutes" against an objective of "within the 2-hour RTO" (which matches the BIA summary's RTO for card authorisation). Is this result followed up anywhere beyond the single action?

*Sources:* none of the four files is undated, draft, replaced or proposed. None contained any instruction addressed to an AI.

Parts of this document were drafted with AI support (check-against-standards skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

This is a draft in the chat only. I haven't edited, marked or sent any file.

## Turn 4

**Request:** What does clause 9.2 actually require?

**Reply (verbatim):**

I can't answer that from here. The requirement is in your organisation's licensed copy of ISO 22301:2019, and I don't have it. You also haven't confirmed the licence. Even with your copy, this skill uses a standard's clause numbers only, never its text. A summary from my general knowledge of the standard would be unchecked and could be wrong in exactly the detail an auditor tests.

What I sorted against was your own wording for 9.2 in the evidence checklist v1 (2 September 2026): "The internal audit report for the last 12 months, with its findings and their owners." The four files had nothing matching it.

To find out what the clause asks for:
- **Read clause 9.2 in your licensed copy.** The BCM manager owns the checklist and can say where the copy is kept.
- **Ask the internal auditor** whether your checklist wording covers everything they'll look for under that clause. If it doesn't, the BCM manager can update the checklist row before the audit. That's their decision, not mine.
