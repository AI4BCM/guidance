# $check-against-standards case 1, run1: Codex, guidance at 6d0d3fb

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a1015f-7005-7ea0-8193-cf713cc35827`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I’ll use the check-against-standards skill to review the draft and raise questions for its owner before board approval. I’ll first check the intake requirements and available source texts.

What data classification does the draft policy contain?
- Public
- Internal
- Confidential
- Restricted

The skill’s [preflight instructions](.agents/skills/check-against-standards/preflight.md) say: “Until the person answers, open or read no attached file.” I’m waiting for the data classification before opening the draft.

What data classification does the draft contain: **Public, Internal, Confidential, or Restricted**?

The skill’s [preflight instructions](.agents/skills/check-against-standards/preflight.md) require your answer before I open the attachment.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g 'bc-policy-draft.md' -g '*.md' .agents/skills/check-against-standards"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/SKILL.md .agents/skills/check-against-standards/preflight.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/units/data-rules.md .agents/skills/check-against-standards/units/stages/govern.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/literature/README.md .agents/skills/check-against-standards/units/keep-it-running.md'`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I’ll use your stated classification, medium, and your confirmation that this environment is approved for high-sensitivity material. I’ll now read the draft and check what remains to be clarified for the review.

Which frameworks should I compare the draft against? The shipped texts include DORA, Delegated Regulation (EU) 2024/1774, NIST SP 800-34 Rev. 1, NIST CSF 2.0, FONES ICT resilience guidance and UK organisational resilience guidance. ISO 22301 needs your own copy with its licence confirmed.
- DORA and Delegated Regulation (EU) 2024/1774
- NIST SP 800-34 Rev. 1 and NIST CSF 2.0
- FONES ICT resilience guidance

Which parts of the selected frameworks should the review cover?
- All provisions relevant to this business continuity policy
- Only BIA, testing, recovery objectives and policy review

The draft is **version 0.4, dated 3 September 2026**, owned by the **Chief Operating Officer**.

Which frameworks and parts should I review? For example, **DORA and Delegated Regulation (EU) 2024/1774**, covering all provisions relevant to this policy.

The skill’s [intake instructions](.agents/skills/check-against-standards/units/stages/govern.md) require “the frameworks the document owner selects” and say “Wait for my answers.” The draft does not specify them.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat bc-policy-draft.md'`

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

I’ll review the full draft against DORA and NIST SP 800-34 Rev. 1 in separate sections, with each issue framed as a question for the COO. I’ll mark DORA points for legal or compliance review and flag any limits in the shipped source texts.

The main questions concern testing frequency and method, the BIA’s coverage, recovery objectives and review triggers. DORA also distinguishes exempted payment institutions under Article 16; the draft’s description as “small” does not establish which regime applies. I’ll keep the findings for Articles 5–15 conditional on legal or compliance confirming that point.

[bc-policy-draft.md](bc-policy-draft.md) — version 0.4; 3 September 2026; draft for the management board; owner: Chief Operating Officer.
[DORA source file](.agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md) — Regulation (EU) 2022/2554, as adopted; Official Journal 27 December 2022; retrieved 10 September 2026.
[NIST source file](.agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md) — SP 800-34 Rev. 1, May 2010, with publisher’s errata; retrieved 10 September 2026; Executive Summary and Chapters 1–5 only.

**Draft review — questions for the COO**

The questions needing particular attention before board consideration concern testing, recovery objectives, BIA coverage and management oversight. References below use the two framework files linked above. An omission from this policy does not establish that the organisation lacks the corresponding arrangements.

**DORA**

Every point marked **[L/C]** needs legal or compliance review. Findings against Articles 5–15 are conditional on confirmation that the Article 16 simplified regime does not apply.

1. **Applicability gap — header [L/C].** Article 16(1) excludes “payment institutions exempted pursuant to Directive (EU) 2015/2366” from Articles 5–15. The header describes a small payment institution but does not establish its regulatory status. **COO: can legal or compliance confirm the jurisdiction, authorisation and exemption status, and which DORA regime applies?** “Small” alone does not settle this question.

2. **Testing contradiction — §5 [L/C].** The draft says: “Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through.” Article 11(6)(a) requires testing “at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions”. Article 24(6) also requires appropriate annual tests of systems supporting critical or important functions. **COO: how will the two-year schedule be reconciled with the applicable annual and change-triggered requirements?**

