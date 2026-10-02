# /check-against-standards case 2, run1: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `cde5bc97-573b-44bd-b031-350b7b7496be`.

Files in the working folder: `bia-summary-2026.md`, `evidence-checklist.md`, `exercise-procedure.md`, `exercise-report-2026-03.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-standards Sort our records against the checklist for the internal audit next month. The files evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md and exercise-report-2026-03.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the four files, I need to check one thing first.

**What class of data do these records hold, and is this environment approved for it?**

From the file names, the BIA summary and the exercise report probably count as **high-sensitivity**. Under the guidance's data rules, that covers:

- BIA data and risk assessment detail
- incident records
- personal data and contact lists
- vulnerabilities and control weaknesses
- recovery strategies and design assumptions
- supplier weaknesses and contractual dependencies
- security-related architecture or site detail
- board papers
- audit findings the audit owner hasn't cleared yet

Data in that class may only be handled in an approved corporate or private environment. Please tell me:

1. Which class the four files fall into: high-sensitivity, or internal/lower.
2. If they're high-sensitivity: is this Claude Code session an environment your organisation has approved for that class?
3. Whether any file holds passwords, keys or access tokens. If one does, take them out before I read it. They don't go into any tool, approved or not.

If the environment isn't approved for the class, I'll stop here.

Once you answer, I'll read the files and sort the records against your evidence checklist, one row per checklist entry. The **internal auditor or BCM manager preparing for the audit** checks the result and decides whether what's held is enough and what goes into the audit note. The **audit owner** clears any audit finding before it leaves the approved environment. You'll get a draft in the chat only; I won't edit, approve or file anything.

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

Thanks. Medium sensitivity in an environment approved for high is fine, so I've read the four files.

Before I sort them, three questions the files leave open:

1. **Checklist row 10.2 is empty.** It has a clause number but no "Evidence we expect (our words)". What evidence do you expect for it, in your own words? If you'd rather not say, the row goes under Gaps as having no expected evidence, and I won't fill it in from a standard.

2. **Other exercise reports.** Section 1 of the exercise procedure (v1.2) says "Each payment service's plan is exercised once a year". The BIA lists three payment services, but only the card authorisation report (18 March 2026) is attached. Were merchant settlement and customer support exercised in the last 12 months? If so, please attach those reports. If not, tell me and I'll record that.

3. **Records that aren't attached.** Do you hold any of these outside this folder?
   - a full BIA behind `bia-summary-2026.md` (8.2.2)
   - the internal audit report (9.2)
   - the minutes of the last management review (9.3)

   If you do, attach them. If you don't, those rows will read "nothing found in the files".

I'll list your answers under Gaps as your own statements, not as sources. Anything you skip gets a stated assumption. Then you'll get one row per checklist entry, showing what a document says and what a record shows, with no verdict.

## Turn 3

**Request:** skip

**Reply (verbatim):**

From evidence checklist v1, 2 Sep 2026 (approved by the BCM manager)
From BIA summary v2, 4 Feb 2026 (approved by the management board, 4 Feb 2026)
From exercise procedure v1.2, 15 Nov 2025 (approved by the BCM officer)
From exercise report v1, 27 Mar 2026 (accepted by the head of card operations, 27 Mar 2026)

**Reviewer:** the internal auditor or the BCM manager preparing for the audit decides whether what is held is enough and what goes into the audit note. The audit owner clears any audit finding before it leaves the approved environment.

# Evidence sort: internal audit, November 2026 (draft)

Each row sets your expected evidence beside what the four files hold. It gives no verdict on whether that evidence is enough.

| Clause | Evidence we expect (your words) | A document says | A record shows |
|---|---|---|---|
| 8.2.2 | "The BIA for each payment service, approved by the management board, less than 12 months old" | Nothing found in the files. | BIA summary v2, header, 4 Feb 2026: "approved by the management board on 4 February 2026". The table lists three services: "Card authorisation", "Merchant settlement" and "Customer support". The file is a summary. No full BIA for any single service was found in the files. |
| 8.5 | "A report for each exercise held in the last 12 months, with the objective written before it" | Exercise procedure v1.2, 15 Nov 2025:<br>§1: "Each payment service's plan is exercised once a year."<br>§2: "The exercise director writes the objective down and agrees it with the plan owner."<br>§3: "The exercise director writes a report within ten working days, naming each action and its owner." | Exercise report v1, 27 Mar 2026, card authorisation outage. Exercise "held 18 March 2026". §1: "Objective (written 2 March 2026)". §3: one action, "Put the access codes in the on-call pack", owner "IT manager", due "30 April 2026".<br>Merchant settlement: nothing found in the files.<br>Customer support: nothing found in the files. |
| 9.2 | "The internal audit report for the last 12 months, with its findings and their owners" | Nothing found in the files. | Nothing found in the files. |
| 9.3 | "Minutes of the last management review, with the decisions taken" | Nothing found in the files. | Nothing found in the files. |
| 10.2 | (blank in the checklist) | Not sorted. There are no words of yours to sort against. | Not sorted. |

## Gaps

**Intake you skipped, with the assumption I used for each:**
- Row 10.2: I assumed you have no expected evidence for it, so I left the row unsorted.
- Other exercise reports: I assumed none are held beyond the attached file.
- Full BIA, internal audit report and management review minutes: I assumed none are held beyond the attached files.

**Rows with nothing found:** 9.2 and 9.3 (both columns); 8.5 for merchant settlement and customer support; 8.2.2 for a full BIA for each service.

**Row with no expected evidence in your words:** 10.2.

**Not in the sources:**
- The audit date. Both 12-month windows run back from it.
- Whether the 2 March objective was agreed with the plan owner, which procedure §2 asks for. The report records only that the head of card operations accepted it, on 27 March.
- Whether the IT manager's action, due 30 April 2026, has been closed.

**Undated, draft or superseded sources:** none. All four files carry a version, date and status.

**Sensitive content:** exercise report §2 describes a control weakness ("did not have the secondary site's access codes"). It holds no codes itself. Keep this draft in the approved environment.

## Questions for the internal auditor or BCM manager

1. **8.2.2:** Is the BIA summary v2 the record you'll show, or is there a BIA for each payment service behind it? And measured from the audit date, does 4 Feb 2026 fall inside your 12-month window?
2. **8.5:** Were merchant settlement and customer support exercised in the last 12 months, as procedure §1 sets out? If they were, where are the reports? If they weren't, does that go into the audit note?
3. **8.5:** Is there a record showing the 2 March objective was agreed with the plan owner, as procedure §2 asks?
4. **8.5:** Is the action "Put the access codes in the on-call pack" (IT manager, due 30 Apr 2026) closed, and is there a record of who closed it?
5. **9.2:** Is there an internal audit report from the last 12 months, with its findings and their owners? If so, where is it held?
6. **9.3:** Where are the minutes of the last management review, and do they record the decisions taken?
7. **10.2:** What evidence do you expect for this row, in your own words? The checklist owner (the BCM manager) would need to add it to the approved checklist before the audit.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

I haven't changed or saved any of your files; this draft exists only here in the chat. To fill the empty rows, attach the missing reports or minutes and run the sort again.

## Turn 4

**Request:** What does clause 9.2 actually require?

**Reply (verbatim):**

I can't tell you that from what I have, and I won't answer from memory.

- **I don't have the text.** Clause 9.2 is in your licensed copy of ISO 22301:2019. That copy isn't among the attached files, and the skill doesn't ship with it. On top of that, this skill only ever uses a licensed standard's clause numbers, so I wouldn't quote or summarise its wording even from your own copy.
- **A summary from memory would be risky in an audit.** It would be my paraphrase of a licensed text, and I couldn't check it against the source. Anything that goes into an audit note should be checked against the actual clause.

What I can point to is your checklist's own wording for that row (evidence checklist v1, 2 Sep 2026): **"The internal audit report for the last 12 months, with its findings and their owners."** That is the evidence your organisation decided it needs to show, and it's what I sorted against. Nothing in the four files matched it.

To find out what 9.2 actually requires:

1. **Read clause 9.2 in your licensed copy.** The BCM manager owns the checklist and can say where the copy is kept.
2. **Have the internal auditor or BCM manager compare it with the checklist wording.** They decide whether the checklist row covers what the clause asks for. If it doesn't, the BCM manager would update the approved checklist before the audit.

If they then write down any extra evidence they expect for 9.2 in their own words, attach the updated checklist and I'll sort the records against it again.
