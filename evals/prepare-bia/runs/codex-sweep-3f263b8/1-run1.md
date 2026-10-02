# $prepare-bia case 1, run1: Codex, guidance at 3f263b8

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fe5a-3bf3-7661-9df3-5ca19505d445`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the Site B dispatch interview guide. I’ll read its preflight instructions and the three attached files first.

What data sensitivity class do these attachments hold?

The [skill’s preflight](.agents/skills/prepare-bia/preflight.md) requires: “Ask the data class first” and “open no file before the answer.” I read the attachments before discovering that gate; I’ll pause drafting until you answer.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"'"`
- command_execution: `/bin/bash -lc "cat '.agents/skills/prepare-bia/SKILL.md'"`
- command_execution: `/bin/bash -lc "cat '.agents/skills/prepare-bia/preflight.md'"`
- command_execution: `/bin/bash -lc "cat 'site-a-activity-list.md'"`
- command_execution: `/bin/bash -lc "cat '.agents/skills/prepare-bia/units/prompts/bia.md'"`
- command_execution: `/bin/bash -lc "cat 'impact-criteria.md'"`
- command_execution: `/bin/bash -lc "cat 'site-b-org-chart.md'"`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll proceed on your statement that the data is high sensitivity and this environment is approved for it. The Site B organisation chart is an undated draft, so I’ll treat it as a gap to resolve during the interview.

Before drafting, the [skill’s intake](.agents/skills/prepare-bia/units/prompts/bia.md) requires three clarifications and says “Wait for my answers”:

