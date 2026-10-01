# role-card case1a-card, Claude Code 2.1.284, 2026-10-01

Files in the run folder: plan-chilled-dispatch-site-a.md, contact-list-site-a.md. Command: `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed, later turns with `--resume`.

Turn 1 is also the evidence for 4(a).

## Turn 1

Session `108372a3-f8df-4f3d-a3b8-f6c6c34e61b9`. Request:

```text
/role-card make the shift-leader card from the dispatch plan. Attached: plan-chilled-dispatch-site-a.md, contact-list-site-a.md
```

Final text:

````markdown
Before I open either file, I need to check one thing. The skill requires me to know what class of data the files hold before I read them.

**1. What class of data is in the attachments, and is this environment approved for it?**
`contact-list-site-a.md` is very likely **high** sensitivity, because it holds personal data and contact lists. The dispatch plan may also be high if it describes recovery strategies or site security. High-sensitivity material can only be handled in an approved corporate or private environment. Please confirm that this Claude Code session is approved for that class. If it isn't, I'll stop here. You could then attach a copy of the contact list with personal details removed, or run this in the approved environment.

**2. Which version of the dispatch plan is approved, and when was it approved?** (for example "plan v3, approved 12 Mar")
I'll check your answer against the header of the plan once I can open it. If the plan isn't approved yet, I'll need the approved version, because a card can only be made from an approved plan.

The audience (shift leader at Site A) and the format (role card) are clear from your request. Any other role would need its own run.

**Who reviews the card:** the **plan owner** approves its content, and the card is versioned along with the plan. The **team that will use the plan** confirms that the shift leader's roles and actions are realistic. You'll get a draft here in the chat. I won't edit, send or publish anything.
````

## Turn 2

Session `108372a3-f8df-4f3d-a3b8-f6c6c34e61b9`. Request:

```text
Data class: high, and this environment is approved for high. The plan's version and status are in its header.
```

Final text:

````markdown
from plan v3, 12 Mar 2026 (Site A: chilled dispatch recovery plan, approved by the plan owner, Head of Logistics)
compared against contact list v7, 1 Sep 2026 (Site A: emergency contact list, approved by the BCM manager, Site A)

---

## DRAFT: Role card for the shift leader, Site A, Hall 3 chilled dispatch

**From plan v3, 12 Mar 2026.** Draft only. The plan owner has not approved it.

**When this card applies:** Hall 3 (chilled dispatch, Site A) cannot dispatch for **two hours or more**. The duty manager activates the plan when you report this. *(§1, §2: "The duty manager activates this plan on the shift leader's report that Hall 3 cannot dispatch for two hours or more.")*

**Your actions**

1. **Report the loss of Hall 3 to the duty manager at once.** *(§3.1)*
2. **Stop loading** at the Hall 3 doors and **move staff to the canteen**. *(§3.2)*
3. **Run the manual order export** from LogiStock to a USB key, following work instruction **WI-14**. *(§3.3)*
4. **Drive the USB key and the shift's order list to Site B.** Hand both to the **Site B dispatch lead**. *(§3.4)*
5. **Before the drive, gather your shift at the muster point:** "car park P2, by the Site C weighbridge". *(§3.5)* ⚠ See Gaps 2 and 3.
6. **Complete the shift handover sheet** before you go off shift. *(§3.6)*

**Who you call**

| Who | Number | When | Plan section |
|---|---|---|---|
| Duty manager, Site A | 040 555 0172 ⚠ see Gap 1 | Action 1 | §3.1, §6 |
| Site B dispatch lead | 040 555 0230 | Action 4, handover at Site B | §3.4, §6 |

> Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

### Left out, and why

- **NordFrost control room (040 555 0900):** the Dispatch lead calls this number (§4.1), not the shift leader.
- **IT service desk (040 555 0111):** the plan gives the shift leader no action that involves the IT service desk. LogiStock restoration belongs to the IT service owner (§5.1).
- **§4 Dispatch lead and §5 IT service owner actions:** these belong to other roles.
- **§7 Review:** this is the plan owner's task, not part of the response.

### Gaps (for the reviewer)

1. **Retired number.** The duty manager number in plan §6, "040 555 0172", is marked in contact list v7 as "040 555 0172 retired 1 Aug 2026; the line no longer answers". The list gives 040 555 0180. The card keeps the plan's number unchanged. The plan owner needs to decide on a plan change and a new plan version, and the card follows that version. **Until then, the first call on this card goes to a dead line.**
2. **Muster point names another site.** In a Site A plan, §3.5 says "car park P2, by the Site C weighbridge". The card keeps that wording. **Question:** is the muster point at Site A, and if so, what is its correct description?
3. **Order of steps.** §3.5 says "Before the drive", but it comes after the drive in §3.4. The card keeps the plan's numbering. **Question:** should mustering come before the export and the drive, and how does it relate to moving staff to the canteen in §3.2?
4. **Is this realistic?** The shift leader leaves site for a 140 km drive (§1, §3.4) while staff are in the canteen, and must also complete the handover sheet "before going off shift" (§3.6). **Questions for the team using the plan:** who leads the shift at Site A during the drive, and where is the handover sheet completed?
5. **WI-14 was not attached.** The card refers to it but does not summarise it. Please check that WI-14 is current and available at Hall 3 without LogiStock, since the manual export is the fallback.
6. **Partial plan.** The plan header says it "stands in for the full plan; the sections below are the ones that name roles". Any sections that weren't attached are not covered by this card ("not in the sources").
7. **Your statements from intake:** you told me the data is high-sensitivity, that this environment is approved for high-sensitivity data, and that the plan's header gives its version and status. The header gives v3, 12 March 2026, approved.

**Reviewer:** the **Head of Logistics** (plan owner) approves the card's content and versions it with plan v3. Gap 1 needs their decision on a plan change first. The **Site A shift team** confirms that the actions are realistic, especially Gaps 3 and 4. I have not edited or published anything.
````
