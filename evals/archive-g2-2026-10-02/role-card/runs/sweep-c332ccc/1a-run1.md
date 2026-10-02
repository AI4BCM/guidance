# /role-card case 1a, run1: Claude Code, guidance at c332ccc

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `9c08ae96-795e-4bc3-9d7a-a94771c0a3dc`.

Files in the working folder: `contact-list-site-a.md`, `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Make the shift-leader card from the dispatch plan. The files plan-chilled-dispatch-site-a.md and contact-list-site-a.md in this folder are attached.

**Reply (verbatim):**

Before I open either file, I need to know how sensitive the data is.

**What class of data do the two attachments hold, and is this environment approved for that class?**

The AI4BCM data rules (`units/data-rules.md`, Sensitivity classes) say:

- **`contact-list-site-a.md`:** contact lists and personal data count as **high sensitivity**. They may only be used in an approved corporate or private environment.
- **`plan-chilled-dispatch-site-a.md`:** an approved plan counts as **medium to high**. It needs an enterprise or private environment (`units/tools.md`, Selection guide, "Implement – plan drafting… action cards"). If it includes recovery strategies or site security details, it is high.

Please confirm two things:
1. The class you'd assign each file (for example "contact list: high; plan: medium").
2. That this Claude Code environment is approved for that class under your organisation's AI and information-classification rules: retention, access and logging have been checked.

If the environment isn't approved for the contact list, I can stop here. Or I can work from the plan alone and list every contact under Gaps as "to be checked against the contact list by the reviewer."

Once you've answered, I'll read the files and ask only what they leave open, such as the plan's approval status. I'll then return the shift-leader card as a draft in the chat and won't change either file. The plan owner approves the card's content, and the team that uses the plan confirms that the roles and actions are realistic.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

The files answer the intake questions:
- **Document:** the Site A chilled dispatch recovery plan, v3, 12 March 2026, approved by the plan owner (Head of Logistics).
- **Audience:** the shift leader.
- **Format:** a role card.

I have no further questions, so the draft follows. Nothing in either file has been changed.

**Reviewer:** the plan owner (Head of Logistics) approves the card's content and versions it with the plan. The Site A shift leaders and the team that runs the plan confirm the actions are realistic.

---

From plan v3, 12 Mar 2026
Checked against contact list v7, 1 Sep 2026

## Shift leader: loss of Hall 3 (chilled dispatch, Site A)

**When this card applies:** Hall 3 cannot dispatch for two hours or more. The duty manager activates the plan on your report. *(§2: "on the shift leader's report that Hall 3 cannot dispatch for two hours or more")*

**Your actions**

1. **Report the loss of Hall 3 to the duty manager at once.** Call 040 555 0172 ⚠ *(see Gaps 1)*. *(§3.1: "Report the loss of Hall 3 to the duty manager at once"; number §6)*
2. **Stop loading at the Hall 3 doors** and move staff to the canteen. *(§3.2: "Stop loading at the Hall 3 doors and move staff to the canteen")*
3. **Export the orders.** Run the manual order export from LogiStock to a USB key, following work instruction WI-14. *(§3.3: "Run the manual order export from LogiStock to a USB key, as set out in work instruction WI-14")*
4. **Drive to Site B** with the USB key and the shift's order list. Hand both to the Site B dispatch lead. *(§3.4: "Drive the USB key and the shift's order list to Site B and hand both to the Site B dispatch lead"; Site B is "140 km away", §1)*
5. **Before the drive, gather your shift at the muster point:** "car park P2, by the Site C weighbridge" ⚠ *(see Gaps 2)*. *(§3.5: "Before the drive, gather your shift at the muster point: car park P2, by the Site C weighbridge")*
6. **Complete the shift handover sheet** before going off shift. *(§3.6: "Complete the shift handover sheet before going off shift")*

**Who you call**

| Who | Number | Why | Source |
|---|---|---|---|
| Duty manager, Site A | 040 555 0172 ⚠ | Report the loss of Hall 3 (action 1) | §3.1, §6 |
| Site B dispatch lead | 040 555 0230 | Hand over the USB key and order list (action 4) | §3.4, §6 |

**Left out, and why**
- **NordFrost control room (040 555 0900):** the dispatch lead calls NordFrost (§4.1), not the shift leader.
- **IT service desk (040 555 0111):** listed in §6, but no shift-leader action in §3 calls it. See Gaps 5.
- **§4 (dispatch lead), §5 (IT service owner) and §7 (review):** these are other roles' actions and plan upkeep.

### Gaps

**Mismatches found in the attached files.** The card above keeps the plan's wording for both.

1. **Duty manager's number is retired.** Plan v3 §6 gives "040 555 0172". Contact list v7 (1 Sep 2026, approved by the BCM manager, Site A) says "040 555 0172 retired 1 Aug 2026; the line no longer answers". The list gives 040 555 0180 as the current number. This affects action 1, the step that starts the whole plan. The card can't use the new number until the plan owner changes the plan and issues a new version.
2. **Muster point names another site.** §3.5 puts the Site A muster point "by the Site C weighbridge". No other attached material puts P2 or a weighbridge at Site A. This may be wording copied from another site's plan. The plan owner should confirm.

**Questions for the reviewer** (the attached material can't settle these):

3. **Order of actions 4 and 5.** §3.5 says "before the drive", but it comes after §3.4, the drive. Should the card list the muster before the drive?
4. **Canteen or muster point?** §3.2 moves staff "to the canteen". §3.5 gathers them at the muster point in car park P2. Are these two separate steps, and when do staff move from one to the other?
5. **IT service desk.** Should the shift leader call the IT service desk, for example if the LogiStock export under WI-14 fails? The plan doesn't say.
6. **Who leads the shift during the drive?** The shift leader drives 140 km to Site B (§3.4), but §3.6 still has them completing the handover sheet "before going off shift". Who leads the staff left on site meanwhile, and where is the sheet completed? Not in the sources.
7. **Threshold wording differs.** §1 says "more than two hours" and §2 says "two hours or more". The card follows §2, the activation section.

**Sources not seen or limited**

8. **Work instruction WI-14** wasn't attached. Its version, date and steps are "not in the sources".
9. **Plan v3 is a partial copy.** It describes itself as standing in for the full plan and holding only "the sections below are the ones that name roles". The full plan may hold more shift-leader actions or contacts. Coverage is unknown.

No passages in either file that try to instruct an AI.

*Parts of this document were drafted with AI support (AI4BCM skill role-card, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].*

---

**Next steps:**
- Pass Gaps 1 and 2 to the plan owner. Fixing them needs plan v4, approved by the owner.
- Have the card versioned with that new plan version, not issued against v3 with the retired number.
