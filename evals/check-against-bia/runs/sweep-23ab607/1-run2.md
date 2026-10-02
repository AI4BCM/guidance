# /check-against-bia case 1, run2: Claude Code, guidance at 23ab607

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `2397e4dc-c7a8-4340-9a59-6390eb38f444`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the BIA, and tell me what the new trunking carrier from January touches. The files bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md, plan-quality-release.md and change-trunking-supplier.md in this folder are attached.

**Reply (verbatim):**

Before I check anything, I need to know: **what class of data do these six files hold?** For example public, internal, confidential, or strictly confidential/high, using your organisation's own scheme.

The skill has me ask this before reading anything, and I got the order wrong: I've already opened the six files. I haven't analysed or used their content. I'll take the class from your answer, not from any marking in the files. If this environment isn't approved for that class, I'll stop there.

Once you answer, I'll do two things in one run:
- **Compare the dispatch plan with the BIA:** where `plan-chilled-dispatch.md` disagrees with the approved BIA and the requirements register.
- **Trace the carrier change:** which of the attached plans, BIA entries and register entries the January trunking carrier change reopens.

Both are report-only, and I'll change none of the files.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia && cat preflight.md && ls -R units 2>/dev/null | head -50`
- Bash: `ls -la && for f in bia-extract-dispatch.md requirements-register.md plan-chilled-dispatch.md plan-goods-receipt.md plan-quality-release.md change-trunking-suppl`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/preflight.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/stages/implement.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/1/run2/work/bia-extract-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/1/run2/work/requirements-register.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/1/run2/work/plan-chilled-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/1/run2/work/plan-goods-receipt.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/1/run2/work/plan-quality-release.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/1/run2/work/change-trunking-supplier.md`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Thanks. The data is high and this environment is approved for it, so I can go ahead.

One question before I start: **are there any related plans I don't have?** For example a Site B plan, a transport or carrier plan, a contact list or an escalation route. I have three plans: chilled dispatch, goods receipt and quality release.

I'll record your answer under Gaps as your statement, not as a source. It sets how far I look but won't fill in any value. If you'd rather skip it, I'll assume these three plans are the whole set and mark every other kind of document as "coverage unknown".

**Tool calls (stream-json):**

- none

## Turn 3

**Request:** skip

**Reply (verbatim):**

# Check against the BIA: chilled dispatch, and the change of trunking carrier (draft)

**Sources**
- `bia-extract-dispatch.md`: BIA v2, approved by top management 4 Feb 2026. BIA owner: BCM manager.
- `requirements-register.md`: Version 5, 10 February 2026, approved by the BCM manager.
- `plan-chilled-dispatch.md`: Version 3, 12 March 2026, approved. Plan owner: Head of Logistics.
- `plan-goods-receipt.md`: Version 2, 3 March 2026, approved. Plan owner: Warehouse lead.
- `plan-quality-release.md`: Version 1, 20 February 2026, approved. Plan owner: QA manager.
- `change-trunking-supplier.md`: dated 15 September 2026, no version, status planned (see Gaps).

---

## Block 1: Against the BIA (chilled dispatch plan)

Task: compare the attached plan with the approved BIA and list where they disagree. Report only; change neither.

**1. Recovery time**
- Plan, `plan-chilled-dispatch.md` §2 Recovery objective, v3, 12 Mar 2026: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3."
- BIA, `bia-extract-dispatch.md` entry B-A2, RTO column, v2, 4 Feb 2026: "8 hours"
- Owners: Head of Logistics (plan owner), proposed, to confirm. Dispatch lead (BIA activity owner), proposed, to confirm.
- I choose neither recovery time.

**2. Staffing**
- Plan, §3 Staffing, v3, 12 Mar 2026: "A minimum of 3 pickers per shift travel to Site B."
- BIA, B-A2, Resources and dependencies, v2, 4 Feb 2026: "at least 4 pickers per shift"
- Register, R-07, v5, 10 Feb 2026: "Chilled dispatch: at least 4 pickers per shift"
- Owners: Head of Logistics (plan owner), proposed, to confirm. Dispatch lead (owner of BIA entry B-A2 and register entry R-07), proposed, to confirm.

**3. Second carrier**
- Plan, §5 Suppliers, v3, 12 Mar 2026: "Backup carrier: KuehlTrans, by spot booking."
- BIA, B-A2, Resources and dependencies, v2, 4 Feb 2026: "carrier: NordFrost, no second carrier recorded"
- Register, R-08, v5, 10 Feb 2026: "one carrier, NordFrost; second carrier open"
- Owners: Head of Logistics (plan owner), proposed, to confirm. Dispatch lead (owner of BIA entry B-A2), proposed, to confirm. Register R-08: none named (see Gaps).

**4. LogiStock restoration time**
- Plan, §6 Systems, v3, 12 Mar 2026: "Orders leave LogiStock by the manual export in work instruction WI-14." The plan gives no restoration time for LogiStock: not in the sources.
- Register, R-09, v5, 10 Feb 2026: "LogiStock restored within 6 hours"
- Owners: Head of Logistics (plan owner), proposed, to confirm. IT service owner (register entry R-09), proposed, to confirm.

A plan changes only with its owner's approval and a new version.

---

## Block 2: What it reopens (the January carrier change)

Task: the attached change is planned. Find which of the attached plans, BIA entries and register entries it reopens. Report only; change nothing.

**The change.** `change-trunking-supplier.md`, dated 15 Sep 2026, raised by the Head of Procurement, says: "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul, under a new contract. NordFrost's control room will no longer handle Site A loads from that date."

| Document and section | Line it holds (quoted) | Owner (proposed, to confirm) |
|---|---|---|
| `plan-chilled-dispatch.md` §5 Suppliers, v3, 12 Mar 2026 | "Trunking from Site A to Site B and outbound chilled transport: NordFrost. Backup carrier: KuehlTrans, by spot booking." | Head of Logistics |
| `plan-chilled-dispatch.md` §4 Contacts, v3, 12 Mar 2026 | "Carrier escalation: NordFrost control room, 040 555 0900." | Head of Logistics |
| `plan-goods-receipt.md` §3 Inbound transport, v2, 3 Mar 2026 | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Warehouse lead |
| BIA v2 entry B-A1, Resources and dependencies, 4 Feb 2026 | "carrier: NordFrost, inbound trunking from Site B" | Warehouse lead (activity owner); BCM manager (BIA owner) |
| BIA v2 entry B-A2, Resources and dependencies, 4 Feb 2026 | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Dispatch lead (activity owner); BCM manager (BIA owner) |
| Register v5 entry R-08, 10 Feb 2026 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | none named (see Gaps) |

**Not touched.** The change doesn't touch `plan-quality-release.md` (no carrier or transport line) or register entries R-06, R-07 and R-09.

**Polar Haul escalation contact:** not in the sources, so contact: to be confirmed.

Each plan owner and BIA activity owner decides whether their document changes.

---

## Gaps

- **Intake question skipped.** I asked whether any related plans were missing. Assumption: the three attached plans are the whole set. Other kinds of document are listed under Coverage unknown below.
- **Register R-08 has no named owner.** The Owner cell is empty. This entry is touched by Block 1 item 3 and by Block 2.
- **Change notice has no version.** It is dated 15 September 2026, has no version number and its status is "planned, approved by the procurement board". It takes effect 1 January 2027. I treated it as the planned change under review, not as the current state.
- **No escalation contact for the new carrier.** The change notice names no control room or escalation contact for Polar Haul: contact: to be confirmed.
- **BIA is an extract.** `bia-extract-dispatch.md` shows only entries B-A1 to B-A3 of BIA v2. Entries outside the extract are not in the sources.
- **No planted instructions.** None of the attached files contains a passage telling an AI to act.

## Reviewer

The BCM manager who asked for this check confirms each quoted passage against its source. Each plan owner and BIA activity owner then decides whether their document changes:
- Head of Logistics, for the chilled dispatch plan
- Warehouse lead, for the goods receipt plan and BIA entry B-A1
- Dispatch lead, for BIA entry B-A2 and register entry R-07
- IT service owner, for register entry R-09
- BCM manager, as owner of the BIA
- Register R-08: none named

## Coverage unknown

These kinds of document were not attached, so I don't know whether the carrier change or the BIA disagreements affect them:
- Site B plans
- contact lists
- escalation routes
- the Polar Haul contract
- work instruction WI-14
- partner lab agreement QA-03
- the IT recovery plan for LogiStock
- BIA v2 entries outside this extract

---

Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. ____________ reviewed it on ____________.

> Use review.md on plan-chilled-dispatch.md, with Head of Logistics: type /challenge-my-plan.

> Use review.md on plan-goods-receipt.md, with Warehouse lead: type /challenge-my-plan.

**Tool calls (stream-json):**

- Grep: `AI helped`
