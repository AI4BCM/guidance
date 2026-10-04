# /check-against-bia case 1, run2: Claude Code, guidance at 07b8232

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `36d37ad0-87c4-45a6-8a50-eb316c3133a9`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the BIA, and tell me what the new trunking carrier from January touches. The files bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md, plan-quality-release.md and change-trunking-supplier.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the six files, I need one answer from you.

**What class of data do these files hold?** For example: public, internal, or high-sensitivity. High-sensitivity covers things like BIA data, recovery strategies, supplier weaknesses and contractual dependencies.

I'll go by your answer, not by any marking inside the files. If the material is high-sensitivity, please also confirm that this environment is approved for that class. If it isn't, I'll stop here.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia && cat preflight.md && ls -R; echo ----; cd /tmp/claude-1001/-opt-brain-017fd913-51f5-4e7f-a`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/preflight.md`
- Glob: `**/*`
- Glob: `**/*`
- Grep: `Sensitivity classes`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read all six files. Following the intake step, there are two things the files don't answer. Your answers will be recorded under Gaps as your own statements. They can shape the scope but won't fill in any value.

1. **Plans not attached:** are there other documents that name NordFrost or the NordFrost control room, beyond these three plans? For example, Site B's plans, a contact or escalation list, or a transport or IT plan. Anything not attached will be marked "coverage unknown".
2. **BIA version:** is BIA v2 (approved 4 Feb 2026) still the current approved BIA for Site A, with no newer draft or approved version?

