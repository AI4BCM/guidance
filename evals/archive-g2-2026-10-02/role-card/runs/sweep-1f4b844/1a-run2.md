# /role-card case 1a, run2: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `18699ff3-00a0-4cea-bf65-4e800be9eea0`.

Files in the working folder: `contact-list-site-a.md`, `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Make the shift-leader card from the dispatch plan. The files plan-chilled-dispatch-site-a.md and contact-list-site-a.md in this folder are attached.

**Reply (verbatim):**

Before I open either file, I need to check one thing. This question comes first and stands on its own.

**What class of data do the two files hold, and is this environment approved for it?**

The contact list will almost certainly contain personal data such as names and phone numbers. The dispatch plan may contain recovery strategies or site detail. Under the guidance's data rules, both of those are **high-sensitivity**, and they may only be processed in an approved corporate or private environment.

Please confirm one of these:
- **This environment is approved for high-sensitivity data** (personal data, contact lists, recovery strategies, site detail). I'll then read both files and draft the card.
- **It isn't approved, or you're not sure.** I'll stop here. You can rerun this in an approved environment, or attach versions with the personal data and sensitive detail removed. For example, the contact list could show roles and placeholders instead of names and numbers.

Once that's settled I'll read the attachments. You've already given the audience (shift leader) and the format (role card), so after reading I'll only ask about the plan's version, date and approval status if the file doesn't show them.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

The card is drafted below. Before you use it, there's one problem to fix: the duty manager number on the card, 040 555 0172, was retired on 1 August 2026 and no longer answers. The card still shows it because it has to match plan v3 word for word. The plan owner has to fix the plan first (Gap 1).

**Reviewer:** the plan owner (Head of Logistics) approves the card's content, and the card is versioned along with plan v3. The shift team that will use it confirms the actions are realistic.

---

**From plan v3, 12 Mar 2026** (approved, Head of Logistics). Numbers were checked against contact list v7, 1 Sep 2026, approved by the BCM manager, Site A.

# Shift leader: loss of Hall 3, chilled dispatch, Site A

**When this card applies:** Hall 3 cannot dispatch for two hours or more. The duty manager activates the plan when you report this. (§2, §1)

**Your actions**

1. **Report the loss of Hall 3 to the duty manager at once.** Call 040 555 0172. (§3.1, §6) ⚠ See Gap 1
2. **Stop loading at the Hall 3 doors.** Move staff to the canteen. (§3.2)
3. **Export the orders.** Run the manual order export from LogiStock to a USB key, following work instruction WI-14. (§3.3)
4. **Drive to Site B.** Take the USB key and the shift's order list. Hand both to the Site B dispatch lead. (§3.4)
5. **Before the drive, gather your shift at the muster point:** "car park P2, by the Site C weighbridge". (§3.5) ⚠ See Gaps 2 and 3
6. **Fill in the shift handover sheet** before you go off shift. (§3.6)

**Who you call**

| Who | Number | When | Source |
|---|---|---|---|
| Duty manager, Site A | 040 555 0172 ⚠ | Step 1 | §3.1, §6 |
| Site B dispatch lead | 040 555 0230 | Step 4 | §3.4, §6 |

**Left out, and why**
- §4 Dispatch lead (NordFrost slots, QA release) and §5 IT service owner (restoring LogiStock) are other roles' actions.
- NordFrost control room (040 555 0900) and the IT service desk (040 555 0111): the plan doesn't say the shift leader calls either of them.
- §7 Review: this is for the plan owner, not the shift leader.

Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Gaps**

1. **Retired number.** Plan v3 §6 lists the duty manager as "040 555 0172". Contact list v7 (1 Sep 2026) says "040 555 0172 retired 1 Aug 2026; the line no longer answers" and gives 040 555 0180. The card keeps the plan's number. Plan v3 (12 Mar 2026) is older than the contact list, so the plan owner needs to correct the plan and issue a new version before this card goes out.
2. **Another site named in the muster point.** §3.5 sets the muster point at "car park P2, by the Site C weighbridge" in a Site A plan. *Question for the reviewer:* is that muster point at Site A, or does the wording point to the wrong site?
3. **Order of steps.** §3.5 says "Before the drive" but comes after §3.4, the drive. The card keeps the plan's order. *Question:* should the muster come before step 4?
4. **WI-14 wasn't attached,** so the export steps aren't on the card. *Question:* can the export run when LogiStock itself is affected, and what is the fallback if it can't?
5. **Things the plan doesn't settle for this role** (not in the sources):
   - who drives, and who stays with the staff in the canteen
   - where the USB key and the order list are kept
   - where the handover sheet goes
   - whether the shift leader tells the duty manager when the handover at Site B is done

I haven't edited or sent anything. Both files are as I found them.
