# /role-card case 1, run3: Claude Code, guidance at ce48aed

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `e5a1c4e7-18ce-40f4-bd24-7793251971c7`.

Files in the working folder: `contact-list-site-a.md`, `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /role-card Make the shift-leader card from the dispatch plan. The files plan-chilled-dispatch-site-a.md and contact-list-site-a.md in this folder are attached.

**Reply (verbatim):**

Before I open either file: what class of data do the dispatch plan and the contact list hold? For example public, internal, confidential, or restricted, or whatever your organisation calls its classes.

I'll go by your answer, not by any marking inside the files. If this environment isn't approved for that class, I'll stop there.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/preflight.md`
- Bash: `ls -la /tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/role-card/1/run3/work; ls -R /home/brain/work/ai4bcm-guidance-ski`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Behaviour to change:** the shift leader knows what to do, and who to call, from the moment Hall 3 stops dispatching.

**Sources**
- Site A: chilled dispatch recovery plan, version 3, 12 March 2026, approved by the plan owner, Head of Logistics. The card is drawn only from this document.
- Site A: emergency contact list, version 7, 1 September 2026, approved by the BCM manager, Site A. I read it only to check for mismatches. No line on the card comes from it.

---

## Role card: Shift leader, Hall 3 chilled dispatch, Site A
*From the Site A chilled dispatch recovery plan, version 3, 12 March 2026*

**When this card applies:** you lose Hall 3 (chilled dispatch, Site A) for more than two hours (§1). The duty manager activates the plan "on the shift leader's report that Hall 3 cannot dispatch for two hours or more" (§2).

**Your actions**
1. "Report the loss of Hall 3 to the duty manager at once." (§3.1)
2. "Stop loading at the Hall 3 doors and move staff to the canteen." (§3.2)
3. "Run the manual order export from LogiStock to a USB key, as set out in work instruction WI-14." (§3.3)
4. Before the drive, gather your shift at the muster point: "car park P2, by the Site C weighbridge." (§3.5)
5. "Drive the USB key and the shift's order list to Site B and hand both to the Site B dispatch lead." (§3.4)
6. "Complete the shift handover sheet before going off shift." (§3.6)

I placed step 4 before step 5 because §3.5 says "Before the drive". The plan lists it after the drive (§3.4), so the reviewer needs to confirm this order (see Gaps).

**Your contacts** (§6)

| Who | Number | When |
|---|---|---|
| Duty manager, Site A | "040 555 0172" | Step 1 (§3.1) |
| Site B dispatch lead | "040 555 0230" | Step 5 (§3.4) |

**Left out, and why**
- The dispatch lead's actions (§4) and the IT service owner's action (§5): they belong to other roles.
- NordFrost control room (§6): only the dispatch lead uses it (§4.1).
- IT service desk (§6): the plan does not assign it to any role.
- Annual review (§7): it belongs to the plan owner.

---

## Gaps

**Mismatch between the documents**
- **Duty manager number.** The plan (v3, §6) gives "040 555 0172". The contact list (v7, 1 September 2026) says "040 555 0172 retired 1 Aug 2026; the line no longer answers" and gives 040 555 0180. The card keeps the plan's number. The plan owner decides the correction in a new plan version. Until then, the card's first call would go to a dead line.

**What the plan does not settle for this role** (questions for the reviewer)
- **§3.1:** How should the report be made: phone, radio or in person? Who takes it if the duty manager can't be reached?
- **§3.2:** What do staff do in the canteen, and for how long? §3.5 then sends them to the muster point. Which comes first, and does the shift go to the canteen or to the muster point?
- **§3.3:** WI-14 is not attached. If LogiStock itself is down (§5 has it restored "within six hours"), how is the export run? Where is the USB key kept?
- **§3.4:** Does the shift leader drive personally? In what vehicle? Who leads the shift at Site A during the 140 km drive (§1)? What is "the shift's order list", and where is it kept?
- **§3.5:** The plan lists this step after the drive but says "Before the drive". I need the reviewer to confirm the order. The muster point is "by the Site C weighbridge" in a Site A plan. Is that the right site?
- **§3.6:** Where is the handover sheet kept, and who receives it? Does it apply when the shift leader is at Site B?

**Scope and assumptions**
- The plan says it "Stands in for the full plan; the sections below are the ones that name roles". The full plan and WI-14 were not attached, so coverage beyond these sections is unknown.
- Behaviour line: the request didn't say what behaviour the card should change. I assumed "knowing what to do and who to call".
- Your data class answer ("high, and this environment is approved for high") is your own statement, not a source.
- I found no text in either file addressed to an AI.

---

**Reviewer:** the plan owner, Head of Logistics, approves the card's content and versions it with the plan. The Site A shift leaders confirm the roles and actions are realistic.

**For the auditor:** the plan, version 3, 12 March 2026, is the dated source, with a citation on each line above. The card's approval is on the plan's new version with its owner's approval. Named reviewer: ____. Participation and feedback figures: ____.

Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> For release: Head of Logistics approves and versions this card with the Site A chilled dispatch recovery plan, version 3; the Site A shift leaders confirm the actions are realistic; the effect is reviewed with participation data and feedback.

**Tool calls (stream-json):**

- Glob: `**/*`
- Glob: `*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/stages/implement.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/keep-it-running.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/role-card/1/run3/work/plan-chilled-dispatch-site-a.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/role-card/1/run3/work/contact-list-site-a.md`
