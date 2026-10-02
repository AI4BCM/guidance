# $prepare-bia case 1, run3: Codex, guidance at 23ab607

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fee4-89ac-7903-945b-5cc5c543dd00`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the Site B dispatch interview guide from the three attached files. I’ll read its preflight instructions and the source material first.

What data classification does the attached material have (for example, public, internal, confidential, or strictly confidential)? The prepare-bia preflight requires your answer before I read the attachments.

What data classification do the attachments have: public, internal, confidential, or strictly confidential?

The [prepare-bia preflight](.agents/skills/prepare-bia/preflight.md) requires your answer before I read them.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/preflight.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll treat the material as high-classification, based on your statement that this environment is approved for it. I’ll read only the three attachments and the skill’s guidance, and keep the draft in this chat.

Who will be interviewed (their role), and what do they know about Site B dispatch that you do not?

Besides the interview guide, what do you need back—for example, an organiser’s question sheet or a candidate register for the owner to correct?

Please confirm that memory, past chats, other project files, connectors and web search are switched off for this task. I am using only the three named attachments and the skill’s guidance.

The Site A list and impact criteria are approved and dated. Site B’s organisation chart is an undated draft, so I’ll use it only to frame questions.

Before drafting, the [skill’s intake instructions](.agents/skills/prepare-bia/units/prompts/bia.md) require these answers:

1. Who will be interviewed, and what do they know about Site B dispatch that you do not?
2. What do you need back besides the guide, if anything?
3. Can you confirm that memory, past chats, other project files, connectors and web search are switched off for this task?

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md impact-criteria.md site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/prompts/bia.md .agents/skills/prepare-bia/units/data-rules.md .agents/skills/prepare-bia/units/keep-it-runni`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/stages/analysis.md .agents/skills/prepare-bia/units/workflow-design.md'`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

I’ll focus on resources and peak weeks for the Site B dispatch lead. The sources do not establish Site B’s shift pattern, carrier, systems or peak weeks, so those will remain questions. I’ll also flag the draft organisation chart and ask both sites’ owners to resolve any conflicting dependency information.

**Site B dispatch interview guide — candidate, to confirm**

Sources:
- **site-a-activity-list.md:** version 3, 12 March 2026; approved by the Site A manager. References below identify the activity row or dependency note.
- **impact-criteria.md:** version 1.1, 4 February 2026; approved by top management.
- **site-b-org-chart.md:** no version or date; HR draft. Listed under Gaps and used only to frame questions.

Scope: draft candidate activities, their resource requirements and interview questions for Site B dispatch, with particular attention to resources and peak weeks.

### Candidate requirements for the owner to correct

Site A information supplies comparison questions; it does not establish Site B requirements. Every entry is **candidate, to confirm**.

| Area | Question for the Site B activity owner | Source and source date |
|---|---|---|
| Activity and peaks | Does Site B perform chilled dispatch, and what does that activity include? Do weeks 49–52 and week 14 also represent your peaks, or do your peaks differ? | Site A activity list, Dispatch row; 12 March 2026 |
| People and mandates | Who performs dispatch, with what skills, authorities and mandates? Is the draft reporting structure still accurate, including the three shift leaders? | Gaps; Site B organisation chart, undated HR draft |
| Seats and buildings | Which seats and buildings does dispatch require? Are the two dock doors recorded for Site A goods receipt relevant to Site B dispatch at all? | Site A activity list, Goods receipt row; 12 March 2026. Site B requirements: not in the sources |
| IT and applications | Does Site B use LogiStock? Does the manual export from Site A reach Site B, and what does dispatch need to use it? | Site A activity list, Dispatch row; 12 March 2026 |
| Suppliers and third parties | Is NordFrost still the carrier at Site A, and does it serve Site B? What other carriers or third parties does Site B dispatch require? | Site A activity list, dependency note; 12 March 2026 |
| Upstream departmental dependencies | Does Site B dispatch require QA release before dispatch? Is QA still covered from Site A, and does Site A’s laboratory support that release? | Site A activity list, Quality release row and dependency note; 12 March 2026. Site B QA coverage: Gaps, undated HR draft |
| Downstream departmental dependencies | Which other departments depend on Site B dispatch, and what do they need from it? | Gaps — not in the sources |

For **each entry**, retain its source and source date above and leave these fields empty before the interview:

| Interview reference | Confirmation date | MTPD | Resource RTO | IT RPO | Departmental relationship RTO |
|---|---|---|---|---|---|
| | | | | | |

No source proposes recovery times. A resource requirement enters the register only when its activity owner confirms it.

### 1. Impacts over time — about 12 minutes

First establish the agreed assessment time horizons; they are **not in the sources**. Assess dispatch in full as the sole activity in this interview’s scope. The attachments do not rank activities by criticality.

At each agreed horizon, ask what happens if Site B dispatch stops, what evidence supports the answer, and whether the effect changes during peak weeks.

Use the approved criteria exactly:

- Financial: level 1, “under EUR 10k a day”; level 2, “EUR 10k–100k a day”; level 3, “over EUR 100k a day”.
- Customer: level 1, “one customer complains”; level 2, “a key account is late”; level 3, “a key account is lost”.
- Regulatory: level 1, “none”; level 2, “a report to the food authority”; level 3, “the authority stops production”.

*Cite: Impact criteria, level rows; 4 February 2026.*

