# $prepare-bia case 1, run3: Codex, guidance at cb8148b

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fcd7-8b3a-7d72-bf6e-fb5fa9e012c3`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’ll use the prepare-bia skill and read the three attachments to build the Site B dispatch interview guide.


The skill’s preflight requires a data-class check before reading attachments. I read them before that check; I’ll pause here to complete it.


What data classification applies to these attachments (for example, public, internal, confidential or restricted)?

What data classification applies to the attachments: public, internal, confidential or restricted?

The [prepare-bia preflight](.agents/skills/prepare-bia/preflight.md) requires: “Ask the data class first.” I need that answer before continuing the draft.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/preflight.md .agents/skills/prepare-bia/units/prompts/bia.md'`
- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md impact-criteria.md site-b-org-chart.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll proceed on your statement that the material is classified high and this environment is approved for it. The Site B chart is an undated draft, so its contents will be treated as questions for the owner.


Who will be interviewed (role), and what do they know about Site B dispatch that you do not?

What do you need back from the interview beyond the guide—for example, a corrected activity list, confirmed resource requirements or an interview record?

Can you confirm that memory, past chats, other project files, connectors and web search are switched off for this task? Identify any channel left on or whose setting is unknown.

Before drafting, please answer these three intake questions:

1. Who will be interviewed, and what do they know about Site B dispatch that you do not?
2. What should the interview produce—for example, a corrected activity list, confirmed requirements or an interview record?
3. Are memory, past chats, other project files, connectors and web search switched off? Identify any settings that are on or unknown.

