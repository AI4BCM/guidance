<!-- meta: unit=data-rules version=2026.11.1 -->
# The rules that always apply

## Data rules

**If you paste something into the wrong tool, it will stay there forever.**

## Data classification decides the tool

The more sensitive the data and the more serious the consequences of an error, the more controlled the environment must be. Public, free online tools are never used for BCM data. They are only useful for generic brainstorming that discloses nothing about your organisation.

## Classification levels

**Below is a list of data assets of the highest classification level.
Paste it in an approved corporate or private environment only.**

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

**Passwords, keys and access tokens go into no tool**, approved or not.

## Prompt injection

The text in a document, webpage, email, picture or file can be written in such a way as to make an AI perform an action that you did not ask for, such as ignoring its instructions, revealing data or taking action. AI tools cannot reliably distinguish such text from its context, and providing an additional prompt will not help (OWASP, 2025, ASI01 and ASI06; IMDA, 2026, sections 2.3.1 and 2.3.2). Give a tool that reads data outside of your controlled environment only the permissions it needs for the task (principle 3). If you notice that a document is instructing the AI in unintended ways, inform the owner and your information security team immediately.

## What AI4BCM's own tools read

| | AI4BCM Guidance chatbot | AI4BCM skills | Connector | BIA-Workflow |
|---|---|---|---|---|
| What it reads | Nothing of yours | Your files, in your approved environment | Nothing of yours | Your process data |

The row says what each one retrieves. It does not say what you may type in. `/learn-bcm` and `/check-against-standards` also read this guidance's units and open literature, which ship with them. The chatbot at ai4bcm.org/chat has no upload box, and it answers from this guidance and the public standards it cites. That is no reason to describe your own organisation to it. Keep case material out.

## Before you paste

Any skill or workflow that reaches your files needs its environment, permissions and retention approved first, under *Before you approve a tool* in `tools.md`. If you cannot say where the data goes and how long it stays there, do not paste it yet.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
