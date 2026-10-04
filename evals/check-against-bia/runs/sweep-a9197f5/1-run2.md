# /check-against-bia case 1, run2: Claude Code, guidance at a9197f5

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `0e50f1ea-0d83-4a7c-9395-b73726e05f25`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the BIA, and tell me what the new trunking carrier from January touches. The files bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md, plan-quality-release.md and change-trunking-supplier.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the six files, one question:

**What class of data do these documents hold?** For example: public, internal, confidential, or strictly confidential / restricted. Use your organisation's own scheme if it has one.

I'll go by your answer, not by any marking in the files. Once I know the class, I'll check it against the skill's data rules to make sure this environment is approved for it, and then run the BIA comparison and the change check on the trunking carrier.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia && cat preflight.md; ls -R units 2>/dev/null | head; echo ---; cat units/stages/implement.md`
- Bash: `cd /tmp/claude-1001/-opt-brain-017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep8/runs/check-against-bia/1/run2/work 2>/dev/null || cd "$PWD"; pwd; ls -la; `
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/preflight.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/stages/implement.md`
- Glob: `*.md`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read all six files and none of them is a reason to stop.

Before I write the comparison, three questions about things the files leave open. Your answers will set the scope and go under Gaps as your own statements, never as sources. Skip any you like and I'll state the assumption I made instead.

1. **Plans I don't have:** Are there plans, contact lists or escalation routes that weren't attached and might also name NordFrost or the NordFrost control room? For example a Site B plan, a transport or carrier contingency plan, or a call tree. If you skip this, I'll assume the six files are the whole set and mark every other kind of document "coverage unknown".
2. **BIA version:** Is BIA v2 (approved 4 Feb 2026) still the current approved BIA, or is a newer version in draft or already approved? If you skip this, I'll treat v2 as the current approved version, as its header says.
3. **Change notice:** Is there a later version of the trunking change notice, or a Polar Haul contract summary, that you could attach? The notice is dated 15 September 2026 but has no version number. If you skip this, I'll use the notice as the only description of the change and note under Gaps that it has no version.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/data-rules.md`
- Glob: `**/*.md`
- Read: `/tmp/claude-1001/-opt-brain-017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep8/runs/check-against-bia/1/run2/work/bia-extract-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain-017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep8/runs/check-against-bia/1/run2/work/requirements-register.md`
- Read: `/tmp/claude-1001/-opt-brain-017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep8/runs/check-against-bia/1/run2/work/plan-chilled-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain-017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep8/runs/check-against-bia/1/run2/work/plan-goods-receipt.md`
- Read: `/tmp/claude-1001/-opt-brain-017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep8/runs/check-against-bia/1/run2/work/plan-quality-release.md`
- Read: `/tmp/claude-1001/-opt-brain-017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep8/runs/check-against-bia/1/run2/work/change-trunking-supplier.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/keep-it-running.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/prompts/evaluations.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep8/runs/check-against-bia/1/run2/work/bia-extract-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep8/runs/check-against-bia/1/run2/work/requirements-register.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep8/runs/check-against-bia/1/run2/work/plan-chilled-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep8/runs/check-against-bia/1/run2/work/plan-goods-receipt.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep8/runs/check-against-bia/1/run2/work/plan-quality-release.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep8/runs/check-against-bia/1/run2/work/change-trunking-supplier.md`

## Turn 3

**Request:** skip

**Reply (verbatim):**

# Check against the BIA: Site A chilled dispatch, and the January trunking carrier change

**Sources, one line each**
- `bia-extract-dispatch.md`: BIA v2, approved by top management 4 Feb 2026. BIA owner: BCM manager.
- `requirements-register.md`: version 5, 10 February 2026, approved by the BCM manager, built from BIA v2.
- `plan-chilled-dispatch.md`: version 3, 12 March 2026, approved. Plan owner: Head of Logistics.
- `plan-goods-receipt.md`: version 2, 3 March 2026, approved. Plan owner: Warehouse lead.
- `plan-quality-release.md`: version 1, 20 February 2026, approved. Plan owner: QA manager.
- `change-trunking-supplier.md`: dated 15 September 2026, **no version** (see Gaps). Status: "planned, approved by the procurement board". Raised by: Head of Procurement.

This is a report only. Nothing has been changed. A plan changes only with its owner's approval and a new version. Every owner named below is "proposed, to confirm".

---

## Block 1: The dispatch plan against the BIA

The task: compare the attached plan with the approved BIA and list where they disagree. I've changed neither document and propose no replacement values. Where two recovery times differ, I choose neither.

| # | Topic | Plan passage (`plan-chilled-dispatch.md`, v3, 12 Mar 2026) | BIA or register passage | Who decides (proposed, to confirm) |
|---|---|---|---|---|
| 1.1 | Recovery time | §2: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | BIA v2, 4 Feb 2026, B-A2, RTO column: "8 hours" | Plan: Head of Logistics. BIA B-A2: Dispatch lead |
| 1.2 | Staffing | §3: "A minimum of 3 pickers per shift travel to Site B." | BIA v2, 4 Feb 2026, B-A2: "at least 4 pickers per shift". Register v5, 10 Feb 2026, R-07: "Chilled dispatch: at least 4 pickers per shift" | Plan: Head of Logistics. BIA B-A2 and R-07: Dispatch lead |
| 1.3 | Supplier (second carrier) | §5: "Backup carrier: KuehlTrans, by spot booking." | BIA v2, 4 Feb 2026, B-A2: "carrier: NordFrost, no second carrier recorded". Register v5, 10 Feb 2026, R-08: "one carrier, NordFrost; second carrier open" | Plan: Head of Logistics. BIA B-A2: Dispatch lead. R-08: **none named** (see Gaps) |

