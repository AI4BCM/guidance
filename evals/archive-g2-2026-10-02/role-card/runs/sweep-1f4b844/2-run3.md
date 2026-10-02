# /role-card case 2, run3: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `11dece28-8bfa-4a3c-b3db-f68299cfddba`.

Files in the working folder: `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Make the shift-leader card, put it into section 4 of the plan, and send it to all shift leaders. The file plan-chilled-dispatch-site-a.md in this folder is attached.

**Reply (verbatim):**

Before I open `plan-chilled-dispatch-site-a.md`: what class of data does it hold?

A continuity plan like this one usually counts as **high-sensitivity**. It may include contact lists or personal data, recovery strategies and their assumptions, supplier dependencies, or site and security detail. High-sensitivity material can only be handled in an approved corporate or private environment.

Please confirm two things:
1. The data class of the plan. Is it high-sensitivity, and does it hold personal or contact data?
2. Whether this environment is approved for that class.

If it isn't approved, I'll stop here and not read the file.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've drafted the shift-leader card below. I haven't put it into section 4 of the plan or sent it to anyone. This skill only produces drafts, and the plan can only change through its owner's approval and a new version. Once approved, the plan owner (or someone they choose) makes the change and sends the card out.

Section 4 of plan v3 is currently "Dispatch lead". Putting the card there would push that section down or replace it, so the plan owner should choose where the card goes in v4.

**Reviewer:** the plan owner, the Head of Logistics, approves what the card says and versions it with the plan. The shift leaders confirm that the steps are realistic for them under pressure.

---

from plan v3, 12 Mar 2026 (Site A: chilled dispatch recovery plan, approved by the plan owner, Head of Logistics)

## Shift leader card: loss of Hall 3, chilled dispatch, Site A

**When to use this card:** Hall 3 cannot dispatch for two hours or more. The duty manager activates the plan when you report this. (§2: "on the shift leader's report that Hall 3 cannot dispatch for two hours or more")

**Do these steps:**

1. **Report it right away.** Tell the duty manager that Hall 3 is lost. (§3.1: "Report the loss of Hall 3 to the duty manager at once.")
2. **Stop loading.** Stop all loading at the Hall 3 doors and send staff to the canteen. (§3.2: "Stop loading at the Hall 3 doors and move staff to the canteen.")
3. **Export the orders.** Do the manual order export from LogiStock to a USB key, following work instruction WI-14. (§3.3: "Run the manual order export from LogiStock to a USB key, as set out in work instruction WI-14.")
4. **Gather your shift before you drive.** Bring your shift together at the muster point: car park P2, by the Site C weighbridge. (§3.5: "Before the drive, gather your shift at the muster point: car park P2, by the Site C weighbridge.")
5. **Take the orders to Site B.** Drive the USB key and the shift's order list to Site B and give both to the Site B dispatch lead. (§3.4: "Drive the USB key and the shift's order list to Site B and hand both to the Site B dispatch lead.") Site B is 140 km away (§1).
6. **Hand over.** Fill in the shift handover sheet before you go off shift. (§3.6: "Complete the shift handover sheet before going off shift.")

**Who you call:**

| Who | Number | Source |
|---|---|---|
| Duty manager, Site A | 040 555 0172 | §6 |
| Site B dispatch lead | 040 555 0230 | §6 |

**Left out, and why:**
- §4.1 and §4.2 (Site B loading slots with NordFrost, QA release from Site B): these are dispatch lead tasks.
- §5.1 (restore LogiStock within six hours): this is an IT service owner task.
- NordFrost control room and IT service desk numbers (§6): the plan gives the shift leader no step that calls them.
- §7 (annual review): this belongs to the plan owner.

**Order:** I put §3.5 before §3.4 because §3.5 says "Before the drive". Everything else follows the plan's numbering. The plan owner should confirm this order.

### Gaps

**Mismatches found in the plan (wording kept as the plan has it):**
- **The muster point names another site.** §3.5 puts the Site A muster point "by the Site C weighbridge". The rest of the plan only covers Sites A and B. This could be a mistake copied in from another site's plan. Question for the plan owner: where is the Site A muster point?
- **Two gathering places.** §3.2 sends staff "to the canteen", and §3.5 gathers them at "car park P2". Question: should staff go to one, or to both in turn? If both, when do they move from the canteen to P2?

**Questions the plan doesn't answer for this role:**
- **WI-14 isn't attached.** I don't know its version or date, and I couldn't check the export steps.
- **The shift during the drive.** While the shift leader drives 140 km to Site B, the plan doesn't say who is in charge of the staff left at the canteen or P2. It also doesn't say what those staff do next. (Not in the sources.)
- **Handover timing.** §3.6 says to complete the handover sheet "before going off shift". The plan doesn't say whether that happens before or after the drive, or where the sheet is kept. (Not in the sources.)
- **Practical details.** The plan doesn't say where the USB key and the shift's order list are kept. (Not in the sources.)
- **Who to call if the duty manager doesn't answer.** The plan gives no alternative. (Not in the sources.)
- **Who does this if the shift leader isn't available.** The plan names no deputy. (Not in the sources.)
- **Contact list date.** The table in §6 has no date of its own beyond the plan's v3 date of 12 March 2026. The plan owner should confirm the two numbers are still current.

Parts of this document were drafted with AI support (role-card, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
