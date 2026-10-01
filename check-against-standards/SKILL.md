---
name: check-against-standards
description: Reviews a policy against the frameworks you select, or your BCMS records against your own evidence checklist, and lists the gaps as questions for their owner.
license: CC BY 4.0. LICENSE in the guidance repository carries the full terms.
disable-model-invocation: true
metadata:
  version: "2026.11.0"
---

First run [`../preflight.md`](../preflight.md).

Hold the reader's material against a reference and hand each **gap** back as a question to the person who owns it;
whether the organisation meets a standard stays a person's call, made against the source text. The input decides the
branch. A policy, charter or scope statement is held against the frameworks the reader selects, with the Govern stage
prompt in [`../units/stages/govern.md`](../units/stages/govern.md), Prompts. BCMS records are sorted against the
reader's own evidence checklist with [`../units/stages/validate.md`](../units/stages/validate.md), Prompts,
**Task choice 3**.

The frameworks a reader selects from ship with the skill; each file's header gives its source, retrieval date and
reuse terms:

- [AI Act, Articles 4, 26 and 50 only](../literature/eur-lex/ai-act-2024-1689-articles-4-26-50.md)
- [DORA](../literature/eur-lex/dora-regulation-2022-2554.md)
- [Delegated regulation 2024/1774](../literature/eur-lex/delegated-regulation-2024-1774.md)
- [NIST SP 800-34r1, chapters 1 to 5](../literature/nist/sp-800-34r1-contingency-planning-body.md)
- [NIST CSF 2.0](../literature/nist/cswp-29-csf-2-0.md)
- [NIST AI RMF 1.0](../literature/nist/ai-100-1-ai-rmf-1-0.md)
- [Swiss FONES ICT minimum standard 2023](../literature/swiss-fones/minimum-standard-ict-resilience-2023.md)
- [UK Cabinet Office organisational resilience guidance](../literature/uk-cabinet-office/organisational-resilience-guidance.md)
- [ESAs JC 2026-25 statement on frontier AI models](../literature/esas/jc-2026-25-frontier-ai-models-statement.md)

A licensed standard counts only as the reader's own copy, the licence confirmed by the reader, and only for its clause
numbers.

The branch's prompt sets every finding's form. This skill adds three things: you give no verdict on the reader's
document or records (that it complies with, meets or conforms to a framework, or is ready, compliant or approved),
and a quoted status, record or instruction keeps its own words; on the records branch each gap is a question for the
reviewer below, no other owner inferred; and a clause appears by its number alone, even from the reader's licensed
copy.

1. **Tell the input apart and ask its intake.** A policy, charter or scope statement takes the policy input: ask which
   document (status and date), which frameworks from the list above or a licensed copy (licence confirmed), and which
   parts are in scope, only where the attachments leave it open. A checklist with BCMS records takes the records
   input: the Intake line of the validate stage prompt, unchanged. Done when the input is named and, for a policy, the
   selected frameworks are known; for records, every checklist row carries the organisation's own words for its
   expected evidence or sits under Gaps.
2. **Find the gaps with the branch's prompt**, whose Output sets the form of each finding: for a policy the Govern
   stage prompt, one block per selected framework; for records Task choice 3, one row per checklist entry. Done when
   every in-scope provision of each selected framework, or every checklist row, has a cited counterpart, a gap, or an
   explicit unresolved status under Gaps; every point no selected text holds carries the label "general practice,
   not in the sources"; and each point on a regulation carries its own mark for legal or compliance review.
3. **Hand each gap to its owner.** Reconcile coverage against the scope set in step 1, then turn each gap into a
   question: for the policy owner on a policy; for records, for the reviewer below, who decides what is enough. Done
   when every framework and part in scope from step 1 has its block, or every checklist row its row; only selected
   frameworks contribute findings and the others appear solely as not reviewed; and every gap and contradiction ends
   as a question addressed to that role.

**Reviewer:** the policy owner answers each question; legal or compliance answers the marked ones; a statement that
the document meets a framework is a person's, against the source text. Records: the internal auditor or the BCM
manager preparing for audit decides whether what is held is enough and whether anything goes into the audit note; the
audit owner clears any audit finding before it leaves the approved environment.

Read next: [`../units/stages/govern.md`](../units/stages/govern.md), Minimum controls and Method step 4 (legal,
compliance, information security and document owners before approval);
[`../units/stages/validate.md`](../units/stages/validate.md), Minimum controls, for records.
