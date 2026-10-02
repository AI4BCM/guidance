# $prepare-bia case 1, run2: Codex, guidance at cb8148b

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fcd7-63fd-7452-97e7-b924cb56ab76`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the Site B dispatch interview guide. I’ll read its preflight and the three attached files first, then ask for any missing intake details.

What data sensitivity class do the three attachments hold, and is this environment approved for that class? The prepare-bia preflight requires this answer before I open the attachments.

What sensitivity class do the attachments hold, and is this environment approved for that class?

The [prepare-bia preflight](.agents/skills/prepare-bia/preflight.md) requires: “Ask the data class first” and “open no file before the answer.” I’ve read the skill instructions but have not opened the three attachments.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g '*.md' -g '"'!node_modules'"' -g '"'!vendor'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/preflight.md .agents/skills/prepare-bia/units/prompts/bia.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Thanks. I’ll read the attachments and identify the remaining intake details needed for the guide.

Who will be interviewed for Site B dispatch, and what do they know that you, as organiser, do not?

What do you need back from the interview: a corrected activity and requirements table, a completed interview record, or another deliverable?

Are memory, past chats, other project files, connectors and web search switched off for this task? I am reading only the three attachments and the skill’s guidance; please identify any other channel left enabled.

The Site A activity list and impact criteria are approved and dated. Site B’s organisation chart is an undated draft, so I’ll flag it under Gaps and won’t treat its roles as confirmed.

Please answer the three intake questions:

1. Who is the interviewee, and what do they know that you do not?
2. What deliverable do you need back from the interview?
3. Are memory, past chats, other project files, connectors and web search switched off? Identify any left enabled.

The [prepare-bia intake](.agents/skills/prepare-bia/units/prompts/bia.md) explicitly requires “Wait for my answers” before drafting.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md impact-criteria.md site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md .agents/skills/prepare-bia/units/keep-it-running.md .agents/skills/prepare-bia/units/stages/an`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

I’ll focus the guide on resources and peak weeks for the Site B dispatch lead. Site A provides comparison points, but Site B’s shift pattern, carrier contacts and resource requirements still need owner confirmation. I’ll keep all recovery fields blank and record the unanswered channel-isolation question as a gap.

Site B dispatch interview guide — pre-interview draft, 2 October 2026

Sources:

- **[A] site-a-activity-list.md**, version 3, 12 March 2026; approved by the site manager. References below use activity IDs and “Dependencies recorded.”
- **[I] impact-criteria.md**, version 1.1, 4 February 2026; approved by top management. References below use impact levels.
- **[B] site-b-org-chart.md**, no version or date; draft from HR. Used only to frame questions under Gaps, not as a current organisational record.

Interviewee: Site B dispatch lead. Intended output: corrected resource requirements and peak weeks.

Use the draft as the thing to correct, not the thing to confirm; record what it could not have known. Every entry below is **candidate, to confirm**. A requirement enters the register only when its activity owner confirms it.

| Candidate activity | People and mandates | Seats and buildings | IT and applications | Suppliers | Department dependencies |
|---|---|---|---|---|---|
| Does Site B perform chilled dispatch, and what does the activity include? [A, A2] | Which roles, skills and decision authorities does it need? **Not in the approved sources for Site B.** | Which seats and buildings does it require? **Not in the sources for dispatch.** | Does Site B use LogiStock or receive Site A’s manual export? [A, A2] | Does it depend on NordFrost, another carrier, or several carriers? [A, Dependencies recorded] | Does dispatch depend on QA release, and what relationship exists with Site A? [A, A2–A3 and Dependencies recorded; B, draft QA statement] |

The following fields apply to every candidate entry and remain empty in this draft:

| Entry | Interview reference | Confirmation date | MTPD | RTO | RPO |
|---|---|---|---|---|---|
| Dispatch activity and peak weeks | | | | | |
| People and mandates | | | | | |
| Seats and buildings | | | | | |
| IT and applications | | | | | |
| Suppliers and third parties | | | | | |
| Department dependencies | | | | | |

**1. Impacts over time**

- What happens as Site B dispatch remains unavailable? For each elapsed period the owner identifies, describe financial, customer and regulatory consequences and the evidence supporting them.
- Where would those consequences fall against the approved criteria below? Do not infer a rating from Site A’s activity list.

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | “under EUR 10k a day” | “one customer complains” | “none” |
| 2 | “EUR 10k–100k a day” | “a key account is late” | “a report to the food authority” |
| 3 | “over EUR 100k a day” | “a key account is lost” | “the authority stops production” |

