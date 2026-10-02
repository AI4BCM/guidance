# /red-team-assumptions case 1, run3: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `5779405e-7a2d-471c-9670-c0502ccef8cb`.

Files in the working folder: `bia-extract-dispatch.md`, `option-paper-dispatch.md`, `supplier-record-nordfrost.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /red-team-assumptions The steering group meets tomorrow. The files option-paper-dispatch.md, bia-extract-dispatch.md and supplier-record-nordfrost.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three files, I need one answer from you.

**What class of data do the attachments hold, and is this environment approved for it?**

Going by their names, the files probably include material the guidance rates as high-sensitivity:

- **BIA data** (`bia-extract-dispatch.md`)
- **Recovery strategies and design assumptions** (`option-paper-dispatch.md`)
- **Supplier weaknesses and contractual dependencies** (`supplier-record-nordfrost.md`)

High-sensitivity material may only be processed in an approved corporate or private environment. Please confirm one of these:

1. **High-sensitivity, and this environment is approved for that class.** I'll go ahead.
2. **Lower class.** Tell me the class and I'll go ahead.
3. **High-sensitivity, but this environment isn't approved, or you're not sure.** I'll stop, and you can run it somewhere that is approved.

Once you answer, I'll read the three files and only ask about scope if they leave it unclear, such as which option or decision the steering group is weighing. Then you'll get the full assumptions list in one reply, ready for tomorrow.

**Who checks the result:** the BCM manager who owns the option paper checks each assumption against the passage it comes from. Each check's owner answers their question. Finance or procurement checks the financial and commercial assumptions. The steering group makes the choice. What I send will be a draft in the chat, and I won't edit or send anything.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

From option paper "Recovery of chilled dispatch, Site A" v1.2, 14 Aug 2026 (status: draft for steering group)
Checked against BIA v2, approved by top management 4 Feb 2026 (extract: chilled dispatch only)
Checked against supplier record NordFrost, 2 May 2026, status "current", no version number (listed under Gaps)

**Reviewer:** the BCM manager who owns the option paper checks each assumption against its passage. The paper doesn't name that person (see Gaps). Each check goes to the owner named below. Finance or procurement checks the items marked "for finance or procurement". The steering group makes the choice on 2 Oct 2026. This is a draft, and nothing has been edited, sent or approved.

The files set the scope: one option (moving chilled dispatch to Site B), one decision (§5), and the whole paper. So I didn't ask any scope questions.

---

# Assumptions behind the option: chilled dispatch moves to Site B

## The strongest case for the option

The paper starts from a real gap. The approved BIA sets an RTO of 8 hours for chilled dispatch, and §1 says there is no current arrangement. The option uses what the organisation already has: a second site 140 km away that isn't exposed to the loss of Hall 3, a spare cold room there, shift leaders who know the Site A work, and a carrier already under contract to 31 Dec 2027. Nothing has to be bought or built, so it could be in place quickly. The decision goes to the steering group, which is the right body.

## Assumptions the option needs (load-bearing)

The option promises three things: chilled dispatch restored **within the 8-hour RTO** (§2), run from Site B's existing capacity (§3), at **"no additional cost"** (§4). Each assumption below names which of these fails if it is false.

The sources give no effort or cost for any check, so the order of the checks is unknown and left to the reviewer.

**A1. Site B's spare cold room is big enough and free when needed**
- **Passage:** §3, "Site B's spare cold room holds two days' Site A volume."
- **Fails if:** the room is smaller than stated, or already in use when Hall 3 is lost (the paper doesn't say it is reserved). Dispatch at Site A volume then can't run from Site B, and the 8-hour outcome in §2 fails.
- **Check:** the measured capacity of the room against Site A's two-day chilled volume, and whether the room is kept free.
- **Question:** "Is the spare cold room at Site B reserved for Site A, and how much of Site A's two-day chilled volume does it hold today?"
- **Owner:** none in the sources (see Gaps).

**A2. Two days' capacity is enough for the outage**
- **Passage:** §3, "two days' Site A volume". The paper says nothing about how long the arrangement must run.
- **Fails if:** Hall 3 stays out of use for longer than Site B's capacity can carry. Dispatch then stops partway through the outage, and the option covers only the first part of the disruption.
- **Check:** the expected time to restore Hall 3 or a replacement, set against how long Site B can keep running at Site A volume.
- **Question:** "How long must Site B carry Site A's chilled dispatch after Hall 3 is lost, and can it do so beyond two days?"
- **Owner:** none in the sources (see Gaps).

**A3. Site A's shift leaders get to Site B and can run dispatch there in time**
- **Passage:** §3, "Site A's shift leaders drive to Site B." §2, "140 km away, within 8 hours."
- **Fails if:**
  - the leaders can't be reached, aren't available, or don't agree to travel 140 km at short notice, or
  - travel plus start-up doesn't fit inside 8 hours.

  Either way the 8-hour outcome fails. The plan also depends on the same people who are affected by the Site A incident: the option shares this requirement with the activity it is meant to protect.
- **Check:** a call-out list, confirmed availability and travel time, and the terms for working at Site B.
- **Question:** "Can enough of you be called out, reach Site B, and start chilled dispatch there inside 8 hours of losing Hall 3, on any shift?"
- **Owner:** Site A's shift leaders. Proposed, to confirm.

**A4. Site B has the hands to pick and load Site A's volume**
- **Passage:** unstated. §3 moves only the shift leaders.
- **Fails if:** Site B's own staff can't absorb Site A's chilled volume on top of their own work. Throughput then falls short and the 8-hour outcome fails. Extra staff would also break §4's "no additional cost".
- **Check:** Site B staffing set against the combined volume.
- **Question:** "Who picks and loads Site A's chilled orders at Site B, and is that staff available without overtime or temporary hires?"
- **Owner:** none in the sources (see Gaps). The cost part is for finance or procurement.

**A5. Chilled stock reaches Site B**
- **Passage:** unstated. §2 and §3 move dispatch, but say nothing about where the goods come from once Hall 3 is lost.
- **Fails if:** stock in Hall 3 is lost with it and inbound supply can't be sent to Site B in time. There is then nothing to dispatch, and the §2 outcome fails.
- **Check:** how inbound chilled stock would be redirected to Site B, and how long that takes.
- **Question:** "Where does the chilled stock dispatched from Site B come from in the first 8 hours, and who redirects it?"
- **Owner:** none in the sources (see Gaps). The sources name no inbound supplier.

**A6. NordFrost collects from Site B at Site A's volume within 8 hours**
- **Passage:** §3, "Carrier 'NordFrost' serves both sites."
- **Fails if:**
  - NordFrost can't redirect collections and add capacity at Site B within 8 hours, or
  - NordFrost is disrupted itself.

  Either way the §2 outcome fails. The supplier record shows "No SLA for recovery support" and "No information on NordFrost's own continuity plan". The BIA records "no second carrier recorded". So the option relies on the same single carrier as the activity it protects: a shared requirement in the sense of design.md, Method step 4.
- **Check:** NordFrost's written commitment to collect Site A's volume at Site B within the RTO, and its own continuity arrangements.
- **Question:** "Will NordFrost commit in writing to collect Site A's chilled volume at Site B within 8 hours of a call, and can it show its own continuity plan?"
- **Owner:** NordFrost. Proposed, to confirm. **For finance or procurement**, because this is a contractual commitment under the contract running to 31 Dec 2027.

**A7. The manual export to Site B's warehouse system works when Site A is down, and fits the RTO**
- **Passage:** §3, "Site B's warehouse system takes Site A orders after a manual export."
- **Fails if:**
  - the export depends on systems or people lost with Hall 3,
  - nobody at hand knows how to run it, or
  - it is too slow for Site A's order volume.

  Orders then don't reach Site B, and the 8-hour outcome fails.
- **Check:** a timed test of the export and import at Site A volume, with Hall 3 assumed unavailable, and a named person to run it.
- **Question:** "Has the export from Site A into Site B's warehouse system been run end to end, how long did it take at full volume, and does it need anything in Hall 3?"
- **Owner:** none in the sources (see Gaps).

**A8. Together, the steps fit inside 8 hours**
- **Passage:** §2, "within 8 hours". The paper has no timeline.
- **Fails if:** the sum of decision, call-out, travel (A3), export (A7), carrier redirection (A6) and stock arrival (A5) is more than 8 hours. The RTO outcome fails even if each step works on its own.
- **Check:** a timed walk-through or exercise of the full sequence.
- **Question:** "From the moment Hall 3 is lost, what is the timed sequence to the first chilled dispatch from Site B, and has it been exercised?"
- **Owner:** none in the sources (see Gaps). The steering group could ask for it as a condition of choosing the option.

**A9. The option costs nothing extra**
- **Passage:** §4, "no additional cost; uses existing capacity".
- **Fails if:** travel and overtime (A3), extra Site B staff (A4), carrier redirection or surcharges (A6), or keeping the cold room reserved (A1) cost money. §4 then fails, and the steering group would be choosing on a cost basis that isn't true.
- **Check:** a costed estimate of running the option for the expected outage length (A2), including the cost of keeping the cold room free.
- **Question:** "What does one activation of the Site B option cost for the expected outage length, and what does it cost to keep the cold room free?"
- **Owner:** none in the sources. **For finance or procurement.**

## Suppliers the option needs

The sources name one supplier: NordFrost.

| Supplier | Own continuity plan shown? | Written SLA? | Second source? |
|---|---|---|---|
| NordFrost (carrier) | No: "No information on NordFrost's own continuity plan" (supplier record) | No SLA for recovery: "No SLA for recovery support" (supplier record) | No: "no second carrier recorded" (BIA v2) |

Inbound suppliers of chilled stock (A5) are not in the sources.

## What holds up

- **The gap is sourced.** §1's RTO of 8 hours matches BIA v2, approved by top management on 4 Feb 2026.
- **The carrier dependency is stated consistently.** The paper, the BIA and the supplier record all name NordFrost. The paper doesn't hide the dependency, it just doesn't test it (A6).
- **NordFrost is under contract.** The contract runs to 31 Dec 2027, past the decision date. This shows a commercial relationship exists. It does not show a recovery commitment.
- **Site B is outside the loss scenario.** The scenario is loss of Hall 3 at Site A, and Site B is a separate site 140 km away. Nothing in the sources puts Site B in the same event, except through the shared carrier (A6) and the Site A people (A3).
- **The decision goes through governance.** §5 puts the choice to the steering group, which fits design.md, Method step 5.

## Gaps

- **The option paper is a draft.** It is v1.2, 14 Aug 2026, "draft for steering group". It is the paper reviewed here, but it isn't treated as current or final.
- **The option paper has no named owner.** The BCM manager who should check these assumptions against their passages isn't identified.
- **The supplier record has no version number and no owner.** It is dated 2 May 2026 with status "current".
- **The BIA is an extract.** The full BIA v2 wasn't attached.
- **"Current arrangement has none" (§1) has no source or date.** It would be settled by the activity owner confirming it.
- **Six checks have no owner in the sources.** A1, A2, A4, A5, A7 and A8 have none, and A9 has no named owner within finance or procurement. They would be settled by the paper's owner naming an owner for each: for example, whoever runs Site B's cold room, Site B operations, the warehouse system, and inbound supply. None of these is named in the sources.
- **The outage duration the option must cover is not in the sources** (A2).
- **No timeline or exercise result for the 8-hour sequence is in the sources** (A8).
- **The order of the checks is unknown.** No effort or cost is stated for any check, so the order is left to the reviewer.
- **No instructions addressed to an AI were found in the attached files.**

Parts of this document were drafted with AI support (red-team-assumptions skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

Before tomorrow, the paper's owner should check each passage citation. Ideally they also put a name against the six checks that have none, so each question reaches someone before the steering group chooses.
