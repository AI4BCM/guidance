# /debrief-to-action case 1, run1: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `d7fb6d1f-faac-4244-b822-f696c74ab069`.

Files in the working folder: `debrief-notes-cold-store.md`, `exercise-brief-cold-store.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /debrief-to-action Turn the debrief from last week's cold store exercise into findings and actions. The files exercise-brief-cold-store.md and debrief-notes-cold-store.md in this folder are attached.

**Reply (verbatim):**

Before I open the two attachments, one question about the data itself.

**What class of data do `exercise-brief-cold-store.md` and `debrief-notes-cold-store.md` hold, and is this environment approved for that class?**

Under the AI4BCM data rules, debrief and exercise material often counts as **high-sensitivity**. That's the case if it contains any of the following:

- vulnerabilities or control weaknesses the exercise exposed
- recovery strategies or design assumptions (for example, how long the cold store can hold temperature)
- names, contact details or other personal data of participants
- supplier weaknesses or contractual dependencies
- security-related site detail about the cold store

High-sensitivity material may only be processed in an **approved corporate or private environment**. That means an enterprise-licensed or self-hosted setup your organisation has cleared for this class of data, with known retention and access controls. A public or personal tool is not enough.

Please tell me:

1. Whether the files hold any of the high-sensitivity items above (or say they're low or medium sensitivity if they don't).
2. Whether this Claude Code environment is approved for that class.

If both answers allow it, I'll read the files and draft the proposed findings, what worked, and actions against the objective in the exercise brief. If the environment isn't approved for what the files hold, I'll stop here and won't read them.

For when we go ahead: the **exercise director or BCM manager** reviews the draft. They decide which proposed findings go into the exercise report or the lessons log, and each proposed action owner confirms their action before it becomes theirs. I'll return the draft here in the chat and won't edit or send anything.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

From exercise brief "cold store power loss (Site A)", version 2, 3 September 2026, approved by the exercise director, Site A.
From debrief notes "cold store power loss exercise, Site A", hot debrief of 18 September 2026. They have no version number and are marked "Raw notes, not reviewed" (see Gaps).

**Reviewer:** the exercise director or BCM manager decides which of these proposed findings go into the exercise report or the lessons log. Each proposed owner confirms their action before it is theirs. Everything below is a draft. I have recorded, assigned and sent nothing.

**Objective** (brief, "Objective"): "Within 60 minutes of the cold store alarm, the out-of-hours duty manager is reached and decides whether chilled stock moves to Site B."

**Result against it:** missed. The alarm sounded at 22:00. The duty manager was reached at 23:15, which the notes record as "75 minutes after the alarm". The decision was logged at 23:27, 87 minutes after the alarm.

---

## Proposed findings

**PF1. The escalation call was not made when the alarm was logged.**
- **Role and step:** night security desk. The step was escalating to the duty manager after the 22:04 log entry.
- **Missing guard:** logging the alarm did not prompt the call. The notes also show no clear rule on whether the desk or the shift supervisor makes it. About 36 minutes passed before the supervisor checked, at 22:40.
- **Note 2:** "[night security] said he forgot the escalation step: 'I logged it and went back on my round, I thought the shift supervisor would call.'"

**PF2. The call list in SI-07 sent the desk to a duty manager who left in July.**
- **Role and step:** security desk at 22:40, calling the number on the SI-07 list.
- **Missing guard:** nothing updated the list when the duty manager changed, and nothing tested the numbers. SI-07 is v4, 1 June 2026, so the July departure is after that version.
- **Note 3:** "Desk called the number on the SI-07 list: 'number not in service'. The list still shows the duty manager who left in July."

**PF3. The duty manager had no way to confirm space at Site B before deciding.**
- **Role and step:** duty manager, deciding at 23:20–23:25.
- **Missing guard:** there was no known contact or route for checking and booking cold-room space at Site B out of hours. The decision was made with the space unconfirmed.
- **Note 5:** "duty manager asked whether Site B's cold room had space for two days' stock. Nobody could say … no one at the debrief knew who books space at Site B."
- **Note 6:** "decided: move chilled stock to Site B, space unconfirmed."

**PF4. Site B was not briefed as part of the exercise.**
- **Role and step:** exercise control, during exercise set-up.
- **Missing guard:** the brief does not list a notice to Site B night staff. Because of that, the exercise could not show whether Site B can answer a capacity question at night.
- **Note 5:** "Site B night staff had not been told an exercise was running".

## What worked, against the same objective

- **W1. Night shift supervisor, 22:40.** The supervisor's own cross-check held and caught the missed escalation. Note 3: "shift supervisor asked the desk whether the duty manager knew."
- **W2. The switchboard as a fallback route, 23:15.** It held when the SI-07 number failed. Note 4: "duty manager reached through the switchboard on her mobile." The notes don't say who placed the call.
- **W3. Duty manager, 23:15 to 23:27.** Once reached, the duty manager asked the right question, decided within 12 minutes and logged the decision. Note 8, from the exercise director: "the decision itself was sound once the duty manager had the facts."

**Outside the objective, not judged:**
- Note 7, dispatch lead working through DP-12 from 23:30: "The checklist made it easy, I did not need to think about who to call." This happened after the decision was logged, which is where the scope ends.
- Note 9, the facilitator's suggestion for the next exercise (see Gaps).

## Proposed actions

**A1 (PF1). Make the escalation call a prompted desk step with one named caller.**
- **Outcome:** the desk calls the duty manager directly after logging a cold store alarm, without waiting for anyone else.
- **Done when:** a revised SI-07 states who makes the call, the desk-book entry has a "duty manager called at / by" field, and a re-run reaches the duty manager within the 60-minute objective.
- **Owner:** Petra Lindqvist, Facilities manager, Site A, named as SI-07 owner in the brief. *Proposed, to confirm.*

**A2 (PF2, W2). Correct the SI-07 call list and keep it current.**
- **Outcome:** every number on SI-07 reaches the current duty manager, and the switchboard is written in as the fallback route.
- **Done when:** SI-07 v5 is issued with every number test-called and dated, and it says what triggers an update (a change of duty manager) and how often the numbers are test-called.
- **Owner:** Petra Lindqvist, Facilities manager, Site A. *Proposed, to confirm.*

**A3 (PF3). Set up an out-of-hours route to confirm and book cold-room space at Site B.**
- **Outcome:** the duty manager can find out Site B's capacity before deciding.
- **Done when:** the contact and route are written into the document the duty manager uses at the decision point, and someone at Site B answers a test call at night.
- **Owner:** none named in the notes or the brief (see Gaps).

**A4 (PF4). Put a Site B notice into the brief of any exercise that relies on Site B.**
- **Outcome:** Site B staff take part and can answer during the exercise.
- **Done when:** the next brief that involves Site B lists the notice and who sends it.
- **Owner:** exercise director, Site A. The brief names this role, not a person. *Proposed, to confirm.*

---

## Gaps

- **The debrief notes are unreviewed.** They have no version and are marked "Raw notes, not reviewed". I used them as the raw record of the debrief. Before PF1 to PF4 become findings, put them to the people who were there: night security, the shift supervisor and the dispatch lead.
- **The duty manager's account is missing.** The duty manager was not listed as present at the debrief. Their account of 23:15 to 23:27 is not in the sources.
- **SI-07 and DP-12 were not attached.** These are SI-07 v4 (1 June 2026) and DP-12 v2 (20 May 2026). What SI-07 says about who makes the escalation call is not in the sources.
- **The scope is unclear about the carrier call.** The scope ends "when the duty manager's decision is logged", yet it puts "carrier booking beyond the first call" out of scope, which suggests the first carrier call was in. I judged against the objective, which ends at the decision.
- **A3 has no owner.** Neither the notes nor the brief names an owner, and nobody at the debrief knew who books space at Site B.
- **A4 names a role only.** The brief names the exercise director role, not a person.
- **Note 9 was not taken up.** It reads: "next quarter, run a full-scale exercise on carrier failure during the transfer." It falls outside this objective, and this skill recommends no exercise. If you want to explore it, ask through `/ask-ai4bcm`.
- **One name was removed.** The notes name the night security officer. I replaced the name with the role, as above.
- **Nothing came from you.** I asked no intake questions, so none of the above rests on your own statements.

Parts of this document were drafted with AI support (debrief-to-action skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
