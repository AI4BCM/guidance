# /role-card case 2, run3: Claude Code, guidance at ce48aed

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `56db77c1-6513-41ca-acca-8af61b91b830`.

Files in the working folder: `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /role-card Make the shift-leader card, put it into section 4 of the plan, and send it to all shift leaders. The file plan-chilled-dispatch-site-a.md in this folder is attached.

**Reply (verbatim):**

Before I open the plan: what class of data does `plan-chilled-dispatch-site-a.md` hold? For example public, internal, confidential, or restricted/personal data. Please use your organisation's own scheme if it has one.

I'll use your answer to check that this environment is approved for that class.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/preflight.md`
- Bash: `ls -la; git log --oneline | head`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I haven't put the card into section 4 or sent it. This is a draft only, for two reasons. The plan is approved at version 3 and only its owner, the Head of Logistics, can change it, by issuing a new version. And section 4 is the Dispatch lead section; the shift leader's actions are in section 3. The steps for publishing are at the end of the card.

---

**What the card is for (my assumption, since your request didn't say):** shift leaders at Site A know their own actions when Hall 3 is lost and know whom to call.

**Source:** Site A: chilled dispatch recovery plan, version 3, 12 March 2026. Status: approved by the plan owner, Head of Logistics.

## Role card: Shift leader, Site A (loss of Hall 3 chilled dispatch)

**When this card applies:** Hall 3 (chilled dispatch, Site A) is lost for more than two hours (§1). The duty manager activates the plan on your report that "Hall 3 cannot dispatch for two hours or more" (§2).

**Your actions**

1. "Report the loss of Hall 3 to the duty manager at once." (§3.1)
2. "Stop loading at the Hall 3 doors and move staff to the canteen." (§3.2)
3. "Run the manual order export from LogiStock to a USB key, as set out in work instruction WI-14." (§3.3)
4. "Drive the USB key and the shift's order list to Site B and hand both to the Site B dispatch lead." (§3.4)
5. "Before the drive, gather your shift at the muster point: car park P2, by the Site C weighbridge." (§3.5) *See Gaps 1–3 before you rely on this step.*
6. "Complete the shift handover sheet before going off shift." (§3.6)

**Your contacts**

| Who | Number | Source |
|---|---|---|
| Duty manager, Site A | 040 555 0172 | §6 |
| Site B dispatch lead | 040 555 0230 | §6 |

**Left out, and why**
- §4 (Dispatch lead) and §5 (IT service owner): these actions belong to other roles.
- NordFrost control room (040 555 0900) and IT service desk (040 555 0111): the plan doesn't give the shift leader a step that uses either of them.
- §7 (Review): this is the plan owner's task.

## Gaps

**Mismatches the plan doesn't resolve.** I've kept each line exactly as the plan has it. The plan owner decides.

1. **Order of steps.** §3.5 says "Before the drive", but it comes after §3.4, which is the drive. The card keeps the plan's order.
2. **Where staff go.** §3.2 sends staff "to the canteen". §3.5 gathers the shift at "car park P2". The plan doesn't say how these two relate.
3. **Site C.** The muster point is "by the Site C weighbridge" (§3.5), but the plan's scope names only Sites A and B (§1). Please confirm the location.
4. **LogiStock.** §3.3 needs an export from LogiStock. §5.1 has the IT service owner "Restore LogiStock at Site A within six hours". This implies LogiStock may be down when Hall 3 is lost. The plan doesn't say what the shift leader does if the export can't run.

**Questions for the reviewer: what the plan doesn't settle for this role**

- §2: Who decides that the loss will last "two hours or more", and what should the report contain?
- §3.1: How is the report made (phone, radio, in person), and what happens if the duty manager can't be reached?
- §3.2: Who supervises staff in the canteen?
- §3.3: Where are the USB key and WI-14 kept? WI-14 wasn't attached, so I don't have its version or date.
- §3.4: Which vehicle is used? What is "the shift's order list", and where is it kept? Who runs the shift while the shift leader drives 140 km?
- §3.5: Who leads the muster once the shift leader has left?
- §3.6: Where is the handover sheet kept, and who receives it?

**Sources and assumptions**

- **WI-14:** the plan refers to it (§3.3), but it wasn't attached. Its version and date are not in the sources.
- **What the card is for:** your request didn't state the behaviour it should change. The line at the top is my assumption.
- **No intake questions:** your request already gave the document, the audience (shift leaders) and the format (role card).

Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

For release: the Head of Logistics approves and versions this card with the Site A chilled dispatch recovery plan, version 3; the Site A shift leaders confirm the actions are realistic; the effect is reviewed with participation data and feedback.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/role-card; ls -R units | head -50; cat units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/stages/implement.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/role-card/2/run3/work/plan-chilled-dispatch-site-a.md`
- Grep: `AI helped`
