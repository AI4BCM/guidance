# /debrief-to-action case 3, run2: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `843974c6-72e6-4047-bd22-949f89a13925`.

Files in the working folder: `debrief-notes-cold-store.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /debrief-to-action Turn these notes into findings and actions. The file debrief-notes-cold-store.md in this folder is attached.

**Reply (verbatim):**

Before I work on these notes I need to know one thing.

**What data class do the debrief notes hold (for example public, internal, confidential or restricted)?** They name a staff member, mention another person's personal mobile, and describe a security gap at Site A. If this environment isn't approved for that class, I'll stop here.

I've already opened the file, which I shouldn't have done before asking. I haven't analysed it or sent it anywhere, and I won't until you've answered.

Once the class is settled, the next step is the exercise's objective, which has to come from the exercise plan or brief, so please attach that document. You've only attached the notes. Without the plan or brief I can't propose any findings. I'd only return the Gaps, and an objective you type in yourself would go under Gaps as well.

The exercise director or BCM manager reviews the result. They decide which proposed findings go into the exercise report or the lessons log.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

The data class is high and this environment is approved for high, so I've read the notes. You haven't attached the exercise plan or brief, so I can't judge the notes against an objective. As the skill requires, this reply stops at the Gaps: it contains no findings, no "what worked" lines and no actions.

**Source:** "Debrief notes: cold store power loss exercise, Site A". The notes have no version number. They are dated 18 September 2026 and marked "Raw notes, not reviewed".

## Gaps

1. **The exercise objective is missing.** No exercise plan or brief is attached, so I have no record of what this exercise was meant to test before it ran. Without that, none of the notes can become a proposed finding, and an objective you type in won't fill the gap either. The closest thing in the notes is the exercise director's judgement in note 8: "the decision itself was sound once the duty manager had the facts". That is a verdict reached afterwards, not the objective set beforehand. **To continue:** attach the plan or brief that holds the objective, then run `/debrief-to-action` again.
2. **The notes are raw and unreviewed.** They are the facilitator's own record, taken 18 September 2026 from 01:00 to 01:40, with no version number. When the analysis runs, they stay the raw record, kept separate from it (validate.md, Method step 3). The people who were there should see any pattern before it becomes a finding (Method step 5).
3. **The notes name an individual.** Note 2 names the person on the night security desk. In any draft, the name will be replaced with the role, [night security desk officer]. The raw notes themselves are left as they are, and their retention is for the notes' owner to decide.
4. **The notes name no owners.** No one in the notes is named as responsible for:
   - keeping the SI-07 contact list current (note 3)
   - booking cold-room space at Site B (note 5: "no one at the debrief knew who books space at Site B")
   - telling Site B night staff that an exercise is running (note 5)

   If any of these become actions once the objective is attached, they'll appear with no owner unless the plan names one.
5. **Note 9 is outside this skill's scope.** It is the facilitator's suggestion to "run a full-scale exercise on carrier failure during the transfer". This skill doesn't recommend exercises. If you want that theme looked at, ask separately through `/ask-ai4bcm`.

I haven't changed or sent anything.

## Turn 3

**Request:** I don't have the brief to hand. The objective was to reach the duty manager within an hour.

**Reply (verbatim):**

Thanks. I've added it to the Gaps, but I still can't judge the notes against it. The skill only accepts an objective quoted from a plan or brief written before the exercise. An objective given from memory afterwards can't show what the exercise was set up to test, and an auditor would look for the written version.

**Source:** "Debrief notes: cold store power loss exercise, Site A". The notes have no version number. They are dated 18 September 2026 and marked "Raw notes, not reviewed".

## Gaps (additions)

1. **Your statement of the objective, not from a source:** "The objective was to reach the duty manager within an hour." I haven't judged the notes against it. It may help identify the right brief, but it doesn't replace it. One point to check when you find the brief: it should say whether the hour runs from the alarm at 22:00, from when the alarm was logged at 22:04, or from some other point.
2. **The exercise brief or plan still isn't attached.** The exercise director or facilitator probably holds it, or it's filed with the exercise documents. When you have it, attach it and run `/debrief-to-action` again. I'll then propose findings and actions, with the night security desk officer's name replaced by the role, as above.

Gaps 1 to 5 from my previous reply still apply. I haven't changed or sent anything.
