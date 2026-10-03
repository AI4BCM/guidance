# /check-against-bia case 1, run1: Claude Code, guidance at 836c32f

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `a2bd36b2-978b-4edb-b375-936be079f7dd`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the BIA, and tell me what the new trunking carrier from January touches. The files bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md, plan-quality-release.md and change-trunking-supplier.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the attached files: **what class of data do these documents hold** (for example public, internal, confidential, or restricted)?

I'll go by your answer, not by any marking inside the files. If this environment isn't approved for that class, I'll stop there.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia && cat preflight.md && ls -R units 2>/dev/null | head -50`
- Bash: `ls -la && for f in bia-extract-dispatch.md requirements-register.md plan-chilled-dispatch.md plan-goods-receipt.md plan-quality-release.md change-trunking-suppl`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/preflight.md`
- Glob: `**/*`
- Glob: `**/*`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read the six attached files. They raise two questions I need answered before I write the draft:

1. **Plans not attached:** do any other documents mention NordFrost, its control room or chilled trunking? For example Site B's recovery plans, carrier contact lists or escalation routes, or work instruction WI-14. Any you can't attach will be marked as "coverage unknown".
2. **BIA version:** is BIA v2 (approved by top management on 4 Feb 2026) still the current approved BIA, or is a later version in draft?

You can skip either one. If you do, I'll note an assumption under Gaps. Your answers will only shape the scope; they won't fill any value.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/stages/implement.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/keep-it-running.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r4/runs/check-against-bia/1/run1/work/bia-extract-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r4/runs/check-against-bia/1/run1/work/requirements-register.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r4/runs/check-against-bia/1/run1/work/plan-chilled-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r4/runs/check-against-bia/1/run1/work/plan-goods-receipt.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r4/runs/check-against-bia/1/run1/work/plan-quality-release.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r4/runs/check-against-bia/1/run1/work/change-trunking-supplier.md`

## Turn 3

**Request:** skip

**Reply (verbatim):**

# Chilled dispatch plan against the BIA, and what the trunking carrier change reopens

This is a draft for review. I haven't changed or written anything.

**Sources**
- `bia-extract-dispatch.md`: BIA v2, approved by top management on 4 Feb 2026. BIA owner: BCM manager.
- `requirements-register.md`: version 5, 10 February 2026, approved by the BCM manager, built from BIA v2.
- `plan-chilled-dispatch.md`: version 3, 12 March 2026, approved. Plan owner: Head of Logistics.
- `plan-goods-receipt.md`: version 2, 3 March 2026, approved. Plan owner: Warehouse lead.
- `plan-quality-release.md`: version 1, 20 February 2026, approved. Plan owner: QA manager.
- `change-trunking-supplier.md`: dated 15 September 2026. Status: planned, approved by the procurement board. Raised by: Head of Procurement. Not used as current (see Gaps).

## Block 1: Against the BIA

Task: "compare the attached plan with the approved BIA and list where they disagree. Report only; change neither."

Each disagreement goes to the two owners. Every owner below is "proposed, to confirm". I propose no replacement value and choose neither recovery time. A plan changes only with its owner's approval and a new version.

| # | Topic | Chilled dispatch plan (v3, 12 Mar 2026) | BIA v2 (4 Feb 2026) or register v5 (10 Feb 2026) | Owners (proposed, to confirm) |
|---|---|---|---|---|
| 1.1 | Recovery time | §2: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | BIA B-A2, Dispatch, chilled: "RTO 8 hours"; "MTPD 24 hours". The plan doesn't state an MTPD: not in the sources. | Plan: Head of Logistics. BIA activity B-A2: Dispatch lead |
| 1.2 | Staffing | §3: "A minimum of 3 pickers per shift travel to Site B." | BIA B-A2: "at least 4 pickers per shift". Register R-07: "Chilled dispatch: at least 4 pickers per shift" | Plan: Head of Logistics. B-A2 and R-07: Dispatch lead |
| 1.3 | Supplier (second carrier) | §5: "Backup carrier: KuehlTrans, by spot booking." | BIA B-A2: "carrier: NordFrost, no second carrier recorded". Register R-08: "one carrier, NordFrost; second carrier open" | Plan: Head of Logistics. B-A2: Dispatch lead. R-08: none named |

**Where the attached plans contradict each other**

