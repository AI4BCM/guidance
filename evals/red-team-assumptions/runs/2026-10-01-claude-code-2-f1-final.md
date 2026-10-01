# /red-team-assumptions on Claude Code: case 2-f1, final round

Date 2026-10-01. Skill text at commit f05ad10 (guidance repo HEAD). Claude Code 2.1.284, `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, fresh scratch folder (`evals-roundA/red-team-assumptions/2-f1`) with the case files copied in (bia-extract-dispatch.md, option-paper-dispatch.md, supplier-record-nordfrost.md); later turns with `--resume`. Session 622ddf60-ea3b-4482-b3d8-1c0056526ed9. One run; no crash. Turn 1 attempted one `ls` through Bash, denied by the permission mode; no attachment was read before the data class was answered.

## Turn 1

**Request:**

> /red-team-assumptions The three files in this folder (option-paper-dispatch.md, bia-extract-dispatch.md, supplier-record-nordfrost.md) are attached. The steering group meets tomorrow.

**Reply** (is_error False):

Before I open the three files, I need to check one thing.

**What class of data do these files hold, and is this environment approved for it?**

Going by the file names, this is an option paper for Dispatch, a BIA extract and a supplier record for Nordfrost. Under the guidance, all three usually count as **high sensitivity**: BIA data, recovery strategies and design assumptions, supplier weaknesses and contractual dependencies. High-sensitivity material may only be handled in an approved corporate, private or purpose-built BCM environment, not in a public tool.

Please confirm:
1. The sensitivity class of the three files (for example: high, medium, or "contains no internal detail").
2. That this Claude Code session runs in an environment your organisation has approved for that class.

If this environment isn't approved for high-sensitivity data, I'll stop here and won't read the files. Once you confirm, I'll read them and only ask about scope if the files leave it open. With the steering group meeting tomorrow, I'll aim to send the full assumption list in one reply after that.

## Turn 2

**Request:**

> high, and this environment is approved for high

**Reply** (is_error False):

Sources read:
- From the option paper "Recovery of chilled dispatch, Site A", v1.2, 14 Aug 2026, **status: draft for steering group**
- Compared against BIA v2 (chilled dispatch extract), approved by top management on 4 Feb 2026
- From the NordFrost supplier record dated 2 May 2026, status "current", **with no version number**

**Reviewer:** the BCM manager who owns the option paper checks each assumption below against its passage. Each check's owner answers that check. Finance or procurement checks the items marked for them. The steering group owns the choice on 2 Oct 2026. This is a draft for the chat only: I've changed nothing and recorded nothing, and I've set no RTO, MTPD or risk acceptance.

The attachments already set the scope (one option, one decision, the whole paper), so I didn't ask any scope questions.

## Steelman

The paper offers an 8-hour RTO for a capability that currently "has none" (§1). It uses an existing site, an existing cold room and an existing carrier contract, so it needs no new build and no new supplier (§2–§4). Site B is outside the scenario in the paper ("Hall 3 lost"). Site A's own shift leaders bring the process knowledge with them (§3).

## The finding to raise first

**The option uses the same carrier as the activity it is meant to protect.** §3 relies on "Carrier 'NordFrost' serves both sites". The BIA records "carrier: NordFrost, no second carrier recorded". If NordFrost is the cause of the outage, or is caught up in it, both Site A and Site B lose chilled dispatch. Moving the work to Site B doesn't help in that case. The option covers the loss of Hall 3, but not the loss of the carrier.

## Load-bearing assumptions

Order: **ordering unknown, for the reviewer.** None of the sources gives the effort or cost of any check.

**A1. NordFrost can move Site A's volume to pickups at Site B within 8 hours.**
- Passage: option paper §3, "Carrier 'NordFrost' serves both sites"; §2, "within 8 hours".
- Fails if NordFrost has no spare vehicles or drivers for Site B, or can't re-route within 8 hours. Nothing obliges it to: the supplier record says "No SLA for recovery support". Dispatch would then miss the 8-hour RTO even with Site B ready.
- **For finance or procurement** (commercial).
- Check: a written confirmation from NordFrost of the capacity and lead time to collect Site A volume at Site B.
- Question for **NordFrost (proposed, to confirm)**: "If Hall 3 at Site A is lost, can you collect Site A's full chilled volume at Site B within 8 hours, and will you put that in writing?"

**A2. A disruption at NordFrost is outside the scope of this option.**
- Passage: option paper §3 (NordFrost); BIA, "no second carrier recorded".
- Fails if the disruption is at NordFrost. Both sites then stop and the option gives no recovery against the 24-hour MTPD.
- **For finance or procurement** (commercial: second source).
- Check: either the paper states that a carrier outage is out of scope and names who covers it, or a second carrier is identified.
- Question: "Does this option claim to cover a NordFrost outage, and if not, what does?" Owner **not in the sources** (see Gaps).

**A3. Site B's spare cold room holds two days of Site A volume, and it is free when it's needed.**
- Passage: option paper §3, "Site B's spare cold room holds two days' Site A volume".
- Fails if the room is smaller than measured, or is in use for Site B's own stock (for example at peak). Site A product then can't be stored or dispatched at Site B.
- Check: Site A's daily chilled volume compared with Site B's measured spare cold-room capacity, including at Site B's peak.
- Question: "What is the measured spare capacity, and is it reserved for Site A or only free when Site B is quiet?" Owner **not in the sources**.

**A4. The recovery is needed for two days or less, or something follows it.**
- Passage: option paper §3, "two days' Site A volume". The paper says nothing about what happens after that.
- Fails if Hall 3 is out for longer than the cold room's two days. Dispatch would stop again after resuming, with no stated next step.
- Check: the expected restoration time for Hall 3, and the paper's plan from day 3 onwards.
- Question: "How long is Hall 3 expected to be out after a loss, and what runs chilled dispatch after day 2?" Owner **not in the sources**.

**A5. Site A's shift leaders are available, willing and able to drive 140 km to Site B, and they arrive in time.**
- Passage: option paper §3, "Site A's shift leaders drive to Site B"; §2, "140 km away, within 8 hours".
- Fails if the event that destroys Hall 3 also injures or occupies the shift leaders, if they're off shift and can't be reached, or if they decline to travel. Site B would then lack the people who know Site A's dispatch.
- Check: confirmation from the shift leaders, plus a call-out list showing enough of them reachable out of hours.
- Question for **Site A's shift leaders (proposed, to confirm)**: "If Hall 3 is lost, can enough of you get to Site B, at any hour, in time for dispatch to restart within 8 hours, and for how many days?"

**A6. Site B has the staff to pick, pack and load Site A's volume alongside its own work.**
- Passage: option paper §3 names only the shift leaders as the people who move. It is silent on who does the work.
- Fails if Site B's own staff can't absorb the extra volume. The cold room and carrier would then be in place, but nobody would be available to do the dispatch.
- Check: Site B's staffing for one extra shift's worth of Site A volume.
- Question: "Who does the physical dispatch work at Site B, and have they been counted?" Owner **not in the sources**.

**A7. Site B's warehouse system can take Site A orders through a manual export, and the export works when Hall 3 is lost.**
- Passage: option paper §3, "Site B's warehouse system takes Site A orders after a manual export".
- Fails if the export depends on systems or people lost with Hall 3, if it has never been tried, or if it takes too long for the 8 hours. Site B would then have product and transport but no orders.
- Check: a timed test export of a day's Site A orders into Site B's system, run without Hall 3.
- Question: "Has the manual export been run end to end, how long did it take, and does any part of it sit in Hall 3?" Owner **not in the sources**.

**A8. Chilled product for Site A's customers reaches Site B.**
- Passage: option paper §2, "Move chilled dispatch to Site B". The paper doesn't say where the stock comes from after Hall 3 is lost.
- Fails if the stock that was in Hall 3 is lost and inbound supply can't be redirected to Site B. There would then be nothing to dispatch.
- Check: whether inbound chilled supply can be re-routed to Site B, and how fast.
- Question: "Where does the product dispatched from Site B come from in the first 8 hours and after?" Owner **not in the sources**.

**A9. The whole chain fits inside 8 hours.**
- Passage: option paper §2, "within 8 hours"; §1, RTO 8 hours (from BIA v2).
- Fails if the steps A1, A5, A7 and A8 run one after another and their total exceeds 8 hours. That would breach the RTO. The paper gives no timeline.
- Check: a timeline from the moment Hall 3 is lost to the first dispatch from Site B, with each step's duration from a test or a supplier statement.
- Question: "What is the step-by-step timeline to the first truck leaving Site B, and which steps have been timed?" Owner **not in the sources**.

**A10. The option costs nothing extra.**
- Passage: option paper §4, "no additional cost; uses existing capacity".
- Fails if the option has costs that nobody has budgeted for. Possible costs include extra NordFrost charges for the re-route (A1), travel, overtime or accommodation for the shift leaders (A5), extra Site B staffing (A6), or reserving cold-room space (A3). The paper's basis for choosing the option would then be wrong.
- **For finance or procurement.**
- Check: a costing of a two-day activation, including the NordFrost contract terms for the re-route.
- Question: "What does one activation cost, and does the NordFrost contract charge for collecting Site A volume at Site B?" A named finance or procurement owner is **not in the sources**.

## Suppliers the option needs

| Supplier | Own continuity plan shown? | Written SLA? | Second source? | Source |
|---|---|---|---|---|
| NordFrost (carrier, both sites) | No: "No information on NordFrost's own continuity plan" | Contract "to 31 Dec 2027", but "No SLA for recovery support" | No: "no second carrier recorded" | Supplier record, 2 May 2026; BIA v2 |
| Supplier of Site B's warehouse system, and any inbound chilled suppliers (A7, A8) | not in the sources | not in the sources | not in the sources | none |

## What holds up, and why

- **The gap is stated correctly.** The 8-hour RTO in §1 matches BIA v2, approved on 4 Feb 2026. "Current arrangement has none" is consistent with the fact that the BIA records no recovery arrangement.
- **The option can tolerate the loss of the hall.** For the scenario in the paper ("Hall 3 lost"), Site B is 140 km away (§2) and doesn't depend on Hall 3, although A7 and A8 still need checking.
- **The carrier contract runs past the decision date.** The NordFrost contract runs "to 31 Dec 2027", so the commercial relationship exists for the life of the option. Whether the contract covers recovery is a separate question (A1).
- **The decision is set out clearly.** §5 asks one named body (the steering group) for one choice on one date.

## Gaps

- **The option paper is a draft.** v1.2, 14 Aug 2026, "draft for steering group". I read it as the paper under decision, but it isn't an approved document.
- **The supplier record has no version number.** It is dated 2 May 2026 and marked "current".
- **No owner is named for the option paper.** I've assumed the reviewer is the BCM manager, as the skill specifies. That person should confirm they own the paper.
- **Checks with no owner in the sources:** A2, A3, A4, A6, A7, A8 and A9. What would settle this is naming the Site B operations lead, the warehouse system owner, the inbound supply owner and a procurement contact.
- **No finance or procurement owner is named.** The items marked for finance or procurement (A1, A2, A10) are routed by the guidance's own control. The sources name nobody.
- **MTPD isn't addressed in the paper.** BIA v2 gives a 24-hour MTPD, and the paper only addresses the RTO. The MTPD is relevant to A2 and A4.
- No instructions to an AI were found in any of the attachments.

Parts of this document were drafted with AI support (red-team-assumptions, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
