# $prepare-bia case 1, run1: Codex, guidance at 23ab607

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fee3-ec79-7ca3-ba61-9226804390b7`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the Site B dispatch interview guide. I’ll read its preflight instructions and the three attached files, then ask for the organiser details the skill requires.

What data sensitivity class do the attached materials hold?

The [prepare-bia preflight](.agents/skills/prepare-bia/preflight.md) requires: “Ask the data class first.” I listed filenames too early, but have not opened the attachments. It requires this check before reading them.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/preflight.md .agents/skills/prepare-bia/units/prompts/bia.md .agents/skills/prepare-bia/SKILL.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll read the three attachments now and keep the draft in chat, with all recovery fields empty.

The Site A list and impact criteria are approved and dated. Site B’s organisation chart is an undated, unversioned HR draft, so I’ll treat it as provisional.

Before drafting, the [prepare-bia skill](.agents/skills/prepare-bia/SKILL.md) requires these organiser details:

1. What is the interviewee’s role, and what do they know that you don’t?
2. What do you need back from the interview—for example, corrected dispatch activities, resource requirements and unresolved dependencies?
3. Please confirm that memory, past chats, other project files, connectors and web search are switched off for this task.

I’ll record your answers under Gaps as “own statements, not sources.”

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md impact-criteria.md site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/keep-it-running.md .agents/skills/prepare-bia/units/stages/analysis.md'`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

Sources:
- **Site A: activity list (chilled food production)** — version 3, 12 March 2026; approved by the site manager.
- **Impact criteria** — version 1.1, 4 February 2026; approved by top management.
- **Site B: organisation structure** — no version or date; HR draft, listed under Gaps and used only to frame questions.

# Site B dispatch interview guide

**Draft: every entry is “candidate, to confirm”.**

Interviewee: Site B dispatch lead, subject to confirmation of activity ownership. The activity owner confirms each requirement and sets MTPD, RTO and RPO. Top management approves the BIA results.

Ask the owner to **“use the draft as the thing to correct, not the thing to confirm; record what it could not have known”.** No requirement enters the register until the owner confirms it.

## Candidate activities and scope

Site A’s list provides comparison questions, not evidence that Site B performs the same activities. The sources do not rank activities by impact. Assess dispatch fully because it is the interview’s scope; ask only about differences for other activities if the owner includes them.

| Candidate activity question | Status | Source |
|---|---|---|
| Does Site B perform chilled dispatch, and where does the dispatch lead’s responsibility begin and end? | candidate, to confirm | Site A activity list, activity A2 |
| Is chilled goods receipt a separate Site B activity, and what does dispatch need from it? | candidate, to confirm | Site A activity list, activity A1; Gaps: Site B scope unconfirmed |
| Is quality release a separate activity supporting Site B dispatch, and which owner confirms that relationship? | candidate, to confirm | Site A activity list, activity A3 and Dependencies recorded; Gaps: provisional Site B QA coverage |
| Does payroll create any relevant dispatch dependency, or should it remain outside this interview’s scope? | candidate, to confirm | Site A activity list, activity A4; Gaps: no dispatch dependency recorded |

## 1. Impacts over time — 12 minutes

**Candidate, to confirm:** For an interruption of Site B dispatch, how do financial, customer and regulatory impacts develop over time? At which elapsed points does each impact change, and what evidence supports those points?

Use the approved criteria separately for each impact dimension:

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | Under EUR 10k a day | One customer complains | None |
| 2 | EUR 10k–100k a day | A key account is late | A report to the food authority |
| 3 | Over EUR 100k a day | A key account is lost | The authority stops production |

Source: **Impact criteria**, level table. No Site B impact ratings or elapsed thresholds are in the sources.

**Candidate, to confirm:** Are Site A’s dispatch peaks—weeks 49–52 and week 14—also Site B’s peaks? Where do they differ, and how does that change the interruption impacts?

Source: **Site A activity list**, activity A2.

