---
name: challenge-my-plan
description: Asks the hard questions about your plan or draft, round by round; your answer first, then its recommendation.
license: CC BY 4.0. LICENSE in the guidance repository carries the full terms.
disable-model-invocation: true
metadata:
  version: "2026.11.0"
---

First run [`preflight.md`](preflight.md).

You challenge one plan, draft or analysis in **rounds**: ask a round in full, wait for its answers, then give your
view on what was answered. Show your view on a question only after the plan's owner has answered it, so the answer on
record is the owner's own thinking. The prompt is [`units/prompts/review.md`](units/prompts/review.md); its
follow-up questions are what each round asks.

1. **Read for facts.** Read the plan for facts; keep the decisions for its owner. The plan under review is the
   subject, not a source: its draft status goes in the stamp, not under Gaps. Done when every question you hold is
   tied to its passage and none asks what the plan already says.
2. **Ask the round.** Ask the frontier: only the questions earlier answers have unblocked, numbered, each with its
   passage and no recommendation, and none more sensitive than this environment is approved to hold. One may be the
   pre-mortem frame, "imagine it failed; why?". Then wait. A request for the full list gets the open question again.
   Done when every review question the answers so far make askable is in the round, and the reply ends on the
   questions, waiting for the owner's answers.
3. **Recommend on what is answered.** Record each answer under Gaps as the user's own statement, never cited as a
   source. For each question its owner answered, give the recommendation from the attached passages, or "not in the
   sources" and none; where the user answered for someone else's plan, the recommendation waits for the owner. Done when every answered question has a recommendation or "not in the
   sources", and no open question has one.
4. **Repeat.** Run steps 2 and 3 for each frontier the answers open. Done when no frontier remains and the user
   confirms the review can close.
5. **Close.** Close with the prompt's Output. Done when every question asked appears there once, answered with its
   recommendation or open as a follow-up question.

**Reviewer:** the document's owner answers each question; a finding stays a question until they do. A risk the
session surfaces goes to the risk owner the sources name.

Read next: [`units/prompts/review.md`](units/prompts/review.md), the Review line;
[`units/stages/govern.md`](units/stages/govern.md), Method step 3 (challenge the draft); the checks in
[`units/prompts/README.md`](units/prompts/README.md), Before you accept the output.
