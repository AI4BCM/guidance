# role-card case1a-card, final round (f05ad10), Claude Code 2.1.284, 2026-10-01

Files in the run folder: plan-chilled-dispatch-site-a.md, contact-list-site-a.md. Guidance repo at f05ad10. Command: `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`.

Turn 2 answers the data class alone; the skill asked no intake question, so no format answer was given.

## Turn 1

Session `74ae077b-7164-4465-ae38-b302ca7fdda3`. Request:

```text
/role-card make the shift-leader card from the dispatch plan. Attached: plan-chilled-dispatch-site-a.md, contact-list-site-a.md
```

Final text:

`````markdown
Before I open either attachment, I need one answer from you.

**What class of data do these two files hold, and is this environment approved for it?**

From the file names, both are probably **high-sensitivity** under the AI4BCM data rules:
- `contact-list-site-a.md` likely has personal data and contact lists.
- `plan-chilled-dispatch-site-a.md` likely has recovery strategies and possibly site detail.

High-sensitivity material should only be used in an approved corporate or private environment. Please confirm one of these:

1. **Yes.** The files are high-sensitivity, and this Claude Code session is approved for that class under your organisation's AI or information-security policy. I'll go ahead.
2. **They're lower sensitivity** than the names suggest, for example a sanitised or test copy. Tell me which class, and I'll go ahead.
3. **Not approved, or you're not sure.** I'll stop here. You can rerun the skill once you've checked with information security.

When this is settled, I'll read the files. I'll only ask about anything they leave unclear, such as the plan's version and approval status. Then I'll draft the shift-leader role card in this chat. I won't write, send or change anything.

**Who reviews the card:** the plan owner approves what it says, and it's versioned with the dispatch plan. The team that will use the plan confirms that the shift leader's roles and actions are realistic.
`````

## Turn 2

Session `74ae077b-7164-4465-ae38-b302ca7fdda3`. Request:

```text
Data class: high, and this environment is approved for high.
```

Final text:

`````markdown
The attachments already give me the document, the audience and the format, so I have no intake questions:
- **Document:** Site A chilled dispatch recovery plan, version 3, 12 March 2026, approved by the Head of Logistics.
- **Audience:** shift leader.
- **Format:** role card.

Here's the draft. I haven't written, saved or sent it anywhere.

---

**From plan v3, 12 Mar 2026** (Site A chilled dispatch recovery plan, approved by the Head of Logistics)
Contacts checked against contact list v7, 1 Sep 2026 (Site A emergency contact list, approved by the BCM manager, Site A)

## Role card: Shift leader, Hall 3 chilled dispatch, Site A

**When this card applies:** Hall 3 is lost for more than two hours (§1). The duty manager activates the plan when you report that Hall 3 can't dispatch for two hours or more (§2).

**Your actions**

1. **Report** the loss of Hall 3 to the duty manager at once. (§3.1, "Report the loss of Hall 3 to the duty manager at once.")
2. **Stop loading** at the Hall 3 doors and move staff to the canteen. (§3.2)
3. **Export orders:** run the manual order export from LogiStock to a USB key, following work instruction WI-14. (§3.3)
4. **Gather your shift** before the drive, at the muster point: "car park P2, by the Site C weighbridge". (§3.5)
5. **Drive** the USB key and the shift's order list to Site B, 140 km away (§1), and hand both to the Site B dispatch lead. (§3.4)
6. **Complete** the shift handover sheet before going off shift. (§3.6)

Actions 4 and 5 appear here in the order the text gives ("Before the drive"), not in the plan's numbering. See Gaps.

**Who you call**

| Role | Number | Why |
|---|---|---|
| Duty manager, Site A | 040 555 0172 | Action 1 (§3.1, §6) |
| Site B dispatch lead | 040 555 0230 | Action 5 (§3.4, §6) |

**Left out, and why**
- NordFrost control room (040 555 0900) and IT service desk (040 555 0111): listed in §6, but the plan gives the shift leader no action involving them.
- §4 (dispatch lead), §5 (IT service owner) and §7 (review): these are other roles' actions or the plan owner's task.

**Gaps**

*Mismatches the attached material shows. The card keeps the plan's wording.*
- **Duty manager number has been retired.** Plan §6 gives 040 555 0172. Contact list v7 (1 Sep 2026) says "040 555 0172 retired 1 Aug 2026; the line no longer answers" and gives 040 555 0180. The card shows the plan's number until the plan owner issues a new plan version. This is the call that activates the plan.
- **Muster point names another site.** §3.5 says "car park P2, by the Site C weighbridge" in a Site A plan.

*Questions for the reviewer that the material can't settle*
- §3.1 says report "at once". §2 says activation follows a report that Hall 3 can't dispatch "for two hours or more". Does the shift leader report immediately, once two hours is expected, or both?
- §3.5 ("Before the drive") is numbered after §3.4 (the drive). Is the order on the card right?
- Who runs the shift and the staff in the canteen while the shift leader drives 140 km to Site B? The plan doesn't say.
- When should the handover sheet (§3.6) be done if the shift leader is at Site B at the end of the shift?
- Work instruction WI-14 wasn't attached, so I couldn't check it: not in the sources.
- The plan describes itself as "Stands in for the full plan". Other sections of the full plan might hold more shift-leader actions: not in the sources.
- The plan is dated 12 March 2026 and the contact list 1 September 2026. The contact list is the newer controlled source for numbers.

*Other*
- No intake questions were asked, so none of my own statements shape this draft.
- No embedded instructions were found in either file.

Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next steps:**
- **Plan owner (Head of Logistics):** approve the card's content and version it with plan v3. The duty manager number and the Site C muster point probably need a new plan version, since the card shouldn't move ahead of the plan.
- **Hall 3 shift team:** confirm the actions are realistic, especially the drive to Site B and who covers the shift while the shift leader is away.
`````
