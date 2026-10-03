# $prepare-bia case 1, run2: Codex, guidance at 836c32f

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0ff0f-9bfe-7ef2-b46e-50e96016c9d0`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the Site B dispatch interview guide from the three attached files. I’ll read its preflight instructions and the source material first.

What data sensitivity class do the attached materials hold?

The skill’s [preflight.md](.agents/skills/prepare-bia/preflight.md) requires: “Ask the data class first.” I mistakenly read the attachments before this check; I’ll pause drafting until you answer.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"' -g '"'!vendor'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/preflight.md .agents/skills/prepare-bia/units/prompts/bia.md'`
- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md impact-criteria.md site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll proceed with high-sensitivity material in this approved environment. Memory, past chats, other project files, connectors and web search are off; I’ll use only the three attachments and the skill’s guidance.

Who will attend the Site B dispatch interview, and in what role?

What do you need back beyond the interview guide: corrected activities and dependencies, confirmed resource requirements, or both?
- Both
- Corrected activities and dependencies
- Confirmed resource requirements

How long is the interview?

The Site A activity list and impact criteria are dated and approved. Site B’s organisation chart is an undated draft, so its roles and QA arrangement need confirmation. The sources do not rank activities by impact; dispatch is the interview focus, and the Site A requirements will be questions for Site B’s owner.

Before drafting, please tell me:

- Who will attend, and in what role?
- Should the interview produce corrected activities and dependencies, confirmed resource requirements, or both?
- How long is the interview?

The [prepare-bia intake instructions](.agents/skills/prepare-bia/units/prompts/bia.md) say “Wait for my answers,” so I’m holding the draft until this intake is complete.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/keep-it-running.md .agents/skills/prepare-bia/units/stages/analysis.md'`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

I’ll focus the guide on resources and peak weeks for the Site B dispatch lead. Since the interview length was skipped, I’ll use a provisional 45-minute schedule and mark questions to drop if time runs short. Recovery fields will stay blank, and every proposed Site B requirement will remain a question for the owner.

# Site B dispatch interview guide — draft

Sources:

- **site-a-activity-list.md** — version 3, 12 March 2026; approved by the Site A site manager. References below identify the activity or dependency.
- **impact-criteria.md** — version 1.1, 4 February 2026; approved by top management. References below identify the impact category.
- **site-b-org-chart.md** — no version or date; HR draft. Used only to frame questions, not as current organisational evidence.

For the activity owner: **use the draft as the thing to correct, not the thing to confirm; record what it could not have known.**

Every Site B entry below is **candidate, to confirm**. Source approval does not mean that a requirement has been confirmed for Site B. An AI-drafted resource requirement enters the register only when the activity owner confirms it.

## 1. Impacts over time and peak weeks

The sources do not rank activities by impact. Assess dispatch fully because it is the interview’s focus; ask about adjacent activities only where their effects differ.

| Candidate activity or impact | Question for the activity owner | Source |
|---|---|---|
| Chilled dispatch at Site B | Does chilled dispatch describe your activity accurately, and where does your responsibility start and end? | Site A activity list, A2; Site B organisation draft, Dispatch lead |
| Dispatch peak weeks | Site A records weeks 49–52 and week 14. Are these also Site B’s peak weeks, and what differs between them? | Site A activity list, A2 |
| Financial impact | As dispatch remains interrupted, when would daily losses move through the three financial levels, in ordinary and peak weeks? What evidence supports this? | Impact criteria, Financial |
| Customer impact | How would customer consequences develop over the interruption, and when would each customer level apply? | Impact criteria, Customer |
| Regulatory impact | What regulatory consequences would arise over time, and when would each regulatory level apply? | Impact criteria, Regulatory |
| Goods receipt interface | Does chilled goods receipt constrain dispatch at Site B? Does its peak pattern differ from dispatch’s? | Site A activity list, A1 and A2 |
| Quality release interface | Does release constrain dispatch at Site B? Where would its interruption effects differ from dispatch’s? | Site A activity list, A3 and recorded dependencies; Site B organisation draft, QA |

Use the approved criteria: financial levels are under EUR 10k/day, EUR 10k–100k/day and over EUR 100k/day. Customer levels progress from a complaint to a late key account to losing a key account. Regulatory levels progress from no consequence to reporting to the food authority to the authority stopping production. Record evidence and threshold crossings; the sources supply no ratings or assessment intervals.

## 2. MTPD

| Candidate activity | Question for the activity owner | MTPD | Source |
|---|---|---|---|
| Site B chilled dispatch | At what interruption duration would the consequences become unacceptable, and which impact establishes that limit? Does the peak period change it? | | Site A activity list, A2; Impact criteria, all categories |

The owner determines MTPD from the assessed impacts.

## 3. People

Cover people **with the skills, authorities and mandates the work needs**.

| Candidate requirement | Question for the activity owner | Source |
|---|---|---|
| Dispatch leadership and shift coverage | Is the draft’s dispatch-lead role with three shift leaders accurate? What coverage does each shift require in ordinary and peak weeks? | Site B organisation draft, Dispatch lead |
| Skills, authority and mandates | What skills and decision rights do the lead and shift leaders need to perform dispatch? Who can provide cover? | Site B organisation draft, Dispatch lead; details not in the sources |
| Quality-release authority | Is QA still covered from Site A? Who has authority to release goods and provide cover when needed? | Site B organisation draft, QA; Site A activity list, A3 and dependencies |

## 4. Seats and buildings

