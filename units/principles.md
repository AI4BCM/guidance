<!-- meta: unit=principles version=2026.09 cites=1.1,1.2,1.4.1,1.4.2,1.4.8,quick-start -->
# Principles

This guidance helps BCM professionals choose AI tools for BCM tasks, apply them safely and bring them into BCM work without weakening governance, control or resilience. It does not cover continuity planning for AI systems or AI-dependent services, the design, training or procurement of AI platforms, cybersecurity architecture for AI, or the legal interpretation of AI regulation, and it replaces none of the organisation's own BCM framework, policies, information security requirements, legal advice or professional judgement. Where those questions arise, the BCM professional works with the specialists who own them, and where this guidance and an internal rule differ, the stricter control applies. The guidance assumes no particular standard. A reader working to ISO 22301:2019, to BSI-Standard 200-4, to the practices of a professional body, or to a method their organisation has established over years, can use it as it stands; the guidance is neither derived from nor certified against any of them.

## 1. Accountability stays human

AI does not own the BCMS. Any AI-generated output entering a BCMS artefact, report or decision is reviewed before it is relied upon by a competent person holding the sources and time to reject it. Where either is missing, the reviewer escalates instead of approving. Approval counts and override rates are worth tracking, and alone they do not demonstrate effective review; a low override rate may signal rubber-stamping (IMDA, 2026, section 2.2.2).

## 2. Match the tool to the sensitivity

The more sensitive the information, and the more serious the consequence of error, the more controlled the AI environment. Public and free online tools are never used for BCM data: BIA data, risk assessment detail, incident records, vulnerabilities, contact and personnel lists, recovery strategies, supplier weaknesses and site or architecture detail. Classify the material before it is pasted, not after.

## 3. Sources only, state gaps, cite

Bind the model to approved internal repositories and official external sources; require it to answer from those alone, name what is missing instead of filling it, and cite the document behind each statement. Check the cited passage against the claim it supports. Retrieval reduces invention; it does not review. A stale register may be amplified rather than solved.

## 4. What AI never does alone

Prohibited or tightly restricted:

- declaring an incident or crisis without authorisation
- invoking plans autonomously
- sending external communications unsupervised
- approving policy or strategy changes
- accepting risk
- altering controlled records without review
- interpreting law or regulation without expert review

Permissions enforce these limits; prompt wording only requests them, and the authority remains human (IMDA, 2026, section 2.3.1; NCSC and CISA, 2023).

Prohibited outright, and no approval makes it acceptable:

- fabricating evidence, audit material or records
- replacing human welfare, ethical or safety judgement

Review enforces these two. A record that fails the citation check in principle 3 is rejected whoever approved the task, and a welfare, ethical or safety judgement is made by the person accountable for it.

## 5. Value, not speed

Success is whether quality, usability, timeliness, insight and governance improved. Speed alone says nothing. A bulky document that looks complete is not necessarily useful, accurate or operationally credible. No bulk plan generation.

## Minimum control checklist

Before any AI-assisted BCM task, confirm that:

- ☐ the tool is approved for the type of data involved
- ☐ the information is suitable for that environment
- ☐ the task is clearly defined and bounded
- ☐ the output is grounded in approved and current sources, citations checked
- ☐ a competent reviewer has the sources, the time and a route to escalate
- ☐ any actions or record changes have approval gates
- ☐ traceability is sufficient for accountability
- ☐ fallback methods exist if the tool is unavailable

## The rule

Ask AI to prepare, compare, summarise, retrieve, and challenge. But require people to decide, approve, and act.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
