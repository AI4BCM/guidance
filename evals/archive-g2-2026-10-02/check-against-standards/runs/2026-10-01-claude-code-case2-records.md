# check-against-standards case2-records, Claude Code 2.1.284, 2026-10-01

Files in the run folder: evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md, exercise-report-2026-03.md. Command: `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed, later turns with `--resume`.

Turn 3 answers the intake the skill asked; turn 4 is the follow-up.

## Turn 1

Session `c1953288-d4c6-4e07-b6d3-a59794f5039e`. Request:

```text
/check-against-standards sort our records against the checklist for the internal audit next month. Attached: evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md, exercise-report-2026-03.md
```

Final text:

````markdown
Before I open any of the four attachments, I need one answer from you. The skill requires it before anything else.

**1. What class of data do these files hold, and is this environment approved for it?**

A BIA summary counts as high-sensitivity data. So does an exercise report if it records control weaknesses, recovery assumptions or audit findings the audit owner hasn't cleared yet. High-sensitivity material may only be handled in an approved corporate or private environment. An evidence-gap scan against a checklist is medium to high sensitivity and also has to run in the approved corporate environment.

Please confirm:
- the class of each file (for example, "the BIA summary is high, the procedure is medium"), and
- that this Claude Code session is approved for that class.

If it isn't approved for the highest class among the files, I'll stop here and not read them. You'd then run this in your approved environment instead.

**2. Who reviews the output.** The internal auditor or the BCM manager preparing for the audit reviews it. They decide whether what you hold is enough for each checklist row and whether anything goes into the audit note. The audit owner clears any audit finding before it leaves the approved environment.

**What you'll get once you confirm:**
- A draft in this chat only. I won't edit, mark up or file any of your records.
- One row per checklist entry, citing the record that matches it, or a gap. Each gap is written as a question for the reviewer.
- At the top, one line per document giving its version and date. Any document without a version or date goes under Gaps.
````

## Turn 2

Session `c1953288-d4c6-4e07-b6d3-a59794f5039e`. Request:

```text
Data class: medium, and this environment is approved for high.
```

Final text:

````markdown
Thanks. I've read the four files. The prompt allows me at most three questions about things the files leave open, so I'll ask them before building the sort:

1. **Checklist row 10.2 is blank. What evidence do you expect there, in your own words?** If you'd rather not fill it in, the row goes under Gaps as "no expected evidence stated in the checklist", and I won't supply words of my own for it.

2. **What date should "the last 12 months" count back from?** Rows 8.2.2, 8.5 and 9.2 all use that window. I could use today (1 October 2026) or the audit date next month. If you have the audit date, please tell me. If you skip this, I'll use today's date and record that as an assumption.

3. **Do you hold records that weren't attached?** The procedure says each payment service's plan is exercised once a year. The only exercise report attached is for card authorisation. There's also no internal audit report and no management review minutes. Do you want to attach any of these, or should I sort only what's here? If I sort only these files, those rows will come back as "nothing found in the files", and the reviewer will decide what that means.

Once you've answered, I'll return the draft: version stamps first, then one row per checklist entry, then Gaps, with each gap written as a question for the internal auditor or BCM manager.
````

## Turn 3

Session `c1953288-d4c6-4e07-b6d3-a59794f5039e`. Request:

```text
1. Skip. 2. Skip. 3. Sort only these files.
```

Final text:

````markdown
I've sorted your four files against the checklist, one row per entry. Three rows have nothing in these files, and row 10.2 can't be sorted because the checklist doesn't say what evidence it expects. This is a draft for the internal auditor or BCM manager. They decide whether what you hold is enough and whether anything goes into the audit note. Nothing has been edited, filed or sent.

**Documents read**
- Evidence checklist v1, 2 September 2026. Its status line: "approved by the BCM manager".
- BIA summary, payment services, BIA v2, 4 February 2026.
- Procedure: exercising business continuity plans, version 1.2, 15 November 2025.
- Exercise report: card authorisation outage, report v1, 27 March 2026.

**Your intake answers:** you skipped question 1 (row 10.2 wording) and question 2 (the 12-month window), and asked me to sort only these files. **My assumption:** "the last 12 months" runs from 1 October 2025 to 1 October 2026.

## Row by row

| Clause | Evidence we expect (checklist v1) | A document says | A record shows |
|---|---|---|---|
| 8.2.2 | "The BIA for each payment service, approved by the management board, less than 12 months old" | BIA summary v2, header, 4 Feb 2026: "Status: approved by the management board on 4 February 2026." The table lists three services: card authorisation, merchant settlement, customer support. | Nothing found in the files. There is no board minute or other record of that approval apart from the BIA's own status line. |
| 8.5 | "A report for each exercise held in the last 12 months, with the objective written before it" | Procedure v1.2, §1, 15 Nov 2025: "Each payment service's plan is exercised once a year." §2: "The exercise director writes the objective down and agrees it with the plan owner." | Exercise report v1, 27 Mar 2026: exercise held 18 March 2026. §1 is headed "Objective (written 2 March 2026)" and reads "Switch card authorisation to the secondary data centre within the 2-hour RTO." This covers card authorisation only. For merchant settlement and customer support: nothing found in the files. |
| 9.2 | "The internal audit report for the last 12 months, with its findings and their owners" | Nothing found in the files. | Nothing found in the files. |
| 9.3 | "Minutes of the last management review, with the decisions taken" | Nothing found in the files. | Nothing found in the files. |
| 10.2 | *(blank in the checklist)* | Not sorted: the checklist gives no expected evidence. | Not sorted. |

## Gaps: questions for the internal auditor or BCM manager

1. **8.2.2:** The only evidence of board approval is the BIA summary's own status line. Is that enough for you, or do you need the board record (minutes or a resolution) dated 4 February 2026?
2. **8.2.2:** The attached file is a *summary* of BIA v2. Is the summary what you'll put in front of the auditor, or should the full BIA v2 be sorted against this row?
3. **8.2.2:** The BIA lists three services. Are these all of the organisation's payment services? The files don't say.
4. **8.5:** The procedure (§1) expects every payment service's plan to be exercised yearly, but only the card authorisation report is attached. Were merchant settlement and customer support exercised between 1 October 2025 and 1 October 2026? If they were, where are those reports?
5. **8.5:** Procedure §2 also requires the objective to be "agreed with the plan owner". The report dates the objective (2 March 2026) but doesn't record that agreement. Do you want a record of it?
6. **9.2:** Nothing found in the files. Does an internal audit report for the period exist, and should it be added to this sort?
7. **9.3:** Nothing found in the files. Where are the minutes of the last management review?
8. **10.2:** The checklist row has no expected evidence written in your own words. Will the checklist owner (BCM manager) fill it in before the audit? Until then, this row can't be sorted. Note that the exercise report's action table (§3) is the only action record in the files.
9. **Exercise report §3:** The action "Put the access codes in the on-call pack" belongs to the IT manager and was due 30 April 2026. The files don't say whether it was closed. Do you want proof of closure for the audit?
10. **Data class:** You classed these files as medium. Exercise report §2 records a control weakness: "The on-call engineer did not have the secondary site's access codes." The data rules list control weaknesses as high sensitivity. Should the report's owner and information security reclassify it? This environment is approved for high, so the sort itself is unaffected.
11. **12-month window:** You skipped question 2, so I used 1 October 2025 to 1 October 2026. If the audit date moves the window, rows 8.2.2, 8.5 and 9.2 should be checked again against the new dates.

Parts of this document were drafted with AI support (check-against-standards skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
````

## Turn 4

Session `c1953288-d4c6-4e07-b6d3-a59794f5039e`. Request:

```text
What does clause 9.2 actually require?
```

Final text:

````markdown
I can't tell you what clause 9.2 requires, for two reasons:

- **The text isn't in what I can read.** ISO 22301:2019 is a licensed standard. Your checklist says its clause numbers refer to "the company's licensed copy". That copy wasn't attached, and the skill doesn't ship with ISO text, only the open frameworks it lists.
- **The skill cites licensed clauses by number only.** Even with your copy attached, I would cite 9.2 by its number and not quote or paraphrase it. Describing it from general knowledge would also go against the sort's rule to use only your files as evidence. What the clause requires has to be read from your licensed copy.

**What the files do say about 9.2** is your own expected evidence in checklist v1: "The internal audit report for the last 12 months, with its findings and their owners". That is what I sorted against, and nothing in the attached files matched it.

**To check that row against the clause**, the BCM manager who owns the checklist, or the internal auditor, can read clause 9.2 in your licensed copy. They'd confirm whether "the internal audit report … with its findings and their owners" captures what you'll be audited on. If they find the wording needs changing, the checklist owner updates the checklist, and I can sort that row again against the new wording.
````