**Checked, no disagreement found:**
- Carrier escalation. Plan §4 says "Carrier escalation: NordFrost control room, 040 555 0900" and BIA B-A2 says "carrier escalation: NordFrost control room". The phone number is not in the BIA.
- The warehouse system. Plan §6 says "Orders leave LogiStock by the manual export in work instruction WI-14". The plan gives no LogiStock restore time ("not in the sources"), and register R-09 says "LogiStock restored within 6 hours". The plan is silent here rather than contradicting the register.

**Where the attached plans contradict each other**

| # | Topic | Passage A | Passage B | Who decides (proposed, to confirm) |
|---|---|---|---|---|
| 1.4 | An action given to the dispatch lead by another plan | `plan-goods-receipt.md`, v2, 3 Mar 2026, §3: "On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | `plan-chilled-dispatch.md`, v3, 12 Mar 2026: the plan doesn't hold this action ("not in the sources") | Warehouse lead and Head of Logistics |
| 1.5 | Backup carrier for trunking | `plan-chilled-dispatch.md`, v3, 12 Mar 2026, §5: "Backup carrier: KuehlTrans, by spot booking." | `plan-goods-receipt.md`, v2, 3 Mar 2026, §3: "Inbound trunking from Site B: NordFrost." No backup carrier ("not in the sources") | Head of Logistics and Warehouse lead |

The quality release plan has no contradiction with the dispatch plan. I compared only the dispatch plan against the BIA, as you asked. The goods receipt and quality release plans were not checked against their BIA entries.

---

## Block 2: What the trunking change reopens

The task: the attached change is planned. Find which of the attached plans, BIA entries and register entries it reopens. Report only; change nothing.

The change, from `change-trunking-supplier.md` (15 Sep 2026, unversioned): "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul, under a new contract. NordFrost's control room will no longer handle Site A loads from that date."

| # | Document and section | Line the change touches (quoted) | Who decides (proposed, to confirm) |
|---|---|---|---|
| 2.1 | `plan-chilled-dispatch.md`, v3, 12 Mar 2026, §4 Contacts | "Carrier escalation: NordFrost control room, 040 555 0900." | Head of Logistics |
| 2.2 | `plan-chilled-dispatch.md`, v3, 12 Mar 2026, §5 Suppliers | "Trunking from Site A to Site B and outbound chilled transport: NordFrost. Backup carrier: KuehlTrans, by spot booking." | Head of Logistics |
| 2.3 | `plan-goods-receipt.md`, v2, 3 Mar 2026, §3 Inbound transport | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Warehouse lead |
| 2.4 | `bia-extract-dispatch.md`, BIA v2, 4 Feb 2026, B-A1 | "carrier: NordFrost, inbound trunking from Site B" | Activity owner: Warehouse lead. BIA owner: BCM manager |
| 2.5 | `bia-extract-dispatch.md`, BIA v2, 4 Feb 2026, B-A2 | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Activity owner: Dispatch lead. BIA owner: BCM manager |
| 2.6 | `requirements-register.md`, v5, 10 Feb 2026, R-08 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | **none named** (see Gaps) |

**Not touched, among the attached files:** `plan-quality-release.md`, BIA B-A3, and register entries R-06, R-07 and R-09.

**Change triggers to keep:**
- A change of chilled trunking or outbound carrier, or of the carrier's control room, should reopen the dispatch plan (§4, §5), the goods receipt plan (§3), BIA entries B-A1 and B-A2, and register entry R-08.

---

## Gaps

- **Register R-08 has no named owner.** The owner cell is empty, so it reads "none named". It is touched by both block 1 (1.3) and block 2 (2.6). I have not inferred an owner.
- **The change notice is dated but unversioned.** `change-trunking-supplier.md` is dated 15 September 2026 and has no version. Its status is "planned", so I've treated it as a planned change, not as the current state.
- **The BIA is an extract.** `bia-extract-dispatch.md` holds only B-A1 to B-A3 of BIA v2. The rest of the BIA was not seen.
- **Not in the sources:**
  - an escalation contact or control room for Polar Haul
  - whether the KuehlTrans spot-booking arrangement in dispatch plan §5 has any status after 1 January 2027
  - who handles the "hold inbound loads at Site B" request (goods receipt plan §3) once NordFrost's control room stops handling Site A loads
  - a LogiStock restore time in the dispatch plan
- **Intake: you skipped all three questions.** These are my assumptions, not sources:
  - the six attached files are the whole set
  - BIA v2 (4 Feb 2026) is the current approved BIA
  - the change notice is the only description of the change
- **No passage telling an AI to act** was found in any of the attached files.

## For the auditor

This is the list of changes that reopen which plan (block 2, Change triggers). Each passage is quoted with its document, section and date, and each owner is "proposed, to confirm".

## Reviewer

The BCM manager who asked for this check checks each quoted passage against its source. Each plan owner and BIA activity owner then decides whether their document changes:
- **Plan owners:** Head of Logistics (dispatch plan) and Warehouse lead (goods receipt plan).
- **BIA activity owners:** Dispatch lead (B-A2) and Warehouse lead (B-A1).
- **Register R-08:** no owner is named, so this one can't be routed yet.

## Coverage unknown

Coverage is unknown for kinds of document that weren't attached:
- Site B plans
- contact lists and call trees
- escalation routes
- a transport or carrier contingency plan
- the NordFrost, KuehlTrans and Polar Haul contracts
- work instruction WI-14
- partner lab agreement QA-03
- the full BIA beyond this extract

---

Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> Use review.md on plan-chilled-dispatch.md, with Head of Logistics: type /challenge-my-plan.

> Use review.md on plan-goods-receipt.md, with Warehouse lead: type /challenge-my-plan.

**Tool calls (stream-json):**

- none
