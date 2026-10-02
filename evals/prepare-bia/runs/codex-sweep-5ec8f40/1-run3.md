# $prepare-bia case 1, run3: Codex, guidance at 5ec8f40

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0feba-f0e3-7471-8a7b-64f372648e16`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the Site B dispatch interview guide. I’ll read its preflight instructions and the three attached files first.


What data sensitivity class do the attached materials hold?
- Public
- Internal
- Confidential
- Restricted

What data sensitivity class do the attachments hold: Public, Internal, Confidential or Restricted?

The [prepare-bia preflight](.agents/skills/prepare-bia/preflight.md) requires me to “ask the data class first” and “open no file before the answer.” I need this before reading the attachments.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/preflight.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll treat the material as High sensitivity and use your statement that this environment is approved. I’ll read only the three attachments and the skill’s guidance, with memory, past chats, other project files, connectors and web search excluded.


Who will be interviewed for Site B dispatch, and what do they know that you as organiser do not?

How long is the interview, and what do you need back beyond the interview guide—for example, a candidate register or a list of unresolved differences between sites?

Please confirm that memory, past chats, other project files, connectors and web search are excluded, so the only organisational sources are the three attached files.
- Confirmed: use only the three attachments
- A wider source scope is needed

Site A’s approved list names dispatch, LogiStock, NordFrost and a dependency on quality release. Site B’s organisation chart is an undated draft, so I’ll use it only to frame questions about roles and QA coverage. The sources contain no activity ranking or agreed time horizons; those remain gaps.


Before drafting, I need three details:

- Who is the interviewee, and what do they know that you do not?
- How long is the interview, and what do you need back beyond the guide?
- Confirm that only the three attachments may supply organisational information, with memory, past chats, other project files, connectors and web search excluded.

The [prepare-bia intake](.agents/skills/prepare-bia/units/prompts/bia.md) says to “Wait for my answers.” These details will set the scope and length of the guide.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/prompts/bia.md .agents/skills/prepare-bia/units/data-rules.md .agents/skills/prepare-bia/units/keep-it-runni`
- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md impact-criteria.md site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/stages/analysis.md .agents/skills/prepare-bia/units/workflow-design.md'`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

I’ll focus on dispatch resources and peak weeks, with the Site B dispatch lead as interviewee. I’ll record your answers as organiser statements. Since interview length and source exclusions were left unanswered, I’ll draft a short core question sheet and assume only the three attachments are in scope.


Sources:
- **site-a-activity-list.md** — version 3, 12 March 2026; approved by the Site A site manager.
- **impact-criteria.md** — version 1.1, 4 February 2026; approved by top management.
- **site-b-org-chart.md** — no version or date; draft from HR. Listed under Gaps; used only to frame questions, not as current evidence.

# Site B dispatch interview guide — draft

**Task:** Draft candidate activities, their resource requirements and interview questions for Site B dispatch, focusing on resources and peak weeks.

**Interviewee:** Site B dispatch lead, according to the organiser.

Tell the activity owner: **“Use the draft as the thing to correct, not the thing to confirm; record what it could not have known.”**

Every entry below is **candidate, to confirm**. A resource requirement enters the register only after the activity owner confirms it.

## Candidate activity and resource questions

Site A provides comparison prompts; its resources and peak weeks are not established requirements for Site B.

| Entry | Question for the activity owner | Source and source date | Status |
|---|---|---|---|
| Activity and peaks | Does Site B carry out chilled dispatch, and do weeks 49–52 and week 14 apply here, or are its peak weeks different? | site-a-activity-list.md, A2; 12 March 2026 | candidate, to confirm |
| People and mandates | Which people, skills, authorities and mandates does dispatch require? Does the draft structure of a dispatch lead and three shift leaders reflect the current arrangement? | site-b-org-chart.md, Dispatch branch; undated draft, under Gaps | candidate, to confirm |
| Seats and buildings | Which seats, buildings and dispatch facilities are required? Site B requirements are not in the sources. | Gaps | candidate, to confirm |
| IT and applications | Does Site B use LogiStock, and can it receive the manual export that Site A lists? Which applications does Site B actually require? | site-a-activity-list.md, A2; 12 March 2026 | candidate, to confirm |
| Suppliers and third parties | Does Site B depend on NordFrost? Which carriers are required, and are alternatives available? | site-a-activity-list.md, recorded dependencies; 12 March 2026 | candidate, to confirm |
| Upstream departmental dependency | Does Site B dispatch require quality release from Site A, and how is that relationship handled? | site-a-activity-list.md, A2–A3 dependency; 12 March 2026. site-b-org-chart.md, QA branch; undated draft, under Gaps | candidate, to confirm |
| Other departmental dependencies | Which other departments provide inputs to dispatch or depend on its outputs? These relationships are not in the sources. | Gaps | candidate, to confirm |

For **each entry**, retain its source and source date above and leave these audit and recovery fields empty:

| Interview reference | Confirmation date | MTPD | RTO | RPO | Dependency RTO |
|---|---|---|---|---|---|
| | | | | | |

No attached source proposes a recovery time.

## 1. Impacts over time

**Candidate, to confirm:** For chilled dispatch, what financial, customer and regulatory impacts develop across the agreed assessment horizons, during ordinary weeks and peak weeks?

Use the approved criteria from **impact-criteria.md, impact-level table, 4 February 2026**:

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | under EUR 10k a day | one customer complains | none |
| 2 | EUR 10k–100k a day | a key account is late | a report to the food authority |
| 3 | over EUR 100k a day | a key account is lost | the authority stops production |