For any additional activity brought into scope, ask where its impacts and peaks differ from dispatch; do not repeat the full assessment automatically.

## 2. MTPD — 5 minutes

**Candidate, to confirm:** At what point would dispatch interruption become unacceptable under the approved impact criteria, and why? Does that point differ during peak weeks?

Sources: **Impact criteria**, level table; **Site A activity list**, activity A2. Site B’s MTPD is not in the sources. Leave the field empty for the owner to set.

## 3. People — 8 minutes

Cover people **“with the skills, authorities and mandates the work needs”.**

**Candidate, to confirm:** Does the HR draft’s dispatch structure still apply, including the three shift leaders? What shift pattern applies in ordinary and peak weeks, and what staffing, skills, decision authority and cover does each shift require?

Source: **Gaps** — Site B organisation structure, dispatch reporting line, undated draft; organiser’s statement about the interviewee’s knowledge.

Do not translate the draft’s three shift leaders into a confirmed minimum staffing requirement.

## 4. Seats and buildings — 5 minutes

**Candidate, to confirm:** Does Site B dispatch require particular seats, buildings or dock facilities? Site A records two dock doors for goods receipt; is there any corresponding requirement relevant to Site B dispatch?

Source: **Site A activity list**, activity A1; **Gaps** — Site B dispatch facilities are not in the sources. The Site A dock count does not establish a Site B requirement.

## 5. IT and applications — 7 minutes

Cover IT and applications **“each with its RTO and its RPO”.**

**Candidate, to confirm:** Does Site B dispatch use LogiStock? Site A records a possible manual export to Site B: is that route still available, what does it support, and what must be available at each site for it to work?

**Candidate, to confirm:** For each application the owner identifies, what RTO and RPO does the owner set, based on the dispatch impacts and data needs?

Source: **Site A activity list**, activity A2. Site B application requirements and the export route’s current capability are unconfirmed. All recovery fields remain empty.

## 6. Suppliers and other third parties — 7 minutes

**Candidate, to confirm:** Site A’s March list names NordFrost: is NordFrost still the carrier there, and does Site B also rely on it? Who are Site B’s current carriers and contacts, and is there an alternative carrier?

Source: **Site A activity list**, activity A1 and Dependencies recorded; **Gaps** — organiser’s statement that the dispatch lead knows carrier contacts.

Site A records no second carrier. That does not establish a single-carrier dependency at Site B. Each supplier requirement needs owner confirmation.

## 7. Dependencies — 8 minutes

Cover **“up- and downstream relationships with other departments, each recorded with the RTO the relationship carries”.** Keep departmental relationships separate from suppliers.

**Candidate, to confirm:** Does Site B dispatch need quality release before it can dispatch, as Site A does? Is QA still covered from Site A, and what does each owner understand the handover to require?

Sources: **Site A activity list**, Dependencies recorded; **Gaps** — Site B organisation structure, QA line, undated draft.

**Candidate, to confirm:** Does the recorded manual export create an upstream or downstream departmental dependency between the sites? Which departments own each end, what is exchanged, and what RTO does each relationship carry?

Source: **Site A activity list**, activity A2.

**Candidate, to confirm:** Does Site B dispatch have a departmental relationship with goods receipt or the warehouse, and which other upstream or downstream relationships need recording?

Source: **Site A activity list**, activities A1–A2; **Gaps** — provisional Site B warehouse reporting line; actual departmental relationships are not in the sources.

Put any cross-site disagreement **to the two owners, not to the model**. No direct contradiction is established by the attachments.

## Candidate resource record

Each row remains a question. Blank cells are intentional.