Which weeks are Site B’s peaks, and what makes them peaks? Are Site A’s weeks 49–52 and week 14 relevant? If the owner identifies separate dispatch activities, ask where their impacts differ before extending the full assessment.

### 2. MTPD — about 5 minutes

At what point would the evidenced impacts become unacceptable, in normal weeks and peak weeks? Which impact determines that point?

The activity owner sets MTPD. Its field remains empty in this draft.

### 3. People — about 8 minutes

Who is needed on each shift, **with the skills, authorities and mandates the work needs**? How does that requirement change during peak weeks?

Is the draft reference to three shift leaders still accurate? Who can authorise dispatch and cover the required responsibilities when someone is unavailable?

*Cite: Gaps; Site B organisation chart, undated HR draft.*

### 4. Seats and buildings — about 5 minutes

Which seats and buildings are required to perform Site B dispatch, and how do requirements change at peaks?

Do the two dock doors listed for Site A goods receipt have any relevance to Site B dispatch? Establish Site B’s requirement separately.

*Cite: Site A activity list, Goods receipt row; 12 March 2026. Site B requirements: not in the sources.*

### 5. IT and applications — about 8 minutes

Does Site B use LogiStock? Which applications and information does dispatch require, and what does each support?

The Site A list says manual export to Site B is possible. What is exported, can Site B use it, and what limitations does it have?

For every required application, ask the owner to establish **its RTO and its RPO**, supported by the impact assessment. Leave both fields empty here.

*Cite: Site A activity list, Dispatch row; 12 March 2026.*

### 6. Suppliers and other third parties — about 7 minutes

Is NordFrost still the carrier recorded for Site A, and is it also used at Site B? Which carriers and other third parties does Site B dispatch require?

The Site A record contains no second carrier. What alternatives does Site B actually have? Who holds the current carrier contacts, and where can the owner verify them?

A single supplier, carrier or contact remains a question until the owner establishes the requirement.

*Cite: Site A activity list, dependency note; 12 March 2026.*

### 7. Dependencies — about 8 minutes

Record **up- and downstream relationships with other departments, each with the RTO the relationship carries**.

Does QA release have to precede Site B dispatch? Is QA still provided from Site A, and what role does Site A’s laboratory play? What does dispatch need from QA, and what does QA need from dispatch?

Which other departments provide inputs to dispatch or depend on its outputs? Ask each relationship’s owners to reconcile their records; leave relationship RTO fields empty here.

*Cite: Site A activity list, Quality release row and dependency note; 12 March 2026. Site B QA coverage: Gaps, undated HR draft.*

### Organiser’s take-in sheet

Allow about **60 minutes**, including 7 minutes for source checks. Questions marked **Drop first** can be deferred if time runs short.

**Source checks and possible conflicts — 7 minutes**

Does Site B receive QA support from Site A, and does that include the release needed before dispatch?

Does the export described by Site A actually support Site B dispatch?

Are the reporting lines and three shift leaders in the draft organisation chart still accurate?

If the sites give different answers, what should we put to both owners to resolve the difference?

**Impacts and peaks — 12 minutes**

What stops when dispatch stops?

Which weeks are your peaks, and why?

Do the Christmas weeks and week fourteen listed for Site A also apply here?

At each agreed time point, what financial, customer and regulatory impacts occur?

What evidence supports those impacts?

**Maximum tolerable disruption — 5 minutes**

When do those impacts become unacceptable?

Does that point change during peak weeks?

**People — 8 minutes**

What is the shift pattern?

Who must be available on each shift, with which skills and authority?

How does that change during peak weeks?

Who can cover each required responsibility?

**Seats and buildings — 5 minutes**

Which seats and buildings must be available for dispatch?

What additional capacity do peak weeks require?

**Drop first:** Are Site A’s two goods-receipt dock doors relevant to this discussion?

**IT and applications — 8 minutes**

Which systems and information does dispatch need?

Do you use LogiStock?

Can you use the manual export from Site A?

What recovery time and data-loss limit will you set for each required application?

**Suppliers — 7 minutes**

Which carriers and other third parties do you require?

Is NordFrost still one of them?

Where are the current carrier contacts verified?

What alternatives are actually available?

**Dependencies — 8 minutes**

What must QA provide before you dispatch?

Which other departments do you depend on?

Which departments depend on you?

What recovery time must each departmental relationship carry?

### Gaps and review

- **Own statements, not sources:** the organiser identifies the Site B dispatch lead as interviewee, says they know the shift pattern and carrier contacts, and requests resources and peak weeks. These statements shape scope and fill no requirement value.
- **Channel confirmation omitted:** the organiser did not answer the channel question. Working assumption: exclude memory, past chats, other project files, connectors and web search. Only the three attachments and skill guidance were used.
- **Site B organisation chart:** undated, unversioned HR draft; current approval and accuracy are unresolved. The owner should correct it or provide a dated, approved replacement.
- Site B’s confirmed resources, peak weeks, impacts, assessment time horizons and recovery values are **not in the sources**.
- No established cross-site conflict is evidenced yet. Put any conflict found during the interview **to the two owners, not to the model**.

Tell the owner to **“use the draft as the thing to correct, not the thing to confirm; record what it could not have known”**.

The **activity owner** confirms each requirement and sets MTPD, RTO and RPO. **Top management approves the BIA results.** Hand on the interview record with confirmed and unconfirmed marks intact; every entry in this draft remains **candidate, to confirm**.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

**Tool calls (JSON events):**

- none
