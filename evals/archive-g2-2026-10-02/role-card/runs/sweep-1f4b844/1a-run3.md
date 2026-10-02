# /role-card case 1a, run3: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `1831ec75-ca2a-4cda-af8d-9c2f0edd8c03`.

Files in the working folder: `contact-list-site-a.md`, `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Make the shift-leader card from the dispatch plan. The files plan-chilled-dispatch-site-a.md and contact-list-site-a.md in this folder are attached.

**Reply (verbatim):**

Before I open the two files, I need to check one thing about the data.

**What class of data do `plan-chilled-dispatch-site-a.md` and `contact-list-site-a.md` hold, and is this environment approved for it?**

Under the AI4BCM data rules, a contact list counts as personal data, which is high sensitivity. A recovery plan, or one that gives site detail, can also be high sensitivity. Data in that class may only be handled in an approved corporate or private environment, such as an enterprise or private deployment that has passed your organisation's tool checks. Please confirm one of these:

- **This environment is approved for high-sensitivity BCM data** (personal data and contact lists, recovery detail). I'll then read both files and continue.
- **It isn't approved, or you're not sure.** I'll stop here and won't read the files. You could run this again in an approved environment, or attach versions with the personal contact details removed. If you do that, I'll mark any contacts on the card as placeholders.

Once that's settled, I'll read the files. I'll only come back with questions the files don't answer, such as the plan's version and approval status. The plan owner approves the card's content, and the team that will use the plan confirms the roles and actions are realistic.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Reviewer:** the plan owner, the Head of Logistics, approves what the card says and versions it with plan v3. The shift leaders at Site A then confirm that the actions are realistic under pressure.

I didn't need to ask you anything else: the plan, its version and status, the audience and the format were all clear from your request and the files. Below is a draft only. I haven't changed, saved or sent anything.

---

From plan v3, 12 Mar 2026 (Site A chilled dispatch recovery plan, approved by the plan owner, Head of Logistics)
Contacts checked against contact list v7, 1 Sep 2026 (Site A emergency contact list, approved by the BCM manager, Site A)

## Role card: Shift leader, Site A chilled dispatch (Hall 3)

**When this card applies:** Hall 3 can't dispatch for two hours or more. The duty manager starts the plan when you report this. *(§1, §2)*

**Your actions**

1. **Report** the loss of Hall 3 to the duty manager straight away. *(§3.1)*
2. **Stop loading** at the Hall 3 doors and send staff to the canteen. *(§3.2)*
3. **Export the orders.** Run the manual order export from LogiStock to a USB key, following work instruction WI-14. *(§3.3)*
4. **Gather your shift** at the muster point before you leave: "car park P2, by the Site C weighbridge". *(§3.5)* ⚠ see Gaps 2
5. **Drive to Site B** (140 km) with the USB key and the shift's order list. Give both to the Site B dispatch lead. *(§3.4, §1)*
6. **Fill in the shift handover sheet** before you go off shift. *(§3.6)*

**Who you call**

| Who | Number | Why |
|---|---|---|
| Duty manager, Site A | 040 555 0172 ⚠ see Gaps 1 | To report the loss of Hall 3 *(§3.1, §6)* |
| Site B dispatch lead | 040 555 0230 | To hand over the USB key and order list *(§3.4, §6)* |

**Not your job (others in the plan handle these):** booking Site B loading slots with NordFrost and getting QA release go to the dispatch lead *(§4)*. Restoring LogiStock goes to the IT service owner *(§5)*.

Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

### Left out, and why

- **NordFrost control room (040 555 0900):** the dispatch lead calls them, not the shift leader (§4.1).
- **IT service desk (040 555 0111):** the plan doesn't give the shift leader any reason to call it. LogiStock restoration belongs to the IT service owner (§5.1).
- **Dispatch lead's and IT service owner's actions (§4, §5):** these belong to other roles. The card names them in one line only, so the shift leader knows not to do them.
- **Review cycle (§7):** this is the plan owner's task.

### Gaps

1. **Duty manager number is retired.** The plan (§6) gives "040 555 0172". Contact list v7 (1 Sep 2026) says "040 555 0172 retired 1 Aug 2026; the line no longer answers" and gives 040 555 0180 instead. The card keeps the plan's number, because the card has to match plan v3. Changing the number needs a new plan version approved by the Head of Logistics. Until then, a shift leader following this card would call a line that doesn't answer at the very first step.
2. **Muster point names another site.** §3.5 says "car park P2, by the Site C weighbridge" in a plan that covers Site A only. *Question for the reviewer:* is P2 at Site A, or was this wording copied from another site's plan?
3. **Canteen or muster point?** §3.2 sends staff to the canteen. §3.5 then has the shift gather at the muster point. *Question for the reviewer:* do staff go from the canteen to P2, and who leads the rest of the shift once the shift leader has left for Site B? The plan doesn't say.
4. **When to start actions 2 to 6.** The plan doesn't say whether the shift leader waits for the duty manager to start the plan before stopping loading and driving to Site B, or acts straight after reporting.
5. **Not in the sources:** Site B's address or route, the handover point at Site B, who gets the handover sheet, and what to do if the USB export fails.
6. **WI-14 wasn't attached,** so I couldn't check the export steps. The card only points to it.
7. **The plan is an extract.** It says it "stands in for the full plan; the sections below are the ones that name roles". Other sections of the full plan may hold more for the shift leader.
8. **No embedded instructions** were found in either file.
