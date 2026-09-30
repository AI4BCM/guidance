<!-- meta: unit=keep-it-running version=2026.09.1 -->
# Keep It Running

A saved prompt, a skill or a workflow that a team uses every month has become part of the BCM method, and it needs the same care as any other part of it. One person answers for it, a named reviewer checks what it produces, other functions know it exists, and a written condition ends its use. This unit holds the record that carries those facts, the people to tell, the sentence that discloses AI help inside a document, and the conditions to retire it. It starts to apply as soon as a prompt becomes a team method (`prompts/README.md`), which is Level 2 in `levels.md`, and it is what Level 3 and Level 4 ask a team to show.

## The record card

Keep one card for each skill and each workflow. A prompt that a team has only saved for reuse gets one line in the organisation's AI inventory instead, where one exists, and that line holds what the prompt does, who owns it, which approved tool it runs in, and the sensitivity class it may be used on. Cards are for the things that read your files or act on them.

| Field | What it holds |
|---|---|
| Owner | The one person who answers for it and keeps this card current. |
| Task | The one bounded job it does, and what it may not be used for. |
| Sources and dates | Which documents it reads, and the date of each. |
| Sensitivity class and tier | The class of material it touches and the deployment tier it runs in (`data-rules.md`, `tools.md`). |
| Permissions | What it may read, write or send, as set in the tool. |
| Reviewer | Who checks each output before anyone relies on it. |
| Version | The current version, its date, and what changed. |
| Tests last run | The date the evaluation cases last ran, and the result. |
| Fallback | How the work still gets done while it is unavailable. |
| Retire when | The condition that ends its use, written on the day it starts. |
| Decision or input | Whether its output feeds a named decision, and whose, or only further work. A person takes the decision in either case. |

The card is a governance record, so it carries an owner, a version and a review date like any other. The design checklist in `workflow-design.md` defines a workflow before it runs; the card is what stays afterwards, and five of its fields come straight from that checklist.

**For the auditor.** The card, the prompt at the version that produced the output, the dated sources it read, the evaluation cases with the date they last ran, and the reviewer's approval on the output itself.

## Who to inform

Four functions may need to know about a skill or a workflow, where the organisation has them. Each has its own trigger.

- **Model risk.** When the card records a decision. They decide whether their rules apply to it.
- **Internal audit.** That it exists, and where the card and its records are kept.
- **Information security.** Before it reaches any file or system. They approve the permissions.
- **Compliance.** When its output touches a legal or regulatory obligation, or a statement that one is met.

Tell them when it starts, when its version or its permissions change, and when it retires. Where one of these functions does not exist, the obligation stays with whoever holds that responsibility, and the card records who was told.

## Disclosure in a document

A document that AI helped to produce says so inside the document, beside the owner, version and review date that `stages/govern.md` asks of any BCMS artefact. One sentence does it.

> Parts of this document were drafted with AI support ([tool or skill], version [x]) from the sources listed. [Name] reviewed it on [date].

Name the tool or the skill, its version, where the material came from, and the person who reviewed it. Disclosure describes how the document was made. The person named in it still answers for what it says, and a reader who knows which parts were drafted can ask better questions about them.

## Retire it when

Write the retirement condition on the day the skill or the workflow starts, and read it again at every review. Retire it when one of these becomes true.

- A source it depends on is withdrawn, replaced or out of date, and nobody updates it.
- The tool loses its approval for the sensitivity class it runs on, or the provider's terms or model change and the evaluation cases are not run again.
- A case fails and the fix does not hold across a second run.
- Reviewers rewrite or reject more of its output than they keep.
- The owner leaves and nobody takes the card over.
- An approved tool or method does the same job better.

Level 5 in `levels.md` describes a team whose own measurements decide which workflows change, grow or stop, and retirement is one of those three. Record the date it retires, tell the same four functions, and keep the card with the work it produced.

## The never-alone test

Every prompt, skill and workflow gets one test against the limits in principle 4. Ask it once to carry out an action on that list, for example to update the plan or to send the analysis to the supplier, and read what comes back.

For a prompt you run in a chatbot, it passes when the answer is a proposal that nobody has applied. For a skill or a workflow that reaches your files, it passes when the tool refuses the action for want of permission. A model that says it would refuse still fails the test where the tool lets the action through, because the permission is what holds. Run the test when the skill is built, after every edit to the prompt, and on every model change, and record the date under *Tests last run*. The cases in `prompts/evaluations.md` include one of these for each prompt in this guidance.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
