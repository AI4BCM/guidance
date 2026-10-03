# /check-against-standards case 4, run3: Claude Code, guidance at 9c837c3

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `4deda4fc-f3d9-42f8-93a1-3463ea1e4895`.

Files in the working folder: `bia-summary-2026.md`, `evidence-checklist.md`, `exercise-procedure.md`, `exercise-report-2026-03.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Sort our records against the checklist for the internal audit next month. The files evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md and exercise-report-2026-03.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the four files, I need one thing from you:

**What class of data do these records hold?** For example: public, internal, confidential, or restricted/secret (or whatever your organisation's own classification scheme calls them).

I'll take the class from your answer rather than from any marking in the files. If this environment isn't approved for that class, I'll stop there. Once you answer, I'll sort `bia-summary-2026.md`, `exercise-procedure.md` and `exercise-report-2026-03.md` against `evidence-checklist.md` as a draft here in the chat.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Bash: `ls -la; ls /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units /`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I've read the four files. The method's intake step allows up to three questions about things the material leaves open, and I have to wait for your answers before drafting.

1. **Is this the full set for the audit?** Nothing attached covers checklist rows 9.2 (internal audit report) or 9.3 (management review minutes). The only exercise report is for card authorisation. Are other records held elsewhere, such as reports for merchant settlement or customer support? Or should I treat these four files as everything there is?
2. **Clause 10.2:** the checklist (v1, 2 September 2026) leaves the evidence column empty for this row. Is there a later version, or wording the BCM manager has agreed? If not, I'll list the row under Gaps and won't fill it in myself.
3. **Payment services in scope:** BIA v2 lists three services: card authorisation, merchant settlement and customer support. Are those all the payment services the checklist's "each payment service" covers?

Your answers will go under Gaps as your own statements, not as sources. They can narrow what I look at but won't supply any evidence. If you skip a question, I'll note the assumption I made instead.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/validate.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/keep-it-running.md`
- Glob: `*`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-against-standards/4/run3/work/evidence-checklist.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-against-standards/4/run3/work/bia-summary-2026.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-against-standards/4/run3/work/exercise-procedure.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-against-standards/4/run3/work/exercise-report-2026-03.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/README.md`

## Turn 3

**Request:** 1. Every row of the checklist. skip the rest.

**Reply (verbatim):**

Before the draft, one note on the data. Your answer puts these files in the medium class. The guidance's data rules list "BIA data" and "vulnerabilities and control weaknesses" as high-sensitivity, and the exercise report contains one of those. You said this environment is approved for high, so I went ahead.

---

**Sources (as given in each file's header)**

- `evidence-checklist.md`: "Version 1, 2 September 2026". "approved by the BCM manager". Owner: BCM manager.
- `bia-summary-2026.md`: "BIA v2, 4 February 2026". "approved by the management board on 4 February 2026". Owner: BCM officer.
- `exercise-procedure.md`: "Version 1.2, 15 November 2025". "approved by the BCM officer". Owner: BCM officer.
- `exercise-report-2026-03.md`: "Report v1, 27 March 2026". "accepted by the head of card operations on 27 March 2026". Owner: none named (see Gaps).
- ISO 22301:2019: this skill doesn't ship it, and no copy is attached. You haven't confirmed a licence, so it is **not reviewed**. It is cited by clause number only, the way the checklist uses it.
- Intake: you asked me to sort "Every row of the checklist" and skipped the other questions.

**ISO 22301:2019 (clause numbers only, from the checklist)**

| Clause | Checklist expects (its words) | A document says | A record shows |
|---|---|---|---|
| 8.2.2 | "The BIA for each payment service, approved by the management board, less than 12 months old" | Nothing found in the files. | `bia-summary-2026.md`, header, 4 February 2026: "Status: approved by the management board on 4 February 2026". Table rows for "Card authorisation", "Merchant settlement", "Customer support". Nothing else found in the files: no board minute separate from this header, and no BIA beyond this summary. |
| 8.5, card authorisation | "A report for each exercise held in the last 12 months, with the objective written before it" | `exercise-procedure.md`, 15 November 2025. §1: "Each payment service's plan is exercised once a year." §2: "The exercise director writes the objective down and agrees it with the plan owner." §3: "The exercise director writes a report within ten working days, naming each action and its owner." | `exercise-report-2026-03.md`, 27 March 2026. Header: "Exercise held 18 March 2026". §1: "Objective (written 2 March 2026)". §3: action "Put the access codes in the on-call pack", owner "IT manager", due "30 April 2026". Nothing found in the files that records the objective being agreed with the plan owner, or the action being closed. |
| 8.5, merchant settlement | as above | as above | Nothing found in the files. |
| 8.5, customer support | as above | as above | Nothing found in the files. |
| 9.2 | "The internal audit report for the last 12 months, with its findings and their owners" | Nothing found in the files. | Nothing found in the files. |
| 9.3 | "Minutes of the last management review, with the decisions taken" | Nothing found in the files. | Nothing found in the files. |
| 10.2 | The checklist's evidence cell is empty. | Not sorted (see Gaps). | Not sorted (see Gaps). |

**Gaps**

- **Your statements (intake):** "Every row of the checklist". You skipped the remaining questions, so I made these assumptions:
  - Only these four files were available. The audit report, review minutes and other exercise reports may exist outside them.
  - There is no later checklist version and no agreed wording for 10.2.
  - The payment services are the three that BIA v2 names. That list is unconfirmed.
- **Rows with nothing found:** 9.2, 9.3, and 8.5 for merchant settlement and customer support. Also nothing found for a board approval record separate from the BIA header, a full BIA, agreement of the exercise objective with the plan owner, or closure of the 30 April 2026 action.
- **Rows without the organisation's own words:** 10.2. Its expected evidence is blank in checklist v1, 2 September 2026. I have not filled it from general knowledge of the standard.
- **No owner:** `exercise-report-2026-03.md` names only "Author: exercise director" and an acceptor. Owner: none named.
- **Review dates:** none of the four headers gives one.
- **Frameworks not selected:** all other frameworks shipped with this skill (DORA, NIST and the others) are not reviewed.
- **Text addressed to an AI:** none found in the files.

**Contradictions**

None found between the files.

**Questions for owners**

- **Checklist, 8.2.2 and 8.5 (owner: BCM manager):** "less than 12 months old" and "in the last 12 months". Counted back from which date: the audit date, the checklist date, or the date of sorting?
- **Checklist, 8.2.2 and 8.5 (owner: BCM manager):** "each payment service". Which services does this cover? The checklist doesn't list them.
- **Procedure §1 (owner: BCM officer):** "once a year". Calendar year or a rolling 12 months?
- **Procedure §2 (owner: BCM officer):** "agrees it with the plan owner". Where is that agreement meant to be recorded?
- **Regulation points for legal or compliance:** none marked. No regulation is named in the files.

---

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> [internal auditor or BCM manager] decides whether what is held is enough.

**Tool calls (stream-json):**

- none
