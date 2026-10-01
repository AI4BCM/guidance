# /debrief-to-action case 3, run2: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `77628999-6043-42a9-9c86-c6a22422cab2`.

Files in the working folder: `debrief-notes-cold-store.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /debrief-to-action Turn these notes into findings and actions. The file debrief-notes-cold-store.md in this folder is attached.

**Reply (verbatim):**

Before I open `debrief-notes-cold-store.md`, I need to know one thing: **what class of data is in it?**

Exercise debrief notes often hold material that counts as high-sensitivity under this guidance. That includes:

- control weaknesses or vulnerabilities found during the exercise
- incident records or live crisis information
- recovery strategies and design assumptions
- weaknesses or contractual dependencies of suppliers
- detail about security architecture or sites (a cold store may count)
- personal data, such as names, contact details or personnel records

Please confirm one of these:

1. **High-sensitivity**, and this Claude Code environment is approved by your organisation for that class. I'll go ahead.
2. **High-sensitivity**, and this environment is **not** approved for it. I'll stop here and won't open the file.
3. **Not high-sensitivity** (for example internal or public). I'll go ahead.

Also, if the file has any passwords, keys or access tokens in it, please take them out first. They don't go into any tool, approved or not.

Once you've answered, I'll read the notes. To judge them I also need the exercise objective, quoted from the plan or exercise brief. If that document isn't in this folder, I'll ask you for it next.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Source stamp:** from `debrief-notes-cold-store.md`, raw facilitator notes from the hot debrief on 18 Sep 2026. They have no version number and say "Raw notes, not reviewed".

**Who reviews this:** the accountable reviewer, which is the exercise director or the BCM manager. They decide which proposed findings go into the exercise report or the lessons log. Each proposed owner then confirms their own action.

## Gaps

1. **There's no exercise objective, so I've written no findings.** No plan or exercise brief is attached, and the notes don't state what the exercise was meant to test. Without that objective I can't say what passed or failed. I haven't written any proposed findings, any "what worked" items or any actions. Please attach the exercise plan or brief that sets out the objective (with its version and date), and I'll do the rest of the analysis against it.
   - If you type the objective here instead of attaching it, I'll treat it as your own statement and list it here. I won't judge the notes against it.
2. **The notes are raw and unversioned.** They're marked "Raw notes, not reviewed" and have no version. I'll use them only as the raw record. They should stay separate from the analysis, and the people who were there should confirm them before anything becomes a finding.
3. **Two documents the notes rely on aren't attached:** SI-07 (the escalation and contact list) and DP-12 (the dispatch checklist). Their versions and dates are unknown. That matters most for SI-07: line 3 says it "still shows the duty manager who left in July".
4. **Site B wasn't in the debrief.** Line 5 says "Site B night staff had not been told an exercise was running, and no one at the debrief knew who books space at Site B". Nobody from Site B was present to give their side.
5. **Owners:** the notes name nobody who owns any follow-up. Unless the plan names owners, every action will be listed here as having no owner.
6. **One person is named.** Line 2 names the night security officer. In the draft I'll replace the name with the role, [night security desk]. You may want to check whether the raw record should keep the name, given your retention and notice rules.
7. **Exercise suggestion out of scope:** line 9 has the facilitator's suggestion of a full-scale exercise on carrier failure during the transfer. This skill doesn't recommend exercises. If you want to pursue it, ask separately through `/ask-ai4bcm`.

Once the plan or exercise brief with the objective is in this folder, I'll draft the proposed findings, what worked and the actions.

## Turn 3

**Request:** I don't have the brief to hand. The objective was to reach the duty manager within an hour.

**Reply (verbatim):**

I've noted that, but I still can't judge the notes against it. Because you've typed the objective from memory rather than quoting it from the plan or brief, this skill treats it as your own statement, not a source. The exercise report and the lessons log need an objective that can be traced to the document written before the exercise. Otherwise a finding rests on what someone remembers the goal was. So there are still no proposed findings and no actions. The Gaps below are updated.

**Source stamp:** from `debrief-notes-cold-store.md`, raw facilitator notes from the hot debrief on 18 Sep 2026. They have no version number and say "Raw notes, not reviewed".

**Who reviews this:** the accountable reviewer, which is the exercise director or the BCM manager. They decide which proposed findings go into the exercise report or the lessons log. Each proposed owner confirms their own action.

## Gaps

1. **The objective is your statement, not a source.** You said: "The objective was to reach the duty manager within an hour." Nothing has been judged against it.
   - Please check it against the plan or exercise brief when you have it. Make sure the wording, the time limit and the point the clock starts from all match. The notes time the escalation from the 22:00 alarm (line 4: "75 minutes after the alarm").
   - Also check whether the brief sets other objectives. For example, the notes record the Site B transfer and dispatch steps in detail (lines 5 to 7), and those may have objectives of their own.
2. **The notes are raw and unversioned.** They're marked "Raw notes, not reviewed" and have no version. I'll use them as the raw record only, kept separate from the analysis. The people who were there should confirm them before anything becomes a finding.
3. **Two documents aren't attached:** SI-07 (the escalation and contact list) and DP-12 (the dispatch checklist). Their versions and dates are unknown.
4. **Site B wasn't in the debrief.** Nobody from Site B was present (line 5).
5. **Owners:** the notes name nobody who owns any follow-up.
6. **One person is named.** Line 2 names the night security officer. In any draft I'll use the role, [night security desk].
7. **Exercise suggestion out of scope:** the facilitator's suggestion of a carrier-failure exercise (line 9) is a separate request for `/ask-ai4bcm`.

Once the plan or brief is in this folder, run `/debrief-to-action` again and I'll draft the proposed findings, what worked and the actions against the objective as it's written there.
