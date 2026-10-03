# $check-against-standards case 1, run2: Codex, guidance at 6d0d3fb

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a1015f-973a-7ae0-84cf-e5c98960fa16`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I’m using the check-against-standards skill to review the draft and identify questions for its owner. I’ll first check the review instructions and available framework sources.

What data classification does the draft policy contain (for example, public, internal, confidential, or restricted)?

What data classification does the draft policy contain: public, internal, confidential, or restricted?

The skill’s [preflight.md](.agents/skills/check-against-standards/preflight.md) requires your answer before I open the attached policy: “Until the person answers, open or read no attached file.”

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g 'bc-policy-draft.md' -g '*.md' .agents/skills/check-against-standards"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/SKILL.md .agents/skills/check-against-standards/preflight.md'`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I’ll use medium as the data class and your confirmation that this environment is approved for high. I’ll read the draft and check what review scope still needs to be agreed.

Which frameworks should I compare the draft against? The skill includes DORA, Delegated Regulation (EU) 2024/1774, NIST SP 800-34 Rev. 1, NIST CSF 2.0, FONES ICT resilience, and UK organisational resilience guidance. ISO 22301 requires your own copy and confirmation that its licence permits this use.
- DORA and Delegated Regulation (EU) 2024/1774
- NIST SP 800-34 Rev. 1 and NIST CSF 2.0

Which parts of the selected frameworks should the review cover?
- All provisions relevant to this continuity policy
- Only scope, roles, BIA, testing, recovery objectives, and review

The draft names the Chief Operating Officer as owner and is version 0.4, dated 3 September 2026, with status “draft for the management board.”

Please select the frameworks and review scope in the questions above. DORA and Delegated Regulation (EU) 2024/1774 are available options; applicability would remain for legal or compliance to confirm.

