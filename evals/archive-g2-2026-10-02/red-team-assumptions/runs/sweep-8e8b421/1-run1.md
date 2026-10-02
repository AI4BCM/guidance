# /red-team-assumptions case 1, run1: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `2f796845-99a2-4905-8a6a-97140e824745`.

Files in the working folder: `bia-extract-dispatch.md`, `option-paper-dispatch.md`, `supplier-record-nordfrost.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /red-team-assumptions The steering group meets tomorrow. The files option-paper-dispatch.md, bia-extract-dispatch.md and supplier-record-nordfrost.md in this folder are attached.

**Reply (verbatim):**

Before I open the three attachments, I need one thing from you.

**What class of data do these files hold, and is this environment approved for it?**

From their names, they probably contain BIA data, recovery strategy and design assumptions, and supplier contract dependencies. The AI4BCM data rules class all three as **high-sensitivity**. They may only be processed in an approved corporate or private environment. Please confirm:

1. the sensitivity class of `option-paper-dispatch.md`, `bia-extract-dispatch.md` and `supplier-record-nordfrost.md`
2. that this Claude Code session is an environment your organisation has approved for that class.

If the environment isn't approved for that class, I'll stop here and won't open the files.

Once you confirm, here's how it will run:
- **Reviewer:** the BCM manager who owns the option paper checks each assumption against the passage it comes from. Each check's owner answers their check. Finance or procurement checks the financial and commercial assumptions. The steering group owns the choice of option.
- **Output:** a draft in this chat, ready for tomorrow's steering group. It lists only the assumptions the option depends on, each ending with the check that would settle it and a question for that check's owner. It has no scores. I won't edit, send or publish anything.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

From option paper v1.2, 14 Aug 2026 (status "draft for steering group").
Compared against BIA v2 (extract: chilled dispatch), approved by top management 4 Feb 2026.
From supplier record NordFrost, 2 May 2026, status "current" (it has no version number).

**Reviewer:** the BCM manager who owns the option paper checks each assumption against the passage it comes from. Each check's owner answers their check. Finance or procurement checks the items marked for them. The steering group owns the choice on 2 Oct 2026.

**Scope:** the files cover one option (move chilled dispatch to Site B within 8 hours) and one decision (§5), so I asked no scope questions.

---

## Red-team draft: recovery of chilled dispatch, Site A

### Steelman

The option reuses what already exists. Site B is 140 km away and has a spare cold room. Site A's shift leaders already know the work. The carrier is already under contract to 31 Dec 2027, and Site B's warehouse system can take Site A orders. Nothing new has to be bought or contracted, which is why it looks fast to set up and is costed at "no additional cost; uses existing capacity" (§4). The 140 km also keeps Site B clear of whatever takes out Hall 3.

### Assumptions the option rests on

**Order of checks:** ordering unknown, for the reviewer. None of the sources gives the effort or cost of any check.

**A1. Site B's spare cold room is free and big enough when it's needed.**
- Passage: option paper §3, "Site B's spare cold room holds two days' Site A volume."
- Fails if: the room is smaller than Site A's volume, or Site B is using it at the time of the disruption. Then dispatch can't restart at Site B, and the 8-hour RTO (§1, BIA v2) is missed.
- Check: compare the cold room's measured usable capacity with Site A's daily chilled volume at peak, and confirm the room is kept free all year.
- Owner: not in the sources (see Gaps).
- Question: *"Is Site B's spare cold room big enough for two days of Site A's peak chilled volume, and is it kept free all year so it is spare on the day it's needed?"*

**A2. The disruption is over within two days, or something else takes over after day two.** The paper doesn't say this, but the option depends on it.
- Passage: option paper §3, "two days' Site A volume". The paper says nothing about day three onward.
- Fails if: Hall 3 is out for longer than two days. The option then runs out of capacity, and there is no arrangement for the rest of the outage.
- Check: an estimate of how long Hall 3 takes to restore, and the arrangement for after day two.
- Owner: not in the sources (see Gaps).
- Question: *"How long would losing Hall 3 last in the scenario this option is meant for, and what takes over after day two?"*

**A3. Site A's shift leaders can reach Site B and run dispatch within 8 hours, at any hour.**
- Passage: option paper §3, "Site A's shift leaders drive to Site B."
- Fails if:
  - they can't be reached or released at any hour, or
  - the same event affects them, or
  - the 140 km drive plus start-up doesn't fit inside 8 hours, or
  - shift leaders alone can't staff dispatch at Site B.

  In any of these cases, the RTO is missed.
- Check: a timed call-out to Site B, starting outside normal hours, and a confirmation of who else staffs dispatch there.
- Owner: Site A's shift leaders (proposed, to confirm).
- Question: *"If called at any hour, can enough of you be at Site B and ready to dispatch within 8 hours? Who else would you need to staff it?"*

**A4. NordFrost can move its collections to Site B within 8 hours and is not hit by the same event.** For finance or procurement.
- Passages:
  - option paper §3, "Carrier "NordFrost" serves both sites."
  - BIA v2, "carrier: NordFrost, no second carrier recorded"
  - supplier record, "No SLA for recovery support." and "No information on NordFrost's own continuity plan."
- Fails if: NordFrost can't or won't move collections in time, or NordFrost itself is disrupted. Dispatch then stops at both sites. Here the option depends on the same thing as the activity it is meant to protect (design.md, Method step 4). It is a single point of failure, and there is no second carrier to fall back on.
- Check: written confirmation from NordFrost of how quickly it can move collections to Site B, and evidence of its own continuity arrangements.
- Owner: NordFrost (proposed, to confirm), through whoever holds the contract. The sources don't name that person.
- Question: *"Will NordFrost commit in writing to moving chilled collections from Site A to Site B within 8 hours? Can it show its own continuity plan?"*

**A5. Site A orders can be exported and taken into Site B's system within the RTO, with Hall 3 lost.**
- Passage: option paper §3, "Site B's warehouse system takes Site A orders after a manual export."
- Fails if:
  - the export depends on systems, network or staff tied to Hall 3, or
  - the manual export and import can't be done fast enough or at full volume.

  Orders then don't reach Site B in time, and the RTO is missed.
- Check: a test run of the manual export and import at one day's volume, with Hall 3 treated as unavailable.
- Owner: not in the sources (see Gaps).
- Question: *"Can Site A orders be exported by hand and loaded into Site B's warehouse system at full daily volume within the RTO, without anything in Hall 3?"*

**A6. The steps fit inside 8 hours end to end.** The paper doesn't say this, but the option depends on it.
- Passage: option paper §2, "within 8 hours". The paper gives no timeline for its steps.
- Fails if: travel (A3), carrier redirection (A4), order transfer (A5) and readying the cold room (A1) add up to more than 8 hours. The RTO is then missed, even though each step works on its own.
- Check: a step-by-step timeline from the moment Hall 3 is lost to the first dispatch from Site B, ideally confirmed in an exercise.
- Owner: not in the sources (see Gaps).
- Question: *"What is the timeline from losing Hall 3 to the first chilled dispatch from Site B? Has it been exercised against the 8-hour RTO?"*

**A7. The goods to dispatch get to Site B.** The paper doesn't say this, but the option depends on it.
- Passage: option paper §2 and §3. The paper covers capacity, staff, carrier and orders, but not how the chilled stock reaches Site B.
- Fails if: the stock is lost with Hall 3 and nothing redirects supply to Site B. There is then nothing to dispatch, whatever capacity is ready.
- Check: confirmation of where the stock for Site A orders comes from once Hall 3 is lost.
- Owner: not in the sources (see Gaps).
- Question: *"With Hall 3 lost, where does the chilled stock for Site A orders come from, and how does it reach Site B within the RTO?"*

**A8. The option really costs nothing extra.** For finance or procurement.
- Passage: option paper §4, "no additional cost; uses existing capacity".
- Fails if: travel and working-time costs (A3), carrier redirection charges (A4), or displaced Site B volume (A1) cost money. The steering group would then be choosing on a cost basis that isn't true.
- Check: a costed estimate of activating the option, covering staff travel and hours, carrier charges and the use of Site B capacity.
- Owner: not in the sources (see Gaps).
- Question: *"What does activating this option actually cost per day, including staff travel and hours, carrier charges and the use of Site B capacity?"*

### Suppliers the option needs

| Supplier | Own continuity plan | Written SLA | Second source | Source |
|---|---|---|---|---|
| NordFrost (carrier) | Not shown: "No information on NordFrost's own continuity plan." | None for recovery: "No SLA for recovery support." | None: "no second carrier recorded" | Supplier record, 2 May 2026; BIA v2 extract |

The sources name no other supplier. Nothing in them says whether Site B's warehouse system or any other part of the option depends on a third party.

### What holds up, and why

- **The gap is sourced and current.** The 8-hour RTO in §1 matches BIA v2, which top management approved on 4 Feb 2026. That BIA is older than the paper.
- **The target sits inside the BIA's tolerance.** An 8-hour RTO against a 24-hour MTPD (BIA v2) leaves 16 hours of margin before the MTPD is reached, if the RTO slips.
- **Two days of capacity, if real, covers more than the MTPD.** That holds only if A1 and A2 are confirmed.
- **The carrier dependency is out in the open.** The paper names NordFrost in §3, consistent with the BIA. The weakness is in A4, not hidden.
- **The contract covers the decision period.** The NordFrost contract runs to 31 Dec 2027 (supplier record), so the commercial relationship exists. Recovery support is a separate question (A4).
- **The second site is separate from Hall 3.** At 140 km away (§2), Site B is unlikely to be hit by a local event at Site A. The paper doesn't define the scenario beyond "Hall 3 lost".

### Gaps

- **The paper is a draft.** Option paper v1.2, 14 Aug 2026, is "draft for steering group". I read it as the paper under review, not as an approved arrangement.
- **The paper has no named owner.** It names no author or owner, so the BCM manager who reviews this draft isn't named in the sources.
- **Most checks have no owner in the sources.** No person or body is named for A1, A2, A5, A6, A7 or A8. Each is settled once the steering group or the paper's owner assigns one: for example the Site B site lead for A1, IT for A5, and finance for A8.
- **The paper doesn't mention the MTPD.** It doesn't say what happens if the RTO slips toward the 24-hour MTPD.
- **Nothing covers day three onward:** not in the sources (see A2).
- **Nothing about a supplier behind Site B's warehouse system:** not in the sources.
- **The supplier record has no version number.** It is dated 2 May 2026 and marked current.
- **No instructions addressed to an AI** were found in the three files.

---

Parts of this document were drafted with AI support (red-team-assumptions, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

Nothing has been edited, sent or recorded. Before tomorrow, the paper's owner can check each passage cited above and get the eight questions to the owners named there. The steering group will need owners for the six checks the sources leave without one.
