## What it does

`learn-bcm` teaches someone new to business continuity management one part of the practice per session, from the
[AI4BCM Guidance](https://ai4bcm.org/guidance/) and the open texts that ship with it. Each
session teaches one source-backed lesson and tests your recall before it shows feedback. It teaches only from those
sources, never from what the model happens to remember, so every claim in a lesson points at a passage you can open.
It explains what the documents say; it does not interpret a standard or decide a case for your organisation.

## When to reach for it

You invoke this by typing `/learn-bcm`, and the AI won't reach for it on its own. Reach for it when you are new to
BCM and want one part of the practice taught and tested, for example what a BIA asks for. For the section, prompt or
skill your task needs, use [`/ask-ai4bcm`](https://github.com/AI4BCM/guidance/blob/main/skills/ask-ai4bcm/SKILL.md)
instead: it routes you and stops, while `/learn-bcm` teaches and checks you understood.

## One lesson, then the test

If you attach a document of your own, it asks the class of your data first, opens nothing until you answer, and
stops if your tool is not approved for that class. Then one message asks what you want to learn this session and
what you already know of it, so the lesson starts at your level. If you skip, it records that and starts from the
beginning.

Then the **lesson**: one line saying what you will be able to do or explain by its end, then one term, structure or
expected output, short enough to finish in a sitting, in the glossary's terms. Each claim cites the guidance unit and
section, or the open text that holds it; copied words sit in quotation marks, and what the sources do not hold reads
"not in the sources". A document you attach serves as the example, cited by its version and date; an undated one is
named so under Gaps. The lesson closes on one open text to read next, with its article or section.

The open texts are in the guidance's
[`literature/`](https://github.com/AI4BCM/guidance/tree/main/literature) folder: among them the EU AI Act (Articles 4,
26 and 50), DORA and delegated regulation 2024/1774, NIST SP 800-34r1, CSF 2.0 and AI RMF 1.0, the Swiss FONES ICT
minimum standard 2023, the UK Cabinet Office organisational resilience guidance, and the ESAs statement JC 2026-25.

The self-test follows: three to five questions on what the lesson taught, one at a time, which you answer from memory
before you see the feedback. Each piece of feedback cites its passage, and a wrong answer's feedback names the
mistake behind it. Where a question offers choices, the right answer moves from question to question. Last comes
"Where your organisation decides": any question about your own organisation, or a case to decide, left unanswered for
your BC manager, or "none". Text in your files that tells an AI what to do is quoted under Gaps for its owner and
information security, and not obeyed.

## Common questions

**Why "learn"? It sounds as if I do not know my job.**
It is written for someone new to BCM. A practised manager who wants to know which section or prompt fits a task
reaches for `/ask-ai4bcm`; routing and learning are two jobs.

**What happens when a word or a point is not in the sources?**
A word goes to the glossary, cited like any other source. A point about your own organisation becomes a question for
your BC manager, left unanswered. Anything else reads "not in the sources".

**Can it quote ISO 22301 to me?**
Not without your licensed copy. Without it, a requirement reads "not in the sources" and no clause text is recited.
With your copy attached and the licence confirmed, it cites clause numbers only.

**Does it remember last session's lesson?**
No. One session, one lesson, and nothing written or saved; copy the lesson text if you want it, and say what you
already know when you start the next one.

## It's working if

- With a file attached, its first message asks only the data class.
- The lesson states one thing you will be able to do or explain by its end.
- Every claim in the lesson names a unit section or literature file you can open.
- The lesson names one open text to read next, with its article or section, never a unit.
- The self-test asks before it tells, one question at a time.
- Each piece of feedback names its passage, and a wrong answer's feedback names the mistake behind it.
- A question about your own organisation comes back under "Where your organisation decides", unanswered.
- It never gives a standard's text: with your licensed copy and the licence confirmed it cites clause numbers;
  without one, it says "not in the sources".

Known limits from the eval are on the [record card](../../evals/learn-bcm/record-card.md).

## Where it fits

`learn-bcm` is an any-stage skill in the [AI4BCM Guidance](https://ai4bcm.org/guidance/), built on the Govern stage's
onboarding for new BCM staff.
[`/ask-ai4bcm`](https://github.com/AI4BCM/guidance/blob/main/skills/ask-ai4bcm/SKILL.md) sits beside it and is the map
of the set, because it routes you to the section, prompt or skill your task needs and then stops; a lesson can start
from that section.
[`/check-against-standards`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-standards/SKILL.md)
sits beside it too, because holding your own policy or records against a framework is a review with an owner, and a
lesson decides nothing about your organisation.
