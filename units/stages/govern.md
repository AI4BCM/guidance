<!-- meta: unit=stages/govern version=2026.09 -->
# Establishing and Governing BCM

## Situation

Governance work is mostly writing: policy, scope, roles, management reporting. That makes it the stage where AI drafts fastest and where a fluent draft does most damage. A well-worded policy reads as agreed long before anyone agreed to it.

The line is fixed. AI may prepare and challenge governance material. It cannot set management intent, assign accountability, or declare a BCMS compliant. Those are decided through the organisation's own governance route, by people who can be held to them.

## Typical AI uses

- drafting policy, charter and scope statements from the approved framework
- reviewing governance documents for ambiguity, gaps and contradiction
- preparing implementation roadmaps and governance work plans
- turning BCMS metrics and open actions into a management report draft
- producing role and responsibility summaries for review
- summarising changes in official guidance or regulation for a person to interpret, on request or from a workflow that watches approved official sources
- helping a newer practitioner learn the BCMS's structure, vocabulary and expected outputs from approved governance material

The capability and environment for each use are in the selection guide in `tools.md`.

## Minimum controls

The one control that matters: **a claim of compliance or alignment is never accepted from a model.** Any statement that the organisation meets a standard, a regulation or its own policy is verified by a person against the source text.

- Final policy, scope and governance decisions stay with management. A draft enters the normal approval route with its status unchanged.
- Only approved tools touch internal governance content; licensed standards text only where the licence permits.
- An AI-supported artefact carries the same document control as any other: owner, version, review date.

## Method

1. Fix the approved sources and their dates: current policy, the framework, the organisation structure, prior management review output.
2. Ask for the draft with the output structure named, and require it to mark what the sources do not cover.
3. Ask the same model to attack the draft: which clauses are ambiguous, unenforceable, or open to two readings. The challenge prompt is worth more than the drafting prompt.
4. Take it to the people who will live with it — legal, compliance, information security, document owners — before it enters approval.
5. Approve and control it normally. Then review the use case: keep it only while it improves governance, not because it is fast.

## Learning the practice

A newer practitioner learns the BCMS faster from its own documents than from a generic explanation, and a bounded assistant over those documents is the lowest-risk use of AI in this stage. This is practitioner learning. Staff induction is the embedding stage's work and has its own method in `stages/embed.md`.

| | Learning the practice |
|---|---|
| Inputs | the approved policy, framework, scope statement, procedures and glossary, with their dates; licensed standards text only where the licence permits |
| Capability | the "Learning BCM terms and methods as a newer practitioner" row of the `tools.md` selection guide |
| Output | an explanation of a term, a structure or an expected output, tied to the document that defines it here and marked where the documents are silent |
| Review boundary | the practitioner or a colleague checks the explanation against the source before acting on it; the assistant explains what the documents say and does not interpret a standard or decide a case |

Where the documents are silent, the answer is a question for the BC manager, and the practitioner learns that too.

## Prompts

The drafting prompt is `prompts/draft.md`; the case below runs it with the policy, scope statement, steering group terms of reference and organisation chart attached and two action lists as the named structure. `prompts/review.md` is step 3 of the method, and `prompts/management-report.md` is the other governance prompt.

## Case example

**Prompt.** A new site has been acquired. What do we change, and what must the site comply with?

**Response.** The scope statement names four sites and not the fifth. No role exists for onboarding a site at all. At the acquired site: no BC coordinator, no seat on the steering group, no local plan owner. Four actions for the parent, nine for the site.

**What changed.** Onboarding actions exist for both sides and the work can start. The organisation had no onboarding checklist before — it had whoever did it last time.

## Level

Level 2, Team-level structured use. A repeatable prompt over a fixed set of attached governance documents needs agreed tools and a written data rule, not connectors. It reaches Level 3 when the same question runs against the live governance repository.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
