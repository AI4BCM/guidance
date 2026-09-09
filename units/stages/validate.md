<!-- meta: unit=stages/validate pp=6 version=2026.09 cites=7.1,7.2,7.4,7.5,7.6 -->
# Validation, Exercising, Review and Improvement

## Situation

Validation produces more evidence than anyone reads. Exercise reports, debrief notes, audit observations and post-incident material accumulate, and the finding that matters is usually the one that appears in three of them.

That is where AI earns its place here: after the event, turning volume into a pattern; before it, producing variation so the fourth exercise is not the third one again. It does not replace the exercise director, facilitator or auditor. And the material is sensitive — debriefs and incident records name people and weaknesses, so they stay in approved environments.

## Typical AI uses

- generating scenarios, timed injects and facilitator notes to a stated objective
- drafting role-play messages from regulators, customers, suppliers or media
- transcribing and structuring debriefs into strengths, weaknesses, actions and open questions
- clustering lessons and comparing findings across exercises and incidents
- scanning BCMS material against a checklist for possible evidence gaps
- turning validation metrics and action progress into a management review narrative

## Minimum controls

The one control that matters: **AI proposes a theme; a person makes it a finding.** Nothing enters the exercise report, the lessons log or the audit note without the accountable reviewer deciding it belongs there.

- Scenarios are checked for plausibility and learning value before delivery. An unrealistic inject teaches the wrong lesson convincingly.
- Debrief records, transcripts and incident material are analysed in approved environments only, under notice, consent and retention rules.
- Improvement actions keep human owners and human closure. Progress reporting may be assisted; sign-off is not.

## Method

1. State what the activity is meant to test before asking for content. A scenario written without an objective will be entertaining and prove nothing.
2. Draft the package — scenario, injects, facilitator notes, debrief questions — and have the exercise director judge realism and proportion.
3. Capture the debrief with approved tools, and keep the raw record separate from the analysis.
4. Analyse across events, not only within one: what recurs is worth more than what was worst on the day.
5. Put the pattern to the people who were there before it becomes a finding, then track the action to a named owner.

## Prompts

```
Role: you are supporting a BCM professional planning an exercise programme.
Task: read the attached exercise reports and identify recurring findings, then recommend what to exercise first at a site with no exercise history.
Sources: use only the attached reports and the site profile. Do not assume findings from other organisations.
Output: recurring findings with the reports each appears in, then one recommended exercise with its objective.
Gaps: state which reports are missing from the set and what that leaves untested.
Cite: quote the finding text from each report.
```

## Case example

**Prompt.** Three years of exercise reports. What do we exercise first at the new site?

**Response.** One finding recurs across the last three exercises: the out-of-hours duty manager was not reached. Recommendation: a discussion-based exercise on the escalation route. The new site has no exercise history, so start simple.

**What changed.** The first exercise for the new site was scheduled against the organisation's own recurring finding. That finding had sat in the reports for three years; nobody had had time to read them all together.

## Level

Level 3, Connected and governed use. Comparing findings across years means retrieval over the controlled validation record with a documented use case, so the same comparison can be re-run after the next exercise and the conclusion can be traced to the reports behind it.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
