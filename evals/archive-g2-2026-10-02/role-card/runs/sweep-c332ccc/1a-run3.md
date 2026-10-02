# /role-card case 1a, run3: Claude Code, guidance at c332ccc

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `dae54782-d6cf-4096-aa67-6ac2157a2bc5`.

Files in the working folder: `contact-list-site-a.md`, `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Make the shift-leader card from the dispatch plan. The files plan-chilled-dispatch-site-a.md and contact-list-site-a.md in this folder are attached.

**Reply (verbatim):**

Before I open either file, I need to know what class of data they hold. That decides whether this environment is allowed to handle them.

**What sensitivity class do `plan-chilled-dispatch-site-a.md` and `contact-list-site-a.md` fall under, and is this environment approved for that class?**

The AI4BCM data rules (`units/data-rules.md`, Sensitivity classes) put both kinds of file in the **high** class:
- **Contact lists and personal data** (names, phone numbers) count as high sensitivity.
- **Recovery strategies and site detail** in a dispatch plan count as high sensitivity too.

High-sensitivity material may only go into an approved corporate or private environment, meaning an enterprise or private setup that has passed the checks in `units/tools.md`, "Before you approve a tool". Please confirm one of these:

1. **High, and this environment is approved for high-sensitivity BCM data.** I'll read both files and start the card.
2. **Lower class** (for example, the files are anonymised or fictional training material). Tell me which class and I'll go ahead on that basis.
3. **Not sure, or not approved.** I'll stop here. Once the files are in an approved environment, or redacted to a class this one allows, you can run it again.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

The request and the files already answer the three intake questions, so I've gone straight to the draft. The **plan owner, Head of Logistics**, approves the card's content and versions it with the plan. The **Site A shift team that uses the plan** confirms the roles and actions are realistic. I haven't changed, saved or sent anything. The card exists only in this chat.

---

**From plan v3, 12 March 2026** (Site A chilled dispatch recovery plan, approved by the plan owner, Head of Logistics)
**Compared against contact list v7, 1 September 2026** (Site A emergency contact list, approved by the BCM manager, Site A)

## Role card: Shift leader, Site A chilled dispatch (Hall 3)

**When this card applies**
- Hall 3 cannot dispatch for two hours or more. Your report to the duty manager is what activates the plan. (§1, §2: "on the shift leader's report that Hall 3 cannot dispatch for two hours or more")

**Your actions**
1. **Tell the duty manager straight away that Hall 3 is down.** (§3.1: "Report the loss of Hall 3 to the duty manager at once.") Duty manager, Site A: **040 555 0172** (§6). *See Gap 1. The contact list says this number no longer answers.*
2. **Stop loading at the Hall 3 doors and send staff to the canteen.** (§3.2: "Stop loading at the Hall 3 doors and move staff to the canteen.")
3. **Run the manual order export from LogiStock onto a USB key**, following work instruction WI-14. (§3.3: "as set out in work instruction WI-14")
4. **Drive the USB key and this shift's order list to Site B** (140 km away) and hand both to the Site B dispatch lead. (§3.4; distance from §1) Site B dispatch lead: **040 555 0230** (§6).
5. **Before you set off, gather your shift at the muster point: "car park P2, by the Site C weighbridge".** (§3.5) *See Gap 2 and Gap 3.*
6. **Fill in the shift handover sheet before you go off shift.** (§3.6: "Complete the shift handover sheet before going off shift.")

**Numbers you call**

| Who | Number | Source |
|---|---|---|
| Duty manager, Site A | 040 555 0172 (*see Gap 1*) | §6 |
| Site B dispatch lead | 040 555 0230 | §6 |

**Left out, and why**
- §4 (dispatch lead: NordFrost loading slots, QA release) belongs to the dispatch lead, not the shift leader.
- §5 (IT service owner: restore LogiStock within six hours) belongs to the IT service owner.
- The NordFrost control room (040 555 0900) and IT service desk (040 555 0111) numbers in §6: the plan gives the shift leader no action that calls either one.
- §7 (annual review) is a task for the plan owner.
- The steps inside WI-14 aren't attached, so they aren't on this card. The card only points to WI-14.

### Gaps
1. **The duty manager's number is retired (needs the plan owner's decision).** Plan v3 §6 gives "040 555 0172". Contact list v7 (1 Sep 2026) says "040 555 0172 retired 1 Aug 2026; the line no longer answers" and gives 040 555 0180. The card keeps the plan's number unchanged. Action 1 is the one that activates the plan, so as written the shift leader would be calling a dead line. Only the plan owner can correct it, with a new plan version.
2. **The muster point names another site.** §3.5 puts the Site A muster point "by the Site C weighbridge". The card keeps this wording. Question for the reviewer: is this point really at Site A, or was it copied from the Site C plan?
3. **Canteen or muster point?** §3.2 sends staff to the canteen. §3.5 gathers the shift at the muster point "before the drive". Question for the reviewer: should staff go to the canteen first and then the muster point, or is one of these wrong? The plan also lists the muster step (3.5) after the drive step (3.4), although it says to muster first. The card puts mustering before the drive, as the words of §3.5 say.
4. **Is it realistic for the shift leader to leave?** Questions for the shift team: who leads the shift while the shift leader drives 140 km to Site B (§3.4)? And can the handover sheet (§3.6) be finished before going off shift if the shift leader is still on the road? The plan doesn't settle either point.
5. **WI-14 isn't attached.** Its steps and version are not in the sources. If the export depends on a working LogiStock, the plan doesn't say what the shift leader does when LogiStock is also down (§5 plans for restoring it).
6. **The attached plan is only part of it.** The plan says it "Stands in for the full plan; the sections below are the ones that name roles". The full plan may hold more shift-leader actions that I haven't seen.
7. **From your request, not from a source:** the audience is the shift leader and the format is a role card.

Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next step:** send the card to the Head of Logistics with Gaps 1–3. Gap 1 needs fixing before the card goes into use: the duty manager's number on it is the retired one, and calling that number is what activates the plan.
