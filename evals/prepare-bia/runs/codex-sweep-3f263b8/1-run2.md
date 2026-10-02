# $prepare-bia case 1, run2: Codex, guidance at 3f263b8

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fe5a-62d5-72b3-aae8-ea7ccb516016`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the Site B dispatch interview guide from the three attached files. I’ll read its preflight instructions and source material first.

What data classification do the attached materials hold, and is this environment approved for that class?

What data classification do the attached materials hold, and is this environment approved for that class?

The skill’s [preflight.md](.agents/skills/prepare-bia/preflight.md) requires: “Ask the data class first” and “open no file before the answer.” I’ve read the skill instructions; the three attached documents remain unopened.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/preflight.md .agents/skills/prepare-bia/units/prompts/bia.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll use your confirmation that this environment is approved for high-classification data and read the three attachments now.

Who will be interviewed (role), and what Site B dispatch knowledge do they have that you do not?

What do you need back from the interview beyond this guide—for example, a corrected activity list, requirements for owner confirmation, or a recorded impact assessment?

Can you confirm that memory, past chats, other project files, connectors and web search are switched off for this task? I will use only the three attachments and the skill’s instructions; flag any channel left on.

The skill’s [Intake](.agents/skills/prepare-bia/units/prompts/bia.md) requires “Wait for my answers” before drafting. Please answer the three intake questions above.

The Site B organisation chart is an undated, unversioned HR draft. I’ll flag it under Gaps and use it only to frame questions, not as current evidence of Site B’s requirements.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md impact-criteria.md site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md .agents/skills/prepare-bia/units/keep-it-running.md'`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

I’ll focus the guide on resources and peak weeks for the Site B dispatch lead. The Site A list provides comparison questions, but it does not establish Site B’s requirements. I’ll record your answers as organiser statements, flag the unanswered channel-setting question under Gaps, and leave all recovery fields blank.

Source documents:
- **[A] site-a-activity-list.md** — version 3, 12 March 2026; approved by the Site A site manager. Sections: activity table, A2–A3; Dependencies recorded.
- **[I] impact-criteria.md** — version 1.1, 4 February 2026; approved by top management. Section: impact-level table.
- **[B] site-b-org-chart.md** — no version or date; HR draft. Listed under Gaps; not used as current evidence.

**Site B dispatch interview guide — pre-interview draft**

Interview scope: resources and peak weeks. Each entry below is **candidate, to confirm**. A resource requirement drafted by AI is only a question for the activity owner; it enters the register only after owner confirmation.

Tell the owner: **“Use the draft as the thing to correct, not the thing to confirm; record what it could not have known.”**

### 1. Impacts over time

| ID | Candidate activity or impact question | Evidence | Status |
|---|---|---|---|
| C1 | Does Site B perform chilled dispatch? What does the activity include, and where does its responsibility start and end? | [A], A2 describes Site A only; Site B activity scope is not in the sources. | candidate, to confirm |
| C2 | Which weeks are peaks at Site B? Do Site A’s weeks 49–52 and week 14 apply, or does Site B differ? What resources change during peaks? | [A], A2 | candidate, to confirm |
| C3 | As dispatch remains interrupted, when would each financial, customer or regulatory impact level be reached? Record the evidence and distinguish normal from peak weeks. | [I], impact-level table | candidate, to confirm |

Apply the attached criteria without assigning Site B an impact level in advance:

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | under EUR 10k a day | one customer complains | none |
| 2 | EUR 10k–100k a day | a key account is late | a report to the food authority |
| 3 | over EUR 100k a day | a key account is lost | the authority stops production |

Source: [I], impact-level table; wording reproduced exactly.

### 2. The MTPD

**Candidate, to confirm:** Based on the impacts established in section 1, when would disruption become unacceptable, and why? Does the conclusion differ during peak weeks? The activity owner sets MTPD.

| Candidate activity | MTPD | Interview | Confirmation date |
|---|---|---|---|
| C1 — Site B chilled dispatch, subject to correction | | | |

Basis: [A], A2; [I], impact-level table. Site B’s MTPD is **not in the sources**.

### 3. People

