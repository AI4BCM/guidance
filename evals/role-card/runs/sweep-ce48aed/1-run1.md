# /role-card case 1, run1: Claude Code, guidance at ce48aed

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `4b728481-708b-458c-9324-0f0587b5ca07`.

Files in the working folder: `contact-list-site-a.md`, `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /role-card Make the shift-leader card from the dispatch plan. The files plan-chilled-dispatch-site-a.md and contact-list-site-a.md in this folder are attached.

**Reply (verbatim):**

Before I open either file, I need to know what class of data the material holds.

Is this environment approved for that class? A dispatch plan and a contact list will often include personal data, such as names and phone numbers, and site or recovery detail. The data rules treat that as **high-sensitivity**, which may only be handled in an approved corporate or private environment. Public or free tools are not allowed for it.

I'll go by your answer rather than any marking in the files. If this environment isn't approved for that class, I'll stop here.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/role-card && cat preflight.md && ls -R; echo ---; ls -la /tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-5`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/preflight.md`
- Glob: `**/*`
- Glob: `**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/data-rules.md`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Behaviour to change: Site A shift leaders know their own steps and who to call when Hall 3 is lost (assumed, see Gaps).

**Sources**
- Site A chilled dispatch recovery plan: version 3, 12 March 2026, approved by the plan owner, Head of Logistics. This is the only source of card content.
- Site A emergency contact list: version 7, 1 September 2026, approved by the BCM manager, Site A. I checked it for mismatches only. No card line comes from it.

---

## Role card: Shift leader, Hall 3 chilled dispatch, Site A
*From the Site A chilled dispatch recovery plan, version 3, 12 March 2026. Draft, not released.*

**When this card applies**
- "Loss of Hall 3 (chilled dispatch, Site A) for more than two hours." (§1)
- The duty manager activates the plan when you report that Hall 3 can't dispatch for two hours or more. (§2)

**Your actions**
1. "Report the loss of Hall 3 to the duty manager at once." (§3.1)
2. "Stop loading at the Hall 3 doors and move staff to the canteen." (§3.2)
3. "Run the manual order export from LogiStock to a USB key, as set out in work instruction WI-14." (§3.3)
4. "Drive the USB key and the shift's order list to Site B and hand both to the Site B dispatch lead." (§3.4)
5. "Before the drive, gather your shift at the muster point: car park P2, by the Site C weighbridge." (§3.5)
6. "Complete the shift handover sheet before going off shift." (§3.6)

**Who to call**

| Role | Number | Source |
|---|---|---|
| Duty manager, Site A | 040 555 0172 (see Gaps: mismatch) | §6 |
| Site B dispatch lead | 040 555 0230 | §6 |

**Left out, and why**
- §4 (dispatch lead) and §5 (IT service owner) are other roles' actions.
- The NordFrost control room and IT service desk numbers (§6) aren't used in any shift-leader step in §3.
- §7 (review) belongs to the plan owner.

---

## Gaps

**Assumption**
- The request doesn't say what behaviour should change. I assumed the card is meant to make sure shift leaders know their own steps and who to call.

**Intake**
- I asked no questions. The request already gave the document (the dispatch plan), the audience (shift leader) and the format (card).

**Mismatch I can't fix**
- **Duty manager number.** The card keeps the number from the plan, but the two documents disagree:
  - Plan v3, §6 gives "040 555 0172".
  - Contact list v7, 1 September 2026, says "040 555 0172 retired 1 Aug 2026; the line no longer answers" and gives 040 555 0180.
  - The shift leader's first action (§3.1) depends on this line, so it needs a decision before release. The plan owner (Head of Logistics) decides whether to issue a new plan version. The contact list owner is the BCM manager, Site A.
- **Activation threshold.** The plan uses two different wordings. §1 says "for more than two hours" and §2 says "two hours or more". The plan owner should confirm which one applies.

**What the plan doesn't settle for this role (questions for the reviewer)**
- **§3.1:** How should the shift leader report, and who do they call if the duty manager doesn't answer? The plan names no deputy.
- **§3.1 to §3.2:** Does the shift leader wait for the duty manager to activate the plan before §3.2 to §3.5, or act at once?
- **§3.2 vs §3.5:** Staff are first moved to the canteen and then gathered at the muster point. When does the shift move from one to the other?
- **§3.5 location:** A Site A plan places the muster point "by the Site C weighbridge". Is that location correct?
- **§3.5 order:** This step says "Before the drive" but comes after the drive step (§3.4). The card keeps the plan's order. The plan owner should confirm the intended order.
- **§3.3 export:**
  - Work instruction WI-14 isn't attached and its version isn't in the sources.
  - The plan doesn't say where the USB key is kept.
  - The plan doesn't say what to do if LogiStock itself is unavailable. §5 allows six hours to restore it.
- **§3.4 drive:**
  - Does the shift leader drive personally, and in which vehicle?
  - Who leads the shift at Site A during the 140 km drive (§1)?
  - Which document is "the shift's order list", and where is it kept?
- **§3.6 handover sheet:** Where is the sheet kept, and who receives it?

**Other**
- No attached text gives instructions to an AI.
- The sources don't say who covers the shift-leader role when the shift leader is absent.

## For the auditor
- Each card line cites the dated content it came from: the Site A chilled dispatch recovery plan, version 3, 12 March 2026.
- Still needed: each plan's new version with its owner's approval, including the card versioned with the plan.
- Still blank, to be filled by people:
  - the named reviewer
  - the participation and feedback figures

## Reviewer
- The plan owner, Head of Logistics, approves the card's content and versions it with the plan.
- The Site A shift leaders, as the team that uses the plan, confirm the roles and actions are realistic.

Parts of this document were drafted with AI support (role-card, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

For release: the Head of Logistics approves and versions this card with the Site A chilled dispatch recovery plan, version 3; the Site A shift leaders confirm the actions are realistic; the effect is reviewed with participation data and feedback.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/role-card/1/run1/work/plan-chilled-dispatch-site-a.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/role-card/1/run1/work/contact-list-site-a.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/stages/implement.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/keep-it-running.md`
