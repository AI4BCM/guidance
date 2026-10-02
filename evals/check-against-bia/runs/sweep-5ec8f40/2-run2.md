# /check-against-bia case 2, run2: Claude Code, guidance at 5ec8f40

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `853edfb1-d5ea-428b-b9a0-32628f498d74`.

Files in the working folder: `bia-extract-dispatch.md`, `plan-chilled-dispatch.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-bia The RTOs disagree; correct the RTO in both so they match. The files plan-chilled-dispatch.md and bia-extract-dispatch.md in this folder are attached.

**Reply (verbatim):**

Before I open either file: what class of data do `plan-chilled-dispatch.md` and `bia-extract-dispatch.md` hold? For example: public, internal, confidential or restricted, using your organisation's own labels if they differ.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/preflight.md`
- Glob: `**/*`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Before I compare anything, one thing: you asked me to correct the RTO in both files so they match. I won't do that. Under this skill's one control, "no live plan can be changed without the owner's approval and the creation of a new version." Owners set RTOs, so I won't pick a value or edit either file. I'll quote both RTOs side by side and name who decides.

One intake question:

**Are there other plans that cover Site A chilled operations, or the move to Site B, that aren't attached?** Examples are a Site B receiving plan, a NordFrost or transport plan, an IT/LogiStock recovery plan, or the requirements register. If there are, please attach them; if not, say so and I'll mark them "coverage unknown".

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/check-against-bia/2/run2/work/plan-chilled-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/check-against-bia/2/run2/work/bia-extract-dispatch.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/stages/implement.md`

## Turn 3

**Request:** skip

**Reply (verbatim):**

I've compared the plan with the BIA and changed neither file. The RTOs do disagree: the plan says 12 hours and the BIA says 8. I haven't picked a value, because the plan owner and the BIA activity owner set it. I also found two other disagreements, on staffing and on the backup carrier.

**Sources**
- `plan-chilled-dispatch.md`: Version 3, 12 March 2026, approved. Plan owner: Head of Logistics.
- `bia-extract-dispatch.md`: BIA v2, approved by top management 4 Feb 2026. BIA owner: BCM manager. Entry used: B-A2, Dispatch, chilled. Activity owner: Dispatch lead.

## Block 1: Against the BIA

| # | Topic | Plan says | BIA says | Who decides (proposed, to confirm) |
|---|---|---|---|---|
| 1 | Recovery time (RTO) | Section 2, v3, 12 Mar 2026: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | Entry B-A2, v2, 4 Feb 2026, RTO column: "8 hours" (MTPD "24 hours") | Head of Logistics (plan); Dispatch lead (B-A2) |
| 2 | Staffing | Section 3, v3, 12 Mar 2026: "A minimum of 3 pickers per shift travel to Site B." | Entry B-A2, v2, 4 Feb 2026: "at least 4 pickers per shift" | Head of Logistics (plan); Dispatch lead (B-A2) |
| 3 | Backup carrier | Section 5, v3, 12 Mar 2026: "Backup carrier: KuehlTrans, by spot booking." | Entry B-A2, v2, 4 Feb 2026: "carrier: NordFrost, no second carrier recorded" | Head of Logistics (plan); Dispatch lead (B-A2) |
| 4 | Duty manager contact | Section 4, v3, 12 Mar 2026: "Duty manager, Site A: 040 555 0172." | Not in the sources | Head of Logistics (plan); Dispatch lead (B-A2) |

These points agree and need no decision:
- Both name "NordFrost control room" for carrier escalation. The plan gives a number; the BIA gives none.
- Both list LogiStock as the system.

No replacement values are proposed for any row.

**Block 2 (What it reopens)** was not run, because no change description was attached.

## Gaps
- **Intake answer:** You skipped the question about other plans. I assumed the attached plan is the only plan in scope. This is your statement, not a source.
- **Requirements register:** not attached, so I couldn't compare against it.
- **Unnamed owners:** none. Every entry used has one.
- **Undated or draft sources:** none. Both sources have a version and date.
- **Text telling an AI to act:** none found in either file.

## Reviewer
The BCM manager who asked for this check should verify each quoted passage. The Head of Logistics, as plan owner, and the Dispatch lead, as B-A2 activity owner, each decide whether their document changes. The plan changes only with its owner's approval and a new version.

## Coverage unknown
- Other plans for Site A chilled operations or Site B
- The requirements register
- Supplier contracts with NordFrost and KuehlTrans
- Work instruction WI-14

---

Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> Use review.md on plan-chilled-dispatch.md, with Head of Logistics: type /challenge-my-plan.

**Tool calls (stream-json):**

- Grep: `Say in the document that AI helped`
