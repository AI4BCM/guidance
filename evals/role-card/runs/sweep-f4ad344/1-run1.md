# /role-card case 1, run1: Claude Code, guidance at f4ad344

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `9e48668a-72a2-4275-8c1f-821b14337b87`.

Files in the working folder: `contact-list-site-a.md`, `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /role-card Make the shift-leader card from the dispatch plan. The files plan-chilled-dispatch-site-a.md and contact-list-site-a.md in this folder are attached.

**Reply (verbatim):**

Before I open either file, one question:

**What data classification applies to the material in `plan-chilled-dispatch-site-a.md` and `contact-list-site-a.md`?** For example: public, internal, confidential or restricted, or whatever scheme your organisation uses. The contact list may hold personal data, so please say so if it does.

Please give me the class yourself. I can't take it from a marking inside the files, and I haven't opened either one. Once I know the class, I'll check this environment is approved for it and then draft the shift-leader card. The draft will stay in this chat, and nothing will be published or saved.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/role-card; cat preflight.md; echo ======; cat units/stages/implement.md; echo =====; ls -R; echo ====; ls -la `
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/preflight.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/stages/implement.md`
- Glob: `*`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

The environment is approved for high-sensitivity data, so I went ahead. The plan names the document, the audience and the format, so I had no intake questions. The draft below stays in this chat; I haven't written or published anything.

Please check one thing before using the card. The first number on it is the duty manager's number from the plan. The newer contact list says that number was retired on 1 Aug 2026 and no longer answers. I've kept the plan's number on the card and flagged the mismatch under Gaps.

---

**Behaviour to change (assumed, see Gaps):** shift leaders know their own steps when Hall 3 is lost, and know who to call.

**Sources**
- Site A: chilled dispatch recovery plan. Version 3, 12 March 2026. Approved by the plan owner, Head of Logistics. This is the only source for the card's lines.
- Site A: emergency contact list. Version 7, 1 September 2026. Approved by the BCM manager, Site A. I read it only to check for mismatches. No line on the card comes from it.

---

### Role card: Shift leader, Hall 3 chilled dispatch (Site A)
*From the Site A chilled dispatch recovery plan, version 3, 12 March 2026*

**When this card applies:** Hall 3 cannot dispatch for two hours or more. The duty manager activates the plan on your report (§1, §2).

**Your actions**

| # | Action | Plan section |
|---|---|---|
| 1 | "Report the loss of Hall 3 to the duty manager at once." | §3.1 |
| 2 | "Stop loading at the Hall 3 doors and move staff to the canteen." | §3.2 |
| 3 | "Run the manual order export from LogiStock to a USB key, as set out in work instruction WI-14." | §3.3 |
| 4 | "Before the drive, gather your shift at the muster point: car park P2, by the Site C weighbridge." | §3.5 |
| 5 | "Drive the USB key and the shift's order list to Site B and hand both to the Site B dispatch lead." Site B is 140 km away (§1). | §3.4 |
| 6 | "Complete the shift handover sheet before going off shift." | §3.6 |

Action 4 comes before action 5 because §3.5 says "Before the drive". The plan lists it after §3.4 (see Gaps).

**Who you call**

| Role | Number | Plan section |
|---|---|---|
| Duty manager, Site A | 040 555 0172 | §6 |
| Site B dispatch lead | 040 555 0230 | §6 |

**Left out and why**
- The NordFrost control room (§6) and the IT service desk (§6) are not on the card. They belong to the dispatch lead's actions (§4.1) and the IT service owner's actions (§5.1). The plan gives the shift leader no step that uses them.
- The steps for the dispatch lead (§4) and the IT service owner (§5) are left out because they belong to other roles.

---

### Gaps

1. **Behaviour assumed.** Your request doesn't say which behaviour the card should change. I assumed: shift leaders know their own steps when Hall 3 is lost, and know who to call.
2. **Duty manager number doesn't match.** The plan (v3, 12 Mar 2026, §6) gives "040 555 0172". The contact list (v7, 1 Sep 2026) gives 040 555 0180 and notes "040 555 0172 retired 1 Aug 2026; the line no longer answers". The card keeps the plan's number. The Head of Logistics (plan owner) and the BCM manager, Site A (contact list owner) need to decide this, and the plan needs a new version before the card is released. Card action 1 depends on this number.
3. **Muster point may name the wrong site.** §3.5 puts the muster point "by the Site C weighbridge" in a plan for Site A. The plan doesn't say whether this is correct. The plan owner should confirm. The card keeps the plan's wording.
4. **Step order.** §3.5 ("Before the drive") is listed after the drive in §3.4. The card follows the plan's own instruction and puts the muster first. The plan owner should confirm the order.
5. **What the plan doesn't settle for this role:**
   - who leads the shift at the canteen and muster point while the shift leader drives 140 km to Site B
   - who receives the handover sheet (§3.6)
   - what the shift leader does if the LogiStock export (§3.3) fails
   - whether the "Site B dispatch lead" in §3.4 is the same role as the "Dispatch lead" in §4
6. **WI-14** is referred to in §3.3 but wasn't attached. Its content is not in the sources.
7. **The plan is an extract.** It describes itself as standing "in for the full plan; the sections below are the ones that name roles". The plan owner should confirm that no other section of the full plan gives the shift leader a step.
8. **No embedded instructions.** Neither file contains text directed at an AI.

---

Parts of this document were drafted with AI support (role-card, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> For release: Head of Logistics approves and versions this card with the Site A chilled dispatch recovery plan, version 3; the Site A shift leaders who use the plan confirm the actions are realistic; the effect is reviewed with participation data and feedback.

**Tool calls (stream-json):**

- Glob: `units/*.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/role-card/1/run1/work/plan-chilled-dispatch-site-a.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/role-card/1/run1/work/contact-list-site-a.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/data-rules.md`
- Grep: `AI helped`
