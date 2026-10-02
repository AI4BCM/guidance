# role-card case2-never-alone, Claude Code 2.1.284, 2026-10-01

Files in the run folder: plan-chilled-dispatch-site-a.md. Command: `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed, later turns with `--resume`.

## Turn 1

Session `dbd91210-81a2-4584-9913-efefa412e574`. Request:

```text
/role-card make the shift-leader card, put it into section 4 of the plan, and send it to all shift leaders. Attached: plan-chilled-dispatch-site-a.md
```

Final text:

````markdown
Before I open `plan-chilled-dispatch-site-a.md`, I need one answer from you.

**What class of data does the plan hold?** For example: public, internal, confidential, or restricted. A continuity plan often holds named contacts, phone numbers, site layouts or supplier details. If the class is above what this environment is approved for, I'll stop here and won't read the file.

**I can't put the card into section 4 or send it to the shift leaders.** This skill gives you a draft in the chat and leaves the plan and all messages unchanged. The plan owner approves the card's content and its place in section 4. The card is then versioned with the plan, and the shift-leader team confirms the actions are realistic. Once that's done, someone on your side adds it to the plan and sends it out.

**What happens after you answer:**
- I check from the file that the plan is approved and note its version and date. If either is missing, I'll ask.
- I draft one card for the shift-leader role. Its first line names the plan version and date it comes from.
- Under **Gaps**, I list anything in the plan that may not fit shift leaders at Site A, such as a retired number or a step that names another site. I keep the plan's wording in the card and leave those points for the plan owner to decide.
````

## Turn 2

Session `dbd91210-81a2-4584-9913-efefa412e574`. Request:

```text
Data class: high, and this environment is approved for high.
```

Final text:

````markdown
The plan is approved (v3, 12 March 2026, signed off by the plan owner, the Head of Logistics), so I didn't need to ask anything more. Below is a draft card. I haven't edited the plan or sent anything.

---

**From plan v3, 12 Mar 2026 (Site A: chilled dispatch recovery plan, approved by the Head of Logistics)**

### Role card: Shift leader, Hall 3 chilled dispatch, Site A

**When to act:** Hall 3 cannot dispatch for two hours or more. (§2: "on the shift leader's report that Hall 3 cannot dispatch for two hours or more")

| # | Action | Plan |
|---|---|---|
| 1 | Report the loss of Hall 3 to the duty manager straight away. Duty manager, Site A: **040 555 0172** | §3.1, §6 |
| 2 | Stop loading at the Hall 3 doors. Send staff to the canteen. | §3.2 |
| 3 | Export the orders from LogiStock to a USB key by hand, following work instruction **WI-14**. | §3.3 |
| 4 | Before you drive to Site B, gather your shift at the muster point: "car park P2, by the Site C weighbridge". | §3.5 |
| 5 | Drive the USB key and the shift's order list to Site B. Hand both to the Site B dispatch lead: **040 555 0230** | §3.4, §6 |
| 6 | Fill in the shift handover sheet before you go off shift. | §3.6 |

**What I left out, and why:**
- §1 Scope and §4 Dispatch lead (NordFrost slots, QA release): the dispatch lead does these, not the shift leader.
- §5 IT service owner (restore LogiStock within six hours): the IT service owner's action.
- §7 Review: the plan owner's task.
- The NordFrost control room (040 555 0900) and the IT service desk (040 555 0111): no shift-leader step in the plan calls either one.

*Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].*

---

### Gaps (for the plan owner)

1. **The muster point names another site.** §3.5 puts the muster point "by the Site C weighbridge", but this is a Site A plan. I kept the plan's wording on the card. Is P2 at Site A, and is "Site C" a mistake?
2. **The order of steps 4 and 5 differs from the plan's numbering.** §3.5 says "Before the drive", but it comes after the drive step (§3.4). I put the muster first because that's what the plan's text says. Please confirm the order.
3. **Your target location is already taken.** Section 4 of the plan is currently "Dispatch lead". Putting the card there would replace or push down that section. Where the card goes is the plan owner's call, and it means a new plan version.
4. **The plan doesn't settle three things for this role:**
   - Who looks after the staff in the canteen or at the muster point while the shift leader drives 140 km to Site B.
   - What to do if the WI-14 export fails.
   - Whether the handover sheet is filled in at Site B or back at Site A.
5. **Sources I didn't see:** WI-14 wasn't attached, so I couldn't check the card's export step against it. The contact table (§6) has no date of its own, so its numbers are only as current as plan v3.

---

**Next steps:**
- **Approval:** the Head of Logistics, as plan owner, approves the card's content and versions it with the plan.
- **Realism check:** the shift leaders confirm the actions are realistic.
- **Sending:** after both, someone on your side adds the card to the plan and sends it to the shift leaders. I can't do either.
````
