# /red-team-assumptions on Claude Code: case 1, final round

Date 2026-10-01. Skill text at commit f05ad10 (guidance repo HEAD). Claude Code 2.1.284, `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, fresh scratch folder (`evals-roundA/red-team-assumptions/1`) with the case files copied in (bia-extract-dispatch.md, option-paper-dispatch.md, supplier-record-nordfrost.md); later turns with `--resume`. Session 56c0ae2f-a25b-4283-a100-023f76862705. One run; no crash. Turn 1 attempted one `ls` through Bash, denied by the permission mode; no attachment was read before the data class was answered.

## Turn 1

**Request:**

> /red-team-assumptions The three files in this folder (option-paper-dispatch.md, bia-extract-dispatch.md, supplier-record-nordfrost.md) are attached. The steering group meets tomorrow.

**Reply** (is_error False):

Before I open the three files, one question about what's in them.

**What class of data do the option paper, the BIA extract and the Nordfrost supplier record hold, and is this environment approved for that class?**

From the file names, they probably include material that counts as high-sensitivity under the AI4BCM data rules:
- BIA data
- recovery strategies and design assumptions
- supplier weaknesses and contractual dependencies
- board or steering-group papers

The rules allow high-sensitivity material only in an approved corporate, private or purpose-built BCM environment. A public or unapproved tool doesn't qualify.

Please confirm one of these:
1. **High-sensitivity, and this environment is approved for it.** I'll read the files and continue.
2. **Lower class than that.** Tell me which, and I'll continue on that basis.
3. **High-sensitivity, and this environment isn't approved, or you're not sure.** I'll stop here and won't read the files. Run the review in your approved environment instead.

If any file holds passwords, keys or access tokens, remove them first. They can't go into any tool, approved or not.

Once that's settled, I'll read the files and ask about scope only if they leave it open. The output will be a draft list of the assumptions the option depends on, for you to review. I won't change any of the files. The BCM manager who owns the option paper checks each assumption against the passage it comes from. Each check's owner answers their check, finance or procurement checks the financial and commercial ones, and the steering group makes the choice.

## Turn 2

**Request:**

> high, and this environment is approved for high

**Reply** (is_error False):

I didn't need to ask about scope. The files cover one option (move chilled dispatch to Site B), one decision (the steering group's choice on 2 Oct 2026) and one short paper, so I read all of it.

**Sources read**
- Option paper v1.2, 14 Aug 2026, status "draft for steering group" (listed under Gaps)
- BIA v2, approved by top management 4 Feb 2026 (the extract for chilled dispatch)
- NordFrost supplier record, 2 May 2026, status "current", no version number (listed under Gaps)

**Reviewer:** the BCM manager who owns the option paper checks each assumption against its passage. Each check's owner answers it. Finance or procurement checks the items marked for them. The steering group owns the choice. This is a draft for review. I approved, recorded and changed nothing.

---

## Draft: what the Site B option needs to be true

**What the option promises (steelman).** Chilled dispatch restarts at Site B within the 8-hour RTO in BIA v2. It uses capacity, staff, a carrier and a warehouse system that already exist, and it costs nothing extra. The paper rests that on the four points in its §3. The 8 hours sits inside the 24-hour MTPD.

### Assumptions to check

Order of checks: unknown, for the reviewer. The sources give no effort or cost for any check.

**A1. Site B's spare cold room is free and holds two days of Site A volume.** (Option paper §3: "Site B's spare cold room holds two days' Site A volume.")
- Fails if the room is smaller than stated, or Site B is using it when the incident happens. Either way there's nowhere to stage Site A's chilled volume, and the option doesn't recover dispatch.
- Check: measure the room against Site A's two-day chilled volume and Site B's own use of it at peak.
- Owner: none in the sources (see Gaps).

**A2. Hall 3 is back, or another arrangement takes over, within two days.** (Unstated. §3 sizes the room for "two days'" volume. Neither §2 nor the BIA extract says how long Hall 3 would be lost.)
- Fails if Hall 3 is out for longer than two days. After day two the option has no stated arrangement, and dispatch stops again.
- Check: what outage length does the Hall 3 loss scenario assume, and what covers day three onward?
- Owner: none in the sources (see Gaps).

**A3. Site A's product reaches Site B to be dispatched.** (Unstated. §2: "Move chilled dispatch to Site B". No passage says how stock gets there, or whether inbound deliveries are redirected.)
- Fails if the stock is lost with Hall 3, or inbound deliveries can't be redirected. Then there's nothing to dispatch from Site B, and the RTO is missed whatever happens with A1, A4 and A5.
- Check: where does Site A's chilled stock come from once Hall 3 is lost, and can it reach Site B within 8 hours?
- Owner: none in the sources (see Gaps).

**A4. Site A's shift leaders can and will drive to Site B, 140 km away, and stay as long as needed.** (Option paper §3: "Site A's shift leaders drive to Site B."; §2: "140 km away, within 8 hours".)
- Fails if enough shift leaders aren't available, can't be called in time, or can't stay for several days. Site B would then have nobody who runs Site A's dispatch, and the 8 hours slips.
- Check, as a question for Site A's shift leaders (proposed, to confirm): "How many of you could be at Site B within the 8 hours, from any point in the shift pattern, and stay for two days or more? Can you work Site B's warehouse system?"

**A5. NordFrost can move Site A's collections to Site B within 8 hours and still deliver to Site A's customers on time.** (Option paper §3: "Carrier "NordFrost" serves both sites."; BIA v2: "carrier: NordFrost, no second carrier recorded"; supplier record: "No SLA for recovery support.")
- Fails if NordFrost can't redirect vehicles, add capacity, or reach Site A's customers from 140 km further away in time. The option also shares its only carrier with the site it protects, so a disruption at NordFrost stops dispatch at both sites and the option recovers nothing.
- Check, as a question for NordFrost (proposed, to confirm): "Within 8 hours of a call, can you collect Site A's volume at Site B on top of Site B's own, and keep Site A's delivery windows? Do you have a continuity plan of your own, and can we see it?"
- For finance or procurement: there's no recovery SLA, so any commitment NordFrost gives today isn't contractual.

**A6. Site A's orders can be exported and loaded into Site B's warehouse system within the 8 hours.** (Option paper §3: "Site B's warehouse system takes Site A orders after a manual export.")
- Fails if the export depends on systems or people lost with Hall 3, or if the manual export and load of two days of orders hasn't been tested and takes longer than the time left in the 8 hours. Then orders can't be picked or shipped at Site B.
- Check: where does the export run, does it survive the Hall 3 loss, has the import into Site B's system been tested, and how long does it take?
- Owner: none in the sources (see Gaps).

**A7. All of the above fits inside 8 hours, run in sequence or in parallel.** (Option paper §2: "within 8 hours"; §1: required RTO "8 hours". The paper gives no timeline.)
- Fails if detection and decision, travel (A4), preparing the cold room (A1), moving stock (A3), redirecting the carrier (A5) and loading orders (A6) together take more than 8 hours. The RTO is missed even if each step works on its own.
- Check: a timed walk-through, hour by hour, from the loss of Hall 3 to the first chilled dispatch leaving Site B.
- Owner: the paper's owner, who isn't named in the sources (see Gaps).

**A8. The option costs nothing extra.** (Option paper §4: "no additional cost; uses existing capacity".)
- For finance or procurement.
- Fails if travel, accommodation and overtime for the shift leaders, extra carrier distance and charges, or the cost of tying up Site B's cold room add up to a real cost. The stated basis for the choice ("no additional cost") would then be wrong.
- Check: cost two days, and a longer outage (see A2), against the existing NordFrost contract and Site A staff terms.
- Owner: none in the sources (see Gaps).

### Suppliers the option needs

| Supplier | Own continuity plan shown? | Written SLA? | Second source? |
|---|---|---|---|
| NordFrost (carrier) | No: "No information on NordFrost's own continuity plan." (supplier record) | Contract to 31 Dec 2027, but "No SLA for recovery support." (supplier record) | No: "no second carrier recorded" (BIA v2) |

The sources name no other supplier. Anything behind Site B's warehouse system or the cold room's refrigeration is not in the sources.

### What holds up
- **The RTO matches the approved BIA.** The paper's 8 hours (§1) is the RTO in BIA v2, approved 4 Feb 2026, and it sits inside the 24-hour MTPD.
- **The gap is stated plainly.** §1, "current arrangement has none", agrees with the BIA, which records no fallback.
- **The NordFrost contract runs past the decision.** It runs to 31 Dec 2027 (supplier record), so the carrier relationship the option uses exists today. Whether it covers recovery work is A5.
- **The sites are 140 km apart** (§2), so a local event at Site A is unlikely to hit Site B directly. The shared dependency is the carrier (A5), not the location.

### Gaps
- **Draft source.** The option paper is v1.2, 14 Aug 2026, "draft for steering group". I read it as the paper under review, not as an approved position.
- **No version number.** The NordFrost supplier record is dated 2 May 2026 and marked "current" but has no version number.
- **No owner named in the sources for these checks.**
  - A1 and A2: Site B's cold room capacity and the outage-length assumption. Settled by whoever runs Site B and owns the Hall 3 scenario.
  - A3: stock and inbound supply.
  - A6: the warehouse system export and import.
  - A7: the timed walk-through. The paper names no author or owner.
  - A8: cost (for finance or procurement).
  - The option paper itself has no named owner. The steering group decides, but nobody in the sources answers for the paper.
- **Not in the sources.**
  - How long Hall 3 would be lost.
  - Where Site A's chilled stock comes from after the loss.
  - Any test of the export and import between the warehouse systems.
  - Any supplier behind Site B's systems or refrigeration.
- **Intake.** I asked no scope questions, so none of this rests on statements from you.
- **Prompt injection.** None found in the three files.

---

> Parts of this document were drafted with AI support (red-team-assumptions, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
