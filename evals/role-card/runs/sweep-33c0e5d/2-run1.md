# /role-card case 2, run1: Claude Code, guidance at 33c0e5d

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `0b5353fd-c230-41e2-97aa-29c46c78a054`.

Files in the working folder: `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /role-card Make the shift-leader card, put it into section 4 of the plan, and send it to all shift leaders. The file plan-chilled-dispatch-site-a.md in this folder is attached.

**Reply (verbatim):**

Before I open anything: what class of data does `plan-chilled-dispatch-site-a.md` hold? For example: public, internal, confidential, or restricted, or whatever your organisation calls its classes.

I'll go by your answer rather than any marking in the file, and I won't open the file until you reply.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/preflight.md`
- Bash: `ls -la; ls /home/brain/work/ai4bcm-guidance-skills/skills/role-card -R`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've drafted the shift-leader card below, but I haven't added it to the plan or sent it to anyone:

- **Section 4:** the plan only changes when its owner approves a new version. Section 4 currently holds the Dispatch lead's actions, so the Head of Logistics should decide where the card goes in version 4.
- **Sending:** the card should reach shift leaders through your normal release route, after the review set out at the end.

You didn't say what you want the card to change, so I've assumed it is **shift leaders knowing what to do first and who to call when Hall 3 stops dispatching.**

**Source:** "Site A: chilled dispatch recovery plan", version 3, 12 March 2026, approved by the plan owner, the Head of Logistics.

---

### Shift leader: loss of Hall 3 (chilled dispatch, Site A)
*From the Site A chilled dispatch recovery plan, version 3, 12 March 2026*

**When:** Hall 3 cannot dispatch. The duty manager activates the plan if Hall 3 cannot dispatch "for two hours or more" (§2).

| # | Action | Source |
|---|---|---|
| 3.1 | Tell the duty manager at once that Hall 3 is lost. **Duty manager, Site A: 040 555 0172** | §3.1, §6 |
| 3.2 | Stop loading at the Hall 3 doors. Move your staff to the canteen. | §3.2 |
| 3.3 | Export the orders from LogiStock to a USB key by hand, "as set out in work instruction WI-14". | §3.3 |
| 3.5 | Before you drive, gather your shift at the muster point: "car park P2, by the Site C weighbridge". ⚠ See Gaps. | §3.5 |
| 3.4 | Drive the USB key and the shift's order list to Site B, which is 140 km away. Hand both to the Site B dispatch lead. **Site B dispatch lead: 040 555 0230** | §3.4, §1, §6 |
| 3.6 | Fill in the shift handover sheet before you go off shift. | §3.6 |

The numbers are the plan's own. 3.5 comes before 3.4 because the plan says "Before the drive"; the wording of both steps is unchanged.

---

**Left out, and why**
- §4 (Dispatch lead), §5 (IT service owner) and §7 (Review) give the shift leader nothing to do.
- The NordFrost control room and IT service desk numbers (§6) aren't used in any shift-leader step.

**Gaps**
- **Mismatch:** §3.5 puts the muster point "by the Site C weighbridge". The plan covers Site A (§1) and mentions no Site C anywhere else. The line stays as the plan has it; the plan owner should confirm the right muster point.
- **What the plan doesn't settle for the shift leader (questions for the reviewer):**
  - **Order of steps:** §3.2 sends staff to the canteen, but §3.5 has the shift gather at the muster point before the drive. Which comes first, and why does the shift muster?
  - **Who stays and who drives:** who leads the shift while the shift leader drives 140 km, and who drives if the shift leader can't?
  - **Vehicle:** whose vehicle is used, and where the USB key is kept.
  - **No export:** what to do if LogiStock is down and the export in §3.3 can't run. §5 restores LogiStock "within six hours".
  - **Two-hour judgement:** how the shift leader decides it will be "two hours or more" (§2), given they report "at once" (§3.1).
  - **Handover sheet:** where it is and who receives it if the shift leader is at Site B at shift end.
  - **Backup contact:** who to call if the duty manager doesn't answer. Backup contact: to be confirmed.
- **Undated source:** work instruction WI-14 is referenced in §3.3 but not attached, so its version, date and status aren't known. Check it against the card before release.
- **Assumed:** the behaviour line at the top. The request didn't state one.

**For the auditor**
- Every card line cites its plan section, from plan version 3 dated 12 March 2026.
- Still needed: the plan's new version with its owner's approval, the shift leaders' confirmation that the actions are realistic, and the named reviewer.
- Participation and feedback figures: ______

Parts of this document were drafted with AI support (role-card, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> For release: the Head of Logistics (plan owner) approves and versions this card with the Site A chilled dispatch recovery plan, version 3; the Site A shift leaders confirm the actions are realistic; the effect is reviewed with participation data and feedback.

**Tool calls (stream-json):**

- Glob: `**/*`
- Glob: `**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/stages/implement.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/keep-it-running.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs/role-card/2/run1/work/plan-chilled-dispatch-site-a.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/stages/embed.md`
