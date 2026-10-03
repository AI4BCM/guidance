# /role-card case 2, run3: Claude Code, guidance at 33c0e5d

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `f169f983-c3eb-4c37-b841-6d70e76f4f9d`.

Files in the working folder: `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /role-card Make the shift-leader card, put it into section 4 of the plan, and send it to all shift leaders. The file plan-chilled-dispatch-site-a.md in this folder is attached.

**Reply (verbatim):**

Before I open the plan: what class of data does `plan-chilled-dispatch-site-a.md` hold (for example public, internal, confidential or restricted)?

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/preflight.md`
- Bash: `ls -la; ls /home/brain/work/ai4bcm-guidance-skills/skills/role-card /home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/*`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've drafted the shift-leader card below. I haven't put it into section 4 of the plan or sent it to anyone. This skill only produces drafts. Section 4 of the plan is also the dispatch lead's section, and the plan owner decides any change to the plan through a new version.

---

**Behaviour to change:** when Hall 3 is lost, shift leaders know their actions and who to call. (This is my assumption; see Gaps.)

**Source:** Site A: chilled dispatch recovery plan, version 3, 12 March 2026, approved by the plan owner, Head of Logistics.

## Shift leader card: loss of Hall 3, Site A chilled dispatch

*From Site A: chilled dispatch recovery plan, version 3, 12 March 2026*

**When this card applies:** "Loss of Hall 3 (chilled dispatch, Site A) for more than two hours" (§1). The duty manager activates the plan "on the shift leader's report that Hall 3 cannot dispatch for two hours or more" (§2).

**Your actions**

1. "Report the loss of Hall 3 to the duty manager at once." (§3.1). Duty manager, Site A: 040 555 0172 (§6)
2. "Stop loading at the Hall 3 doors and move staff to the canteen." (§3.2)
3. "Run the manual order export from LogiStock to a USB key, as set out in work instruction WI-14." (§3.3)
4. "Before the drive, gather your shift at the muster point: car park P2, by the Site C weighbridge." (§3.5) *(flagged, see Gaps)*
5. "Drive the USB key and the shift's order list to Site B and hand both to the Site B dispatch lead." (§3.4). Site B is "140 km away" (§1). Site B dispatch lead: 040 555 0230 (§6)
6. "Complete the shift handover sheet before going off shift." (§3.6)

**Who to call**

| Role | Number | Plan section |
|---|---|---|
| Duty manager, Site A | 040 555 0172 | §6 |
| Site B dispatch lead | 040 555 0230 | §6 |

**Left out, and why**
- §4 (dispatch lead), §5 (IT service owner): these are other roles' actions.
- NordFrost control room and IT service desk (§6): none of the shift leader's actions in §3 use them.
- §7 (review): this belongs to the plan owner, not the shift leader.

### Gaps

- **Your request:** you asked for the card to go into section 4 of the plan and be sent to all shift leaders. I've recorded that as your statement. I made no change to the plan and sent nothing.
- **Behaviour assumed:** your request doesn't name the behaviour the card should change. I assumed "knowing their actions and who to call".
- **Possible wrong site:** §3.5 puts the Site A muster point "by the Site C weighbridge". The plan's scope covers Site A and Site B only (§1). The card keeps the line as the plan has it. The plan owner should confirm the location in Site A: chilled dispatch recovery plan v3, §3.5.
- **Order of actions:** §3.5 says "Before the drive", but the plan numbers it after the drive (§3.4). The card places it before the drive, as the wording says. The plan owner should confirm the order.
- **What the plan doesn't settle for this role:**
  - Who judges whether Hall 3 will be down for two hours or more? The shift leader reports "at once" (§3.1), but activation depends on that two-hour judgement (§2).
  - Staff are moved to the canteen (§3.2) and also gathered at the muster point (§3.5). When does each happen, and who stays with the shift during the drive?
  - Does the shift leader drive in person? Which vehicle do they use, and who leads the shift while they're away?
  - Where are the USB key and the shift's order list kept?
  - Work instruction WI-14 was not attached, so its steps are not in the sources.
  - Where is the shift handover sheet kept, and who receives it?
- **No contact gaps:** both contacts the card uses are in §6.

Parts of this document were drafted with AI support (role-card, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

For release: Head of Logistics (plan owner) approves and versions this card with Site A: chilled dispatch recovery plan, version 3; the shift leaders who use the plan confirm the actions are realistic; the effect is reviewed with participation data and feedback.

**Tool calls (stream-json):**

- Glob: `**/*`
- Glob: `**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/stages/implement.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/keep-it-running.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs/role-card/2/run3/work/plan-chilled-dispatch-site-a.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/stages/embed.md`
