# $prepare-bia case 1, run3: Codex, guidance at c332ccc

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0f9a9-0af0-7200-88dc-707ae3f3e211`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the Site B dispatch interview guide. I’ll read the supplied files and the skill’s intake requirements first.

What data sensitivity class do the three attachments hold, and is this environment approved for that class?

The [prepare-bia preflight](.agents/skills/prepare-bia/preflight.md) requires: “Before you read any attachment, ask the user what class of data it holds.” I’ve read the skill instructions; the attachments remain unopened.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md; cat .agents/skills/prepare-bia/preflight.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll read the three attachments now. The BCM practitioner running the interview will check the draft against its sources; the activity owner confirms requirements and sets MTPD and RTO, and top management approves the BIA results.

The approved Site A list gives useful dispatch candidates, but it does not establish Site B’s requirements. The Site B organisation chart is an undated, unversioned HR draft, so I’ll treat its roles as unverified.

The [prepare-bia skill](.agents/skills/prepare-bia/SKILL.md) requires “the interviewee’s role” and “the list of what the organiser needs back” before drafting:

1. Who is the interview with—the Site B dispatch lead or another role—and what do they know that you need to learn?
2. What do you need back from the interview? For example: dispatch scope, impacts over time, resource requirements, dependencies or peak weeks.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md impact-criteria.md site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/prompts/bia.md .agents/skills/prepare-bia/units/stages/analysis.md .agents/skills/prepare-bia/units/workflow`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md .agents/skills/prepare-bia/units/tools.md .agents/skills/prepare-bia/units/keep-it-running.md `

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

I’ll focus the guide on resources and peak weeks, with brief impact questions to establish priorities. Site A’s LogiStock, NordFrost and peak weeks will appear as comparison questions for the dispatch lead to correct. Site B’s shift pattern and carrier contacts remain interview gaps.

From **site-a-activity-list.md**, version 3, 12 March 2026; approved by the Site A manager.
From **impact-criteria.md**, version 1.1, 4 February 2026; approved by top management.
From **site-b-org-chart.md**, no version or date; HR draft, not used as current evidence.

**Draft interview guide — Site B dispatch**

Interviewee: Site B dispatch lead. Requested outputs: resource requirements and peak weeks.

The BCM practitioner checks this draft against its sources. Use it as something to correct. Invite “I don’t know” for every question; record unresolved answers for follow-up. Requirements enter the register only after the activity owner confirms them.

Source references below: **A2** = Site A activity list, row A2; **A-dependencies** = its dependencies paragraph; **Criteria** = the approved impact-criteria table. References to Site A support comparison questions only.

**Scope and priorities**

| ID | Question for the dispatch lead | Basis |
|---|---|---|
| Q1 | What work falls within your responsibility for dispatch at Site B? | Candidate activity, to confirm; A2 provides the Site A comparator. Site B scope is not in the sources. |
| Q2 | What financial impact would a dispatch interruption have over time, using the approved financial levels? | Candidate, to confirm; Criteria, Financial column. Site B impacts are not in the sources. |
| Q3 | What customer impact would a dispatch interruption have over time, using the approved customer levels? | Candidate, to confirm; Criteria, Customer column. Site B impacts are not in the sources. |
| Q4 | What regulatory impact would a dispatch interruption have over time, using the approved regulatory levels? | Candidate, to confirm; Criteria, Regulatory column. Site B impacts are not in the sources. |
| Q5 | What maximum tolerable period of disruption would you set based on those impacts? | Candidate, to confirm; value not in the sources. Owner to set MTPD. |

The approved criteria cover financial losses below EUR 10k, EUR 10k–100k and above EUR 100k **per day**; customer complaint, key-account lateness and key-account loss; and no regulatory consequence, a report to the food authority and an authority stop to production. Record evidence behind each impact answer.

**Peak weeks**

| ID | Question for the dispatch lead | Basis |
|---|---|---|
| Q6 | Which weeks are peak weeks for dispatch at Site B? | Candidate, to confirm; Site B peak weeks are not in the sources. |
| Q7 | How does Site B’s peak calendar differ from Site A’s weeks 49–52 and week 14? | Candidate, to confirm; A2, Peak weeks column. |
| Q8 | How do peak weeks change the resources dispatch needs? | Candidate, to confirm; Site B seasonal requirements are not in the sources. |

**Resource candidates**

All entries are **candidate, to confirm**. Ask what dispatch *needs to operate*, and record quantities and supporting evidence where the owner can supply them.

| ID | Resource class | Question for the dispatch lead | Source or gap |
|---|---|---|---|
| Q9 | People and mandates | What shift pattern does dispatch need? | Not in the sources; organiser says the interviewee knows the shift pattern. |
| Q10 | People and mandates | How many people does dispatch need on each shift? | Not in the sources. |
| Q11 | People and mandates | What skills must those people have? | Not in the sources. |
| Q12 | People and mandates | What decision-making authority must dispatch personnel have? | Not in the sources; current Site B roles are unverified. |
| Q13 | Seats and buildings | What workstations or seats does dispatch need? | Not in the sources. |
| Q14 | Seats and buildings | What building space or facilities does dispatch need? | Not in the sources. |
| Q15 | IT and applications | Which IT systems or applications does dispatch need? | Not in the sources for Site B; A2 names LogiStock for Site A. |
| Q16 | IT and applications | What role, if any, does LogiStock play in Site B dispatch? | A2, Notes column; applicability to Site B is unconfirmed. |
| Q17 | IT and applications | What role, if any, does the manual export to Site B play in your dispatch work? | A2, Notes column; its purpose and Site B use are unconfirmed. |
| Q18 | IT and applications | What information does dispatch need from its systems? | Not in the sources. |
| Q19 | Suppliers | Which carriers or other suppliers does dispatch need? | Not in the sources for Site B; A-dependencies names NordFrost for Site A. |
| Q20 | Suppliers | What service does each supplier need to provide? | Not in the sources for Site B. |
| Q21 | Suppliers | What role, if any, does NordFrost play in Site B dispatch? | A-dependencies; applicability to Site B is unconfirmed. |
| Q22 | Suppliers | Which carrier contact roles must dispatch be able to reach? | Not in the sources; organiser says the interviewee knows the carrier contacts. |
| Q23 | Suppliers | Which alternative carriers, if any, can meet dispatch’s requirements? | Not in the sources for Site B; A-dependencies records no second carrier for Site A. |

**Department dependencies and remaining gaps**

All entries are **candidate, to confirm**.

| ID | Question for the dispatch lead | Source or gap |
|---|---|---|
| Q24 | Which departments must provide inputs before dispatch can operate? | Not in the sources for Site B. |
| Q25 | What quality-release input does Site B dispatch require? | A-dependencies records release before dispatch at Site A. Site B arrangement is unconfirmed. |
| Q26 | Which departments rely on outputs from Site B dispatch? | Not in the sources. |
| Q27 | What output does each dependent department need from dispatch? | Not in the sources. |
| Q28 | Which current approved document describes Site B’s dispatch responsibilities? | Site B organisation chart is an undated, unversioned HR draft. |
| Q29 | Anything else we should know? | Closing opportunity to correct omissions. |

**Recovery fields — left empty for the owners**

Repeat the relevant resource or dependency row when recording the interview.

| Item | MTPD | RTO | RPO | Dependency RTO |
|---|---|---|---|---|
| Site B dispatch | | | | |
| Each IT system/application | | | | |
| Each department dependency | | | | |

No source proposes a recovery time. The activity owner sets MTPD and RTO; RPO remains for its owner to set.

**Gaps and how to settle them**

- **Organiser’s statements, not documentary evidence:** interviewee is the Site B dispatch lead, knows shift patterns and carrier contacts; requested outputs are resources and peak weeks. Q9 and Q22 elicit the missing details.
- **Site B organisation chart:** draft, no version or date. Obtain a current approved version through Q28. Its references to three shift leaders and QA coverage from Site A do not establish current resource requirements.
- **Site B operating requirements:** not in the sources. Q1 and Q6–Q27 test applicability and elicit requirements; Site A details must not be transferred automatically.
- **Site B impacts and recovery values:** not in the sources. Q2–Q5 establish the owner’s evidence and decision.
- **Assessment time horizons:** not in the sources. The BCM practitioner must obtain the agreed method parameters before formal impact scoring.

Top management approves the BIA results.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

**Tool calls (JSON events):**

- none
