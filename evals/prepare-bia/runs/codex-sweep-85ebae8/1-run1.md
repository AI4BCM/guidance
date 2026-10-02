# $prepare-bia case 1, run1: Codex, guidance at 85ebae8

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fc67-e3fa-7411-8314-d7710ab13692`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the interview guide from your files. I’ll check the material and identify any interview details needed before drafting.

What data sensitivity class do the three attached documents hold, and is this environment approved for that class?

Before I open the attachments, what data sensitivity class do they hold, and is this environment approved for that class?

The skill’s [preflight.md](.agents/skills/prepare-bia/preflight.md) requires: “Ask the data class first” and “open no file before the answer.” I’ve read the skill instructions only.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd && rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"' . /home/brain/.codex/skills/role-bia-facilitation 2>/dev/null"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/preflight.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Thanks. I’ll read the three documents and the skill’s drafting guidance, then check which interview details remain open.

Who is the Site B interview with (a role is enough), and what do they know that you need to learn from them?

What do you need back from the interview—for example, resource requirements, peak weeks, dependencies or impacts over time?

The impact criteria are approved. Site A’s activity list can support candidate questions, but Site B’s org chart is an undated, unversioned HR draft, so I’ll flag it as a gap.

To tailor the guide:

1. Who is the interview with—a role is enough—and what do they know that you need to learn?
2. What do you need back from them, such as resources, peak weeks, dependencies or impacts over time?

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md impact-criteria.md site-b-org-chart.md .agents/skills/prepare-bia/units/prompts/bia.md .agents/skills/prepare-bia/uni`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

I’ll focus the guide on resources and peak weeks, with questions for the dispatch lead about shift patterns and carrier contacts. I’ll use Site A’s details as prompts to correct, leave recovery fields blank, and flag the draft Site B org chart for checking.

**Draft: Site B dispatch interview guide**

Sources:
- **S1 — site-a-activity-list.md:** version 3, 12 March 2026; approved by Site A’s site manager. Sections: activity table, rows A1–A3; Dependencies recorded.
- **S2 — impact-criteria.md:** version 1.1, 4 February 2026; approved by top management. Section: impact-level table.
- **G1 — site-b-org-chart.md:** undated, unversioned HR draft; listed under Gaps and not used as current evidence.

Interviewee: Dispatch lead, Site B.  
Requested output: resource requirements and peak weeks.  
Status: draft for review by the BCM practitioner conducting the interview.

Site A’s arrangements are starting points for questions, not established Site B requirements. Invite the interviewee to correct or reject them. “I don’t know” is a useful answer; record it as an unresolved point.

### Candidate questions and coverage

All entries are **[candidate, to confirm]**. Question numbers refer to the interview sequence below.

| Theme | Candidate question | Basis | Guide |
|---|---|---|---|
| Activity boundary | Does Site B dispatch include chilled products? | S1, A2; applicability to Site B unresolved | Q1–2 |
| Peak weeks | Which weeks are peak weeks for Site B dispatch? | S1, A2 records peaks at Site A | Q8–10 |
| People and mandates | What staffing does Site B dispatch require across its shifts? | S1, A2 identifies a dispatch lead; other requirements not in the sources | Q11–15 |
| Seats and buildings | What seats and building facilities does Site B dispatch require? | Not in the sources; Site A’s two dock doors belong to goods receipt, A1 | Q16–17 |
| IT and applications | Does Site B dispatch require “LogiStock”? | S1, A2; Site B applicability unresolved | Q18–20 |
| Suppliers | Does Site B dispatch require NordFrost? | S1, Dependencies recorded; Site B applicability unresolved | Q21–24 |
| Upstream departments | Does Site B dispatch require quality release before dispatch? | S1, A3 and Dependencies recorded | Q25–26 |
| Downstream departments | Which departments require outputs from Site B dispatch? | Not in the sources | Q27 |

Recovery fields remain empty:

| Activity MTPD | Activity RTO | IT/application RTO | IT/application RPO | Department dependency RTO |
|---|---|---|---|---|
| | | | | |

No source proposes a recovery time.

### Interview sequence

Each numbered question is **[candidate, to confirm]**. Capture corrections, supporting evidence and unresolved points beside each answer.

**Activity boundary and impacts**