Ask for evidence behind each assessment and when each threshold would be reached. Leave ratings unfilled before the interview.

The sources do not rank activities or supply assessment horizons. Dispatch is the sole activity receiving a full impact discussion because it is the requested scope, not because the sources rank it highest. If the owner identifies separate dispatch activities, ask where their impacts differ before extending the assessment.

## 2. The MTPD

**Candidate, to confirm:** At what point do dispatch impacts become unacceptable, using the approved criteria, and does that point differ during peak weeks?

The activity owner sets MTPD. Its field remains empty.

## 3. People

**Candidate, to confirm:** What shift pattern applies, and which people are needed on each shift, with the skills, authorities and mandates the work needs?

Does the HR draft accurately describe the dispatch lead and three shift leaders? How do requirements change in peak weeks? Does any requirement depend on one person, and what cover exists?

Source: **site-b-org-chart.md, Dispatch branch**, undated draft under Gaps. Shift patterns and required staffing are **not in the sources**.

## 4. Seats and buildings

**Candidate, to confirm:** Which seats, buildings and dispatch facilities are essential, and how do their requirements change during peak weeks?

Site B requirements are **not in the sources**. Site A’s two dock doors are recorded for goods receipt, not dispatch; they must not be carried into Site B’s dispatch requirements.

Source: **site-a-activity-list.md, A1**, 12 March 2026.

## 5. IT and applications

**Candidate, to confirm:** Which IT systems and applications does dispatch need, each with its RTO and its RPO?

Does Site B use LogiStock? Is the manual export from Site A usable at Site B, and what does it require at the receiving end?

Source: **site-a-activity-list.md, A2**, 12 March 2026. The owner sets each RTO and RPO; both fields remain empty.

## 6. Suppliers and other third parties

**Candidate, to confirm:** Which carriers and other third parties are required, including during peak weeks?

Does NordFrost serve Site B? Who holds the carrier contacts, and what alternatives are available? Site A records no second carrier; this is not evidence that Site B has only one.

Source: **site-a-activity-list.md, recorded dependencies**, 12 March 2026. A single carrier or contact person remains a question, not a finding.

## 7. Dependencies

**Candidate, to confirm:** What are dispatch’s up- and downstream relationships with other departments, each recorded with the RTO the relationship carries?

Does Site A QA release Site B’s goods before dispatch? What must pass between QA and dispatch? Which other departments provide inputs or receive dispatch outputs?

Sources: **site-a-activity-list.md, A2–A3 dependency**, 12 March 2026; **site-b-org-chart.md, QA branch**, undated draft under Gaps. Each dependency RTO remains empty.

## Cross-site comparison

The attachments establish **no confirmed conflict** between sites. They leave these differences unresolved:

- Site A lists LogiStock and a manual export to Site B; Site B’s receiving arrangements are undocumented.
- Site A dispatch depends on quality release; the Site B draft says QA is covered from Site A, without defining the release relationship.
- Site A lists NordFrost with no second carrier recorded; Site B’s carriers are undocumented.
- Site A lists dispatch peaks in weeks 49–52 and week 14; Site B’s peak weeks are undocumented.

Put any conflicting accounts **to the two owners, not to the model**: the dispatch leads for dispatch arrangements, with the Site A QA manager involved in the release relationship.

## Gaps

- **Own statements, not sources:** The organiser says the interviewee is the Site B dispatch lead, who knows the shift pattern and carrier contacts; the requested return is resources and peak weeks. These statements shape the interview but fill no resource values.
- **Own statements, not sources:** The organiser classifies the material as High and states that this environment is approved for High.
- Interview length was not supplied. Assumption: use the short core sheet below; timing remains to be settled.
- Source exclusions were not explicitly confirmed. Assumption applied: only the three attachments supply organisational evidence; memory, past chats, other project files, connectors and web search were excluded.
- The Site B organisation chart is an undated, unversioned HR draft. A dated, approved chart or owner correction is needed.
- Site B’s approved activity list, resource requirements, peak weeks and dependency records are not in the sources. Owner evidence is needed.
- Activity priorities and assessment horizons are not in the sources. Agreed method parameters are needed before completing impact ratings.

## Organiser’s take-in sheet

Does Site A’s manual export actually support dispatch at Site B, and where do the two sites’ accounts differ?

Does Site A QA release your goods before dispatch, and does QA describe that relationship the same way?

Do you use NordFrost, and what other carriers can you use?

Are weeks 49–52 and week 14 your peak weeks, or are your peaks different?

What financial, customer and regulatory impacts develop as dispatch remains stopped, especially during peak weeks?

When do those impacts become unacceptable?

What is your shift pattern, and which people, skills and decision powers does each shift need?

Does the draft showing three shift leaders match how dispatch works today?

Which seats, buildings and dispatch facilities do you need during normal and peak weeks?

Which systems and applications do you need, and what recovery time and data loss limit will you set for each?

Where are carrier contacts held, and who can use them if the usual contact person is unavailable?

Which departments do you depend on, which depend on you, and what recovery time does each relationship carry?

What has this draft missed or got wrong?

The **activity owner** confirms each requirement and sets MTPD, RTO and RPO. **Top management approves the BIA results.** Hand on confirmed and unconfirmed marks intact.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

**Tool calls (JSON events):**

- none
