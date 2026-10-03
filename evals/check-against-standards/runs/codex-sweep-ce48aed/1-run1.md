# $check-against-standards case 1, run1: Codex, guidance at ce48aed

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a1019a-db18-7313-88b1-24863626f003`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I’m using the check-against-standards skill to review the draft and identify questions for its owner before board submission. I’ll first check the review instructions, policy details, and available sources.

What data sensitivity class does the draft policy contain?

The skill’s [preflight.md](.agents/skills/check-against-standards/preflight.md) requires: “Until the person answers, open or read no attached file.” I haven’t opened the policy.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g 'bc-policy-draft.md' -g '*preflight*' -g 'SKILL.md' -g 'README.md' -g 'govern.md' -g 'data-rules.md' -g '*princ`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/preflight.md .agents/skills/check-against-standards/SKILL.md'`
- command_execution: `/bin/bash -lc "rg --files -g AGENTS.md -g bc-policy-draft.md -g '*intake*' -g '*checklist*' ."`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/units/data-rules.md'`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I’ll treat the policy as medium sensitivity, based on your classification, and proceed in this approved environment. I’ll read the draft and check the framework selection needed for the review.

Which frameworks and parts should I compare the draft against? DORA and Delegated Regulation (EU) 2024/1774 are available with the skill; ISO 22301 would require your copy with its licence confirmed.
- DORA and Delegated Regulation (EU) 2024/1774 — business continuity provisions
- DORA only — business continuity provisions
- NIST SP 800-34 Rev. 1 — chapters 1–5

If you select DORA, what jurisdiction and authorisation status apply to the payment institution, including any exemption relevant to the simplified ICT risk-management framework?

The policy is version 0.4, dated 3 September 2026, marked draft, and owned by the Chief Operating Officer.

