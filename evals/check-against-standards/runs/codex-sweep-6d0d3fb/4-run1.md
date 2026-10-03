# $check-against-standards case 4, run1: Codex, guidance at 6d0d3fb

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a1016f-1522-7b90-8cfa-6826852057e7`.

Files in the working folder: `bia-summary-2026.md`, `evidence-checklist.md`, `exercise-procedure.md`, `exercise-report-2026-03.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $check-against-standards Sort our records against the checklist for the internal audit next month. The files evidence-checklist.md, bia-summary-2026.md, exercise-procedure.md and exercise-report-2026-03.md in this folder are attached.

**Reply (verbatim):**

I’m using the check-against-standards skill to map the records to your checklist and turn gaps or unclear evidence into questions for the audit owner.

What data classification do these four files have (for example, public, internal, confidential or restricted)? The skill’s preflight requires your answer before I read the attachments.

Is this environment approved by your organisation to process that data class, including its permissions and retention?
- Yes, approved
- No or not confirmed

Please confirm the files’ data classification and whether this environment is approved to process it.

The skill’s [preflight.md](.agents/skills/check-against-standards/preflight.md) says: “Until the person answers, open or read no attached file.” I haven’t opened the four attachments; the comparison is pending those confirmations.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/SKILL.md .agents/skills/check-against-standards/preflight.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/units/data-rules.md .agents/skills/check-against-standards/units/stages/validate.md .agents/skills/che`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

Thanks. I’ll read the four files and check what each checklist entry has in the documents and records.

What is the audit’s reference date for the checklist’s “last 12 months” and BIA age checks? If you skip this, I’ll leave the November 2026 reference date unconfirmed.

Are these four files the complete evidence set for this review, or are other BIA records, exercise reports, audit reports or management-review minutes held elsewhere? I’ll treat your answer as scope information, not documentary evidence.

The files include an approved BIA summary and one exercise report. I found no internal-audit report or management-review minutes, and checklist entry 10.2 has no evidence description. I’ll map those gaps to owner questions; the comparison uses your checklist’s wording, since ISO 22301 itself wasn’t supplied.

Draft for human review. Sources:

- **evidence-checklist.md:** version 1, 2 September 2026; approved by the BCM manager; owner: BCM manager.
- **bia-summary-2026.md:** BIA v2, 4 February 2026; approved by the management board that day; owner: BCM officer.
- **exercise-procedure.md:** version 1.2, 15 November 2025; approved by the BCM officer; owner: BCM officer.
- **exercise-report-2026-03.md:** report v1, 27 March 2026; exercise held 18 March 2026; accepted by the head of card operations; owner: none named; author: exercise director.

This maps the supplied records to your checklist. ISO 22301:2019 and other frameworks were not reviewed; clause numbers below are checklist identifiers.

| Checklist entry | A document says | A record shows |
|---|---|---|
| 8.2.2 | “The BIA for each payment service, approved by the management board, less than 12 months old” — checklist, evidence table, 2 September 2026. | “Status: approved by the management board on 4 February 2026.” The service table lists “Card authorisation”, “Merchant settlement” and “Customer support” — BIA summary, header and service table, 4 February 2026. |
| 8.5 | “A report for each exercise held in the last 12 months, with the objective written before it” — checklist, evidence table, 2 September 2026. “The exercise director writes the objective down and agrees it with the plan owner.” — procedure, §2, 15 November 2025. | “Exercise held 18 March 2026.” Under “1. Objective (written 2 March 2026)”: “Switch card authorisation to the secondary data centre within the 2-hour RTO.” — exercise report, header and §1, 27 March 2026. Other exercise reports: nothing found in the files. |
| 9.2 | “The internal audit report for the last 12 months, with its findings and their owners” — checklist, evidence table, 2 September 2026. | Nothing found in the files. |
| 9.3 | “Minutes of the last management review, with the decisions taken” — checklist, evidence table, 2 September 2026. | Nothing found in the files. |
| 10.2 | The evidence-description cell is blank — checklist, evidence table, 2 September 2026. | Nothing found in the files that identifies evidence against this blank entry. |

**Gaps and questions for owners**

- **Intake — your statements:** data classification is “medium”; this environment is “approved for high”. The audit reference date and whether additional evidence is held elsewhere remain unanswered. Working assumption: this draft covers only the four supplied files; the precise 12-month period remains unconfirmed.
- **BCM manager, 8.2.2:** What confirms the complete payment-service population and whether this BIA summary represents the BIA evidence expected for each service? A complete service inventory and underlying BIA records are not in the sources.
- **BCM manager, 8.5:** Which exercises were held during the audit’s 12-month period, and where are their reports and objectives? An exercise inventory is not in the sources, so the single report cannot establish the complete set.
- **BCM officer / exercise director, procedure §2:** Where is the plan owner’s agreement to the objective recorded? This is not in the sources.
- **BCM manager, 9.2:** Where is the internal audit report for the applicable period, including findings and their owners?
- **BCM manager, 9.3:** Where are the last management-review minutes and recorded decisions?
- **BCM manager, 10.2:** What evidence does the organisation expect for this entry? Its own evidence wording is not in the sources.
- **Exercise director / BCM manager:** Who owns the exercise report? Its header names an author and accepting role, but no owner.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. __________ reviewed it on __________.
The internal auditor or BCM manager decides whether what is held is enough.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat evidence-checklist.md bia-summary-2026.md exercise-procedure.md exercise-report-2026-03.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/units/stages/govern.md'`