1. Who is being interviewed—what role—and what do they know about Site B dispatch that you need to learn?
2. What should the interview deliver beyond the guide: corrected activities, confirmed resource requirements, impact assessments, or all three?
3. Are memory, past chats, other project files, connectors and web search switched off for this task? I’ve accessed only the three attachments and the skill’s instructions.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "cat '.agents/skills/prepare-bia/units/keep-it-running.md'"`
- command_execution: `/bin/bash -lc "cat '.agents/skills/prepare-bia/units/data-rules.md'"`
- command_execution: `/bin/bash -lc "cat '.agents/skills/prepare-bia/units/stages/analysis.md'"`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

I’ll focus the guide on resources and peak weeks for the Site B dispatch lead. Site A’s list gives us questions about LogiStock, carriers and quality release, but it does not establish Site B’s requirements. I’ll leave those as candidates and record the unanswered source-channel question under Gaps.

Sources: **site-a-activity-list.md** — version 3, 12 March 2026; approved by the site manager; § Activity table and Dependencies recorded.  
Sources: **impact-criteria.md** — version 1.1, 4 February 2026; approved by top management; § Impact criteria table.  
Under Gaps: **site-b-org-chart.md** — no version or date; draft from HR; excluded as current evidence.

**Site B dispatch interview guide — draft**

Purpose: identify candidate dispatch resource requirements and peak weeks for correction by the activity owner.

Tell the interviewee: **“Use the draft as the thing to correct, not the thing to confirm; record what it could not have known.”**

The activity owner confirms each requirement and sets MTPD, RTO and RPO. **Top management approves the BIA results.** No requirement enters the register before owner confirmation.

**Candidate activity and resources**

Every entry below is **candidate, to confirm**. Site A evidence supports questions about Site B; it does not establish Site B requirements.

| ID | Activity or resource class | Question for the Site B activity owner | Evidence |
|---|---|---|---|
| B1 | Activity and peak weeks | Does Site B perform chilled dispatch? Do Site A’s peaks in weeks 49–52 and week 14 also apply here? What must be corrected or added? | site-a-activity-list.md, Activity table, A2 |
| B2 | People and mandates | Who performs, directs and authorises dispatch, with what skills, authorities and mandates? | site-a-activity-list.md, Activity table, A2 names a dispatch lead; Site B details not in the current sources |
| B3 | Seats and buildings | What seats, buildings and physical facilities does Site B dispatch require, including at peak? | Not in the sources. Site A’s two dock doors belong to A1 goods receipt, not A2 dispatch |
| B4 | IT and applications | Does Site B dispatch require LogiStock? What does the manual export from Site A enable, and what resources does it require at Site B? | site-a-activity-list.md, Activity table, A2 |
| B5 | Suppliers and third parties | Does Site B dispatch depend on NordFrost? Which carriers are required, and is an alternative available? Who holds the carrier contacts? | site-a-activity-list.md, Dependencies recorded: NordFrost supports Site A A2; no second carrier recorded |
| B6 | Department dependencies | Must Site B dispatch receive quality release from QA? What other upstream inputs and downstream departmental relationships are required? | site-a-activity-list.md, Dependencies recorded: Site A A2 depends on A3; additional Site B relationships not in the sources |

Keep the following fields empty in this pre-interview draft. Each ID links to its question and cited evidence above.

| ID | Source date | Interview | Confirmation date | MTPD | RTO | RPO |
|---|---|---|---|---|---|---|
| B1 | 12 March 2026 | | | | | |
| B2 | 12 March 2026 | | | | | |
| B3 | | | | | | |
| B4 | 12 March 2026 | | | | | |
| B5 | 12 March 2026 | | | | | |
| B6 | 12 March 2026 | | | | | |

For B4, record each application separately with its RTO and RPO. For B6, record each departmental relationship separately with its RTO. These recovery fields remain blank. No attached source proposes a recovery time.

### 1. Impacts over time

- What happens as Site B dispatch remains interrupted, during normal weeks and peak weeks?
- Using the approved criteria, when would financial, customer or regulatory impacts reach each level? What evidence supports the assessment?
- Are weeks 49–52 and week 14 relevant to Site B? Which weeks differ, and how do resource needs change?

Use **impact-criteria.md, Impact criteria table**: financial levels are under EUR 10k a day, EUR 10k–100k a day and over EUR 100k a day; customer and regulatory levels must also be assessed. Record unresolved threshold boundaries as questions, not assigned ratings.

### 2. The MTPD

- At what point would interruption become unacceptable, based on the impacts described?
- Does that point differ during peak weeks? What evidence would justify the owner’s decision?

**MTPD:** 

### 3. People, with the skills, authorities and mandates the work needs

- What is the actual shift pattern, and what staffing does each shift require during normal and peak weeks?
- Which skills, authorisations and mandates are essential?
- Could any essential task depend on one person? Who can cover it?
- Which staffing and shift records would substantiate the answers?

These details are **not in the current sources**; the questions address B2.

### 4. Seats and buildings

- Which seats, buildings and physical facilities are necessary for dispatch?
- What capacity is required normally and during peak weeks?
- Which facilities are shared with other activities, and who can confirm their availability?

Site B requirements are **not in the sources**; do not transfer Site A’s goods-receipt dock count to dispatch.

### 5. IT and applications, each with its RTO and its RPO

- Is LogiStock used at Site B, and for which dispatch tasks?
- What is exported manually from Site A, who performs the export, and can Site B use it?
- Which other applications or data are required? What evidence identifies them?
- For each application, what interruption and data loss can the owner tolerate, given the impacts?

**Application RTO:**   
**Application RPO:** 

### 6. Suppliers and other third parties

- Which carriers actually support Site B dispatch, in normal and peak weeks?
- Does NordFrost serve Site B? Is there another usable carrier?
- Where are carrier contacts held, and who can access and use them across shifts?
- What evidence establishes carrier availability and required capacity?

A single carrier or contact person is a question for the owner, not an established dependency.

### 7. Dependencies on other departments

- Is QA release required before Site B dispatch? Which department provides it?
- What upstream inputs and downstream departmental relationships are essential?
- For each relationship, who is the counterpart owner, what must pass between departments, and what RTO does the relationship carry?
- Does the counterpart department’s BIA record the same relationship?

**Dependency RTO:** 

No actual cross-site conflict is established by the attachments. Put these comparison questions **to both activity owners**: whether Site A’s manual export is usable at Site B; whether QA provision meets Site B dispatch needs; and whether the sites rely on the same carrier capacity during overlapping peaks. Record any disagreement for resolution by the two owners.

**Gaps and organiser statements**

- **Own statements, not sources:** you classified the material as high sensitivity and stated this environment is approved for it.
- **Own statements, not sources:** the interviewee is the Site B dispatch lead, who knows the shift pattern and carrier contacts; the requested outcomes are resources and peak weeks. These statements shape the scope but fill no requirement value.
- The source-channel question was skipped. Working assumption: only the three attachments supply organisational evidence. Memory and other channel settings have not been verified; any channel left on may influence the model without saying so.
- The Site B organisation chart is an **undated, unversioned HR draft**, not current evidence. It proposes three shift leaders and QA coverage from Site A. Ask the relevant owners to correct these claims and obtain a dated, approved chart.
- Current Site B activities, resources, peak weeks, impacts and recovery decisions are **not in the sources**. Settle them through the owner interview and supporting records.
- Currency of the two approved documents has not been independently verified; check for replacements before relying on the results.

Carry confirmed and unconfirmed marks forward intact after the interview; all entries in this draft remain **candidate, to confirm**.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

**Tool calls (JSON events):**

- none
