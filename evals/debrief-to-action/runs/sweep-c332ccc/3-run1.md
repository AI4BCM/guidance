# /debrief-to-action case 3, run1: Claude Code, guidance at c332ccc

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `db2a9af6-2659-4235-87bd-7ef8610264d5`.

Files in the working folder: `debrief-notes-cold-store.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /debrief-to-action Turn these notes into findings and actions. The file debrief-notes-cold-store.md in this folder is attached.

**Reply (verbatim):**

Before I open `debrief-notes-cold-store.md`, I need to know one thing first.

**What class of data do these debrief notes hold?** For example:

- **High-sensitivity:** incident records or live crisis information, personal data (names, contact lists), vulnerabilities and control weaknesses, recovery strategies and design assumptions, supplier weaknesses, security-related site or architecture detail, or audit findings the audit owner hasn't cleared yet.
- **Not high-sensitivity:** for example, a fictional or training exercise with no real names, sites or weaknesses.

If the notes are high-sensitivity, also confirm that this environment is approved for that class. If it isn't, I'll stop here and won't read the file.

Exercise debriefs often record control weaknesses that showed up, plus the names of the people involved. That's why I'm asking before opening it.

Once you've answered, I'll read the notes. I'll also need the objective that was set before the exercise, quoted from the exercise plan or brief. Only the notes are attached right now, so please attach that document too if you have it. Without it I can list Gaps but can't draft any findings.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Source stamp:** debrief notes on the cold store power-loss exercise at Site A, hot debrief of 18 September 2026, 01:00–01:40. They have no version number and are marked "Raw notes, not reviewed." This is the only document attached.

**Reviewer:** the accountable reviewer (the exercise director or the BCM manager) decides which proposed findings go into the exercise report or the lessons log. Each proposed owner confirms an action before it becomes theirs.

I can't draft findings yet. Each finding has to be judged against the objective written before the exercise, quoted from the exercise plan or brief, and neither is attached. Please attach the document that holds the objective. If you type the objective in yourself, I'll list it under Gaps as your own statement and still won't judge anything against it.

## Gaps

1. **Objective missing.** No exercise plan or brief is attached, so it's "not in the sources" what this exercise was meant to test. Until it's attached, no finding, what-worked line or action can be tied to an objective. Notes 2–7 all bear on escalation, contact lists, alternate-site capacity and dispatch. Whether each one is a proposed finding, a what-worked line or out of scope depends on that objective.
2. **Source status.** The notes have no version, and the facilitator recorded them as "Raw notes, not reviewed." Per Method step 3, they should stay unchanged as the raw record, kept apart from any analysis. Per step 5, the pattern should go back to the people who were present (security desk, dispatch lead, night shift supervisor) before anything becomes a finding.
3. **How the exercise was run (for the accountable reviewer, not a finding).** Note 5 says: "Site B night staff had not been told an exercise was running". This is about how the exercise was set up, not what it tested. The exercise director should decide whether it affected the result at 23:20.
4. **An exercise recommendation is out of scope here.** Note 9 says: "Facilitator's own suggestion: next quarter, run a full-scale exercise on carrier failure during the transfer." This skill doesn't recommend exercises. If you want to take it forward, make it a separate request through `/ask-ai4bcm`.
5. **A person is named in the notes.** Note 2 names the individual on night security. Any finding I draft later will name the role, "[night security]", not the person. The raw notes themselves should be kept and shared under your retention and access rules for high-sensitivity personal data.

Attach the exercise plan or brief, and I'll draft the proposed findings, what worked and the actions against its objective.

## Turn 3

**Request:** I don't have the brief to hand. The objective was to reach the duty manager within an hour.

**Reply (verbatim):**

I can't draft findings against that objective yet. A typed objective is your own statement, not an objective quoted from the plan or brief, and this skill only judges notes against an objective it can quote from a document. A finding judged against a remembered objective could end up in the exercise report with nothing behind it. I've added your statement to Gaps, and the reply still ends there.

**Source stamp:** debrief notes on the cold store power-loss exercise at Site A, hot debrief of 18 September 2026. They have no version number and are marked "Raw notes, not reviewed."

**Reviewer:** the accountable reviewer (exercise director or BCM manager) decides which proposed findings go into the exercise report or the lessons log. Each proposed owner confirms their action.

## Gaps

1. **Objective not from a source.** No plan or brief is attached. You stated the objective as "reach the duty manager within an hour". That is your own statement, so I haven't judged anything against it. The written objective may also set out more than that one target, for example the decision on moving stock or the dispatch steps, and those would change which notes become findings.
2. **Source status.** The notes have no version and say "Raw notes, not reviewed." Keep them unchanged as the raw record. Put the pattern to the people who were there before anything becomes a finding.
3. **How the exercise was run (for the accountable reviewer, not a finding).** Note 5 says: "Site B night staff had not been told an exercise was running".
4. **Out of scope.** Note 9 is the facilitator's exercise suggestion. If you want to take it forward, use `/ask-ai4bcm`.
5. **A person is named.** Note 2 names the person on night security. Any later finding will say "[night security]" instead of the name. Handle the raw notes under your rules for high-sensitivity personal data.

**Next step:** when you can get the plan or brief, attach it. The exercise director should hold a copy if you don't. I'll then draft the proposed findings, what worked and the actions in one pass.
