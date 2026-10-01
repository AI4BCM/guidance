# /debrief-to-action case 1, run1: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `aa3b6fc9-c071-4cc4-9c6d-01fee1c0cac0`.

Files in the working folder: `debrief-notes-cold-store.md`, `exercise-brief-cold-store.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /debrief-to-action Turn the debrief from last week's cold store exercise into findings and actions. The files exercise-brief-cold-store.md and debrief-notes-cold-store.md in this folder are attached.

**Reply (verbatim):**

Before I open either file, I need one answer from you.

**What class of data do `exercise-brief-cold-store.md` and `debrief-notes-cold-store.md` hold, and is this environment approved for it?**

Exercise debrief notes often contain high-sensitivity material, for example:

- control weaknesses or vulnerabilities the exercise exposed
- recovery strategies and design assumptions
- supplier weaknesses or contractual dependencies, such as a refrigeration or logistics provider
- site or security-related details about the cold store
- names, contact lists or other personal data about participants

Data like this may only be processed in an approved corporate or private environment. Please tell me one of these:

1. The files hold **high-sensitivity** data, and this Claude Code session is an **approved** environment for it. I'll go ahead.
2. The files hold **only lower-sensitivity** data (nothing from the list above). I'll go ahead.
3. The files hold high-sensitivity data and this environment is **not** approved. I'll stop here and won't open them.

Also confirm that the files contain no passwords, keys or access tokens. Those can't go into any tool, approved or not.

When you've answered, I'll read both files. I'll take the objective from the exercise brief and draft **proposed** findings, what worked, and actions. The exercise director or BCM manager will decide which findings go into the exercise report or lessons log. Each proposed owner confirms their action before it becomes theirs.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

from exercise brief "Cold store power loss (Site A)" v2, 3 Sep 2026, approved by the exercise director, Site A
from debrief notes "Cold store power loss exercise, Site A", 18 Sep 2026, no version, "Raw notes, not reviewed" (see Gaps)

# Cold store power loss, Site A: proposed findings and actions

**Reviewer:** the exercise director, Site A, or the BCM manager decides which proposed findings go into the exercise report or the lessons log. Each proposed owner confirms their action before it becomes theirs. This is a draft only. I have recorded, assigned and sent nothing.

## The objective being judged

The objective is quoted from exercise brief v2, section "Objective":

> "Within 60 minutes of the cold store alarm, the out-of-hours duty manager is reached and decides whether chilled stock moves to Site B."

| Part of the objective | Target | What the notes show | Met? |
|---|---|---|---|
| Duty manager reached | by 23:00 | 23:15, "75 minutes after the alarm" (note 4) | No |
| Decision on moving stock to Site B | by 23:00 | Decided 23:25, "Logged at 23:27" (note 6), 87 minutes after the alarm | No, the decision came late and was taken with "space unconfirmed" |

## Proposed findings

**PF-1. The escalation step was not carried out after the alarm was logged.**
- **Part of the objective missed:** "within 60 minutes … the out-of-hours duty manager is reached"
- **Role:** night security desk
- **Step:** escalating the alarm under SI-07, after logging it in the desk book
- **Missing guard:** nothing in the desk routine stops the desk from returning to its round before the escalation call is made. Nothing says whether the desk or the shift supervisor makes that call. Each side assumed the other would.
- **Note it rests on:** note 2: "22:04 alarm logged in the desk book. [night security] … forgot the escalation step: 'I logged it and went back on my round, I thought the shift supervisor would call.'"
- **Impact:** the duty manager was not called for 40 minutes, until the shift supervisor asked at 22:40 (note 3).

**PF-2. The SI-07 call list gives a number for a duty manager who has left.**
- **Part of the objective missed:** "the out-of-hours duty manager is reached" within 60 minutes
- **Role:** security desk, using the list; the SI-07 list owner, keeping it current
- **Step:** calling the duty manager from the SI-07 list
- **Missing guard:** no update of the list when a listed person leaves, and no periodic test that the numbers work. The list was last versioned 1 June 2026 (brief). The departure was in July.
- **Note it rests on:** note 3: "Desk called the number on the SI-07 list: 'number not in service'. The list still shows the duty manager who left in July."
- **Impact:** the duty manager was reached only through the switchboard, at 75 minutes (note 4).

**PF-3. Site B cold room capacity could not be confirmed out of hours, so the decision was taken without it.**
- **Part of the objective missed:** "decides whether chilled stock moves to Site B" within 60 minutes. The decision was made, but at 87 minutes and with one of its deciding facts missing.
- **Role:** out-of-hours duty manager, as decision-maker, and the people around them
- **Step:** confirming Site B capacity before deciding
- **Missing guard:** the arrangements give no out-of-hours contact or route for booking or confirming space at Site B.
- **Note it rests on:** note 5: "duty manager asked whether Site B's cold room had space for two days' stock. Nobody could say. … no one at the debrief knew who books space at Site B." Note 6: "move chilled stock to Site B, space unconfirmed."
- **Exercise design point for the reviewer:** "Site B night staff had not been told an exercise was running" (note 5). Even with a contact, Site B could not have played its part. Part of this finding may therefore come from how the exercise was set up rather than from the arrangement itself. That should be put to the people who were there.

## What worked, against the same objective

- **W-1.** The alarm was logged within four minutes: "22:04 alarm logged in the desk book" (note 2). Role: night security desk. Step: recording the alarm. Safeguard that held: the desk book entry, which gave the timeline the debrief relied on.
- **W-2.** A cross-check by the shift supervisor started the escalation that had been missed: "22:40 shift supervisor asked the desk whether the duty manager knew" (note 3). Role: night shift supervisor. Step: checking escalation. Safeguard that held: a second role asking whether the call had been made. It came late, but without it the call might not have come at all.
- **W-3.** The switchboard served as a fallback route when the listed number failed: "duty manager reached through the switchboard on her mobile" (note 4). Role: security desk and switchboard. Step: reaching the duty manager. Safeguard that held: an alternative contact route.
- **W-4.** The decision-maker asked for the deciding fact before acting: "duty manager asked whether Site B's cold room had space" (note 5). The exercise director's view (note 8) was: "the decision itself was sound once the duty manager had the facts." Role: duty manager. Step: the decision. Safeguard that held: the decision-maker's own check. Note 8 says "once the duty manager had the facts", but note 5 shows the space fact was never obtained. The exercise director should settle what they meant.

## Proposed actions

| # | For | Action | Outcome | Done when | Owner (proposed, to confirm) |
|---|---|---|---|---|---|
| A-1 | PF-1 | Revise SI-07 to state who makes the escalation call (desk or shift supervisor) and that the desk does not return to its round until the call is made. Add a desk-book field for "duty manager called at / by". | The escalation call is made straight after the alarm is logged, with no gap between roles. | SI-07 is reissued with the step and the field, and a later alarm test shows the duty manager reached within 60 minutes. | Petra Lindqvist, Facilities manager, Site A (SI-07 owner, per brief), proposed, to confirm |
| A-2 | PF-2 | Correct the duty manager entry on the SI-07 list. Add a trigger to update the list when a listed person leaves or changes role, plus a regular test call of every number. | Every number on the list reaches the person it names. | The list is reissued with the current duty manager, and a recorded test call reaches each listed number. | Petra Lindqvist, Facilities manager, Site A, proposed, to confirm |
| A-3 | PF-2 | Add the switchboard route to SI-07 as the named fallback when a listed number fails. | The fallback that worked in the exercise becomes the written route. | SI-07 names the fallback route. | Petra Lindqvist, Facilities manager, Site A, proposed, to confirm |
| A-4 | PF-3 | Name who confirms and books Site B cold room space out of hours, and add that contact where the duty manager can find it. | The duty manager can confirm Site B capacity before deciding. | A named Site B contact is in the arrangement, and a test call confirms they can answer out of hours. | **No owner named in the notes or the brief** (see Gaps) |
| A-5 | PF-3 | Tell Site B night staff in advance of any future exercise that involves them. | Site B can play its part in the exercise. | The next exercise brief lists Site B among those notified. | **No owner named in the notes or the brief** (see Gaps) |

## Gaps

- **Unreviewed source.** The debrief notes have no version. They are marked "Raw notes, not reviewed", dated 18 Sep 2026. They are used here as the raw record. Under the stage method, each proposed finding goes back to the people present (security desk, dispatch lead, shift supervisor, facilitator, exercise director) before it becomes a finding.
- **Documents not attached.** SI-07 v4 and DP-12 v2 are named in the brief but were not attached. Whether SI-07 already sets an escalation step, a call time or a fallback route: not in the sources.
- **No owner for A-4.** Neither source names anyone. Note 5 says "no one at the debrief knew who books space at Site B."
- **No owner for A-5.** The brief names the exercise director's role but no person. The reviewer may assign it.
- **Note 8 against note 5.** The exercise director said the decision was sound "once the duty manager had the facts", but the space fact was never confirmed. The exercise director should resolve this.
- **Outside the objective.** Note 7 covers the DP-12 checklist and the carrier booking at 23:30–23:50. That came after the decision was logged, which is where the brief's scope ends, so it is not judged here. The dispatch lead's comment, "The checklist made it easy…", may still be worth recording separately.
- **Exercise suggestion not taken up.** Note 9 is the facilitator's proposal for a full-scale carrier-failure exercise. This skill recommends no exercise. Raise it separately through `/ask-ai4bcm` if you want it considered.
- **Intake.** No intake questions were asked, because the brief and the notes answered them.
- **Prompt injection.** None found in either file.

Parts of this document were drafted with AI support (debrief-to-action skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next step:** send this draft to the exercise director or BCM manager. They take the three proposed findings back to the people who were in the debrief. Petra Lindqvist confirms or declines A-1 to A-3, and the reviewer names owners for A-4 and A-5.
