# $prepare-bia case 1, run1: Codex, guidance at c332ccc

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0f9a8-6e26-7de2-bf83-f5c40fbbb64a`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’ll use the prepare-bia skill to read the source material and structure the Site B dispatch interview guide.

What data classification applies to the three attachments, and is this environment approved for that class?

The [prepare-bia preflight](.agents/skills/prepare-bia/preflight.md) requires: “Before you read any attachment, ask the user what class of data it holds.” I’ll wait for your answer before opening them.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!LICENSE'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/preflight.md .agents/skills/prepare-bia/SKILL.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll read the attachments now. The BCM practitioner running the interview will check the guide against its sources; the activity owner sets MTPD and RTO, and top management approves the BIA results.

The approved Site A list provides dispatch topics to explore, but does not establish Site B’s requirements. Site B’s org chart is an undated, unversioned HR draft.

1. Who is the interview with—Site B’s dispatch lead or another role—and what knowledge do they bring that you need?
2. What do you need back from the interview? For example: activity boundaries, impacts over time, resource requirements, departmental dependencies, or peak weeks.

The [prepare-bia intake](.agents/skills/prepare-bia/SKILL.md) requires knowing “the interviewee’s role” and “what the organiser needs back” before drafting. The impact criteria are already attached.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md impact-criteria.md site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/prompts/bia.md .agents/skills/prepare-bia/units/stages/analysis.md .agents/skills/prepare-bia/units/workflow`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

I’ll focus the guide on resources and peak weeks for Site B’s dispatch lead. Site A’s dispatch details will serve as prompts to correct, while Site B’s shift pattern, carrier contacts and organisation structure remain questions for the interview.

From **site-a-activity-list.md**, version 3, 12 March 2026; approved by the Site A site manager.  
From **impact-criteria.md**, version 1.1, 4 February 2026; approved by top management.  
Read **site-b-org-chart.md**, undated, unversioned HR draft; listed under Gaps and not treated as current evidence.

## Draft interview guide — Site B dispatch

**Interviewee:** Dispatch lead, Site B.  
**Requested outcome:** Resource requirements and peak weeks.  
**Reviewer:** BCM practitioner running the interview, who checks this draft against its sources.

Tell the interviewee: “Please correct the draft wherever it differs from Site B. ‘I don’t know’ is a useful answer; we will record it as a follow-up.”

Source references below: **A** = Site A activity list; **I** = impact criteria; **G** = numbered gap below. Site A facts support candidate questions only; they do not establish Site B requirements.

### 1. Scope and interruption impacts

Ask these first to establish what the resources must support.

| ID | Question | Status and basis |
|---|---|---|
| Q1 | Which work falls within your responsibility for dispatch at Site B? | **candidate, to confirm** — A, row A2; G2 |
| Q2 | Does Site B’s dispatch activity include chilled products? | **candidate, to confirm** — A, row A2; G2 |
| Q3 | How would financial losses develop over time if Site B dispatch stopped, using the approved financial thresholds? | **candidate, to confirm** — I, Financial column; G3 |
| Q4 | How would customer impacts develop over time if dispatch stopped, using the approved customer criteria? | **candidate, to confirm** — I, Customer column; G3 |
| Q5 | How would regulatory impacts develop over time if dispatch stopped, using the approved regulatory criteria? | **candidate, to confirm** — I, Regulatory column; G3 |
| Q6 | Based on those impacts, what maximum tolerable period of disruption (MTPD) would you set for this activity? | **candidate, to confirm** — G3; owner decision |

The approved criteria distinguish financial losses of under EUR 10k, EUR 10k–100k and over EUR 100k per day; customer impacts from a complaint through a late key account to loss of a key account; and regulatory impacts from none through reporting to the food authority to an authority stop on production. No Site B impact level is assigned in this draft.

### 2. Peak weeks

| ID | Question | Status and basis |
|---|---|---|
| Q7 | Which weeks are peak weeks for Site B dispatch? | **candidate, to confirm** — G4 |
| Q8 | How does Site B’s peak calendar differ from Site A’s recorded “weeks 49–52, week 14”? | **candidate, to confirm** — A, row A2 |
| Q9 | What evidence supports the peak weeks you identified? | **candidate, to confirm** — G4 |

### 3. Candidate resource requirements

For each resource answer, record what dispatch **needs to operate**, including any change during peak weeks.