1. Does Site B dispatch include chilled products? *(S1, A2)*
2. What work falls within the Site B dispatch activity? *(G2)*
3. How would a dispatch interruption affect financial losses over time? *(S2, Financial column; G3)*
4. How would a dispatch interruption affect customers over time? *(S2, Customer column; G3)*
5. How would a dispatch interruption affect regulatory outcomes over time? *(S2, Regulatory column; G3)*
6. What evidence supports those impact estimates? *(G3)*
7. At what interruption duration would dispatch impacts become unacceptable? *(S2; G3 — owner’s MTPD judgment, not a value supplied by this draft)*

Facilitator: use the approved financial, customer and regulatory criteria. Agree the missing assessment time horizons through the BCM method before recording comparable impact ratings. Leave draft recovery fields empty.

**Peak weeks**

8. Which weeks are peak weeks for Site B dispatch? *(S1, A2 as comparator)*
9. Do Site A’s peak periods—weeks 49 through 52 and week 14—also apply at Site B? *(S1, A2)*
10. What resource requirements change during Site B’s peak weeks? *(G4)*

**People and mandates**

11. What shift pattern does Site B dispatch require? *(G4)*
12. What minimum staffing is required for each shift? *(G4)*
13. Which roles are required for dispatch to operate? *(S1, A2; G4)*
14. What skills must those roles have? *(G4)*
15. What decision-making mandates must those roles hold? *(G4)*

**Seats and buildings**

16. What seats or workstations are required for dispatch? *(G5)*
17. What building facilities are required for dispatch? *(G5)*

Facilitator: do not carry Site A’s two dock doors into dispatch requirements; S1 assigns them to goods receipt.

**IT and applications**

18. Does Site B dispatch require “LogiStock”? *(S1, A2)*
19. What other IT or applications are required for dispatch? *(G5)*
20. Does the manual export to Site B recorded at Site A support Site B dispatch? *(S1, A2)*

Record each required application separately. Its RTO and RPO fields remain blank in this draft for the owner to set through the BIA.

**Suppliers and carrier contacts**

21. Does Site B dispatch require NordFrost? *(S1, Dependencies recorded)*
22. What other suppliers are required for dispatch? *(G6)*
23. Which carrier contacts are needed to operate dispatch? *(G6)*
24. Where is the authoritative carrier-contact record maintained? *(G6)*

**Department dependencies**

25. Does Site B dispatch require quality release before dispatch? *(S1, Dependencies recorded)*
26. Which departments provide inputs required by Site B dispatch? *(G7)*
27. Which departments require outputs from Site B dispatch? *(G7)*

For each relationship, record the required input or output and its department owner. Leave the dependency RTO blank in this draft.

**Close**

28. Which answers need checking against another record? *(G2–G7)*
29. Anything else we should know?

### Gaps and how to resolve them

| Gap | Unresolved point | What would settle it |
|---|---|---|
| G1 | Site B org chart is an undated, unversioned HR draft. It lists three shift leaders and QA coverage from Site A; neither is treated as current evidence. | A dated, approved organisation record; dispatch lead’s corrections recorded during interview. |
| G2 | Site B dispatch boundary and product scope: **not in the sources**. | Interview answers and current activity documentation. |
| G3 | Site B impacts, supporting evidence and assessment time horizons: **not in the sources**. | Owner’s impact evidence; assessment horizons agreed through the BCM method. |
| G4 | Site B peak weeks, shift pattern, staffing, skills and mandates: **not in the sources**. | Dispatch lead’s answers, supported by current shift and demand records. |
| G5 | Site B seats, buildings and IT requirements: **not in the sources**. | Owner’s requirements and supporting current records. |
| G6 | Site B suppliers and carrier contacts: **not in the sources**. | Owner’s answers and authoritative supplier/contact records. |
| G7 | Site B departmental dependencies: **not in the sources**. | Owner’s answers, checked with the corresponding department owners. |
| G8 | The task prompt references README.md checks, but that file was unavailable at the referenced skill location. | BCM practitioner obtains and applies those checks before relying on the guide. |

**Organiser’s statements, not documentary evidence:** the interview is with Site B’s dispatch lead, who knows the shift pattern and carrier contacts; the requested outputs are resources and peak weeks. The organiser also states that the material is high-sensitivity and this environment is approved for that class. No intake answer was skipped.

The BCM practitioner checks this guide against its sources. A drafted requirement enters the register only when the activity owner confirms it. The owner sets MTPD, RTO and RPO; top management approves the BIA results.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/README.md .agents/skills/prepare-bia/units/principles.md'`
