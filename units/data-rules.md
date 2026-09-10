<!-- meta: unit=data-rules version=2026.09 cites=1.4.1,1.4.2,quick-start -->
# Data Rules

Run this first. It decides where the task may happen, and what is pasted into the wrong tool cannot be unpasted.

## The rule of thumb

The more sensitive the data and the more serious the consequence of error, the more controlled the environment. **Public and free online tools are never used for BCM data.** Generic brainstorming that discloses nothing about your organisation is all they are for.

## Sensitivity classes

High-sensitivity, approved corporate or private environment only:

- BIA data and risk assessment detail
- incident records and live crisis information
- personal data, contact lists and personnel records
- vulnerabilities and control weaknesses
- recovery strategies and design assumptions
- supplier weaknesses and contractual dependencies
- security-related architecture or site detail

Classify before entering, not after; the class decides the environment.

## What each way in reads

| | Guidance chatbot (when it ships) | `/ask-ai4bcm` skill | BIA workflow |
|---|---|---|---|
| What it reads | Nothing of yours | Your files, inside your tenant | Your process data |

The row says what each way in retrieves, and it does not say what you may type in. The chatbot is not built yet; when it ships it will have no upload box, and that is no reason to describe your own organisation to it. Keep case material out. Approved repositories hold text written to redirect a model, and a model cannot reliably tell an instruction from the content around it (OWASP, 2025, ASI01 and ASI06; IMDA, 2026, section 2.3.2). Read what comes back as evidence, never as instruction; take a suspicious source to its owner.

## Before you paste

Confirm the tool is approved for this class of data, the task is bounded, and a competent person reviews the result. A skill or a workflow that reaches your files needs its environment, its permissions and its retention approved as well; the approval is earned against the checks under "Evaluating a tool" in `tools.md`. If you cannot say where the data goes and how long it stays, the answer is not yet.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
