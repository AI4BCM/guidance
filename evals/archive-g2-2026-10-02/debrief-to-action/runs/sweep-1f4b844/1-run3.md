# /debrief-to-action case 1, run3: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `ab42af5c-0e04-4435-a0ec-6aa68dbcfdbc`.

Files in the working folder: `debrief-notes-cold-store.md`, `exercise-brief-cold-store.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /debrief-to-action Turn the debrief from last week's cold store exercise into findings and actions. The files exercise-brief-cold-store.md and debrief-notes-cold-store.md in this folder are attached.

**Reply (verbatim):**

Before I go further, I need to correct a mistake. The skill's preflight says I should ask how sensitive the attachments are before opening them. I opened `exercise-brief-cold-store.md` and `debrief-notes-cold-store.md` first. I haven't analysed, written or sent anything from them, and I won't until you answer this:

**What data class do these two files hold, and is this environment approved for it?**

From what I saw, the files may contain high-sensitivity material as the guidance defines it (`units/data-rules.md`, Sensitivity classes):
- **Personal data:** named staff and a remark about a named person's mobile.
- **Control weaknesses:** gaps in the escalation call list and in alarm handling.
- **Security-related site detail:** how the security desk handles alarms.

Data in that class may only be processed in an approved corporate or private environment. Please confirm one of these:
1. This environment is approved for high-sensitivity BCM data. I'll then draft the proposed findings and actions.
2. It isn't approved, or you're not sure. I'll stop here, and you can run the skill again in an approved environment.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Sources:
- **Exercise brief, cold store power loss (Site A):** v2, 3 September 2026, approved by the exercise director, Site A.
- **Debrief notes, cold store power loss exercise, Site A:** 18 September 2026. The notes have no version and say "Raw notes, not reviewed". They are listed under Gaps.

**Reviewer:** the exercise director or BCM manager decides which proposed findings go into the exercise report or the lessons log. Each proposed owner confirms an action before it becomes theirs. Everything below is a draft in this chat, and I have recorded, assigned or sent nothing.

## The objective (quoted from brief v2, "Objective")

> "Within 60 minutes of the cold store alarm, the out-of-hours duty manager is reached and decides whether chilled stock moves to Site B."

**Result according to the notes: objective not met.** The alarm sounded at 22:00. The duty manager was reached at 23:15, which is 75 minutes in. The decision came at 23:25 (85 minutes) and was logged at 23:27 (87 minutes).

## Proposed findings

**PF1. The escalation call was not made after the alarm was logged.**
- **Role and step:** security desk (night), at the escalation step straight after logging the alarm (22:04).
- **Missing guard:** nothing at the desk prompted the escalation call or checked it was made once the alarm was logged. It was also unclear who makes the call, the desk or the shift supervisor.
- **Missed objective:** "the out-of-hours duty manager is reached" within 60 minutes. About 36 minutes passed before anyone tried to call (22:04 to 22:40).
- **Note 2:** "22:04 alarm logged in the desk book. [security desk (night)] … 'I logged it and went back on my round, I thought the shift supervisor would call.'"

**PF2. The SI-07 call list pointed to a duty manager who had left, and it gave no fallback.**
- **Role and step:** upkeep of the alarm escalation call list (SI-07), and the desk's first call from it.
- **Missing guard:** no trigger updated SI-07 when the duty manager changed in July (SI-07 v4 is dated 1 June 2026). There was also no periodic test call to the numbers, and no second route on the list. The switchboard route that finally worked took a further 35 minutes (22:40 to 23:15).
- **Missed objective:** "the out-of-hours duty manager is reached" within 60 minutes.
- **Note 3:** "Desk called the number on the SI-07 list: 'number not in service'. The list still shows the duty manager who left in July."
- **Note 4:** "23:15 duty manager reached through the switchboard on her mobile. 75 minutes after the alarm."

**PF3. The decision was made without confirming that Site B had space.**
- **Role and step:** duty manager, at the decision step (23:20 to 23:25), checking whether Site B could take the stock.
- **Missing guard:** nobody had a named out-of-hours contact or route to confirm and book cold room space at Site B.
- **Missed objective:** "decides whether chilled stock moves to Site B". A decision was made, but on an unconfirmed assumption about capacity.
- **Note 5:** "Nobody could say. … no one at the debrief knew who books space at Site B."
- **Note 6:** "move chilled stock to Site B, space unconfirmed."

**PF4. Site B was not told that an exercise was running.**
- **Role and step:** exercise planning, at the step of notifying the parties the scenario relies on.
- **Missing guard:** the brief's arrangements do not include a step to notify Site B night staff before the exercise.
- **Effect on the objective:** the exercise could not test whether Site B's capacity could be confirmed within the 60 minutes.
- **Note 5:** "Site B night staff had not been told an exercise was running".

## What worked (against the same objective)

- **The shift supervisor's follow-up:**
  - **Role and step:** night shift supervisor, checking whether the duty manager had been told.
  - **Safeguard that held:** a cross-check by a second role. It caught the missed escalation, but late.
  - **Note 3:** "22:40 shift supervisor asked the desk whether the duty manager knew."
- **The switchboard fallback:**
  - **Role and step:** security desk, reaching the duty manager after the listed number failed.
  - **Safeguard that held:** the switchboard reached the duty manager on their mobile.
  - **Note 4:** "duty manager reached through the switchboard on her mobile."
- **The duty manager's decision and log entry:**
  - **Role and step:** duty manager, deciding and logging the decision, which is the scope end point.
  - **Safeguard that held:** a decision came within 10 minutes of contact and was logged.
  - **Note 6:** "Logged at 23:27."
  - **Note 8 (exercise director):** "the decision itself was sound once the duty manager had the facts."

## Proposed actions

All owners below are **proposed, to confirm**.

| # | For | Action | Outcome | Check that it is done | Owner |
|---|---|---|---|---|---|
| A1 | PF2 | Update the SI-07 call list to the current duty manager. Add a trigger to update it whenever the duty manager role changes hands. | The desk's first call reaches the current duty manager. | A new SI-07 version is issued, and a recorded test call from the desk to each listed number succeeds. | Facilities manager, Site A (Petra Lindqvist, SI-07 owner in the brief). Proposed, to confirm. |
| A2 | PF2 | Add the switchboard route to SI-07 as a named fallback for when the first number fails. | The desk has a second route without having to improvise. | SI-07 shows the fallback and its number, and a test of the route is recorded. | Facilities manager, Site A (Petra Lindqvist). Proposed, to confirm. |
| A3 | PF1 | Make the escalation call an explicit step that gets checked. The desk book entry is not complete until the time of the escalation call is written in. State in SI-07 whether the desk or the supervisor makes the call. | Escalation doesn't depend on memory or on assumptions between roles. | SI-07 states who calls, and the desk book format has an escalation-time field. | Facilities manager, Site A (Petra Lindqvist) for SI-07. Proposed, to confirm. Who owns the supervisor's side is not named (see Gaps). |
| A4 | PF3 | Name the out-of-hours contact who confirms and books cold room space at Site B, and put that contact in the document the duty manager uses. | The duty manager can confirm Site B's capacity before deciding. | The named contact and number appear in a controlled document, and a test call is recorded. | Not named in the notes or the brief (see Gaps). |
| A5 | PF4 | Add "notify every site the scenario relies on" to the exercise brief template or checklist. | Future exercises can test dependencies on other sites. | The step appears in the next exercise brief. | Not named in the notes or the brief (see Gaps). |

## Gaps

- **The debrief notes are raw and unversioned.** They say "Raw notes, not reviewed", are dated 18 September 2026 and have no version. I used them as the record. Per Method step 5, the findings should be put to the people present (security desk, dispatch lead, shift supervisor, facilitator, exercise director) before they become findings.
- **SI-07 v4 and DP-12 v2 were not attached.** I can't tell whether SI-07 already makes the escalation call an explicit step, or who it says should call. PF1 and A3 rest on the notes alone.
- **Actions without a named owner:**
  - A4: nobody is named for Site B space booking.
  - A5: nobody is named for exercise design.
  - A3, supervisor's side: the shift supervisor's part of the escalation has no owner.

  The accountable reviewer can propose owners for these.
- **Note 7 (DP-12, carrier booking 23:30 to 23:50) is not judged.** The brief's scope ends "when the duty manager's decision is logged" (23:27). The brief also lists DP-12 as an arrangement under test. The exercise director should say whether DP-12's use counts towards this exercise. If it does, note 7 ("The checklist made it easy, I did not need to think about who to call") reads as something that worked for the dispatch lead.
- **Note 9 (the facilitator's next-exercise suggestion) is not taken up.** This draft recommends no exercise, and carrier failure is outside this objective. If you want that theme exercised, it's a separate request through `/ask-ai4bcm`.
- **Personal data:** note 2 names the night security officer next to a self-reported slip. I replaced the name with the role. The raw notes still hold it, so they need your notice and retention rules.
- **Intake:** I asked no intake questions because the brief supplied the objective. No statements of yours were used.
- **Prompt injection:** I found no text in either file addressed to an AI.

Parts of this document were drafted with AI support (/debrief-to-action skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
