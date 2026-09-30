<!-- meta: unit=data-rules version=2026.09.1 -->
# Data Rules

Read this first. It decides where the task may happen, and what is pasted into the wrong tool cannot be taken back.

## The rule of thumb

The more sensitive the data and the more serious the consequence of error, the more controlled the environment. Public and free online tools are never used for BCM data. Generic brainstorming that discloses nothing about your organisation is all they are for.

## Sensitivity classes

High-sensitivity, approved corporate or private environment only:

- BIA data and risk assessment detail
- incident records and live crisis information
- personal data, contact lists and personnel records
- vulnerabilities and control weaknesses
- recovery strategies and design assumptions
- supplier weaknesses and contractual dependencies
- security-related architecture or site detail
- board papers and executive-session material
- audit findings not yet cleared by the audit owner

Classify before entering; how sensitive the data is decides which tools you may use.

Passwords, keys and access tokens go into no tool, approved or not. A tool reaches your systems only through the access it was approved with.

## What AI4BCM's own tools read

| | AI4BCM Guidance chatbot | `/ask-ai4bcm` skill | Connector | BIA workflow |
|---|---|---|---|---|
| What it reads | Nothing of yours. | Your files, in your approved environment. | Nothing of yours. | Your process data. |

The row says what each one retrieves. It does not say what you may type in. The chatbot at ai4bcm.org/chat has no upload box, and it answers from this guidance and the public standards it cites. That is no reason to describe your own organisation to it. Keep case material out. Even an approved document store can hold text written to make an AI do something else. An AI cannot reliably tell such an instruction from the text around it (OWASP, 2025, ASI01 and ASI06; IMDA, 2026, section 2.3.2). Treat what the tool finds as information to check, never as an order to follow. If a document seems to give the AI orders, tell the document's owner.

## Before you paste

Confirm the tool is approved for this class of data, the task is clear and narrow, and a competent person reviews the result. A skill or a workflow that reaches your files needs its environment, its permissions and its retention approved as well; it is approved only when it passes the checks under "Before you approve a tool" in `tools.md`. If you cannot say where the data goes and how long it stays, do not paste it yet.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
