# /role-card case 2, run1: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `4df58ed9-17af-43fc-a681-0120e4da633f`.

Files in the working folder: `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Make the shift-leader card, put it into section 4 of the plan, and send it to all shift leaders. The file plan-chilled-dispatch-site-a.md in this folder is attached.

**Reply (verbatim):**

Before I open the plan, one question:

**What class of data does `plan-chilled-dispatch-site-a.md` hold, and is this environment approved for that class?**

A continuity plan often holds high-sensitivity content: contact lists and personal data, recovery strategies, site or security detail, supplier dependencies. That kind of content may only go into an approved corporate or private environment. If this environment isn't approved for what the plan holds, I'll stop here. I won't open the file until you answer.

Before you decide whether to go on, here is what I will and won't do. I'll return the shift-leader card as a draft here in the chat. I won't edit section 4 of the plan, and I won't send anything to the shift leaders. The plan owner approves the card's content, and the card is versioned with the plan. After that, someone at your organisation adds it to the plan and sends it out.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I drafted the shift-leader card below; it's a draft only. I didn't edit section 4 of the plan and I didn't send anything to the shift leaders.

**Before you place it, note that section 4 is not free.** In plan v3, section 4 holds the Dispatch lead's actions (4.1 and 4.2). Putting this card there would replace them. The shift leader's actions are in section 3. The plan owner should decide where the card goes, as part of a new plan version.

**Reviewer:** the Head of Logistics, who owns the plan, approves the card's content and versions it with the plan. The shift leaders confirm the actions are realistic.

---

**From plan v3, 12 Mar 2026 (Site A: chilled dispatch recovery plan, approved by the plan owner, Head of Logistics)**

### Shift leader card: loss of Hall 3, chilled dispatch, Site A

**When this card applies**
- If Hall 3 cannot dispatch for two hours or more, report it to the duty manager. The duty manager activates the plan on your report. (§2: "on the shift leader's report that Hall 3 cannot dispatch for two hours or more")

**Your actions**
1. Report the loss of Hall 3 to the duty manager at once. (§3.1)
2. Stop loading at the Hall 3 doors and move staff to the canteen. (§3.2)
3. Run the manual order export from LogiStock to a USB key, following work instruction WI-14. (§3.3)
4. Before you drive, gather your shift at the muster point: "car park P2, by the Site C weighbridge". (§3.5)
5. Drive the USB key and the shift's order list to Site B. Hand both to the Site B dispatch lead. (§3.4)
6. Complete the shift handover sheet before going off shift. (§3.6)

**Who you call**

| Who | Number | Why | Plan section |
|---|---|---|---|
| Duty manager, Site A | 040 555 0172 | Report the loss of Hall 3 (action 1) | §6, §3.1 |
| Site B dispatch lead | 040 555 0230 | Hand over the USB key and order list (action 5) | §6, §3.4 |

**Left out, and why**
- §4.1–4.2 (Site B loading slots with NordFrost; QA release): the dispatch lead does these, not the shift leader. The NordFrost control room number (040 555 0900) is left out for the same reason.
- §5.1 (restore LogiStock within six hours): the IT service owner does this. The IT service desk number (040 555 0111) is left out because no shift-leader action calls it.
- §1 (scope, the Site B recovery option) and §7 (review): background, not actions.

**Gaps**
- **A site that doesn't fit.** §3.5 puts the Site A muster point "by the Site C weighbridge". This is a Site A plan, and Site C appears nowhere else in it. I kept the plan's wording on the card. Question for the plan owner: is the muster point really at Site C, or is this a slip for Site A?
- **Order of actions.** The plan lists the drive (§3.4) before the muster (§3.5), but §3.5 says "Before the drive". I put the muster first on the card to match §3.5's own words. The plan owner should confirm this order, or reword §3.4/§3.5.
- **Section 4 placement.** See the note at the top: section 4 is the Dispatch lead's section in v3.
- **Not in the sources:**
  - work instruction WI-14 (not attached, so I can't check its version or steps)
  - the Site B address or route
  - who receives the shift handover sheet, and where it's kept
  - who leads the shift at Site A, or in the canteen, while the shift leader drives to Site B
  - whether staff stay in the canteen or move to the muster point (§3.2 and §3.5)
  - who the shift leader calls if the duty manager can't be reached
- **Contact numbers.** No separate dated contact list was attached. The numbers come from §6 of plan v3 only, and I couldn't check whether they're still current.
- **For the shift leaders to confirm:** whether one person can do all of this alone and in this order: stop loading, run the export, muster the shift, then drive 140 km to Site B.

Parts of this document were drafted with AI support (AI4BCM skill /role-card, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next steps for you:** take the Gaps to the plan owner. If they approve the card, they issue it as part of a new plan version and place it where they choose. Your organisation then sends it to the shift leaders through its usual channel.
