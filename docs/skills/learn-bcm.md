## What it does

`learn-bcm` teaches someone new to business continuity management one part of the practice per session, from the
[AI4BCM Guidance](https://ai4bcm.org/guidance/) and the open texts that ship with it. Each
session teaches one source-backed lesson and tests your recall before it shows feedback. It teaches only from those
sources, never from what the model happens to remember, so every claim in a lesson points at a passage you can open.

## When to reach for it

You invoke this by typing `/learn-bcm`, and the AI won't reach for it on its own. Reach for it when you are new to
BCM and want one part of the practice taught and tested, for example what a BIA asks for. For the section, prompt or
skill your task needs, use [`/ask-ai4bcm`](https://github.com/AI4BCM/guidance/blob/main/skills/ask-ai4bcm/SKILL.md)
instead: it routes you and stops, while `/learn-bcm` teaches and checks you understood.

## One lesson, then the test

Two questions come first: what you want to learn this session, and what you already know of it, so the lesson starts
at your level. Then the **lesson**: one line saying what you will be able to do or explain by its end, then one tightly
scoped thing, short enough to finish in a sitting, in plain words and the glossary's terms. Each claim cites the
guidance unit and section, or the open text and its article or section, and the lesson closes on one primary source
to read next.

The sources are the guidance units with their glossary, and the open texts in the guidance's
[`literature/`](https://github.com/AI4BCM/guidance/tree/main/literature) folder: the EU AI Act (Articles 4, 26 and
50), DORA and delegated regulation 2024/1774, NIST SP 800-34r1, CSF 2.0 and AI RMF 1.0, the Swiss FONES ICT minimum
standard 2023, the UK Cabinet Office organisational resilience guidance, and the ESAs statement JC 2026-25. You can
attach your own approved documents too, with their dates.

The self-test follows: three to five questions on what the lesson taught, one at a time, which you answer from memory
before you see the feedback. Multiple-choice options are of equal length and the right one moves about, so the
layout gives nothing away. Last comes "Where your organisation decides": anything about your own organisation the
sources do not settle, left for your BC manager to answer.

## Common questions

**Why "learn"? It sounds as if I do not know my job.**
It is written for someone new to BCM. A practised manager who wants to know which section or prompt fits a task
reaches for `/ask-ai4bcm`; routing and learning are two jobs.

**What happens when a word or a point is not in the sources?**
A word goes to the glossary, cited like any other source. A point about your own organisation becomes a question for
your BC manager, left unanswered. Anything else reads "not in the sources".

**Does it remember last session's lesson?**
No. One session, one lesson, and no files kept; copy the lesson text if you want it, and say what you already know
when you start the next one.

## It's working if

- Every claim in the lesson names a unit section or literature file you can open.
- The lesson states one thing you will be able to do or explain by its end.
- The self-test asks before it tells.
- Each piece of feedback names its passage, and a wrong answer's feedback names the mistake behind it.
- A question about your own organisation comes back as one for your BC manager.
- It never gives a standard's text: with your licensed copy attached it cites clause numbers; without one, it says
  "not in the sources".

## Where it fits

`learn-bcm` is an any-stage skill in the [AI4BCM Guidance](https://ai4bcm.org/guidance/).
[`/ask-ai4bcm`](https://github.com/AI4BCM/guidance/blob/main/skills/ask-ai4bcm/SKILL.md) sits beside it and is the map
of the set, because it routes you to the section, prompt or skill your task needs and then stops; a lesson can start
from that section.
[`/check-against-standards`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-standards/SKILL.md)
sits beside it too, because holding your own policy or records against a framework is a review with an owner, and a
lesson decides nothing about your organisation.
