---
name: ask-ai4bcm
description: Names the section, prompt, level, gate and data rule for your task, then stops.
license: CC BY 4.0. LICENSE in the guidance repository carries the full terms.
disable-model-invocation: true
metadata:
  version: "2026.11.0"
---

# Ask AI4BCM

You don't remember fifteen units and ten skills, so ask.

This routes, then stops. Every answer names the **skill** or prompt to run, the unit to read, the **maturity level**
the work needs, the **gate** that level turns on, the effort, and the data rule, which runs first. It never runs a
skill or a prompt: a skill starts only when the reader types its name. Unit links resolve in a clone or a plugin
install; otherwise read `units/` at github.com/AI4BCM/guidance.

## The main flow: the six lifecycle stages

1. **Govern**: scope, roles, policy. [`../units/stages/govern.md`](../units/stages/govern.md) + [`../units/prompts/draft.md`](../units/prompts/draft.md). Skill: **`/check-against-standards`** for a draft policy or BCMS records; management reporting runs [`../units/prompts/management-report.md`](../units/prompts/management-report.md). Level 2; gate: a saved prompt, approved tools, a written data rule. Forty minutes for the draft. Data: [`../units/data-rules.md`](../units/data-rules.md).
2. **Embed**: staff knowing what to do. [`../units/stages/embed.md`](../units/stages/embed.md) + [`../units/prompts/awareness.md`](../units/prompts/awareness.md). Skill: **`/role-card`**, one approved document for one audience. Level 2; gate: a fixed content base, a saved prompt, a named reviewer. Forty minutes. Data: [`../units/data-rules.md`](../units/data-rules.md).
3. **Analysis**: what an activity needs, what a disruption costs. [`../units/stages/analysis.md`](../units/stages/analysis.md); workflow in [`../units/workflow-design.md`](../units/workflow-design.md). Most readers start on the lower rung. Data: the most sensitive material in BCM, [`../units/data-rules.md`](../units/data-rules.md).
   - **Before the interview, no connector.** Skill: **`/prepare-bia`** ([`../units/prompts/bia.md`](../units/prompts/bia.md), Task choice 1, recovery fields blank). Level 2, Repeatable; gate: a saved prompt, approved tools, a written data rule, a named reviewer. Forty minutes per activity. Afterwards the AI4BCM BIA-Workflow takes the record to a signed BIA.
   - **Over connected records.** Level 3; gate: all five self-check questions in [`../units/levels.md`](../units/levels.md) answer yes with evidence. An afternoon.
4. **Design**: choosing continuity solutions. [`../units/stages/design.md`](../units/stages/design.md) + [`../units/prompts/review.md`](../units/prompts/review.md). Skill: **`/red-team-assumptions`** on the option everyone already likes. Level 3; gate: retrieval across both registers with role-based access. An afternoon. Data: [`../units/data-rules.md`](../units/data-rules.md).
5. **Implement**: writing and maintaining plans. [`../units/stages/implement.md`](../units/stages/implement.md) + [`../units/prompts/review.md`](../units/prompts/review.md). Skill: **`/check-against-bia`** for a plan or a coming change. Level 3; gate: auditable retrieval over the approved plans. Forty minutes. Data: [`../units/data-rules.md`](../units/data-rules.md).
6. **Validate**: exercising and reviewing. [`../units/stages/validate.md`](../units/stages/validate.md) + [`../units/prompts/exercise.md`](../units/prompts/exercise.md). Skill: **`/debrief-to-action`** for one exercise's notes. Level 3; gate: retrieval over the controlled validation record. An afternoon. Data: debriefs name people, [`../units/data-rules.md`](../units/data-rules.md).

## On-ramps

