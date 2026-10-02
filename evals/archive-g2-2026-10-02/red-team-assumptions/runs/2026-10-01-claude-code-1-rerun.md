# /red-team-assumptions on Claude Code: case 1-rerun

Date 2026-10-01. Skill text at commit 7d6a3c6. Claude Code 2.1.284, `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed, fresh scratch folder (`1-rerun`) with the case files copied in; turn 2 with `--resume`. One run; no crash.

## Turn 1

**Request:**

> /red-team-assumptions The three files in this folder (option-paper-dispatch.md, bia-extract-dispatch.md, supplier-record-nordfrost.md) are attached. The steering group meets tomorrow.

**Reply** (session f081865f-77fb-4985-8287-6752de81b68d, is_error False):

Before I open the three files, I need one answer from you. This is the first step of every AI4BCM skill.

**What class of data do the files hold, and is this environment approved for it?**

From the file names, they look like recovery-strategy and design assumptions (the option paper), BIA data (the BIA extract), and supplier contract and dependency detail (the Nordfrost record). Under `units/data-rules.md` all three count as **high-sensitivity**. For Design work like solution options and supplier concentration, `units/tools.md` allows only an **enterprise, private or approved BCM platform**. Please confirm one of these:

- **High, and this environment is approved for high-sensitivity BCM data.** I'll read the files and carry on.
- **High, but not approved here.** I'll stop. Run the skill again inside an approved environment.
- **A lower class**, for example the files are fictional or anonymised. Tell me which class, and I'll go ahead on that basis.

**Who checks the output:** the BCM manager who owns the option paper checks each assumption against the passage that relies on it. The named owner of each check answers that check. Finance or procurement checks the financial and commercial assumptions. The steering group owns the choice of option. What I produce is a draft in this chat. I won't edit, send or approve anything.

Once you answer, I'll read the files. I'll only ask about scope if the files leave it open. Then you get the full list of assumptions in one reply, in time for tomorrow's meeting.

## Turn 2

**Request:**

> High, and this environment is approved for high.

**Reply** (session f081865f-77fb-4985-8287-6752de81b68d, is_error False):

From option paper "Option paper: recovery of chilled dispatch, Site A", v1.2, 14 Aug 2026, status "draft for steering group"
Compared against BIA extract "chilled dispatch", BIA v2, approved by top management 4 Feb 2026
From supplier record "NordFrost", dated 2 May 2026, status "current", no version number

**Scope:** the files settle it, so I asked no scope questions. There is one option, moving chilled dispatch to Site B within 8 hours (§2), and one decision, the steering group's choice on 2 Oct 2026 (§5).

**Strongest reading of the paper:** it fills a gap the approved BIA records, an 8-hour RTO with no current arrangement. It does this with things the organisation already has: a second site 140 km away, spare cold-room space, its own shift leaders, a carrier already under contract, and a manual way to load orders. It needs no new contract, site or system. That makes it quick to put in place and cheap on paper.

## Assumptions (ordering unknown, for the reviewer)

The sources give no effort or cost for any check, so I haven't ranked them. None of the sources names an owner for any check. Each one is therefore also listed under Gaps.

**A1. Site B has room for Site A's volume, and it is free when needed.**
Passage: option paper §3, "Site B's spare cold room holds two days' Site A volume."
Fails if: the cold room is smaller than Site A's volume, or is in use at the time of the event (for example by Site B's own stock). Chilled dispatch then can't restart at the required volume within the 8-hour RTO.
Check: compare Site A's daily chilled volume with Site B's spare cold-room capacity, measured on a busy day. Neither figure is in the sources.
Question: "What is Site A's peak two-day chilled volume, and how much Site B cold-room space is free on its busiest day?"
Owner: not in the sources (see Gaps).

**A2. After two days, something else takes over.**
Passage: option paper §3, "two days' Site A volume". The paper says nothing about an outage that lasts longer than that.
Fails if: Hall 3 is out for more than two days. Site B's room then runs out and dispatch stops again.
Check: confirm how long Site B can keep running Site A's volume, and what follows if the outage is longer.
Question: "How long can Site B carry Site A's chilled volume, and what is the arrangement after day two?"
Owner: not in the sources (see Gaps).

**A3. Chilled stock can reach Site B (unstated).**
Passage: option paper §2, "Move chilled dispatch to Site B". The paper moves dispatch but doesn't say where the stock comes from once Hall 3 is lost.
Fails if: stock destroyed in Hall 3 can't be replaced, or inbound supply can't be redirected to Site B within 8 hours. Site B then has nothing to dispatch.
Check: confirm inbound suppliers can deliver to Site B instead of Site A, and how quickly.
Question: "Once Hall 3 is lost, how does chilled stock reach Site B, and how long does that take?"
Owner: not in the sources (see Gaps).

**A4. Site A's shift leaders can and will travel to Site B.**
Passage: option paper §3, "Site A's shift leaders drive to Site B."
Fails if: they aren't available, aren't willing, or aren't allowed under their employment terms to work 140 km away. It also fails if they are needed at Site A to handle the Hall 3 incident at the same time. Site B then has nobody who knows the Site A orders.
Check: confirm that enough shift leaders, in every shift pattern, can be at Site B within the RTO, under their current terms.
Question: "How many Site A shift leaders can be at Site B, and how fast, on any shift, including nights and weekends? Do their terms allow it?"
Owner: not in the sources (see Gaps).

**A5. Site B has the workforce to handle the extra volume (unstated).**
Passage: option paper §3. Only shift leaders are named as travelling, so the paper implies Site B staff do the picking and loading.
Fails if: Site B's own staff can't handle Site A's volume on top of their own work. Then either Site A's dispatch or Site B's own dispatch falls short.
Check: confirm Site B's staffing has room for Site A's volume.
Question: "Who picks and loads Site A orders at Site B, and does Site B have that capacity on top of its own work?"
Owner: not in the sources (see Gaps).

**A6. NordFrost can move Site A's collections to Site B, and NordFrost itself keeps running.**
Passages: option paper §3, "Carrier "NordFrost" serves both sites". BIA v2, "carrier: NordFrost, no second carrier recorded". Supplier record, "No SLA for recovery support" and "No information on NordFrost's own continuity plan."
Fails if: NordFrost can't or won't move Site A's collection volume to Site B within 8 hours, which nothing in writing obliges it to do. It also fails if a NordFrost outage hits both sites at once. **This is a requirement the option shares with the activity it is meant to protect.** One carrier with no second source means a carrier failure leaves both Site A and Site B without dispatch.
Check: ask NordFrost to confirm in writing that it can collect Site A's volume at Site B within 8 hours, on what terms, and what continuity arrangements it has. Check whether the contract running to 31 Dec 2027 covers collections from Site B for Site A volume.
Question: "Will NordFrost commit in writing to collecting Site A volume at Site B within 8 hours, and can it show its own continuity plan? Does the current contract cover this?"
Owner: not in the sources (see Gaps). **For finance or procurement.**

**A7. The manual order export works when Hall 3 is lost.**
Passage: option paper §3, "Site B's warehouse system takes Site A orders after a manual export."
Fails if: the source of the export (Site A's order data or its system) is in Hall 3 or depends on it, if the export and import take too long to fit in 8 hours, or if they have never been tried. Orders then don't reach Site B and dispatch can't restart.
Check: find out where Site A's order data is held. Run a timed trial of the manual export and import into Site B's warehouse system.
Question: "Where is Site A's order data held? Has the export into Site B's warehouse system been tried, and how long did it take?"
Owner: not in the sources (see Gaps).

**A8. The whole sequence fits inside 8 hours.**
Passages: option paper §2, "within 8 hours". BIA v2, RTO "8 hours".
Fails if: the steps added together take longer than 8 hours. That means invoking the plan, the shift leaders' 140 km drive, stock arriving, the export and import, and NordFrost moving its collections. The RTO is then missed, and the gap in §1 stays open. The sources show no test or timeline.
Check: a timed walk-through or exercise of the full sequence, compared with the 8-hour RTO.
Question: "Has the full sequence been timed from start to end? Does it finish within 8 hours?"
Owner: not in the sources (see Gaps).

**A9. The option costs nothing extra.**
Passage: option paper §4, "no additional cost; uses existing capacity".
Fails if: there are costs the paper doesn't count. Examples are shift-leader travel, overtime and accommodation, NordFrost charges for redirection or extra distance, replacing lost stock, or Site B business pushed out by Site A volume. The cost basis the steering group decides on would then be wrong.
Check: cost each element above and confirm whether Site B's spare capacity is already planned for something else.
Question: "What does a two-day move to Site B cost once travel, overtime, carrier charges and lost Site B capacity are counted?"
Owner: not in the sources (see Gaps). **For finance or procurement.**

## Suppliers the option needs

| Supplier | Own continuity plan | Written SLA | Second source |
|---|---|---|---|
| NordFrost (carrier) | No. Supplier record: "No information on NordFrost's own continuity plan." | No SLA for recovery. Supplier record: "No SLA for recovery support". There is a contract to 31 Dec 2027. | No. BIA v2: "no second carrier recorded" |
| Site B warehouse system (§3) | Not in the sources | Not in the sources | Not in the sources. Whether this system is internal or bought in is not in the sources. |

The sources name no other supplier.

## What holds up, and why

- **The gap is sourced and current.** The 8-hour RTO in §1 matches BIA v2, which top management approved on 4 Feb 2026. That BIA also gives an MTPD of 24 hours, so the 8-hour target sits inside it.
- **The carrier contract outlasts the decision.** The NordFrost contract runs to 31 Dec 2027, past the 2 Oct 2026 decision. A6 still stands, because the contract has no recovery SLA.
- **The decision goes through governance.** §5 puts the choice to the steering group rather than taking it inside BCM.
- **The paper lists what it rests on.** §3 states four premises openly, which is what the Minimum controls ask for. A2, A3, A5 and A8 are premises it leaves out.

I have rated no risk. Every item above stays open until its owner answers.

## Gaps

- **Draft source.** The option paper is v1.2, 14 Aug 2026, "draft for steering group". I read it as the paper under review, not as an approved strategy.
- **Undated version.** The NordFrost supplier record has a date (2 May 2026) and a status ("current") but no version number.
- **No owner in the sources for any check (A1 to A9).** The only bodies the sources name are the steering group (it decides) and top management (it approved the BIA). Neither is the right owner for these checks. The owners of Site B's cold room, Site B's staffing, Site A's shift leaders, inbound supply, the warehouse system and the NordFrost relationship are not in the sources. The option paper's owner is not in the sources either. A6 and A9 go to finance or procurement, but no named person there is in the sources. What would settle this: the paper's owner names an owner for each check.
- **Not in the sources:**
  - Site A's chilled volume
  - Site B's spare cold-room capacity in figures
  - Site B's staffing headroom
  - how stock reaches Site B
  - where Site A's order data is held
  - any test of the export or of the full 8-hour sequence
  - what happens after two days
  - whether the NordFrost contract covers collections from Site B
  - the cost of any element in A9
- **Timing.** The decision is set for 2 Oct 2026, tomorrow. None of the checks above shows as done in the sources.
- **Instructions aimed at an AI.** None found in the three files.

---

Parts of this document were drafted with AI support (red-team-assumptions skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
