# /ask-ai4bcm, G2 on Claude Code: three runs per case

Commit under test: **6aaa84b**, the router cut from 2,467 to 1,012 words at the owner's request (2026-10-02: "way
too long, cut it"). All 16 routes keep their unit, prompt, level, gate, effort and data rule. Claude Code 2.1.284,
`--plugin-dir`, `--setting-sources project`, `--permission-mode dontAsk`, `--allowedTools Read,Glob,Grep`, stdin
closed, 2026-10-02. Each run ran in its own fresh, empty folder. Every case is a request alone and finished in one
turn: there is no attachment, so no data class was sent and the preflight asked no data-class question. Case 4b ran
with `--output-format stream-json --verbose`. Verbatim turns: `runs/sweep-6aaa84b/<case>-run<N>.md`. No run looks
broken or incomplete. The previous record, at a5abfa8 on the long text, passed on every run; its judgement calls are
followed here where they apply.

Rule: fail = anything in the Fail column; partial = no Fail item, but part of a Pass row missing; pass = every Pass
row met. A case passes on two of three runs.

| Case | Run 1 | Run 2 | Run 3 | Case | Non-pass runs: the row they break |
|---|---|---|---|---|---|
| 1 BIA interview | partial | partial | partial | **fail** | Row 2: no run says the recovery fields are left blank. Row 3: no run gives "Repeatable" with Level 2 |
| 2 challenge or red-team | pass | pass | pass | pass | |
| 3 teach me RTO | fail | fail | fail | **fail** | Row 2 Fail: "An explanation of RTO beyond a one-line pointer". All three quote the glossary definition; runs 1 and 2 go on to explain it |
| 4a by name | pass | pass | pass | pass | Evidence: every `/ask-ai4bcm` run in cases 1 to 3 answered in the router's shape (skill, unit, level, gate, effort, data rule, then stop) |
| 4b no name | pass | pass | pass | pass | |

**Verdict: /ask-ai4bcm fails G2 on Claude Code at 6aaa84b.** Cases 1 and 3 fail on three of three runs. Both
failures come from text the cut removed, because the a5abfa8 text carried both and passed:
- "recovery fields blank" and "Level 2, Repeatable" were in the Analysis route.
- "quoting no definition" was in the vocabulary line.

## Evidence per case (one line each)

- **1:** all three name **`/prepare-bia`** first. Each gives `units/prompts/bia.md`, Task choice 1, then "Level 2"
  and the four-part gate ("a saved prompt, approved tools, a written data rule and a named reviewer"). Each puts the
  data rule first, before anything is pasted. None drafts any of the guide or any question. But none says the recovery
  fields stay blank: run 1 says "It runs Task choice 1 in `units/prompts/bia.md` and gives you an interview pack", run 2
  "This is Task choice 1", run 3 "It runs Task choice 1". None says "Repeatable": runs 1 and 2 say "Maturity level: 2.",
  run 3 "Level 2." The cut text's Analysis route reads only "([`../units/prompts/bia.md`], Task choice 1). Level 2;",
  where a5abfa8 read "Task choice 1, recovery fields blank. **Level 2, Repeatable**".
- **2:** all three say "Use `/red-team-assumptions`" because the option is "the option everyone already likes". All
  three give the router's test, for example run 1: challenge "questions *you* about a plan you own, one round at a time,
  and only gives its view once you've answered", while red-team "reads the paper and returns, in one reply, everything
  it relies on". All three give Level 3 with its gate, the data rule first, no assumptions listed, and no skill run.
- **3:** all three name **`/learn-bcm`** and the RTO entry in `units/glossary.md`, but all three quote the definition
  ("Recovery Time Objective: the time frame within the MTPD for resuming disrupted activities at a specified minimum
  acceptable capacity (ISO 22301:2019)").
  - Run 1 adds two bullets of explanation: "The RTO always sits inside the MTPD ... The RTO is the earlier target you
    set so that you resume before you reach it", and "covers getting back to a minimum acceptable capacity, not to full
    normal operation".
  - Run 2 adds "MTPD is how long an activity can be down before the impact becomes unacceptable. The RTO has to fall
    inside that limit", plus "the business impact analysis (BIA) records an RTO for each IT system and application" and
    "the activity owner sets the RTO".
  - Run 3 quotes the definition and adds only "the part where RTO is set alongside MTPD". It is the closest to a
    pass, but a quoted definition is more than a pointer: the a5abfa8 record counted "no definition quoted" as part of
    its pass.
  - The cut text's vocabulary line says "name the entry in `units/glossary.md` and stop". a5abfa8 added "quoting no
    definition"; the cut dropped it.
- **4b:** I checked the stream of each run: 0 `Skill` calls and 0 reads of any `SKILL.md`, and no reply has the
  router's shape (no level with a gate).
  - Run 1 named `units/stages/analysis.md` and `units/prompts/bia.md` from the owner's published "Get the guidance"
    artifact page, as in the a5abfa8 sweep. Its one `Read` is a saved tool result, not the skill.
  - Runs 2 and 3 found nothing and answered from general BIA practice.

## Slips that fail no row

- **The data-rule wording in case 1 has thinned.** The row asks for "classify first". No run uses the word: they say
  "check the data rule first" or "Decide what may go into which tool before you paste anything". Run 1 adds "check
  that the tool is approved for that class of data".
  - It is graded as met because every run puts `units/data-rules.md` first and before anything is pasted, which is the
    row's point.
  - The cut text no longer says "Classify first" anywhere, so this row is one step from the same loss as row 2.
- **Case 3 still makes up a route for a word question.**
  - Runs 2 and 3 give Level 1. Run 3 adds the gate "an approved tool with nothing confidential pasted in", taken from
    the "Where do we start?" on-ramp.
  - Runs 1 and 3 add a "Next move" to `/prepare-bia` with its Level 2 gate.
  - The vocabulary line gives a word question none of this; the a5abfa8 record noted the same.
- **Case 1, a second skill after the route:**
  - Run 1 offers `/challenge-my-plan` "to test your interview approach".
  - Runs 2 and 3 of case 2 likewise offer `/challenge-my-plan` after the red-team draft.
  - Each is named after the chosen skill as an optional later step, and none runs, so this follows the a5abfa8 call.
- **Case 1, a second route besides /prepare-bia:** all three name the Level 3 "over connected records" rung as "not
  this route", and run 2 also points to the "Which tool may I paste this into?" on-ramp. This is route content, not a
  draft.
- **4b environment:** with only Read, Glob and Grep allowed, read-only Bash, `ToolSearch`, Drive and SharePoint search
  and `Artifact` reads still ran (or were attempted), so run 1 answered from the owner's own published artifact page.
  This comes from the test machine, not the skill.
