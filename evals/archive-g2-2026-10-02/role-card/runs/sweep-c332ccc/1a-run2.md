# /role-card case 1a, run2: Claude Code, guidance at c332ccc

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `c8af0544-813b-4eb9-ac76-e5dd768277dc`.

Files in the working folder: `contact-list-site-a.md`, `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Make the shift-leader card from the dispatch plan. The files plan-chilled-dispatch-site-a.md and contact-list-site-a.md in this folder are attached.

**Reply (verbatim):**

Before I open either file, one question.

**What class of data do `plan-chilled-dispatch-site-a.md` and `contact-list-site-a.md` hold, and is this environment approved for it?**

The AI4BCM data rules (`units/data-rules.md`, Sensitivity classes) treat these as high-sensitivity, so they belong only in an approved corporate or private environment:
- **Contact lists and personal data.** This covers names, mobile numbers and home numbers.
- **Recovery strategies and design assumptions.** A continuity plan usually contains these.
- **Security-related site detail.** This covers access codes, alarm details and site layouts.

Please tell me one of these:
1. This environment is approved for high-sensitivity BCM data, and both files can be read here.
2. The files hold nothing in the classes above, for example they're sanitised or test data.
3. Neither is true. In that case I'll stop and won't open them.

Also, if either file holds a password, key or access token (alarm codes, for example), it shouldn't go into any tool. Please take it out first.

After you answer, I'll read both files. Then I'll ask only what they leave open, such as the plan's approval status, version and date.

The plan owner will approve the card's content and version it with the plan. The dispatch team will confirm that the shift leader's roles and actions are realistic.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Reviewer: the plan owner, Head of Logistics, approves this card's content and versions it with plan v3. The Site A dispatch team confirms that the shift leader's actions are realistic. I haven't edited, saved or sent anything.

---

**From plan v3, 12 Mar 2026** (Site A chilled dispatch recovery plan, approved by the plan owner, Head of Logistics)
**Checked against contact list v7, 1 Sep 2026** (Site A emergency contact list, approved by the BCM manager, Site A)

## Role card: Shift leader, Hall 3 chilled dispatch, Site A

**When this card applies:** when Hall 3 "cannot dispatch for two hours or more" (§2). You report this, and the duty manager activates the plan (§2).

**Actions, in plan order**

1. Report the loss of Hall 3 to the duty manager "at once" (§3.1).
2. "Stop loading at the Hall 3 doors" and move staff "to the canteen" (§3.2).
3. Run "the manual order export from LogiStock to a USB key", following work instruction "WI-14" (§3.3).
4. "Before the drive", gather your shift at the muster point: "car park P2, by the Site C weighbridge" (§3.5). *See Gap 2.*
5. Drive "the USB key and the shift's order list" to Site B and hand both to "the Site B dispatch lead" (§3.4).
6. Complete "the shift handover sheet before going off shift" (§3.6).

*Steps 4 and 5 are in time order. The plan numbers them 3.5 and 3.4. See Gap 3.*

**Contacts you call**

| Who | Number | Source |
|---|---|---|
| Duty manager, Site A | 040 555 0172 *(see Gap 1)* | §6 |
| Site B dispatch lead | 040 555 0230 | §6 |

**Left out, and why**
- §1 Scope, apart from the trigger. It describes the recovery option, which the shift leader doesn't carry out.
- §4 Dispatch lead (NordFrost slots, QA release). These are another role's actions.
- §5 IT service owner (restore LogiStock). This is another role's action.
- §6 NordFrost control room (040 555 0900) and IT service desk (040 555 0111). The plan gives the shift leader no action that calls either one.
- §7 Review. This belongs to the plan owner.

## Gaps (for the reviewer)

1. **Retired number.** Plan §6 gives the duty manager as "040 555 0172". Contact list v7 says "040 555 0172 retired 1 Aug 2026; the line no longer answers" and lists 040 555 0180 instead. The card keeps the plan's number. The plan owner decides whether plan v3 needs a new version before this card is issued. As it stands, the card's first action goes to a line that doesn't answer.
2. **Another site in the muster point.** Plan §3.5 says "car park P2, by the Site C weighbridge" in a Site A plan. The card keeps that wording. Question for the reviewer: is P2 at Site A, and is "Site C" a copying error?
3. **Step order.** §3.5 says "Before the drive", but it's numbered after §3.4, which is the drive. Question: is the card's time order right, and should the plan be renumbered?
4. **Trigger wording.** §1 says "more than two hours" and §2 says "two hours or more". The card uses §2 because that's the activation rule. Question: which threshold is meant?
5. **Local fit, which the material can't settle.**
   - Who leads the shift at Site A, and who completes the handover sheet (§3.6), while the shift leader drives 140 km to Site B?
   - Does the shift go to the canteen (§3.2) before or after the muster at P2 (§3.5)?
   - Does the shift leader have access to WI-14 and a USB key on shift? WI-14 wasn't attached, so I can't confirm what it says.
   - Plan §3.3 needs LogiStock running at Site A, and the IT service owner's target to restore it is six hours (§5.1). Question: does the manual export work while LogiStock is down?
6. **Contact list status.** Plan v3 (12 Mar 2026) is older than contact list v7 (1 Sep 2026). Nothing in the attachments shows the plan's contacts were checked after 1 Aug 2026.

Parts of this document were drafted with AI support (AI4BCM skill role-card, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

Next: if you want a card for another audience, such as the dispatch lead, that's a separate run.
