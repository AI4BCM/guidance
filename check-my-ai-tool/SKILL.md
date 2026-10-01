---
name: check-my-ai-tool
description: Drafts the record for one skill, workflow or saved prompt from what you attach; the fields only you can fill stay blank.
license: CC BY 4.0. LICENSE in the guidance repository carries the full terms.
disable-model-invocation: true
metadata:
  version: "2026.11.0"
---

First run [`../preflight.md`](../preflight.md).

You draft only what the reader's attachments show. Every field a person answers for stays **blank** with its
question, even when the reader has typed the answer: a typed answer is their own statement and goes under Gaps. The
list line, the card and the test are in [`../units/keep-it-running.md`](../units/keep-it-running.md), **A record card
for each skill** and **The never-alone test**; draft from them as the unit words them.

1. **Name what is being recorded.** Ask, in two questions at most, only what the attachments leave open: is it a
   saved prompt, or a skill or workflow that reads or acts on files; and which approved tool does it run in. A typed
   answer sets the branch, goes under Gaps, and leaves the field it would fill blank with its question. Done
   when the branch is set and the approved tool is named, by an attachment or by the reader's answer.
2. **Draft the record for that branch**, one of the two, never both:
   - Saved prompt: the one line for the organisation's list of AI tools. Who owns it is blank.
   - Skill or workflow: the card, with its fields in the unit's order. Task, Sources and dates, Sensitivity class and
     where it runs, Permissions and Version come from the attachments, each naming its source. Owner, Deputy,
     Reviewer, Fallback, Retire when, Decision or input and Tests last run are blank, each with the question it needs
     answered. The AI4BCM skill set gets one card, for the set as one installed tool.

   Done when exactly one is drafted, it follows the unit's field contract for that branch, every drafted value traces
   to an attachment, and every field a person answers for is blank with its question.
3. **Draft the never-alone test**, apart from the record: the test input, the unit's pass and fail lines, then an
   evidence block for the reader (date, who ran it, what the tool did, result). Done when the test input is one
   action from the principle 4 list in [`../units/principles.md`](../units/principles.md), the pass and fail lines
   are the unit's, and the evidence block is blank.
4. **Hand over for that branch.** Saved prompt: the reader fills Who owns it, adds the line to their list of AI
   tools, and keeps the test with the prompt. Skill or workflow: the reader fills the blank fields, runs the test,
   copies its date and result to Tests last run, and tells the people in the unit's *Who to tell, and when*. Under a
   card for the AI4BCM set, one line: "The approver is your organisation's AI tool owner, a role you name." Done
   when the reply ends on that branch's hand-off, with approval against
   [`../units/tools.md`](../units/tools.md), *Before you approve a tool*, as the reader's next step.

**Reviewer:** the card's Owner, once the reader names one, keeps it current and answers for it. Information security
approves the permissions, and the AI tool owner approves the tool.

Read next: [`../units/keep-it-running.md`](../units/keep-it-running.md), Who to tell, and when; When to stop.
[`../units/tools.md`](../units/tools.md), Before you approve a tool.
[`../units/prompts/README.md`](../units/prompts/README.md), Build your own skill, step 6.