| ID | Candidate resource question | Evidence / gap | Status |
|---|---|---|---|
| P1 | Who performs Site B dispatch, with the skills, authorities and mandates the work needs? Who may make dispatch decisions and authorise exceptions? | Site B requirements are not in the current sources. [B], organisation structure, is a draft only. | candidate, to confirm |
| P2 | Is the draft’s dispatch lead and three-shift-leader structure accurate? What staffing is needed for each shift and during confirmed peak weeks? | [B], organisation structure; draft, undated. Shift pattern and staffing requirements are not in the sources. | candidate, to confirm |
| P3 | Which people hold the necessary carrier contacts and authority to use them? Is any required knowledge or mandate held by only one person? | Not in the sources; establish with the activity owner. | candidate, to confirm |

### 4. Seats and buildings

| ID | Candidate resource question | Evidence / gap | Status |
|---|---|---|---|
| S1 | Which seats, workspaces and buildings does Site B dispatch require, and in what quantities during normal and peak weeks? | Not in the sources. Site A’s two dock doors belong to goods receipt, A1; they do not establish a dispatch requirement for Site B. | candidate, to confirm |

### 5. IT and applications

| ID | Candidate resource question | Evidence | Status | RTO | RPO |
|---|---|---|---|---|---|
| T1 | Does Site B dispatch require LogiStock? If so, for which work and data? | [A], A2 records its use at Site A only. | candidate, to confirm | | |
| T2 | What does the recorded manual export to Site B support? What systems or applications must Site B have to receive and use it? | [A], A2; receiving requirements are not in the sources. | candidate, to confirm | | |

Have the owner identify each required application and its RTO and RPO during the interview. No recovery times are proposed in the attached sources.

### 6. Suppliers and other third parties

| ID | Candidate resource question | Evidence / gap | Status |
|---|---|---|---|
| V1 | Does Site B dispatch depend on NordFrost? Which carriers and other third parties are required, for what services and during which peaks? | [A], Dependencies recorded, identifies NordFrost for Site A’s A1 and A2 only. Site B requirements are not in the sources. | candidate, to confirm |
| V2 | For each confirmed service, what contacts and alternatives exist? Is a single carrier behind any requirement? | [A] records no second carrier for Site A; that does not establish Site B’s carrier position. | candidate, to confirm |

### 7. Dependencies

Record up- and downstream relationships with other departments separately, each with the RTO the relationship carries.

| ID | Candidate dependency question | Evidence / gap | Status | Relationship RTO |
|---|---|---|---|---|
| D1 | Does Site B dispatch depend on quality release from Site A? What release information and authority must be available before dispatch? | [A], A3 and Dependencies recorded; [B] suggests Site A QA coverage but is an undated draft. | candidate, to confirm | |
| D2 | Does Site B depend on a manual export from Site A dispatch? What is handed over, by whom, and for which activity? | [A], A2 | candidate, to confirm | |
| D3 | What other upstream inputs and downstream departmental handovers does Site B dispatch require? | Not in the sources. | candidate, to confirm | |

**Gaps and cross-site comparison**

- **Organiser’s own statements, not sources:** interviewee is the Site B dispatch lead; they know the shift pattern and carrier contacts. Requested interview outputs are resources and peak weeks. These statements shape scope but supply no register values.
- **Channel settings:** the third intake question was unanswered. Working assumption: evidence is restricted to the three attachments. Memory, past-chat and channel settings were not verified; this conversation remains available, and the model may draw on it without saying so. No connectors, web search or other project content were used.
- **[B]:** undated, unversioned HR draft. Obtain a dated, approved organisation chart and owner correction before treating its structure as current.
- Site B activities, peak weeks, staffing, premises, applications, carriers and departmental relationships remain unsettled. The activity owner’s interview and confirmation would settle them.
- No confirmed cross-site conflict can be established from these attachments. Compare peak weeks, application/export arrangements, carrier reliance and QA release responsibilities. Put every difference or conflict **to the two owners, not to the model**.

For every candidate ID, retain its cited source and source date above, plus these blank fields:

| Entry ID | Interview | Confirmation date | MTPD | RTO | RPO |
|---|---|---|---|---|---|
| | | | | | |

The activity owner confirms each requirement and sets MTPD and RTO; owners set RPO. **Top management approves the BIA results.** Preserve confirmed and unconfirmed marks when handing on the interview record.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. Reviewer: ______. Review date: ______.

**Tool calls (JSON events):**

- none
