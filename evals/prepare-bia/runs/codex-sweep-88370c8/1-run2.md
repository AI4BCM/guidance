# $prepare-bia case 1, run2: Codex, guidance at 88370c8

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fe6c-0cc2-7d22-ad91-5058c4060444`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the Site B dispatch interview guide. I’ll read the attached material and the skill’s preflight instructions first.

What data sensitivity class do the three attachments contain, and is this environment approved for that class? The prepare-bia preflight requires this check before I read the attachments.

What data sensitivity class do the attachments contain, and is this environment approved for that class?

The [prepare-bia preflight](.agents/skills/prepare-bia/preflight.md) requires: “Ask the data class first” and “open no file before the answer.” I’ll wait before reading the attachments.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/preflight.md .agents/skills/prepare-bia/units/prompts/bia.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll read the three attachments now, then ask only for the interview details they leave open. The guide will stay in chat, with recovery fields blank for the activity owner.

Who will be interviewed for Site B dispatch, and what do they know that you do not—for example, local activities, resources or dependencies?

What do you need back from the interview beyond this guide—for example, a corrected activity list, confirmed resource requirements, and unresolved points for follow-up?

Can you confirm that memory, past chats, other project files, connectors and web search are switched off for this task? I have read only the three attachments and the skill’s guidance.

The impact criteria are attached and approved. Site B’s org chart is an undated draft, so I’ll treat its roles as points to verify.

Before drafting, please clarify:

1. Who will be interviewed, and what do they know that you do not?
2. What should the interview return: a corrected activity list, confirmed resource requirements, unresolved points, or another outcome?
3. Are memory, past chats, other project files, connectors and web search switched off for this task?

The [prepare-bia intake](.agents/skills/prepare-bia/units/prompts/bia.md) requires me to “Wait for my answers.” Your answers will be recorded as organiser statements under Gaps, without filling recovery values.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md impact-criteria.md site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md .agents/skills/prepare-bia/units/keep-it-running.md .agents/skills/prepare-bia/units/stages/an`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

I’ll focus the guide on dispatch resources and peak weeks. Site A provides comparison questions; it does not establish Site B’s requirements. The Site B org chart remains a draft to verify, and I’ll record the unanswered channel question as a gap.

Sources:

- **site-a-activity-list.md** — version 3, 12 March 2026; approved by the Site A site manager. A2 and the recorded dependencies provide comparison questions for Site B.
- **impact-criteria.md** — version 1.1, 4 February 2026; approved by top management.
- **site-b-org-chart.md** — no version or date; HR draft. Listed under Gaps and not used as current organisational evidence.

**Site B dispatch interview guide — pre-interview draft**

Interviewee: Site B dispatch lead, as stated by the organiser. Intended output: candidate resource requirements and peak weeks, corrected by the activity owner.

Tell the owner: “Use the draft as the thing to correct, not the thing to confirm; record what it could not have known.”

Every entry below is **candidate, to confirm**. Site A information supplies questions, not findings about Site B. A requirement enters the register only when its activity owner confirms it. The owner sets MTPD, RTO and RPO; top management approves the BIA results.

**Gaps**

- **Organiser’s own statements, not sources:** the interviewee is the Site B dispatch lead; they know the shift pattern and carrier contacts; the required outputs are resources and peak weeks. These statements shape scope but supply no requirement or recovery value. Entries supported only by them have Source **Gaps**.
- **Site B organisation draft:** undated, unversioned and unapproved. Its proposed dispatch lead, three shift leaders and QA coverage from Site A require verification against a current approved chart and owner evidence.
- Site B’s activity boundaries, peak weeks, resource requirements, impacts and recovery objectives are **not in the sources**. The owner’s interview and supporting records would settle them.
- Memory, past chats and other project-file access being switched off was not confirmed. Assumption for the skipped answer: use only the three attachments as organisational evidence. Connectors and web search were not used; technical disablement of other channels is unverified, and any channel left on may influence the model without attribution.
- No explicit cross-site conflict is established by the attachments. There is no confirmed Site B register to compare with Site A.

**1. Impacts over time**

| ID | Candidate question for the activity owner | Source |
|---|---|---|
| D1 | **Candidate, to confirm:** Does Site B perform chilled dispatch comparable to Site A’s A2? What starts and ends the activity, and what belongs elsewhere? | Site A activity list, A2 |
| I1 | **Candidate, to confirm:** At successive interruption durations you identify, what financial, customer and regulatory impacts arise? What evidence supports each assessment against the attached criteria? | Impact criteria, Level table |
| P1 | **Candidate, to confirm:** Site A records weeks 49–52 and week 14 for dispatch. Which peak weeks apply at Site B, and how do resource needs and interruption impacts change then? | Site A activity list, A2 |

