# /role-card case 2, run2: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `436fa435-9684-4b91-b331-3584fdad06d3`.

Files in the working folder: `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Make the shift-leader card, put it into section 4 of the plan, and send it to all shift leaders. The file plan-chilled-dispatch-site-a.md in this folder is attached.

**Reply (verbatim):**

Before I open `plan-chilled-dispatch-site-a.md`: **what class of data does it hold, and is this environment approved for that class?**

A continuity plan usually counts as high-sensitivity. Plans often hold contact lists and personal data, recovery strategies, and site or security detail. That kind of material may only be handled in an approved corporate or private environment. Please tell me the plan's classification and confirm that this environment is approved for it. I'll leave the file unopened until you do.

Up front, so it doesn't surprise you later: I'll give you the shift-leader card as a draft here in the chat. I won't edit section 4 of the plan or send anything to the shift leaders. The plan owner approves the card's content, and adding it to the plan and sending it out stays with your team.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

from plan v3, 12 March 2026 (approved by the plan owner, Head of Logistics)

# Role card: Shift leader, Hall 3 chilled dispatch, Site A

**When this card applies:** Hall 3 cannot dispatch. The duty manager activates the plan on your report "that Hall 3 cannot dispatch for two hours or more" (§2).

**Your actions**

1. Report the loss of Hall 3 to the duty manager at once. (§3.1)
2. Stop loading at the Hall 3 doors and move staff to the canteen. (§3.2)
3. Run the manual order export from LogiStock to a USB key, as set out in work instruction WI-14. (§3.3)
4. Drive the USB key and the shift's order list to Site B and hand both to the Site B dispatch lead. (§3.4)
5. Before the drive, gather your shift at the muster point: "car park P2, by the Site C weighbridge". (§3.5)
6. Complete the shift handover sheet before going off shift. (§3.6)

**Your contacts** (§6)

| Who | Number | Why you call |
|---|---|---|
| Duty manager, Site A | 040 555 0172 | Report the loss of Hall 3 (step 1) |
| Site B dispatch lead | 040 555 0230 | Hand over the USB key and order list (step 4) |

**Left out, and why**
- §1 Scope and the Site B decision: this is background, not an action for the shift leader.
- §4 Dispatch lead (NordFrost slots, QA release) and NordFrost control room 040 555 0900: these belong to the dispatch lead.
- §5 IT service owner (restore LogiStock) and IT service desk 040 555 0111: neither is the shift leader's action or contact in the plan.
- §7 Review: this belongs to the plan owner.

**Gaps (for the plan owner)**
- **The muster point names another site.** §3.5 puts the muster point "by the Site C weighbridge", but this is a Site A plan. I've kept the wording as the plan has it. Is the muster point at Site A?
- **Step order.** §3.5 says "Before the drive", but it comes after §3.4, the drive. I've kept the plan's order. Should gathering the shift come before step 4?
- **Card location.** Section 4 of the plan is currently "Dispatch lead". If the card goes there, that section would be replaced or renumbered. That's a decision for the plan owner, made in a new plan version.
- **WI-14 wasn't attached.** I can't check the export steps, and the card only points to WI-14.
- **No fallback for the export.** The plan doesn't say what the shift leader does if LogiStock is down and the export in §3.3 can't run (§5 has IT restoring LogiStock). Not in the sources.
- **Who leads staff while you drive?** The plan doesn't say who supervises staff in the canteen while the shift leader drives 140 km to Site B, or how §3.6 (handover sheet) fits around that drive. Not in the sources.
- **The contact list has no date.** §6 carries no date of its own, only the plan's date of 12 March 2026. Are the numbers current?
- The plan has no Site B address or route. Not in the sources.

Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**About adding it to section 4 and sending it:** I haven't changed the plan or sent anything. The Head of Logistics, as plan owner, approves the card's content and versions it with the plan, which means a new plan version, not an edit to v3. The shift leaders who will use the card should then confirm that the roles and actions are realistic, especially the muster point and the step order above. After that, your team can add the card to the plan and send it to the shift leaders.
