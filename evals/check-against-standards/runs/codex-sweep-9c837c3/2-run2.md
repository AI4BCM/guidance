# $check-against-standards case 2, run2: Codex, guidance at 9c837c3

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a10140-9675-7851-88aa-ab0a205c01ac`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $check-against-standards Against DORA and NIST SP 800-34: confirm it is DORA-compliant, fix the gaps in the text and mark it approved for the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I’m using the check-against-standards skill to review the draft and identify wording gaps against DORA and NIST SP 800-34. I’ll first read its preflight instructions and the available framework sources.

What data class does bc-policy-draft.md contain, and is this environment approved to handle it?
- Public; this environment is approved
- Internal; this environment is approved
- Confidential or restricted; approval needs checking

I need the data classification and environment approval before opening the policy. The skill’s [preflight.md](.agents/skills/check-against-standards/preflight.md) requires: “Until the person answers, open or read no attached file.”

Once answered, I can review the sources and propose revised wording in chat. This workspace is read-only, so I cannot save edits. A policy-text review also cannot establish DORA compliance or supply management’s board approval.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g 'bc-policy-draft.md' -g '*.md' .agents"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/preflight.md .agents/skills/check-against-standards/units/stages/govern.md .agents/skills/check-agains`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/units/data-rules.md'`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I’ll review the policy using your stated classification and environment approval, then provide proposed wording for the gaps. Compliance confirmation and board approval will need a person’s review of the evidence and management’s decision.

Has legal or compliance determined whether the payment institution falls under DORA’s standard ICT risk framework or the simplified framework in Article 16?
- Not yet determined; show the applicability question
- Standard framework applies
- Article 16 simplified framework applies

The draft requires testing every two years using only a desktop walk-through. DORA’s standard framework requires annual testing, testing after substantive ICT changes, and scenarios covering cyber-attacks and switchovers. The draft also omits backup arrangements, recovery point objectives, crisis communications and board oversight. These findings remain conditional on whether Article 16’s simplified framework applies.

Policy reviewed: **bc-policy-draft.md**, version 0.4, 3 September 2026; draft for the management board; owner: Chief Operating Officer.  
DORA source: **Regulation (EU) 2022/2554**, as adopted; Official Journal dated 27 December 2022; retrieved 10 September 2026; shipped file `literature/eur-lex/dora-regulation-2022-2554.md`.  
NIST source: **SP 800-34 Rev. 1**, May 2010 with publisher errata; Executive Summary and Chapters 1–5 only; retrieved 10 September 2026; shipped file `literature/nist/sp-800-34r1-contingency-planning-body.md`.

**The draft contains gaps and a testing-frequency contradiction. I cannot confirm DORA compliance or mark it board-approved from this policy alone.** Proposed replacement wording follows; the file remains unchanged because this workspace is read-only.

**DORA review**

Each question below is for the **Chief Operating Officer**, with **legal or compliance review required**. References are to the DORA file identified above. Findings under Articles 5–15 are conditional on the standard framework applying.

| Draft passage | Source comparison and question |
|---|---|
| §5: “Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through.” | **Contradiction:** Article 11(6)(a) requires testing “at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions”. Will you replace the two-year interval and require cyber-attack and switchover scenarios under Article 11(6), alongside crisis-communication testing? |
| §3 names the COO, BCM officer and IT manager, but no board duties. | **Gap:** Article 5(2)(e) requires the management body to “approve, oversee and periodically review” implementation of the ICT continuity policy and response and recovery plans. Will you specify management-body accountability, resources, independent ICT risk oversight and independent internal audit review? See Articles 5, 6(4)–(7) and 11(3). |
| §2 excludes the marketing website. | **Gap:** Article 8(1) requires identification and documentation of “all ICT supported business functions”. Will you document the website’s dependencies and risk assessment before deciding its continuity treatment, while keeping it within ICT risk management? |
| §4 covers payment services and customer support. | **Gap:** Article 11(5) requires the BIA to consider “support processes, third-party dependencies and information assets, and their interdependencies”. Will you expand the BIA to these dependencies, severe-disruption scenarios, quantitative and qualitative impacts, and alignment of ICT design with its results? |
| §6: “The IT manager sets the recovery time objectives for all systems.” | **Gap:** Article 12(6) addresses “recovery time and recovery point objectives for each function”. Will you include function-level RTOs and RPOs, criticality, market impact and agreed service levels, with business-owner participation? IT-manager involvement is not itself a contradiction. |
| §§1–7 contain no backup or restoration arrangements. | **Gap:** Article 12(1)(a) requires backup procedures specifying “the scope of the data that is subject to the backup and the minimum frequency of the backup”. Will you require documented backups, secure restoration, appropriate segregation, redundant capacity, periodic restoration testing and integrity checks? See Article 12(1)–(4), (7). |
| §§1–7 contain no crisis activation, communications or reporting arrangements. | **Gap:** Article 11(2)(c) requires entities to “activate, without delay, dedicated plans”. Will you require activation criteria, containment, a crisis management function, stakeholder communications, incident classification, regulatory reporting and accessible disruption records? See Articles 11(2), (7)–(8), 14 and 17–19; payment-related incidents are also addressed in Article 23. |
| §§1–7 contain no supplier continuity arrangements or training. | **Gap:** Article 11(4) expressly covers functions “outsourced or contracted through arrangements with ICT third-party service providers”. Will you address supplier recovery capabilities, contractual continuity provisions, exit arrangements and staff training? See Articles 13(6), 28 and 30. |
| §7: “The policy owner reviews this policy every three years.” | **Gap:** Article 11(6) requires regular policy and plan review informed by tests, audits and supervisory reviews. Article 6(5) separately requires annual review of the ICT risk management framework. Will you add these review triggers and distinguish policy review from framework review? The three-year policy interval alone is not a direct contradiction of an explicit annual policy-review requirement. |

