# /red-team-assumptions case 1, run2: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `a5d35cce-2b0b-418d-924a-a899b7f773e3`.

Files in the working folder: `bia-extract-dispatch.md`, `option-paper-dispatch.md`, `supplier-record-nordfrost.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /red-team-assumptions The steering group meets tomorrow. The files option-paper-dispatch.md, bia-extract-dispatch.md and supplier-record-nordfrost.md in this folder are attached.

**Reply (verbatim):**

Before I open the three files: what class of data do they hold, and is this environment approved for that class?

Going by the filenames, they probably include:
- **BIA data** (`bia-extract-dispatch.md`)
- **recovery strategies and design assumptions** (`option-paper-dispatch.md`)
- **supplier weaknesses and contractual dependencies** (`supplier-record-nordfrost.md`)

Under `units/data-rules.md`, all three of those are **high sensitivity**. Option and supplier work at the Design stage may only run in an **enterprise, private or approved platform** (`units/tools.md`, Selection guide).

Please confirm two things:
1. The class of the data in these files: high, or lower than the filenames suggest.
2. That this Claude Code environment is approved for that class. That means its retention, access and contract terms have been checked under *Before you approve a tool* in `units/tools.md`.

If it isn't approved for high-sensitivity data, I'll stop here and won't read the files. If it is, I'll read them, then ask only the scope questions the files leave open. You'll still have the list before tomorrow's steering group.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

From option paper v1.2, 14 Aug 2026 (status: draft for steering group)
Compared against BIA extract, BIA v2, approved by top management 4 Feb 2026
Supplier record NordFrost, 2 May 2026, status current (no version number; listed under Gaps)

**Reviewer:** the BCM manager who owns the option paper checks each assumption against its passage. Each check's owner answers their check. Finance or procurement checks the items marked for them. The steering group makes the choice on 2 Oct 2026. This is a draft for review: I have changed nothing and rated nothing.

I asked no scope questions because the attachments already set the scope. There is one option (move chilled dispatch to Site B) and one decision (§5, steering group, 2 Oct 2026).

## Steelman

The paper starts from an approved requirement: an 8-hour RTO from BIA v2 (§1). It answers that requirement with capacity, people and a carrier the organisation already has (§3), at "no additional cost" (§4). Site B is 140 km away, so losing Hall 3 at Site A is unlikely to affect it as well. Under the paper's own logic the option is quick, cheap and uses known parts.

## Assumptions the option rests on

All the checks below are in the order they appear in the paper. The sources give no effort or cost for any check, so the order of work is unknown and left for the reviewer.

**A1. Site B's cold room is free and big enough when it is needed.**
- **Passage:** §3, "Site B's spare cold room holds two days' Site A volume."
- **Fails if** the room is smaller than that, or Site B is already using it (for example at a seasonal peak). Site A's chilled volume then has nowhere to go and dispatch does not resume.
- **Check:** measure the free capacity against Site A's daily chilled volume on Site B's busiest days.
- **Question for the owner:** *"Can Site B guarantee room for two days of Site A's chilled volume at any time of year, at 8 hours' notice?"* No Site B owner is named in the sources (see Gaps).

**A2. The disruption ends, or a next step starts, before the two days are up.**
- **Passage:** §3, "two days' Site A volume". The paper says nothing about what happens after two days.
- **Fails if** Hall 3 stays out of action for longer than the cold room's capacity covers. Dispatch would stop again after two days, with no further arrangement.
- **Check:** compare the expected time to restore Hall 3, or to set up a longer-term fallback, against the two-day capacity.
- **Question for the owner:** *"What happens to chilled dispatch on day three if Hall 3 is still lost?"* For the paper's owner, who is not named (see Gaps).

**A3. Chilled stock can reach Site B.**
- **Passage:** §2, "Move chilled dispatch to Site B". The paper doesn't say where the stock comes from. This premise is not in the sources.
- **Fails if** the stock is lost along with Hall 3, or inbound deliveries can't be redirected to Site B within 8 hours. Site B would then have nothing to dispatch.
- **Check:** trace the inbound flow for Site A's chilled products and confirm it can be redirected to Site B within 8 hours.
- **Question for the owner:** *"If Hall 3 is lost, where does the product Site B dispatches come from, and how fast can it get there?"* No owner is named in the sources (see Gaps).

**A4. Site A's shift leaders can get to Site B in time, at any hour.**
- **Passage:** §3, "Site A's shift leaders drive to Site B."
- **Fails if** the shift leaders can't be reached, have no transport, or aren't able or obliged to work 140 km away. The 8-hour RTO would then be missed.
- **Check:** confirm a call-out list, travel time and willingness for every shift, including nights and weekends. Also check whether employment terms allow the redeployment. HR is not in the sources.
- **Question for the owner:** *"Can each of you be at Site B within the 8 hours, on any shift, and do your terms allow it?"* For Site A's shift leaders (proposed, to confirm).

**A5. Site B has enough staff to handle Site A's volume as well as its own.**
- **Passage:** §3 moves only the shift leaders. The paper doesn't say who picks, packs and loads. This premise is not in the sources.
- **Fails if** Site B's staff can't absorb the extra volume. Shift leaders without staff to lead can't run dispatch.
- **Check:** compare Site B's spare staff hours against the labour that Site A's chilled volume needs.
- **Question for the owner:** *"Who does the physical dispatch work at Site B, and are there enough of them?"* No owner is named in the sources (see Gaps).

**A6. NordFrost can switch collections to Site B within 8 hours, with no recovery SLA.** For finance or procurement.
- **Passage:** §3, "Carrier 'NordFrost' serves both sites". The supplier record says "No SLA for recovery support."
- **Fails if** NordFrost won't, or can't, move vehicles and routes to Site B within 8 hours. Nothing in writing obliges it to.
- **Check:** ask NordFrost for written confirmation of the lead time and capacity for the switch, and review the contract terms.
- **Question for the owner:** *"Will NordFrost commit in writing to collecting Site A's chilled volume at Site B within 8 hours, and on what terms?"* For NordFrost (proposed, to confirm), through procurement.

**A7. NordFrost isn't hit by the same disruption.** This is a requirement the option shares with what it is meant to protect.
- **Passage:** §3, "Carrier 'NordFrost' serves both sites". BIA v2 says "no second carrier recorded". The supplier record says "No information on NordFrost's own continuity plan."
- **Fails if** NordFrost itself is disrupted, whether on its own or by the same event. Chilled dispatch then stops at both sites, and moving to Site B gains nothing.
- **Check:** get NordFrost's continuity plan and find out whether any second carrier can be engaged.
- **Questions for the owners:**
  - For NordFrost (proposed, to confirm): *"Do you have a continuity plan that covers your service to both our sites, and can we see it?"*
  - For procurement (proposed, to confirm): *"Is a second carrier available?"*

**A8. Site B's warehouse system can take Site A's orders within 8 hours.**
- **Passage:** §3, "Site B's warehouse system takes Site A orders after a manual export."
- **Fails if** the export can't be run with Hall 3 lost, takes too long, or produces data Site B's system rejects. Orders then don't reach the place doing the dispatch.
- **Check:** time a test of the manual export and import, from a location other than Hall 3, including the product and customer data.
- **Question for the owner:** *"Has the manual export into Site B's system been tested, and how long does it take?"* No owner is named in the sources (see Gaps).

**A9. All the steps together fit inside 8 hours.**
- **Passage:** §2, "within 8 hours". This depends on A1, A3, A4, A5, A6 and A8 all happening in time.
- **Fails if** the steps add up to more than 8 hours. The RTO from BIA v2 is then missed, and the 24-hour MTPD gets closer.
- **Check:** lay out a timed sequence of the steps, then run a walkthrough or exercise. The sources contain no evidence that either has been done.
- **Question for the owner:** *"What is the end-to-end time, step by step, and has it been exercised?"* For the paper's owner, who is not named (see Gaps).

**A10. The option costs nothing extra.** For finance or procurement.
- **Passage:** §4, "no additional cost; uses existing capacity".
- **Fails if** any of these turn out to cost money: NordFrost charging for rerouting or longer distances (A6), travel, overtime or accommodation for the shift leaders (A4), extra labour at Site B (A5), or Site B's own volume being pushed out of the cold room (A1). The cost basis the steering group is being asked to decide on would then be wrong.
- **Check:** cost each of those items for the two-day window and for a longer one.
- **Question for the owner:** *"Does 'no additional cost' still hold once carrier, travel, overtime and lost Site B capacity are priced?"* For finance or procurement.

## Suppliers the option needs

| Supplier | Own continuity plan | Written SLA | Second source |
|---|---|---|---|
| NordFrost (§3) | Not shown: "No information on NordFrost's own continuity plan" (supplier record) | Contract to 31 Dec 2027, but "No SLA for recovery support" (supplier record) | None: "no second carrier recorded" (BIA v2) |

The sources name no other supplier. Any supplier behind Site B's warehouse system or the manual export is not in the sources.

## What holds up

- **The required RTO:** the 8 hours in §1 matches BIA v2, which is approved and dated.
- **The gap is stated:** §1 sets the required outcome against the current arrangement and cites the BIA, as Method step 1 asks.
- **The carrier contract covers the decision date:** it runs to 31 Dec 2027. This does not settle A6 or A7.
- **Distance from the event:** 140 km of separation (§2) makes it unlikely that losing Hall 3 also affects Site B's premises. This does not cover the shared carrier (A7).

## Gaps

- **The option paper is a draft:** v1.2, 14 Aug 2026, "draft for steering group". I read it as the paper under review, not as an approved position.
- **Owners not named in the sources:**
  - who owns the option paper (A2, A9)
  - who is responsible for Site B (A1, A5)
  - who owns the inbound flow (A3)
  - who owns the warehouse systems and export (A8)
  - HR, for the shift leaders' terms (A4)
  
  The paper's owner, or the steering group, would settle these by naming owners.
- **The supplier record has no version number.** It is dated 2 May 2026 and marked current. Whoever keeps the supplier record can settle this.
- **The paper doesn't mention the MTPD.** BIA v2 gives an MTPD of 24 hours. The paper has no fallback if the 8-hour RTO slips.
- **Not in the sources:**
  - the duration beyond two days (A2)
  - inbound stock (A3)
  - Site B labour (A5)
  - any test or exercise of the option (A8, A9)
- **Intake:** I asked no questions, so no user statements are recorded here.
- **Instructions aimed at an AI:** none found in the attachments.

*Parts of this document were drafted with AI support (red-team-assumptions, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].*

---

A7 (the shared carrier) and A10 (the cost claim) bear most directly on what the steering group is being asked to decide tomorrow. Whether to raise them before the meeting, and with whom, is up to the paper's owner.
