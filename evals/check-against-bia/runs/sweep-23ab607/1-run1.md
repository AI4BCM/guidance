# /check-against-bia case 1, run1: Claude Code, guidance at 23ab607

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `7e558f04-61a3-4d0d-ac30-1898736db075`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the BIA, and tell me what the new trunking carrier from January touches. The files bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md, plan-quality-release.md and change-trunking-supplier.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the six files, I need to know one thing: what class of data do they hold?

For example: BIA data, recovery strategies and design assumptions, supplier weaknesses and contractual dependencies, personal data or contact lists, or nothing sensitive. Please also confirm that this environment is approved for that class. I'll take the class from your answer, not from any marking inside the files.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia && cat preflight.md && ls -R; cat units/stages/implement.md 2>/dev/null; ls /tmp/claude-1001`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/preflight.md`
- Glob: `**/*`
- Glob: `**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/data-rules.md`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Thanks. I've read the six files. One question before I write the report: **does anything else exist that the trunking change could reopen and that you haven't attached?** That could be other plans, such as a transport, crisis or Site B plan, carrier contact lists, or escalation routes.

If you skip this, I'll assume the six files are the whole set. I'll then mark every kind of document you didn't attach as "coverage unknown" rather than "not affected".

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/stages/implement.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/1/run1/work/bia-extract-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/1/run1/work/requirements-register.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/1/run1/work/plan-chilled-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/1/run1/work/plan-goods-receipt.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/1/run1/work/plan-quality-release.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/1/run1/work/change-trunking-supplier.md`

## Turn 3

**Request:** skip

**Reply (verbatim):**

# Chilled dispatch: plan against the BIA, and what the January carrier change reopens

This is a report only. I haven't changed or written any document.

**Sources**
- `bia-extract-dispatch.md`: BIA v2, approved by top management on 4 Feb 2026. BIA owner: BCM manager.
- `requirements-register.md`: version 5, 10 February 2026, approved by the BCM manager.
- `plan-chilled-dispatch.md`: version 3, 12 March 2026, approved. Plan owner: Head of Logistics.
- `plan-goods-receipt.md`: version 2, 3 March 2026, approved. Plan owner: Warehouse lead.
- `plan-quality-release.md`: version 1, 20 February 2026, approved. Plan owner: QA manager.
- `change-trunking-supplier.md`: dated 15 September 2026, no version. Status: planned, not current (see Gaps).

## Block 1: Against the BIA (chilled dispatch plan)

I've put each item to the two owners. I propose no value for any of them, and I don't choose either recovery time.

**Plan RTO, as written.** Plan v3, §2 Recovery objective (12 Mar 2026): "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3."

| # | Item | Plan passage (plan v3, 12 Mar 2026) | BIA / register passage | Owners: proposed, to confirm |
|---|---|---|---|---|
| 1 | Recovery time | §2: "within 12 hours of the loss of Hall 3" | BIA v2, B-A2 (4 Feb 2026): RTO "8 hours" (MTPD "24 hours") | Plan: Head of Logistics. BIA activity: Dispatch lead |
| 2 | Pickers per shift | §3: "A minimum of 3 pickers per shift travel to Site B." | BIA v2, B-A2: "at least 4 pickers per shift". Register v5, R-07 (10 Feb 2026): "Chilled dispatch: at least 4 pickers per shift" | Plan: Head of Logistics. BIA activity and R-07: Dispatch lead |
| 3 | Second carrier | §5: "Backup carrier: KuehlTrans, by spot booking." | BIA v2, B-A2: "carrier: NordFrost, no second carrier recorded". Register v5, R-08: "one carrier, NordFrost; second carrier open" | Plan: Head of Logistics. BIA activity: Dispatch lead. R-08: none named |
| 4 | LogiStock recovery time | §6: "Orders leave LogiStock by the manual export in work instruction WI-14." No restore time: not in the sources | Register v5, R-09: "LogiStock restored within 6 hours" | Plan: Head of Logistics. R-09: IT service owner |

The carrier escalation line agrees on both sides: plan §4 says "NordFrost control room" and BIA B-A2 says "carrier escalation: NordFrost control room". Block 2 covers it.

A plan changes only with its owner's approval and a new version.

## Block 2: What the trunking change reopens

**The change.** `change-trunking-supplier.md` (15 Sep 2026, planned): "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul" and "NordFrost's control room will no longer handle Site A loads from that date."

**Change trigger to keep:** when the chilled carrier changes, reopen the dispatch plan, the goods receipt plan, BIA entries B-A1 and B-A2, and register entry R-08.

| Document touched | Section (date) | Line quoted | Owner: proposed, to confirm |
|---|---|---|---|
| Chilled dispatch plan v3 | §4 Contacts (12 Mar 2026) | "Carrier escalation: NordFrost control room, 040 555 0900." | Head of Logistics |
| Chilled dispatch plan v3 | §5 Suppliers (12 Mar 2026) | "Trunking from Site A to Site B and outbound chilled transport: NordFrost. Backup carrier: KuehlTrans, by spot booking." | Head of Logistics |
| Goods receipt plan v2 | §3 Inbound transport (3 Mar 2026) | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Warehouse lead |
| BIA v2, B-A1 | Goods receipt, chilled (4 Feb 2026) | "carrier: NordFrost, inbound trunking from Site B" | Activity: Warehouse lead. BIA: BCM manager |
| BIA v2, B-A2 | Dispatch, chilled (4 Feb 2026) | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Activity: Dispatch lead. BIA: BCM manager |
| Register v5, R-08 | (10 Feb 2026) | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | none named |

- **Not touched:** the quality release plan v1. Its text says nothing about carriers or transport.
- **Polar Haul escalation contact:** to be confirmed. It's not in the sources.

## Gaps

- **R-08 has no owner.** Register v5, R-08 names none, and I haven't inferred one from a department or role.
- **The change notice has no version.** It is dated 15 September 2026 and its status is "planned, approved by the procurement board". It's raised by the Head of Procurement. I've read it as a planned change, not as current fact.
- **Polar Haul details are missing.** No contact, control room, contract date or second-carrier arrangement for Polar Haul appears in the sources.
- **The KuehlTrans backup is in the plan only.** It appears in plan §5 but not in BIA v2 or register v5, and the change notice doesn't say whether it continues after 1 January 2027.
- **Intake was skipped.** I've assumed the six attached files are the whole set.
- **No embedded instructions.** None of the attached documents contains text instructing an AI to act.

## Reviewer

The BCM manager who asked checks each quoted passage. Each plan owner and BIA activity owner decides whether their own document changes:
- **Block 1:** the Head of Logistics (plan) and the Dispatch lead (B-A2, R-07).
- **Block 2:** the Head of Logistics and the Warehouse lead (plans), the Dispatch lead and the Warehouse lead (B-A2, B-A1), and the BCM manager (BIA owner). R-08: none named.

## Coverage unknown

These kinds of document weren't attached, so I can't say whether the change reopens them:
- carrier and supplier contact lists
- escalation routes and call trees
- Site B plans
- a transport or crisis management plan
- the supplier register and carrier contracts
- work instruction WI-14
- the risk register

---

Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> Use review.md on plan-chilled-dispatch, with Head of Logistics: type /challenge-my-plan.

> Use review.md on plan-goods-receipt, with Warehouse lead: type /challenge-my-plan.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/keep-it-running.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/prompts/evaluations.md`
- Grep: `reopen|Typical AI uses`