| Class | ID | Question for the activity owner | Status and basis |
|---|---|---|---|
| People and mandates | Q10 | What shift pattern must Site B dispatch support? | **candidate, to confirm** — G5 |
| People and mandates | Q11 | How many people are needed in each dispatch role per shift? | **candidate, to confirm** — A, row A2 identifies a dispatch lead at Site A; Site B quantities are G5 |
| People and mandates | Q12 | What skills are required for each dispatch role? | **candidate, to confirm** — G5 |
| People and mandates | Q13 | What decision authority does each dispatch role need? | **candidate, to confirm** — G5 |
| Seats and buildings | Q14 | What seats or workstations does dispatch require? | **candidate, to confirm** — G6 |
| Seats and buildings | Q15 | What buildings or working areas does dispatch require? | **candidate, to confirm** — G6 |
| IT and applications | Q16 | Which IT systems or applications does Site B dispatch require? | **candidate, to confirm** — A, row A2 names “LogiStock” at Site A; Site B use is G7 |
| IT and applications | Q17 | What role, if any, does the Site A manual export play in Site B dispatch? | **candidate, to confirm** — A, row A2: “manual export to Site B possible” |
| IT and applications | Q18 | What RTO would you set for each required system or application? | **candidate, to confirm** — G7; recovery fields remain empty |
| IT and applications | Q19 | What RPO is required for each required system or application? | **candidate, to confirm** — G7; recovery fields remain empty |
| Suppliers | Q20 | Which carriers or other suppliers does Site B dispatch require? | **candidate, to confirm** — A, Dependencies recorded identifies NordFrost for Site A; Site B suppliers are G8 |
| Suppliers | Q21 | What service must each supplier provide for dispatch to operate? | **candidate, to confirm** — G8 |
| Suppliers | Q22 | Which carrier contacts should the interview record reference? | **candidate, to confirm** — G8 |

Do not transfer Site A’s two dock doors into Site B’s requirements: that detail belongs to **goods receipt**, A row A1.

### 4. Departmental dependencies

Treat carriers as suppliers above. Record relationships with other departments separately.

| ID | Question | Status and basis |
|---|---|---|
| Q23 | Which departments must provide an input before Site B can dispatch? | **candidate, to confirm** — A, Dependencies recorded: Site A dispatch depends on quality release; G9 |
| Q24 | What input is required from each upstream department? | **candidate, to confirm** — A, row A3 and Dependencies recorded; G9 |
| Q25 | Which departments depend on an output from Site B dispatch? | **candidate, to confirm** — G9 |
| Q26 | What output does each downstream department require? | **candidate, to confirm** — G9 |
| Q27 | What RTO must each departmental relationship carry? | **candidate, to confirm** — G9; recovery fields remain empty |

### 5. Check the gaps and close

| ID | Question | Status and basis |
|---|---|---|
| Q28 | What corrections are needed to the dispatch-related structure in the draft Site B org chart? | **candidate, to confirm** — G1; draft reference only |
| Q29 | Who can provide the current approved Site B organisation chart? | **candidate, to confirm** — G1 |
| Q30 | Which resource requirements change during Site B’s peak weeks? | **candidate, to confirm** — G4–G8 |
| Q31 | Who should resolve each answer recorded as “I don’t know”? | **candidate, to confirm** — unresolved gaps |
| Q32 | Anything else we should know? | **candidate, to confirm** — closing question |

## Gaps and how to settle them

| Gap | What remains unresolved | How to settle it |
|---|---|---|
| G1 | Site B org chart: undated, no version, HR draft. It proposes three shift leaders and QA coverage from Site A; neither is established as current. | Corrections from the interviewee and a current approved chart; Q28–Q29. |
| G2 | Site B’s dispatch boundary and chilled-product scope: **not in the approved sources**. | Owner’s description; Q1–Q2. |
| G3 | Site B impacts, agreed assessment time horizons and recovery values: **not in the sources**. The criteria also do not specify the point at which disruption becomes intolerable. | BCM practitioner supplies agreed method parameters; owner provides impact evidence and sets recovery values; Q3–Q6, Q18–Q19, Q27. |
| G4 | Site B peak weeks: **not in the sources**. Site A’s calendar is a comparison prompt. | Owner’s calendar and supporting evidence; Q7–Q9, Q30. |
| G5 | Site B shift pattern, staffing, skills and mandates: **not in the approved sources**. | Owner’s account of requirements; Q10–Q13, Q30. |
| G6 | Site B seats and buildings: **not in the sources**. | Owner’s requirements; Q14–Q15, Q30. |
| G7 | Site B IT requirements and use of the Site A manual export: **not established by the sources**. | Owner’s explanation, with system-owner follow-up where needed; Q16–Q19, Q30. |
| G8 | Site B suppliers, required services and carrier contacts: **not in the sources**. | Owner’s requirements and contact references; Q20–Q22, Q30. |
| G9 | Site B upstream and downstream departmental relationships: **not in the approved sources**. | Owner’s account, followed by reconciliation with the other departmental owners; Q23–Q27. |

**Organiser statements, not documentary sources:** You identified the Site B dispatch lead as the interviewee, said they know the shift pattern and carrier contacts, and requested resources and peak weeks. These statements shape the interview scope; they supply no staffing, supplier or peak-week values.

Recovery fields remain empty:

| Candidate item | MTPD | RTO | RPO | Dependency RTO |
|---|---|---|---|---|
| Site B dispatch | | | | |
| Each required IT system/application | | | | |
| Each departmental relationship | | | | |

A drafted requirement enters the register only after the activity owner confirms it. The owner sets MTPD and RTO; top management approves the BIA results.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

**Tool calls (JSON events):**

- none
