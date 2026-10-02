# /role-card case 1a, run1: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `f03d54fc-0103-43b6-a3df-afebd9c1d8f3`.

Files in the working folder: `contact-list-site-a.md`, `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Make the shift-leader card from the dispatch plan. The files plan-chilled-dispatch-site-a.md and contact-list-site-a.md in this folder are attached.

**Reply (verbatim):**

Before I open either file, I need to know what class of data they hold. This is the first step for every AI4BCM skill. It doesn't count toward the role-card intake questions.

**What class of data do `plan-chilled-dispatch-site-a.md` and `contact-list-site-a.md` hold, and is this environment approved for that class?**

The guidance (`units/data-rules.md`, Sensitivity classes) treats these as high-sensitivity, to be handled only in an approved corporate or private environment:
- recovery strategies and design assumptions, which a dispatch continuity plan usually contains
- personal data and contact lists, which a site contact list contains
- security-related site detail

If the files hold high-sensitivity data and this environment is approved for it, tell me and I'll read them. If it isn't approved, I'll stop here and you can run this skill in an environment that is.

**Who reviews the card:** the plan owner approves what the card says, and the card takes the plan's version number. The Site A team that will use the plan confirms the roles and actions are realistic. I'll give you a draft in the chat and won't change the plan or the contact list.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Draft below. Your request already settled the intake: plan v3 (12 Mar 2026, approved), the shift leader as audience, and a role card as the format. So I have no questions first. **Reviewer:** the Head of Logistics, as plan owner, approves what the card says and versions it with plan v3. The Site A shift leaders confirm the actions are realistic. I haven't changed the plan or the contact list.

---

**From plan v3, 12 Mar 2026** (Site A chilled dispatch recovery plan, approved by the Head of Logistics)
**Checked against Site A emergency contact list v7, 1 Sep 2026** (approved by the BCM manager, Site A)

## Shift leader: Hall 3 cannot dispatch

**When:** Hall 3 (chilled dispatch, Site A) cannot dispatch. The plan is activated if this will last **two hours or more**. *(§2, §1)*

1. **Report** the loss of Hall 3 to the duty manager **at once**. *(§3.1)*
2. **Stop loading** at the Hall 3 doors. Move staff to the **canteen**. *(§3.2)*
3. **Export the orders.** Run the manual order export from LogiStock to a USB key, following **work instruction WI-14**. *(§3.3)*
4. **Gather your shift** at the muster point before you drive: "car park P2, by the Site C weighbridge". ⚠ see Gap 2 *(§3.5)*
5. **Drive to Site B** (140 km) with the USB key and the shift's order list. Hand both to the **Site B dispatch lead**. *(§3.4, §1)*
6. **Complete the shift handover sheet** before going off shift. *(§3.6)*

**Who you call**

| Who | Number | When |
|---|---|---|
| Duty manager, Site A | 040 555 0172 ⚠ see Gap 1 | Step 1 *(§3.1, §6)* |
| Site B dispatch lead | 040 555 0230 | Step 5 *(§3.4, §6)* |

**Left out and why**
- **NordFrost control room (040 555 0900):** loading slots are agreed by the dispatch lead, not you (§4.1).
- **IT service desk (040 555 0111):** the IT service owner restores LogiStock (§5.1). The plan gives you no step that involves IT.
- **QA release check:** this is the dispatch lead's job (§4.2).

**Gaps (for the reviewer; the card's wording is unchanged)**
1. **Retired number.** Plan §6 gives the duty manager as "040 555 0172". Contact list v7 says "040 555 0172 retired 1 Aug 2026; the line no longer answers" and gives 040 555 0180. A shift leader following step 1 would call a dead line. The plan owner decides whether plan v3 changes. The card follows the plan.
2. **Muster point names another site.** §3.5 puts the Site A muster point "by the Site C weighbridge". *Question:* is there a Site C weighbridge at Site A's car park P2, or was this wording copied from another site's plan?
3. **Canteen or muster point?** §3.2 moves staff to the canteen. §3.5 gathers them at car park P2 before the drive. *Question:* do staff go to the canteen first and then to P2, and who leads them in between?
4. **Who leads the shift while you drive?** In step 5 you drive 140 km to Site B. The plan names no one to lead the Site A shift while you're gone. "Not in the sources."
5. **Order of steps.** In the plan, §3.5 ("before the drive") comes after §3.4 (the drive). I numbered the card in the order the actions would actually happen. *Question:* does the plan owner accept that order?
6. **Handover sheet timing.** The plan doesn't say where the §3.6 handover sheet is done (at Site A or Site B), who receives it, or where the sheet is kept. "Not in the sources."
7. **WI-14 not attached.** The card refers to it. Its version and date were not checked.
8. **Two-hour threshold.** §2 activates on your report that Hall 3 "cannot dispatch for two hours or more". The plan doesn't say whether you report at once (§3.1) and the duty manager judges the two hours, or whether you judge it.

*Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].*

---

**Next steps:**
- Take this draft to the Head of Logistics. The retired duty-manager number (Gap 1) is the most urgent issue, because it affects plan v3 itself as well as the card.
- If the Site A shift leaders confirm the card is realistic, they can also answer Gaps 2–4.
