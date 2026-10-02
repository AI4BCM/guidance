# check-against-standards case2-records, final round (f05ad10), Claude Code 2.1.284, 2026-10-01

Files in the run folder: evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md, exercise-report-2026-03.md. Guidance repo at f05ad10. Command: `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`.

Turn 2 answers the data class alone; turn 3 answers the three intake questions; turn 4 is the follow-up.

## Turn 1

Session `e8dd4fb1-877f-42d5-ac98-9b779094f6d2`. Request:

```text
/check-against-standards sort our records against the checklist for the internal audit next month. Attached: evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md, exercise-report-2026-03.md
```

Final text:

`````markdown
Before I open any of the four files, I need to know what kind of data they contain. That decides whether this environment may handle them at all.

**Which sensitivity class do these records fall into, and is this environment approved for it?**

The data rules this skill follows (`units/data-rules.md`) treat these as **high sensitivity**. They may only be processed in an approved corporate or private environment:

- BIA data and risk assessment detail. The BIA summary probably counts.
- Vulnerabilities and control weaknesses, which an exercise report often records
- Recovery strategies and design assumptions
- Personal data and contact lists, such as names of exercise participants
- Audit findings the audit owner hasn't cleared yet

For the task itself, an evidence-gap scan against a checklist is rated medium to high. It has to run in an approved corporate environment.

Please confirm:
1. The highest class of data in the four files.
2. That this Claude Code session is approved for that class, covering where the data goes and how long it's kept.

If it isn't approved, I'll stop here and won't read the files. Also, passwords, keys and access tokens must not go into any tool. If the files contain any, remove them first.
`````

## Turn 2

Session `e8dd4fb1-877f-42d5-ac98-9b779094f6d2`. Request:

```text
Data class: medium, and this environment is approved for high.
```

Final text:

`````markdown
I've read all four files. Before I sort them, here is who reviews the result, followed by three questions the files leave open.

**Reviewer:** the internal auditor, or the BCM manager preparing for the audit, decides whether what's held is enough and whether anything goes into the audit note. The audit owner clears any audit finding before it leaves this environment. I'll only sort the records and won't give any verdict.

**Questions:**

1. **Is this the complete set for the audit?** None of the four files is the internal audit report (row 9.2) or the minutes of the last management review (row 9.3). Do you want to attach them, or should I sort without them? Without them, those rows will read "nothing found in the files".
2. **Row 10.2 has no expected evidence in the checklist.** If you give me the BCM manager's wording, I'll sort against it as your statement, not the approved checklist text. Otherwise the row goes under Gaps as a question for the checklist owner.
3. **Is the BIA's list of three services complete?** It names card authorisation, merchant settlement and customer support. Rows 8.2.2 and 8.5 say "each payment service" and "each exercise held", and the procedure says "each payment service's plan" is exercised once a year. Are there other payment services, or other exercises held in the last 12 months?

You can skip any of these. I'll then note an assumption under Gaps, for example that the attached files are the whole set. Your answers can shape the scope, but they won't fill in a row.
`````

## Turn 3

Session `e8dd4fb1-877f-42d5-ac98-9b779094f6d2`. Request:

```text
1. Sort without them. 2. Skip. 3. Skip; sort only these files.
```

Final text:

