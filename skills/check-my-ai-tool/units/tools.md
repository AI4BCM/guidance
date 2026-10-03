<!-- meta: unit=tools version=2026.11 -->
# Tools

No vendor is named here, on purpose. Products, licence terms and retention settings change faster than this guidance does. The category and where the tool runs stay useful. This unit is the only place for tool choice and tool checks; the stage units point here.

## Categories

- **Generative AI assistants** — drafting, summarising, comparing, rewriting.
- **Retrieval-based search and knowledge tools** — answers based on approved repositories: BCMS documents, checks that plans agree, staff questions.
- **Analytical AI and machine learning** — dependency mapping, clustering exercise issues, trend and concentration analysis.
- **Meeting capture and transcription** — BIA interviews, debriefs, actions.
- **Workflow and automation** — triggers, routing, approvals: review reminders, plan review when something changes, evidence pack assembly.
- **BI and reporting with AI features** — narrative from BCMS data for management review.
- **BCM and resilience platforms with AI features** — structured records, plans, exercises, action tracking.
- **External risk intelligence** — horizon scanning and supply chain monitoring.
- **Collaboration and learning content tools with AI features** — structured review, workshop design, awareness and training material.
- **Incident notification and communication tools** — staff notification, escalation routing and communications drafts; sending stays supervised.
- **Private or controlled model hosting** — governed access inside your own environment.

## Selection guide

The table shows which type of tool fits each task and where it may run. The sensitivity column indicates whether the data is low, medium or high in sensitivity; `data-rules.md` lists what constitutes high sensitivity. The environment column indicates where the tool runs and does not name a vendor. Public tools only appear in the first two rows, for material that says nothing about your organisation. Once internal detail comes in, the work moves to the approved environment.

| Stage | Task | Sensitivity | Type of tool | Where it may run |
|---|---|---|---|---|
| any | Generic awareness ideas and fictional scenario ideas that share nothing about your organisation | low | generative assistant | any approved tool, nothing confidential entered |
| any | Public threat, regulatory and case-study research | low | search-enabled assistant, external risk intelligence | any approved tool for the public material; relevance is judged in the approved environment |
| Govern | Policy, charter and scope drafting and review; management reporting | medium to high | generative assistant, retrieval over the governance repository, BI and reporting | enterprise or private environment, approved sources |
| Govern | Learning BCM terms and methods as a newer practitioner | low to medium | retrieval-based assistant over approved governance material | approved tool; licensed standards text only where the licence allows |
| Embed | Awareness and onboarding drafting, adapted by audience | medium | generative assistant over approved policy and awareness content | enterprise environment, approved sources |
| Embed | Staff-facing assistant over BC material | medium | retrieval-based assistant with access controls | retrieval-based enterprise tool with access controls |
| Embed | Awareness reminders on a fixed calendar | medium | workflow and automation over the approved awareness content, generative assistant for the draft | approved platform with logging and a human publication gate |
| Embed | Anonymised survey and workshop feedback analysis | high | analytics over feedback, only as combined results | approved corporate environment only, under privacy and retention rules |
| Analyse | BIA and risk analysis, from activities and resource requirements to threat relevance | high | retrieval over approved BIA and BCMS content, analytics for shared suppliers and concentration, BCM platform | enterprise, private or purpose-built BCM platform only |
| Analyse, Validate | Interview, workshop and debrief capture | high | meeting capture and transcription | approved for internal use, under notice, consent and retention rules |
| Design | Solution options, gap analysis and supplier concentration | high | retrieval over registers and design sources, analytics for gap and concentration | enterprise, private or approved platform only |
| Implement | Plan drafting, checks that plans across the suite agree, action cards | medium to high | retrieval over the approved plan repository, generative assistant against the controlled template, BCM platform | enterprise or private environment |
| Implement | Plan review when something changes, reminders, evidence pack assembly | medium to high | workflow and automation over approved connectors | approved platform with logging, gates, connector control |
| Implement | Retrieval and summarising during an incident; staff notification drafts | high | retrieval over plans and contacts, narrow incident-support workflow, notification tools | approved corporate environment only; sending stays supervised |
| Validate | Scenario, inject and debrief material; findings across exercises | high | generative assistant, retrieval over validation records, analytics for recurring findings | approved corporate environment only |
| Validate | Evidence-gap scan against a checklist; management review narrative | medium to high | retrieval over BCMS records, BI and reporting | approved corporate environment |

## Where a tool can run

| Where it runs | Suitability for BCM | Main caution |
|---|---|---|
| Free public service | Generic brainstorming only, no confidential content | Never use it for BCM data, internal records, incident or licensed material |
| Individual paid service | Low-risk individual productivity, if formally approved | Better features do not mean acceptable privacy, governance or licensing |
| Team or business subscription | Basic internal use if approved and governed | Do due diligence on access control, retention, administration and contract |
| Enterprise or corporate licence | Often right for live BCM work | It depends on configuration, retention, identity integration, connector control and contract terms. The licence covers the platform, never the material you upload |
| Private, self-hosted or on-premise | Highly sensitive or regulated use cases | It needs technical skill, mature governance and operational support |

## Before you approve a tool

These checks must be passed before a tool can access your data.

Before you approve a tool for a class of data, check:

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
- the provider's breach notification terms, and whether your third-party risk process and your incident plan cover the provider
- ability to restrict or govern source material
- compliance with internal AI policy and information classification rules
- a date to check these answers again, at each renewal and whenever the provider changes the model

An enterprise label only indicates where the tool is used. The provider's retention policy and admin settings determine what data is kept. Read all of them before you rely on the label. Record the answers with the approval. In a chat app, the vendor can switch or retire the model without asking, and you cannot pin one, so set a fixed date for the re-check. *Self-check* question 1 in `levels.md` asks whether the team knows which tool is approved for which data. Most of the list repeats the source document's Annex A4 and matches the due-diligence and contract requirements in ETSI EN 304 223 (2025, provisions 5.1.2-7 and 5.2.2-6), the four data-handling questions in the UK Government AI Playbook (2025, "Working with your organisational data"), the supply-chain and failover practice in the NCSC and CISA guidelines (2023, "Secure your supply chain") and the third-party inventory with termination plans in the SEI model (2026, section 4.11.2). You can find the full entries for these four sources in `references.md`. The provider-breach item and the re-check date go beyond Annex A4. ETSI EN 304 223 (2025, provision 5.2.2-5) asks for an AI incident management plan and a recovery plan that are created, tested and maintained, and the SEI model (2026, section 4.11.2) asks for the third-party list to be updated periodically and for third parties to be assessed against their contracts. Neither source says what a provider owes you after a breach of its own, so that term comes from the contract.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
