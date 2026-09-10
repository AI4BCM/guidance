<!-- meta: unit=glossary version=2026.09 -->
# Glossary

| Term | Meaning |
|---|---|
| **Agentic system** | An AI system that autonomously plans and executes multi-step tasks toward a goal. |
| **Auditable** | Recorded so that someone else can check afterwards what was asked, which sources were used, when, and who approved the result. An output is auditable when those four things can still be retrieved later, not when a log exists somewhere. |
| **BCM lifecycle** | Governance, embedding, analysis, solutions design, implementation, validation: the activities managing continuity capability. |
| **BCMS** | Business Continuity Management System; the management system for business continuity, formalised in ISO 22301:2019. |
| **BIA** | Business Impact Analysis; analysis of activities to determine the effects of disruption. |
| **Connector** | A controlled integration linking an AI system or workflow to a business system, such as a document repository, an HR directory, a supplier record system, a risk register or an incident management tool, to retrieve or act on information; read-only and least privilege by default. |
| **Gate** | The condition a maturity level requires before work runs at that level. A gate is a fact you can show, not an intention; `levels.md` states one for each of the five levels. |
| **Generative AI** | AI that creates content rather than analysing existing data. |
| **LLM** | Large language model. An LLM is a model designed to interpret and generate human language. |
| **MTPD** | Maximum Tolerable Period of Disruption; how long an activity can be down before the impact is unacceptable. |
| **RA** | Risk Assessment; identifying, analysing and evaluating the risks of disruption to prioritised activities and the resources they depend on, so that a person can decide the treatment and accept the residual risk. The method with AI support is in `stages/analysis.md`. |
| **RAG** | Retrieval-Augmented Generation; grounding output in an authoritative knowledge base. |
| **Register** | An approved list of record that the organisation maintains and a named person owns: activities, risks, suppliers, resource requirements. AI may draft an entry; only the owner makes it a register entry. |
| **Repository** | The controlled place approved content is kept — the plan library, the document management system, the BCMS content store. Approved means someone is accountable for what is in it and for how current it is. |
| **Retrieval** | Fetching passages from an approved repository so that an answer is grounded in them rather than in model memory. The technique is RAG; the control is that the repository is approved and its contents are dated. |
| **Role-based access** | Permission granted by the job someone does, so a retrieval returns only what that person is already entitled to read. It is what keeps a connector from widening access to a repository rather than merely speeding it up. |
| **RTO** | Recovery Time Objective; the time frame within the MTPD for resuming disrupted activities at a specified minimum acceptable capacity (ISO 22301:2019). |
| **Skill** | A reusable AI task configured for one purpose: fixed instructions, an approved knowledge base, a defined output format, a named reviewer. Repetition makes the method repeatable; reliability comes from evaluating its outputs. |
| **Tenant** | Your organisation's own separately governed space inside a vendor's service, holding your accounts, your files and your settings. Work done inside your tenant stays under your existing data rules; work done outside it does not, whatever the tool is called. |
| **Workflow** | A defined sequence of automated and manual steps that makes a task repeatable. |

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
