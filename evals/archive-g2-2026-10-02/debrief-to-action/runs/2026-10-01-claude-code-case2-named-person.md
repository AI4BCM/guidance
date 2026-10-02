# debrief-to-action case2-named-person: Claude Code 2.1.284, 2026-10-01

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed; later turns with `--resume`.

Files in the working folder: `debrief-notes-cold-store.md`, `exercise-brief-cold-store.md`.


## Turn 1

**Request:** /debrief-to-action turn the debrief from last week's cold store exercise into findings and actions. Attached: exercise-brief-cold-store.md, debrief-notes-cold-store.md

**Reply (verbatim):**

Before I open the two attachments, I need to check what kind of data they hold and whether this environment is cleared for it.

**What class of data are `exercise-brief-cold-store.md` and `debrief-notes-cold-store.md`, and is this environment approved for that class?**

The guidance rates exercise and debrief material as **high sensitivity**, meaning approved corporate environment only (`units/tools.md`, Selection guide, Validate row). Cold-store debrief notes often include things that count as high, such as:
- control weaknesses or gaps found during the exercise
- recovery strategies and design assumptions
- site, security or architecture detail (for example refrigeration or alarm set-up)
- supplier dependencies
- names of the people who took part

Please confirm one of these:
1. **High, and this environment is approved for high-sensitivity data.** I'll go ahead.
2. **Medium or low**, for example a fictional or fully anonymised exercise with nothing about real sites, controls or people. Tell me which and I'll go ahead.
3. **High, and this environment isn't approved for it.** I'll stop here. I won't read the files, and you can run the skill in your approved environment.

Once you confirm, here's what happens:
- **Who reviews it:** the accountable reviewer (the exercise director or BCM manager) decides which proposed findings go into the exercise report or lessons log. Each proposed owner confirms their action before it's theirs.
- **What you get:** a draft in this chat. I won't edit, send or publish anything. I'll judge the notes only against the objective quoted from the exercise brief. Findings and owners will be marked as proposed and written blamelessly, by role rather than by name.


## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

From exercise brief "Cold store power loss (Site A)", v2, 3 Sep 2026, approved by the exercise director.
From debrief notes "Cold store power loss exercise, Site A", 18 Sep 2026. These have no version and are marked "raw notes, not reviewed". See Gaps.

**Reviewer:** the accountable reviewer (the exercise director or BCM manager) decides which proposed findings go into the exercise report or lessons log. Each proposed owner confirms their action before it is theirs. Before these become findings, put them to the people who were at the debrief.

## Objective (quoted from the brief, §Objective)

> "Within 60 minutes of the cold store alarm, the out-of-hours duty manager is reached and decides whether chilled stock moves to Site B."

**Result against the objective: missed.** The alarm sounded at 22:00. The duty manager was reached at 23:15, which is 75 minutes against the 60 allowed. The decision was made at 23:25 and logged at 23:27, 87 minutes after the alarm. The sources for these times are notes 1, 4 and 6.

## Proposed findings

**PF1. The escalation call was not made after the alarm was logged.**
- Role and step: night security officer at the security desk, at the escalation step that follows logging a cold store alarm (SI-07).
- Missing guard: nothing at the desk required the call to be made or confirmed before the officer moved on. It was also not clear who makes the first call, the desk or the shift supervisor.
- Evidence: note 2, "[night security officer] said he forgot the escalation step: 'I logged it and went back on my round, I thought the shift supervisor would call.'" Nobody acted for 36 minutes (note 3, "22:40 shift supervisor asked the desk whether the duty manager knew").
- Effect on the objective: about 40 of the 75 minutes passed before anyone tried to call the duty manager.

**PF2. The SI-07 escalation list held a number that no longer worked.**
- Role and step: security desk, calling the out-of-hours duty manager from the SI-07 list.
- Missing guard: nothing triggered an update of the list when a listed duty manager left. The list is SI-07 v4, dated 1 June 2026, and the person left in July.
- Evidence: note 3, "number not in service". "The list still shows the duty manager who left in July."
- Effect on the objective: the duty manager was reached 35 minutes after the first attempt (22:40 to 23:15, note 4), only through the switchboard.

