# $prepare-bia case 1, run2: Codex, guidance at c332ccc

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0f9a8-94da-7e30-afd4-6ef00c80a2cc`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the Site B dispatch interview guide. I’ll read the attached material and the skill instructions, then ask for any missing interview details.

What sensitivity class applies to the three attachments—public, internal, confidential, or restricted—and is this environment approved for that class?

The [prepare-bia preflight](.agents/skills/prepare-bia/preflight.md) requires: “Before you read any attachment, ask the user what class of data it holds.” I haven’t opened the attachments.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/preflight.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

The approved Site A list gives dispatch candidates, but Site B’s org chart is an undated draft, so its roles and reporting lines need checking. The BCM practitioner running the interview will review the guide against the sources; the activity owner confirms requirements and sets MTPD and RTO.

Two interview details remain, as required by the [prepare-bia intake](.agents/skills/prepare-bia/SKILL.md):

1. Who is the interview with? A role is enough, plus what they know that you need to learn.
2. What do you need back from them—for example, dispatch scope, resources, peak weeks, impacts, or dependencies?

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/prompts/bia.md .agents/skills/prepare-bia/units/stages/analysis.md .agents/skills/prepare-bia/units/workflow`
- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md impact-criteria.md site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md .agents/skills/prepare-bia/units/tools.md .agents/skills/prepare-bia/units/keep-it-running.md `

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

I’ll focus the guide on resources and peak weeks for the Site B dispatch lead. Site A’s details will be prompts to correct, with gaps left open for the interview. I’ll keep all recovery fields blank.

From **site-a-activity-list.md**, version 3, 12 March 2026; approved by the Site A manager.
From **impact-criteria.md**, version 1.1, 4 February 2026; approved by top management.
Read **site-b-org-chart.md**, undated HR draft, no version; listed under Gaps and not treated as current evidence.

**Draft interview guide — Site B dispatch**

Interviewee: Dispatch lead, Site B.  
Required outputs: resources needed to operate dispatch and peak weeks.

The BCM practitioner running the interview checks this guide against its sources. Use the candidates as a draft to correct. A requirement enters the register only after the activity owner confirms it. The owner sets MTPD and RTO; top management approves the BIA results.

Tell the interviewee: “Please correct any Site A comparison that does not apply here. ‘I don’t know’ is a useful answer; we’ll record it for follow-up.”

Source references below: **A** = Site A activity list; **I** = impact criteria. **G** references a gap listed below. Every table entry is **candidate, to confirm**.

**Scope and impacts**

Ask about impacts before discussing resource recovery. Use the approved time horizons once supplied; none are attached.

| ID | Question for the dispatch lead | Basis |
|---|---|---|
| Q1 | What work falls within your dispatch activity at Site B? | A, row A2; Site B scope is G2 |
| Q2 | How would financial losses from a dispatch interruption develop over time? | I, Financial column |
| Q3 | How would customer impacts from a dispatch interruption develop over time? | I, Customer column |
| Q4 | How would regulatory impacts from a dispatch interruption develop over time? | I, Regulatory column |
| Q5 | What evidence supports the impact estimates? | G3 |
| Q6 | At what interruption duration would the impacts become unacceptable? | G3; owner’s MTPD decision |

Use the criteria as supplied:

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | “under EUR 10k a day” | “one customer complains” | “none” |
| 2 | “EUR 10k–100k a day” | “a key account is late” | “a report to the food authority” |
| 3 | “over EUR 100k a day” | “a key account is lost” | “the authority stops production” |

**Peak weeks**

| ID | Question for the dispatch lead | Basis |
|---|---|---|
| Q7 | Which calendar weeks are peak weeks for Site B dispatch? Site A records weeks 49–52 and week 14 as comparison points. | A, row A2 |
| Q8 | What causes those peaks at Site B? | G4 |
| Q9 | How do the resources needed for dispatch change during those peak weeks? | G4 |

**Resource requirements**

Record what dispatch needs to operate. Current staffing or equipment alone does not establish the requirement.

| ID | Resource class | Question for the dispatch lead | Basis |
|---|---|---|---|
| Q10 | People and mandates | What shift pattern must Site B dispatch support? | G1, G5; organiser identifies interviewee’s knowledge |
| Q11 | People and mandates | How many people are required in each dispatch role per shift? | G5 |
| Q12 | People and mandates | What skills are required for each dispatch role? | G5 |
| Q13 | People and mandates | What decision authority is required for each dispatch role? | G1, G5 |
| Q14 | Seats and buildings | What workspaces are required to operate dispatch? | G6 |
| Q15 | Seats and buildings | What building facilities are required to operate dispatch? | G6 |
| Q16 | IT and applications | Which applications does Site B dispatch require? Site A names LogiStock. | A, row A2; G7 |
| Q17 | IT and applications | What other IT resources does Site B dispatch require? | G7 |
| Q18 | IT and applications | What role, if any, does the manual export from Site A play in Site B dispatch? | A, row A2 |
| Q19 | Suppliers | Which carriers are required for Site B dispatch? Site A records NordFrost. | A, Dependencies recorded; G8 |
| Q20 | Suppliers | What service is required from each carrier? | G8 |
| Q21 | Suppliers | Which carrier contacts should dispatch use? | G8; organiser identifies interviewee’s knowledge |
| Q22 | Suppliers | Which alternative carriers, if any, are available to Site B dispatch? | A, Dependencies recorded; G8 |
| Q23 | Suppliers | Which other suppliers are required for dispatch? | G8 |

**Dependencies on other departments**

| ID | Question for the dispatch lead | Basis |
|---|---|---|
| Q24 | What quality-release input must Site B dispatch receive before it can proceed? | A, row A3 and Dependencies recorded; G1, G9 |
| Q25 | Which department provides that input to Site B? | G1, G9 |
| Q26 | What other inputs does dispatch require from other departments? | G9 |
| Q27 | Which departments depend on outputs from Site B dispatch? | G9 |

For each dependency identified, record the department and the required input or output separately. Carrier requirements belong under suppliers.

**Recovery fields — deliberately blank**

Repeat the relevant row for each resource or dependency identified during the interview.

| Activity, resource or relationship | MTPD | RTO | RPO | Dependency RTO |
|---|---|---|---|---|
| Site B dispatch | | | | |
| Each required IT resource or application | | | | |
| Each departmental dependency | | | | |

No source proposes a recovery time.

**Gaps and follow-up**

| Gap | What remains unresolved | What would settle it |
|---|---|---|
| G1 | Site B org chart: undated HR draft, no version. Its three shift leaders, reporting lines and Site A QA coverage are unverified. | Dispatch lead’s corrections through Q10–Q13 and Q24–Q25; dated, approved chart from HR. |
| G2 | Site B dispatch boundary: **not in the sources**. | Owner’s answer to Q1. |
| G3 | Site B impacts, supporting evidence, MTPD and approved assessment time horizons: **not in the sources**. | Q2–Q6; BCM practitioner supplies the agreed time horizons before impact assessment. |
| G4 | Site B peak weeks, causes and resource changes: **not in the sources**. Site A’s weeks are comparison candidates. | Q7–Q9. |
| G5 | Required shift pattern, staffing, skills and mandates: **not in the sources**. | Q10–Q13, including peak requirements from Q9. |
| G6 | Required dispatch workspaces and building facilities: **not in the sources**. Site A’s two dock doors concern goods receipt, not dispatch. | Q14–Q15. |
| G7 | Site B IT requirements and the purpose of Site A’s manual export: **not in the sources**. | Q16–Q18. |
| G8 | Site B suppliers, required services, carrier contacts and alternatives: **not in the sources**. No second carrier is recorded for Site A; that does not establish Site B’s position. | Q19–Q23. |
| G9 | Site B departmental dependencies and their recovery requirements: **not in the sources**. | Q24–Q27 and subsequent owner decisions. |
| G10 | Organiser’s own statements: interviewee is the Site B dispatch lead, knows shift patterns and carrier contacts; requested outputs are resources and peak weeks. These shape scope and supply no requirement values. | Interview record provides the operational answers. |

**Closing question:** Anything else we should know?

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/prompts/README.md'`
