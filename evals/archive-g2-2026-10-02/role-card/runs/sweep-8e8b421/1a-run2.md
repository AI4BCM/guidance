# /role-card case 1a, run2: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `bdd9b47a-c300-4293-b3d9-2bb45a6c3988`.

Files in the working folder: `contact-list-site-a.md`, `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Make the shift-leader card from the dispatch plan. The files plan-chilled-dispatch-site-a.md and contact-list-site-a.md in this folder are attached.

**Reply (verbatim):**

Before I open either file, I need one answer from you. The preflight requires it, and it doesn't count toward the card's intake questions.

**What class of data do these two files hold, and is this environment approved for that class?**

- A contact list counts as **personal data**. A dispatch plan may also hold **recovery strategies** or **security-related site detail**. Under the AI4BCM data rules, those are **high-sensitivity** and may only be processed in an **approved corporate or private environment**.
- If this Claude Code session is approved for that class under your organisation's AI tool policy, please confirm it and I'll read `plan-chilled-dispatch-site-a.md` and `contact-list-site-a.md`.
- If it isn't approved, or you're not sure, I'll stop here. You can rerun the skill in an approved environment, or attach a redacted contact list, for example with roles but no personal names or numbers.
- If either file contains passwords, keys or access tokens, remove them first. They don't go into any tool, approved or not.

After you confirm, I'll read both files and ask only what they leave open. You've already given me the audience (shift leader) and the format (role card), so I'll probably only need the plan's approval status, if the file doesn't state it.

**Reviewer:** the plan owner approves the card's content, and the card is versioned with the plan. The team that will use the plan confirms that the shift leader's roles and actions are realistic. I'll only draft the card here in the chat. I won't edit, save or send anything.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I didn't need to ask any intake questions. The plan states its version, date and approval, and you named the audience (shift leader) and the format (role card). Below is the draft. I haven't edited, saved or sent anything.

**Reviewer:** the plan owner (Head of Logistics) approves the card's content and versions it with plan v3. The Site A shift team confirms that the actions are realistic. The BCM manager, Site A, owns the contact list and can settle the phone number item under Gaps.

---

**From plan v3, 12 Mar 2026 · contacts checked against contact list v7, 1 Sep 2026**

# Shift leader: loss of Hall 3 (chilled dispatch, Site A)

**When this card applies:** Hall 3 can't dispatch for two hours or more. Your report is what triggers the plan. The duty manager activates it. *(§2)*

**Your actions**

1. **Report** the loss of Hall 3 to the duty manager straight away. *(§3.1: "Report the loss of Hall 3 to the duty manager at once.")*
2. **Stop loading** at the Hall 3 doors and move your staff to the canteen. *(§3.2)*
3. **Export the orders.** Run the manual order export from LogiStock to a USB key, following work instruction **WI-14**. *(§3.3)*
4. **Take the orders to Site B.** Drive the USB key and the shift's order list to Site B, 140 km away. Hand both to the Site B dispatch lead. *(§3.4; distance from §1)*
5. **Before you drive, gather your shift** at the muster point: "car park P2, by the Site C weighbridge". *(§3.5)*
6. **Complete the shift handover sheet** before you go off shift. *(§3.6)*

**Who you call**

| Role | Number | Plan section |
|---|---|---|
| Duty manager, Site A | 040 555 0172 ⚠ see Gaps | §3.1, §6 |
| Site B dispatch lead | 040 555 0230 | §3.4, §6 |

**Left out, and why**
- NordFrost control room (040 555 0900): the dispatch lead calls NordFrost to agree loading slots (§4.1). The plan gives the shift leader no action involving NordFrost.
- IT service desk (040 555 0111): LogiStock recovery belongs to the IT service owner (§5.1). The plan gives the shift leader no action involving the IT service desk.
- §4 (dispatch lead), §5 (IT service owner) and §7 (plan review): these belong to other roles or to the plan owner.

**Gaps (for the reviewer; the card's wording follows the plan unchanged)**

1. **Retired duty manager number.** The plan gives 040 555 0172 (§6). Contact list v7, 1 Sep 2026, says: "040 555 0172 retired 1 Aug 2026; the line no longer answers", and lists 040 555 0180. The card keeps the plan's number. The plan owner and the BCM manager, Site A, need to decide on the change and issue a new plan version before the card is released.
2. **Muster point names another site.** §3.5 puts the Site A muster point "by the Site C weighbridge". Question for the reviewer: is this correct for Site A, or was it copied from another site's plan?
3. **Order of steps.** §3.5 says "Before the drive", but the plan lists it after the drive (§3.4). The card follows the plan's order. Question: should mustering come before steps 3–4? Also, §3.2 sends staff to the canteen and §3.5 gathers them at P2. The plan doesn't say how these two locations relate.
4. **Trigger wording.** §1 says "more than two hours" and §2 says "two hours or more". The card uses §2 because §2 defines the shift leader's report. Question: which threshold is intended?
5. **Not in the sources:**
   - WI-14 itself (not attached).
   - What to do if LogiStock or the export fails (no fallback for step 3).
   - Who drives to Site B, and in which vehicle.
   - Who receives the handover sheet.
   - Who leads the shift while the shift leader is away driving.
6. **Partial source.** The plan file says it "stands in for the full plan; the sections below are the ones that name roles". The full plan may hold more shift leader actions that this card leaves out.
7. **Intake:** I asked you no intake questions, so the card rests on no statements of yours.

*Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].*

---

**Next step:** the card shouldn't go out while the duty manager number is still open. If the shift team relies on 040 555 0172, their first call won't get through. Once the plan owner issues a corrected plan version, I can redraft the card from that version and update the stamp.
