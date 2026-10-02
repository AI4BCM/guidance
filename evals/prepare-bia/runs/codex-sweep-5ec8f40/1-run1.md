# $prepare-bia case 1, run1: Codex, guidance at 5ec8f40

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0feb7-dfac-7140-a50c-f63efa9228e8`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the Site B dispatch interview guide. I’ll read its preflight and the three attached files, then gather the organiser details it requires.

What data classification do the attached files have (for example, public, internal, confidential or restricted)?

The skill’s [preflight](.agents/skills/prepare-bia/preflight.md) requires: “Ask the data class first” and “open no file before the answer.” I’ll wait for the classification before opening the attached material.

What data classification do the three attachments have: public, internal, confidential or restricted?

The skill’s [preflight](/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs-codex/prepare-bia/1/run1/work/.agents/skills/prepare-bia/preflight.md) requires “Ask the data class first” before opening them.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"' -g '"'!'"\\.git'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/preflight.md .agents/skills/prepare-bia/units/prompts/bia.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll treat the material as high classification and this environment as approved for it. I’ll now read the attachments and gather the remaining organiser details before drafting.

What role does the interviewee hold, and what do they know about Site B dispatch that you do not?

What do you need back from the interview, and how long is the interview?

Please confirm that memory, past chats, other project files, connectors and web search are switched off for this task, with only the three attachments and the skill’s guidance in scope; identify any channel left on.

The Site A activity list and impact criteria are dated and approved. The Site B chart is an undated, unversioned HR draft, so I’ll use it only to raise questions. The attachments provide no activity ranking, impact time horizons or Site B recovery times; those will remain open.

Before drafting, please provide:

1. The interviewee’s role and what they know about Site B dispatch that you do not.
2. What you need back from the interview and its duration.
3. Confirmation that memory, past chats, other project files, connectors and web search are switched off for this task—or which remain on.

The [skill’s intake instructions](/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs-codex/prepare-bia/1/run1/work/.agents/skills/prepare-bia/units/prompts/bia.md) require “Wait for my answers.” The Site B chart is also an undated draft, so its contents will become questions for the owner; all recovery fields will stay blank.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md impact-criteria.md site-b-org-chart.md .agents/skills/prepare-bia/units/data-rules.md .agents/skills/prepare-bia/unit`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/stages/analysis.md .agents/skills/prepare-bia/units/workflow-design.md .agents/skills/prepare-bia/units/prom`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

I’ll focus on dispatch resources and peak weeks, using Site A’s dispatch record as a comparison. Interview length and the channel confirmation were omitted, so I’ll list them under Gaps and keep the take-in sheet short. LogiStock, NordFrost and the draft chart’s staffing details will remain questions for the Site B owner.

site-a-activity-list.md — Version 3, 12 March 2026; approved by the Site A site manager.
impact-criteria.md — Version 1.1, 4 February 2026; approved by top management.
site-b-org-chart.md — No version or date; HR draft, listed under Gaps and used only for questions.

**Site B dispatch interview guide — candidate, to confirm**

Purpose: draft candidate activities, resource requirements and interview questions for Site B dispatch, focusing on resources and peak weeks.

Tell the dispatch lead: **“Use the draft as the thing to correct, not the thing to confirm; record what it could not have known.”**

Every entry below is **candidate, to confirm**. A resource requirement enters the register only when its activity owner confirms it. All MTPD, RTO and RPO fields remain empty, including dependency RTOs. Interview references and confirmation dates remain blank before the interview.

**1. Impacts over time**

Candidate activity: does Site B carry out chilled dispatch, and where does its responsibility start and end?  
Source: site-a-activity-list.md, activity A2, 12 March 2026. Site A’s activity is a comparison prompt, not evidence of Site B’s operation.

For dispatch, ask how a stoppage develops across the organisation’s agreed time horizons. The horizons are **not in the sources**; obtain them before completing the ratings.

| Candidate impact question | Approved criterion | Source |
|---|---|---|
| How does the financial impact of stopped dispatch change over time, and what evidence supports each rating? | Level 1: under EUR 10k/day; level 2: EUR 10k–100k/day; level 3: over EUR 100k/day. | impact-criteria.md, Financial column, 4 February 2026 |
| When would dispatch disruption cause customer complaints, a late key account or the loss of a key account? | Levels 1, 2 and 3 respectively. | impact-criteria.md, Customer column, 4 February 2026 |
| Could dispatch disruption lead to a food-authority report or an authority stopping production, and when? | Level 1: none; level 2: report; level 3: production stopped by the authority. | impact-criteria.md, Regulatory column, 4 February 2026 |

Ask whether Site B’s peak weeks match Site A’s weeks 49–52 and week 14, and how peaks change these impacts.  
Source: site-a-activity-list.md, A2, 12 March 2026.

The sources do not rank activities by impact. Dispatch receives the full discussion because it is the requested scope. For goods receipt, quality release or payroll, ask only whether they fall within this interview’s scope and where their impacts differ; do not assume Site B performs them.  
Source: site-a-activity-list.md, A1, A3 and A4, 12 March 2026.

**2. The MTPD**

At what point would the evidenced impacts of stopped dispatch become unacceptable, including during peak weeks?

The activity owner sets the MTPD after considering impacts over time. No value is proposed here.

**3. People**

Which people are required for dispatch, **“with the skills, authorities and mandates the work needs”**?

Does the draft chart’s reference to three shift leaders reflect the current organisation? What shift pattern operates in normal and peak weeks, and what staffing and decision authority does each shift need?

Sources: site-a-activity-list.md, A2, 12 March 2026; site-b-org-chart.md, dispatch branch, undated draft—see Gaps. Staffing requirements and shift patterns are not established by an approved Site B source.

**4. Seats and buildings**

Which seats, buildings and dispatch locations are required at Site B, and what capacity must they provide during peak weeks?

Site B dispatch premises requirements are **not in the sources**. Site A’s two dock doors belong to goods receipt, A1; they must not be transferred to Site B dispatch as a requirement.

**5. IT and applications**

Does Site B dispatch use “LogiStock”? If so, which dispatch work depends on it?

What does Site A’s possible manual export to Site B provide, and does it support Site B dispatch in practice?

For each confirmed application, ask the owner to specify its RTO and RPO through the interview process. Leave both fields empty in this draft.

Source: site-a-activity-list.md, A2, 12 March 2026. Site B’s use of the system and the export’s operational role are unconfirmed.

**6. Suppliers and other third parties**

Which carriers and other third parties does Site B dispatch require? Does “NordFrost” serve Site B, and are other carriers available?

Which carrier contacts does the dispatch lead use, who maintains them, and how does carrier availability change during peak weeks?

Source: site-a-activity-list.md, Dependencies recorded, 12 March 2026. NordFrost and the absence of a recorded second carrier concern Site A; neither establishes Site B’s arrangements. The interviewee’s knowledge of carrier contacts is an organiser statement under Gaps.

**7. Dependencies**

Ask about **“up- and downstream relationships with other departments, each recorded with the RTO the relationship carries”**.

Does Site B dispatch require quality release from Site A before dispatch? What must QA provide, and which owner confirms the relationship?

Which relationships with warehouse or other departments must work for dispatch to continue? Which departments depend on dispatch’s outputs?

Sources: site-a-activity-list.md, Dependencies recorded, 12 March 2026; site-b-org-chart.md, QA and warehouse branches, undated draft—see Gaps. Additional relationships are **not in the sources**.

No direct contradiction is established by these attachments. Put the following unresolved cross-site questions **to the two owners, not to the model**:

- Site A’s quality-release dependency versus the draft statement that Site A covers Site B QA: Site B dispatch lead and Site A QA manager.
- The manual export’s meaning and limits: dispatch leads at both sites.
- Any differences in carrier provision or peak weeks found during the interview: dispatch leads at both sites.

The following is a candidate capture register; every row remains **candidate, to confirm**.

| Candidate question | Class | Source and date | MTPD | RTO | RPO | Interview reference | Confirmation date |
|---|---|---|---|---|---|---|---|
| Does Site B perform chilled dispatch within the proposed boundary? | Activity | Site A activity list, A2; 12 March 2026 | | | | | |
| Which dispatch roles, skills, authorities and mandates are required? | People | Site A activity list, A2; 12 March 2026; Gaps for Site B staffing | | | | | |
| Which seats and buildings are required? | Seats and buildings | Gaps: not in the sources | | | | | |
| Is LogiStock required for Site B dispatch? | IT and applications | Site A activity list, A2; 12 March 2026 | | | | | |
| Is the manual export to Site B required, and what supports it? | IT and applications | Site A activity list, A2; 12 March 2026 | | | | | |
| Is NordFrost required, and which other carriers serve dispatch? | Suppliers | Site A activity list, Dependencies recorded; 12 March 2026 | | | | | |
| Is Site A quality release required before Site B dispatch? | Department dependency | Site A activity list, Dependencies recorded; 12 March 2026; Gaps for Site B arrangement | | | | | |
| Which other departments supply or receive essential dispatch outputs? | Department dependencies | Gaps: not in the sources | | | | | |

No attached source proposes recovery times.

**Gaps**

- **Own statements, not sources:** the organiser identifies the interviewee as the Site B dispatch lead, who knows shift patterns and carrier contacts; the required return is resources and peak weeks. These statements shape the interview, not requirement values.
- **Own statement, not a source:** material is high classification and this environment is approved for high.
- **Interview duration:** omitted. Assumption: use the short take-in sheet below; no duration is assigned.
- **Channel status:** confirmation that memory, past chats, other project files, connectors and web search are switched off was omitted. Their disabled status is unconfirmed. This draft draws only on the three attachments, organiser statements and skill guidance.
- **Site B chart:** undated, unversioned HR draft. Its three shift leaders and Site A QA coverage are questions, not current findings. Obtain a dated, approved chart and owner correction.
- **Missing evidence:** Site B activity boundaries, resource requirements, peak weeks, impact ranking and agreed time horizons are not in the sources. Obtain owner evidence and the approved method parameters.
- **Financial thresholds:** the criteria do not explicitly resolve exactly EUR 10k/day and EUR 100k/day. Ask the criteria owner to clarify the boundaries.

**Organiser’s take-in sheet**

Does Site A release every load before Site B dispatches it, and will both owners agree on that relationship?
What does the manual export from Site A allow your team to do?
Does the draft chart still reflect your shift leaders and QA coverage?
Where does your dispatch responsibility start and end?
Which weeks are busiest, and do they differ from weeks 49–52 and week 14?
How do financial, customer and regulatory impacts grow during a stoppage, especially at peak?
When would those impacts become unacceptable?
What shift pattern, staffing, skills and decision authority do you need?
Which seats and buildings do you need, and what capacity is required at peak?
Which applications do you need, and what recovery time and data-loss limit does each need?
Which carriers do you use, what alternatives exist, and who maintains their contacts?
Which departments must provide something to dispatch, which depend on you, and what recovery time does each relationship need?
What has this draft missed or misunderstood?

The activity owner confirms each requirement and sets MTPD, RTO and RPO. **Top management approves the BIA results.** Preserve confirmed and unconfirmed marks through handover.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

**Tool calls (JSON events):**

- none