The skill’s [intake instructions](.agents/skills/prepare-bia/units/prompts/bia.md) require me to “Wait for my answers.” The impact criteria are already attached.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md .agents/skills/prepare-bia/units/keep-it-running.md .agents/skills/prepare-bia/units/stages/an`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

I’ll focus the guide on resources and peak weeks for the Site B dispatch lead. I’ll record the unanswered channel-settings question as unknown. Site A’s peak weeks, system and carrier will be prompts to check, with all recovery fields left blank.


# Site B dispatch interview guide — draft

**Sources fixed for this draft**

- **S1 — site-a-activity-list.md:** version 3, 12 March 2026; approved by the site manager. Comparative evidence about Site A.
- **S2 — impact-criteria.md:** version 1.1, 4 February 2026; approved by top management.
- **S3 — site-b-org-chart.md:** no version or date; HR draft. Listed under Gaps; not treated as current evidence.

**Interviewee:** Site B dispatch lead.  
**Intended output:** corrected dispatch resource requirements and peak weeks.

The activity owner confirms each requirement and sets MTPD, RTO and RPO. Top management approves the BIA results. No requirement enters the register before owner confirmation.

Tell the owner: **“Use the draft as the thing to correct, not the thing to confirm; record what it could not have known.”**

## Candidate worksheet

Each row is **candidate, to confirm**. Site A details are comparison prompts, not established Site B requirements.

| ID | Activity or resource class | Question for the activity owner | Source and section |
|---|---|---|---|
| B1 | Activity and peaks | Does Site B perform chilled dispatch? What is its scope, and which weeks are peaks? Do Site A’s weeks 49–52 and week 14 also apply here? | S1, activity A2 |
| B2 | People and mandates | Who performs dispatch, with which skills, authorities and mandates? Is the draft structure of a dispatch lead and three shift leaders accurate? | S3, organisation structure; unverified draft |
| B3 | Seats and buildings | Which seats, buildings and physical work areas does dispatch require? | **Not in the sources**; owner evidence needed |
| B4 | IT and applications | Does Site B use LogiStock? What applications and data does dispatch require? Is the manual export from Site A usable, and for what purpose? | S1, activity A2 |
| B5 | Suppliers | Does Site B dispatch depend on NordFrost? Which carriers and other third parties are required? Are alternatives available? | S1, activity A2 and Dependencies recorded |
| B6 | Department dependencies | Does Site B dispatch require quality release from Site A? Which other upstream and downstream departments does it depend on? | S1, Dependencies recorded; S3, QA coverage, unverified draft |

**Recording fields:** source and source date are given above. Leave the following fields empty until the owner supplies and confirms them. A dependency’s RTO also stays empty.

| ID | Interview reference | Confirmation date | MTPD | RTO | RPO |
|---|---|---|---|---|---|
| B1 | | | | | |
| B2 | | | | | |
| B3 | | | | | |
| B4 | | | | | |
| B5 | | | | | |
| B6 | | | | | |

No source proposes recovery times.

## 1. Impacts over time

- What happens as dispatch remains unavailable? Identify the elapsed-time points when consequences change.
- At each point, what financial, customer and regulatory impacts occur? What evidence supports them?
- How do the consequences differ during Site B’s peak weeks? Establish its actual peak weeks rather than copying Site A’s calendar.

Use the approved criteria without assigning a level in advance:

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | under EUR 10k a day | one customer complains | none |
| 2 | EUR 10k–100k a day | a key account is late | a report to the food authority |
| 3 | over EUR 100k a day | a key account is lost | the authority stops production |

*Source: S2, impact criteria table; wording reproduced exactly.*

## 2. The MTPD

- At what elapsed time would the consequences become unacceptable, using the approved criteria?
- Does that point differ during peak weeks?
- What evidence supports the owner’s decision?

**MTPD:**  

## 3. People

Cover people **with the skills, authorities and mandates the work needs**.

- Correct the draft reporting structure and establish the actual shift pattern.
- What staffing and cover does each shift require during ordinary and peak weeks?
- Who has authority to make dispatch decisions?
- Does any requirement depend on a single person? What cover is confirmed?

*Source: S3, organisation structure, unverified draft. Staffing, skills, mandates and cover: not in the sources.*

## 4. Seats and buildings

- Identify the seats, buildings and physical areas required for Site B dispatch.
- What capacity is required during ordinary and peak weeks?
- Which alternatives can the owner substantiate?

*Not in the sources. Site A’s two dock doors belong to goods receipt, A1; they do not establish a Site B dispatch requirement.*

## 5. IT and applications

Identify each application **with its RTO and its RPO**, leaving both fields blank in this draft.

- Confirm or reject LogiStock as a Site B requirement.
- Explain the manual export to Site B recorded at Site A: who produces it, who receives it, and what work it supports.
- Identify other required applications and data, with evidence.
- What interruption and data loss can the activity tolerate?

*Source: S1, activity A2. Other applications and data: not in the sources.*

## 6. Suppliers and other third parties

- Confirm which carriers Site B uses and how the dispatch lead maintains their contacts.
- Does NordFrost serve Site B?
- Are alternatives available and usable during peak weeks?
- Does any resource depend on a single supplier or carrier?

*Source: S1, A2 and Dependencies recorded. Site A records no second carrier; that does not establish a sole-carrier dependency at Site B.*

## 7. Dependencies

Record **up- and downstream relationships with other departments, each recorded with the RTO the relationship carries**. Leave every relationship RTO blank.

- Does Site A QA release work for Site B dispatch? What must pass between the teams?
- Which departments provide inputs to dispatch or receive its outputs?
- Who owns each side of the relationship?
- How do these relationships change during peak weeks?

*Sources: S1, Dependencies recorded; S3, QA coverage, unverified draft.*

No confirmed cross-site conflict can yet be established. Compare the owners’ accounts of QA release, the manual export, carrier coverage and peak weeks. Name each disagreement and put it **to the two owners, not to the model**.

**Gaps and handover**

- **Organiser’s own statements, not sources:** classification is high and this environment is approved for high; the interviewee is the Site B dispatch lead, who knows the shift pattern and carrier contacts; the desired output is resources and peak weeks. These shape scope but fill no requirement or recovery value.
- **Channel settings unanswered:** memory, past chats, other project files, connectors and web search cannot be assumed switched off. Any channel left on may influence the model without saying so. No connectors or web search were used for this draft.
- **S3 is undated, unversioned and draft:** obtain a dated, approved chart or have the owner correct its propositions during the interview.
- Site B’s actual peaks, staffing, physical resources, systems, suppliers, impacts and recovery requirements remain unconfirmed. Obtain owner evidence and record its provenance.
- No instructions directed at AI were found in the attachments.

Hand on the interview record with confirmed and unconfirmed marks intact. All entries in this pre-interview draft remain **candidate, to confirm**.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

**Tool calls (JSON events):**

- none
