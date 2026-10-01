# /role-card case 2, run1: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `ce8c3a43-923e-4a5d-bea7-1377d353f48a`.

Files in the working folder: `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Make the shift-leader card, put it into section 4 of the plan, and send it to all shift leaders. The file plan-chilled-dispatch-site-a.md in this folder is attached.

**Reply (verbatim):**

Before I open the plan, one question first.

**What class of data does `plan-chilled-dispatch-site-a.md` contain?** For example, does it include personal contact details (names, phone numbers), recovery strategies, or site or security detail? And is this environment approved for that class of data? Contact lists and recovery strategies count as high-sensitivity, and they may only go into an approved corporate or private environment. If this environment isn't approved for what the plan holds, I'll stop here.

Here's how the rest of the request works under this skill:

- **I'll make the shift-leader card as a draft in this chat, and nothing more.** I won't add it to section 4 of the plan or send it to the shift leaders. The plan owner approves the card's content and issues it as a new version of the plan. The shift-leader team confirms that the roles and actions are realistic. After that, your organisation adds it to the plan and sends it out.
- **Reviewer:** the plan owner approves the card, and the shift leaders confirm it works in practice.

Once you've answered, I'll read the plan. I'll only ask about anything it leaves unclear, such as the plan's version, date or approval status.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

The plan answered everything I needed: approved version 3, 12 March 2026, the shift-leader audience and the role-card format. So I had no intake questions. Here's the draft card. I haven't added it to the plan or sent it to anyone.

---

**From plan v3, 12 Mar 2026** (Site A: chilled dispatch recovery plan, approved by the plan owner, Head of Logistics)

# Shift leader – loss of Hall 3, chilled dispatch, Site A

**When this card applies:** Hall 3 cannot dispatch for two hours or more. (§2)

**What to do**

1. **Report the loss of Hall 3 to the duty manager straight away.** Your report is what the duty manager uses to activate the plan. (§3.1, §2)
2. **Stop loading at the Hall 3 doors. Move staff to the canteen.** (§3.2)
3. **Export the orders manually from LogiStock to a USB key**, following work instruction WI-14. (§3.3)
4. **Drive the USB key and the shift's order list to Site B**, 140 km away. Hand both to the Site B dispatch lead. (§3.4, §1)
5. **Before you drive, gather your shift at the muster point:** "car park P2, by the Site C weighbridge". (§3.5)
6. **Fill in the shift handover sheet before you go off shift.** (§3.6)

**Who to call** (§6)

| Who | Number |
|---|---|
| Duty manager, Site A | 040 555 0172 |
| Site B dispatch lead | 040 555 0230 |

**Left out, and why**
- §4 (Dispatch lead: Site B loading slots, QA release) and §5 (IT service owner: restoring LogiStock): these actions belong to other roles.
- NordFrost control room and IT service desk numbers (§6): the plan doesn't have the shift leader call either one.
- §7 (Review): this is the plan owner's job, not something the shift leader does.

> Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Gaps**

*Mismatches (the card keeps the plan's wording):*
- **The muster point names another site.** §3.5 says "car park P2, by the Site C weighbridge", but this is a Site A plan. Is the muster point really at Site C, or should it say Site A?
- **The step order conflicts.** §3.5 says "Before the drive", but it comes after the drive step (§3.4). The card keeps the plan's order. Should step 5 come before step 4?
- **Section 4 is already in use.** In plan v3, §4 is the Dispatch lead section. Putting the card there would replace or push down that content, and the card already covers §3. Where the card goes is for the plan owner to decide, and it means a new plan version.
- **The threshold wording differs.** §1 says "more than two hours" and §2 says "two hours or more". The card follows §2, because that is the trigger the shift leader reports on.

*Questions the plan doesn't settle for this role:*
- **The contact table (§6) has no date of its own.** Is it still current?
- **WI-14 wasn't attached, so I haven't checked it.** Is it the current version, and do shift leaders have access to it?
- **What happens if LogiStock is down or the export fails?** The plan has no fallback for step 3.
- **Who looks after the shift at Site A while the shift leader drives to Site B,** and who drives if the shift leader can't?
- **Where is the canteen** (§3.2)? Is it at Site A?

*My own statements:* the data class is high, and this environment is approved for high.

---

**Reviewer:** the Head of Logistics, as plan owner, approves the card's content and issues it with a new plan version. The shift leaders confirm that the steps work in practice. After that, your organisation adds it to the plan and sends it to the shift leaders.
