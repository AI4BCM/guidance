# check-against-bia baseline (no skill loaded), run1: Claude Code, guidance at 23ab607

`claude -p --setting-sources project --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `67c42e27-9f03-497f-936d-55d396dbc785`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Check the dispatch plan against the BIA, and tell me what the new trunking carrier from January touches. The files bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md, plan-quality-release.md and change-trunking-supplier.md in this folder are attached.

**Reply (verbatim):**

The dispatch plan doesn't meet the BIA on two points: its recovery time is too slow, and it staffs fewer pickers than required. The January carrier change also breaks contact details and actions in two plans, and the BIA itself is out of date. I only had the six files to work from; I didn't check anything outside them.

## 1. Dispatch plan vs BIA (entry B-A2, chilled dispatch)

| Item | BIA / register | Dispatch plan | Result |
|---|---|---|---|
| Time to resume (RTO) | 8 hours (B-A2) | 12 hours (§2) | **Gap.** The plan allows 4 hours more than the BIA. It is still inside the 24-hour maximum tolerable outage (MTPD), but the RTO is the target the plan has to meet. |
| Pickers per shift | At least 4 (B-A2, R-07) | 3 travel to Site B (§3) | **Gap.** One picker short per shift. |
| Carrier | NordFrost, "no second carrier recorded" (B-A2); R-08 says the second carrier is still open | NordFrost, with KuehlTrans as backup "by spot booking" (§5) | **Mismatch.** The plan relies on a backup the BIA and register don't recognise. A spot booking is also not a commitment, so it can't be counted as a second carrier until it's confirmed or contracted. One side has to be updated. |
| Carrier escalation | NordFrost control room | NordFrost control room, 040 555 0900 | Matches (until January, see below). |
| Warehouse system | LogiStock; R-09: restored within 6 hours | Manual export via WI-14 (§6) | Consistent. The 6-hour restore fits inside the 8-hour RTO. The plan describes a workaround and leaves the restore to the IT service owner, which is fine. |
| Owner | Activity owner: Dispatch lead | Plan owner: Head of Logistics | Not a defect, but the dispatch lead should at least review the plan. |

The plan (12 March) was approved after BIA v2 (4 February) and the register (10 February). It should already have picked up the 8-hour RTO and the 4-picker minimum.

## 2. What the January carrier change touches

From 1 January 2027, Polar Haul replaces NordFrost for trunking between Site A and Site B (both directions) and for outbound chilled transport from Site A. NordFrost's control room stops handling Site A loads.

**Directly affected:**
1. **BIA B-A2 (dispatch):** the carrier and the carrier escalation (NordFrost control room) both become wrong.
2. **BIA B-A1 (goods receipt):** "inbound trunking from Site B: NordFrost" becomes wrong.
3. **Register R-08:** names NordFrost as the only carrier and **has no owner**. That's the main risk: nobody is responsible for carrying this change through.
4. **Dispatch plan §4:** the escalation number 040 555 0900 stops working for Site A loads.
5. **Dispatch plan §5:** the named carrier becomes wrong. The recovery option itself (moving dispatch to Site B) depends on A-to-B trunking, so the new carrier has to be able to support it.
6. **Goods receipt plan §3:** the step where someone "asks NordFrost to hold inbound loads at Site B" would go to a carrier that no longer handles these loads. That step is also carried out by the **dispatch lead**, not the goods receipt plan's owner (the warehouse lead). That cross-plan dependency is easy to miss.

**Questions the change raises:**
- Does the Polar Haul contract cover recovery: moving dispatch to Site B at short notice, holding loads at Site B, and a 24/7 escalation contact? The change notice doesn't say.
- Does the KuehlTrans spot-booking backup still stand? If it does, R-08's "second carrier open" could finally be closed properly.
- The change came from procurement and doesn't mention business continuity. The BIA is owned by the BCM manager and approved by top management, so updating it needs that route.

**Not affected:** the quality release plan (B-A3, R-06). It has no carrier dependency.

## 3. Suggested actions (about 3 months left before 1 January)
1. Give R-08 an owner (probably the Head of Logistics or the dispatch lead) and tell the BCM manager about the change notice.
2. Update BIA B-A1 and B-A2 and register R-08 for Polar Haul, and decide whether KuehlTrans counts as the second carrier.
3. Revise the dispatch plan: get the recovery time to 8 hours or less, staff at least 4 pickers per shift, and update the §4 contact and §5 carrier, both effective 1 January 2027.
4. Revise goods receipt plan §3 so the hold-at-Site-B request goes to Polar Haul.
5. Check the Polar Haul contract against these recovery needs before it starts.

**Tool calls (stream-json):**

- Bash: `ls -la && for f in bia-extract-dispatch.md requirements-register.md plan-chilled-dispatch.md plan-goods-receipt.md plan-quality-release.md change-trunking-suppl`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/baseline/run1/work/bia-extract-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/baseline/run1/work/requirements-register.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/baseline/run1/work/plan-chilled-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/baseline/run1/work/plan-goods-receipt.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/baseline/run1/work/plan-quality-release.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/baseline/run1/work/change-trunking-supplier.md`
