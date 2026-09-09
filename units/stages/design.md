<!-- meta: unit=stages/design pp=4 version=2026.09 cites=5.1,5.2,5.4,5.5,5.6 -->
# Continuity Strategies and Solutions Design

## Situation

Design is where analysis becomes spending. The work is comparison: what the BIA requires against what the organisation can currently do, and which option is worth its money, its complexity and its trade-off.

AI is useful here for two things that are hard to do by hand — holding many registers in view at once, and attacking an option that everyone in the room already likes. It does not decide. Investment, priority and risk acceptance are business decisions, taken with stakeholders and approved through governance.

## Typical AI uses

- gap analysis between required recovery outcomes and current capability
- generating a long-list of strategy options by resource type
- comparing shortlisted options against internal constraints
- naming shared dependencies and single points of failure across sites
- drafting the structure of an option paper or business case
- controlled scanning for new service models, for human review

## Minimum controls

The one control that matters: **an option produced by AI is advisory until a named owner confirms it is workable here.** Plausibility is not feasibility.

- Internal design, architecture, cost and supplier detail is handled in approved environments only. Generic brainstorming may happen elsewhere, with no internal detail disclosed.
- Financial and commercial assumptions are checked by finance or procurement. AI does not justify an investment on its own authority.
- Assumptions, dependencies and residual risks stay visible in the paper instead of being smoothed out of it.

## Method

1. Start from the gap: required outcome against current arrangement, with the source and date of each.
2. Generate broadly and generically — people, premises, technology, suppliers, logistics, records, manual workarounds.
3. Move the shortlist into the approved environment before the analysis needs real constraints.
4. Red-team it. Ask what assumptions would have to be true for this option to fail, and which dependency the option quietly shares with the thing it is meant to protect.
5. Put the paper to the full stakeholder group — business owners, IT, facilities, procurement, finance, HR, risk — and let them own the choice.

## Prompts

```
Role: you are a BCM analyst reviewing continuity strategy options.
Task: compare the two attached dependency registers and identify where both sites depend on the same supplier, system or route.
Sources: use only the attached registers and supplier records. Do not add suppliers or capabilities from general knowledge.
Output: a table of shared dependencies, then the options each shared dependency rules out.
Gaps: state which entries are undated or unconfirmed, and what would settle them.
Cite: name the register and entry behind each shared dependency.
```

## Case example

**Prompt.** From both dependency registers: where do the two sites depend on the same supplier?

**Response.** Three shared suppliers. Refrigerated transport is the sharpest: one shipping company serves both sites and no second one is recorded anywhere. The existing site's plan names the acquired site's carrier as its backup — the same company under a different name.

**What changed.** A single point of failure across both sites was identified and procurement began contracting a second carrier. It surfaced only because both registers were in one place; neither register alone contained the finding.

## Level

Level 3, Connected and governed use. Comparing registers means retrieval across approved repositories with role-based access and a documented use case, so the comparison can be repeated when either register changes. Below that, the same question is answered from whatever someone happened to paste in.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
