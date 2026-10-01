# /debrief-to-action case 1, run2: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `c0b37ffe-f892-4720-bd97-d189ed97d59f`.

Files in the working folder: `debrief-notes-cold-store.md`, `exercise-brief-cold-store.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /debrief-to-action Turn the debrief from last week's cold store exercise into findings and actions. The files exercise-brief-cold-store.md and debrief-notes-cold-store.md in this folder are attached.

**Reply (verbatim):**

Before I go further, I have to tell you something and ask you something.

**What happened:** This skill's preflight says to ask what class of data the attachments hold *before* opening them. I opened `exercise-brief-cold-store.md` and `debrief-notes-cold-store.md` before asking. That was my mistake. I haven't drafted anything, and I won't until you answer.

**The question:** What class of data do these two files hold, and is this environment approved for that class?

The guidance's data rules (`units/data-rules.md`) list these as high-sensitivity, for an approved corporate or private environment only:

- personal data, contact lists and personnel records
- vulnerabilities and control weaknesses
- incident records and live crisis information
- security-related architecture or site detail
- recovery strategies and design assumptions
- supplier weaknesses and contractual dependencies

From what I've already seen, the notes name individual staff and describe a broken escalation contact list. That is at least personal data and a control weakness at Site A.

- **If this environment is approved for high-sensitivity BCM data:** say so. I'll then draft the proposed findings, what worked, and actions against the brief's objective, as a draft in this chat only. The exercise director, as accountable reviewer, decides what goes into the report or lessons log.
- **If it isn't approved, or you're not sure:** I'll stop here and work with nothing from these files. You may also want to tell whoever owns this environment's approvals that the files were opened here.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Thanks. Here is the draft. Nothing has been recorded, assigned or sent.

**Sources**
- From exercise brief "cold store power loss (Site A)", version 2, 3 September 2026, approved by the exercise director.
- From debrief notes, 18 September 2026. They have no version and say "Raw notes, not reviewed" (see Gaps).

**Reviewer:** the exercise director, as accountable reviewer, decides which proposed findings go into the exercise report or the lessons log. Each proposed owner confirms their action before it is theirs.

**Objective**, quoted from the brief: *"Within 60 minutes of the cold store alarm, the out-of-hours duty manager is reached and decides whether chilled stock moves to Site B."*

Both parts were missed:
- **Reached:** at 23:15, 75 minutes after the alarm (note 4).
- **Decides:** the decision was logged at 23:27, 87 minutes after the alarm (note 6).

---

## Proposed findings

**PF1. Escalation stopped at the desk after the alarm was logged**
- **Part of the objective missed:** "the out-of-hours duty manager is reached" within 60 minutes.
- **Role and step:** night security desk, the escalation step after logging the alarm at 22:04.
- **Note 2:** "[Night security] said [they] forgot the escalation step: 'I logged it and went back on my round, I thought the shift supervisor would call.'"
- **Missing guard:** nothing marked the escalation as done. Who calls (the desk or the shift supervisor) was not clear enough to stop each assuming the other would. Nothing escalated until the supervisor asked at 22:40, 36 minutes after the log (note 3).

**PF2. The duty manager number on the SI-07 call list was out of date**
- **Part of the objective missed:** "the out-of-hours duty manager is reached" within 60 minutes.
- **Role and step:** whoever keeps the SI-07 call list, at the step of updating it when staff change.
- **Note 3:** "number not in service". "The list still shows the duty manager who left in July."
- **Missing guard:** nothing triggers a list update when a duty manager leaves, and the numbers are not test-called. SI-07 v4 is dated 1 June 2026, before the July departure. Reaching the duty manager through the switchboard then took another 35 minutes, 22:40 to 23:15 (note 4).

**PF3. The decision was taken without confirmed space at Site B**
- **Part of the objective missed:** "decides whether chilled stock moves to Site B". A decision was taken, late, but without the fact it rests on.
- **Role and step:** duty manager, deciding on the move; no arrangement gave them Site B capacity.
- **Note 5:** "Nobody could say. Site B night staff had not been told an exercise was running, and no one at the debrief knew who books space at Site B."
- **Note 6:** "move chilled stock to Site B, space unconfirmed."
- **Missing guard:** none of the arrangements under test (SI-07, DP-12) includes a Site B capacity check or a contact who can book space. The exercise also did not tell Site B night staff it was running.

## What worked, against the same objective

- **W1. Shift supervisor, checking whether the duty manager knew (22:40, note 3).** The cross-check worked as a backstop and started the escalation. It came 36 minutes after the alarm, so it held late.
- **W2. Switchboard as a fallback route (note 4).** It reached the duty manager "through the switchboard on her mobile" after the list failed. The sources don't say whether this route is written down (see Gaps).
- **W3. Duty manager, deciding and logging once reached (notes 6 and 8).** The decision was logged at 23:27, 12 minutes after contact, so the decision log worked. The exercise director said: "the decision itself was sound once the duty manager had the facts". The reviewer may want to set this against "space unconfirmed" in note 6.

## Proposed actions

All owners are **proposed, to confirm**.

| # | For | Action | Outcome | Done when | Owner |
|---|---|---|---|---|---|
| A1 | PF1 | State in SI-07 which role calls the duty manager, and when (for example, straight after logging the alarm), with the time of the call recorded in the desk book. Brief the night security desk on it. | The desk escalates without waiting for another role. | The next SI-07 version shows the step and its role, and night security confirm the briefing. | Petra Lindqvist, Facilities manager, Site A (named in the brief as SI-07 owner), proposed, to confirm |
| A2 | PF2 | Correct the duty manager entry on the SI-07 call list. Add a trigger to review the list whenever an out-of-hours duty manager joins or leaves, plus a dated test call of every number. | The list reaches the current duty manager at first attempt. | Every number on the list answers a dated test call. | Petra Lindqvist, proposed, to confirm |
| A3 | PF2 | If the switchboard route is not already in SI-07, add it as the fallback when a number fails. | The desk has a second route without improvising. | SI-07 names the fallback route. | Petra Lindqvist, proposed, to confirm |
| A4 | PF3 | Find out who books cold-room space at Site B out of hours, and add a capacity check with that contact to the arrangement the duty manager uses before deciding. | The decision rests on confirmed Site B space. | The named contact and the check appear in a controlled document, and a test call confirms them. | **No owner named in the notes or the brief** (see Gaps) |
| A5 | PF3 | For future exercises that involve Site B, tell Site B night staff in advance that an exercise is running. | Site B can answer questions during the exercise. | The next exercise brief that involves Site B lists Site B in its notification list. | Exercise director (role named in the brief, no person named; see Gaps), proposed, to confirm |

---

## Gaps

- **The debrief notes** have no version, are dated 18 September 2026, and say "Raw notes, not reviewed". The proposed findings should go to the people who were there (security desk, shift supervisor, dispatch lead) before any becomes a finding.
- **The duty manager is not on the debrief's attendee list.** Their account of notes 4 to 6 is not in the sources.
- **SI-07 v4 (1 June 2026) and DP-12 v2 (20 May 2026) were not attached.** I could not check whether SI-07 assigns the escalation call to the desk, or whether it lists the switchboard fallback. PF1, A1 and A3 depend on that.
- **No owner is named for A4**, the Site B booking contact and capacity check. Note 5 says no one at the debrief knew who books space at Site B.
- **A5's owner** is the exercise director, a role the brief names without naming a person.
- **Note 7 falls outside the exercise scope.** The dispatch work (DP-12, first truck slot by 23:50) happened after the decision was logged at 23:27, which is where the brief's scope ends. The brief also places "carrier booking beyond the first call" out of scope. I judged note 7 against nothing. The reviewer may want to record it separately. The note says: "The checklist made it easy, I did not need to think about who to call." DP-12 is listed as an arrangement under test, but the scope ends before it applies, which is worth raising with the brief's owner.
- **Note 8 and note 6 pull against each other.** The exercise director called the decision "sound once the duty manager had the facts", but it was taken with "space unconfirmed". This is for the reviewer to settle.
- **Note 9**, the facilitator's suggestion of a full-scale carrier-failure exercise, is not taken up here. This skill recommends no exercise.
- **Intake:** I asked no questions, because the brief supplied the objective.
- **Prompt injection:** none found in either file.

Parts of this document were drafted with AI support (/debrief-to-action, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

To turn a theme into a next exercise (for example the escalation route, or note 9's carrier failure), ask for it separately through `/ask-ai4bcm`.