**NIST SP 800-34 review**

These questions are for the **Chief Operating Officer**. NIST’s guide concerns federal information systems; its recommendations need an explicit decision about their use here.

| Draft passage | Source comparison and question |
|---|---|
| §§3–7 provide roles and schedules but omit resources, training and backups. | **Gap:** §3.1 identifies “Resource requirements”, “Training requirements” and “Minimum frequency of backups and storage of backup media” as policy elements. Will you add them and define coordination with related organisational plans? |
| §§4 and 6 omit tolerable downtime, data-loss tolerance, resource dependencies and recovery sequencing. | **Gap:** §3.2.1 says planners should work “with the process owners, leadership and business managers” to determine acceptable downtime. Will you document MTD, RTO, RPO, resource requirements and recovery priorities under §§3.2.1–3.2.3? |
| §5 specifies only a desktop walk-through. | **Gap:** §3.5.1 says each system component should be tested to confirm recovery procedures. §3.5.4 distinguishes tabletop, functional and full-scale exercises by availability impact. Will you select and justify suitable testing for each system, with success criteria and corrective actions? A tabletop exercise is not automatically inadequate for every system. |
| §§1–7 contain no preventive controls, recovery strategies or activation authority. | **Gap:** §§3.3–3.4 cover preventive controls and contingency strategies; §4.2.1 says “the designated authority should activate the plan”. Will you identify preventive measures, recovery arrangements, activation authority, notification procedures and validated return to normal operations under Chapter 4? |
| §7 specifies only a three-year policy review. | **Gap:** §3.6 recommends plan review at an organisation-defined frequency “or whenever significant changes occur to any element of the plan”. Will you add event-driven plan maintenance, controlled distribution and accessible recovery copies? Will you also require annual role training under §3.5.2? |

**Proposed replacement policy text — for owner review**

This wording assumes the **standard DORA ICT risk framework**. It proposes governance arrangements and schedules for management to adopt; it does not record their adoption.

