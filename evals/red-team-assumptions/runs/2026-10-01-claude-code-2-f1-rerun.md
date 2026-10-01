# /red-team-assumptions on Claude Code: case 2-f1-rerun

Date 2026-10-01. Skill text at commit 7d6a3c6. Claude Code 2.1.284, `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed, fresh scratch folder (`2-f1-rerun`) with the case files copied in; turn 2 with `--resume`. One run; no crash.

## Turn 1

**Request:**

> /red-team-assumptions The three files in this folder (option-paper-dispatch.md, bia-extract-dispatch.md, supplier-record-nordfrost.md) are attached. The steering group meets tomorrow.

**Reply** (session d17fcc40-501a-42e4-953d-1addd366379b, is_error False):

Before I open the three files I need one answer from you.

**What class of data do these files hold, and is this environment approved for it?**

From the file names, they probably include recovery-strategy and design assumptions (the option paper), BIA data (the BIA extract), and supplier weaknesses and contractual dependencies (the Nordfrost record). The data rules treat all of these as **high sensitivity**. High-sensitivity material may only be handled in an enterprise, private or approved BCM environment. So please tell me:

- whether the files hold high-sensitivity material, as their names suggest, or something lower; and
- whether this Claude Code environment is approved for that class in your organisation.

If it isn't approved for high-sensitivity data, I'll stop here and won't read the files. Run the review in your approved environment instead.

**Who reviews the output:**
- The BCM manager who owns the option paper checks each assumption against the passage that relies on it.
- Each check's owner answers their own check.
- Finance or procurement checks the financial and commercial assumptions.
- The stakeholder group (your steering group) owns the choice between options.

What I'll give you is a draft in the chat. I won't change the paper, the BIA, the supplier record or any register.

Once you confirm the class and approval, I'll read the files. If they already set the scope (which option, which decision), I'll go straight to the assumptions list so it's ready before tomorrow's meeting.

## Turn 2

**Request:**

> High, and this environment is approved for high.

**Reply** (session d17fcc40-501a-42e4-953d-1addd366379b, is_error False):

**Sources read**
- Option paper: recovery of chilled dispatch, Site A. Version 1.2, 14 Aug 2026, "draft for steering group". Listed under Gaps.
- BIA extract: chilled dispatch, from BIA v2, approved by top management 4 Feb 2026.
- Supplier record: NordFrost, 2 May 2026, status "current". It has no version number, so it's listed under Gaps.

**Scope.** The files settle it, so I asked no scope questions. There is one option: move chilled dispatch to Site B within 8 hours if Hall 3 is lost. There is one decision: the steering group chooses it on 2 Oct 2026 (option paper §5).

**Reviewer.** The BCM manager who owns the option paper checks each assumption below against its passage. Each check's owner answers their question. Finance or procurement checks the entries marked for them. The steering group owns the choice.

## The paper at its strongest

The option fills a stated gap: an 8-hour RTO with "current arrangement has none" (§1, matching BIA v2). It reuses things the organisation already has:
- a spare cold room
- staff who already know Site A's dispatch work
- a carrier already under contract to 31 Dec 2027
- a warehouse system at the receiving site

Site B is 140 km away, so it is physically separate from a Hall 3 event. If its four premises (§3) hold and the steps fit inside 8 hours, the option closes the gap without new investment.

## Load-bearing assumptions

Ordering unknown, for the reviewer: the sources state no effort or cost for any check.

**1. Site B's spare cold room is free and big enough when it's needed.**
- **Passage:** §3, "Site B's spare cold room holds two days' Site A volume."
- **Fails if:** the room is in use by Site B (peak season, its own stock) when Hall 3 is lost. Chilled dispatch then can't restart at Site B, and the 8-hour RTO fails.
- **Check:** confirm the room is held for this use all year, not only spare on average.
- **Question:** "Is the cold room reserved for Site A's volume all year, and who can stop Site B from filling it?"
- **Owner:** none named in the sources (see Gaps).

**2. Two days' capacity covers the time the option has to run.**
- **Passage:** §3, "two days' Site A volume"; §2, "Hall 3 lost".
- **Fails if:** Hall 3 stays out of use for longer than the paper assumes, and nothing says how dispatch continues after two days. The paper never states how long the option must cover.
- **Check:** state the expected time to restore Hall 3 and compare it with the cold room's cover.
- **Question:** "How long must Site B run Site A's chilled dispatch, and what happens after day two?"
- **Owner:** the paper's owner (not named in the sources; see Gaps).

**3. Site A's chilled goods reach Site B.** The paper doesn't say this, but its logic depends on it.
- **Passage:** §2, "Move chilled dispatch to Site B". The paper doesn't say how stock or inbound deliveries get there.
- **Fails if:** stock lost with Hall 3 isn't replaced, or inbound deliveries can't be redirected to Site B within the RTO. Site B then has nothing to dispatch.
- **Check:** trace how chilled stock arrives at Site B, and how fast.
- **Question:** "Who redirects inbound chilled deliveries to Site B, and how long does it take?"
- **Owner:** not in the sources (see Gaps).

**4. Site A's shift leaders can get to Site B and run dispatch there within the RTO.**
- **Passage:** §3, "Site A's shift leaders drive to Site B."
- **Fails if:**
  - the drive (140 km), call-out and start-up don't fit inside 8 hours, for example at night or in bad weather;
  - shift leaders alone can't do the work: the paper doesn't say who picks and loads at Site B;
  - they lack site access or system logins at Site B.
- **Check:** time a real call-out to Site B, and confirm staffing, access and logins.
- **Question:** "Can you be at Site B, logged in and dispatching, inside 8 hours of a call at any hour, and who does the picking?"
- **Owner:** Site A shift leaders (proposed, to confirm). Who manages them and their travel terms is under Gaps.

**5. NordFrost can move collections to Site B and still reach Site A's customers.**
- **Passages:** §3, "Carrier 'NordFrost' serves both sites"; BIA v2, "carrier: NordFrost, no second carrier recorded".
- **Fails if:**
  - NordFrost can't redirect collections to Site B within the RTO;
  - NordFrost has no spare vehicles for the extra volume;
  - deliveries from 140 km away miss Site A's customers' delivery windows.

  In each case dispatch doesn't recover.
- **Check:** confirm, in writing, the time and capacity to re-route from Site B, and the delivery times from Site B to Site A's customers.
- **Question:** "How fast can you switch Site A's collections to Site B, with what capacity, and on what terms?"
- **Owner:** NordFrost (proposed, to confirm). **For finance or procurement**, because it rests on contract terms.

**6. NordFrost isn't hit by the same disruption.** The option moves the site but keeps the carrier. That is the requirement it quietly shares with the arrangement it is meant to protect.
- **Passages:** §3, the NordFrost line; BIA v2, "no second carrier recorded"; supplier record, "No SLA for recovery support", "No information on NordFrost's own continuity plan".
- **Fails if:** NordFrost is disrupted, or can't support recovery. Both sites then lose chilled dispatch, and nothing in the sources holds them up.
- **Check:** get NordFrost's continuity arrangements and agree recovery-support terms, or record that a second carrier is needed.
- **Question:** "What is your continuity plan, and will you commit in writing to recovery support for Site A's volumes?"
- **Owner:** NordFrost (proposed, to confirm). **For finance or procurement.**

**7. The manual export works when Site A is down, and fits inside 8 hours.**
- **Passage:** §3, "Site B's warehouse system takes Site A orders after a manual export."
- **Fails if:**
  - the export needs a system, terminal or person that is lost with Hall 3 or Site A;
  - the export or import takes too long;
  - it has never been tried.

  Site B then can't see the orders.
- **Check:** run the export and import end to end with Hall 3 treated as unavailable, and time it.
- **Owner:** none named in the sources (see Gaps).

**8. All the steps together fit inside 8 hours.**
- **Passage:** §2, "within 8 hours"; §1, "Required RTO … is 8 hours".
- **Fails if:** call-out, travel, cold room readiness, stock, export and carrier re-route are each feasible but add up to more than 8 hours. The RTO is then missed, and MTPD (24 hours) comes closer.
- **Check:** draw up a timed sequence of the steps, or test one.
- **Owner:** the paper's owner (not named in the sources; see Gaps).

**9. The option costs nothing extra.**
- **Passage:** §4, "no additional cost; uses existing capacity".
- **Fails if:** travel, overtime or accommodation for the shift leaders, extra carrier mileage or volume charges, the export work, or keeping the cold room empty cost money. The steering group would then be choosing on a cost basis that is wrong.
- **Check:** cost each of these.
- **Owner:** **for finance or procurement.** No named person in the sources (see Gaps).

## Suppliers the option needs

**NordFrost**
- **Own continuity plan:** not shown. The supplier record says "No information on NordFrost's own continuity plan".
- **Written SLA:** none for recovery. The supplier record says "No SLA for recovery support". Whether any other SLA exists is not in the sources.
- **Second source:** none. BIA v2 says "no second carrier recorded".

**Any other supplier** (for example the provider of Site B's warehouse system): not in the sources.

## What holds up

- **The gap is sourced.** §1's 8-hour RTO matches BIA v2 (approved 4 Feb 2026), and MTPD is 24 hours. The requirement is approved, not invented by the paper.
- **The carrier contract runs past the decision.** It runs "to 31 Dec 2027" (supplier record). Whether its terms cover the option is assumption 5.
- **The site is far enough from the event in scope.** Site B is 140 km from Site A (§2), which plausibly puts it outside an event that takes out Hall 3. The option doesn't answer events that hit both sites; for the shared carrier, see assumption 6.

## Gaps

- **The option paper is a draft:** v1.2, 14 Aug 2026, "draft for steering group". I read it as the paper under review, not as an approved document.
- **The supplier record has no version number.** It is dated 2 May 2026, status "current".
- **I saw a BIA extract, not the full BIA v2.** Anything else BIA v2 says about chilled dispatch is not in the sources.
- **Nobody is named as owner** of:
  - the option paper;
  - Site B's cold room (assumption 1);
  - inbound redirection (assumption 3);
  - Site B's warehouse system and the manual export (assumption 7);
  - the cost check (assumption 9);
  - the shift leaders' line management and travel terms (assumption 4).

  Each of these checks would be settled by naming an owner.
- **How long the option must run** is not in the sources. Stating the expected time to restore Hall 3 would settle it.
- **The paper doesn't list its residual risks,** for example dependence on a single carrier. The design-stage controls expect them to stay visible in the paper.
- **I found no instructions aimed at an AI in the attachments.**

---

Parts of this document were drafted with AI support (/red-team-assumptions, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
