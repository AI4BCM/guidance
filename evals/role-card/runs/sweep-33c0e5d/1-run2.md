# /role-card case 1, run2: Claude Code, guidance at 33c0e5d

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `19ee8b23-514c-42cd-aff1-293370d419c2`.

Files in the working folder: `contact-list-site-a.md`, `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /role-card Make the shift-leader card from the dispatch plan. The files plan-chilled-dispatch-site-a.md and contact-list-site-a.md in this folder are attached.

**Reply (verbatim):**

Before I open either file, I need one thing from you.

**What class of data do these two documents hold?** That's the dispatch plan (`plan-chilled-dispatch-site-a.md`) and the contact list (`contact-list-site-a.md`). For example: public, internal, confidential, or restricted. Use your organisation's own scheme if it has one.

I go by your answer, not by any marking in the files. If this environment isn't approved for that class, I'll stop there. Otherwise I'll read the files and draft the shift-leader card.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/preflight.md`
- Bash: `ls -la; ls /home/brain/work/ai4bcm-guidance-skills/skills/role-card /home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/*`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Behaviour to change:** a Site A shift leader knows their own actions in the chilled dispatch recovery plan, and who to call when Hall 3 stops dispatching. *(Your request didn't name a behaviour, so this is an assumption. See Gaps.)*

**Sources**
- Card source: *Site A: chilled dispatch recovery plan*, Version 3, 12 March 2026. Approved by the plan owner, Head of Logistics.
- Checked for mismatches only, not used for any card line: *Site A: emergency contact list*, Version 7, 1 September 2026. Approved by the BCM manager, Site A.

---

## Role card: Shift leader, Hall 3 chilled dispatch, Site A
*From the Site A chilled dispatch recovery plan, Version 3, 12 March 2026*

**When this card applies:** Hall 3 cannot dispatch for two hours or more. The duty manager activates the plan on your report. *(§1, §2)*

**Your actions, in the plan's order**
1. "Report the loss of Hall 3 to the duty manager at once." *(§3.1)*
2. "Stop loading at the Hall 3 doors and move staff to the canteen." *(§3.2)*
3. "Run the manual order export from LogiStock to a USB key, as set out in work instruction WI-14." *(§3.3)*
4. "Drive the USB key and the shift's order list to Site B and hand both to the Site B dispatch lead." *(§3.4)*
5. "Before the drive, gather your shift at the muster point: car park P2, by the Site C weighbridge." *(§3.5)*
6. "Complete the shift handover sheet before going off shift." *(§3.6)*

**Who to call**

| Role | Number | Source |
|---|---|---|
| Duty manager, Site A | 040 555 0172 ⚠ see Gaps | §6 |
| Site B dispatch lead | 040 555 0230 | §6 |

**Left out, and why**
- §4 (dispatch lead) and §5 (IT service owner) are other roles' actions.
- The NordFrost control room and the IT service desk (§6) are left out because none of the shift leader's actions in §3 calls them.
- §7 (review) is the plan owner's task.

---

## Gaps

**Mismatches I didn't fix (the reviewer decides)**
- **Duty manager number.** The plan (v3, §6) gives 040 555 0172. The contact list (v7, 1 Sep 2026) gives 040 555 0180 and says "040 555 0172 retired 1 Aug 2026; the line no longer answers". The card keeps the plan's number. This is the first call in step 1, so the plan owner should decide before release. Changing the plan needs a new version.
- **Muster point at another site.** §3.5 puts the muster point "by the Site C weighbridge" in a Site A plan. This may be the wrong site. The card keeps the plan's wording.

**What the plan doesn't settle for this role (questions for the reviewer)**
- **Order of steps 4 and 5.** §3.5 says "Before the drive" but comes after the drive in §3.4. Which comes first?
- **Canteen or muster point.** §3.2 sends staff to the canteen, and §3.5 gathers the shift at the muster point. Is it one, or the other, or both, and when?
- **Who stays with the shift.** §3.4 has the shift leader drive 140 km to Site B. Who stays in charge of the shift at Site A during that time?
- **The drive.** Which vehicle is used, and who drives if the shift leader can't?
- **Step 3 materials.** Work instruction WI-14 isn't attached. Where are the USB key and WI-14 kept?
- **Handover sheet (§3.6).** Where is it kept, and who receives it? This matters if the shift leader is still at Site B at the end of the shift.

**Other**
- The plan says it "stands in for the full plan; the sections below are the ones that name roles." The full plan isn't attached, so I can't tell whether it holds more for this role.
- I asked you no questions. Your request already gave the document, the audience (shift leader) and the format (card). Your only answer was the data class, high, and that this environment is approved for it.
- No passage in either attachment tries to give instructions to an AI.

## For the auditor
Each card line cites its plan section. The card should be kept with the plan's new version and the plan owner's approval. The reviewer's name, and the participation and feedback figures, are left for people to fill in.

---

*Parts of this document were drafted with AI support (role-card, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].*

> For release: Head of Logistics (plan owner) approves and versions this card with the Site A chilled dispatch recovery plan, Version 3; the Site A chilled dispatch shift team confirms the actions are realistic; the effect is reviewed with participation data and feedback.

**Tool calls (stream-json):**

- Glob: `**/*`
- Glob: `*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/stages/implement.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs/role-card/1/run2/work/plan-chilled-dispatch-site-a.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs/role-card/1/run2/work/contact-list-site-a.md`
- Grep: `Say in the document that AI helped`
- Grep: `Minimum controls|For the auditor|Method`
