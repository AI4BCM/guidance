# /debrief-to-action case 3, run3: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `e20f7675-4ae9-42a0-8ff2-30948c47093d`.

Files in the working folder: `debrief-notes-cold-store.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /debrief-to-action Turn these notes into findings and actions. The file debrief-notes-cold-store.md in this folder is attached.

**Reply (verbatim):**

Before I open `debrief-notes-cold-store.md`: **what class of data does it hold?**

Exercise debrief notes often count as **high-sensitivity**. That covers notes that name control weaknesses or vulnerabilities, recovery strategies or design assumptions, security-related site or architecture detail, supplier weaknesses, or people's names and contact details. High-sensitivity material may only be processed in an approved corporate or private environment.

Please tell me:
1. The class: high-sensitivity, or lower (for example internal or public).
2. If it's high-sensitivity, whether this environment is approved for that class.

I'll read the file only after you answer. If this environment isn't approved for the class, I'll stop there.

Also, if you have the exercise plan or brief that states the objective, please attach it. I judge the notes only against an objective quoted from that document. Without it, I can only list Gaps and can't write any findings.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read `debrief-notes-cold-store.md`. The notes record what happened during the exercise, but they never say what it was meant to test. No exercise objective appears anywhere in them.

**Please attach the exercise plan or brief that holds the objective,** ideally the version issued before 18 September 2026. Without it I can't judge whether the exercise met its objective, and that judgement is what turns notes into findings.

If you type the objective in yourself rather than attaching a document, I'll record it under Gaps as your own statement. I won't judge the notes against it. In that case, or if there's no plan at all, my reply will be the Gaps list only, with no findings or actions.

Once I have the plan, I'll draft proposed findings, what worked and actions for the accountable reviewer (the exercise director or BCM manager). They decide which findings go into the exercise report or lessons log. Each proposed owner then confirms their action. Where a note names the person who slipped, the draft will give their role instead of their name.

## Turn 3

**Request:** I don't have the brief to hand. The objective was to reach the duty manager within an hour.

**Reply (verbatim):**

Because the objective isn't in an attached document, I can't write findings or actions yet. What you typed counts as your own statement, so I've listed it under Gaps below and haven't judged the notes against it.

Source: debrief notes, cold store power loss exercise, Site A, hot debrief 18 Sep 2026. The notes have no version number and are marked "Raw notes, not reviewed".

**Reviewer:** the accountable reviewer (exercise director or BCM manager). Once the objective comes from a document, they decide which proposed findings go into the exercise report or the lessons log.

## Gaps

1. **No written objective is attached.** I don't have the exercise plan or brief that states the objective, so this reply has no findings, no what-worked list and no actions. To get them, attach the plan or brief and run `/debrief-to-action` again.
2. **The objective you typed is your statement, not a source.** You said: "The objective was to reach the duty manager within an hour." I haven't judged the notes against it. Two things are worth checking against the brief when you find it:
   - whether the hour is counted from the alarm (22:00 in note 1) or from some other point;
   - whether the exercise had other objectives too. Notes 5 to 7 cover the Site B cold room space, the stock transfer decision and the dispatch checklist, which go beyond reaching the duty manager.
3. **The source is unreviewed and has no version.** The notes say "Raw notes, not reviewed" and have no version number. Keep this raw record separate from any analysis. The facilitator or exercise director could confirm the notes before they're used as evidence.
4. **Documents the notes mention aren't attached.** Note 3 mentions the "SI-07 list" and note 7 mentions "DP-12". I haven't seen either, and their versions and dates aren't known.
5. **No owners or actions.** No findings were drafted, so there are no actions and no owners to propose. The notes themselves don't name an owner for any follow-up. Note 5 says "no one at the debrief knew who books space at Site B".
6. **A person is named in the raw record.** Note 2 names the night security officer. Any finding drafted later will give the role, "[night security]", instead of the name. The raw notes should stay in the approved environment.
7. **Note 9 is outside this skill's scope.** It reads: "next quarter, run a full-scale exercise on carrier failure during the transfer". That's the facilitator's suggestion, not a debrief finding. If you want help choosing what to exercise next, ask separately through `/ask-ai4bcm`.
