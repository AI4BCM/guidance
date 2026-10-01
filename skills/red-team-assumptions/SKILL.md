---
name: red-team-assumptions
description: Lists what the strategy silently relies on, and the check that would settle each.
license: CC BY 4.0. LICENSE in the guidance repository carries the full terms.
disable-model-invocation: true
metadata:
  version: "2026.11.0"
---

First run [`preflight.md`](preflight.md).

You list only what the option needs to be true. Each **load-bearing** assumption ends on the check that would settle
it and a question for the person who can run that check, and you score nothing. The prompt is
[`units/stages/design.md`](units/stages/design.md), Prompts, **Task choice 2**, with
[`units/prompts/review.md`](units/prompts/review.md) as its check.

1. **Ask the scope.** Ask the prompt's Intake questions, only those the attachments leave open, and wait. Done when
   every scope question is answered or recorded as skipped, or the attachments answered them all and none was asked.
2. **Steelman, then test.** Steelman the paper (a draft paper is listed under Gaps with its status, as the prompt's
   Gaps line says, and is still the paper being read), then test each claim the option rests on: it is load-bearing
   if an option outcome fails when the claim is false. Keep those as assumptions, each with its passage; the rest go
   to what holds up. Done when every claim the option rests on is either under what holds up or a retained
   assumption that names the option outcome that fails if it is false.
3. **Send the whole list.** Send it in one reply, in the prompt's Output, which sets the check and its owner, the
   supplier fields, the order and the finance-or-procurement mark. Done when every retained assumption and every
   supplier the option needs is in this one reply, and the reply asks the user nothing further.

**Reviewer:** the BCM manager who owns the option paper checks each assumption against its passage; each check's
owner answers it; finance or procurement checks financial and commercial assumptions; the stakeholder group owns the
choice.

Read next: [`units/stages/design.md`](units/stages/design.md), Method step 4 and Minimum controls; Level 3, in
its Level section.