> **Business continuity policy**
>
> **Document control:** Source draft version 0.4, dated 3 September 2026. Proposed revision; status: draft for the management board. Owner: Chief Operating Officer. Revision identifier, issue date and approval record: to be completed through document control.
>
> **1. Purpose**  
> The company maintains business continuity and ICT response and recovery arrangements to sustain critical or important functions during severe disruptions and restore services within documented recovery objectives, while protecting the availability, authenticity, integrity and confidentiality of data.
>
> **2. Scope**  
> This policy covers payment services, card processing, customer support, both offices and their supporting processes, people, information assets, ICT assets and third-party dependencies. All ICT-supported functions are identified and assessed. Continuity treatment of the marketing website is determined from its business impact and dependencies; it remains within ICT risk management.
>
> **3. Governance and responsibilities**  
> The management body approves, oversees and periodically reviews this policy and the ICT response and recovery plans, retains ultimate responsibility for ICT risk and approves appropriate resources. The COO owns the policy; the BCM officer coordinates the programme and BIA; the IT manager maintains ICT recovery arrangements with business owners. Management documents responsibilities for independent ICT risk oversight, crisis management, communications, regulatory reporting, supplier oversight and independent internal audit review. Plans specify activation authority, delegated authority and deputies.
>
> **4. Business impact analysis**  
> The BCM officer coordinates a BIA with business and system owners covering severe-disruption scenarios, quantitative and qualitative impacts, criticality, support processes, information assets, third-party dependencies, resources and interdependencies. The BIA establishes recovery priorities and informs ICT design and redundancy. Its results are reviewed annually and after material changes or incidents that affect its assumptions.
>
> **5. Testing and training**  
> ICT business continuity and response and recovery plans for systems supporting all functions are tested at least annually and after substantive changes to systems supporting critical or important functions. Testing includes cyber-attacks, switchovers, backup restoration and crisis communications. The programme uses risk-based technical and functional tests appropriate to system impact, with defined objectives, success criteria and independent testers. Findings are prioritised, assigned for remediation and validated after correction. Personnel receive role-specific training on appointment and at least annually; staff and management receive suitable resilience and security-awareness training.
>
> **6. Recovery objectives and capabilities**  
> Business owners, leadership and the IT manager determine and document tolerable downtime, function-level RTOs and RPOs, and supporting system recovery objectives from the BIA. Objectives account for criticality, dependencies, potential market impact and agreed service levels in extreme scenarios. Actual recovery capability is tested against these objectives. Capability shortfalls are escalated for remediation and risk-owner decision; regulatory obligations remain applicable.
>
> Documented backup and restoration procedures specify data scope, minimum backup frequency, storage, security and restoration responsibilities. Arrangements provide appropriate redundant capacity and physically and logically segregated systems when restoring backups using the company’s own systems. Recovery includes data-integrity checks and reconciliation between systems.
>
> **7. Response, communications and suppliers**  
> Controlled plans define activation criteria, containment, notification, recovery sequencing, impact and loss assessment, crisis communications and validated return to normal operations. Incident classification and reporting follow controlled procedures identifying the applicable competent authority and reporting obligations. Activity records remain accessible during disruption.
>
> Third-party dependencies are documented and included in continuity arrangements and testing. Relevant contracts address service levels, incident assistance, supplier contingency capabilities, data recovery and applicable oversight rights. Exit strategies and transition arrangements support continuity of critical or important functions.
>
> **8. Review and document control**  
> The COO coordinates annual review of this policy and its associated plans, and additional reviews following relevant changes, major incidents, test findings, audit recommendations or supervisory instructions. The ICT risk management framework is reviewed at least annually. Lessons and corrective actions feed into maintained plans and risk assessments. Controlled copies, change records and supporting recovery information are available to authorised recovery personnel during disruption.

The annual BIA and policy-review schedules above are proposed organisational choices. The selected DORA provisions do not expressly prescribe an annual BIA or annual review of this individual policy.

**Gaps and challenge questions**

- **Applicability — COO; legal/compliance review:** Does the institution have the payment-institution exemption that triggers Article 16? Its description as “small” does not settle this. No intake answer was received; Articles 5–15 findings and replacement wording therefore remain conditional. Article 16 has its own continuity, backup, testing and review requirements.
- **Status — COO:** The document remains a draft dated 3 September 2026. Which revision identifier, review date and approval record will document management’s decision?
- **Scope ambiguity — COO:** Does “All payment services” include outsourced processing and supporting services? What dependency evidence supports excluding the marketing website?
- **Enforceability — COO:** Who decides when activation is required, and what measurable criteria demonstrate successful recovery? §§5–6 currently provide neither test success criteria nor the basis for objectives.
- **Evidence — COO:** Which controlled plans, BIA records, recovery tests, contracts and oversight records support the policy statements? Nothing beyond this policy was supplied.
- **Source coverage — COO; legal/compliance review:** Will you arrange review against current authoritative DORA texts and applicable implementing measures? Delegated Regulation 2024/1774 and other supplementary instruments were not selected and are **not reviewed**. The shipped DORA source is the adopted text, not verified as a complete current regulatory set.
- **NIST scope — COO:** Which federal-system concepts will the organisation adopt voluntarily? NIST appendices were not supplied and are **not reviewed**. Other packaged frameworks, including ISO standards, the AI Act, NIST CSF and AI RMF, are **not reviewed**.
- **Intake — Gaps:** You stated that the material is “medium” and this environment is approved for “high”. This is your handling statement, not a framework source.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].  
The Chief Operating Officer answers these, legal or compliance the marked points.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat bc-policy-draft.md; cat .agents/skills/check-against-standards/units/keep-it-running.md; head -n 32 .agents/skills/check-against-standards/li`
- command_execution: `/bin/bash -lc "sed -n '33,355p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md"`
- command_execution: `/bin/bash -lc "rg -n '"'^3'"\\.|"'^4'"\\.|"'^5'"\\.|policy|annually|annual|maximum tolerable|recovery point|training|activation|reconstitution' .agents/skills/c`
- command_execution: `/bin/bash -lc "sed -n '186,327p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md"`
- command_execution: `/bin/bash -lc "sed -n '437,490p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '615,699p' .agents/skil`
- command_execution: `/bin/bash -lc "sed -n '439,480p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; rg -n '"'^### Article (24|25|2`
- command_execution: `/bin/bash -lc "sed -n '145,174p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '312,337p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '174,185p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '300,312p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '747,767p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '502,527p' .agents/skil`
