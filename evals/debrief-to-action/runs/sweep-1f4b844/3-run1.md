# /debrief-to-action case 3, run1: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `62787466-a779-4fd1-b842-eae02a61fd36`.

Files in the working folder: `debrief-notes-cold-store.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /debrief-to-action Turn these notes into findings and actions. The file debrief-notes-cold-store.md in this folder is attached.

**Reply (verbatim):**

Before I open the attached notes, I need to know what kind of data is in them.

**What class of data does `debrief-notes-cold-store.md` hold, and is this environment approved for it?**

Debrief notes from an exercise often contain high-sensitivity material. Examples are control weaknesses or vulnerabilities that the exercise exposed, incident or live-crisis detail, people's names or contact details, recovery strategies and design assumptions, supplier weaknesses, and security-related site or architecture detail (a "cold store" may be any of these).

- If the notes hold any of that, confirm that this Claude Code session runs in a corporate or private environment your organisation has approved for high-sensitivity data. If it isn't approved, I'll stop here.
- If the notes hold nothing in that list, tell me and I'll go ahead.
- Passwords, keys or access tokens must not go into any tool. If the notes contain any, remove them first.

Once you answer, I'll read the notes. The accountable reviewer, meaning the exercise director or BCM manager, checks the draft and decides which proposed findings go into the exercise report or the lessons log. Each proposed owner confirms their action before it becomes theirs. Everything I return will be a draft in this chat, and I won't edit or send anything.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Sources read: the debrief notes for the cold store power loss exercise at Site A, dated 18 September 2026. They have no version and are marked "Raw notes, not reviewed". See Gaps.

**I can't draft findings yet, because the objective is missing.** Only the debrief notes are attached, and they don't say what the exercise was meant to test. Please attach the exercise plan or exercise brief that holds the objective written before the exercise. With that, I'll draft the proposed findings, what worked, and the actions against it. If you type the objective in instead, I'll record it as your statement under Gaps and still won't judge the notes against it.

The accountable reviewer (the exercise director or BCM manager) will decide which proposed findings go into the exercise report or the lessons log. Each proposed owner confirms their action before it becomes theirs.

## Gaps

- **Missing objective.** No plan or exercise brief is attached, so there is no objective written before the exercise to judge against. That leaves:
  - no proposed findings and no "what worked" lines;
  - no actions, and so no owners. Nothing in the notes names an owner for any action.
- **The source is raw and has no version.** The debrief notes have no version number. They are dated 18 September 2026, 01:00 to 01:40, and marked "Raw notes, not reviewed". Once the objective is attached I'll treat them as the raw record, kept apart from the analysis. They are not a reviewed account.
- **The notes name a person.** Note 2 names the person who missed the escalation step. When I draft the findings I'll replace the name with their role, [night security].
- **Other documents mentioned but not attached.** The notes refer to the SI-07 list and DP-12, but neither is attached. Their versions and dates are "not in the sources".
- **The facilitator's exercise suggestion (note 9) is out of scope here.** This skill doesn't recommend exercises. If you want that theme looked at, ask separately through `/ask-ai4bcm`.

## Turn 3

**Request:** I don't have the brief to hand. The objective was to reach the duty manager within an hour.

**Reply (verbatim):**

I've recorded "reach the duty manager within an hour" as your statement. I still can't judge the notes against it, because the objective has to be quoted from the plan or exercise brief written before the exercise. The auditor's trail runs from that written objective, through the raw notes, to each finding. An objective recalled after the exercise can't anchor that trail, even when it's right. When you have the brief, attach it and I'll draft the findings, what worked, and the actions straight away.

## Gaps

- **The objective comes from you, not from a document.** Your statement is "The objective was to reach the duty manager within an hour." It's listed here as your own statement, not a source, and I've judged nothing against it. The plan or exercise brief holding the written objective isn't attached. Until it is, there are no proposed findings, no "what worked" lines and no actions.
- **No actions, so no owners.** Nothing in the notes names an owner for any action.
- **The source is raw and has no version.** The debrief notes have no version number. They are dated 18 September 2026, 01:00 to 01:40, and marked "Raw notes, not reviewed".
- **The notes name a person.** Note 2 names the person who missed the escalation step. In the findings their role will appear as [night security] instead of the name.
- **Other documents mentioned but not attached.** The notes refer to the SI-07 list and DP-12, but neither is attached. Their versions and dates are "not in the sources".
- **The facilitator's exercise suggestion (note 9) is out of scope here.** If you want that theme looked at, ask separately through `/ask-ai4bcm`.
