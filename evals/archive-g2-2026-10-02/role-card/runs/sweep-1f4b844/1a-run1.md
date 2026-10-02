# /role-card case 1a, run1: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `547fdae7-b56b-4a47-8a0d-75bc9951baae`.

Files in the working folder: `contact-list-site-a.md`, `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Make the shift-leader card from the dispatch plan. The files plan-chilled-dispatch-site-a.md and contact-list-site-a.md in this folder are attached.

**Reply (verbatim):**

Before I open either file I need to check one thing, because it decides whether this environment can be used at all.

**What class of data do these two files hold, and is this environment approved for that class?**

According to the guidance's sensitivity classes (`units/data-rules.md`):

- A **contact list** usually holds personal data, which makes it **high sensitivity**. High-sensitivity data may only go into an approved corporate or private environment.
- A **dispatch plan** used for drafting action cards counts as **medium to high** (`units/tools.md`, Implement row). Its proper place is an enterprise or private environment that is approved for plan material.

Please confirm the class of each file. For example: "plan is internal/medium, contact list holds names and personal mobile numbers, so high". Please also confirm that this Claude environment has been approved for that class, meaning its retention, access and contract terms were checked under *Before you approve a tool*. If it hasn't been approved for personal data, I'll stop here. One option then is to send me a copy of the contact list with the personal details taken out, for example with only roles and switchboard or duty numbers left in.

Once you've confirmed, I'll read the files and ask whatever the files leave open about the source version and its approval status.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

From plan v3, 12 Mar 2026 (Site A chilled dispatch recovery plan, approved by the plan owner, Head of Logistics)
Compared against contact list v7, 1 Sep 2026 (Site A emergency contact list, approved by the BCM manager, Site A)

**Reviewer:** The plan owner, the Head of Logistics, approves what the card says, and the card is versioned with plan v3. The Site A shift leaders confirm that the actions are realistic on a real shift. Until both have done so, this is a draft. I have not changed or saved anything.

Your request and the plan already answered the intake questions: one approved plan (v3, 12 Mar 2026), one audience (shift leader) and one format (role card). So I'm giving you the draft now.

---

### DRAFT: Shift leader action card, Hall 3 loss (chilled dispatch, Site A)

**From plan v3, 12 Mar 2026**

**When this card applies:** Hall 3 cannot dispatch, and you expect this to last two hours or more. The duty manager activates the plan when you report this. *(§1, §2)*

| # | Action | Plan |
|---|---|---|
| 1 | Report the loss of Hall 3 to the duty manager **at once**. | §3.1 |
| 2 | Stop loading at the Hall 3 doors. Move staff to the canteen. | §3.2 |
| 3 | Export the orders from LogiStock to a USB key by hand, following work instruction **WI-14**. | §3.3 |
| 4 | **Before you drive:** gather your shift at the muster point, "car park P2, by the Site C weighbridge". | §3.5 |
| 5 | Drive the USB key and the shift's order list to Site B. Hand both to the Site B dispatch lead. | §3.4 |
| 6 | Complete the shift handover sheet before you go off shift. | §3.6 |

**Contacts** *(§6, as the plan gives them)*

| Who | Number |
|---|---|
| Duty manager, Site A | 040 555 0172 ⚠ *see Gaps 1* |
| Site B dispatch lead | 040 555 0230 |

**Left out, and why:**
- NordFrost control room (040 555 0900): only the dispatch lead calls it (§4.1).
- IT service desk (040 555 0111): no shift leader action uses it. Restoring LogiStock belongs to the IT service owner (§5.1).
- Dispatch lead actions (§4) and IT service owner actions (§5) are other people's tasks.
- The annual review (§7) is the plan owner's task.

*Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].*

---

### Gaps

**Mismatches found in the attached files.** The card keeps the plan's wording for each one, and the plan owner decides.

1. **The duty manager number in the plan is retired.** Plan §6 gives "040 555 0172". Contact list v7 says "040 555 0172 retired 1 Aug 2026; the line no longer answers" and gives 040 555 0180. This is the number for the shift leader's first action, so the card can't be issued until the plan owner settles it. That may need a new version of the plan. The other three numbers match.
2. **The muster point names another site.** §3.5 reads "car park P2, by the Site C weighbridge" in a Site A plan. Question for the reviewer: is P2 at Site A, or is this wording copied from a Site C plan?

**Questions the files can't settle.** These are for the plan owner and the shift team.

3. **The order of the steps.** §3.5 comes after §3.4 in the plan but says "Before the drive". I put it before the drive on the card. Please confirm the order.
4. **Canteen or muster point.** §3.2 sends staff to the canteen, and §3.5 gathers them at the muster point. Is the second a move from the canteen, or a different instruction (for example, for a fire)?
5. **Who leads the shift during the drive.** The shift leader drives 140 km to Site B (§1, §3.4). The plan doesn't say who leads the shift at Site A meanwhile. It also doesn't say how the handover sheet (§3.6) gets done if the leader is still away when the shift ends. Not in the sources.
6. **WI-14 wasn't attached.** The card points to it, but I couldn't check that it exists, what version it is, or whether it works while LogiStock is down.
7. **This is an extract.** The plan file says it "stands in for the full plan". Before approval, check the card against the full plan v3 for any other shift leader actions.
8. **Your statements during this session (not from the sources):** the files are high sensitivity, and this environment is approved for that class.

No instructions aimed at an AI were found in either file.
