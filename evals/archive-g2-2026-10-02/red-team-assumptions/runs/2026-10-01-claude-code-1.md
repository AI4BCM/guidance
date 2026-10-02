# /red-team-assumptions on Claude Code: case 1

Date 2026-10-01. Claude Code 2.1.284, `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed, scratch folder with the case files copied in; later turns with `--resume`. One run; no crash.

## Turn 1

**Request:**

> /red-team-assumptions The three files in this folder (option-paper-dispatch.md, bia-extract-dispatch.md, supplier-record-nordfrost.md) are attached. The steering group meets tomorrow.

**Reply** (session 3ab8649a-b497-451b-b76a-769a015eb11b, is_error False):

Before I open the three files, I need one answer from you.

**What class of data do these files hold, and is this environment approved for it?**

The filenames suggest an option paper (recovery strategy and design assumptions), a BIA extract and a supplier record (supplier weaknesses and contractual dependencies). Under the guidance's data rules, all three of those are **high-sensitivity**. High-sensitivity material may only be handled in an approved enterprise, private or purpose-built BCM environment. This applies to Design-stage work on solution options and supplier concentration (`units/data-rules.md`, Sensitivity classes; `units/tools.md`, Selection guide).

Please confirm both of these:
1. The class these files belong to (for example, high: recovery strategy, BIA data, supplier dependencies).
2. That this Claude environment is approved for that class. That means its retention, access and contract terms have passed your organisation's tool checks.

If it isn't approved, I'll stop here and won't read the files.

**Who reviews the output:** the BCM manager who owns the Dispatch option paper. They check each assumption I list against the passage it comes from. The person named for each check answers that check. Finance or procurement check the financial and commercial assumptions, and the steering group owns the choice of option.

When you've confirmed, I'll read the files. I'll then ask only the scope questions the files don't already answer. I know the steering group meets tomorrow, so I'll keep those questions short.

## Turn 2

**Request:**

> High, and this environment is approved for high.

**Reply** (session 3ab8649a-b497-451b-b76a-769a015eb11b, is_error False):

I've read the three files. Before I build the list I have three scope questions, because the files leave these points open:

1. **Version.** The option paper is v1.2, dated 14 Aug 2026, with the status "draft for steering group". Is v1.2 the version the steering group will see tomorrow, or is there a later one? Either way I'll read v1.2 and list it under Gaps as a draft.
2. **Site B sources.** The option depends on Site B: its cold room capacity, its warehouse system, and whatever Site B itself already needs NordFrost and that cold room for. None of the three files covers Site B. Do you want to attach a Site B requirements register, BIA extract or capacity record? If not, I'll mark those points "not in the sources".
3. **Owners.** None of the files names an owner for any check. Which roles should the questions go to for:
   - Site B operations
   - Site A shift leaders (operations or HR)
   - NordFrost (procurement)
   - the warehouse system and export (IT)

   If you'd rather not say, I'll list those checks as "no owner in the sources".

Your answers can shape the scope, but I won't use them as values in the list. I'll record them under Gaps as your own statements, not as sources. You can skip any question, and I'll note it as an assumption.

## Turn 3

**Request:**

> Skip all three questions; go ahead with the three files as they are.

**Reply** (session 3ab8649a-b497-451b-b76a-769a015eb11b, is_error False):

*From option paper "Recovery of chilled dispatch, Site A", v1.2, 14 Aug 2026 (draft for steering group). Checked against BIA v2, approved by top management on 4 Feb 2026 (extract: chilled dispatch). Also from the NordFrost supplier record dated 2 May 2026, status current, which has no version number.*

# Draft: what the Site B dispatch option relies on

**Reviewer:** the BCM manager who owns the option paper checks each assumption against the passage it comes from. The owner of each check answers it. Finance or procurement check the items marked for them. The steering group owns the choice.

**The paper's strongest case.** The paper takes its gap from an approved source: the 8-hour RTO is in BIA v2. It proposes one concrete option that uses a site the company already has. It lists what that option rests on in §3 instead of hiding it. The 8-hour target sits within the 24-hour MTPD, and the paper asks for a clear decision (§5).

## Assumptions the option needs (all proposed, to confirm)

The sources name no owner for any of these checks, so each question below has the owner "no owner in the sources".

**1. Site B's cold room capacity is really spare.** §3: "Site B's spare cold room holds two days' Site A volume."
- *Fails if* the room is smaller than Site A's chilled volume, or Site B is already using it when Hall 3 is lost. Dispatch from Site B then can't start within 8 hours.
- *Check:* the measured capacity of the spare cold room compared with Site A's chilled volume, plus any current or planned use of it by Site B.
- *Question:* "How much can the spare cold room hold today, does anything at Site B use it or have a claim on it, and who confirms that it's free on any given day?"

**2. Hall 3 is back, or something else takes over, within two days.** §3 says "two days' Site A volume". The paper doesn't say what happens after that.
- *Fails if* Hall 3 is out for longer than the cold room's two days of volume. Dispatch then stops a second time, with no arrangement in the paper.
- *Check:* whether "two days" limits how long the option can run, and what follows if Hall 3 isn't restored by then.
- *Question:* "Is two days a limit on how long the option can run? If so, what happens on day three?"

**3. Site A's shift leaders can and will go to Site B in time.** §3: "Site A's shift leaders drive to Site B." §2 says Site B is "140 km away".
- *Fails if* the shift leaders aren't available, aren't required to work at another site, or can't arrive early enough. The 140 km drive comes out of the 8 hours. Dispatch then has no one to run it within the RTO.
- *Check:* the shift-leader roster and the terms that cover working at another site. Also, whether the shift leaders are enough or other Site A staff are needed as well.
- *Question:* "Who goes, how are they called out at any hour, are they required to work at Site B, and how long does it take from the call to the start of dispatch at Site B?"

**4. NordFrost moves collections to Site B within the RTO.** This one is for finance or procurement. §3: "Carrier "NordFrost" serves both sites."
- *Fails if* NordFrost can't or won't redirect collections to Site B within 8 hours, or is itself disrupted. This is the dependency the option shares with what it's meant to protect: the same single carrier serves both the failed site and the recovery site.
  - The BIA records "no second carrier recorded".
  - The supplier record says "No SLA for recovery support" and "No information on NordFrost's own continuity plan".
- *Check:* written confirmation from NordFrost of the time it needs to move Site A's collections to Site B. Also, NordFrost's own continuity plan.
- *Question:* "Will NordFrost commit in writing to collecting Site A volume at Site B within the 8 hours, and will it share its continuity plan?"

**5. Site B's warehouse system can take Site A's orders in time.** §3: "Site B's warehouse system takes Site A orders after a manual export."
- *Fails if* the export can't be run once Hall 3 is lost, if Site B's system can't accept Site A's customers, products or orders, or if the export and import together take too much of the 8 hours.
- *Check:* a timed test of exporting a day's Site A orders and importing them into Site B's system. Also, where the export runs from.
- *Question:* "Has the manual export ever been run into Site B's system? How long did it take, and does it still work if Hall 3 is lost?"

**6. Chilled goods are available at Site B to dispatch.** The paper doesn't state this, but dispatch needs it.
- *Fails if* the product that would have left Hall 3 isn't at Site B or can't get there. There is then nothing to dispatch, whatever the cold room, staff, carrier and system can do. The paper doesn't say how goods reach Site B.
- *Check:* where the stock to be dispatched comes from once Hall 3 is lost, and how long it takes to arrive at Site B.
- *Question:* "Where does Site B get the chilled stock it dispatches for Site A, and how soon after the loss of Hall 3?"

**7. All the steps together fit within 8 hours.** §2 says "within 8 hours". The paper gives no timeline.
- *Fails if* the decision to invoke, the call-out, the 140 km drive, the export, NordFrost's redirection and the stock arriving add up to more than 8 hours. The option then misses the RTO taken from BIA v2.
- *Check:* a timeline from the loss of Hall 3 to the first dispatch from Site B, tested by a walk-through or an exercise.
- *Question:* "Can you put the steps on a timeline with times, and has it been walked through?"

**8. The option costs nothing extra.** This one is for finance or procurement. §4: "no additional cost; uses existing capacity".
- *Fails if* the option brings costs: travel, overtime or accommodation for shift leaders working 140 km away, NordFrost charges for redirecting, or a cost to whatever Site B gives up to free the cold room. The steering group would then be choosing on a stated zero cost that doesn't hold.
- *Check:* finance costs a two-day relocation, using assumptions 1 to 6.
- *Question:* "What would a two-day relocation actually cost, including staff, carrier and Site B's displaced use?"

**Order of checks:** ordering unknown, for the reviewer. The sources state no effort or cost for any check.

## Suppliers the option needs

| Supplier | Own continuity plan shown? | Written SLA? | Second source? | Source |
|---|---|---|---|---|
| NordFrost (carrier) | No: "No information on NordFrost's own continuity plan" | Contract to 31 Dec 2027, but "No SLA for recovery support" | No: "no second carrier recorded" | Supplier record, 2 May 2026; BIA v2 |
| Warehouse system provider (Site B) | not in the sources | not in the sources | not in the sources | Option paper §3 names the system but no supplier |

## What holds up, and why

- **The 8-hour RTO.** §1 says the RTO for chilled dispatch is 8 hours. The approved BIA v2 states the same, and the option aims at that figure.
- **RTO within MTPD.** The 8-hour target sits inside the BIA's 24-hour MTPD, so the paper isn't aiming past the tolerance limit.
- **The gap, "current arrangement has none" (§1).** None of the three files confirms or contradicts this. The option's outcome doesn't depend on it, so it isn't load-bearing here.
- **The paper lists its own assumptions.** §3 is open about four of them, which makes the paper checkable as written.

## Gaps

- **Option paper v1.2, 14 Aug 2026, is a draft** ("draft for steering group"). It is the paper reviewed here, but it is not an approved document.
- **The supplier record has a date (2 May 2026) and the status "current", but no version.**
- **Your skipped answers, recorded as assumptions:**
  - v1.2 is the version the steering group will see on 2 Oct 2026.
  - No Site B records were used. Site B's capacity, its own use of the cold room and its warehouse system are "not in the sources".
  - No owners were given. Every check above has no owner in the sources. The paper's owner would need to assign them before any can be answered.
- **Residual risk is not stated in the paper.** The paper names no residual risk, such as the single carrier or what happens after two days. The design stage's minimum controls ask for residual risks to stay visible in the paper.
- **No risk owner is named** in the sources for accepting the remaining dependence on NordFrost.
- **No instructions to an AI** were found in the three files.

---

*Parts of this document were drafted with AI support (red-team-assumptions skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].*
