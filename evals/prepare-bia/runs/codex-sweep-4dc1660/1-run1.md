# $prepare-bia case 1, run1: Codex, guidance at 4dc1660

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0ff33-210f-7f10-a028-2cb076a9259e`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the Site B dispatch interview guide from the three attached files. I’ll keep memory, past chats, other project files, connectors and web search off.


What data sensitivity class do the attached materials hold (for example, Public, Internal, Confidential or Strictly confidential)?

The [prepare-bia preflight](.agents/skills/prepare-bia/preflight.md) requires: “Ask the data class first.” I’ll wait for your classification before reading the attached material.


What data sensitivity class do the three attachments hold—Public, Internal, Confidential or another class?

The [skill’s preflight](.agents/skills/prepare-bia/preflight.md) requires “Ask the data class first” and prohibits reading attachments until you answer.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g '*.md' -g '"'!node_modules'"' -g '"'!vendor'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/preflight.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md .agents/skills/prepare-bia/units/prompts/bia.md .agents/skills/prepare-bia/units/keep-it-runni`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll treat the material as high sensitivity in this approved environment. Site A’s activity list and the impact criteria are approved and dated; Site B’s organisation chart is an undated draft. I’ll use the Site A details as questions to test at Site B.


Who will the Site B dispatch interview be with (role or roles)?

What do you need back from the interview?
- Completed candidate activity and resource record
- Interview notes and unresolved questions

How long will the interview run?

Before drafting, please tell me:

- Who will the interview be with?
- What do you need back from it?
- How long will it run?

The [skill’s intake](.agents/skills/prepare-bia/units/prompts/bia.md) requires “Wait for my answers.” These answers will shape the guide’s scope and timing.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md impact-criteria.md site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/stages/analysis.md .agents/skills/prepare-bia/units/workflow-design.md'`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

I’ll focus the guide on resources and peak weeks for the Site B dispatch lead. Since you left the duration open, I’ll use a provisional 30-minute schedule. The sources give no activity ranking or agreed impact time horizons, so the draft will leave those open and use dispatch as the interview focus.


**Site B dispatch interview guide — draft**

Sources and dates:

- **site-a-activity-list.md:** version 3, 12 March 2026; approved by the Site A site manager; owner: Site A BCM manager.
- **impact-criteria.md:** version 1.1, 4 February 2026; approved by top management.
- **site-b-org-chart.md:** no version or date; HR draft. Listed under Gaps and used only to frame questions.

Purpose: identify Site B dispatch resources and peak weeks. All Site B entries below are **candidate, to confirm**. Site A’s approved information retains that status for Site A; it does not establish Site B’s requirements.

Tell the activity owner: **“Use the draft as the thing to correct, not the thing to confirm; record what it could not have known.”**

### 1. Impacts over time and activity scope

| Candidate question for the activity owner | Status | Source |
|---|---|---|
| Does “Dispatch, chilled” describe your activity at Site B, and where does your responsibility start and end? | candidate, to confirm | site-a-activity-list.md, A2 |
| Are weeks 49–52 and week 14 also dispatch peak weeks at Site B? What differs? | candidate, to confirm | site-a-activity-list.md, A2 |
| Does goods receipt fall within this interview’s scope, or belong to the warehouse lead? Do its peak weeks differ from dispatch? | candidate, to confirm | site-a-activity-list.md, A1; site-b-org-chart.md, Warehouse lead |
| Is quality release a separate activity supplied by Site A, and where is the handover to Site B dispatch? | candidate, to confirm | site-a-activity-list.md, A3 and Dependencies recorded; site-b-org-chart.md, QA |

The sources do not rank activities. Cover dispatch’s impacts in full because it is the interview focus. For any additional activity brought into scope, ask only where its impacts differ.

At each **agreed assessment time horizon**, ask what a dispatch interruption would cause financially, for customers and for regulatory obligations, including during peak weeks. Ask for evidence supporting each assessment.

Use the approved criteria without assigning ratings in advance:

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | under EUR 10k a day | one customer complains | none |
| 2 | EUR 10k–100k a day | a key account is late | a report to the food authority |
| 3 | over EUR 100k a day | a key account is lost | the authority stops production |

Source: impact-criteria.md, criteria table. Assessment time horizons and the treatment of exactly EUR 100k per day are not settled by this document.

### 2. MTPD

Ask: **At what point would the evidenced consequences of interrupted dispatch become unacceptable, and what supports that point? Would peak weeks change it?**

The activity owner sets MTPD. Leave the field empty in this draft.

### 3. People

Ask about people **with the skills, authorities and mandates the work needs**.

| Candidate requirement question | Status | Source |
|---|---|---|
| Does the draft reporting structure still apply: dispatch lead with three shift leaders? | candidate, to confirm | site-b-org-chart.md, Dispatch lead |
| What shift coverage, skills, decision authority and mandates does dispatch require, including in peak weeks? | candidate, to confirm | site-b-org-chart.md, Dispatch lead; details not in the sources |
| Who can cover each required role, and does any requirement depend on one person? | candidate, to confirm | Gaps — cover and individual dependencies not in the sources |

### 4. Seats and buildings

| Candidate requirement question | Status | Source |
|---|---|---|
| What seats, workspaces and buildings does Site B dispatch require? | candidate, to confirm | Gaps — not in the sources |
| Site A records two dock doors for goods receipt. Does Site B dispatch use dock doors, and what capacity does it require during peak weeks? | candidate, to confirm | site-a-activity-list.md, A1; Site B applicability not established |

