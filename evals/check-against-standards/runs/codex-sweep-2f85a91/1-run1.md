# $check-against-standards case 1, run1: Codex, guidance at 2f85a91

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a101be-778b-7b33-bd43-abda0069c741`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I’m using the check-against-standards skill to review the draft and identify questions for its owner before board approval. I’ll first check the review instructions and available source texts.

What sensitivity class does the draft contain—public, internal, confidential, or high-sensitivity—and is this environment approved for that class?

The skill’s [preflight.md](.agents/skills/check-against-standards/preflight.md) requires that answer before reading the attachment. I opened the draft too early; I’ve stopped the review pending your answer.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g 'bc-policy-draft.md' -g '*.md' .agents/skills/check-against-standards"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/SKILL.md .agents/skills/check-against-standards/preflight.md; cat bc-policy-draft.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/units/data-rules.md .agents/skills/check-against-standards/units/stages/govern.md .agents/skills/check`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

Your stated class is medium, and the environment is approved for high. I’ll use that classification and continue with the review intake.

Which frameworks and parts should I compare the draft against? Available texts include DORA, Delegated Regulation (EU) 2024/1774, NIST SP 800-34 Rev. 1, NIST CSF 2.0, the Swiss ICT minimum standard, and UK Organisational Resilience Guidance. For ISO 22301, I need your copy and confirmation that its licence permits this use.
- DORA Articles 5–6 and 11–12, plus Delegated Regulation (EU) 2024/1774 Articles 24–26
- NIST SP 800-34 Rev. 1, chapters 3–5
- NIST CSF 2.0, Govern and Recover

Which jurisdiction and regulatory regime apply to the organisation, and is it subject to any exemption or simplified ICT risk management framework? This scopes the review; legal or compliance will need to confirm applicability.

Please answer the framework and jurisdiction questions above before I compare the policy.