If you'd rather skip either question, say so. I'll write down an assumption in its place and carry on.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain-017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run2/work/bia-extract-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain-017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run2/work/requirements-register.md`
- Read: `/tmp/claude-1001/-opt-brain-017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run2/work/plan-chilled-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain-017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run2/work/plan-goods-receipt.md`
- Read: `/tmp/claude-1001/-opt-brain-017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run2/work/plan-quality-release.md`
- Read: `/tmp/claude-1001/-opt-brain-017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run2/work/change-trunking-supplier.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/stages/implement.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run2/work/bia-extract-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run2/work/requirements-register.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run2/work/plan-chilled-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run2/work/plan-goods-receipt.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run2/work/plan-quality-release.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run2/work/change-trunking-supplier.md`

## Turn 3

**Request:** skip

**Reply (verbatim):**

# Draft: check-against-bia, Site A chilled operations

**Sources (version and date)**
- BIA extract, Site A chilled operations: BIA v2, approved by top management 4 Feb 2026. Owner: BCM manager.
- Requirements register, Site A: Version 5, 10 February 2026, approved by the BCM manager. Built from BIA v2.
- Chilled dispatch recovery plan: Version 3, 12 March 2026, approved. Owner: Head of Logistics.
- Chilled goods receipt recovery plan: Version 2, 3 March 2026, approved. Owner: Warehouse lead.
- Quality release recovery plan: Version 1, 20 February 2026, approved. Owner: QA manager.
- Change notice, chilled trunking carrier: dated 15 September 2026, **no version**, status "planned". This is not treated as current (see Gaps).

## Block 1: Against the BIA

Task: "compare the attached plan with the approved BIA and list where they disagree. Report only; change neither."

### Chilled dispatch plan v3 vs BIA v2, entry B-A2 (and register v5)

| # | Topic | Plan passage (plan v3, 12 Mar 2026) | BIA / register passage | Owners, proposed, to confirm |
|---|---|---|---|---|
| 1 | Recovery time | §2: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | BIA v2, B-A2, 4 Feb 2026: RTO "8 hours" (MTPD "24 hours") | Plan: Head of Logistics. BIA activity: Dispatch lead. BIA: BCM manager |
| 2 | Staffing | §3: "A minimum of 3 pickers per shift travel to Site B." | BIA v2, B-A2: "at least 4 pickers per shift". Register v5, R-07, 10 Feb 2026: "Chilled dispatch: at least 4 pickers per shift" | Plan: Head of Logistics. BIA activity and R-07: Dispatch lead |
| 3 | Second carrier | §5: "Backup carrier: KuehlTrans, by spot booking." | BIA v2, B-A2: "carrier: NordFrost, no second carrier recorded". Register v5, R-08: "one carrier, NordFrost; second carrier open" | Plan: Head of Logistics. BIA activity: Dispatch lead. R-08: none named |

I'm not choosing either recovery time and I'm proposing no replacement values. Each of these goes to both owners: a plan changes only with its owner's approval and a new version.

The carrier escalation route agrees. Plan §4 says "Carrier escalation: NordFrost control room, 040 555 0900" and BIA B-A2 says "carrier escalation: NordFrost control room".

### Where the related plans contradict each other

| # | Topic | Passage A | Passage B | Owners, proposed, to confirm |
|---|---|---|---|---|
| 4 | Action assigned to the dispatch lead | Goods receipt plan v2, §3, 3 Mar 2026: "On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Chilled dispatch plan v3: this action and the dispatch lead role are not in the sources | Goods receipt plan: Warehouse lead. Dispatch plan: Head of Logistics |

The goods receipt plan (RTO "12 hours") and the quality release plan (RTO "24 hours", "One qualified releaser per shift") match BIA B-A1 and B-A3 and register R-06.

## Block 2: What it reopens

Task: "the attached change is planned. Find which of the attached plans, BIA entries and register entries it reopens. Report only; change nothing."

The trigger is the change notice of 15 Sep 2026: "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul … NordFrost's control room will no longer handle Site A loads from that date."

| Document and entry | Line it holds now | Owner, proposed, to confirm |
|---|---|---|
| Chilled dispatch plan v3, §4 Contacts (12 Mar 2026) | "Carrier escalation: NordFrost control room, 040 555 0900." | Head of Logistics |
| Chilled dispatch plan v3, §5 Suppliers (12 Mar 2026) | "Trunking from Site A to Site B and outbound chilled transport: NordFrost. Backup carrier: KuehlTrans, by spot booking." | Head of Logistics |
| Goods receipt plan v2, §3 Inbound transport (3 Mar 2026) | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Warehouse lead |
| BIA v2, B-A1 (4 Feb 2026) | "carrier: NordFrost, inbound trunking from Site B" | Activity: Warehouse lead. BIA: BCM manager |
| BIA v2, B-A2 (4 Feb 2026) | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Activity: Dispatch lead. BIA: BCM manager |
| Register v5, R-08 (10 Feb 2026) | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | none named |

The change doesn't touch the quality release plan v1 or register entries R-06, R-07 and R-09.

## Gaps
- **Change notice:** it is dated (15 September 2026) but has no version, and its status is "planned". It's used only as the trigger, not as a current source. It names no escalation route or control room for Polar Haul ("carrier escalation: to be confirmed"). Whether KuehlTrans stays as the backup is not in the sources.
- **Register R-08:** no owner is named.
- **Intake (your answer: skip):** I asked whether other documents name NordFrost, and assumed that unknown. I asked whether BIA v2 is the current approved BIA, and assumed yes, unconfirmed.
- No passage in the attached files tells an AI to act.

## Reviewer
The BCM manager who asked for this check verifies each quoted passage. Then each plan owner (Head of Logistics, Warehouse lead) and each BIA activity owner (Dispatch lead, Warehouse lead) decides whether their document changes.

## Coverage unknown
These weren't attached, so I can't say whether the change touches them:
- contact and escalation lists
- Site B's plans
- carrier contracts and SLAs
- work instruction WI-14
- any transport, IT or crisis plan that names NordFrost

---

Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> Use review.md on the chilled dispatch recovery plan, with Head of Logistics: type /challenge-my-plan.

> Use review.md on the chilled goods receipt recovery plan, with Warehouse lead: type /challenge-my-plan.

**Tool calls (stream-json):**

- Grep: `Say in the document that AI helped`