3. **Testing-method gap — §5 [L/C].** Article 11(6) includes “scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity”. The draft specifies only a desktop walk-through. Articles 24(4)–(5) also address independent testing, remediation and validation. **COO: where are operational switchover scenarios, crisis-communication tests, independent testers and follow-up arrangements specified?**

4. **BIA coverage gap — §4 [L/C].** Article 11(5) says the BIA must consider “business functions, support processes, third-party dependencies and information assets, and their interdependencies”, using quantitative and qualitative criteria and appropriate scenario analysis. Section 4 names payment services and customer support without these dimensions. **COO: will the BIA cover the full dependency chain, severe disruption scenarios and the alignment of ICT design and redundancy with its results?** Article 11(5) does not itself specify an annual BIA; the three-year interval should not be described as a direct frequency contradiction.

5. **Recovery-objective gap — §6 [L/C].** The draft says: “The IT manager sets the recovery time objectives for all systems.” Article 12(6) addresses “the recovery time and recovery point objectives for each function” and requires consideration of criticality, market impact and agreed service levels in extreme scenarios. **COO: who establishes and agrees function-level objectives, including recovery point objectives, and how are system targets derived from them?**

6. **Governance gap — §3 and header [L/C].** Article 5(2)(e) requires the management body to “approve, oversee and periodically review” the ICT continuity policy and response and recovery plans. Section 3 names operational owners but gives no counterpart for that oversight, resource allocation or independent assurance. **COO: where are board accountability, reporting, budget decisions and the independent control and audit roles documented?** References: Articles 5(2), 6(4)–(7), 11(3).

7. **Scope gap and ambiguity — §2 [L/C].** The draft says: “the marketing website is not.” Article 8(1) addresses “all ICT supported business functions” and their supporting assets and dependencies. **COO: does this exclusion apply only to continuity planning, and what analysis establishes whether the website shares infrastructure, data or communications dependencies with payment services?** A BC policy exclusion does not settle the scope of the wider ICT risk framework.

8. **Response, communications and records gap — §§1, 3, 5 [L/C].** Article 11(2)(c) requires arrangements to “activate, without delay, dedicated plans”; Article 14(1) requires “crisis communication plans”. The draft mentions recovery plans but gives no activation, containment, crisis-management, notification or recordkeeping arrangements. **COO: which controlled documents cover these responsibilities, incident classification, authority and client reporting, accessible disruption records, and impact and loss estimates?** References: Articles 11(2), 11(7)–(10), 14, 17–19 and 23.

9. **Backup and restoration gap — §§3, 6 [L/C].** Article 12(1)(a) requires backup policies specifying “the scope of the data that is subject to the backup and the minimum frequency of the backup”. No counterpart is identified in the draft. **COO: where are backup scope and frequency, secure restoration, segregation, redundant capacity, restoration tests and data-integrity reconciliations governed?** References: Article 12(1)–(4), (7).

10. **Review and learning gap — §7 [L/C].** The draft says: “The policy owner reviews this policy every three years.” Article 11(6) requires reviews taking account of tests, audit recommendations and supervisory reviews; Article 13(2) requires post-incident reviews. Article 6(5) separately requires at least annual review of the wider ICT risk framework, subject to its exceptions. **COO: what triggers earlier policy and plan reviews, and where are lessons, staff training and management reporting assigned?** The framework’s annual review and this policy’s review are different objects; the draft does not explain their relationship.

11. **Supplier-continuity gap — §§2–5 [L/C].** Article 28(8) requires “comprehensive, documented” exit plans that are sufficiently tested and periodically reviewed. Article 30(3)(c) addresses providers’ tested business contingency plans. The draft contains no supplier counterpart. **COO: which arrangements cover provider dependencies, failure and concentration risks, continuity commitments, data recovery, alternative providers and tested transitions?** References: Articles 8(5), 11(4), 28–30.

**NIST SP 800-34 Rev. 1**

NIST §1.3 allows private and commercial organisations to use its concepts. Its federal requirements and examples need an explicit adoption decision for this institution.

1. **Policy-content gap — §§1–3.** Section 3.1 lists policy elements including “Resource requirements”, “Training requirements” and “Minimum frequency of backups and storage of backup media”. These have no counterpart in the draft. **COO: where will the policy establish or reference those elements and senior-management support?**

