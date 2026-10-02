# /ask-ai4bcm, G2 on Claude Code: three runs per case

Commit under test: **0bd09b1**, the router at 1,021 words: the 6aaa84b cut (owner, 2026-10-02: "way too long, cut
it") with three phrases put back that the 6aaa84b sweep failed cases 1 and 3 on. "recovery fields blank" and "Level 2,
Repeatable" are back in the Analysis route, "quoting no definition" is back in the vocabulary line, and "Classify
first" now opens the precondition. Claude Code 2.1.284, `--plugin-dir`, `--setting-sources project`,
`--permission-mode dontAsk`, `--allowedTools Read,Glob,Grep`, stdin closed, 2026-10-02. Each run ran in its own fresh,
empty folder. Every case is a request alone and finished in one turn. There is no attachment, so no data class was sent
and the preflight asked no data-class question. Cases 1 to 3 ran with `--output-format json`, case 4b with
`--output-format stream-json --verbose`. Verbatim turns: `runs/sweep-0bd09b1/<case>-run<N>.md`. No run looks broken or
incomplete. The 6aaa84b record's judgement calls are followed here where they apply, and the owner's rulings of
2026-10-02 in `evals/README.md` apply.

Rule: fail = anything in the Fail column; partial = no Fail item, but part of a Pass row missing; pass = every Pass
row met. A case passes on two of three runs.

| Case | Run 1 | Run 2 | Run 3 | Case | Non-pass runs: the row they break |
|---|---|---|---|---|---|
| 1 BIA interview | pass | pass | pass | pass | |
| 2 challenge or red-team | pass | pass | pass | pass | |
| 3 teach me RTO | pass | pass | pass | pass | |
| 4a by name | pass | pass | pass | pass | Evidence: every `/ask-ai4bcm` run in cases 1 to 3 answered in the router's shape (skill, unit, level, gate, effort, data rule, then stop) |
| 4b no name | pass | pass | pass | pass | |

**Verdict: /ask-ai4bcm passes G2 on Claude Code at 0bd09b1** (12 of 12 runs, every case). Both 6aaa84b failures are
gone:
- Case 1, rows 2 and 3: all three runs now say the recovery fields stay blank and give "Level 2, Repeatable" (run 3:
  "2, Repeatable").
- Case 3, row 2: no run quotes the glossary definition, and none says what an RTO is.

## Evidence per case (one line each)

- **1:** all three name **`/prepare-bia`** first, with `units/prompts/bia.md`, Task choice 1 and the recovery fields
  blank:
  - run 1: "It runs [`units/prompts/bia.md`], Task choice 1, and leaves the recovery fields blank"
  - run 2: "Task choice 1. Leave the recovery fields blank"
  - run 3: "**Task choice 1**. Leave the recovery fields blank"

  All three give Level 2, Repeatable with the four-part gate ("a saved prompt, approved tools, a written data rule and
  a named reviewer"). All three put `units/data-rules.md` first, before anything is pasted. None drafts any part of the
  guide or any question, and none starts the skill.
- **2:** all three say "Use `/red-team-assumptions`" for "the option everyone already likes". All three give the
  router's test, for example run 3: challenge "questions you about a plan you own, round by round, and only gives its
  view after you answer", while red-team "reads the paper and returns the full list of those assumptions in one reply".
  All three give Level 3 with its gate, the data rule first, no assumptions listed, and no skill run.
- **3:** all three name **`/learn-bcm`** for the teaching and the RTO entry in `units/glossary.md` (each gives "line
  30"). None quotes the definition, none expands the acronym, and none states how RTO relates to MTPD:
  - Run 2 says only that "the glossary defines RTO in relation to MTPD".
  - Run 3 says that `analysis.md` "covers ... how it relates to the MTPD".

  What they add is where the term is used: run 1 "that's where the business impact analysis (BIA) sets RTOs", run 2
  "where RTOs get set". I grade that as routing context, not an explanation.

  Run 3 comes closest to the line. It says that `analysis.md` "says that AI can test whether a proposed RTO fits the
  impact criteria but doesn't set it", and that `/prepare-bia` "leaves the RTO field blank, because the activity owner
  sets that number in the interview, not the AI". That describes the unit and the next skill, not the term, so I grade
  it as a pass. If the owner reads "who sets it" as explanation, only run 3 moves to fail, and the case still passes on
  runs 1 and 2.
- **4b:** I checked each run's session file: 0 `Skill` tool calls and 0 reads of any `SKILL.md`. No reply has the
  router's shape (no level with a gate).
  - Runs 1 and 3 named `units/stages/analysis.md` and `units/prompts/bia.md` from the owner's published "Get the
    guidance" artifact page, as in the two earlier sweeps.
  - Run 3 quotes "what is pasted into the wrong tool cannot be unpasted", which is the router's precondition line. It
    comes from a saved `Artifact` tool result (`tool-results/artifact-adb025cb-1789052426-a3ff.html` holds the
    phrase), not from the skill.
  - Run 2 found nothing and answered from general BIA practice, with a sample interview prompt of its own.

## Slips that fail no row

- **Case 1 run 1 still does not say "classify".** It says "Read [`units/data-rules.md`] before you paste anything".
  Runs 2 and 3 now use the word ("Before anything else, classify your material", "Classify what you plan to use before
  you paste anything"). Graded as met under the 6aaa84b call: every run puts `units/data-rules.md` first and before
  anything is pasted. The owner's "Classify first" ruling is about the data class being the first question asked, and
  here the router asks none.
- **Case 3 still makes up a route for a word question.**
  - All three give Level 1, and runs 1 and 3 add the gate "an approved tool, with nothing confidential put/pasted in",
    taken from the "Where do we start?" on-ramp.
  - Runs 1 and 3 add a next move to `/prepare-bia` (run 3 with "Level 2").
  - The vocabulary line gives a word question none of this. The a5abfa8 and 6aaa84b records noted the same.
- **A second skill after the route:**
  - Case 1 run 1 offers `/learn-bcm` "to brush up on running a BIA interview".
  - Case 2 runs 1 and 3 offer `/challenge-my-plan` after the red-team pass.

  Each is named after the chosen skill as an optional later step, and none runs, so this follows the earlier call.
- **Case 1, a second route besides /prepare-bia:** all three name the Level 3 "over connected records" rung with its
  self-check gate. This is route content, not a draft.
- **Case 1 run 3 splits dispatch into made-up activities:** "Inbound scheduling, outbound loading and carrier handover
  would be three runs". It is an example of the "per activity" effort rule, not a guide or a question, so it is not a
  draft of the work. Still, it is invented scope the router text does not give.
- **Case 2 run 2 invents a fallback below the gate:** "do the work at Level 2 instead. That means pasting in the paper
  plus the relevant requirements by hand, through an approved tool, with a named reviewer". The Design route names no
  Level 2 option.
- **4b environment:** with only Read, Glob and Grep allowed, read-only Bash, `ToolSearch`, Drive and SharePoint
  search, and `Artifact` reads still ran or were attempted. So runs 1 and 3 answered from the owner's own published
  artifact page, and runs 2 and 3 read `~/.claude/projects/-tmp/memory/MEMORY.md`. This comes from the test machine,
  not the skill.

## Non-pass runs and their cause

**The 6aaa84b failures, one by one:**
- **Case 1, row 2 (recovery fields blank): gone.** All three runs say it, and the restored phrase is the source.
- **Case 1, row 3 ("Level 2, Repeatable"): gone.** All three runs give it.
- **Case 3, row 2 (definition quoted, RTO explained): gone.** No run quotes the definition, and none says what an RTO is.
- **The "Classify first" slip: mostly gone.** Two of three case 1 runs now use the word. Run 1 still says "Read data-rules.md before you paste anything", which meets the row as before.

**Checks I made beyond the run files (read-only):**
- `wc -w` on `ask-ai4bcm/SKILL.md` gives 1,021 words, matching the brief.
- In the 4b session files under `~/.claude/projects/*ask-ai4bcm-4b-run*-work`, the only "Skill" entries are the tool list itself. No tool call ran a skill or read a `SKILL.md`.
- The "cannot be unpasted" quote in 4b run 3 comes from a saved Artifact tool result, not from the skill.
- The other session files in those folders are the 6aaa84b sweep's earlier runs in the same folders.
