# $check-against-standards case 1, run2: Codex, guidance at 9c837c3

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a1013b-85e6-7331-b09c-040511c89d21`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I’m using the check-against-standards skill to review the draft and identify questions for its owner before board review. I’ll first check the required intake and source rules.

What data class does the draft contain: public, internal, confidential, or restricted?
- Public
- Internal
- Confidential
- Restricted

Before I open the draft, please confirm its data class: **public, internal, confidential, or restricted**.

The skill’s [preflight.md](.agents/skills/check-against-standards/preflight.md) requires: “Until the person answers, open or read no attached file.” The draft remains unread.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g 'bc-policy-draft.md' -g '*.md' .agents/skills/check-against-standards"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/SKILL.md .agents/skills/check-against-standards/preflight.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/units/data-rules.md .agents/skills/check-against-standards/units/stages/govern.md .agents/skills/check`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I’ll use your stated classification of medium and your confirmation that this environment is approved for high. I’ll read the draft now and check what framework selection and review scope remain open.

Which frameworks and parts should I compare the policy against? DORA and Delegated Regulation (EU) 2024/1774 are available with the skill; ISO 22301 would require your own copy and confirmation that its licence permits this use.
- DORA and 2024/1774: relevant continuity and ICT recovery provisions
- DORA only: relevant continuity and ICT recovery provisions
- NIST SP 800-34 Rev. 1: chapters 1–5

I’ve read version 0.4, dated 3 September 2026, marked draft for the management board and owned by the Chief Operating Officer.

Please select the frameworks and parts to review. A suggested scope is **DORA and Delegated Regulation (EU) 2024/1774, covering continuity and ICT recovery**.

The skill’s [review intake](.agents/skills/check-against-standards/units/stages/govern.md) requires comparison against “the framework texts I select” and says to wait for your answers. The policy itself names no framework.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat bc-policy-draft.md'`

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

I’ll compare the whole policy against the supplied DORA text and NIST SP 800-34 Rev. 1. I’ll check each source’s coverage and report separate questions for the Chief Operating Officer, with DORA points marked for legal or compliance review.

The draft’s two-year testing interval differs from DORA’s annual testing provision under the full ICT risk management framework. The draft does not say whether the institution has the exemption that would put it under Article 16’s simplified framework, so I’ll make that an explicit legal/compliance question. The supplied NIST text covers the Executive Summary and Chapters 1–5; its appendices are unavailable for this review.

[Policy](bc-policy-draft.md): version 0.4; 3 September 2026; **draft for the management board**; owner: Chief Operating Officer.
[DORA source](.agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md): Regulation (EU) 2022/2554, as adopted; Official Journal dated 27 December 2022; retrieved 10 September 2026.
[NIST source](.agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md): SP 800-34 Rev. 1, May 2010, with publisher’s errata; retrieved 10 September 2026.

**Draft review — questions for the Chief Operating Officer**

The main questions concern testing frequency and method, management oversight, BIA coverage, and how recovery objectives are determined. These are document comparisons; they do not establish whether the organisation meets either framework. A missing policy passage may be covered in another controlled document.

**DORA**

Every question in this block is marked **for legal or compliance review**. Questions referencing Articles 5–15 depend on confirmation that the full framework applies.