Please answer the framework-selection and applicability questions above so I can compare it against the sources you select. The skill requires “the frameworks the document owner selects”; I won’t infer your regulatory obligations from the policy’s header.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/units/stages/govern.md .agents/skills/check-against-standards/literature/README.md .agents/skills/chec`
- command_execution: `/bin/bash -lc 'cat bc-policy-draft.md'`

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

I’ll review the whole policy against DORA and the shipped NIST SP 800-34 Rev. 1 text, which covers chapters 1–5. DORA’s applicability and any exemption remain unconfirmed, so I’ll flag those for legal or compliance review.

The draft’s two-year ICT testing interval differs from DORA’s yearly minimum under the ordinary framework. That point depends on the institution’s authorisation status: Article 16 excludes certain exempt payment institutions from Articles 5–15. I’m also checking the BIA, recovery objectives, review triggers, and whether the desktop walk-through provides the testing NIST describes.

Policy: [bc-policy-draft.md](/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs-codex/check-against-standards/1/run1/work/bc-policy-draft.md), version 0.4, 3 September 2026; draft for the management board; owner: Chief Operating Officer.
DORA: [Regulation (EU) 2022/2554](.agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md), adopted text published in the Official Journal on 27 December 2022; retrieved 10 September 2026.
NIST: [SP 800-34 Rev. 1](.agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md), May 2010, with errata identified in the source header; retrieved 10 September 2026; shipped coverage: Executive Summary and chapters 1–5.

**Draft review**

The main questions concern testing frequency and method, business ownership of recovery objectives, BIA coverage, and review triggers. These are questions for the Chief Operating Officer, not a compliance verdict. Absence from this policy does not establish absence elsewhere in the organisation.

**DORA — contradictions and gaps**

Every point below is marked **for legal or compliance review**. Questions concerning Articles 5–15 depend on confirming whether the ordinary or Article 16 simplified framework applies.

1. **Contradiction: testing frequency.** Policy §5 says: “Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through.” DORA Article 11(6)(a) requires testing “at least yearly”; Article 24(6) separately requires appropriate yearly tests of systems and applications supporting critical or important functions for entities other than microenterprises. **COO: how will the two-year interval be reconciled with the applicable testing requirements?**

2. **Gap: testing scope and execution.** Against the same policy passage, Article 11(6) calls for “scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities”. It also requires crisis communication testing and testing after substantive changes. These have no explicit counterpart in §5. **COO: where are these scenarios, operational tests and change-triggered tests required, and does “desktop walk-through” permit them?**

3. **Gap: BIA coverage.** Policy §4 covers “each payment service and the customer support desk”. Article 11(5) includes “support processes, third-party dependencies and information assets, and their interdependencies”, quantitative and qualitative impacts, and scenario analysis. **COO: where are those dependencies, impact criteria and scenarios included, and how do BIA results determine ICT design and redundancy?** Article 11(5) itself does not prescribe an annual BIA.

4. **Gap: recovery objectives.** Policy §6 says: “The IT manager sets the recovery time objectives for all systems.” Article 12(6) addresses “the recovery time and recovery point objectives for each function”, taking account of criticality, market impact and agreed service levels in extreme scenarios. **COO: how are system RTOs linked to business-function objectives, who agrees the service levels, and where are recovery point objectives established?**

5. **Gap: management accountability and assurance.** Policy §3 assigns policy ownership, programme operation and ICT plan ownership. Article 5(2)(e) requires the management body to “approve, oversee and periodically review” implementation; Article 11(3) addresses independent internal audit review of response and recovery plans. **COO: where are board oversight, reporting, resources and independent assurance established?** Being a draft “for the management board” does not describe those continuing responsibilities.

6. **Gap: backups and restoration.** There is no explicit counterpart in §§1–7 to Article 12(1)’s backup scope, minimum frequency, and restoration procedures; Article 12 also addresses restoration testing, segregation, redundant capacity and data-integrity checks. **COO: which controlled policies and plans govern these measures, including reconciliation of recovered payment data?**

7. **Gap: crisis activation, communications and records.** Article 11(2)(c) requires plans that “activate, without delay”; Articles 11(7)–(8) address crisis management and accessible disruption records, while Article 14 addresses crisis communications. Policy §3 names three roles but no activation authority or crisis communication arrangements. **COO: where are activation, escalation, internal and external communications, and disruption recordkeeping assigned?**

8. **Gap: incident classification and reporting.** Articles 17–19 cover incident handling, classification, management escalation and regulatory reporting. Article 23 extends that chapter to operational or security payment-related incidents. No corresponding arrangements are stated in §§1–7. **COO: which incident policy connects continuity activation to classification, client notification and competent-authority reporting, including payment incidents that are not ICT-related?**

9. **Gap: supplier continuity.** Articles 11(4)–(5), 28(8) and 30(3)(c) address outsourced critical functions, dependencies, tested exit plans and supplier contingency obligations. Policy §§2–5 contain no explicit supplier counterpart. **COO: where are provider dependencies, supplier failure scenarios, contractual continuity requirements and exit arrangements governed?**

10. **Gap: review triggers and lessons.** Policy §7 says: “The policy owner reviews this policy every three years.” Article 11(6) requires reviews informed by tests, audits and supervisory reviews; Article 13(2) addresses post-incident improvements. Article 6(5)’s annual review concerns the **ICT risk management framework**, rather than explicitly prescribing an annual review of this individual policy. **COO: does the three-year schedule allow earlier reviews after incidents, tests, audits, supervisory directions and material changes, and how does it connect to framework review?**

11. **Gap: wider DORA arrangements.** DORA also addresses ICT risk governance, asset identification, protection, detection, training and testing assurance in Articles 6–10, 13(6) and 24–25. Policy §1’s continuity purpose has no explicit cross-references to those arrangements. **COO: which companion documents cover them and connect them to this policy?** Legal or compliance should also establish whether the competent authority has selected the institution for Article 26 threat-led penetration testing; that cannot be inferred from its size.

**NIST SP 800-34 Rev. 1 — gaps and challenges**

NIST §§1.2–1.3 identify this as federal information-system guidance whose concepts may be used by commercial organisations. Its federal mandates and example recovery times are not automatically requirements for this institution.

1. **Gap: policy content.** NIST §3.1 lists “Resource requirements”, “Training requirements”, “Plan maintenance schedule”, and “Minimum frequency of backups and storage of backup media”. These have no explicit counterpart in policy §§1–7. **COO: where are resources, recovery-role training, plan maintenance and backup requirements established or referenced?**

2. **Gap: business involvement in recovery objectives.** Policy §6 assigns RTO setting to the IT manager. NIST §3.2.1 calls for determining acceptable downtime “with the process owners, leadership and business managers”, and discusses maximum tolerable downtime, RTO and RPO. **COO: what business-owner participation and management agreement underpin the IT manager’s decisions, and where are tolerable downtime and data loss documented?**

3. **Gap: BIA maintenance and dependencies.** Policy §4 schedules the BIA every three years. NIST §§3.2–3.2.3 address system components, resources, interdependencies and recovery priorities; §3.6 says: “When a significant change occurs, the BIA should be updated with the new information”. **COO: what triggers an earlier BIA update, and how are dependencies and recovery sequencing captured?**

4. **Potential contradiction: desktop testing for every system.** Policy §5 prescribes testing “by a desktop walk-through”. NIST §3.5.4 says a tabletop exercise is sufficient for low-impact systems, while “For moderate-impact systems, a functional exercise at an organization-defined frequency should be conducted”; high-impact systems receive full-scale functional exercises. **COO: how are exercise methods selected according to system impact, and does §5 allow functional recovery testing?** NIST’s broader guidance does not establish a universal annual testing interval; the annual interval in §3.1 appears in its sample policy.

5. **Gap: training, test criteria and corrective action.** NIST §3.5.2 says: “Training should be provided at least annually.” Sections 3.5–3.5.1 address test objectives, success criteria, after-action reports and corrective actions. Policy §5 states only an interval and method. **COO: where are training, measurable test objectives, results and follow-up requirements specified?**

6. **Gap: activation and return to normal operations.** NIST §4.2.1 says activation criteria “should be stated in the contingency planning policy”; §4.4 describes validating recovery and deactivating the plan. Neither is explicit in policy §§1–7. **COO: who can activate the plans, under what criteria, and who authorises return to normal service after data and functionality checks?**

7. **Gap: recovery strategy and technical safeguards.** NIST §§3.3–3.4 and chapter 5 connect preventive controls, backup methods, alternate capabilities and security to BIA results. Policy §3 names an ICT recovery plan owner without specifying that connection. **COO: where are BIA-based strategy selection, recovery capacity, data protection and applicable platform considerations required?**

**Ambiguities to resolve**

- Policy §2 excludes “the marketing website”. **COO: does that exclusion also cover infrastructure, identity services or communications capabilities shared with payment services?** Compare DORA Article 8(1), (4)–(5), **for legal or compliance review**, and NIST §3.2.
- Policy §§4–5 cover different subjects: the BIA covers services and customer support, while testing covers continuity and ICT recovery plans. **COO: how do the two offices and supporting functions enter the BIA and exercise programme?** Compare DORA Article 11(5), **for legal or compliance review**, and NIST §§3.2 and 3.5.
- Policy §6 says the IT manager “sets” RTOs. **COO: does that mean proposes technical targets or makes the final business decision?** Compare DORA Article 12(6), **for legal or compliance review**, and NIST §3.2.1.

**Gaps — intake, sources and review limits**

- **Your statements:** medium sensitivity; environment approved for high sensitivity; selected frameworks: DORA and NIST SP 800-34; “All of it.” **Scope assumption:** the entire policy and all available parts of both selected texts. These scope statements cite **Gaps**, not framework evidence.
- Jurisdiction, authorisation and exemption status remain unanswered. **COO, for legal or compliance review: which regime applies, including Article 16?** Authorisation and supervisory documentation would settle this. The description “small payment institution” does not settle it.
- The reviewed policy remains **draft**, version 0.4, dated 3 September 2026. No approval record, previous policy, dated source register, next review date or companion plans were supplied. **COO: which controlled documents and source register should support the board’s consideration?**
- The DORA source is the adopted enacting text, without recitals; its current consolidated status has not been verified. NIST appendices and figures are not shipped. **COO: which current authoritative editions and missing material should the human reviewers check?**
- **Not selected; not reviewed:** Delegated Regulation (EU) 2024/1774, ISO 22301, the AI Act, NIST CSF 2.0 and AI RMF, FONES ICT resilience guidance, UK organisational resilience guidance, and the ESAs frontier-AI statement. Supplementary DORA reporting deadlines and detailed technical requirements have not been assessed.

The COO should take these questions to legal, compliance, information security and relevant document owners. People must check the statements against the source texts. The policy remains a draft and enters the normal approval route with its status unchanged; approval stays with management.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
Chief Operating Officer answers these, legal or compliance the marked points.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'wc -l .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md .agents/skills/check-against-standards/literature/ni`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md'`
- command_execution: `/bin/bash -lc "rg -n '"'^#|annual|year|business continuity|recovery time|recovery point'"' .agents/skills/check-against-standards/literature/eur-lex/dora-regula`
- command_execution: `/bin/bash -lc "sed -n '1,220p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md"`
- command_execution: `/bin/bash -lc "rg -n '"'^#|annually|annual|policy should|policy shall|RTO|RPO|maximum tolerable|business process owner'"' .agents/skills/check-against-standards`
- command_execution: `/bin/bash -lc "sed -n '137,335p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md"`
- command_execution: `/bin/bash -lc "sed -n '1,74p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '426,450p' .agents/skills/`
- command_execution: `/bin/bash -lc "sed -n '337,445p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '498,583p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '426,502p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '431,480p' .agents/skil`
- command_execution: `/bin/bash -lc "sed -n '502,547p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '821,941p' .agents/skil`