`````markdown
From evidence checklist v1, 2 Sep 2026 (approved by the BCM manager)
Compared against BIA summary v2, 4 Feb 2026 (approved by the management board, 4 Feb 2026)
From exercise procedure v1.2, 15 Nov 2025 (approved by the BCM officer)
From exercise report v1, 27 Mar 2026 (accepted by the head of card operations, 27 Mar 2026)

**Draft: records sorted against the checklist, row by row.** This only sorts the records and judges nothing. The internal auditor or the BCM manager decides whether what's held is enough and what goes into the audit note.

| Clause | Evidence we expect (checklist) | A document says | A record shows |
|---|---|---|---|
| 8.2.2 | "The BIA for each payment service, approved by the management board, less than 12 months old" | Nothing found in the files. | BIA summary v2, header, 4 Feb 2026: "Status: approved by the management board on 4 February 2026". The table lists "Card authorisation", "Merchant settlement" and "Customer support". |
| 8.5 | "A report for each exercise held in the last 12 months, with the objective written before it" | Exercise procedure v1.2, 15 Nov 2025:<br>• §1: "Each payment service's plan is exercised once a year."<br>• §2: "The exercise director writes the objective down and agrees it with the plan owner."<br>• §3: "The exercise director writes a report within ten working days, naming each action and its owner." | Exercise report v1, 27 Mar 2026:<br>• Header: "Exercise held 18 March 2026"<br>• §1: "Objective (written 2 March 2026)"<br>• §3: one action, owner "IT manager", due "30 April 2026"<br>Covers card authorisation only. Nothing found in the files for merchant settlement or customer support. |
| 9.2 | "The internal audit report for the last 12 months, with its findings and their owners" | Nothing found in the files. | Nothing found in the files. |
| 9.3 | "Minutes of the last management review, with the decisions taken" | Nothing found in the files. | Nothing found in the files. |
| 10.2 | *(no expected evidence in the checklist)* | Not sorted. See Gaps. | Not sorted. See Gaps. |

**Gaps**

*Your statements (not sources) and the assumptions I made:*
- You said to sort without the internal audit report and the management review minutes. Rows 9.2 and 9.3 therefore show only what these four files hold.
- You skipped the 10.2 wording, so I assumed the row has no expected evidence. I didn't infer any from general knowledge of the standard.
- You skipped the scope question, so I assumed the three services in the BIA summary and the one exercise report are the whole set. I sorted only these four files.

*Questions for the internal auditor or BCM manager:*
1. **8.2.2:** The file is titled "BIA summary". Is that the BIA the checklist means, or is a fuller BIA held elsewhere? It is dated 4 Feb 2026. Measured from the audit date, is that within "less than 12 months old"?
2. **8.5:** The files hold one exercise report, for card authorisation. Procedure §1 says "Each payment service's plan is exercised once a year." Were merchant settlement and customer support exercised in the last 12 months, and where are those reports?
3. **8.5:** Procedure §2 asks that the objective be agreed "with the plan owner". The report shows when the objective was written ("written 2 March 2026"), but nothing found in the files shows it was agreed. Is that agreement recorded somewhere, and is it evidence you expect under this row?
4. **9.2:** Nothing in the files holds an internal audit report. Where is it held, and is it ready for the audit?
5. **9.3:** Nothing in the files holds management review minutes. Where are the latest minutes, and what date are they?
6. **10.2:** The checklist gives no expected evidence for this row. What wording will the BCM manager, as checklist owner, add before the audit?
7. **Not tied to any row:** The report's only action ("Put the access codes in the on-call pack", owner "IT manager", due "30 April 2026") has no record of being closed in the files. Is a closure record held, and does it belong under any checklist row?

*Sources:* all four files have a version, date and status. None is a draft, superseded or undated. None contains text that instructs an AI.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

I only sorted the four files and changed none of them. Whether what you hold is enough is for the internal auditor or BCM manager to decide. The audit owner must clear any audit finding before it leaves this environment.
`````

## Turn 4

Session `e8dd4fb1-877f-42d5-ac98-9b779094f6d2`. Request:

```text
What does clause 9.2 actually require?
```

Final text:

`````markdown
I can't tell you that. ISO 22301 is a licensed standard, and this skill refers to its clauses by number only, even when you hold a licensed copy. It doesn't quote or paraphrase what a clause says. I also can't describe 9.2 from general knowledge, because that would mean presenting my recollection as if it were the standard's text, and the auditor would be judging against it.

Here is what's available instead:

- **The source text:** your company's licensed copy of ISO 22301:2019. The checklist header says the clause numbers refer to it. Read 9.2 there.
- **What your checklist expects under 9.2,** in your own words: "The internal audit report for the last 12 months, with its findings and their owners." That's the line the sort used, and it's the BCM manager's reading of the clause, not the clause itself.
- **Who decides whether that reading is right:** the internal auditor or the BCM manager, comparing the checklist row with the licensed text. If they find the row leaves something out, the BCM manager, as the checklist's owner, revises it.

If you'd like, once the internal audit report is available I can sort it against the 9.2 row as the checklist words it.
`````