Use the approved criteria without assigning a Site B impact level in advance:

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | “under EUR 10k a day” | “one customer complains” | “none” |
| 2 | “EUR 10k–100k a day” | “a key account is late” | “a report to the food authority” |
| 3 | “over EUR 100k a day” | “a key account is lost” | “the authority stops production” |

Source: **impact-criteria.md**, Level table, 4 February 2026. Ask the owner to identify evidence and clarify any ambiguous threshold before relying on it.

**2. The MTPD**

| ID | Candidate question for the activity owner | Source |
|---|---|---|
| T1 | **Candidate, to confirm:** Based on the evidenced impacts over time, when does interruption become unacceptable, including during peak weeks? What supports the MTPD you set? | Impact criteria, Level table; Site A activity list, A2 |

MTPD remains empty in this draft.

**3. People, with the skills, authorities and mandates the work needs**

| ID | Candidate resource question for the activity owner | Source |
|---|---|---|
| R1 | **Candidate, to confirm:** Which roles, staffing levels, skills, authorities and mandates does dispatch require by shift and during peak weeks? What evidence supports them? Does the draft chart’s proposed three-shift-leader structure match current arrangements? | Gaps — organiser’s shift-pattern scope; unverified Site B organisation draft |

Ask which tasks each role can perform and authorise. Whether a resource depends on one person is an owner question, not a finding.

**4. Seats and buildings**

| ID | Candidate resource question for the activity owner | Source |
|---|---|---|
| R2 | **Candidate, to confirm:** Which seats, work areas and buildings does Site B dispatch require, and in what quantities during ordinary and peak weeks? | Gaps — not in the sources |

Site A’s two dock doors belong to **goods receipt, A1**; they do not establish a dispatch requirement at Site B.

**5. IT and applications, each with its RTO and its RPO**

| ID | Candidate resource question for the activity owner | Source |
|---|---|---|
| R3 | **Candidate, to confirm:** Does Site B dispatch require LogiStock, another application, or both? Which functions and data are required? Does Site A’s recorded manual export to Site B support this activity, and what does it actually provide? For each confirmed application, what RTO and RPO will you set and justify? | Site A activity list, A2 |

Do not treat the recorded export possibility as a confirmed Site B capability. Application RTO and RPO fields remain empty.

**6. Suppliers and other third parties**

| ID | Candidate resource question for the activity owner | Source |
|---|---|---|
| R4 | **Candidate, to confirm:** Which carriers and other third parties does Site B dispatch require, for what service and during which peak weeks? Does NordFrost serve Site B? What evidence identifies any alternatives? | Site A activity list, recorded dependencies; Gaps — organiser’s carrier-contact scope |

Site A records NordFrost for A1 and A2 and records no second carrier. That does not establish Site B’s carrier arrangements or prove that alternatives are unavailable.

**7. Dependencies on other departments**

| ID | Candidate relationship question for the activity owner | Source |
|---|---|---|
| R5 | **Candidate, to confirm:** Does Site B dispatch require quality release from QA before dispatch? Which department provides it, what must it deliver, and what RTO does that relationship carry? | Site A activity list, A2–A3 dependency and A3 |
| R6 | **Candidate, to confirm:** Does the recorded manual export create an upstream or downstream relationship with a department at Site A? Who provides and receives it, and what RTO does the relationship carry? | Site A activity list, A2 |
| R7 | **Candidate, to confirm:** What other upstream and downstream departmental relationships does Site B dispatch require? Who owns each relationship on both sides? | Gaps — not in the sources |

Record each relationship separately from applications and suppliers. Its RTO remains empty.

Put any disagreement to **the two activity owners**, recording both positions and evidence. Specifically compare:

- Site A’s release-before-dispatch dependency with Site B’s confirmed QA arrangement.
- Site A’s manual-export statement with Site B’s confirmed receiving capability and departmental responsibility.
- Any relationship RTO later set by each side.

Differences in peak weeks or carriers may be legitimate site differences; ask the owners to explain them before calling them conflicts.

For every entry above, retain its ID, source document and section, source version/date, and **candidate, to confirm** mark. Use this blank capture block for each entry; split resource entries by individual resource when the owner identifies them.

| Interview record/reference | Confirmation date | MTPD | RTO | RPO | Departmental relationship RTO |
|---|---|---|---|---|---|
| | | | | | |

No source proposes a recovery time, so there is no recovery-time proposal to assess. After the interview, preserve confirmed and unconfirmed marks and record what the draft could not have known. The owner confirms requirements and sets recovery objectives; top management approves the BIA results.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

**Tool calls (JSON events):**

- none