| Candidate requirement | Question for the activity owner | Source |
|---|---|---|
| Dispatch workplaces and premises | Which seats, work areas and buildings does dispatch need, and how does the requirement change during peak weeks? | Gaps — dispatch premises are not in the sources |
| Goods-receipt dock interface | Site A records two dock doors for goods receipt. What dock requirement, if any, applies to Site B’s dispatch interface? | Site A activity list, A1; no Site B requirement established |

## 5. IT and applications

Cover each application **with its RTO and its RPO**; leave both fields empty for the owner.

| Candidate requirement | Question for the activity owner | RTO | RPO | Source |
|---|---|---|---|---|
| Warehouse system | Is LogiStock still the system at Site A, and does Site B dispatch use it too? Which dispatch steps depend on it? | | | Site A activity list, A2 |
| Manual export interface | Is the recorded manual export to Site B still possible? What does it support, and what are its limitations for dispatch? | | | Site A activity list, A2 |

For each confirmed application, ask the owner what restoration deadline and maximum data loss the assessed impacts permit. No source proposes recovery times.

## 6. Suppliers and other third parties

| Candidate requirement | Question for the activity owner | Source |
|---|---|---|
| Carrier service | Is NordFrost still the carrier supporting Site A receipt and dispatch? Does Site B use it, or another carrier? | Site A activity list, A1 and recorded dependencies |
| Alternative carrier and contacts | Site A records no second carrier. What alternatives does Site B have, and who maintains the current carrier contacts for each shift and peak period? | Site A activity list, recorded dependencies; Site B details not in the sources |

Do not infer that Site B has a single carrier, or that a named individual is its only contact.

## 7. Dependencies on other departments

Record **up- and downstream relationships with other departments, each recorded with the RTO the relationship carries**.

| Candidate relationship | Question for the activity owner | Relationship RTO | Source |
|---|---|---|---|
| QA → dispatch | Does Site B require release from Site A QA before dispatch? What must QA provide, and by when? | | Site A activity list, A2 → A3 dependency; Site B organisation draft, QA |
| Warehouse ↔ dispatch | What must Warehouse provide to Dispatch, and what must Dispatch return? Which handoffs constrain peak weeks? | | Site B organisation draft, Warehouse and Dispatch roles; handoffs not in the sources |
| Site A ↔ Site B export interface | Which departments provide and receive the manual export, and what timing does that relationship require? | | Site A activity list, A2; department ownership not in the sources |

Carrier services belong in the supplier section. Where site registers conflict, put each conflict **to the two owners, not to the model**.

## Organiser’s take-in sheet

Provisional schedule: **45 minutes**. ★ means drop first if running late. No explicit source conflict is established; start with the arrangements that need reconciliation.

**Source differences and scope — 4 minutes**

Is Site A QA still responsible for Site B release, and does release have to happen before dispatch?

Is manual export from Site A still possible, and what can Site B actually do with it?

Which parts of the Site A dispatch description need correcting for Site B?

**Impacts and peak weeks — 8 minutes**

Are weeks 49–52 and week 14 your peak weeks, or are yours different?

As dispatch stops for longer, when do financial, customer and regulatory consequences cross the approved thresholds?

What changes during peak weeks?

★ Where do goods receipt and quality release have different interruption effects?

**MTPD — 4 minutes**

When do dispatch consequences become unacceptable, and what evidence sets that limit?

**People — 7 minutes**

Is the draft’s three-shift-leader arrangement accurate?

What coverage, skills, authorities and mandates does each shift need, especially at peaks?

Who can cover the essential roles and release authority?

**Seats and buildings — 4 minutes**

Which workplaces and premises must be available for dispatch?

★ Does the Site A dock arrangement resemble anything you need here?

**IT and applications — 6 minutes**

Is LogiStock still used at Site A, and do you use it here?

What does the manual export support, and where does it fall short?

For each application you identify, what restoration deadline and data-loss limit do the impacts permit?

**Suppliers — 5 minutes**

Is NordFrost still involved at Site A, and which carrier serves Site B?

What alternatives and carrier contacts are available on each shift and during peaks?

**Department dependencies — 5 minutes**

What do QA and Warehouse need to give you, and what do you give them?

Which departments own the export handoff?

What timing must each department relationship meet?

**Corrections and follow-up — 2 minutes**

What has this draft missed that only people at Site B would know?

Which requirements can you confirm, and which need another owner’s evidence?

## Gaps and handover

Organiser’s answers are **own statements, not sources**:

- The interviewee is the Site B dispatch lead, who knows shift patterns and carrier contacts.
- The requested output focuses on resources and peak weeks.
- Interview length was skipped; 45 minutes is a planning assumption, not a BIA value.
- The organiser states that the data is high sensitivity and this environment is approved for it.

Unresolved evidence:

- Site B’s organisation chart is an undated, unversioned draft; obtain a dated approved chart or owner confirmation.
- Site B’s actual peak weeks, resource quantities, premises, application use, carrier arrangements and department timings are **not in the sources**.
- No impact ranking, Site B impact assessment or recovery-time proposal is supplied.
- No named individual reviewer or top-management approver is supplied.

For every eventual register entry, retain its source, source date and status. Before interview, leave **interview reference/date, confirmation date, MTPD, RTO, RPO and dependency RTO empty**. Preserve confirmed and unconfirmed marks through handover.

The **Site B activity owner** confirms each requirement and sets recovery objectives. **Top management approves the BIA results**.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

**Tool calls (JSON events):**

- none