| Type | Policy passage and source comparison | Question for the Chief Operating Officer |
|---|---|---|
| Applicability gap | Header describes a small payment institution with 140 staff. DORA Articles 2(1)(b), 3(60), 4 and 16(1) distinguish payment institutions, microenterprises, proportionality and exempted payment institutions. | What is the institution’s legal authorisation and exemption status, and does it fall under Articles 5–15 or Article 16’s simplified framework? The word “small” does not settle this. |
| Contradiction, conditional on full framework | §5: “Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through.” Article 11(6)(a): “test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly”. | How will §5 address annual testing and testing after substantive changes to systems supporting critical or important functions? |
| Testing gap | §5 specifies only a desktop walk-through. Article 11(6) requires non-microenterprises’ testing scenarios to include cyber-attacks and switchovers; Articles 24(4)–(6) address independent testing, remediation and annual testing of critical systems. | Where will practical recovery and switchover tests, crisis communication tests, tester independence, corrective actions and validation be required? Has applicability of advanced testing under Article 26 been determined? |
| Governance gap | §3 assigns the COO, BCM officer and IT manager roles. Article 5(2)(a), (e) and (g) addresses management-body responsibility, approval and oversight of continuity arrangements, and resources. | Where will management-body accountability, approval of the policy and recovery plans, oversight, reporting and resource allocation be stated or cross-referenced? |
| Scope and identification gap | §2 excludes the marketing website. Articles 6(2) and 8(1), (4)–(6) address assets, functions, inventories and dependencies. | What dependency assessment supports the website exclusion, including shared infrastructure or communications use, and where are all ICT-supported functions and dependencies mapped? |
| BIA gap | §4 covers payment services and customer support every three years. Article 11(5) addresses severe disruptions, quantitative and qualitative impacts, support processes, third parties, assets and interdependencies; Article 8(1)–(3) addresses annual classification/scenario reviews and major-change assessments. | How will the BIA cover these dependencies and impact criteria, and how will it remain aligned with annual reviews and major changes between its three-year cycles? |
| Recovery-objectives gap | §6: “The IT manager sets the recovery time objectives for all systems.” Article 12(6) addresses both recovery time and recovery point objectives for each function, criticality, market impact and agreed service levels in extreme scenarios. | How will system objectives connect to function-level objectives, tolerable data loss and business needs, and where will RPOs and the decision process be documented? |
| Recovery-arrangements gap | §§1, 3 and 6 refer to recovery but contain no backup or restoration requirements. Articles 11(2)–(4), (8) and 12(1)–(4), (7) address documented response arrangements, activation, backups, redundant capacity, secure restoration, reconciliation and disruption records. | Which controlled plans will implement these provisions, and how will the policy require their maintenance, availability and testing? |
| Crisis and incident-management gap | §§1 and 3 contain no crisis communication or incident-reporting route. Articles 11(7), 14 and 17–19 address crisis management, communications, incident handling, classification and reporting; Article 23 extends Chapter III to payment-related incidents. | Where will activation authority, crisis communications, incident escalation, classification, client notification and regulatory reporting be defined, including payment incidents that are not ICT-related? |
| Review and learning gap | §7 requires policy review every three years. Article 6(5) requires annual review of the non-microenterprise ICT risk management framework and event-triggered reviews; Articles 11(6) and 13(2)–(6) address policy/plan review, incident lessons, reporting and training. | How will this policy participate in those reviews and receive changes arising from incidents, tests, audits and supervisory instructions, and where are training obligations covered? |
| Wider-framework gap | §§1–7 contain no counterpart for the broader ICT control framework in Articles 6–10, or third-party arrangements in Articles 28–30, 31(12) and 42(3). | Which companion policies cover independent risk oversight and audit, protection and detection, supplier registers and due diligence, concentration risk, contractual continuity provisions, tested exit plans and supervisory risk notifications? |
| Conditional information-sharing gap | No counterpart in §§1–7. Article 45 permits information sharing subject to safeguards and requires notification of participation or cessation. | If the institution participates, which controlled arrangements cover safeguards and authority notification? |

**NIST SP 800-34 Rev. 1**

NIST §1.2 presents guidance for federal information systems and excludes general business-process continuity from its direct scope. Its federal-specific requirements need an explicit organisational adoption decision.

