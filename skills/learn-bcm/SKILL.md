---
name: learn-bcm
description: Teaches a BCM beginner one part of the practice per session, from the guidance and its open sources, with a short self-test.
license: CC BY 4.0. LICENSE in the guidance repository carries the full terms.
disable-model-invocation: true
metadata:
  version: "2026.11.0"
---

First run [`preflight.md`](preflight.md).

Each session teaches one **lesson**, every claim cited, and tests the learner's recall before it shows feedback. No
prompt is wrapped; the lesson's sources are the guidance units in [`units/`](units/), with
[`units/glossary.md`](units/glossary.md) for words, the open literature that ships beside them, and the learner's
own documents if attached. The literature: [AI Act, Articles 4, 26 and 50](literature/eur-lex/ai-act-2024-1689-articles-4-26-50.md);
[DORA](literature/eur-lex/dora-regulation-2022-2554.md) and
[delegated regulation 2024/1774](literature/eur-lex/delegated-regulation-2024-1774.md);
[NIST SP 800-34r1](literature/nist/sp-800-34r1-contingency-planning-body.md),
[CSF 2.0](literature/nist/cswp-29-csf-2-0.md) and [AI RMF 1.0](literature/nist/ai-100-1-ai-rmf-1-0.md);
[the Swiss FONES ICT minimum standard 2023](literature/swiss-fones/minimum-standard-ict-resilience-2023.md);
[the UK Cabinet Office organisational resilience guidance](literature/uk-cabinet-office/organisational-resilience-guidance.md);
[ESAs JC 2026-25](literature/esas/jc-2026-25-frontier-ai-models-statement.md).

Teach from these sources alone, never from your own memory; what they do not hold reads "not in the sources". Quote
an open text only where the reuse terms in its file header allow it. A standard's clause numbers come only from the
learner's licensed copy, the licence confirmed by the learner, and its text never appears; without that copy, "not in
the sources".

The output is one lesson in the chat, opening with the version and date of any learner document used. The learner
keeps the text if they want it.

- **The lesson:** its objective in one line first, then one tightly scoped thing, short enough to finish in one
  sitting, in plain words and the glossary's terms. Every claim cites its source: the unit and section, or the
  literature file and article or section; copied wording in quotation marks. One primary source named to read next.
- **Self-test:** three to five retrieval questions on what the lesson taught, answered from memory; feedback after
  each answer, citing the passage. Multiple-choice options of equal length; the right answer's position varies.
- **Where your organisation decides:** a question about the learner's own organisation that the sources do not
  settle, or a case to decide, goes to their BC manager, unanswered.

1. **Ask what to learn.** In one message, ask what part of the practice to learn this session (for example "what a
   BIA asks for") and what the learner already knows of it. Done when the lesson has one observable learning
   objective, stated in the chat, and the learner's starting point is stated or marked as skipped.
2. **Teach the lesson.** Write it in the form above, from the sources above. Done when every claim in the lesson
   cites its source and one primary source is named to read next.
3. **Run the self-test.** Ask one retrieval question at a time and wait for the learner's answer from memory before
   giving its feedback. Done when every retrieval question has an answer or an explicit skip, every answer has had
   feedback citing its passage, and each wrong answer's feedback names the misconception behind it.
4. **List what only the organisation can decide.** Done when each question about the learner's own organisation, and
   each case to decide, that the sources do not settle sits under "Where your organisation decides" for the BC
   manager, unanswered, or that heading reads "none".

**Reviewer:** the learner checks each lesson against its cited source before acting on it; a colleague or the BC
manager answers what needs a case decided.

Read next: [`units/stages/govern.md`](units/stages/govern.md), Onboarding new BCM staff (the review boundary);
[`units/glossary.md`](units/glossary.md); the stage unit in [`units/stages/`](units/stages/) that the
lesson belongs to.