### 5. IT and applications

Cover each confirmed application **with its RTO and its RPO**, which the owner sets.

| Candidate requirement question | Status | Source |
|---|---|---|
| Site A records “LogiStock” for dispatch. Is LogiStock still the one at Site A, and does Site B dispatch use it? | candidate, to confirm | site-a-activity-list.md, A2 |
| Is the recorded manual export to Site B still possible? What information does it provide, and can Site B use it during an interruption? | candidate, to confirm | site-a-activity-list.md, A2 |
| What other IT or applications does Site B dispatch require, and what interruption or data loss could each tolerate? | candidate, to confirm | Gaps — other applications not in the sources |

### 6. Suppliers and other third parties

| Candidate requirement question | Status | Source |
|---|---|---|
| Site A records NordFrost. Is NordFrost still the one for Site A, and does it also serve Site B dispatch? | candidate, to confirm | site-a-activity-list.md, A1 and Dependencies recorded |
| Which carriers does Site B require, and what capacity is needed in peak weeks? | candidate, to confirm | Gaps — Site B carriers and capacity not in the sources |
| Is there a second carrier available to Site B, and is any requirement dependent on a single supplier? | candidate, to confirm | site-a-activity-list.md, Dependencies recorded; no second carrier recorded for Site A |

### 7. Dependencies on other departments

Record **up- and downstream relationships with other departments, each recorded with the RTO the relationship carries**. Leave those RTO fields empty here.

| Candidate relationship question | Status | Source |
|---|---|---|
| Must Site B dispatch receive quality release from Site A before dispatching? Who provides it, and what happens if it is unavailable? | candidate, to confirm | site-a-activity-list.md, Dependencies recorded and A3; site-b-org-chart.md, QA |
| Does Site B rely on Site A’s laboratory, recorded as the only laboratory in the Site A list? | candidate, to confirm | site-a-activity-list.md, A3 |
| What dispatch handovers exist with the Site B warehouse and Site A dispatch, and what must pass in each direction? | candidate, to confirm | site-b-org-chart.md, Warehouse lead; site-a-activity-list.md, A2 |
| Which other departments depend on Site B dispatch, and when do they need its outputs? | candidate, to confirm | Gaps — downstream departmental relationships not in the sources |

Any conflicting account goes **to the two owners, not to the model**.

### Traceability and recovery fields

For **every entry above**, retain its cited source, source version/date and status. Add these fields individually to the interview record; they remain empty before the interview:

| Interview reference | Interview date | Owner confirmation date | MTPD | Resource RTO | Application RPO | Dependency RTO |
|---|---|---|---|---|---|---|
| | | | | | | |

No source proposes recovery times. No AI-drafted requirement enters the register until its activity owner confirms it.

### Organiser’s take-in sheet

Provisional schedule: **30 minutes**. No direct source conflict is established; resolve possible differences between Site A’s record and Site B’s actual work first.

**Source differences and scope — 2 minutes**

Where does Site B dispatch differ from the Site A activity list?

Is the draft reporting structure still right, including QA cover from Site A?

**Impacts and peak weeks — 7 minutes**

Are weeks 49–52 and week 14 your peak weeks too?

What happens financially, to customers and to regulatory obligations as dispatch stays stopped through the agreed time horizons?

How do those consequences change during peak weeks?

Does any other activity in scope have different impacts? **Drop first if late.**

**MTPD — 3 minutes**

When do those consequences become unacceptable, and what evidence supports that point?

**People — 4 minutes**

What people, shift coverage, skills and authority do you need in normal and peak weeks?

Who can cover them, and does anything rely on just one person?

**Seats and buildings — 3 minutes**

What workspaces, buildings and dock capacity does dispatch need?

Does the goods receipt arrangement help explain your dispatch needs? **Drop first if late.**

**IT and applications — 4 minutes**

Do you use LogiStock, and is the manual export from Site A still usable?

What other applications do you need, how soon must each return, and how much data loss can you tolerate?

**Suppliers — 3 minutes**

Is NordFrost still involved, and which carriers does Site B actually use?

What carrier capacity do peak weeks require, and what alternatives are available?

**Departmental dependencies — 4 minutes**

What must QA, the warehouse and Site A dispatch provide before you can work?

Which departments need something from you, and by when?

What has this draft missed that only your team would know?

### Gaps

- **Organiser’s own statements, not sources:** interview with the Site B dispatch lead, who knows shift patterns and carrier contacts; requested output is resources and peak weeks. These shape scope but establish no resource values.
- Interview duration was omitted. **Planning assumption:** 30 minutes, with optional questions marked above.
- High sensitivity and environment approval are the organiser’s own statements.
- Site B’s organisation chart is an **undated, unversioned HR draft**. Obtain a dated, approved structure or owner corrections; do not treat it as current.
- Site B peak weeks, staffing requirements, buildings, applications, carriers and departmental relationships remain unconfirmed.
- Activity ranking and impact assessment time horizons are **not in the sources**. Obtain agreed horizons before rating impacts over time.
- Exactly EUR 100k per day is not explicitly covered by the financial bands. The criteria owner should clarify it.
- The activity owner’s personal name and the top-management approver’s name are **not in the sources**. The activity owner confirms requirements and sets MTPD, RTO and RPO; **top management approves the BIA results**.

Hand on the confirmed and unconfirmed marks intact.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. Reviewer: __________. Review date: __________.

**Tool calls (JSON events):**

- none
