# Saved prompt: supplier continuity summary

Saved prompt, kept in the BCM team's prompt folder. Version 1.1, 2 July 2026 (1.0, 14 April 2026: first version;
1.1: Gaps line added). Runs in: the organisation's approved enterprise chat assistant, AI tools list entry T-04,
approved for high-sensitivity data. Data used with it: supplier questionnaires and contract summaries,
class "high" (supplier weaknesses and contractual dependencies).

What it does: summarises one supplier's continuity questionnaire into a half-page note for the supplier review
meeting: recovery times the supplier states, single points of failure it admits, questions it left blank.

```
Role: BCM analyst preparing a supplier review note for the procurement lead, who decides what to raise with the supplier.
Task: summarise the attached continuity questionnaire of one supplier. Summarise only; rate nothing.
Sources: the attached questionnaire only.
Output: stated recovery times; admitted single points of failure; questions left blank.
Gaps: questions unanswered or answered "see contract". Where the questionnaire says nothing, write "not in the sources".
Cite: question number for each line, with the supplier's words in quotation marks.
```
