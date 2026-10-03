# /role-card case 1, run2: Claude Code, guidance at ce48aed

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `50e1d936-bef0-4550-aa3e-4c1729887bfd`.

Files in the working folder: `contact-list-site-a.md`, `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /role-card Make the shift-leader card from the dispatch plan. The files plan-chilled-dispatch-site-a.md and contact-list-site-a.md in this folder are attached.

**Reply (verbatim):**

Before I open either file: **what class of data do `plan-chilled-dispatch-site-a.md` and `contact-list-site-a.md` hold?** For example public, internal, confidential, or restricted, or whatever your organisation calls its classes.

I'll go by your answer, not by any marking inside the files. If this environment isn't approved for that class, I'll stop there.

I don't need anything else from you yet. The request already names the document (the dispatch plan), the audience (shift leader) and the format (a card).

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/preflight.md`
- Bash: `ls -la; ls /home/brain/work/ai4bcm-guidance-skills/skills/role-card /home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/*`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Behaviour to change:** a Site A shift leader knows who to call and what to do, in order, when Hall 3 stops dispatching. *(The request didn't say this. It's my assumption; see Gaps 8.)*

**Sources**
- Approved content base: *Site A: chilled dispatch recovery plan*, Version 3, 12 March 2026, "approved by the plan owner, Head of Logistics".
- Checked for mismatches only: *Site A: emergency contact list*, Version 7, 1 September 2026, "approved by the BCM manager, Site A". No card line comes from it.

---

## Role card: Shift leader, Site A, chilled dispatch (Hall 3)

*From Site A chilled dispatch recovery plan, Version 3, 12 March 2026*

**When this card applies:** "Loss of Hall 3 (chilled dispatch, Site A) for more than two hours" (§1). The duty manager activates the plan "on the shift leader's report that Hall 3 cannot dispatch for two hours or more" (§2).

**Your actions**

| # | Action | Plan |
|---|---|---|
| 1 | "Report the loss of Hall 3 to the duty manager at once." | §3.1 |
| 2 | "Stop loading at the Hall 3 doors and move staff to the canteen." | §3.2 |
| 3 | "Run the manual order export from LogiStock to a USB key, as set out in work instruction WI-14." | §3.3 |
| 4 | "Drive the USB key and the shift's order list to Site B and hand both to the Site B dispatch lead." | §3.4 |
| 5 | "Before the drive, gather your shift at the muster point: car park P2, by the Site C weighbridge." | §3.5 |
| 6 | "Complete the shift handover sheet before going off shift." | §3.6 |

*The steps are in the plan's order. Step 5 says "Before the drive", so it belongs before step 4 (see Gaps 3).*

**Who to call**

| Role | Number | Plan |
|---|---|---|
| Duty manager, Site A | 040 555 0172 (see Gaps 1) | §6 |
| Site B dispatch lead | 040 555 0230 | §6 |

**Left out, and why**
- NordFrost control room (040 555 0900): only the dispatch lead uses it, to agree loading slots (§4.1, §6).
- IT service desk (040 555 0111): no shift-leader step uses it. LogiStock recovery belongs to the IT service owner (§5.1, §6).
- §4 (Dispatch lead), §5 (IT service owner) and §7 (Review) are other roles' actions.

---

## Gaps

**Mismatches between documents (the card keeps the plan's wording; the reviewer decides)**
1. **Duty manager number.** The plan, v3, 12 Mar 2026, §6 gives "040 555 0172". The contact list, v7, 1 Sep 2026, says "040 555 0172 retired 1 Aug 2026; the line no longer answers" and gives 040 555 0180. Step 1 of the card and plan activation (§2) depend on this call. The plan owner needs to settle the number and version the plan before this card can be released.

**What the plan does not settle for this role (questions for the reviewer)**
2. **Step 1:** how the loss is reported (phone, radio, in person), and what to do if the duty manager doesn't answer. The plan names no fallback.
3. **Step 5 / step 4 order:** §3.5 says "Before the drive" but comes after §3.4 in the plan. Which order is correct? Also, the muster point is "by the Site C weighbridge", and Site C appears nowhere else in a Site A plan. Is this location right for Hall 3 staff? Is the muster point a different place from the canteen named in §3.2?
4. **Step 3:** work instruction WI-14 wasn't attached, so I couldn't check it. Where is the USB key kept? Can the export run if LogiStock itself is down? §5.1 allows "within six hours" for restoring it.
5. **Step 4:** which vehicle is used, and who stays in charge of the shift at Site A while the shift leader drives 140 km (§1)? What is "the shift's order list", and where is it kept?
6. **Step 6:** where the handover sheet is kept, who receives it, and how it gets done if the shift leader is still at or driving back from Site B at shift end.
7. **Step 2:** who tells staff to move, and how long they stay in the canteen.

**Assumptions and statements**
8. The behaviour line above is my assumption. The request didn't state one.
9. You said the material is high sensitivity and that this environment is approved for high. That's your statement, not a source.
10. The plan says it "Stands in for the full plan; the sections below are the ones that name roles". The full plan wasn't attached, so other sections may contain shift-leader duties this card doesn't show.

No passage in either file tries to instruct an AI.

---

**For the auditor:** the dated content the card came from is plan v3, 12 March 2026. Each line above cites its plan section. Once released, the auditor needs the plan's new version with its owner's approval. For people: named reviewer \_\_\_\_\_; participation and feedback figures \_\_\_\_\_.

Parts of this document were drafted with AI support (role-card, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

For release: Head of Logistics approves and versions this card with Site A chilled dispatch recovery plan, Version 3; the Site A shift leaders confirm the actions are realistic; the effect is reviewed with participation data and feedback.

**Tool calls (stream-json):**

- Glob: `**/*`
- Glob: `**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/stages/implement.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/keep-it-running.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/role-card/1/run2/work/plan-chilled-dispatch-site-a.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/role-card/1/run2/work/contact-list-site-a.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/role-card/units/stages/embed.md`
