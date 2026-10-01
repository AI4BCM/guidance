## What it does

`check-against-standards` holds your policy against the frameworks you pick, or your BCMS records against your own
evidence checklist, and hands each gap back as a question to the person who owns it. It lists what is missing and
fills nothing in; whether you meet a standard stays a person's call, made against the source text.

## When to reach for it

You invoke this by typing `/check-against-standards`, and the AI won't reach for it on its own. Reach for it before a
policy goes to approval, or before an audit, when you want to know what is missing.

| You have | Reach for |
| --- | --- |
| A policy, charter or scope statement, and frameworks to hold it against | `/check-against-standards`, policy input |
| Your evidence checklist (clause numbers, your words) and your BCMS records | `/check-against-standards`, records input |
| A plan or a planned change to compare with the approved BIA | [`/check-against-bia`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-bia/SKILL.md) |
| A plan or draft you want pressed with hard questions, round by round | [`/challenge-my-plan`](https://github.com/AI4BCM/guidance/blob/main/skills/challenge-my-plan/SKILL.md) |

## Every gap goes to its owner

The attachment decides the input. With a policy, charter or scope statement, it asks at most three questions the
document leaves open: which version and status, which frameworks, and which parts are in scope. The frameworks ship
with the skill, in the guidance's [`literature/`](https://github.com/AI4BCM/guidance/tree/main/literature) folder:
the EU AI Act (Articles 4, 26 and 50), DORA, delegated regulation 2024/1774, NIST SP 800-34r1, CSF 2.0 and AI RMF
1.0, the Swiss FONES ICT minimum standard 2023, the UK Cabinet Office organisational resilience guidance and the ESAs
statement JC 2026-25. You may add your own licensed copy of a standard, once you confirm the licence allows it; the
skill then cites its clause numbers and nothing more.

For each framework you pick, you get a block of its own: the **gaps** (a framework passage your document has no
counterpart for), the **contradictions** (both passages quoted), and any point no selected text holds, asked as a
question labelled "general practice, not in the sources". Every question on the AI Act, DORA, 2024/1774 or the ESAs
statement is marked for legal or compliance review.

With your evidence checklist and your records, it builds one row per clause number on the checklist. Each row
splits what "a document says" from what "a record shows", because a procedure that describes an exercise is no proof
the exercise took place. Each entry carries its document, section and date; a clause your files do not cover reads
"nothing found in the files", and each such **gap** becomes a question for the internal auditor or the BCM manager.
A checklist row without your own words for the evidence you expect goes under Gaps instead of being filled in from
the model's memory of the standard.

## Common questions

**What do I hold for clause 8.4?**
Attach your checklist and your BCMS records. The 8.4 row shows what a document says and what a record shows, each
with document, section and date, or "nothing found in the files". It answers from your files only, never from the
model's memory of the standard.

**Do I need my own copy of the standard?**
For records, no: your checklist and your records are enough. For a policy, only to cite its clauses by number;
otherwise pick from the open frameworks that ship with the skill. It never gives a standard's text: with your
licensed copy it cites clause numbers only; without one, a question about a standard's content gets "not in the
sources".

**The output says "approved". Is that its verdict?**
No. The word is quoted: your document's own status in the version stamp, a record, or an instruction found in a
file. In its own words the skill gives no verdict, score or percentage.

**Why are policy review and audit evidence one skill?**
Both hold what you have against a reference and list the gaps as questions; the input you attach decides which way
it runs.

## It's working if

- The version and date of your document and of each framework file, or of your checklist, sit at the top.
- Every question names the passage it rests on, and the framework file and article or the clause number.
- A framework you did not pick appears only in the list of frameworks not reviewed.
- Every DORA, AI Act and ESAs point is marked for legal or compliance review.
- A checklist row your files do not cover reads "nothing found in the files".
- Nowhere does it say in its own words that you comply, meet a standard or are ready.

## Where it fits

`check-against-standards` is the Govern stage skill in the [AI4BCM Guidance](https://ai4bcm.org/guidance/); its
records input also serves audit preparation in Validate.
[`/challenge-my-plan`](https://github.com/AI4BCM/guidance/blob/main/skills/challenge-my-plan/SKILL.md) sits beside
it, because a draft you want pressed with questions round by round goes there, where this skill holds it against a
framework. [`/check-against-bia`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-bia/SKILL.md)
sits beside it too, because a plan or a planned change is held against the approved BIA there. When a question falls
outside this skill, [`/ask-ai4bcm`](https://github.com/AI4BCM/guidance/blob/main/skills/ask-ai4bcm/SKILL.md) routes
it to the skill or unit that covers it.