- **"I inherited forty BIAs and no requirements register."** Stage 3 with **`/prepare-bia`** per interview: [`../units/stages/analysis.md`](../units/stages/analysis.md) + [`../units/prompts/bia.md`](../units/prompts/bia.md). Level 2; gate: approved tools, a written data rule, a named reviewer. An afternoon per site. Data: [`../units/data-rules.md`](../units/data-rules.md).
- **"My board wants a one-page AI policy for BCM."** [`../units/principles.md`](../units/principles.md) (handout: [`../units/principles-a4.html`](../units/principles-a4.html)), adopted through your own route with [`../units/prompts/draft.md`](../units/prompts/draft.md); **`/check-against-standards`** holds the draft against your frameworks. Level 2; gate: fixed sources, a named reviewer. Forty minutes. Data: [`../units/data-rules.md`](../units/data-rules.md).
- **"Where do we start?"** [`../units/levels.md`](../units/levels.md), Where to start, by level. **No prompt file here**: the row you land on names it. Level 1 or 2; gate: an approved tool, nothing confidential in. Ten minutes. Data: [`../units/data-rules.md`](../units/data-rules.md).
- **"I have three years of exercise reports."** Stage 6: [`../units/stages/validate.md`](../units/stages/validate.md), its Prompts read-across, then [`../units/prompts/exercise.md`](../units/prompts/exercise.md). Level 3; gate: retrieval over the whole set. An afternoon. Data: [`../units/data-rules.md`](../units/data-rules.md).
- **"What do I hold for clause 8.4?"** **`/check-against-standards`** with your own evidence checklist and records. **No prompt file here**: the skill runs Task choice 3 in [`../units/stages/validate.md`](../units/stages/validate.md). Level 2; gate: the checklist in your own words, a named reviewer. An hour. Data: [`../units/data-rules.md`](../units/data-rules.md).
- **"We are acquiring a company."** The main flow from the top, not from analysis: [`../units/stages/govern.md`](../units/stages/govern.md) + [`../units/prompts/draft.md`](../units/prompts/draft.md). Level 2; gate: approved tools, a written data rule, a named reviewer. Weeks in all. Data: [`../units/data-rules.md`](../units/data-rules.md).
- **"Which tool may I paste this into?"** [`../units/data-rules.md`](../units/data-rules.md), then [`../units/tools.md`](../units/tools.md); the prompt pattern is [`../units/prompts/README.md`](../units/prompts/README.md). **No prompt needed**. Level 2; gate: the data rules are written down; until then the answer is "none yet". Ten minutes.
- **"Which type of tool fits, and may we approve it?"** [`../units/tools.md`](../units/tools.md), the selection guide and Before you approve a tool. Installing these skills is such an approval. **No prompt needed**. Level 2; gate: the answers recorded with the approval. An hour. Data: [`../units/data-rules.md`](../units/data-rules.md).
- **"We run this every month now. What do we keep?"** [`../units/keep-it-running.md`](../units/keep-it-running.md); **`/check-my-ai-tool`** drafts the record. **No prompt needed**. Level 2; gate: the card names an owner, a reviewer and a retire-when condition. An hour for the first card. Data: [`../units/data-rules.md`](../units/data-rules.md).
- **Your situation is not listed.** Name the stage the work belongs to and take that route from the main flow; if it spans two, take the earlier. That route names the rest, so this entry names none of its own. Not placeable at all: [`../units/principles.md`](../units/principles.md) says what the guidance covers.

## Skills

Ten skills, one job each. Each starts only when typed, returns a draft for a named reviewer and writes nothing. Six
are on the stages above; these four serve any stage.

- **`/challenge-my-plan`** asks the hard questions about a plan you own, round by round, and gives its view only after you answer.
- **`/red-team-assumptions`** returns, in one reply, what a paper silently relies on and the check for each. Challenge interviews you; red-team reads the paper and returns the whole list.
- **`/learn-bcm`** teaches one part of the practice per session, then tests you. This router names a section and stops; learn-bcm teaches.
- **`/check-my-ai-tool`** drafts the record for one skill, workflow or saved prompt. The AI4BCM skills share one card.

## Vocabulary underneath

For a word, not a process, name the entry in [`../units/glossary.md`](../units/glossary.md) and stop, quoting no definition; to learn it,
**`/learn-bcm`**. The level ladder and self-check are in [`../units/levels.md`](../units/levels.md); the source behind
every citation is in [`../units/references.md`](../units/references.md).

## After the draft

Every route ends at a draft. Name the next move: the owner the unit names decides; or another skill reads the draft,
which the reader types; or the work belongs to an earlier stage.

## Precondition

Classify first: [`../units/data-rules.md`](../units/data-rules.md) runs before any route. What is pasted into the wrong tool cannot be
unpasted.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
