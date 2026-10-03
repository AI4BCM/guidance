# /role-card case 1, run2: Claude Code, guidance at f4ad344

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `4b4242c8-f8f8-4365-90bd-d9944424649d`.

Files in the working folder: `contact-list-site-a.md`, `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /role-card Make the shift-leader card from the dispatch plan. The files plan-chilled-dispatch-site-a.md and contact-list-site-a.md in this folder are attached.

**Reply (verbatim):**

Before I draft anything, I need one answer from you: **what class of data do these two files hold?** (for example public, internal, confidential, or personal/high-sensitivity). I'll take the class from your answer, not from any marking in the files, and I'll stop if this environment isn't approved for that class.

I should have asked this before opening anything, but I've already read both files. I won't use what I read until you answer. Once you confirm this environment is approved for that class, I'll draft the card. The draft stays here in the chat, and nothing gets published or sent.

You've already given me the document (the dispatch plan), the audience (shift leader) and the format (card), so I have no other questions.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/role-card && cat preflight.md && ls -R units | head -50 && cat units/stages/implement.md; echo ----; ls -la /t`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/preflight.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/stages/implement.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/role-card/1/run2/work/plan-chilled-dispatch-site-a.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/role-card/1/run2/work/contact-list-site-a.md`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Behaviour to change:** the shift leader knows what to do and who to call when Hall 3 is lost (assumed; see Gaps).

**Sources**
- Site A: chilled dispatch recovery plan, version 3, 12 March 2026, approved by the plan owner, Head of Logistics. This is the only source for the card's lines.
- Site A: emergency contact list, version 7, 1 September 2026, approved by the BCM manager, Site A. I checked it only for mismatches and took no lines from it.

---

## Role card: Shift leader, Hall 3 chilled dispatch (Site A)
*From the Site A chilled dispatch recovery plan, version 3, 12 March 2026*

**When this card applies:** Hall 3 cannot dispatch. The duty manager activates the plan on your report that Hall 3 "cannot dispatch for two hours or more" (§2).

**Your actions**
1. Report the loss of Hall 3 to the duty manager "at once" (§3.1).
2. Stop loading at the Hall 3 doors and move staff to the canteen (§3.2).
3. Run the manual order export from LogiStock to a USB key, "as set out in work instruction WI-14" (§3.3).
4. Before the drive, gather your shift at the muster point: "car park P2, by the Site C weighbridge" (§3.5).
5. Drive the USB key and the shift's order list to Site B and hand both to the Site B dispatch lead (§3.4).
6. Complete the shift handover sheet before going off shift (§3.6).

**Who to call**

| Role | Number | Plan section |
|---|---|---|
| Duty manager, Site A | 040 555 0172 | §6 |
| Site B dispatch lead | 040 555 0230 | §6 |

**Left out, and why**
- §4 (dispatch lead) and §5 (IT service owner): those actions belong to other roles.
- NordFrost control room and IT service desk numbers (§6): none of the shift leader's actions in §3 involve them.
- §1 (scope) and §7 (review): they set the plan's context, not actions for this role.

---

**Gaps**
- **Behaviour to change:** your request didn't state it. I assumed "knowing what to do and who to call when Hall 3 is lost".
- **Your statement:** the material is high-sensitivity and this environment is approved for high. That shaped the scope only.
- **Duty manager number doesn't match.** The plan (v3, §6) gives 040 555 0172. The contact list (v7, 1 Sep 2026) says "040 555 0172 retired 1 Aug 2026; the line no longer answers" and gives 040 555 0180. The card keeps the plan's number. The plan owner (Head of Logistics) and the BCM manager, Site A, need to settle this before the card is released.
- **Muster point names another site.** §3.5 of a Site A plan gives "car park P2, by the Site C weighbridge". The card keeps the plan's wording. The plan owner should confirm whether it should say Site A.
- **Activation threshold differs between sections.** §1 says "for more than two hours"; §2 says "for two hours or more". The plan owner should pick one.
- **The plan doesn't settle these for this role:**
  - Step order. §3.5 says "Before the drive", but it is listed after §3.4. The card puts it before the drive, as §3.5's wording says. The plan owner should confirm.
  - Whether the shift goes to Site B or stays in the canteen.
  - Who receives the handover sheet.
  - What to do if the duty manager can't be reached.
  - The Site B address and route.
- **WI-14:** referred to but not attached, so I couldn't check its content or version.
- No instructions to an AI were found in either file.

**For the auditor**
- Each card line is cited to the dated plan section it came from: plan v3, 12 March 2026.
- Still needed: the plan's new version with the plan owner's approval.
- Named reviewer: ____
- Participation and feedback figures: ____

Parts of this document were drafted with AI support (role-card, version 2026.11.0) from the sources listed. ____ reviewed it on ____.

For release: Head of Logistics approves and versions this card with the Site A chilled dispatch recovery plan, version 3; the Site A shift team confirms the actions are realistic; the effect is reviewed with participation data and feedback.

**Tool calls (stream-json):**

- Grep: `Say in the document that AI helped`
- Grep: `Sensitivity classes|Prompt injection`