Source: [I, levels 1–3].

- Are Site B’s dispatch peaks also weeks 49–52 and week 14, as recorded for Site A? Which weeks differ, and why? [A, A2]
- How do those peaks change dispatch impacts and the resources needed? **Site B values: not in the sources.**

**2. The MTPD**

- At what point would the impacts become unacceptable, using the approved criteria? What evidence supports that point?
- Does the point change during peak weeks?

The activity owner sets the MTPD. Its field stays blank in this draft.

**3. People, skills, authorities and mandates**

- Does the draft HR chart’s dispatch lead and three shift leaders reflect the current structure? Obtain a dated, approved chart or owner correction. [B, Dispatch lead bullet; draft]
- What is the actual shift pattern, including peak weeks? Which roles and skills are required on each shift? **Not in the approved sources.**
- Who has the authority and mandate to make dispatch decisions and arrange carrier movements? What cover exists when those people are unavailable? **Not in the sources.**

Record owner-confirmed roles, skills, mandates and staffing needs separately for normal and peak periods.

**4. Seats and buildings**

- Which seats, buildings and dispatch areas does Site B need, and how does demand change in peak weeks? **Not in the sources.**
- Site A records two dock doors for chilled goods receipt. Are any receipt facilities also dependencies of Site B dispatch? Do not carry that quantity into Site B’s requirements. [A, A1]

**5. IT and applications, each with its RTO and RPO**

- Is LogiStock required for Site B dispatch, or does Site B use another application? What work and information does each application support? [A, A2; Site B application requirements not in the sources]
- What does Site A’s stated manual export to Site B enable? Who produces, receives and uses it, and what limitations does it have? [A, A2]
- What availability and data-loss needs should the owner establish for each confirmed application, including during peak weeks?

Application RTO and RPO fields stay blank. The owner sets them; the export statement does not establish a recovery time.

**6. Suppliers and other third parties**

- Which carriers does Site B actually use? Is NordFrost among them? [A, Dependencies recorded]
- Who holds the current carrier contacts, and which dispatch arrangements do those contacts support? **Site B contacts: not in the sources.**
- Site A records no second carrier. Does Site B have alternatives, and what capacity is available during peak weeks? [A, Dependencies recorded]

A single carrier or named contact is a question for the owner, not a finding of sole dependence.

**7. Dependencies on other departments**

- Does Site B dispatch require QA release before dispatch? Who provides it, and what must pass between the departments? [A, A2–A3 and Dependencies recorded]
- Is QA currently covered from Site A, as the draft chart suggests? Does the Site A-only lab affect that relationship? [B, QA bullet; draft. A, A3]
- What department relationship supports the manual export from Site A to Site B? [A, A2]
- Which other upstream or downstream departments depend on dispatch, or supply something dispatch needs? **Not in the sources.**

For each confirmed relationship, record both department owners, the required input or output, peak-week implications and a separate dependency RTO field. Leave that field blank here.

**Gaps and matters to settle**

- **Organiser’s own statements, not sources:** the interviewee is the Site B dispatch lead; they know the shift pattern and carrier contacts. The requested output is resources and peak weeks. These statements shape the interview but establish no requirement or value.
- **Environment statement:** the organiser classified the material as high sensitivity and stated that this environment is approved for high sensitivity.
- **Unanswered isolation question:** channel settings were not confirmed. Working assumption: only the three attachments provide organisational evidence. No connectors, web search or other project files were used. Memory and past-chat isolation cannot be verified; any enabled channel remains a gap because the model may draw on it without saying so.
- **Site B chart:** undated, unversioned HR draft; obtain a current approved source or record the owner’s corrections.
- **Site B resources, impacts, peak weeks and recovery needs:** not settled by the attachments; obtain the dispatch lead’s evidence and confirmations.
- **Cross-site conflicts:** none can be established from these attachments. Differences in peak weeks, applications, carriers, QA coverage or export arrangements must be put to the Site A and Site B owners, not resolved by the model.
- **Source-proposed recovery times:** none are present.

The activity owner confirms each requirement and sets MTPD, RTO and RPO. Top management approves the BIA results. Retain confirmed and unconfirmed marks, source dates, interview references and confirmation dates when handing the interview record onward.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

**Tool calls (JSON events):**

- none