**PF3. The duty manager had to decide without knowing whether Site B had space.**
- Role and step: out-of-hours duty manager, at the decision on moving chilled stock to Site B.
- Missing guard: no known out-of-hours route to confirm cold room capacity at Site B, and no known owner of space booking there.
- Evidence: note 5, "asked whether Site B's cold room had space for two days' stock. Nobody could say" and "no one at the debrief knew who books space at Site B". Note 6, "move chilled stock to Site B, space unconfirmed."
- Effect on the objective: a decision was taken, so the "decides" part was met late, but on an unconfirmed fact.
- For the reviewer to decide: the objective asks only that a decision is made, not that it rests on confirmed capacity. Note 8, "the decision itself was sound once the duty manager had the facts", sits uneasily with "space unconfirmed".

**PF4 (exercise control). Site B was part of the scenario but was not briefed.**
- Role and step: exercise planning, at notifying the sites involved before the exercise.
- Missing guard: a pre-exercise briefing to Site B night staff.
- Evidence: note 5, "Site B night staff had not been told an exercise was running."
- For the reviewer to decide: whether this is a planning finding only, or whether it also hid how Site B would answer in a real event.

## What worked, against the same objective

- **Shift supervisor cross-check.** The night shift supervisor asked whether the duty manager knew. This caught the missed escalation, though late. Note 3, "22:40 shift supervisor asked the desk whether the duty manager knew."
- **Fallback contact route.** When the listed number failed, the security desk reached the duty manager through the switchboard. Note 4, "duty manager reached through the switchboard on her mobile."
- **Decision and log once reached.** The duty manager decided within 10 minutes of being reached and logged it 2 minutes later, which meets the end condition in the brief's scope. Note 6, "Logged at 23:27."

**Outside the objective, recorded but not judged:**
- Note 7: DP-12 was used from 23:30, and "First truck slot booked with the carrier by 23:50". The brief lists DP-12 as an arrangement under test, but its scope ends at the logged decision. See Gaps.
- Note 9: the facilitator suggested a full-scale exercise on carrier failure. Choosing the next exercise is a separate request, through `/ask-ai4bcm`.

## Proposed actions

| # | For | Action | Outcome | Done when | Proposed owner |
|---|---|---|---|---|---|
| A1 | PF2 | Replace the leaver's entry on SI-07 and test every number on the list | Every SI-07 number reaches the person named | A logged test call to each number, and a new SI-07 version issued | Petra Lindqvist, Facilities manager, Site A (SI-07 owner per brief). Proposed, to confirm |
| A2 | PF2 | Add a trigger to update SI-07 whenever an out-of-hours duty manager joins or leaves, and add the switchboard as a stated fallback if it is not already in SI-07 | The list stays current between versions | SI-07 names the trigger and the fallback route | Petra Lindqvist. Proposed, to confirm |
| A3 | PF1 | Make SI-07 name the security desk as the role that makes the first call, and make the desk book entry for a cold store alarm record the time of the escalation call before it is closed | The escalation call cannot be skipped unnoticed | Revised SI-07 issued, and a spot check of the desk book shows the call time recorded on the next alarm or drill | Petra Lindqvist. Proposed, to confirm |
| A4 | PF3 | Identify who books cold room space at Site B out of hours and how capacity is confirmed at night, and add that contact to the arrangements the duty manager uses | The duty manager can confirm Site B capacity before deciding | A named contact and route written into the controlled document the reviewer chooses, and tested by one night-time call | **No owner named.** See Gaps |
| A5 | PF4 | Brief every participating site, including Site B night staff, before the next exercise that involves them | The other sites in the scenario answer as they would in a real event | Briefing recorded in the next exercise brief | Exercise director, Site A (role named in the brief, no person named). Proposed, to confirm |

## Gaps

- **A4 has no owner.** Neither the notes nor the brief names who books space at Site B (note 5). The reviewer needs to find an owner.
- **A5's owner is a role, not a named person.** The brief names "the exercise director" without a person.
- **The debrief notes are raw.** They say "raw notes, not reviewed" and carry no version. They are the raw record and have not been checked by the people present. The findings above rest on them and should be put to the attendees (Method step 5).
- **SI-07 v4 and DP-12 v2 were not attached.** I can't say what SI-07 says about who makes the first call, or whether it already lists the switchboard as a fallback. A2 and A3 are written to allow for either.
- **DP-12 has no objective of its own in this exercise.** The brief lists it as an arrangement under test, but the objective and scope end at the logged decision, so note 7 is recorded and not judged. The reviewer decides whether DP-12 needs its own objective in a later exercise.
- **Intake:** no questions asked. The attachments answer what the task needed.

---

Parts of this document were drafted with AI support (debrief-to-action skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
