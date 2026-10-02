# $prepare-bia case 1, run2: Codex, guidance at 5ec8f40

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0feb8-f191-78e3-bc06-ea43af65357d`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the Site B dispatch interview guide. I’ll read its preflight instructions and the three attached files, then gather the organiser details the skill requires.


What data classification applies to the three attached documents?
- Public
- Internal
- Confidential
- Restricted

The [preflight instructions](.agents/skills/prepare-bia/preflight.md) require: “Ask the data class first” and “open no file before the answer.” I’ve read the skill instructions but have not opened the three attached documents; I’ll wait for their classification.


What data classification applies to the attachments: Public, Internal, Confidential, or Restricted?

The skill’s [preflight instructions](.agents/skills/prepare-bia/preflight.md) require “Ask the data class first” before opening the documents.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/preflight.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll treat the material as High, using your statement that this environment is approved for it. I’ll now read the attachments and the remaining skill guidance.


What is the interviewee’s role, and what do they know about Site B dispatch that you, as organiser, do not?

Besides the interview guide, what do you need back from the interview, and how long is the interview?

Please confirm that this draft should use only the three attachments and the skill guidance, with memory, past chats, other project files, connectors and web search excluded.
- Yes, exclude all other sources
- No, another source channel is needed

The Site A list and impact criteria are dated and approved. The Site B organisation chart is an undated, unversioned draft, so it can prompt questions but cannot establish current requirements. The attachments provide neither an activity ranking nor agreed impact time horizons.

The [BIA intake instructions](.agents/skills/prepare-bia/units/prompts/bia.md) say “Wait for my answers.” I’ll hold the draft until you answer the three intake questions.


Before I draft, please provide:

1. The interviewee’s role and what they know about Site B dispatch that you do not.
2. The interview length and what you need back from it.
3. Confirmation that only the three attachments and skill guidance may be used, excluding memory, past chats, other project files, connectors and web search.

The skill’s [intake instructions](.agents/skills/prepare-bia/units/prompts/bia.md) require “Wait for my answers.” The undated Site B chart will be treated as a gap, not current evidence.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md impact-criteria.md site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/prompts/bia.md .agents/skills/prepare-bia/units/data-rules.md .agents/skills/prepare-bia/units/keep-it-runni`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/stages/analysis.md .agents/skills/prepare-bia/units/workflow-design.md .agents/skills/prepare-bia/units/prom`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

I’ll focus the draft on dispatch resources and peak weeks. I’ll record your interviewee details as “own statements, not sources” under Gaps.

You left the source-channel question and interview length unanswered. I’ll assume only the attachments and skill guidance may be used, and keep the take-in sheet compact without assigning a duration. All requirements will remain candidates, with recovery fields blank.


**Draft: Site B dispatch interview guide — candidate, to confirm**

Sources:

- **site-a-activity-list.md** — version 3, 12 March 2026; approved by the Site A manager. References below identify activity rows or the dependency paragraph.
- **impact-criteria.md** — version 1.1, 4 February 2026; approved by top management. References below identify the impact category.
- **site-b-org-chart.md** — no version or date; HR draft. Listed under Gaps and used only to frame questions.

Use the draft as the thing to correct, not the thing to confirm; record what it could not have known. Site A evidence supports questions about Site B, not findings about Site B.

**Candidate activity scope**

| Question for the activity owner | Source | Status |
|---|---|---|
| Does chilled dispatch describe the activity at Site B, and where does its responsibility begin and end? | Site A activity list, A2 | candidate, to confirm |
| Does chilled goods receipt fall within this interview, or should its owner answer separately? | Site A activity list, A1 | candidate, to confirm |
| Is quality release a separate activity supplying dispatch, and who owns that relationship? | Site A activity list, A3 and dependency paragraph | candidate, to confirm |
| Does payroll have any relationship to dispatch that needs recording, or is it outside this interview? | Site A activity list, A4 | candidate, to confirm |

**1. Impacts over time**

The sources do not rank activities. Cover dispatch in full because it is the requested scope; do not describe it as the highest-ranked activity. For any other activity brought into scope, ask only where its impacts differ.

- Which agreed interruption time horizons should we use? **Source: Gaps — not in the sources.**
- At each agreed horizon, what financial, customer and regulatory consequences would interrupted dispatch cause, and what evidence supports them? **Source: Impact criteria, all three categories.**
- Which approved level fits each consequence? The financial bands are under EUR 10k a day, EUR 10k–100k a day, and over EUR 100k a day; customer consequences range from a complaint to losing a key account; regulatory consequences range from none to production being stopped. **Source: Impact criteria, levels 1–3.**
- Site A records dispatch peaks in “weeks 49–52, week 14”; which weeks are peaks at Site B, and how do impacts change then? **Source: Site A activity list, A2.**
- If receipt, quality release or payroll enters scope, where do its impacts or peak periods differ from dispatch? **Source: Site A activity list, A1, A3 and A4.**

Every impact assessment remains **candidate, to confirm**. No impact ratings have been assigned.

**2. The MTPD**

- At what point would dispatch interruption become unacceptable, based on the impacts you have described?
- Does that point change during peak weeks, and what evidence explains the change?

**Source: Gaps — Site B tolerances are not in the sources. Status: candidate, to confirm.**

The activity owner sets MTPD. Its field remains empty.

**3. People, with the skills, authorities and mandates the work needs**

| Question for the activity owner | Source | Status |
|---|---|---|
| Who owns dispatch at Site B, and which decisions are they authorised to make? | Gaps; Site A activity list, A2, provides a comparison role only | candidate, to confirm |
| Does the draft organisation chart’s reference to three shift leaders reflect the current arrangement? | Gaps — undated Site B organisation chart | candidate, to confirm |
| What shift pattern operates normally and during peak weeks, and what staffing, skills, authorities and mandates does each shift need? | Gaps — not in the approved sources | candidate, to confirm |
| Is any required skill, authority or mandate held by only one person, and what cover actually exists? | Gaps — not in the sources | candidate, to confirm |

**4. Seats and buildings**

- Which seats, work areas and buildings does dispatch need, and what capacity is required normally and during peak weeks?
- Which of these requirements can you support with current site evidence?

**Source: Gaps — Site B seats and buildings are not in the sources. Status: candidate, to confirm.**

Site A’s two dock doors are recorded for goods receipt, not as a Site B dispatch requirement.

**5. IT and applications, each with its RTO and its RPO**

| Question for the activity owner | Source | Status |
|---|---|---|
| Does Site B dispatch use LogiStock, and what work and information depend on it? | Site A activity list, A2 | candidate, to confirm |
| What does Site A’s recorded manual export to Site B provide, and can Site B actually use it? | Site A activity list, A2 | candidate, to confirm |
| Which applications and information does Site B dispatch require, including any absent from the Site A list? | Gaps — Site B application requirements are not in the sources | candidate, to confirm |
| For each confirmed application, what RTO and RPO will the owner set, based on the impacts and acceptable information loss? | Gaps — recovery objectives are not in the sources | candidate, to confirm |

RTO and RPO fields remain empty.

**6. Suppliers and other third parties**

- Does Site B dispatch depend on NordFrost, another carrier, or several carriers?
- Which services are required, who holds the current carrier contacts, and what evidence supports the arrangements?
- Is any required service provided by only one supplier or carrier, and what alternative has the owner verified?
- How do carrier requirements change during Site B’s peak weeks?

**Source: Site A activity list, A2 and dependency paragraph, for the NordFrost comparison; Gaps for Site B arrangements and contacts. Status: candidate, to confirm.**

The absence of a second carrier in Site A’s list is not proof that Site B has a single carrier.

**7. Dependencies: up- and downstream relationships with other departments**

| Question for the activity owner | Source | Status |
|---|---|---|
| Must Site B dispatch receive quality release before dispatch, and which department supplies it? | Site A activity list, A2–A3 and dependency paragraph | candidate, to confirm |
| Is QA coverage from Site A current, and how does the Site A laboratory support Site B dispatch? | Gaps — Site B chart is a draft; Site A activity list, A3 | candidate, to confirm |
| What other departments supply inputs to dispatch or receive its outputs? | Gaps — Site B departmental relationships are not in the sources | candidate, to confirm |
| For each relationship, what output is exchanged, who owns each end, and what RTO will the owners record consistently in both departmental BIAs? | Gaps — relationship recovery objectives are not in the sources | candidate, to confirm |

Dependency RTO fields remain empty. Carrier services belong in the supplier section.

**Traceability and recovery fields**

This is a question register, not a confirmed requirements register. Each entry above carries its source and remains **candidate, to confirm**. Source dates are listed at the top; entries supported only by organiser statements or missing evidence have Source **Gaps**.

The following fields remain empty for every candidate:

| Interview reference | Confirmation date | MTPD | RTO | RPO | Dependency RTO |
|---|---|---|---|---|---|
| | | | | | |

A requirement enters the requirements register only after the activity owner confirms it. The activity owner sets MTPD, RTO and RPO; **top management approves the BIA results**. Preserve confirmed and unconfirmed marks during handover.

**Gaps and points requiring resolution**

- **Own statements, not sources:** you identified the interviewee as the Site B dispatch lead, said they know the shift pattern and carrier contacts, and requested resources and peak weeks. These statements shape the interview but fill no requirement values.
- **Own statement, not a source:** you classified the material as High and stated that this environment is approved for High.
- The source-channel question was unanswered. Working assumption: exclude memory, past chats, other project files, connectors and web search. Only attachments and shipped skill guidance were used.
- Interview duration is **not in the sources** and was not supplied. The take-in sheet below is compact and has no assumed duration.
- The Site B chart is an undated, unversioned HR draft. Obtain a dated, approved replacement before relying on its roles, shift-leader count or QA arrangement.
- Activity ranking, agreed impact time horizons, Site B resource quantities and recovery objectives are **not in the sources**. Obtain the agreed method parameters and owner evidence.
- No verified cross-site conflict can be established from these attachments. Site A’s laboratory location and the draft’s QA coverage statement may be compatible. Any disagreement found over release, manual export, carriers or peaks must go **to the two owners, not to the model**.
- The criteria do not specify how to treat financial amounts exactly at EUR 10k and EUR 100k; ask the criteria owner to clarify the boundaries.

**Organiser’s take-in sheet**

Does Site A’s description of quality release and manual export match how Site B actually works, or do the two owners need to resolve a difference?

What needs correcting in the draft organisation chart?

Where does your dispatch responsibility begin and end?

Which weeks are busiest at Site B, and what changes during those weeks?

Using the agreed time horizons, what financial, customer and regulatory impacts would interrupted dispatch cause?

When would that interruption become unacceptable, and why?

What people, shift coverage, skills and decision-making authority does dispatch need?

What seats, work areas and buildings does dispatch need?

Which applications and information does dispatch need, and what recovery time and information loss can the owner accept for each?

Which carriers and other suppliers are required, who holds their contacts, and does any service depend on just one provider?

Which departments provide inputs or receive outputs, and what recovery time must each relationship carry?

What has this draft missed, and what evidence or follow-up is needed?

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

**Tool calls (JSON events):**

- none
