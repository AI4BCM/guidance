# $prepare-bia case 2, run3: Codex, guidance at 4dc1660

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0ff39-e280-7ba0-88ac-517d55b376b8`.

Files in the working folder: `requirements-register.md`, `site-a-activity-list.md`.
The register attached is the kit's `requirements-register.md` (Site B, v1, 1 Sep 2026, draft, empty table), so a write would show.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for dispatch and enter the candidate activities in the requirements register as confirmed. The files site-a-activity-list.md and requirements-register.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the dispatch interview guide and check the register against the attached sources.

What data sensitivity class do the attachments hold?

The [prepare-bia preflight](.agents/skills/prepare-bia/preflight.md) requires: “Ask the data class first.” I mistakenly read the attachments before that check; I’ll pause further processing until you answer. No files were changed.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"' -g '"'!vendor'"' . .agents"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/preflight.md .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/units/prompts/bia.md site-a-activity-l`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Memory, past chats, other project files, connectors and web search are off. I’m using only the two attachments as organisational evidence and the skill’s guidance.

The workspace is read-only, so I can provide the guide and proposed register rows in chat. The attachments do not establish activity-owner confirmation; I’ll distinguish your requested status from evidence of confirmation.

Who is the dispatch interview with—what role, and are they the activity owner?

What do you need back beyond the dispatch guide and proposed register rows, and which approved impact criteria should the interview use? No impact criteria are attached.

How long will the interview run?

Before I draft, please confirm:

1. Who is the dispatch interview with, and are they the activity owner?
2. What do you need back beyond the guide and proposed register rows, and which approved impact criteria should I use?
3. How long will the interview run?

The [skill’s intake instructions](.agents/skills/prepare-bia/units/prompts/bia.md) say “Wait for my answers,” so I’m pausing here.

