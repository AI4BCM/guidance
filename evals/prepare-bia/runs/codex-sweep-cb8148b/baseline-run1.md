# prepare-bia baseline (no skill loaded), run1: Codex, guidance at cb8148b

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with no `.agents/skills/` (no AI4BCM package). Every agent message of a turn is kept, in order. One driver. Session `01a0fce3-d03d-7601-98c2-a2d621837d45`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’ll read the three files and use them to draft a dispatch interview guide tailored to Site B.

# Site B dispatch interview guide

**Purpose:** Confirm how dispatch operates at Site B, assess the consequences of disruption over time, and identify recovery requirements and dependencies.

**Interviewees:** Dispatch lead, Site B, with input from the three shift leaders. Include the warehouse lead and the person responsible for QA coverage from Site A. Confirm these roles first: Site B’s organisation chart is an undated, unversioned HR draft.

**Preparation:** Request dispatch volumes, customer delivery cut-offs, shift schedules, process instructions, recent disruption records, and any recovery arrangements.

## 1. Confirm the activity and ownership

- What does Site B dispatch handle? Does it include chilled products?
- Where does the activity start and end? Who owns picking, staging, loading, transport booking, dispatch records and delivery confirmation?
- Is the dispatch lead accountable across all shifts? Who deputises?
- What differs between shifts, weekdays and weekends?
- Which activities must happen before dispatch can proceed?

**Record:** Agreed activity description, boundaries, accountable owner, deputies and interfaces with warehouse and QA.

## 2. Validate the Site A comparison

Use Site A’s approved activity list as a prompt, not as evidence of Site B’s arrangements.

| Site A information | Questions for Site B |
|---|---|
| Dispatch handles chilled products | Does Site B handle the same products and temperature requirements? |
| Peak weeks are 49–52 and week 14 | Are these also Site B’s peaks? What volumes and deadlines apply? |
| Dispatch uses LogiStock | Which systems does Site B use, and for which steps? |
| Manual export to Site B is possible | What is exported—data, orders or another item? Can Site B receive and use it? Has this been tested, and at what capacity? |
| QA release is required before dispatch; the lab is at Site A only | Who releases Site B products? How is release communicated and verified? What happens if Site A QA or its lab is unavailable? |
| NordFrost is the carrier; no second carrier is recorded | Which carriers serve Site B? Are alternatives contracted, suitable and available during a wider disruption? |

## 3. Assess disruption impacts over time

Ask: **“If dispatch stopped completely, what would happen, and when?”** Repeat for reduced capacity and peak periods.

Use practical checkpoints such as 2, 4, 8, 24, 48 and 72 hours, then longer if relevant. Adjust these to actual dispatch cut-offs and product constraints.

Apply the approved impact criteria exactly:

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | Under EUR 10k a day | One customer complains | None |
| 2 | EUR 10k–100k a day | A key account is late | A report to the food authority |
| 3 | Over EUR 100k a day | A key account is lost | The authority stops production |

For each checkpoint, ask:

- What daily financial loss would occur? Explain assumptions, including spoilage, penalties and extra transport or storage costs.
- Which customers would be affected, and when would a key account become late or be lost?
- What specific event would require reporting to the food authority or could lead to a production stop? Validate regulatory judgments with QA.
- Would backlog, cold-storage limits, shelf life or missed collection slots worsen the impact or affect production?
- What evidence supports the estimate?

**Record separately:** Financial, customer and regulatory levels, timing, assumptions and evidence. The criteria do not specify how to combine scores or which level is unacceptable; confirm those decisions with the BCM owner and management.

## 4. Establish recovery requirements

- At what point would disruption become unacceptable, and why? Record a proposed **maximum tolerable period of disruption** for management validation.
- How quickly must dispatch resume to avoid that point? Record a proposed **recovery time objective**, allowing time to clear backlog and meet cut-offs.
- What minimum service is needed at restart: loads, pallets or orders per shift, priority customers and operating hours?
- How long would it take to clear the backlog after restarting?
- If records were lost, how much data loss could be tolerated? Which order, stock, traceability and QA-release records must be reconstructed?

Distinguish the required recovery time from the recovery time currently achievable.

## 5. Identify dependencies and workable alternatives

For each dependency, establish the minimum quantity or capacity, owner, restoration time and available workaround.

- **People:** Shift leaders, trained dispatch staff, required qualifications and deputies.
- **Facilities and equipment:** Loading areas, cold storage, handling equipment, power and temperature monitoring.
- **Systems and data:** Dispatch and warehouse systems, connectivity, devices, order data and release records.
- **Internal services:** Warehouse operations, Site A QA, laboratory services and relevant IT support.
- **External services:** Carriers, collection schedules and any outsourced storage or equipment support.

Ask whether manual dispatch, another carrier or another site could support recovery. For each option, confirm activation time, sustainable capacity, access to records, QA and temperature controls, and test evidence.

## 6. Close and validate

Read back the findings and distinguish confirmed facts from estimates and assumptions. Agree owners and dates for unresolved questions.

The interview record should contain:

- Confirmed activity scope and ownership.
- Impact progression under normal and peak conditions.
- Proposed tolerable disruption period, recovery target and minimum service.
- Essential resources, dependencies and evidenced alternatives.
- Gaps, follow-up actions and validation owners.

Have the dispatch lead validate operational findings, QA validate release and regulatory assumptions, and the appropriate site management/BCM authority approve recovery priorities.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md'"`
- command_execution: `/bin/bash -lc 'cat impact-criteria.md'`
- command_execution: `/bin/bash -lc 'cat site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md'`