The skill’s [govern.md](.agents/skills/check-against-standards/units/stages/govern.md) requires comparison against “the framework texts I select” and says to “Wait for my answers,” so I need your selection before making findings.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat bc-policy-draft.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/units/stages/govern.md .agents/skills/check-against-standards/units/data-rules.md .agents/skills/check`

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

I’ll review all provisions relevant to the policy in DORA and NIST SP 800-34 Rev. 1, keeping the findings separate. I’ll mark DORA questions for legal or compliance review and flag where the available files limit the comparison.

Section 5’s two-year testing schedule conflicts with DORA’s annual testing wording, if the ordinary ICT risk framework applies. That qualification matters: DORA has a different route for exempted payment institutions, and the draft does not state its authorisation status. NIST also distinguishes tabletop exercises from operational recovery tests; I’ll reflect that distinction in the owner questions.

[bc-policy-draft.md](bc-policy-draft.md) — version 0.4; 3 September 2026; draft for the management board; owner: Chief Operating Officer.
[DORA](.agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md) — Regulation (EU) 2022/2554, as adopted; Official Journal dated 27 December 2022; retrieved 10 September 2026.
[NIST SP 800-34](.agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md) — Revision 1, May 2010, with publisher errata; retrieved 10 September 2026; Executive Summary and Chapters 1–5 only.

The clearest questions before board consideration concern the two-year testing cycle, recovery objectives assigned solely to IT, and missing governance and recovery arrangements. This is a draft review, with no compliance verdict or approval. Every question below is for the Chief Operating Officer.

**Gaps and review boundaries**

- **Your intake statements:** data class medium; environment approved for high; selected frameworks DORA and NIST SP 800-34; scope “All of it.” These define the review scope, not organisational or framework requirements. *(Gaps.)*
- **Draft status:** the header says “Status: draft for the management board.” COO, what approval and effective-date records will establish the final policy, and when is its next review due? The document reviewed remains this draft. *(Policy header; Gaps.)*
- **DORA applicability — legal/compliance review:** the header identifies a payment institution but gives no jurisdiction or authorisation/exemption status. COO, can legal or compliance confirm applicability and whether Article 16’s simplified framework applies? “Small” and 140 staff do not settle the payment-institution exemption question. Findings against Articles 5–15 below are conditional on that determination. *(Policy header; DORA Articles 2(1)(b), 4 and 16(1).)*
- **Source coverage:** DORA’s file contains adopted enacting terms, without recitals; later amendments and supplementary rules have not been established here. NIST’s appendices and figures are absent. COO, which additional approved texts should resolve those limits before reliance on this review? *(Source headers; Gaps.)*
- **Not reviewed:** Delegated Regulation (EU) 2024/1774, AI Act, NIST CSF 2.0, NIST AI RMF, FONES ICT resilience, UK organisational resilience guidance and the ESAs frontier-AI statement were not selected. ISO 22301 was not selected or supplied with licence confirmation. *(Gaps.)*

**DORA comparison**

Every item in this block is marked **legal/compliance review**. References are to the DORA file linked above.

| Type | Policy passage and framework counterpart | Question for the COO |
|---|---|---|
| Contradiction — testing frequency | §5: “Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through.” Article 11(6)(a): “at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions”. | If the ordinary framework applies, how will the two-year schedule be reconciled with annual testing and testing after substantive changes? |
| Gap — testing breadth and follow-up | §5 has no counterpart to Article 11(6)’s “scenarios of cyber-attacks and switchovers” or Article 24(5)’s “prioritise, classify and remedy all issues”. Articles 24(4), 24(6) and 25 also address independence, annual system testing and appropriate test methods. | Where will cyber-attack, switchover, crisis-communication and technical tests be specified, with independent testers and verified corrective actions? Does “desktop walk-through” limit testing to discussion? |
| Gap / ambiguity — review cycle | §7: “The policy owner reviews this policy every three years.” Article 6(5): “reviewed at least once a year”; Article 11(6) also requires policy and plan review using test, audit and supervisory results. | Is §7 intended as the only review trigger? Where are annual framework review and reviews following major incidents, tests, audits or supervisory instructions addressed? The policy-review interval and framework-review interval need distinguishing. |
| Gap — management accountability | §3 names the COO, BCM officer and IT manager, but no board duties. Article 5(2): “define, approve, oversee and be responsible for the implementation”; Article 5(2)(g) addresses budget and Article 6(4) independent control responsibilities. | Where are management-body approval, oversight, risk tolerance, resources, reporting and independent ICT-risk control responsibilities established? |
| Gap — scope and dependencies | §2 excludes the marketing website and includes ICT supporting the named services. Article 8(1): “all ICT supported business functions”; Articles 8(4)–(6) address assets, dependencies and inventories. | What documented assessment supports the website exclusion, including shared infrastructure and dependencies? Where are all ICT-supported functions, assets and third-party dependencies mapped and classified? |
| Gap — BIA content | §4 covers each payment service and customer support. Article 11(5): “quantitative and qualitative criteria” and “support processes, third-party dependencies and information assets, and their interdependencies”. | Where will the BIA address severe disruption scenarios, support processes, dependencies, impact criteria and alignment of ICT resilience with its results? Article 11(5) does not itself establish a fixed annual BIA interval. |
| Gap — recovery objectives | §6: “The IT manager sets the recovery time objectives for all systems.” Article 12(6): “recovery time and recovery point objectives for each function”, considering criticality, market impact and agreed service levels in extreme scenarios. | How will function-level RTOs and RPOs reflect business impacts and agreed service levels, and how will business owners and management participate in their determination? |
| Gap — response and crisis management | §§1 and 3 have no counterpart to Article 11(2)(c)’s “activate, without delay, dedicated plans” or Article 11(7)’s “crisis management function”. Articles 11(2), 11(8) and 14 also cover impacts, communications and accessible activity records. | Where are activation authority, containment, recovery priorities, crisis leadership, impact estimates, communications ownership and disruption records established? |
| Gap — backups and restoration | §§3 and 6 mention recovery plans and RTOs, but not backups. Article 12(1)(a): “the scope of the data that is subject to the backup and the minimum frequency of the backup”; Article 12(7): “multiple checks and reconciliations”. | Which controlled documents establish backup frequency, restoration testing, segregated recovery systems, redundant capacity and data-integrity checks? |
| Gap — incident handling and reporting | §§1–7 contain no counterpart to Article 17(1)’s “detect, manage and notify ICT-related incidents” or Article 19(1)’s reporting of major incidents. Article 23 extends Chapter III to payment-related operational or security incidents. | Where are detection, classification, logging, escalation, client notification and regulatory reporting duties assigned, including payment incidents that are not ICT-related? |
| Gap — supplier continuity | §§2–5 contain no counterpart to Article 28(8)’s “exit strategies” or Article 30(3)(c)’s supplier obligation to “implement and test business contingency plans”. | Where are outsourced critical functions, supplier oversight, concentration risks, contractual recovery commitments and tested exit/transition arrangements addressed? *(Also Articles 5(3), 11(4), 28–30.)* |
| Gap — assurance, learning and training | §§3, 5 and 7 have no counterpart to Article 11(3)’s “independent internal audit reviews”, Article 13(2)’s post-incident reviews or Article 13(6)’s “compulsory modules” for staff training. | Which documents establish independent assurance, audit follow-up, incident lessons, staff and management training, and annual reporting of relevant findings? *(Also Articles 5(4), 6(6)–(7), 13(3)–(6).)* |
| Gap — links to wider ICT controls | §§1–3 contain no counterpart to Article 6(8)’s “digital operational resilience strategy” or Articles 7–10’s capacity, protection, prevention and detection provisions. | Which approved strategy and security policies connect this continuity policy to those arrangements, including incident thresholds and material single points of failure? |

COO, has the competent authority identified the institution for threat-led penetration testing under Article 26, and, if so, where is that programme linked to §5? This is an applicability question, not an assumed testing obligation. **Legal/compliance review.**

The comparison does not treat provisions directed at other entity types, supervisors or EU bodies as requirements to insert into this policy. Article 45’s information sharing is optional; participation would bring its associated conditions and notification duties.

**NIST SP 800-34 Rev. 1 comparison**

NIST §1.3 permits use of its concepts by private organisations. Its federal mandates and FIPS classifications are not established here as binding on this payment institution. The medium classification you supplied is also not a FIPS system-impact classification.

| Type | Policy passage and framework counterpart | Question for the COO |
|---|---|---|
| Gap — policy elements | §§2–5 name scope, roles, BIA and testing. NIST §3.1 also lists “Resource requirements”, “Training requirements”, “Plan maintenance schedule” and “Minimum frequency of backups and storage of backup media”. | Where will these elements be established or referenced, and how will senior management support and coordination with security, facilities and other organisational plans be made explicit? |
| Gap — BIA and recovery priorities | §4 covers services and customer support. NIST §3.2 describes system components, business processes, resources and interdependencies; §3.2.3 describes an “information system recovery priority hierarchy”. | How will the BIA map supporting systems and resources to business impacts and sequence their recovery? |
| Gap / ambiguity — ownership of objectives | §6 gives the IT manager all RTO decisions. NIST §3.2.1 calls for acceptable downtime to be determined “with the process owners, leadership and business managers” and distinguishes MTD, RTO and RPO. | How will business owners’ tolerable downtime and data loss guide system objectives, and who resolves objectives that current recovery capabilities cannot achieve? |
| Gap — test depth | §5 permits only a desktop walk-through. NIST §3.5.1 says testing “should be conducted in as close to an operating environment as possible”; §3.5.4 distinguishes tabletop, functional and full-scale exercises by system impact. | How will test methods reflect each system’s recovery needs and include practical restoration, connectivity and return-to-service checks where appropriate? |
| Gap — training and improvement | §§3 and 5 have no training or corrective-action counterpart. NIST §3.5.2: “Training should be provided at least annually”; §3.5 requires after-action reports and corrective actions. | Where are role-specific training, test objectives, success criteria, after-action reporting and corrective-action ownership established? |
| Gap — maintenance and change triggers | §7 addresses only policy review every three years. NIST §3.6 calls for plan review at an organisation-defined frequency “or whenever significant changes occur to any element of the plan”, and BIA updates after significant change. | Who maintains plans, contact lists and BIAs between policy reviews, and what changes trigger updates and redistribution? |
| Gap — recovery strategy | §§3 and 6 have no counterpart to preventive controls and contingency strategies in NIST §§3.3–3.4, or the technical considerations in Chapter 5. | Which plans document BIA-based choices for backups, alternate facilities, telecommunications, suppliers, redundancy and secure recovery, with resources adequate to deliver them? |
| Gap — activation and completion | §3 assigns plan ownership but not activation authority. NIST §4.2.1 says activation criteria “should be stated in the contingency planning policy”; §§4.3–4.4 cover recovery sequencing, escalation, validation and deactivation. | Who activates the plans, who succeeds them if unavailable, what triggers activation, and who validates recovery and authorises return to normal operation? |

NIST §3.1’s **sample** policy says “The plan recovery capabilities and personnel shall be tested annually.” COO, should that sample commitment be adopted? The two-year interval should be considered against it, while recognising that §§3.5–3.5.4 otherwise describe organisation-defined exercise frequencies.

**Further challenge questions**

- COO, what measurable service level does §1’s “keeps its payment services running” promise during disruption, and how will it relate to recovery priorities and tolerances? *(Policy §1; DORA Articles 6(8)(b), 12(6); NIST §3.2.1. Legal/compliance review for DORA.)*
- COO, how do §3’s BCM programme responsibility and IT recovery-plan ownership divide decisions when business priorities and technical capabilities conflict? *(Policy §3; DORA Article 5(2)(c); NIST §§3.1, 3.4.4. Legal/compliance review for DORA.)*

Management retains approval and policy decisions through the normal approval route. The COO should take the relevant questions to legal, compliance, information security and the supporting document owners; a person must check each finding against the source text.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. _____ reviewed it on _____.
Chief Operating Officer answers these, legal or compliance the marked points.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md'`
- command_execution: `/bin/bash -lc "rg -n '"'^### Article|''^## CHAPTER'"' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md"`
- command_execution: `/bin/bash -lc "rg -n '"'^#|annually|annual|policy|RTO|RPO|MTD'"' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- command_execution: `/bin/bash -lc "sed -n '137,298p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md"`
- command_execution: `/bin/bash -lc "sed -n '1,74p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '600,710p' .agents/skills/`
- command_execution: `/bin/bash -lc "sed -n '247,292p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '312,335p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "head -n 20 .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '751,805p' .agents/skills/chec`
- command_execution: `/bin/bash -lc "sed -n '235,247p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '292,298p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '747,752p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '434,453p' .agents/skil`
- command_execution: `/bin/bash -lc "sed -n '519,585p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '747,750p' .agents/skills/check-`