| Type | Policy passage and source comparison | Question for the Chief Operating Officer |
|---|---|---|
| Policy-content gap | §§1–3 establish purpose, scope and three roles. NIST §3.1 also identifies resource requirements, training, plan maintenance and backup frequency/storage as policy elements. | Where will these elements be stated or cross-referenced, and which federal-specific conventions does the organisation intend to adopt? |
| BIA gap | §4 defines coverage and a three-year cycle. NIST §§3.2–3.2.3 address system/process dependencies, resources, outage impacts, tolerable downtime and recovery priorities, including reconsideration as systems change. | What method and change triggers will ensure that the BIA identifies those elements and informs recovery priorities? |
| Recovery-objectives gap | §6 assigns RTO setting to the IT manager. NIST §3.2.1 calls for work with process owners, leadership and business managers on acceptable downtime and distinguishes MTD, RTO and RPO. | How will business owners validate downtime and data-loss tolerances, and how will system RTOs fit within process MTDs? |
| Potential contradiction in testing method | §5 says “by a desktop walk-through”. NIST §3.5.1 says testing “should be conducted in as close to an operating environment as possible”; §3.5.4 differentiates tabletop, functional and full-scale exercises by impact level. | Is the walkthrough intended to be the only validation method, and how will exercises and operational tests reflect each system’s assessed impact and recovery needs? |
| Training and improvement gap | §5 contains no training, test criteria or follow-up. NIST §§3.5–3.5.4 address annual role training, explicit test objectives, after-action reports and corrective actions. | Where will these activities and their schedules be required? |
| Strategy and technical gap | §§2–6 provide no recovery-strategy requirements. NIST §§3.3–3.4.6 and Chapter 5 address preventive controls, backups, alternate facilities, equipment, telecommunications, suppliers, security and resources. | Which recovery plans will document the applicable strategies, their costs and dependencies, and demonstrate how they support BIA-derived objectives? |
| Activation and return-to-service gap | §3 names plan ownership but no activation authority or recovery teams. NIST §§3.4.6 and 4.1–4.5 address authority and successors, notification, recovery sequencing, escalation, validation and deactivation. | Where will these responsibilities and procedures be defined and coordinated with business continuity, crisis communication and other plans? |
| Maintenance gap | §7 addresses policy review only. NIST §3.6 addresses plan reviews at an organisation-defined frequency and after significant changes, controlled distribution, accessible copies and change records. | What separate arrangements will keep recovery plans, contacts and supporting documents current and available during disruption? |

**Gaps and limits**

- **Your intake statements:** data class “medium”; environment approved for high; selected frameworks DORA and NIST SP 800-34; scope “All of it”. These define review scope and access, not organisational evidence. *(Source: Gaps — intake.)*
- **Draft status:** version 0.4, dated 3 September 2026, remains a draft. No approval record or last-review date was supplied. COO: what document-control and approval records will accompany the board submission? *(Policy header.)*
- **Source coverage:** the supplied DORA conversion contains enacting terms, excluding recitals and footnote texts; it is the adopted text, not a verified current consolidation. The NIST conversion contains the Executive Summary and Chapters 1–5; appendices and figures are **not reviewed**. COO: what authoritative source checks will settle these limits before reliance? *(Source-file headers.)*
- **Other frameworks:** Delegated Regulation 2024/1774, AI Act, NIST AI RMF and CSF, FONES, UK resilience guidance, ESAs statement and the skill’s other reference texts were not selected and are **not reviewed**. ISO standards were neither selected nor supplied with licence confirmation and are **not reviewed**.
- **Missing supporting evidence:** no BIA, asset inventory, plans, test results, contracts or companion policies were attached. Their existence and effectiveness cannot be established from this draft.
- **Ambiguous wording:** COO, does §6’s “sets” mean proposes or finally approves objectives; does §5’s “tested” mean discussion or demonstrated recovery; and does §7’s three-year review permit earlier changes? What wording or referenced procedure will resolve each reading? *(Policy §§5–7; DORA Articles 5, 11–12; NIST §§3.2.1, 3.5–3.6.)*

The draft remains unchanged for its normal approval route. Management retains approval decisions; a person must check these comparisons against the authoritative sources, with information security and document owners involved in the relevant technical and supporting-document questions.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
Chief Operating Officer answers these, legal or compliance the marked points.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md'`
- command_execution: `/bin/bash -lc "sed -n '1,100p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; rg -n '"'^#{2,4} '"' .agents/ski`
- command_execution: `/bin/bash -lc "sed -n '178,370p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md"`
- command_execution: `/bin/bash -lc "sed -n '130,277p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md"`
- command_execution: `/bin/bash -lc "sed -n '369,590p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md"`
- command_execution: `/bin/bash -lc "sed -n '426,496p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md"`
- command_execution: `/bin/bash -lc "sed -n '496,605p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md"`
- command_execution: `/bin/bash -lc "rg -n '"'^#{2,4} '"' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md"`
- command_execution: `/bin/bash -lc "sed -n '619,753p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md"`
- command_execution: `/bin/bash -lc "sed -n '492,573p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md"`
- command_execution: `/bin/bash -lc "sed -n '821,949p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md"`
- command_execution: `/bin/bash -lc "sed -n '590,740p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md"`
- command_execution: `/bin/bash -lc "sed -n '741,900p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md"`
- command_execution: `/bin/bash -lc "sed -n '901,1046p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md"`
- command_execution: `/bin/bash -lc "sed -n '829,852p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '887,909p' .agents/skil`
