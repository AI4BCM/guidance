<!-- meta: unit=data-rules version=2026.09 cites=1.4.1,1.4.2,quick-start -->
# Data Rules

Run this first. It decides where the task may happen, and it is the rule you cannot recover from: what is pasted into the wrong tool cannot be unpasted.

## The rule of thumb

The more sensitive the data, and the more serious the consequence of an error, the more controlled the environment has to be. **Public and free online tools are never used for BCM data** — not for a quick check, not because the account is paid. Generic brainstorming that discloses nothing about your organisation is all they are for.

## Sensitivity classes

High-sensitivity, approved corporate or private environment only:

- BIA data and risk assessment detail
- incident records and live crisis information
- personal data, contact lists and personnel records
- vulnerabilities and control weaknesses
- recovery strategies and design assumptions
- supplier weaknesses and contractual dependencies
- security-related architecture or site detail

Classify before entering, not after. The classification decides the tool; the tool does not decide what may go into it.

## What each way in reads

The three ways of using this guidance read different things:

| | Guidance chatbot | `/ask-ai4bcm` skill | BIA workflow |
|---|---|---|---|
| What it reads | Nothing of yours | Your files, inside your tenant | Your process data |

The chatbot answers from the guidance alone: no classification question arises, and no live data goes in. The skill runs inside your own tenant, so your existing data rules already cover it. The workflow holds process data under its own controls.

## Before you paste

Confirm the tool is approved for this class of data, the task is bounded, and a competent person reviews the result. If you cannot say where the data goes and how long it stays, the answer is not yet.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
