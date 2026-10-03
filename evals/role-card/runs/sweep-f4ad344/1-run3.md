# /role-card case 1, run3: Claude Code, guidance at f4ad344

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `8a71b58e-2ccb-4d85-bfd9-21080a9f08d1`.

Files in the working folder: `contact-list-site-a.md`, `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /role-card Make the shift-leader card from the dispatch plan. The files plan-chilled-dispatch-site-a.md and contact-list-site-a.md in this folder are attached.

**Reply (verbatim):**

Before I open either file: what class of data do the dispatch plan and the contact list hold?

For example, is it internal, or high-sensitivity? High-sensitivity covers personal data and contact lists, recovery strategies, and security-related site detail. Is this environment approved for that class?

I'll use the class you give me, not any marking in the files. I'll only read them once you've answered.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/role-card; cat preflight.md; ls -R; cd -; ls -la`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/preflight.md`
- Glob: `**/*`
- Glob: `**/*`
- Grep: `Sensitivity classes`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

No intake questions were needed: your request already names the document (the dispatch plan), the audience (shift leader) and the format (card). I used the contact list only to check for mismatches, and I found no text in either file telling an AI to act. This is a draft only. I haven't written or published anything.

---

**Shift leader card: loss of Hall 3, chilled dispatch, Site A**

Behaviour to change: the shift leader knows their own steps in the plan and whom to call when Hall 3 can't dispatch. This is assumed, because the request doesn't say (see Gaps).

Sources:
- Site A: chilled dispatch recovery plan, version 3, 12 March 2026, approved by the plan owner, Head of Logistics. Every line on the card comes from this plan.
- Site A: emergency contact list, version 7, 1 September 2026, approved by the BCM manager, Site A. I read it for mismatches only; no line on the card comes from it.

**When this card applies:** Hall 3 can't dispatch for two hours or more. The duty manager activates the plan on your report (§2).

**Your actions**
1. Report the loss of Hall 3 to the duty manager "at once" (§3.1).
2. Stop loading at the Hall 3 doors and move staff to the canteen (§3.2).
3. Run the manual order export from LogiStock to a USB key, "as set out in work instruction WI-14" (§3.3).
4. Gather your shift at the muster point before the drive: "car park P2, by the Site C weighbridge" (§3.5). See Gaps: this location and the order of the steps need checking.
5. Drive the USB key and the shift's order list to Site B. Hand both to the Site B dispatch lead (§3.4).
6. Complete the shift handover sheet before you go off shift (§3.6).

**Who to call**

| Role | Number | Source |
|---|---|---|
| Duty manager, Site A | "040 555 0172" (see Gaps: this number may no longer be in use) | §6 |
| Site B dispatch lead | "040 555 0230" | §6 |

**Left out, and why**
- Dispatch lead steps (§4.1, §4.2) and IT service owner steps (§5.1) belong to other roles.
- The NordFrost control room and IT service desk numbers (§6) aren't linked to any shift leader step in the plan.
- Scope (§1) and review (§7) are for the plan owner, not for action during an incident.

**Gaps**
- **Behaviour to change:** the request didn't name one. I assumed plan ownership and knowing who to call.
- **Duty manager number mismatch:** the plan (v3, 12 March 2026, §6) gives "040 555 0172". The contact list (v7, 1 September 2026) gives 040 555 0180 and notes "040 555 0172 retired 1 Aug 2026; the line no longer answers". The card keeps the plan's number. The plan owner (Head of Logistics) and the contact list owner (BCM manager, Site A) need to settle it before release. This is the first call on the card.
- **Muster point at another site:** §3.5 places the muster point "by the Site C weighbridge", but this is a Site A plan. The plan owner needs to confirm the location.
- **Order of steps:** §3.5 says "Before the drive" but comes after the drive step (§3.4). The card follows the step's own wording, which moves it to step 4. The plan owner needs to confirm the order.
- **Activation threshold:** §1 says "more than two hours" and §2 says "two hours or more". The plan doesn't settle which one triggers your report.
- **What the plan doesn't settle for this role:**
  - What to do if LogiStock is also down and the §3.3 export can't run. §5.1 suggests it can fail, and the plan gives no fallback.
  - Who supervises staff in the canteen or at the muster point while you drive to Site B.
  - Where the handover sheet is kept and who receives it.
  - WI-14 isn't attached, so I didn't check the export steps.
- **Owners:** both sources name their owners. No undated, draft or replaced source was used.

Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

For release: the Head of Logistics approves and versions this card with the Site A chilled dispatch recovery plan, version 3; the Site A shift leaders confirm the actions are realistic; the effect is reviewed with participation data and feedback.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/role-card/1/run3/work/plan-chilled-dispatch-site-a.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/role-card/1/run3/work/contact-list-site-a.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/stages/implement.md`
- Grep: `Say in the document that AI helped`
