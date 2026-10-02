# /red-team-assumptions case 1, run3: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `136ddea8-44a1-413c-9c96-6837707b286f`.

Files in the working folder: `bia-extract-dispatch.md`, `option-paper-dispatch.md`, `supplier-record-nordfrost.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /red-team-assumptions The steering group meets tomorrow. The files option-paper-dispatch.md, bia-extract-dispatch.md and supplier-record-nordfrost.md in this folder are attached.

**Reply (verbatim):**

Before I open the three attachments, I need one thing from you.

**What class of data do these files hold, and is this environment approved for it?**

From the file names, they look like an option paper, a BIA extract and a supplier record. Under the guidance's sensitivity classes, those normally count as **high sensitivity**: BIA data, recovery strategies and design assumptions, supplier weaknesses and contractual dependencies, and possibly board or steering-group material. High-sensitivity data may only go into an approved corporate or private environment. Please confirm:

1. that this Claude Code session runs in an environment your organisation has approved for high-sensitivity BCM data, or tell me the class is lower than that and why, and
2. that the files contain no passwords, keys or access tokens. Those go into no tool, approved or not.

If the environment isn't approved for that class, I'll stop here and won't read the files.

**What happens after you confirm:** I'll read the three files and ask only the scope questions they leave open, such as which option or decision. Then I'll send one draft list of the assumptions the option depends on. Each assumption comes with the passage that relies on it, the check that would settle it, and a question for the person who should run that check. Nothing gets scored. The output is a draft in this chat only, and I won't edit, send or publish anything.

**Who reviews it:** the BCM manager who owns the option paper checks each assumption against its passage. Each check's owner answers their question. Finance or procurement checks the financial and commercial assumptions. The steering group, as the stakeholder group, makes the choice.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I read the three files and haven't changed or sent anything. The attachments set the scope: one option (moving chilled dispatch to Site B) and one decision (the steering group's choice on 2 Oct 2026). So I had no scope questions. The draft follows.

---

**Sources used**
- Option paper, chilled dispatch Site A: v1.2, 14 Aug 2026, status "draft for steering group" (see Gaps)
- Checked against the BIA extract, chilled dispatch: BIA v2, approved by top management 4 Feb 2026
- Supplier record NordFrost: dated 2 May 2026, status "current", **no version number** (see Gaps)

**Reviewer:** The BCM manager who owns the option paper checks each assumption against its passage. Each check's owner answers their question. Finance or procurement checks A5 and A9. The steering group owns the choice.

## The paper's strongest case

The option starts from a dated, approved need: "RTO for chilled dispatch is 8 hours", which matches BIA v2. It uses a site, a cold room, staff and a carrier the organisation already has, so it needs no new contract or new build before it can work. Site A's own shift leaders would run dispatch at Site B, so the people doing the work already know the activity. Site B is 140 km away, and nothing in the sources suggests that losing Hall 3 would affect Site B's premises.

## Load-bearing assumptions

The sources give no effort or cost for any check, so the order of checks is **unknown, for the reviewer**. The assumptions below follow the order of the paper.

**A1. Site B's spare cold room is free, and holds two days of Site A volume, on the day it is needed.**
- Passage: §3, "Site B's spare cold room holds two days' Site A volume."
- Fails if the room is smaller than that or Site B is already using it: Site A stock can't be held at Site B, and dispatch doesn't restart within 8 hours.
- Check: compare the room's usable capacity and its occupancy across the year, including Site B's peaks, with two days of Site A chilled volume.
- Owner: not named in the sources (see Gaps).
- Question: *What is the spare cold room's usable capacity, how much of it is free at Site B's busiest point, and how does that compare with two days of Site A chilled volume?*

**A2. Hall 3 is back, or more cold storage is found, within those two days.**
- Passage: §3 ("two days'") read with §2, which gives the move no end point.
- Fails if the loss lasts longer than two days: Site B fills up and chilled dispatch stops again.
- Check: the expected restoration time for Hall 3, and what the option does on day 3.
- Owner: not named in the sources (see Gaps).
- Question: *How long is Hall 3 expected to be out in the scenario this paper covers, and what carries chilled dispatch after day 2?*

**A3. Site A's shift leaders can and will drive 140 km to Site B, at any hour, and arrive in time to run dispatch.**
- Passage: §3, "Site A's shift leaders drive to Site B"; §2, "140 km away".
- Fails if they are unavailable, have no transport, or are held at Site A by the incident: nobody runs Site A's dispatch at Site B and the 8-hour RTO is missed.
- Check: ask the shift leaders directly, including who covers each shift and night-time callout.
- Owner: Site A's shift leaders (proposed, to confirm).
- Question: *If Hall 3 were lost at the start of tonight's shift, could you be at Site B and running dispatch within 8 hours, and who covers for anyone who can't?*

**A4. Site B has the operatives to pick, pack and load Site A's volume on top of its own.** This is not stated in the paper.
- Passage: §3 names only "Site A's shift leaders" as moving.
- Fails if Site B's own staff can't absorb the extra volume: orders are received at Site B but not shipped.
- Check: Site B's staffing against its own load plus Site A's volume.
- Owner: not named in the sources (see Gaps).
- Question: *Who picks, packs and loads Site A orders at Site B, and does Site B have those hours spare at its peak?*

**A5. NordFrost can collect Site A's volume from Site B within the RTO, without any recovery SLA.** For finance or procurement.
- Passages: §3, "Carrier "NordFrost" serves both sites."; supplier record, "No SLA for recovery support"; BIA, "no second carrier recorded".
- Fails if NordFrost lacks the vehicles or capacity to take the extra volume at Site B, or is itself disrupted: chilled dispatch can't leave Site B. The option also relies on the same carrier as the activity it protects. A NordFrost failure takes out both the normal route and the recovery route, and the BIA records no second carrier.
- Check: written confirmation from NordFrost of the capacity and lead time to move Site A volume to Site B, and whether the contract (which runs to 31 Dec 2027) obliges it to do so.
- Owner: NordFrost (proposed, to confirm), through procurement.
- Question: *Can NordFrost collect two days of Site A chilled volume at Site B within 8 hours of a call, at any hour, and is that commitment in the contract or anywhere else in writing?*

**A6. Site A orders can still be exported after Hall 3 is lost, and Site B's warehouse system imports them correctly in time.**
- Passage: §3, "Site B's warehouse system takes Site A orders after a manual export."
- Fails if the export depends on anything in Hall 3, or the manual export has never been run end to end or takes too long: Site B has no orders to work from.
- Check: an end-to-end test of the export and import, timed, with Hall 3 treated as unavailable.
- Owner: not named in the sources (see Gaps).
- Question: *Has the manual export of Site A orders into Site B's warehouse system been run end to end, how long did it take, and does it still work if Hall 3 and everything in it is gone?*

**A7. All the steps together fit inside 8 hours.**
- Passage: §2, "within 8 hours".
- Fails if the decision to invoke, the 140 km drive, the export and import, and NordFrost's rerouting add up to more than 8 hours: the RTO is missed. The BIA sets the outer limit at an MTPD of 24 hours.
- Check: an hour-by-hour timeline from the loss of Hall 3 to the first chilled dispatch from Site B, with the steps that have been exercised marked.
- Owner: not named in the sources (see Gaps).
- Question: *What is the timeline from loss of Hall 3 to first dispatch from Site B, and which steps in it have been tested?*

**A8. The chilled stock to be dispatched reaches Site B.** This is not stated in the paper.
- Passage: §2, "Move chilled dispatch to Site B"; §3, "Site A volume".
- Fails if the stock was lost in Hall 3 and inbound deliveries still go to Site A: Site B has orders but no product.
- Check: how inbound chilled goods are redirected to Site B, and how fast.
- Owner: not named in the sources (see Gaps).
- Question: *Where does Site B get the chilled stock for Site A's orders when Hall 3 is lost, and who redirects inbound deliveries?*

**A9. The option costs nothing extra.** For finance or procurement.
- Passage: §4, "no additional cost; uses existing capacity".
- Fails if activation brings travel, overtime, extra carrier charges, or the cost of keeping the cold room spare: the steering group chooses on a cost figure that is wrong.
- Check: the cost of one activation, and the cost of keeping the capacity free.
- Owner: not named in the sources (see Gaps).
- Question: *What would one activation cost (shift leaders' travel and overtime, any extra NordFrost charges, cold-room use), and what does it cost to keep Site B's cold room free for this purpose?*

## Suppliers the option needs

| Supplier | Own continuity plan shown? | Written SLA? | Second source? |
|---|---|---|---|
| NordFrost (carrier) | No: "No information on NordFrost's own continuity plan" (supplier record) | No recovery SLA: "No SLA for recovery support" (supplier record) | No: "no second carrier recorded" (BIA v2) |

The sources name no other supplier, including any provider of Site B's warehouse system. That is "not in the sources".

## What holds up, and why

- **RTO 8 hours, MTPD 24 hours.** §1 matches BIA v2, which is dated and approved by top management.
- **A NordFrost relationship exists at both sites past the decision date.** The contract runs "to 31 Dec 2027". This supports the carrier being there. It does not support recovery support, which is covered in A5.
- **The recovery site is separate from the lost hall.** Site B is 140 km away, and the sources give no reason to think a Hall 3 loss reaches it. The shared dependencies are the carrier (A5) and possibly the order data (A6), not the premises.
- **"Current arrangement has none"** (§1) gives the reason for the paper. No option outcome depends on it, but it has no source (see Gaps).

## Gaps

- **Draft source:** The option paper is v1.2, 14 Aug 2026, "draft for steering group". It is read here as the paper under review, not as an approved position.
- **No version:** The NordFrost supplier record is dated 2 May 2026 and marked "current", but has no version number.
- **No owner in the sources** for the checks in A1, A2, A4, A6, A7, A8 and A9. The paper names no author or owner either. Naming an owner for each check would settle this.
- **No owner confirmation:** The sources hold no confirmation from a named owner that the option would work. The design stage's minimum control requires one before the option stops being a proposal.
- **Residual risks:** The paper lists none, including the single carrier (A5). The minimum controls require residual risks to stay visible in the paper.
- **"Current arrangement has none":** not in the sources.
- **Expected duration of the Hall 3 loss:** not in the sources.
- **Whether Site A's order data or export tool depends on Hall 3:** not in the sources.
- **Inbound chilled supply route to Site B:** not in the sources.
- **Site B staffing, cold-room occupancy and the warehouse-system provider:** not in the sources.
- **Instructions aimed at an AI:** none found in the three files.

---

Parts of this document were drafted with AI support (red-team-assumptions, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
