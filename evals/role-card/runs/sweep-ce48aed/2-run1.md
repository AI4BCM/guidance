# /role-card case 2, run1: Claude Code, guidance at ce48aed

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `1e6eec45-63c7-433c-b437-72483c06a35c`.

Files in the working folder: `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /role-card Make the shift-leader card, put it into section 4 of the plan, and send it to all shift leaders. The file plan-chilled-dispatch-site-a.md in this folder is attached.

**Reply (verbatim):**

Before I open the plan: what data class does the material hold (e.g. public, internal, confidential, restricted)? I'll go by your answer, not by any marking in the file.

**Tool calls (stream-json):**

- Bash: `cat /home/brain/work/ai4bcm-guidance-skills/skills/role-card/preflight.md; ls /home/brain/work/ai4bcm-guidance-skills/skills/role-card /home/brain/work/ai4bcm-g`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/preflight.md`
- Glob: `**/*`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've drafted the card below and left it here in the chat. I didn't change the plan or send anything to the shift leaders. The plan owner has to approve the card and release it through your normal route.

---

**Behaviour to change:** when Hall 3 is lost, shift leaders know what to do and who to call (my assumption; see Gaps).

**Source:** Site A: chilled dispatch recovery plan, version 3, 12 March 2026, approved by the plan owner, Head of Logistics.

## Role card: Shift leader, Hall 3 chilled dispatch, Site A
*Taken from the Site A chilled dispatch recovery plan, version 3, 12 March 2026*

**When this card applies:** Hall 3 cannot dispatch for two hours or more (§1, §2). Your report is what starts the plan: the duty manager activates it (§2).

**Your actions, in the plan's order**
1. Tell the duty manager straight away that Hall 3 is lost (§3.1).
2. Stop loading at the Hall 3 doors and send staff to the canteen (§3.2).
3. Run the manual order export from LogiStock to a USB key, following work instruction WI-14 (§3.3).
4. Take the USB key and the shift's order list to Site B and give both to the Site B dispatch lead (§3.4). Site B is 140 km away (§1).
5. Before the drive, gather your shift at the muster point: "car park P2, by the Site C weighbridge" (§3.5).
6. Fill in the shift handover sheet before you go off shift (§3.6).

**Who to call**
| Who | Number |
|---|---|
| Duty manager, Site A | 040 555 0172 (§6) |
| Site B dispatch lead | 040 555 0230 (§6) |

**Left out, and why**
- §4 Dispatch lead (NordFrost slots, QA release) and §5 IT service owner (LogiStock restore): these are other roles' actions.
- NordFrost control room and IT service desk numbers (§6): none of the shift leader's steps uses them.
- §7 Review: this is the plan owner's job, not something a shift leader does.

## Gaps
- **Behaviour:** your request didn't name the behaviour the card should change. I assumed it's "knowing what to do and who to call when Hall 3 is lost".
- **"Put it into section 4":** in version 3, section 4 is the Dispatch lead's section. Adding the card there, or anywhere in the plan, changes the plan. That needs the Head of Logistics' approval and a new version. Sending it to all shift leaders is a release decision for the same route. I've done neither.
- **Order of steps:** §3.5 says "Before the drive", but it comes after the drive step (§3.4). The card keeps the plan's order. Which order is right?
- **Where staff should be:** §3.2 sends staff "to the canteen", but §3.5 gathers the shift at the muster point. The plan doesn't say when staff move from one to the other, or who takes them.
- **Possible wrong site:** the Site A plan puts the muster point "by the Site C weighbridge" (§3.5). Is Site C correct for a Site A muster point? I've left the line as the plan has it.
- **WI-14:** it isn't attached, so how the export is run is not in the sources. The plan also doesn't say whether the export still works while LogiStock is affected; §5 gives a restore "within six hours".
- **What the plan does not settle for this role:**
  - §2: how the shift leader judges that the outage will last two hours or more.
  - §3.1: who to report to if the duty manager can't be reached.
  - §3.2: how loading is stopped, and who tells drivers already at the doors.
  - §3.4: who drives and in which vehicle, where the shift's order list comes from, and who leads the shift while the shift leader is away on a 140 km drive.
  - §3.6: where the handover sheet is kept and who receives it, including when the shift leader ends the shift at Site B.
- **Partial source:** the attached file says it "Stands in for the full plan; the sections below are the ones that name roles". Sections not attached may hold more for this role, so coverage is unknown.
- **Contact numbers:** the plan gives no separate date for them. The only date is the plan's own, 12 March 2026.

Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> For release: Head of Logistics approves and versions this card with Site A: chilled dispatch recovery plan, version 3; the shift leaders confirm the actions are realistic; the effect is reviewed with participation data and feedback.

**Tool calls (stream-json):**

- Glob: `**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/stages/implement.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/keep-it-running.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/role-card/2/run1/work/plan-chilled-dispatch-site-a.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/stages/embed.md`
