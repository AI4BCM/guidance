<!-- meta: unit=data-rules version=2026.09.1 -->
# Data Rules

Read this first. It determines where the task can be carried out, and anything pasted into the wrong tool cannot be undone.

## Sensitivity decides the tool

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

| | AI4BCM Guidance chatbot | AI4BCM skills | Connector | BIA-Workflow |
|---|---|---|---|---|
| What it reads | Nothing of yours | Your files, in your approved environment | Nothing of yours | Your process data |

The row says what each one retrieves. It does not say what you may type in. `/learn-bcm` and `/check-against-standards` also read this guidance's units and open literature, which ship with them. The chatbot at ai4bcm.org/chat has no upload box, and it answers from this guidance and the public standards it cites. That is no reason to describe your own organisation to it. Keep case material out.

## Prompt injection

The text in a document, webpage, email or file can be written in such a way as to make an AI perform an action that you did not ask for, such as ignoring its instructions, revealing data or taking action. AI tools cannot reliably distinguish such text from the surrounding content, and a line in your prompt will not stop them (OWASP, 2025, ASI01 and ASI06; IMDA, 2026, section 2.3.2). Treat information found by the tool as something to be checked, not as an order to be followed. Give a tool that reads outside material only the permissions needed for the task (principle 4). If a document appears to instruct the AI, inform its owner and your information security team.

## Before you paste

Confirm that the tool has been approved for this class of data and that the task is clear and specific. A competent person must also review the result. Any skill or workflow that accesses your files must also have its environment, permissions and retention approved; this will only be approved once the checks under *Before you approve a tool* in `tools.md` have been passed. If you cannot specify where the data goes and how long it stays there, do not paste it yet.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