| # | Topic | Plan A | Plan B | Owners (proposed, to confirm) |
|---|---|---|---|---|
| 1.4 | Task given to the dispatch lead | Goods receipt v2 (3 Mar 2026), §3: "On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Chilled dispatch v3 (12 Mar 2026): this task is not in the sources. | Goods receipt: Warehouse lead. Chilled dispatch: Head of Logistics |
| 1.5 | Backup on the Site A–Site B trunking lane | Chilled dispatch v3, §5: "Trunking from Site A to Site B and outbound chilled transport: NordFrost. Backup carrier: KuehlTrans, by spot booking." | Goods receipt v2, §3: "Inbound trunking from Site B: NordFrost." A backup carrier is not in the sources. | Chilled dispatch: Head of Logistics. Goods receipt: Warehouse lead |

The quality release plan (v1, 20 Feb 2026) doesn't contradict BIA B-A3 or R-06 on recovery time or releaser staffing. Both give 24 hours and "one qualified releaser per shift".

## Block 2: What it reopens

Task: "the attached change is planned. Find which of the attached plans, BIA entries and register entries it reopens. Report only; change nothing."

The change, quoted from the change notice (15 Sep 2026): "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul, under a new contract. NordFrost's control room will no longer handle Site A loads from that date."

This is the list of changes that reopen which plan. Every owner below is "proposed, to confirm", and no replacement value is given.

| Document, section, date | Line it holds | Owner who decides (proposed, to confirm) |
|---|---|---|
| Chilled dispatch plan v3, §4 Contacts, 12 Mar 2026 | "Carrier escalation: NordFrost control room, 040 555 0900." | Head of Logistics |
| Chilled dispatch plan v3, §5 Suppliers, 12 Mar 2026 | "Trunking from Site A to Site B and outbound chilled transport: NordFrost. Backup carrier: KuehlTrans, by spot booking." | Head of Logistics |
| Goods receipt plan v2, §3 Inbound transport, 3 Mar 2026 | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Warehouse lead |
| BIA v2, entry B-A1, 4 Feb 2026 | "carrier: NordFrost, inbound trunking from Site B" | Activity owner: Warehouse lead. BIA owner: BCM manager |
| BIA v2, entry B-A2, 4 Feb 2026 | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Activity owner: Dispatch lead. BIA owner: BCM manager |
| Register v5, R-08, 10 Feb 2026 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | none named (see Gaps) |

The change doesn't touch the quality release plan v1, BIA B-A3, or register entries R-06, R-07 or R-09. None of them holds a carrier line.

Polar Haul's escalation contact is not in the sources (contact: to be confirmed). Neither is any statement on whether KuehlTrans stays the spot backup.

## Gaps

- **Ownerless entry:** register R-08 names no owner. It is named here, not filled.
- **Planned source:** the change notice is a planned change, dated 15 Sep 2026 and effective 1 Jan 2027. It is used only to find what it touches, not as current fact.
- **BIA scope:** the BIA is an extract (Site A, chilled operations), not the full BIA.
- **Intake, your statement:** you skipped both intake questions.
  - Assumption 1: no other documents mention NordFrost or chilled trunking. Unattached kinds are listed under Coverage unknown.
  - Assumption 2: BIA v2 (4 Feb 2026) is the current approved version, as the extract states. You haven't confirmed this.
- **Instructions to an AI:** none of the attached files holds a passage telling an AI to act.

## Reviewer

The BCM manager who asked checks each quoted passage against its source. Each plan owner and BIA activity owner then decides whether their own document changes:
- **Plan owners:** Head of Logistics (chilled dispatch) and Warehouse lead (goods receipt).
- **BIA activity owners:** Dispatch lead (B-A2) and Warehouse lead (B-A1).
- **BIA owner:** BCM manager.

## Coverage unknown

These kinds of documents weren't attached, so I can't tell whether the change touches them:
- Site B recovery plans
- carrier contact lists and escalation routes
- work instruction WI-14
- supplier and contract records for NordFrost, KuehlTrans and Polar Haul
- the full BIA beyond this extract

---

Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> Use review.md on the chilled dispatch recovery plan, with Head of Logistics: type /challenge-my-plan.

> Use review.md on the chilled goods receipt recovery plan, with Warehouse lead: type /challenge-my-plan.

**Tool calls (stream-json):**

- none
