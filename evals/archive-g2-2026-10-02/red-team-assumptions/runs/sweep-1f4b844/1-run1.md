# /red-team-assumptions case 1, run1: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `6daeb833-84f9-4315-a673-840e8bd068da`.

Files in the working folder: `bia-extract-dispatch.md`, `option-paper-dispatch.md`, `supplier-record-nordfrost.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /red-team-assumptions The steering group meets tomorrow. The files option-paper-dispatch.md, bia-extract-dispatch.md and supplier-record-nordfrost.md in this folder are attached.

**Reply (verbatim):**

Before I open the three attachments, one question about the data, since the files decide which environment they can go into.

**What class of data do `option-paper-dispatch.md`, `bia-extract-dispatch.md` and `supplier-record-nordfrost.md` hold, and is this environment approved for that class?**

From the file names, they probably contain high-sensitivity material: BIA data, a recovery strategy option and its design assumptions, and supplier weaknesses or contractual dependencies for Nordfrost. Under the AI4BCM data rules, that class may only be handled in an approved corporate or private environment. Please confirm one of these:

- **This environment is approved for high-sensitivity BCM data.** I'll read the files and continue.
- **It isn't approved, or you're not sure.** I'll stop here. You can run the skill again in an approved environment, or attach versions with the BIA figures, supplier weaknesses and contract terms removed.

Also tell me if any file holds passwords, keys or access tokens. Those can't go into any tool, so they'd need to be removed first.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Sources read**
- Option paper: recovery of chilled dispatch, Site A, v1.2, 14 Aug 2026, status "draft for steering group". It is a draft (see Gaps), but it is the paper under review.
- Compared against BIA v2, approved by top management 4 Feb 2026 (extract: chilled dispatch).
- Supplier record: NordFrost, dated 2 May 2026, status "current", no version number (see Gaps).

**Reviewer:** the BCM manager who owns the option paper checks each assumption against its passage. Each check's owner answers their question. Finance or procurement check the items marked for them. The steering group owns the choice on 2 Oct 2026.

**Scope:** the attachments set it: one option (§2, move chilled dispatch to Site B within 8 hours), one decision (§5), the whole paper. I asked no scope questions. This is a draft for the chat only. I haven't edited, recorded or approved anything, and I've rated no risks.

---

## Steelman

The paper starts from an approved requirement: "Required RTO for chilled dispatch is 8 hours", which matches BIA v2. It answers that requirement with existing assets: a second site, a spare cold room, staff who know the work, and a carrier already under contract. It also writes down what it rests on (§3) instead of hiding it. If the four §3 claims hold, dispatch could plausibly be running again within the RTO and well inside the 24-hour MTPD, without building new capacity.

## Load-bearing assumptions

The option's outcomes are: (a) chilled dispatch is running from Site B within 8 hours, (b) it keeps running for as long as Hall 3 is out, and (c) the steering group is told the option costs nothing extra. Each assumption below would break at least one of these.

**A1. Site B's cold room is spare and big enough when it's needed.**
Passage: §3, "Site B's spare cold room holds two days' Site A volume."
Fails if the room is already in use by Site B when Hall 3 is lost, or holds less than stated. Outcome (a) fails.
Check: a capacity and availability statement for the cold room across Site B's year.
Owner: not in the sources (see Gaps G4). Question: *"Is the cold room free in every week of the year, and does it hold two days of Site A chilled volume at the required temperature?"*

**A2. The arrangement only has to last two days.** This is unstated.
Passage: §3, "two days' Site A volume". The paper gives no expected duration for losing Hall 3.
Fails if Hall 3, or another replacement, isn't back within two days. Outcome (b) fails once the cold room is full.
Check: an estimate of how long it takes to restore Hall 3, or a named next step after day two.
Owner: not in the sources (G4). Question: *"How long would Hall 3 be out, and what happens on day three?"*

**A3. Chilled goods can be brought into Site B for Site A orders.** This is unstated.
Passage: §2, "Move chilled dispatch to Site B". The paper says nothing about where the stock to dispatch comes from once Hall 3 and its contents are lost.
Fails if inbound chilled stock can't be redirected to Site B in time. Outcome (a) fails, because there's nothing to dispatch.
Check: walk through how inbound deliveries would be redirected to Site B.
Owner: not in the sources (G4). Question: *"Who redirects inbound chilled deliveries to Site B, and how fast can that happen?"*

**A4. Site A's shift leaders can and will reach Site B in time, and they're enough.**
Passage: §3, "Site A's shift leaders drive to Site B." §2 gives the distance as "140 km away".
Fails if the shift leaders can't be reached or aren't available out of hours, won't make the trip, or can't run the work without more people. Site B's own staff aren't mentioned. Outcomes (a) and (b) fail.
Check: confirmation from the shift leaders, plus a list of who does the physical dispatch work at Site B.
Owner: Site A's shift leaders (proposed, to confirm). Question: *"Can you be called out and reach Site B, 140 km away, at any hour, and stay several days? Who else would you need there?"*

**A5. NordFrost can move Site A volume out of Site B within 8 hours.** For finance or procurement.
Passage: §3, "Carrier 'NordFrost' serves both sites." BIA: "carrier: NordFrost, no second carrier recorded". Supplier record: "No SLA for recovery support", "No information on NordFrost's own continuity plan."
The option relies on the same carrier as the activity it protects (design.md, Method step 4).
Fails if NordFrost has no spare capacity at Site B, can't reroute at short notice, or is hit by the same disruption. Outcome (a) fails, and there's no second carrier to fall back on.
Check: written confirmation from NordFrost of how much it can move from Site B and how fast, and of its own continuity arrangements.
Owner: finance or procurement, putting the question to NordFrost (proposed, to confirm). Question: *"Will NordFrost commit in writing to moving Site A's chilled volume from Site B within 8 hours of a call, and can it show its own continuity plan?"*

**A6. The manual export works when Hall 3 is lost.**
Passage: §3, "Site B's warehouse system takes Site A orders after a manual export."
Fails if the export depends on Site A systems or people affected by losing Hall 3, or if the export and import can't be done inside the 8 hours. Outcome (a) fails. Nothing in the sources says how current the exported orders have to be (G6).
Check: a timed trial export from Site A's system into Site B's warehouse system, run without Hall 3.
Owner: not in the sources (G4). Question: *"Where does the export run from? Has it been done end to end, and how long did it take?"*

**A7. The whole sequence fits inside 8 hours.**
Passage: §2, "within 8 hours". Nothing shows the separate steps (call-out, the 140 km drive, cold room readiness, stock in, the export, the carrier pickup) adding up to 8 hours or less.
Fails if the steps together take more than 8 hours. Outcome (a) misses the RTO.
Check: a timed walkthrough or exercise of the full sequence. The sources don't say whether one has been run (G5).
Owner: not in the sources (G4). Question: *"Has the full move to Site B been timed, and what was the end-to-end time?"*

**A8. There really is no extra cost.** For finance or procurement.
Passage: §4, "no additional cost; uses existing capacity".
Fails if travel, overtime or accommodation for the shift leaders, carrier rerouting charges, or the cost of Site B giving up its cold room have a price. Outcome (c) fails, and the steering group would be choosing on a wrong cost.
Check: a costed estimate for a two-day activation, and for a longer one.
Owner: finance or procurement (proposed, to confirm). Question: *"What would a two-day move to Site B cost in staff, travel, carrier and displaced Site B use, and is any of it already budgeted?"*

**Order of checks:** ordering unknown, for the reviewer. The sources state no effort or cost for any check.

## Suppliers the option needs

| Supplier | Own continuity plan shown? | Written SLA? | Second source? |
|---|---|---|---|
| NordFrost (carrier) | No: "No information on NordFrost's own continuity plan" (supplier record) | No: "No SLA for recovery support" (supplier record) | No: "no second carrier recorded" (BIA v2) |
| Warehouse system provider (§3) | not in the sources | not in the sources | not in the sources |

## What holds up

- **The gap is sourced and current.** §1's 8-hour RTO matches BIA v2, which top management approved on 4 Feb 2026.
- **The target is consistent.** 8 hours is inside the 24-hour MTPD (BIA v2), so meeting the RTO leaves headroom before the MTPD.
- **The carrier contract covers the decision horizon.** It runs "to 31 Dec 2027" (supplier record). That covers having a contract, not recovery support, which is A5.
- **The assumptions are visible.** §3 lists what the option rests on, as design.md Minimum controls asks.
- **The second site is separate.** Site B is 140 km away (§2), so a loss limited to Site A's Hall 3 shouldn't reach the site itself. The shared dependencies are the carrier (A5) and possibly the order system (A6), not the building.

## Gaps

- **G1.** The option paper v1.2, 14 Aug 2026, is "draft for steering group". It was read as the paper under review, not as an approved position.
- **G2.** The supplier record has a date (2 May 2026) and status ("current") but no version number.
- **G3.** The option paper names no owner or author. The reviewer role, the BCM manager who owns the paper, is not in the sources.
- **G4.** The checks for A1, A2, A3, A6 and A7 have no owner in the sources. Each needs a named owner (for example for Site B, operations or IT) before it can be answered. Their questions are written above.
- **G5.** Whether the option has ever been exercised or timed: not in the sources.
- **G6.** The paper lists no residual risks (design.md, Minimum controls). It doesn't say how up to date order data must be for the manual export: not in the sources.
- **G7.** Who owns accepting the risk of having no second carrier: not in the sources.
- **G8.** The sources record no answer to any of these checks ahead of the 2 Oct 2026 decision.
- No instructions addressed to an AI were found in the attachments.

---

> Parts of this document were drafted with AI support (/red-team-assumptions, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
