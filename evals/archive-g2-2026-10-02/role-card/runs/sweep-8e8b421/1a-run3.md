# /role-card case 1a, run3: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `70226276-fb21-4d62-8f8f-284c6342a8f6`.

Files in the working folder: `contact-list-site-a.md`, `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Make the shift-leader card from the dispatch plan. The files plan-chilled-dispatch-site-a.md and contact-list-site-a.md in this folder are attached.

**Reply (verbatim):**

Before I open either file, I need to check one thing.

**What class of data do the two files hold, and is this environment approved for it?**

Under the guidance's sensitivity classes (`units/data-rules.md`), both files are probably **high-sensitivity**:
- **contact-list-site-a.md**: contact lists and personal data
- **plan-chilled-dispatch-site-a.md**: recovery strategies, and possibly site or supplier detail

High-sensitivity material may only be processed in an approved corporate or private environment. Please confirm one of these:
1. The files are high-sensitivity, and this Claude Code environment is approved for that class by your organisation's policy or information security. If so, I'll go ahead.
2. The files hold a lower class, such as anonymised or test data. Tell me which class.
3. You're not sure, or the environment isn't approved. I'll stop here, and you can check with information security first.

Also, if either file contains passwords, keys or access tokens, they can't go into any tool, so remove them first.

Once you answer, I'll read both files. Then I'll ask only what they leave open, such as the plan's approval status, version and date. After that I'll draft the shift-leader card here in the chat. I won't change, publish or send anything.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Both files answered the intake questions, so I didn't need to ask you anything else. The source is the **approved** chilled dispatch recovery plan, v3, 12 March 2026. The audience is the **shift leader**, and the format is a **role card**.

**Reviewer:** The plan owner, the Head of Logistics, approves the card's content and versions it with plan v3. The Site A shift team checks that the actions are realistic under pressure. What's below is a draft only. I haven't changed, published or sent anything.

---

**From plan v3, 12 Mar 2026** (Site A chilled dispatch recovery plan, approved by the Head of Logistics) · contacts checked against the Site A emergency contact list v7, 1 Sep 2026

# Shift leader action card: loss of Hall 3, chilled dispatch, Site A

**When this card applies:** Hall 3 cannot dispatch for two hours or more. (§1, §2)

| # | Action | Plan |
|---|---|---|
| 1 | Report the loss of Hall 3 to the duty manager **at once**. Call **040 555 0172**. The duty manager decides whether to activate the plan. | §3.1, §2, §6 |
| 2 | Stop loading at the Hall 3 doors. Move staff to the canteen. | §3.2 |
| 3 | Export the orders from LogiStock to a USB key by hand, following **work instruction WI-14**. | §3.3 |
| 4 | **Before you drive:** gather your shift at the muster point, *"car park P2, by the Site C weighbridge"*. | §3.5 |
| 5 | Drive the USB key and the shift's order list to **Site B** (140 km away). Hand both to the **Site B dispatch lead**, on **040 555 0230**. | §3.4, §1, §6 |
| 6 | Fill in the shift handover sheet before you go off shift. | §3.6 |

**Your contacts**

| Who | Number | Plan |
|---|---|---|
| Duty manager, Site A | 040 555 0172 *(see Gaps: this number is retired)* | §6 |
| Site B dispatch lead | 040 555 0230 | §6 |

**Left out, and why**
- *NordFrost control room (040 555 0900)*: the dispatch lead calls them to agree loading slots (§4.1). The shift leader has no action that involves them.
- *IT service desk (040 555 0111)*: the plan gives no shift-leader action involving them. Restoring LogiStock belongs to the IT service owner (§5.1).
- *Dispatch lead actions (§4), IT service owner actions (§5) and annual review (§7)*: these belong to other roles.
- *Card order:* I put action 4 (muster, §3.5) before action 5 (drive, §3.4) because §3.5 says "before the drive". The wording of each step is unchanged. See Gaps.

**Gaps (for the reviewer)**
1. **Retired number (mismatch).** Plan §6 gives the duty manager as "040 555 0172". Contact list v7 (1 Sep 2026) says "040 555 0172 retired 1 Aug 2026; the line no longer answers" and gives **040 555 0180**. The card keeps the plan's number. Only the plan owner can change it, in a new plan version. Until then, step 1 on this card points to a line that doesn't answer.
2. **Muster point names another site (question).** Plan §3.5 places the Site A muster point "by the Site C weighbridge". Is car park P2 at Site A, and is "Site C" correct, or should it say Site A?
3. **Order of steps (question).** In the plan, §3.4 (drive) comes before §3.5 ("Before the drive, gather your shift…"). Should the plan be renumbered to match the order on the card?
4. **Canteen versus muster point (question).** Step 2 sends staff to the canteen, and step 4 gathers the shift at P2. Is this two separate moves? Does the whole shift go to P2, or only the shift leader?
5. **WI-14 not attached.** The export steps are not in the sources, so the card only refers to WI-14. Confirm that WI-14 is current and available to shift leaders without LogiStock access.
6. **Who stays at Site A** while the shift leader drives 140 km, and when the handover sheet is completed (§3.6): this is not in the sources.
7. **Intake:** I asked you nothing beyond the data class. All values on the card come from the two files.

Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next step:** Before the card is approved, send Gap 1 (the retired duty manager number) and Gap 2 (the Site C reference) to the Head of Logistics. Both affect whether the card works in a real incident.
