# /red-team-assumptions case 1, run2: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `50df9286-ab84-4e34-a8b1-1439338943c7`.

Files in the working folder: `bia-extract-dispatch.md`, `option-paper-dispatch.md`, `supplier-record-nordfrost.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /red-team-assumptions The steering group meets tomorrow. The files option-paper-dispatch.md, bia-extract-dispatch.md and supplier-record-nordfrost.md in this folder are attached.

**Reply (verbatim):**

Before I open the three attachments, I need one answer from you. Per the skill's preflight, this question comes first and on its own.

**What class of data do these files hold, and is this environment approved for it?**

From their names (an option paper, a BIA extract and a supplier record), the files probably contain material the AI4BCM data rules treat as **high-sensitivity**. That covers BIA data, recovery strategies and design assumptions, supplier weaknesses and contractual dependencies, and possibly steering-group papers. High-sensitivity data may only be processed in an **approved corporate or private environment**.

Please confirm one of these:

1. **High-sensitivity, and this Claude Code environment is approved for it** by your organisation's information security policy. I'll go ahead and read the files.
2. **Not high-sensitivity** (for example, sanitised or fictional training material). Say what class it is and I'll go ahead.
3. **High-sensitivity, and this environment is not approved, or you're not sure.** I'll stop here without reading the files. I can then tell you how to prepare a sanitised version, or explain the method so you can apply it yourself in an approved environment.

Once that's settled I'll read the files. I'll only ask about scope if the files leave it open.

For the steering group: the BCM manager who owns the option paper checks each assumption against the passage it comes from. The person who owns each check answers it, and finance or procurement checks the financial and commercial assumptions. The stakeholder group makes the choice. You'll get a draft in this chat, and I won't edit, send or approve anything.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Source versions:
- Option paper v1.2, 14 Aug 2026, status "draft for steering group".
- Checked against BIA v2, approved by top management 4 Feb 2026 (extract only).
- NordFrost supplier record, dated 2 May 2026, status "current", no version number (listed under Gaps).

The files settle the scope: one option (move chilled dispatch to Site B) and one decision (the steering group's choice on 2 Oct 2026). So I asked no scope questions. The BCM manager who owns the option paper checks each assumption below against the passage it comes from.

# What the Site B option needs to be true

## The paper's strongest case

The option reuses things the business already has: Site B, the carrier NordFrost, and Site A's own shift leaders. It needs no new contract. The gap it addresses is sourced and dated. The paper also states its premises openly (§3), so each one can be tested.

## Load-bearing assumptions

The sources give no effort or cost for any check, so the order of the checks is unknown and left to the reviewer.

**A1. Site B's cold room is big enough and actually free.**
- **Passage:** §3: "Site B's spare cold room holds two days' Site A volume." §4: "uses existing capacity".
- **Fails if:** the room holds less than that, or Site B is already using it when Hall 3 is lost. Site A's chilled stock then has nowhere to go at Site B, and dispatch can't restart within the 8-hour RTO.
- **Check:** compare the room's measured usable capacity with Site A's daily chilled volume, and look at how the room is used across the year.
- **Question:** "What is the usable capacity of the spare cold room in days of Site A volume, and is it still free at Site B's own peak?"
- **Owner:** none named in the sources (see Gaps).

**A2. Goods to dispatch reach Site B. The paper doesn't state this.**
- **Passage:** §2: "Move chilled dispatch to Site B, 140 km away, within 8 hours." The paper doesn't say where the goods come from once Hall 3 is lost.
- **Fails if:** the stock in Hall 3 is lost and incoming chilled deliveries can't be sent to Site B in time. Then there is nothing to dispatch within 8 hours.
- **Check:** find a documented way to send incoming chilled goods, or surviving stock, to Site B, and how long it takes.
- **Question:** "How would chilled stock for Site A orders get to Site B after Hall 3 is lost, and how many hours would that take?"
- **Owner:** none named in the sources (see Gaps).

**A3. Enough staff can get to Site B in time to handle Site A's volume.**
- **Passage:** §3: "Site A's shift leaders drive to Site B."
- **Fails if:** the shift leaders can't get there in time (140 km, at any hour, from whatever shift they're on). It also fails if shift leaders alone can't do the picking and loading. The paper names nobody else for that work. Either way, dispatch doesn't restart within 8 hours.
- **Check:** time a rostered call-out, and set a headcount for the work at Site B.
- **Question** (owner: Site A's shift leaders, proposed, to confirm): "If you were called at any hour, how many of you could be working at Site B, and how fast? Who would do the picking and loading with you?"
- **Gap:** nobody is named to own the headcount question.

**A4. NordFrost can collect Site A's volume at Site B within the RTO.**
- **Passage:** §3: "Carrier "NordFrost" serves both sites." Supplier record: "No SLA for recovery support."
- **Fails if:** NordFrost can't add Site A's volume at Site B within 8 hours. Goods are then ready but don't leave.
- **Check:** written confirmation from NordFrost of how much it can collect at Site B, and how fast. This is **for finance or procurement**.
- **Question** (owner: NordFrost, proposed, to confirm): "Within how many hours could you collect Site A's chilled volume at Site B, in addition to Site B's own, and on what contract terms?"

**A5. NordFrost keeps working while Site A is disrupted.** The option shares its carrier with the activity it is meant to protect.
- **Passage:** §3 "Carrier "NordFrost" serves both sites". BIA v2: "no second carrier recorded". Supplier record: "No information on NordFrost's own continuity plan."
- **Fails if:** NordFrost is hit by the same event, or fails during the recovery. Chilled dispatch then stops at both sites, and the option gives no recovery at all.
- **Check:** see NordFrost's own continuity plan, and confirm whether a second carrier exists or can be contracted. The second-carrier part is **for finance or procurement**.
- **Question** (owner: NordFrost, proposed, to confirm): "Do you have a continuity plan that covers your service to both Site A and Site B, and will you share it?"
- **Gap:** nobody is named to own the second-carrier question.

**A6. Site A's orders can be exported and Site B can take them in.**
- **Passage:** §3: "Site B's warehouse system takes Site A orders after a manual export."
- **Fails if:** Site A's order system or its data depend on Hall 3, or nobody available can run the export, or Site B's import fails. Site B then can't see the orders.
- **Check:** a timed test export and import, plus a record of where Site A's system is hosted. Its hosting is not in the sources.
- **Question:** "Has a manual export from Site A into Site B's warehouse system been run? How long did it take, and does it still work with Hall 3 down?"
- **Owner:** none named in the sources (see Gaps).

**A7. The option costs nothing extra.**
- **Passage:** §4: "no additional cost; uses existing capacity".
- **Fails if:** travel, overtime, NordFrost charges for Site B collections, or pushing aside Site B's own use of the cold room cost money. The steering group would then choose on a wrong cost basis. This is **for finance or procurement**.
- **Check:** a costed run of A1 to A6 for one disruption lasting up to the 24-hour MTPD.
- **Question:** "What would one move to Site B cost in travel, overtime, carrier charges and Site B capacity given up?"
- **Owner:** none named in the sources (see Gaps).

**A8. The whole sequence fits inside 8 hours.**
- **Passage:** §2: "within 8 hours". The paper gives no timeline.
- **Fails if:** the steps take longer than 8 hours in total: the decision to move, staff travel, getting stock there, the order export and NordFrost re-routing. The BIA's 8-hour RTO is then missed, and the 24-hour MTPD is the outer limit.
- **Check:** a timed walkthrough or exercise of the whole move, start to finish.
- **Question:** "From the moment Hall 3 is lost, how long until the first Site A order leaves Site B?"
- **Owner:** none named in the sources (see Gaps).

## Suppliers the option needs

| Supplier | Own continuity plan shown? | Written SLA? | Second source? |
|---|---|---|---|
| NordFrost | No: "No information on NordFrost's own continuity plan" (supplier record) | No SLA for recovery. There is a contract to 31 Dec 2027, but "No SLA for recovery support" (supplier record) | None: "no second carrier recorded" (BIA v2) |

The sources name no other supplier. Whether Site B's warehouse system or the manual export depend on a third party is not in the sources.

## What holds up

- **The gap is sourced and consistent:** the 8-hour RTO in §1 matches BIA v2, approved 4 Feb 2026, and "current arrangement has none" states the gap plainly.
- **The BIA leaves a margin:** the BIA gives a 24-hour MTPD beyond the 8-hour RTO.
- **The carrier contract is in force:** the NordFrost contract runs to 31 Dec 2027, past the decision date of 2 Oct 2026. Whether it covers collections at Site B is A4.
- **The claimed capacity would be enough:** if A1 holds, two days of cold-room capacity is more than the 24-hour MTPD window.

## Gaps

- **The option paper is a draft:** v1.2, 14 Aug 2026, "draft for steering group". I read it as the paper under review, not as an agreed strategy. It names no author or owner.
- **The supplier record has no version:** NordFrost record, 2 May 2026, "current", no version number.
- **I only have an extract of the BIA:** the full BIA v2 wasn't attached.
- **These checks have no owner in the sources:**
  - A1, cold room
  - A2, getting stock to Site B
  - A3, the headcount part
  - A5, second carrier
  - A6, order export
  - A7, cost
  - A8, end-to-end timing

  What would settle this: the paper's owner names an owner for each check before the steering group relies on the option.
- **Not in the sources:**
  - Site A's daily chilled volume
  - Site B's own BIA or requirements, including its cold-room peak
  - where Site A's order system is hosted
  - any timeline or exercise result for the move
- **No embedded instructions:** none of the files contained instructions aimed at an AI.

Each "Fails if…" above is a question for its owner and stays open until that owner answers it. I rated no risk and recommend nothing. The steering group still owns the choice.

Parts of this document were drafted with AI support (red-team-assumptions skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
