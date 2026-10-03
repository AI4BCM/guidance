# prepare-bia baseline (no skill loaded), run1: Codex, guidance at 836c32f

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with no `.agents/skills/` (no AI4BCM package). Every agent message of a turn is kept, in order. One driver. Session `01a0ff1d-94a1-7dc1-9730-e415da62155f`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’ll read the three files and use them to draft a dispatch interview guide tailored to Site B.

# Site B dispatch interview guide — draft

**Purpose:** Establish Site B’s dispatch activities, the consequences of disruption over time, recovery needs and dependencies for the business impact analysis (BIA).

**Interviewees:** Dispatch lead, Site B, with input from the three shift leaders. Confirm this structure first: Site B’s organisation chart is an undated, unversioned HR draft. Seek follow-up input from the warehouse lead, Site A QA and the site manager.

**Suggested duration:** 60–75 minutes.

## 1. Confirm scope and ownership

- What does Site B dispatch, to which customers, and during which operating hours?
- Where does dispatch start and end? Which tasks belong to warehouse, QA or carriers?
- Who owns the activity, who acts as deputy, and who can authorise workarounds?
- Do all three shifts perform the same tasks? What differs between shifts?
- Which dispatch tasks need separate assessment because their deadlines, impacts or dependencies differ?

Ask the interviewee to describe a normal shipment from order receipt through release, loading, departure and confirmation. Record the actual Site B workflow.

## 2. Test the Site A reference against Site B

Site A’s approved activity list is a starting point for questions, **not an approved description of Site B**.

| Site A reference | Question for Site B |
|---|---|
| Chilled dispatch | Does Site B dispatch chilled products? What temperature, storage-life and handling constraints apply? |
| Peaks in weeks 49–52 and week 14 | Does Site B have the same peaks? What other dates, daily cut-offs or customer deadlines matter? |
| LogiStock warehouse system | Which systems does Site B use, and which dispatch tasks depend on each? |
| QA release required before dispatch | What release evidence does Site B require, and how does Site A QA provide it? |
| NordFrost; no second carrier recorded | Which carriers serve Site B? Are alternatives contracted, available and suitable? |
| Manual export to Site B possible | What is exported, how would Site B receive and use it, and has this process been tested? |

For each item, record **confirmed, different, not applicable or unresolved**, with supporting evidence.

## 3. Assess disruption impacts over time

Start with a complete dispatch stoppage, then consider reduced capacity. Ask when consequences begin, when they escalate, and how peak periods change the answers.

Use checkpoints such as **2, 4, 8, 24, 48 and 72 hours**, adjusting them to actual shipment deadlines. These are interview prompts, not predetermined recovery targets.

Apply the approved impact criteria:

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | Under EUR 10k a day | One customer complains | None |
| 2 | EUR 10k–100k a day | A key account is late | A report to the food authority |
| 3 | Over EUR 100k a day | A key account is lost | The authority stops production |

Ask:

- What financial loss arises at each checkpoint—such as spoilage, penalties, lost sales or additional transport costs? Explain the estimate and avoid double counting.
- Which customers are affected first? When would a key account become late or be at risk of loss?
- Could a disruption require reporting to the food authority or lead to a production stop? Ask QA to validate the trigger and timing.
- Would stock accumulation constrain storage, goods receipt or production?
- What changes during peaks, weekends or a disruption affecting both sites?

Record each impact dimension separately, including assumptions and evidence. The supplied criteria do not specify which level is unacceptable or how to combine scores; obtain that decision from the authorised BIA owner.

## 4. Establish recovery needs

- What is the longest interruption Site B could tolerate before impacts become unacceptable, and why?
- By when must dispatch resume to avoid that point?
- What minimum service is needed initially: shipments per hour, priority customers, product groups or percentage of normal throughput?
- Which orders should take priority, and who decides?
- How long would backlog clearance take at reduced and normal capacity?
- What dispatch data must be restored, and how much data loss could be tolerated?
- What reconciliation is needed after manual operation?

Record proposed recovery targets separately from current demonstrated capability. Flag any gap for validation.

## 5. Identify dependencies and workarounds

For each dependency, capture the provider or owner, minimum requirement, failure consequence, available substitute and latest test evidence.

Cover:

- **People:** minimum staffing per shift, required skills, deputies and cross-training.
- **QA at Site A:** release availability, out-of-hours cover and fallback arrangements.
- **Warehouse and facilities:** stock access, loading capacity, refrigeration, power and equipment.
- **Systems and data:** order information, stock records, release status, labels, connectivity and dispatch confirmation.
- **Carriers:** collection cut-offs, capacity, temperature controls and alternative transport.
- **Other sites:** whether Site A could support Site B, with what capacity, prerequisites and lead time.

For each workaround, ask: Who authorises it? How quickly can it start? What throughput can it sustain? How long can it operate? What food-safety and traceability controls must remain in place?

## 6. Close and capture actions

Read back the activity scope, earliest material impacts, proposed recovery needs and critical dependencies.

Request relevant evidence: dispatch procedures, shipment volumes, customer cut-offs, staffing arrangements, carrier agreements, QA release procedures and workaround test records.

Use this capture template:

| Finding or proposal | Evidence / assumption | Validation owner | Due date |
|---|---|---|---|
| Activity scope and owner | | | |
| Impacts and escalation times | | | |
| Maximum tolerable interruption | | | |
| Recovery time and minimum capacity | | | |
| Data recovery requirement | | | |
| Dependencies and workaround gaps | | | |

**Expected output:** A Site B dispatch BIA draft with confirmed facts, explicit assumptions, proposed recovery requirements and assigned follow-up actions. Interview findings remain subject to validation and approval.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd && rg --files -g '*.md'"`
- command_execution: `/bin/bash -lc 'cat site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md'`
- command_execution: `/bin/bash -lc 'cat impact-criteria.md'`
