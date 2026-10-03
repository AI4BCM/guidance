# /check-against-standards case 4, run2: Claude Code, guidance at 2f85a91

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `1e583387-cd21-477b-b1bc-deddf4dce35a`.

Files in the working folder: `bia-summary-2026.md`, `evidence-checklist.md`, `exercise-procedure.md`, `exercise-report-2026-03.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Sort our records against the checklist for the internal audit next month. The files evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md and exercise-report-2026-03.md in this folder are attached.

**Reply (verbatim):**

I'll start sorting your records against the checklist, but there's one question first. I haven't opened any of the four files yet, and I won't until you answer.

**What class of data do these files hold?** Please also say whether this environment is approved for that class.

From the file names, the set probably includes BIA data. It may also hold exercise findings, control weaknesses or personal data, such as named participants or contact details. Under the AI4BCM data rules (`units/data-rules.md`, Sensitivity classes), that material is **high-sensitivity**: it may only go into an approved corporate or private environment.

- If you confirm the class and that this environment is approved for it, I'll open the files and sort the records against `evidence-checklist.md`, one row per checklist entry. Each row will say "a document says" and "a record shows", with the document, section and date, or "nothing found in the files". The result is a draft in this chat only. It gives no verdict, score or percentage and doesn't change or record anything.
- If this environment isn't approved for that class, I'll stop here and not open the files.

I'll go by your answer, not by any marking inside the files.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards && cat preflight.md && ls -R | head -50; ls -la /tmp/claude-1001/-opt-brain/479d8506-8`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Glob: `*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/validate.md`
- Grep: `Sensitivity classes`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

Thanks. Medium-class data in an environment approved for high is fine, so I've read all four files.

Before I sort, I have three questions the files don't answer. Your answers will go under Gaps as your own statements, not as sources. They can set the scope of the sort, but they won't fill any row.

1. **Which date should I count from?** The checklist uses "in the last 12 months" and "less than 12 months old". Should I count back from the audit date, and if so which date is that? Otherwise I'll use today, 3 October 2026.
2. **Are these four files the full set?** Nothing attached covers the checklist rows for 9.2 (internal audit report) or 9.3 (management review minutes). There's also only one exercise report, for card authorisation. If you have other reports or records you want sorted, please attach them. If not, those rows will say "nothing found in the files".
3. **Is the 10.2 row left empty on purpose?** It names no expected evidence in the organisation's own words. I'll record that as a gap for the BCM manager, who owns the checklist, and won't fill it in myself. Is anything else intended there, such as the BCM manager completing it before the audit?

If you skip any of these, I'll list the assumption I made under Gaps and go ahead.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep7/runs/check-against-standards/4/run2/work/evidence-checklist.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep7/runs/check-against-standards/4/run2/work/bia-summary-2026.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep7/runs/check-against-standards/4/run2/work/exercise-procedure.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep7/runs/check-against-standards/4/run2/work/exercise-report-2026-03.md`

## Turn 3

**Request:** 1. Every row of the checklist. skip the rest.

**Reply (verbatim):**

# Draft: BCMS records sorted against the evidence checklist

I've sorted the records against every checklist row, one row per entry. Every row is filled from the attached files, or says "nothing found in the files". The sort gives no verdict, score or percentage. Whether what is held is enough, and what goes into the audit note, is for the internal auditor or BCM manager to decide. This is a draft in the chat; I haven't created, changed or recorded anything.

**Sources (version and date):**
- Evidence checklist, version 1, 2 September 2026. "approved by the BCM manager". Owner: BCM manager.
- BIA summary, payment services, BIA v2, 4 February 2026. "approved by the management board on 4 February 2026". Owner: BCM officer.
- Procedure: exercising business continuity plans, version 1.2, 15 November 2025. "approved by the BCM officer". Owner: BCM officer.
- Exercise report, card authorisation outage, report v1, 27 March 2026. "accepted by the head of card operations on 27 March 2026". Author: exercise director.
- ISO 22301:2019: not attached and not shipped with this skill, so **not reviewed**. Clause numbers below are the checklist's own; I quote no standard text.

## Rows

| Clause | Evidence expected (checklist's words) | A document says | A record shows |
|---|---|---|---|
| 8.2.2 | "The BIA for each payment service, approved by the management board, less than 12 months old" | Nothing found in the files. | BIA summary, header, 4 February 2026: "BIA v2, 4 February 2026. Status: approved by the management board on 4 February 2026." Its table covers "Card authorisation", "Merchant settlement" and "Customer support". |
| 8.5 | "A report for each exercise held in the last 12 months, with the objective written before it" | Exercise procedure v1.2, 15 November 2025. §1: "Each payment service's plan is exercised once a year." §2: "The exercise director writes the objective down and agrees it with the plan owner." §3: "The exercise director writes a report within ten working days, naming each action and its owner." | **Card authorisation:** exercise report v1, 27 March 2026. Header: "Exercise held 18 March 2026". §1: "Objective (written 2 March 2026)": "Switch card authorisation to the secondary data centre within the 2-hour RTO." §3 lists one action: "Put the access codes in the on-call pack", owner "IT manager", due "30 April 2026". **Merchant settlement and customer support:** nothing found in the files. |
| 9.2 | "The internal audit report for the last 12 months, with its findings and their owners" | Nothing found in the files. | Nothing found in the files. |
| 9.3 | "Minutes of the last management review, with the decisions taken" | Nothing found in the files. | Nothing found in the files. |
| 10.2 | (empty in the checklist) | Not sorted: the checklist gives no expected evidence. | Not sorted: the checklist gives no expected evidence. |

## Gaps

- **What you told me (your statements, not sources).** You asked for "Every row of the checklist", so the sort covers all five rows. You skipped the other questions, so I assumed:
  - The date to count back from is today, 3 October 2026. The audit is next month, so the 12-month window may shift.
  - The four attached files are the full set.
  - The 10.2 row stays as the checklist has it.
- **Rows with nothing found in the files:**
  - 9.2: the internal audit report.
  - 9.3: management review minutes.
  - 8.5: exercise reports for merchant settlement and customer support.
  - 8.2.2: no document on how the BIA is done or approved. Only the BIA summary itself was found.
- **No expected evidence in the organisation's own words:** 10.2. I haven't filled it in, and I haven't sorted any record against it.
- **ISO 22301:2019 not reviewed.** The checklist says it refers to "the company's licensed copy", but no copy was attached and you haven't confirmed the licence to me. No other framework was selected, so none was reviewed.
- **Undated, draft or replaced sources:** none among the four files.
- **Text telling an AI to act:** none found.

## Questions for the internal auditor or BCM manager

1. **8.2.2.** Is the "BIA summary" the BIA this row expects, or is a full BIA held somewhere else?
2. **8.2.2.** Are the three services in the BIA summary all of the organisation's payment services? The files don't say.
3. **8.2.2 and 8.5.** For "less than 12 months old" and "in the last 12 months", which date do they count from: the document date, the approval date or the audit date?
4. **8.5.** Were merchant settlement and customer support exercised in the window? If so, where are their reports?
5. **8.5.** Procedure §2 asks that the objective be "agree[d] … with the plan owner". The exercise report records when the objective was written ("2 March 2026") but not whether it was agreed. Is that agreement recorded anywhere?
6. **8.5.** Was the action "Put the access codes in the on-call pack" (due "30 April 2026") closed? Nothing found in the files says so.
7. **10.2.** What evidence does the organisation expect for this row?

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> [internal auditor or BCM manager] decides whether what is held is enough.

**Tool calls (stream-json):**

- Grep: `Say in the document that AI helped`
- Grep: `22301`