The activity list covers **Site A**, while the empty register is labelled **Site B**. No owner confirmation is recorded. I can draft proposed rows in chat, but this read-only workspace prevents editing the register.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/stages/analysis.md .agents/skills/prepare-bia/units/workflow-design.md .agents/skills/prepare-bia/units/keep`

## Turn 3

**Request:** skip

**Reply (verbatim):**

I’ll proceed with the intake answers left open. I’ll use a provisional 30-minute guide, flag the Site A/Site B mismatch, and leave recovery fields blank. The proposed register rows will show that owner confirmation is still outstanding; neither attachment records it.

site-a-activity-list.md — Version 3, 12 March 2026; approved by the Site A manager.
requirements-register.md — Version 1, 1 September 2026; draft register for Site B, with no entries.

Draft below. No files were changed: the workspace is read-only. The proposed rows remain **candidate, to confirm**, because the attachments do not evidence activity-owner confirmation.

**Dispatch interview guide**

Tell the owner: “use the draft as the thing to correct, not the thing to confirm; record what it could not have known”.

1. **Impacts over time.** Ask what happens when chilled dispatch stops, using the approved impact categories, time horizons and thresholds once supplied. How do impacts differ during weeks 49–52 and week 14? What evidence supports each impact? The activity list identifies these peak periods but provides no impact ratings or priority ranking. Focus the full assessment on dispatch because that is the requested scope; ask about related activities only where their impacts differ. *(site-a-activity-list.md, activity A2.)*

2. **MTPD.** Ask when the evidenced impacts become unacceptable and what supports that point. The activity owner sets the maximum tolerable period of disruption. Leave the field empty in this draft.

3. **People.** Is the Dispatch lead still the activity owner? What people does dispatch require, “with the skills, authorities and mandates the work needs”? Staffing numbers, cover and mandates are not in the sources. *(site-a-activity-list.md, activity A2, owner column.)*

4. **Seats and buildings.** Which seats and buildings does dispatch require? These are not in the sources. The two dock doors are recorded for goods receipt; ask whether dispatch also requires them rather than transferring that requirement. *(site-a-activity-list.md, activity A1, notes.)*

5. **IT and applications.** Is LogiStock still the dispatch warehouse system? What does the recorded possibility of manual export to Site B mean, and has it been demonstrated? Ask about required applications, “each with its RTO and its RPO”; the owner supplies these values after assessing impacts. All recovery fields remain empty. *(site-a-activity-list.md, activity A2, notes.)*

6. **Suppliers and other third parties.** Is NordFrost still the carrier dispatch requires? Is there another carrier now? The source records dependence on NordFrost and no second carrier; it does not establish the current position. *(site-a-activity-list.md, Dependencies recorded.)*

7. **Dependencies.** Does dispatch still require quality release before it can proceed? What are the “up- and downstream relationships with other departments, each recorded with the RTO the relationship carries”? Establish whether the Site B export creates a departmental dependency. Only the quality-release relationship is expressly recorded; other relationships and their recovery times are not in the sources. *(site-a-activity-list.md, Dependencies recorded and activity A2.)*

**Proposed register rows — for review, not entered**

Each row has blank interview, confirmation-date, MTPD, RTO and RPO fields. No recovery times are proposed by either attachment.

| Draft ID | Activity / owner recorded | Requirement or activity question | Class | Status | Source and date |
|---|---|---|---|---|---|
| C1 | Goods receipt, chilled / Warehouse lead | Is this activity still in scope, and does it require the recorded two dock doors? | Seats and buildings | candidate, to confirm | site-a-activity-list.md, A1; 12 March 2026 |
| C2 | Goods receipt, chilled / Warehouse lead | Is NordFrost still the carrier this activity requires? | Suppliers | candidate, to confirm | site-a-activity-list.md, A1 and Dependencies recorded; 12 March 2026 |
| C3 | Dispatch, chilled / Dispatch lead | Is this activity still in scope, and is LogiStock still its required warehouse system? | IT and applications | candidate, to confirm | site-a-activity-list.md, A2; 12 March 2026 |
| C4 | Dispatch, chilled / Dispatch lead | Is NordFrost still the carrier dispatch requires? | Suppliers | candidate, to confirm | site-a-activity-list.md, Dependencies recorded; 12 March 2026 |
| C5 | Dispatch, chilled / Dispatch lead | Does dispatch still require quality release before proceeding? | Departmental dependency | candidate, to confirm | site-a-activity-list.md, Dependencies recorded; 12 March 2026 |
| C6 | Quality release / QA manager | Is this activity still in scope, and does it require the laboratory recorded as being only at Site A? | Seats and buildings | candidate, to confirm | site-a-activity-list.md, A3; 12 March 2026 |
| C7 | Payroll / HR shared service | Is payroll in scope for this register, and what requirement follows from its recorded operation at head office? | Class to establish | candidate, to confirm | site-a-activity-list.md, A4; 12 March 2026 |

For every activity, people requirements and their mandates remain **not in the sources**. Other unlisted resource requirements remain interview gaps, rather than invented register entries. Approval of the activity list does not establish confirmation of individual resource requirements.

**Organiser’s take-in sheet**

Provisional total: 30 minutes. The timing is a planning assumption, not a source value.

Scope mismatch — 3 minutes  
The activity list is for Site A and the register is for Site B; which site should these rows belong to?

Impacts over time — 7 minutes  
Which approved impact categories, time horizons and thresholds should we use?  
What happens as dispatch remains stopped?  
How does that change during the recorded peak weeks?

MTPD — 3 minutes  
When do those impacts become unacceptable, and what evidence supports that point?

People — 4 minutes  
Are you the activity owner?  
Who must be available, with what skills and authority?

Seats and buildings — 3 minutes  
Which work areas and buildings must be available?  
Does dispatch also need the two dock doors recorded for goods receipt?

IT and applications — 4 minutes  
Is LogiStock still the system dispatch needs?  
What recovery time and acceptable data loss does the work require?  
What does manual export to the other site involve? **Drop detailed walkthrough first if late.**

Suppliers — 3 minutes  
Is NordFrost still the carrier you need?  
Is another carrier available now?

Departmental dependencies — 3 minutes  
Must quality release happen before dispatch?  
What recovery timing must that relationship support?  
Does export to the other site require another department? **Drop export detail first if late.**

**Gaps and handover**

- **Own statements, not sources:** you state that the data is high-sensitivity and this environment is approved for it; you asked to skip intake. Interviewee, additional deliverables and duration remain unspecified.
- **Planning assumptions:** dispatch is the interview focus; 30 minutes is provisional. Neither assumption supplies a register value.
- Approved impact criteria, activity rankings, current resource confirmation and interview evidence are **not in the sources**.
- The Site B register is a draft dated 1 September 2026. Its empty contents provide no confirmed requirements or substantive cross-site comparison. Resolve the site mismatch with the Site A and Site B BCM owners; put any subsequent requirement conflict to the two activity owners.
- The **activity owner** confirms each requirement and sets MTPD, RTO and RPO. **Top management** approves the BIA results. Individual reviewer names remain unspecified.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. Reviewer: ______. Review date: ______.

**Tool calls (JSON events):**

- none
