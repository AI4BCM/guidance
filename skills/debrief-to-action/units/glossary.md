<!-- meta: unit=glossary version=2026.09.1 -->
# Glossary

| Term | Meaning |
|---|---|
| **Agentic system** | An AI system that autonomously plans and executes multi-step tasks toward a goal. Some vendors also call a fixed, rule-based setup an agent, so judge a tool by who decides what comes next. |
| **AI** | Computer systems that perform tasks which normally need human judgement, such as reading, summarising, classifying or predicting. In this guidance the term covers generative AI, retrieval tools, machine learning and the workflows built from them. |
| **Auditable** | Recorded so that someone else can check afterwards what was asked, which sources were used, when, and who approved the result. An output is auditable when those four things can still be retrieved later. |
| **BCM lifecycle** | The six activities that manage continuity capability. They are governance, embedding, analysis, solutions design, implementation and validation. |
| **BCMS** | Business Continuity Management System; the management system for business continuity, set out in ISO 22301:2019. |
| **BIA** | Business Impact Analysis; analysis of activities to determine the effects of disruption. |
| **Connector** | A controlled link between an AI system or workflow and a business system, such as a document repository, an HR directory, a supplier record system, a risk register or an incident management tool. It retrieves or acts on information. Set it to read-only and least privilege unless a write action is approved; many tools switch write actions on by default. |
| **Gate** | A gate has two senses in this guidance. The first is the condition a maturity level requires before work runs at that level. It is a fact you can show, and an intention does not count. *Where to start, by level* states one for each of the five levels. The second is the approval step where a named person approves an action or a record change before it goes ahead, as in the checklist's approval gates. |
| **Generative AI** | AI that creates content rather than analysing existing data. Its output reads fluently whether or not it is correct, which is why every output is reviewed (principle 1). |
| **Invention** | A confident statement that no source supports, also called hallucination. The controls are principle 3 and the citation check. |
| **Invoke** | To put a business continuity plan into effect after a disruption. A person with the authority decides it; AI never invokes a plan on its own (principle 4). |
| **LLM** | Large language model. An LLM is a model designed to interpret and generate human language. Chatbots and most AI assistants are built on one. |
| **Machine learning** | AI that learns patterns from data rather than following written rules. In BCM it appears as analytics, for example recurring themes across exercise reports or concentration across suppliers. |
| **MTPD** | Maximum Tolerable Period of Disruption; how long an activity can be down before the impact is unacceptable. |
| **Override** | A reviewer's change to an AI output, or its rejection. Override rates are worth counting, and a low rate can mean that reviewers approve without checking (principle 1). |
| **Prompt** | The instruction a person gives an AI tool. A prompt requests behaviour and enforces nothing; permissions decide what the tool can reach (principle 4). |
| **Prompt injection** | Text in a document, page or message written to make an AI do something other than what its user asked. An AI cannot reliably tell it from the content around it (principle 4). |
| **RA** | Risk Assessment; identifying, analysing and evaluating the risks of disruption to prioritised activities and the resources they depend on, so that a person can decide the treatment and accept the residual risk. *Two more methods* gives the method with AI support. |
| **RAG** | Retrieval-Augmented Generation; the model first fetches passages from an approved repository, then answers from them. It reduces invention and does not remove it, so citations are still checked (principle 3). |
| **Register** | An approved list of record that the organisation maintains and a named person owns, such as the list of activities, risks, suppliers or resource requirements. AI may draft an entry; only the owner makes it a register entry. |
| **Repository** | The controlled place where approved content is kept, such as the plan library, the document management system or the BCMS content store. Approved means someone is accountable for what is in it and for how current it is. |
| **Retrieval** | Fetching passages from an approved repository so that an answer is based on them rather than on what the model learned in training. The technique is RAG; the control is that the repository is approved and its contents are dated. |
| **Role-based access** | Permission granted by the job someone does, so a retrieval returns only what that person is already entitled to read. With it, a connector speeds up access to a repository without widening it. |
| **RPO** | Recovery Point Objective; the point to which information and data used by an activity is restored to enable the activity to operate on resumption (ISO 22300:2025). |
| **RTO** | Recovery Time Objective; the time frame within the MTPD for resuming disrupted activities at a specified minimum acceptable capacity (ISO 22301:2019). |
| **Skill** | A reusable AI task set up for one purpose. In the tools, a skill holds fixed instructions and sometimes scripts, and loads when a request matches its description. This guidance adds an approved knowledge base, a defined output format and a named reviewer. Its outputs are checked before anyone uses them. |
| **Tenant** | Your organisation's own separately governed space inside a vendor's service, holding your accounts, your files and your settings; some vendors call it a workspace or an organisation. Work done there follows the vendor's terms, your contract and your admin settings, which may or may not meet your existing data rules. Some services host this space on the vendor's own infrastructure. Work done outside it falls under none of your settings, whatever the tool is called. |
| **Workflow** | A defined sequence of automated and manual steps that makes a task repeatable. |

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
