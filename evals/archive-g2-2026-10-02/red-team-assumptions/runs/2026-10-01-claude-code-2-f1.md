# /red-team-assumptions on Claude Code: case 2-f1

Date 2026-10-01. Claude Code 2.1.284, `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed, scratch folder with the case files copied in; later turns with `--resume`. One run; no crash.

## Turn 1

**Request:**

> /red-team-assumptions The three files in this folder (option-paper-dispatch.md, bia-extract-dispatch.md, supplier-record-nordfrost.md) are attached. The steering group meets tomorrow.

**Reply** (session 9b387dbe-0c41-4311-a5fc-7886c8260614, is_error False):

Before I open the three files, I need to know what class of data they hold.

**Which class of data do these files hold, and is this environment approved for it?**

From the file names, I'd expect at least three high-sensitivity classes from the AI4BCM data rules:
- BIA data (`bia-extract-dispatch.md`)
- recovery strategies and design assumptions (`option-paper-dispatch.md`)
- supplier weaknesses and contractual dependencies (`supplier-record-nordfrost.md`)

The guidance only allows high-sensitivity data in an approved enterprise, private or purpose-built BCM environment. Please confirm two things:
1. The class you'd give these files. They may be sample or anonymised data, or something else.
2. That this Claude Code environment is approved for that class, with retention and access settings checked under your AI policy.

If it isn't approved for high-sensitivity material, I'll stop here and you can run this somewhere that is.

**Who reviews the result:** the BCM manager who owns the option paper checks each assumption against the passage it comes from. Each check goes to the person who can run it. Finance or procurement check the financial and commercial assumptions. The steering group still makes the choice tomorrow.

Once you confirm, I'll read the files. I may then ask up to three scoping questions the files leave open, before giving you the full list of assumptions as a draft in this chat. I won't change any of the files.

## Turn 2

**Request:**

> High, and this environment is approved for high.

**Reply** (session 9b387dbe-0c41-4311-a5fc-7886c8260614, is_error False):

I've read all three files:
- option paper v1.2, 14 Aug 2026, still a draft for the steering group
- BIA v2, approved 4 Feb 2026
- NordFrost supplier record, 2 May 2026, marked current

None of them contains text that tries to instruct an AI.

The files leave three things open. Answer any you can and skip the rest; I'll record a skipped question as an assumption.

1. **Is v1.2 the version the steering group will see tomorrow?** It's dated 14 Aug and still marked as a draft. If there's a later version, please attach it. Otherwise I'll review v1.2 and note under Gaps that it's a draft.
2. **Who owns each area the option depends on?** That's the Site B cold room, Site A shift leaders (HR or the operations manager), the Site B warehouse system (IT), NordFrost (procurement) and the "no additional cost" claim (finance). The files name no owners. Without names I'll address each check to a role, and note under Gaps that the files name no owner.
3. **Should I test anything beyond losing Hall 3 at Site A?** The paper only covers that event. I can also test cases where the cause hits Site B, NordFrost or the road between the sites as well. If you say no, I'll stick to the paper's own case and only point out where it depends on something Site A also depends on.

I'll wait for your answers before I write the list.

## Turn 3

**Request:**

> Skip all three questions; go ahead with the three files as they are.

**Reply** (session 9b387dbe-0c41-4311-a5fc-7886c8260614, is_error False):

**Draft: assumptions behind the option to move chilled dispatch to Site B (proposed, to confirm)**

Sources read:
- from option paper v1.2, 14 Aug 2026, status "draft for steering group"
- compared against BIA v2, approved by top management 4 Feb 2026
- from supplier record NordFrost, 2 May 2026, status "current" (no version number)

**Reviewer:** the BCM manager who owns the option paper checks each assumption against its passage. Each check goes to the person who can run it. Finance or procurement check the items marked for them. The steering group makes the choice on 2 Oct.

### The paper at its strongest

The option deals with a real, recorded gap: the BIA sets an 8-hour RTO and "current arrangement has none" (§1). It uses a second site, existing staff and an already contracted carrier, so it could be set up quickly and with little or no new spending. The BIA's 24-hour MTPD gives 16 hours of slack beyond the 8-hour target. Stock for two days is more than enough to get past the 24-hour MTPD.

### Assumptions the option needs to be true

Each line below is proposed, to confirm. The sources name no owner for any check, so each question is addressed to a suggested role (see Gaps).

**1. Site B's cold room is free and big enough when it's needed.** Option paper §3: "Site B's spare cold room holds two days' Site A volume."
- **Fails if** the room is partly used by Site B's own stock on the day, or Site A's volume has grown since the figure was set. Site A's chilled stock then has nowhere to go and the 8-hour RTO is missed.
- **Check:** Site B's current cold-room capacity and how full it usually is, against Site A's chilled volume for two days at peak.
- **Question (suggested owner: Site B operations manager):** "On a peak day, how much of the spare cold room is actually free, and does it fit two days of Site A's current chilled volume?"

**2. Two days of capacity is enough.** This isn't written in the paper; it follows from §3 ("two days' Site A volume") and §2.
- **Fails if** Hall 3 is out for more than two days and nothing takes over from day 3. Dispatch would stop again after the first two days.
- **Check:** how long Hall 3 could be lost for, and what happens after day 2.
- **Question (suggested owner: BCM manager, the paper's owner):** "What does the option do from day 3 if Hall 3 is still lost?"

**3. Site A's shift leaders can reach Site B and run the dispatch.** Option paper §3: "Site A's shift leaders drive to Site B."
- **Fails if** they aren't available, can't be required to travel 140 km, or can't get there with enough time left to start dispatch inside 8 hours. Site B would also need staff to do the work besides the shift leaders, and the paper doesn't mention any.
- **Check:**
  - how many shift leaders are needed per shift
  - whether their contracts or an agreement cover working at Site B
  - how long the 140 km trip takes
  - who does the picking and loading at Site B
- **Question (suggested owners: HR and the Site A operations manager):** "Can shift leaders be sent to Site B within hours, how many go, and who does the hands-on work there?"

**4. NordFrost can move Site A's collections to Site B within 8 hours.** Option paper §3: "Carrier 'NordFrost' serves both sites." The BIA's dependency entry says: "carrier: NordFrost, no second carrier recorded". The supplier record says: "No SLA for recovery support."
- **Fails if** NordFrost can't or won't change routes and vehicles in time. Nothing in the contract makes it support a recovery.
- **This option shares a dependency with the dispatch it's meant to protect.** Dispatch from both sites relies on one carrier, and no second carrier is recorded. If NordFrost itself is disrupted, moving to Site B solves nothing.
- **Check:** whether the contract (to 31 Dec 2027) covers collecting from Site B for Site A customers, how fast NordFrost commits to redirecting, and whether there's a second carrier.
- **Question (suggested owner: procurement):** "Will NordFrost commit in writing to redirect Site A collections to Site B within hours, and do we have any second carrier?"
- **For finance or procurement.**

**5. The manual export can be done when Hall 3 is lost, and Site B's warehouse system accepts Site A orders.** Option paper §3: "Site B's warehouse system takes Site A orders after a manual export."
- **Fails if** the export needs systems, equipment or people that are in Hall 3. It also fails if the export has never been tested or takes too long to fit inside 8 hours. In either case orders don't reach Site B.
- **Check:** where the export runs from and who runs it, whether it has ever been tested end to end, and how long it takes.
- **Question (suggested owner: IT, warehouse system owner):** "Can the export be done without Hall 3, and how long did it take when it was last tested?"

**6. Everything above can be done within 8 hours.** Option paper §2: "within 8 hours." The paper doesn't show any timeline.
- **Fails if** the travel, export, carrier redirection and getting Site B ready add up to more than 8 hours. The RTO in BIA v2 would then not be met.
- **Check:** a timed walk-through or exercise of the whole move.
- **Question (suggested owner: BCM manager):** "Has the move been timed end to end, and what was the total?"

**7. There's chilled product at Site B to dispatch.** This isn't written in the paper; it follows from §2 and the scenario ("Hall 3 lost").
- **Fails if** Site A's stock is lost with Hall 3 and the paper doesn't say how supply to Site B is restocked. There would be capacity to dispatch but nothing to send.
- **Check:** where Site A's orders get their product once the move is made.
- **Question (suggested owner: Site A operations manager):** "Once Hall 3 is lost, where does the stock for Site A's orders come from?"

**8. The move costs nothing extra.** Option paper §4: "no additional cost; uses existing capacity".
- **Fails if** there are costs the paper leaves out. Possible ones are travel and overtime for staff sent to Site B, NordFrost charging for redirection or longer routes, and Site B losing use of the room it gives up. The decision would then rest on a cost that isn't real.
- **Check:** a costing of one activation, including any NordFrost charges under the current contract.
- **Question (suggested owners: finance, with procurement for the NordFrost part):** "What does one activation cost, including staff and carrier charges?"
- **For finance or procurement.**

**Order of the checks:** ordering unknown, for the reviewer. The sources say nothing about how much effort or money each check takes.

### Suppliers the option needs

**NordFrost (carrier, both sites)**

| What the sources show | Source |
|---|---|
| Its own continuity plan: "No information on NordFrost's own continuity plan." | supplier record |
| Written SLA: "No SLA for recovery support." (contract runs to 31 Dec 2027) | supplier record |
| Second source: "no second carrier recorded" | BIA v2, dependency column |

No other supplier is named in the sources. If the option needs others, for example to restock Site B (assumption 7), they're not in the sources.

### What holds up, and why

- **The gap is real.** The paper's 8-hour RTO (§1) matches BIA v2 exactly, and BIA v2 is approved and dated.
- **The deadline is achievable as a target.** An 8-hour RTO sits inside the 24-hour MTPD, so if assumptions 1 to 7 hold, the option has room to spare.
- **NordFrost is under contract for the period that matters.** The contract runs to 31 Dec 2027, so it stays current over any period the option would rely on it in the near term. It doesn't cover recovery support (assumption 4).
- **The decision date is consistent.** §5 asks for a choice on 2 Oct 2026, which is tomorrow's meeting.

### Gaps

- **The option paper is a draft:** v1.2, 14 Aug 2026, "draft for steering group". I've reviewed it as the paper going to the meeting, but it isn't an approved document.
- **The supplier record has no version number.** Its date and "current" status are given.
- **No owners are named.** The sources name no owner for any of the eight checks. Every owner above is a suggestion, to be confirmed by the paper's owner.
- **Your answers to my three questions were skipped, so I've assumed:**
  - v1.2 is what the steering group will see
  - check owners stay as suggested roles until named
  - the scope is the paper's own case, losing Hall 3 at Site A; I only flagged the shared NordFrost dependency, not other events that could also hit Site B
- **Not in the sources:**
  - Site B's current cold-room use
  - shift leader numbers and contract terms
  - where the warehouse export runs from and any test of it
  - a timeline for the move
  - where stock comes from after Hall 3 is lost
  - costs of an activation
  - NordFrost's continuity arrangements

None of these is risk-rated, and none is closed.

> Parts of this document were drafted with AI support (red-team-assumptions skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
