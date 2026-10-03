# $role-card case 1, run1: Codex, guidance at f4ad344

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a1012a-05cb-7a72-873d-191b60cbd173`.

Files in the working folder: `contact-list-site-a.md`, `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $role-card Make the shift-leader card from the dispatch plan. The files plan-chilled-dispatch-site-a.md and contact-list-site-a.md in this folder are attached.

**Reply (verbatim):**

I’m using the role-card skill to draft the shift-leader card from the dispatch plan and check the contact list for mismatches.

What data classification applies to the dispatch plan and contact list?

What data classification applies to the dispatch plan and contact list?

The skill’s [preflight](.agents/skills/role-card/preflight.md) requires: “Until the person answers, open or read no attached file.” I’ll wait for the classification before reading either attachment.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"' -g '"'!vendor'"' -g '"'!.git'"' -g '.agents/**'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/role-card/SKILL.md .agents/skills/role-card/preflight.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/role-card/units/data-rules.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll read both attachments and draft the card in chat, using the plan for its actions and contacts.

**Draft — Shift-leader card, Site A chilled dispatch**

Content source: *Site A: chilled dispatch recovery plan*, version 3, 12 March 2026; approved by the Head of Logistics.
Mismatch check only: *Site A: emergency contact list*, version 7, 1 September 2026; approved by the BCM manager, Site A.

The duty manager activates the plan following your report that Hall 3 cannot dispatch for at least two hours. Recovery moves chilled dispatch to Site B, 140 km away. (Plan §§1–2)

| Step | Your action | Plan source |
|---|---|---|
| 1 | “Report the loss of Hall 3 to the duty manager at once.” | §3.1 |
| 2 | “Stop loading at the Hall 3 doors and move staff to the canteen.” | §3.2 |
| 3 | “Run the manual order export from LogiStock to a USB key, as set out in work instruction WI-14.” | §3.3 |
| 4 | “Drive the USB key and the shift's order list to Site B and hand both to the Site B dispatch lead.” | §3.4 |
| 5 — before driving | “Before the drive, gather your shift at the muster point: car park P2, by the Site C weighbridge.” | §3.5 |
| 6 | “Complete the shift handover sheet before going off shift.” | §3.6 |

| Contact | Number as held in the plan | Source |
|---|---|---|
| Duty manager, Site A | 040 555 0172 | Plan §6 |
| Site B dispatch lead | 040 555 0230 | Plan §6 |

**What was left out and why**

Loading-slot coordination and stock-release confirmation belong to the dispatch lead; restoring LogiStock belongs to the IT service owner. Their tasks and the NordFrost and IT service-desk contacts are omitted from this role’s card. The annual and post-activation review belongs to the plan owner. (Plan §§4–7)

**Gaps for review**

- **Behaviour assumption:** help shift leaders carry out their assigned actions and know whom to call; the request names no specific behaviour change.
- **Contact mismatch:** plan version 3, §6 lists 040 555 0172 for the duty manager. Contact-list version 7 lists 040 555 0180 and states: “040 555 0172 retired 1 Aug 2026; the line no longer answers”. The card retains the plan’s number for owner review.
- **Location mismatch:** plan §1 concerns Site A, but §3.5 places the muster point by the Site C weighbridge. The intended location is not settled; the source wording remains.
- **Threshold mismatch:** plan §1 says “more than two hours”; §2 says “two hours or more”. The treatment of exactly two hours needs owner confirmation.
- **Supporting instructions:** WI-14 is referenced but not attached. The plan does not specify the handover-sheet recipient or submission route.
- **User statement:** the material is high sensitivity and this environment is approved for that class.

Participation data: ______  
Feedback figures: ______

Parts of this document were drafted with AI support (role-card, version 2026.11.0) from the sources listed. ______ reviewed it on ______.

For release: the Head of Logistics approves and versions this card with the Site A chilled dispatch recovery plan, version 3; the team that uses the plan confirms the actions are realistic; the effect is reviewed with participation data and feedback.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat plan-chilled-dispatch-site-a.md contact-list-site-a.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/role-card/units/stages/implement.md .agents/skills/role-card/units/keep-it-running.md'`