The skill’s [review intake](.agents/skills/check-against-standards/units/stages/govern.md) requires “the framework texts I select” and says to “Wait for my answers.” Your selection fixes the sources; jurisdiction and any exemptions determine which regulatory points need legal or compliance review.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat bc-policy-draft.md; head -n 32 .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; head -n 32 .agents/ski`

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

I’ll compare the full draft against DORA and the supplied NIST SP 800-34 Rev. 1 text, which covers chapters 1–5. I’m taking “all of it” as the review scope. Jurisdiction and exemptions remain unspecified, so regulatory applicability will be a question for legal or compliance.

The draft’s two-year testing cycle differs from DORA’s annual testing provisions under the standard ICT risk management framework. The three-year policy review also leaves its relationship to the annual framework review unclear. I’ll keep those questions conditional on applicability and distinguish missing policy content from matters that may be covered in separate plans.

Draft review: **the testing cycle is the clearest conflict to resolve**, subject to confirming DORA applicability. The other main questions concern governance, recovery objectives, BIA coverage and the plans supporting this policy. These are questions for the owner, not a compliance verdict.

Sources and document control:

- **bc-policy-draft.md:** version 0.4; 3 September 2026; draft for the management board; owner: Chief Operating Officer.
- **DORA:** Regulation (EU) 2022/2554; Official Journal dated 27 December 2022; supplied text as adopted, retrieved 10 September 2026.
- **NIST SP 800-34 Rev. 1:** May 2010, with errata referenced in the supplied header; retrieved 10 September 2026; supplied Executive Summary and chapters 1–5.

Citations below identify sections of `bc-policy-draft.md` and articles or sections of the corresponding supplied framework file: `literature/eur-lex/dora-regulation-2022-2554.md` or `literature/nist/sp-800-34r1-contingency-planning-body.md`.

**DORA — questions for the Chief Operating Officer**

Every point in this block is **marked for legal or compliance review**. Points concerning Articles 5–15 depend on whether the standard framework applies; Article 16 provides a different framework for certain exempted entities.

| Type and policy passage | Source comparison and owner question |
|---|---|
| **Contradiction — §5:** “Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through.” | Article 24(6): “Financial entities, other than microenterprises, shall ensure, at least yearly, that appropriate tests are conducted on all ICT systems and applications supporting critical or important functions.” Article 11(6)(a) also specifies annual continuity and recovery plan testing and testing after substantive changes. **If applicable, how will the two-year cycle be reconciled with these provisions?** |
| **Gap — §5, testing method** | Article 11(6) includes “scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities”. **Where are these scenarios, crisis communication tests, and operational recovery tests addressed beyond the desktop walk-through?** |
| **Gap — §5, testing governance** | Article 24(4) requires tests by “independent parties, whether internal or external”; Article 24(5) addresses prioritising and remedying test findings and validating their resolution. **Where are tester independence, remediation and validation responsibilities established? Has the competent authority identified the institution for TLPT under Article 26, and, if so, where are Articles 26–27 addressed?** |
| **Gap — §3, roles** | Article 5(2)(e) gives the management body responsibility to “approve, oversee and periodically review” the ICT continuity policy and response and recovery plans. Article 5 also addresses resources, reporting, training and third-party oversight. **Where are these board responsibilities distinguished from COO ownership, BCM administration and IT plan ownership?** |
| **Gap / ambiguity — §7:** “The policy owner reviews this policy every three years.” | Article 6(5) states that the ICT risk management framework is “reviewed at least once a year”, subject to its microenterprise qualification, and specifies additional review triggers. Article 11(6) links policy and plan reviews to tests, audits and supervisory reviews. **Does three years describe only this policy’s scheduled review, or also the wider framework review? Where are the annual and event-triggered reviews established?** |
| **Gap — §§2 and 4, scope and BIA** | Article 11(5): “The BIA shall consider the criticality of identified and mapped business functions, support processes, third-party dependencies and information assets, and their interdependencies.” **Does the BIA cover these elements, severe disruption scenarios, and quantitative and qualitative impacts beyond payment services and customer support? What triggers updates between scheduled BIAs?** DORA does not specify a fixed BIA refresh interval in this passage. |
| **Gap / ambiguity — §2:** “the marketing website is not.” | Article 8(1) addresses “all ICT supported business functions” and their supporting assets and dependencies. **Is the website excluded only from continuity recovery priorities, or also from the ICT risk inventory? What documented dependency assessment supports the exclusion?** |
| **Gap — §6:** “The IT manager sets the recovery time objectives for all systems.” | Article 12(6) addresses “recovery time and recovery point objectives for each function”, considering criticality and market impact. **Where are function-level objectives, recovery point objectives, agreed service levels and their relationship to system objectives established? Does “sets” include approval authority?** The cited passage does not prescribe a particular job title. |
| **Gap — §§1–7, backups and restoration** | Article 12(1)(a) requires backup procedures specifying “the scope of the data that is subject to the backup and the minimum frequency of the backup”. Article 12 also addresses restoration testing, segregation, redundant capacity and integrity checks. **Which controlled documents address these matters and connect them to this policy?** |
| **Gap — §§1 and 3, activation and crisis management** | Article 11(2)(c) requires arrangements to “activate, without delay, dedicated plans”; Articles 11(7)–(8) address crisis management and accessible disruption records. **Where are activation authority, triggers, containment, recovery priorities, crisis communications and activity recording established?** |
| **Gap — §§1–7, incident reporting** | Article 17(1): “Financial entities shall define, establish and implement an ICT-related incident management process to detect, manage and notify ICT-related incidents.” Articles 18–19 address classification and reporting; Article 23 extends those provisions to operational or security payment-related incidents. **Which procedures connect continuity activation to incident classification, board escalation, client notifications and regulatory reporting?** |
| **Gap — §§2–5, third parties** | Article 28(8): “For ICT services supporting critical or important functions, financial entities shall put in place exit strategies.” Articles 28–30 also cover registers, assessments, concentration risk, contractual continuity provisions and transitions. **Where are outsourced dependencies, provider continuity tests, contractual recovery commitments and tested exit plans addressed? How are relevant critical-provider restrictions and supervisory risks under Articles 31(12) and 42 handled?** |
| **Gap — §§3 and 7, assurance and learning** | Article 6(6) addresses regular independent internal audit; Article 11(3) addresses audit of response and recovery plans. Article 13(6) requires “ICT security awareness programmes and digital operational resilience training as compulsory modules”. **Where are independent assurance, staff and management training, post-incident reviews, lessons learned and annual management reporting established?** |
| **Gap — §§1–7, wider framework connections** | Article 6(1) requires a “sound, comprehensive and well-documented ICT risk management framework”. Articles 7–10 address systems, identification, prevention and detection. **Which controlled framework documents establish these capabilities and their connection to continuity arrangements? If voluntary information sharing under Article 45 is used, where are its safeguards and notification arrangements documented?** |

The supplied DORA text also contains provisions directed to authorities, critical providers and other financial entity types. Their absence from this payment institution’s BC policy is not, by itself, a policy gap.

**NIST SP 800-34 Rev. 1 — questions for the Chief Operating Officer**

NIST describes guidance for federal information systems that private organisations may use. Its federal mandates and FIPS classifications are not assumed to bind this institution.

| Type and policy passage | Source comparison and owner question |
|---|---|
| **Gap — §§2–3, policy foundations** | §3.1 lists “Resource requirements”, “Training requirements”, “Plan maintenance schedule”, and “Minimum frequency of backups and storage of backup media” among policy elements. **Where are these elements established, and which supporting policies does this draft reference?** |
| **Gap — §4, BIA coverage** | §3.2 links systems to business processes, resources and recovery priorities. **How does the service-level BIA identify system components, supporting resources, interdependencies and the sequence in which they must recover?** |
| **Gap / ambiguity — §§4 and 7, changes between reviews** | §3.6: “When a significant change occurs, the BIA should be updated with the new information to identify new contingency requirements or priorities.” **Do the three-year cycles permit updates after significant changes, and how are those triggers connected to change management?** |
| **Gap — §6, recovery objectives** | §3.2.1 says the coordinator should work “with the process owners, leadership and business managers” to determine acceptable downtime. It distinguishes maximum tolerable downtime, RTO and RPO. **How does the IT manager obtain and validate business tolerances, include data-loss tolerances, and ensure system RTOs leave sufficient time for business recovery?** |
| **Potential contradiction — §5, desktop-only approach** | Draft: “by a desktop walk-through.” §3.5.4: “For moderate-impact systems, a functional exercise at an organization-defined frequency should be conducted.” It calls for a full-scale functional exercise for high-impact systems. **If the institution adopts these impact categories, which systems need functional exercises beyond discussion?** This depends on classification; the passage does not prescribe universal annual exercises. |
| **Gap — §5, practical testing and training** | §3.5.1: “Each information system component should be tested to confirm the accuracy of individual recovery procedures.” §3.5.2: “Training should be provided at least annually.” **Where are component recovery tests, success criteria, training and induction for newly assigned recovery personnel established?** |
| **Gap — §3, authority and deputies** | §3.4.6 identifies “a single authoritative role for overall decision-making responsibility, including plan activation”. **Who may activate plans, authorise expenditure and coordinate recovery teams, and who acts when that person is unavailable?** |
| **Gap — §§1–7, activation through return to normal** | §4.2.1: “Activation criteria for system outages or disruptions are unique for each organization and should be stated in the contingency planning policy.” §§4.2–4.5 cover notification, assessment, recovery, escalation, validation and deactivation. **Where are these criteria and supporting procedures documented, including authority to declare recovery complete?** |
| **Gap — §§2 and 6, recovery strategy** | §3.4.1 says recovery methods “should address disruption impacts and allowable downtimes identified in the BIA”. §§3.3–3.4 and chapter 5 discuss preventive measures, backups, alternate facilities, equipment, telecommunications and security. **Which documented strategies demonstrate how required recovery times and data-loss tolerances can be achieved across the relevant platforms?** |
| **Gap — §7, plan control** | §3.6 says plans should be reviewed “whenever significant changes occur to any element of the plan” and addresses distribution, accessible copies and version control. **Does this policy’s review cycle also govern operational plans, and where are their change triggers, controlled distribution and availability during an outage established?** |

**Gaps and limits of this review**

- **Intake statements — cite: Gaps.** You classified the material as medium, confirmed approval of this environment for high, and selected DORA and NIST SP 800-34 with “all of it” as scope. Jurisdiction, exemption status and regulatory regime remain unspecified. The comparison uses conditional applicability; legal or compliance needs to establish whether Articles 5–15 or Article 16 apply.
- **Draft status.** Version 0.4 remains a draft dated 3 September 2026. The next review date and management approval are not in the supplied document. COO: what controlled review date and approval record will accompany the policy through the normal approval route?
- **Supporting evidence.** No BIA, recovery plans, incident procedures, supplier records, training records or framework documents were supplied. Missing policy counterparts do not establish that the organisation lacks those arrangements. COO: which controlled documents settle the questions above?
- **Source coverage and currency.** DORA was supplied as adopted, without recitals; subsequent amendments and implementing texts were not established from the selected sources. NIST’s appendices and figures were not supplied. These portions are **not reviewed**. The publisher texts govern any conversion discrepancies.
- **Frameworks not selected — not reviewed:** Delegated Regulation (EU) 2024/1774, ISO 22301, NIST CSF 2.0, Swiss ICT minimum standard, UK Organisational Resilience Guidance, and the supplied AI-related frameworks. No licensed ISO text was supplied.
- **Human review and approval.** The COO should resolve these questions with legal, compliance, information security and supporting document owners. A person must check each comparison against the source text. The draft’s status remains unchanged; policy and approval decisions stay with management.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
Chief Operating Officer answers these, legal or compliance the marked points.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'wc -l .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md .agents/skills/check-against-standards/literature/ni`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md'`
- command_execution: `/bin/bash -lc "rg -n '"'^### Article|''^#|annual|annually|policy|maximum tolerable|recovery point'"' .agents/skills/check-against-standards/literature/nist/sp-8`
- command_execution: `/bin/bash -lc "sed -n '164,460p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md"`
- command_execution: `/bin/bash -lc "rg -n '"'^### Article'"' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '1,45p' .agents/skills/ch`
- command_execution: `/bin/bash -lc "sed -n '137,207p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '235,297p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '434,501p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '659,777p' .agents/skil`
- command_execution: `/bin/bash -lc "sed -n '349,430p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '498,584p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '669,777p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md"`
- command_execution: `/bin/bash -lc "sed -n '446,497p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '792,839p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '498,584p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '367,393p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '585,791p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '840,1040p' .agents/skills/check`
- command_execution: `/bin/bash -lc "sed -n '208,234p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '425,430p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '46,67p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '502,558p' .agents/skills`
