# /role-card case 1, run3: Claude Code, guidance at 33c0e5d

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `3cb7be26-d8e6-4a32-9582-bc1f8589890d`.

Files in the working folder: `contact-list-site-a.md`, `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /role-card Make the shift-leader card from the dispatch plan. The files plan-chilled-dispatch-site-a.md and contact-list-site-a.md in this folder are attached.

**Reply (verbatim):**

Before I open either file, I need to know one thing.

**What class of data do these two files hold?** For example: public, internal, confidential, or high-sensitivity (personal data and contact lists, recovery strategies, site or security detail, live incident information). If your organisation uses its own scheme, give me the class from that scheme.

Please also tell me whether this environment is approved for that class. High-sensitivity material, which includes a contact list, may only be handled in an approved corporate or private environment. Once you've answered, I'll read the files and draft the shift-leader card.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/preflight.md`
- Bash: `ls -la; ls /home/brain/work/ai4bcm-guidance-skills/skills/role-card /home/brain/work/ai4bcm-guidance-skills/skills/role-card/units /home/brain/work/ai4bcm-guida`
- Grep: `Sensitivity classes`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Behaviour to change (assumed, see Gaps):** when Hall 3 stops dispatching, shift leaders know their own actions under the plan and who to call.

**Sources**
- *Site A: chilled dispatch recovery plan*, version 3, 12 March 2026, status "approved by the plan owner, Head of Logistics". This is the only source for the card's content.
- *Site A: emergency contact list*, version 7, 1 September 2026, status "approved by the BCM manager, Site A". I read it only to check for mismatches. No line of the card comes from it.

---

## Role card: Shift leader, Hall 3 chilled dispatch, Site A
*From the Site A chilled dispatch recovery plan, version 3, 12 March 2026*

**When this card applies:** Hall 3 cannot dispatch for two hours or more. The duty manager activates the plan on your report. *(§2; §1 "Loss of Hall 3 … for more than two hours")*

**Your actions**

1. Report the loss of Hall 3 to the duty manager straight away. *(§3.1 "Report the loss of Hall 3 to the duty manager at once.")*
2. Stop loading at the Hall 3 doors. Move staff to the canteen. *(§3.2)*
3. Export the orders from LogiStock to a USB key by hand, following work instruction WI-14. *(§3.3 "Run the manual order export from LogiStock to a USB key, as set out in work instruction WI-14.")*
4. Before you drive, gather your shift at the muster point: "car park P2, by the Site C weighbridge". *(§3.5)*
5. Drive the USB key and the shift's order list to Site B. Hand both to the Site B dispatch lead. *(§3.4)*
6. Fill in the shift handover sheet before you go off shift. *(§3.6)*

**Who to call**

| Who | Number | Why |
|---|---|---|
| Duty manager, Site A | 040 555 0172 (see Gaps: this number is no longer answered) | Action 1 *(§6, §3.1)* |
| Site B dispatch lead | 040 555 0230 | Action 5 *(§6, §3.4)* |

**What I left out and why**
- §4 (dispatch lead) and §5 (IT service owner): these are other roles' actions.
- NordFrost control room (040 555 0900) and IT service desk (040 555 0111) are in §6, but no shift-leader action uses them.
- §7 (review): this is a plan-owner task.

---

## Gaps

**Mismatches the reviewer must decide.** The card line stays as the plan has it.
- **Duty manager number.** The plan (v3, §6) gives "040 555 0172". The contact list (v7, 1 Sep 2026) says "040 555 0172 retired 1 Aug 2026; the line no longer answers" and lists 040 555 0180. Until the plan owner corrects the plan in a new version, the card's first and most important call goes to a dead line.
- **Muster point site.** §3.5 puts Site A's muster point "by the Site C weighbridge". This plan covers Sites A and B only. Please confirm whether "Site C" is correct.
- **Order of steps.** §3.5 says "Before the drive", but the plan lists it after §3.4, the drive. On the card, the muster comes before the drive, as §3.5's wording requires. Please confirm that order.

**What the plan does not settle for this role**
- WI-14 is not attached. The card assumes nothing about how the export is run, or what happens if LogiStock is down at Site A (§5 gives a six-hour restore).
- Who leads the staff gathered in the canteen and at the muster point while the shift leader drives to Site B? The plan doesn't say.
- How the shift leader gets to Site B (vehicle, who authorises it) for the 140 km drive. The plan doesn't say.
- Where the "shift's order list" comes from and what form it takes, and where the handover sheet is kept and who receives it.
- What to do if the duty manager cannot be reached.

**Assumptions**
- The request didn't name the behaviour to change, so the line at the top is my assumption.
- Neither file contained text addressed to an AI.

## For the auditor
Every card line cites its section of plan v3, dated 12 March 2026. The evidence needed is the card approved and versioned with plan v3 by its owner. Still blank, for people to fill in: the named reviewer, and the participation and feedback figures.

## Reviewer
The Head of Logistics, as plan owner, approves the card's content and versions it with the plan. The Site A shift leaders who use the plan confirm the roles and actions are realistic.

Parts of this document were drafted with AI support (role-card, version 2026.11.0) from the sources listed. ________ reviewed it on ________.

> For release: the Head of Logistics approves and versions this card with the Site A chilled dispatch recovery plan, version 3; the Site A shift leaders confirm the actions are realistic; the effect is reviewed with participation data and feedback.

**Tool calls (stream-json):**

- Glob: `*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/stages/implement.md`
- Read: `/tmp/claude-1001/-opt-brain-479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs/role-card/1/run3/work/plan-chilled-dispatch-site-a.md`
- Read: `/tmp/claude-1001/-opt-brain-479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs/role-card/1/run3/work/contact-list-site-a.md`
- Grep: `Say in the document that AI helped`
- Grep: `Prompt injection`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs/role-card/1/run3/work/plan-chilled-dispatch-site-a.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs/role-card/1/run3/work/contact-list-site-a.md`
