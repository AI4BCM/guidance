<!-- meta: unit=tools version=2026.09 cites=annex-a1,annex-a2,annex-a3,annex-a4,annex-d1,1.3,2.3,3.3,4.3,5.3,6.3,7.3 -->
# Tools

No vendor names, deliberately. Products, licence terms and retention settings change faster than this guidance does; the category and the deployment tier stay useful. This unit is the one place that pairs a BCM task with a capability and an environment, and the one place that lists what a tool is checked against before it is approved. The stage units point here rather than repeating it.

## Categories

- **Generative AI assistants** — drafting, summarising, comparing, rewriting.
- **Retrieval-based search and knowledge tools** — answers grounded in approved repositories: BCMS artefacts, plan consistency checks, staff questions.
- **Analytical AI and machine learning** — dependency mapping, clustering exercise issues, trend and concentration analysis.
- **Meeting capture and transcription** — BIA interviews, debriefs, actions.
- **Workflow and automation** — triggers, routing, approvals: review reminders, change-triggered plan review, evidence pack assembly.
- **BI and reporting with AI features** — narrative from BCMS data for management review.
- **BCM and resilience platforms with AI features** — structured records, plans, exercises, action tracking.
- **External risk intelligence** — horizon scanning and supply chain monitoring.
- **Collaboration and learning content tools with AI features** — structured review, workshop design, awareness and training material.
- **Incident notification and communication tools** — staff notification, escalation routing and communications drafts; sending stays supervised.
- **Private or controlled model hosting** — governed access inside your own environment.

## Deployment tiers

| Tier | Suitability for BCM | Main caution |
|---|---|---|
| Free public service | Generic brainstorming only, no confidential content | Never for BCM data, internal records, incident or licensed material |
| Individual paid service | Low-risk individual productivity, if formally approved | Better features do not mean acceptable privacy, governance or licensing |
| Team or business subscription | Basic internal use if approved and governed | Due diligence on access control, retention, administration, contract |
| Enterprise or corporate licence | Often appropriate for live BCM work | Depends on configuration, retention, identity integration, connector control and the contract terms; the licence covers the platform, never the material you upload |
| Private, self-hosted or on-premise | Highly sensitive or regulated use cases | Needs technical capability, governance maturity, operational support |

## Selection guide

Which capability fits the task, and where it may run. Sensitivity follows the classes in `data-rules.md`; the environment column names a tier and no vendor. Public tools appear in the first two rows only, for material that says nothing about your organisation; once internal detail enters, the work moves to the approved environment.

| Stage | Task | Sensitivity | Capability | Where it may run |
|---|---|---|---|---|
| any | Generic awareness ideas and fictional scenario ideas that disclose nothing about your organisation | low | generative assistant | any approved tool, nothing confidential entered |
| any | Public threat, regulatory and case-study research | low | search-enabled assistant, external risk intelligence | any approved tool for the public material; relevance is judged in the approved environment |
| Govern | Policy, charter and scope drafting and review; management reporting | medium to high | generative assistant, retrieval over the governance repository, BI and reporting | enterprise or private environment, approved sources |
| Govern | Learning BCM terms and methods as a newer practitioner | low to medium | retrieval-based assistant over approved governance material | approved tool; licensed standards text only where the licence permits |
| Embed | Awareness and induction drafting, tailored by audience | medium | generative assistant over approved policy and awareness content | enterprise environment, approved sources |
| Embed | Staff-facing assistant over BC material | medium | retrieval-based assistant with access controls | retrieval-based enterprise tool with access controls |
| Embed | Scheduled awareness drafts and manager reminders | medium | workflow and automation over the approved awareness content, generative assistant for the draft | approved platform with logging and a human publication gate |
| Embed | Anonymised survey and workshop feedback analysis | high | analytics over aggregated feedback | approved corporate environment only, under privacy and retention rules |
| Analyse | BIA and risk analysis, from activities and resource requirements to threat relevance | high | retrieval over approved BIA and BCMS content, analytics for shared suppliers and concentration, BCM platform | enterprise, private or purpose-built BCM platform only |
| Analyse, Validate | Interview, workshop and debrief capture | high | meeting capture and transcription | approved for internal use, under notice, consent and retention rules |
| Design | Solution options, gap analysis and supplier concentration | high | retrieval over registers and design sources, analytics for gap and concentration | enterprise, private or approved platform only |
| Implement | Plan drafting, consistency checks across the suite, action cards | medium to high | retrieval over the approved plan repository, generative assistant against the controlled template, BCM platform | enterprise or private environment |
| Implement | Change-triggered plan review, reminders, evidence pack assembly | medium to high | workflow and automation over approved connectors | approved platform with logging, gates, connector control |
| Implement | Retrieval and summarising during an incident; staff notification drafts | high | retrieval over plans and contacts, bounded incident-support workflow, notification tools | approved corporate environment only; sending stays supervised |
| Validate | Scenario, inject and debrief material; findings across exercises | high | generative assistant, retrieval over validation records, analytics for recurring findings | approved corporate environment only |
| Validate | Evidence-gap scan against a checklist; management review narrative | medium to high | retrieval over BCMS records, BI and reporting | approved corporate environment |

## Evaluating a tool

Before a tool is approved for a class of data, check:

- data retention and deletion settings, and whether the provider trains on your content
- contractual privacy and confidentiality terms
- contract and licence terms for what you upload, including your own licences for standards and copyrighted material
- identity and access management integration
- audit logging and reporting
- connector scope and permission controls
- data residency where relevant
- suitability for sensitive operational content
- support for role-based access
- fallback arrangements if the tool is unavailable, and an exit plan if the provider fails
- ability to restrict or govern source material
- compliance with internal AI policy and information classification rules

An enterprise label names a deployment tier. Permission to upload a licensed standard or a copyrighted publication comes from the licence you hold for it, and what the provider keeps comes from the contract, so both are read before the label counts for anything. Record the answers with the approval; self-check question 1 in `levels.md` asks whether the team knows them. The list restates the source document's Annex A4 and agrees with the due-diligence and contract requirements in ETSI EN 304 223 (2025, provisions 5.1.2-7 and 5.2.2-6), the four data-handling questions in the UK Government AI Playbook (2025, "Working with your organisational data"), the supply-chain and failover practice in the NCSC and CISA guidelines (2023, "Secure your supply chain") and the third-party inventory with termination plans in the SEI model (2026, section 4.11.2), with the full entries in `references.md`.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
