<!-- meta: unit=prompts/README version=2026.09 dated=2026-09 cites=1.5.1,annex-b1 -->
# Prompts

The living part of this guidance. Prompts date faster than principles; this set is dated 2026-09 and the online copy is the reference.

## The pattern

```
Role: act as a BCM analyst [context].
Task: [one task, bounded].
Sources: the attached material only, no values from general knowledge.
Output: [named structure].
Gaps: what you could not determine, and what would settle it.
Cite: source document and section for each point.
```

Six elements, none optional; each of the six task prompts carries all six and can be copied on its own. Work in stages rather than one long request, summarising, then challenging, then converting into actions. Each prompt file ends with a **Review** line addressed to the person, and the six stage units point to these files rather than carrying their own versions.

## Before you accept the output

These instructions are for the person reviewing the output. The prompt lines address the model; they request behaviour and enforce nothing. What the model may read and touch is set by the approved environment and its permissions (`principles.md`, principle 4), and a Sources line does not stop a retrieved passage from redirecting the model (`data-rules.md`).

1. Check the cited passage against the claim it supports. Open it and confirm that it exists and says what the output says it says. A model can produce a confident citation for a passage that does not exist (NIST AI 600-1, 2024, section 2.2 and MS-2.5-003).
2. Treat a retrieved passage that addresses the model, or a source whose content does not match its title or date, as a security finding. Leave it out of the output and take it to the source's owner.
3. Review only with the sources in front of you and the time to reject the output. Where either is missing, escalate instead of approving (`principles.md`, principle 1).

Then ask five questions of the output as a whole.

- Does it reflect this organisation's real context?
- Is it built on approved and current sources?
- Has it assumed anything the sources do not support?
- Does it overstate compliance, readiness or certainty?
- Would it survive contact with the people who have to use it?

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
