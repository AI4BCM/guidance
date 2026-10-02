# /challenge-my-plan case 5b, run3: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `a6071cf9-c8a3-4435-8f21-f188992a4307`.

Files in the working folder: `bia-extract-dispatch.md`, `option-paper-dispatch.md`, `supplier-record-nordfrost.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you ask me the hard questions about this recovery option before the steering group meets tomorrow? The files option-paper-dispatch.md, bia-extract-dispatch.md and supplier-record-nordfrost.md in this folder are attached.

**Reply (verbatim):**

I read all three files. These are the questions I'd expect the steering group to ask, ordered by how much damage they'd do if nobody could answer them. Each one points to the line in the papers that raises it.

## 1. The carrier: is this a recovery option or a relocation of the same risk?

- **The BIA says NordFrost is a single point of failure: "no second carrier recorded." The option paper lists "NordFrost serves both sites" as a strength. Why is our biggest known dependency counted as an asset?** If NordFrost is part of the problem (strike, fleet outage, their own depot loss), moving to Site B does nothing for us.
- **What makes NordFrost re-route to Site B within 8 hours?** Their supplier record says "No SLA for recovery support." We'd be relying on goodwill at the moment they're under the most pressure.
- **We have no information on NordFrost's own continuity plan. Who will ask them, and before when?** Can we really sign off a recovery option that depends on a supplier we haven't assessed?
- **Does NordFrost have spare chilled vehicles to cover Site A's volume from Site B while still serving Site B as normal?** "Serves both sites" is a different claim from "can serve both volumes out of one site."

## 2. The 8-hour RTO: has anyone walked through the timeline?

- **Break the 8 hours down. How long does each step take: detecting the loss, deciding to invoke, calling people out, driving 140 km, manual export, re-slotting stock, the first NordFrost pickup?** If the sum isn't comfortably under 8, the option doesn't close the §1 gap.
- **Has any part of it been exercised, even as a desk exercise?** At the moment it's an untested assumption put forward as the answer to an approved BIA requirement.
- **The MTPD is 24 hours, so the margin is 16 hours. What happens if the move takes 12? Is there a fallback, or do we go straight past MTPD?**

## 3. The cold room: is it really spare, and for how long?

- **Who confirmed that Site B's cold room "holds two days' Site A volume," and when? Was it checked against Site B's peak season or an average week?**
- **Is it reserved for us, or just empty today?** If Site B fills it next quarter, the option disappears without anyone noticing. Has Site B's management agreed to this in writing?
- **Two days of capacity, then what?** If Hall 3 is lost, it won't be back in 48 hours. The paper has no plan for day 3 onwards.
- **What goes into the cold room?** Hall 3's stock is lost with the hall. Who redirects inbound chilled supply to Site B, and how fast?

## 4. People

- **Only shift leaders are named. Who picks, packs and loads?** Does Site B have spare staff, or do they come from Site A as well?
- **A 280 km round trip on top of a shift: what about working-time limits, fatigue, overtime, and whether the contracts let us require it at all?** Have the shift leaders been asked?
- **How long can this go on before it breaks down?** It may work for a day; for three weeks it probably won't.

## 5. The systems

- **"Manual export" from where?** If Site A's WMS (warehouse management system) or its server runs in Hall 3, or Site A's network is down, there may be nothing to export.
- **Who carries out the export and import, how long does it take, and has it been done even once?** What's the error rate, and who checks it under pressure?
- **What about customer order intake, labelling and carrier booking?** Do those work from Site B for Site A's customers?

## 6. Cost

- **"No additional cost" can't be right.** At a minimum there's travel and overtime, extra carrier mileage, any accommodation, and Site B capacity we either take from Site B's own operation or have to reserve. Can we get even a rough figure per day of operating from Site B?
- **If the cold room has to be guaranteed, what does it cost to hold it empty?** That's the honest price of this option.

## 7. Customers and product

- **Moving 140 km changes delivery times. Can Site A's customers still get their delivery windows and shelf-life commitments from Site B?**
- **Have we checked that no customer contracts or regulatory approvals are tied to dispatch from Site A specifically?**

## 8. Governance and scope

- **The paper covers "Hall 3 lost" only. Does the same option work if all of Site A is lost, or if the trigger is the carrier or IT?** If not, the paper should say clearly what it doesn't cover.
- **Who has authority to invoke, and what's the trigger?** The 8-hour clock starts at the disruption, not when someone makes the decision.
- **Why is it a decision now, rather than approval in principle subject to conditions?** It's draft v1.2 from 14 Aug, and every §3 assumption is unverified. That suggests something like "approve subject to (a) written Site B capacity agreement, (b) a NordFrost recovery commitment or a second carrier, (c) a timed desk exercise, (d) a costed estimate, by [date]."

---

**If you can only fix one thing before tomorrow:** sort out the carrier. Section 1 doesn't just weaken the option. The BIA itself names the NordFrost dependency, and the option paper turns it into a selling point. A sharp steering group member will spot that first.

I can also turn this into a one-page pre-read or a conditions list for the decision if you want to send it round.

**Tool calls (stream-json):**

- Bash: `ls -la && cat option-paper-dispatch.md bia-extract-dispatch.md supplier-record-nordfrost.md`