| Resource class | Requirement question | Status | Source and source date | Interview | Confirmation date | MTPD | RTO | RPO | Relationship RTO |
|---|---|---|---|---|---|---|---|---|---|
| People and mandates | What people, shift cover, skills and authority does dispatch require? | candidate, to confirm | Gaps: Site B organisation structure, dispatch line; undated draft; organiser statement | | | | | | |
| Seats and buildings | Which seats, buildings and dock facilities does Site B dispatch require? | candidate, to confirm | Site A activity list, A1; 12 March 2026; Gaps: Site B facilities | | | | | | |
| IT and applications | Are LogiStock and the manual export route required for Site B dispatch? | candidate, to confirm | Site A activity list, A2; 12 March 2026 | | | | | | |
| Suppliers | Which carriers are required, and is NordFrost still relevant? | candidate, to confirm | Site A activity list, A1 and Dependencies recorded; 12 March 2026 | | | | | | |
| Departmental dependency | What QA release relationship does Site B dispatch require? | candidate, to confirm | Site A activity list, Dependencies recorded; 12 March 2026; Gaps: draft Site B QA line | | | | | | |
| Departmental dependency | What intersite relationship supports the manual export? | candidate, to confirm | Site A activity list, A2; 12 March 2026 | | | | | | |
| Departmental dependency | What warehouse or goods-receipt relationship does dispatch require? | candidate, to confirm | Site A activity list, A1–A2; 12 March 2026; Gaps: Site B relationship | | | | | | |

No source proposes recovery times, so there are no source recovery proposals to assess.

## Organiser’s take-in sheet

Allow about **52 minutes**. Questions marked **[drop first]** can be deferred if time runs short. No source conflict is established; start by checking the unresolved differences between sites.

**Impacts and peaks — 12 minutes**

Where does Site B dispatch differ from the Site A list?

Are weeks 49–52 and week 14 your peak weeks too?

When dispatch stops, how do the financial, customer and regulatory impacts change over time?

What evidence supports the impact levels and the points when they change?

[drop first] For any other activity in scope, where do its impacts differ from dispatch?

**MTPD — 5 minutes**

When does the interruption become unacceptable, and does that change at peak times?

**People — 8 minutes**

Does the draft structure with three shift leaders still apply?

What is the shift pattern, and what people, skills, authority and cover does each shift need at normal and peak times?

**Seats and buildings — 5 minutes**

Which seats, buildings and dock facilities does dispatch need?

[drop first] Is Site A’s record of two goods-receipt dock doors relevant to your requirements?

**IT and applications — 7 minutes**

Do you use LogiStock?

Does the manual export from Site A still work, and what does it let you do?

What RTO and RPO do you set for each application you need?

**Suppliers — 7 minutes**

Is NordFrost still relevant, and which carriers do you actually use?

Who holds the current carrier contacts, and is another carrier available?

**Dependencies — 8 minutes**

Do you need QA release before dispatch, and is QA still covered from Site A?

What does each department need to provide, and what RTO does that relationship carry?

Which departments own the manual export at each end?

What do you need from the warehouse, and who needs something from dispatch?

Which differences need both site owners to resolve?

## Gaps

- **Own statements, not sources:** the organiser identifies the interviewee as Site B’s dispatch lead, says they know the shift pattern and carrier contacts, and requests resources and peak weeks. These statements shape the interview; they establish no resource values.
- **Own statements, not sources:** the organiser classifies the material as high sensitivity and states that this environment is approved for high sensitivity.
- **Channel isolation:** the organiser did not answer whether memory, past chats, other project files, connectors and web search are switched off. For this draft, only the three attachments provide organisational evidence; skill documents provide method instructions. No connector or web search was used. The broader switch-off status remains unconfirmed.
- **Site B organisation structure:** undated, unversioned HR draft. Obtain a dated, approved structure and owner confirmation before treating its reporting lines or QA coverage as current.
- **Not in the sources:** Site B’s confirmed activities, activity priority, peak weeks, shift pattern, minimum resources, carrier contacts, impact progression and recovery objectives. Settle these with the activity owner and supporting current records.
- **Cross-site uncertainty:** Site A’s system, carrier, export route and release dependency do not establish Site B’s requirements. Resolve any conflicting accounts with both owners.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. Reviewer: __________. Review date: __________.

**Tool calls (JSON events):**

- none
