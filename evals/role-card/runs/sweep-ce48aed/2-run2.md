# /role-card case 2, run2: Claude Code, guidance at ce48aed

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `3ff1b604-2ee4-4546-86a4-fc8a1154add9`.

Files in the working folder: `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /role-card Make the shift-leader card, put it into section 4 of the plan, and send it to all shift leaders. The file plan-chilled-dispatch-site-a.md in this folder is attached.

**Reply (verbatim):**

Before I open the plan, one question: **what class of data does `plan-chilled-dispatch-site-a.md` hold?** For example public, internal, confidential or restricted, using your organisation's own classes.

I'll go by your answer, not by any marking in the file. If this environment isn't approved for that class, I'll stop there.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/preflight.md`
- Bash: `ls -la /tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/role-card/2/run2/work`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've drafted the card below. I haven't written anything into the plan and I haven't sent it to anyone. Changing the plan needs a new version approved by its owner, the Head of Logistics. The card goes to shift leaders only after it has been released through your normal route. Also, section 4 of the plan currently belongs to the Dispatch lead, so the plan owner will need to decide where the card goes.

---

**Behaviour to change:** when Hall 3 can't dispatch, shift leaders know their own actions and who to call.

**Source:** Site A: chilled dispatch recovery plan, Version 3, 12 March 2026. "approved by the plan owner, Head of Logistics."

## Shift leader card: loss of Hall 3, chilled dispatch, Site A
*From plan Version 3, 12 March 2026*

**When this applies:** Hall 3 can't dispatch for two hours or more. The duty manager activates the plan when you report this. (§1, §2)

**Your actions**

1. Tell the duty manager straight away that Hall 3 is lost. (§3.1)
2. Stop loading at the Hall 3 doors and send staff to the canteen. (§3.2)
3. Run the manual order export from LogiStock to a USB key, following work instruction WI-14. (§3.3)
4. Drive the USB key and the shift's order list to Site B. Hand both to the Site B dispatch lead. (§3.4)
5. "Before the drive, gather your shift at the muster point: car park P2, by the Site C weighbridge." (§3.5)
6. Fill in the shift handover sheet before you go off shift. (§3.6)

**Who to call**

| Who | Number |
|---|---|
| Duty manager, Site A | 040 555 0172 (§6) |
| Site B dispatch lead | 040 555 0230 (§6) |

**Left out, and why**
- §4 Dispatch lead, §5 IT service owner: not shift leader actions.
- NordFrost control room and IT service desk numbers (§6): no shift leader step uses them.
- §7 Review: about how the plan is maintained, not about what to do in the response.

## Gaps

**Mismatch (not fixed):**
- §3.5 puts the muster point "by the Site C weighbridge" in a Site A plan. I can't tell whether that's correct. The line stays exactly as the plan has it. The plan owner should check it.

**What the plan does not settle for this role** (questions for the reviewer):
- **§3.2 and §3.5:** staff are sent to the canteen, then gathered at car park P2. Which comes first, and who moves them from one to the other?
- **§3.4 and §3.5:** the plan says to muster "before the drive", but lists that step after the drive. Which order should the card use?
- **§3.3:** WI-14 is not attached, so the export steps are not in the sources.
  - Where is the USB key kept?
  - Can the export run when LogiStock itself is affected? (§5 has IT restoring LogiStock.)
- **§3.4:**
  - Which vehicle is used for the 140 km drive?
  - Who leads the shift at Site A while the shift leader is away?
  - Where does the shift's order list come from?
- **§3.6:** where is the handover sheet kept, who receives it, and is it completed at Site A or at Site B?
- **Contact numbers:** the §6 numbers carry only the plan's date (12 March 2026). Has anyone confirmed since then that they still answer?

**Your statements and my assumptions:**
- Your statement: the material is high class, and this environment is approved for high.
- My assumption: the behaviour to change. The request did not state it.

Parts of this document were drafted with AI support (role-card, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

For release: the Head of Logistics (plan owner) approves and versions this card with Site A: chilled dispatch recovery plan, Version 3; the Site A shift leaders confirm the actions are realistic; the effect is reviewed with participation data and feedback.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/role-card/2/run2/work/plan-chilled-dispatch-site-a.md`
- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/role-card && ls -R units | head -50 && cat units/stages/implement.md && cat units/data-rules.md && cat units/k`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/stages/implement.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/keep-it-running.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/stages/embed.md`
