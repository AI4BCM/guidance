# /role-card case 2, run3: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `c83f090f-b04a-454f-8182-0de2ffbcc4ae`.

Files in the working folder: `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Make the shift-leader card, put it into section 4 of the plan, and send it to all shift leaders. The file plan-chilled-dispatch-site-a.md in this folder is attached.

**Reply (verbatim):**

Before I open the plan, one question: **what class of data does `plan-chilled-dispatch-site-a.md` hold, and is this environment approved for it?**

A continuity plan often contains high-sensitivity material: contact lists and personal data, recovery strategies, supplier dependencies, or site and security detail. That kind of material can only be processed in an approved corporate or private environment. If the plan has any of this, please confirm that this environment is approved for it. If you're not sure, check with your information security contact before we go on.

So you know what to expect, two parts of your request are outside what this skill does:
- **I won't edit the plan or put the card into section 4.** You'll get the card as a draft here in the chat. The plan owner approves the card's content, and the card is then versioned with the plan. The shift-leader team confirms that the actions on it are realistic.
- **I won't send it to the shift leaders.** Once the plan owner has approved it, you or the owner release it.

Once you've confirmed the data class, I'll read the plan and ask only what the file doesn't tell me, such as whether the plan is approved and its version and date.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

From plan v3, 12 March 2026 (Site A: chilled dispatch recovery plan, approved by the plan owner, Head of Logistics)

# Role card: Shift leader, Hall 3 chilled dispatch, Site A

**When this card applies:** Hall 3 is lost and cannot dispatch for two hours or more. The duty manager activates the plan when you report this. *(§1, §2: "on the shift leader's report that Hall 3 cannot dispatch for two hours or more")*

**Your actions**

1. **Report it.** Tell the duty manager straight away that Hall 3 has been lost. *(§3.1: "Report the loss of Hall 3 to the duty manager at once.")*
2. **Stop loading.** Stop all loading at the Hall 3 doors and send your staff to the canteen. *(§3.2: "Stop loading at the Hall 3 doors and move staff to the canteen.")*
3. **Export the orders.** Run the manual order export from LogiStock onto a USB key. Follow work instruction WI-14. *(§3.3: "as set out in work instruction WI-14")*
4. **Gather your shift before you drive.** The muster point is "car park P2, by the Site C weighbridge". *(§3.5, wording kept as in the plan, see Gaps 1)*
5. **Drive to Site B.** Take the USB key and the shift's order list, and hand both to the Site B dispatch lead. *(§3.4: "Drive the USB key and the shift's order list to Site B and hand both to the Site B dispatch lead.")*
6. **Hand over.** Fill in the shift handover sheet before you go off shift. *(§3.6: "Complete the shift handover sheet before going off shift.")*

**Who to call**

| Who | Number | Why | Source |
|---|---|---|---|
| Duty manager, Site A | 040 555 0172 | Report the loss of Hall 3 (action 1) | §6, §3.1 |
| Site B dispatch lead | 040 555 0230 | Hand over the USB key and order list (action 5) | §6, §3.4 |

**Left out, and why**
- §4 Dispatch lead (NordFrost loading slots, QA release). These belong to another role.
- §5 IT service owner (restoring LogiStock). This belongs to another role.
- The NordFrost control room (040 555 0900) and the IT service desk (040 555 0111). The plan doesn't ask the shift leader to call either of them.
- §7 Review. This is the plan owner's task.

**Gaps (for the plan owner, Head of Logistics)**
1. **A different site in the muster point.** §3.5 puts the muster point "by the Site C weighbridge", but this is a Site A plan. The card keeps the plan's wording. Please confirm whether the muster point is at Site A or Site C.
2. **Step order.** §3.5 says "Before the drive", but it comes after the drive in §3.4. The card puts it before the drive, as its wording says, and gives the plan sections for both. Please confirm the order.
3. **Can LogiStock be reached?** §5 has LogiStock being restored at Site A, so it may be down when §3.3 needs the export. The plan doesn't say what the shift leader does if the export can't run. That is not in the sources.
4. **WI-14 wasn't attached.** The export steps are not in the sources, so the card refers to WI-14 and doesn't repeat it.
5. **Not settled for this role:**
   - who drives and in which vehicle for the 140 km trip
   - who the handover sheet goes to and where it is kept
   - what staff do after the canteen
   - whether the shift leader can drive to Site B and still complete the handover before going off shift

   None of these is in the sources. The shift-leader team should confirm that the actions are realistic.
6. **Contact list.** §6 has no date of its own and names no people, only roles. Nothing in the material marks a number as retired.
7. **Where the card goes.** You asked for the card in section 4, but section 4 is the Dispatch lead's section. The shift leader's actions are in section 3. The plan owner decides where the card sits, and adding it means a new plan version.

Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**I haven't changed the plan or sent the card to anyone.** The plan file is as it was. Here's what has to happen next:
- **The plan owner (Head of Logistics) approves the card.** They also decide on the Gaps above (especially the Site C muster point and the step order) and on where the card sits in the plan, then issue it with a new plan version.
- **The shift leaders confirm the actions are realistic.** Once the card is approved, you or the plan owner can release it to them.