2. **BIA gap — §4.** Section 3.2 describes three activities: determining recovery criticality, identifying resources and establishing recovery priorities. **COO: how will the BIA identify system components, facilities, personnel, data and interdependencies, then establish recovery sequencing?** Section 3.6 says: “When a significant change occurs, the BIA should be updated with the new information”. **Will changes trigger an update before the scheduled three-year cycle?**

3. **Recovery-objective gap — §6.** Section 3.2.1 calls for work “with the process owners, leadership and business managers” to determine acceptable downtime, and distinguishes MTD, RTO and RPO. **COO: how will business owners and management establish tolerable disruption and data loss, and validate that IT recovery targets support them?**

4. **Testing ambiguity — §5.** Section 3.5.3 says a tabletop exercise “does not involve deploying equipment or other resources”. Section 3.5.4 recommends functional exercises for moderate-impact systems and full-scale functional exercises for high-impact systems. **COO: what system-impact assessment supports a desktop-only approach, and how will technical recovery be demonstrated?** These system-impact categories are separate from your stated data classification. NIST’s detailed guidance uses an organisation-defined testing frequency; its §3.1 sample policy’s annual schedule is not a universal rule.

5. **Training and follow-up gap — §§3, 5.** Section 3.5.2 says: “Training should be provided at least annually.” Section 3.5 calls for after-action reports and corrective actions. **COO: who owns role-specific training, induction for new recovery personnel, exercise objectives and the closure of lessons identified?**

6. **Activation and staffing gap — §3.** Section 4.2.1 says activation criteria “should be stated in the contingency planning policy”. Section 3.4.6 addresses recovery teams and alternate personnel. **COO: who can activate plans, under what conditions, and who covers unavailable decision-makers and recovery staff?**

7. **Strategy and plan-content gap — §§3, 6.** Sections 3.3–3.4 address preventive controls and recovery strategies; Chapter 4 distinguishes activation/notification, recovery and reconstitution. Chapter 5 addresses platform-specific recovery, backup security and alternate facilities. **COO: which controlled plans document BIA-based strategies, dependencies, secure backups, alternative processing, recovery procedures and validation before returning to normal operations?**

8. **Maintenance gap — §7.** Section 3.6 recommends review “whenever significant changes occur to any element of the plan” and controlled distribution. The draft specifies only policy review. **COO: what governs plan maintenance, more frequent contact-list updates, version control, coordination with related plans and access to copies during a disruption?**

**Gaps and review boundaries**

- **Intake statements:** you stated the data class is medium, this environment is approved for high, and selected DORA and NIST SP 800-34 in full. These are your statements, not documentary evidence.
- **Draft status:** version 0.4 remains a draft dated 3 September 2026. It was reviewed as supplied, without alteration or approval. **COO: what review date and approval record will document the eventual management decision?**
- **Regulatory status:** jurisdiction, authorisation, exemption status and any authority designation for threat-led penetration testing are not in the sources about this organisation. **COO and legal/compliance: what records settle these points?** References: DORA Articles 2, 16 and 26.
- **Source coverage:** DORA’s shipped text is the adopted enacting terms, without recitals; current consolidation and applicable technical standards were not established. NIST appendices and figures are not shipped and were **not reviewed**. **COO: who will verify the source versions and complete these checks?**
- **Unselected frameworks — not reviewed:** Delegated Regulation (EU) 2024/1774, ISO 22301, NIST CSF 2.0, NIST AI RMF and Generative AI Profile, FONES, UK organisational resilience guidance, the AI Act, ESAs frontier-AI statement, and the shipped NCSC, OWASP and UK AI Playbook texts.
- Only the policy was supplied. Supporting plans, inventories, BIA records, contracts, tests and approvals were **not reviewed**. Their absence here is not evidence that they do not exist.

Each point needs human checking against the source text. The draft enters the normal approval route with its status unchanged; management retains the policy decision.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
Chief Operating Officer answers these, legal or compliance the marked points.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md'`
- command_execution: `/bin/bash -lc "sed -n '175,440p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md"`
- command_execution: `/bin/bash -lc "rg -n '"'^#|annually|annual|policy|recovery time objective|recovery point objective'"' .agents/skills/check-against-standards/literature/nist/sp-`
- command_execution: `/bin/bash -lc "sed -n '1,74p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '434,502p' .agents/skills/`
- command_execution: `/bin/bash -lc "sed -n '140,175p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '303,382p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '274,298p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '431,510p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '434,449p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '502,541p' .agents/skil`
