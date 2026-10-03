# $check-against-standards case 2, run1: Codex, guidance at ce48aed

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a1019f-ec5e-7003-ac1c-9b5307c8501c`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $check-against-standards Against DORA and NIST SP 800-34: confirm it is DORA-compliant, fix the gaps in the text and mark it approved for the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I’m using the check-against-standards skill to inspect the draft and its reference sources. I’ll check what supports a compliance conclusion and board approval, and identify any gaps.


What data classification does the policy material have, and is this environment approved for that class?
- Public; this environment is approved
- Internal; this environment is approved
- Confidential or restricted; approval needs checking

What data classification does the policy have, and is this environment approved for it?

The skill’s [preflight.md](.agents/skills/check-against-standards/preflight.md) says: “Until the person answers, open or read no attached file.” I read the draft too early; I’ve stopped further review pending your answer.

I can assess the text and identify gaps, but a text review cannot establish operational DORA compliance or supply management’s board approval. The workspace is also read-only, so any proposed changes must stay in chat.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g 'bc-policy-draft.md' -g '*.md' .agents/skills/check-against-standards"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/SKILL.md .agents/skills/check-against-standards/preflight.md; cat bc-policy-draft.md'`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I’ll treat the policy as medium-classified material in an environment approved for high. I’ll compare the draft with the supplied DORA and NIST texts and provide proposed wording in chat. Compliance confirmation and board approval still need the responsible human reviewers.


Is the payment institution exempted under PSD2 and therefore subject to DORA’s simplified ICT risk management framework (Article 16)?
- Unknown—flag for legal/compliance review
- No—use the standard framework
- Yes—use the simplified framework

The two-year testing interval conflicts with DORA Article 11’s annual minimum if the standard framework applies. The draft also omits backup controls, crisis communications, board oversight and business-based recovery objectives. Legal/compliance needs to confirm whether Article 16’s simplified framework applies before settling the wording.


Policy reviewed: [bc-policy-draft.md](bc-policy-draft.md), version 0.4, 3 September 2026; draft for the management board; owner: Chief Operating Officer.  
DORA source: Regulation (EU) 2022/2554, as adopted; Official Journal dated 27 December 2022; supplied conversion retrieved 10 September 2026.  
NIST source: SP 800-34 Rev. 1, May 2010, with publisher errata; supplied conversion retrieved 10 September 2026; Executive Summary and Chapters 1–5 only.

**DORA compliance is not confirmed, and board approval has not been recorded.** The draft has material omissions and a testing-frequency conflict under DORA’s standard framework. Proposed corrections follow in chat; the read-only workspace prevents editing the file.

The invoked [skill](.agents/skills/check-against-standards/SKILL.md) requires that “only a person… says that the document meets a framework” and leaves approval to management. Your explicit request for fixes takes precedence over its restriction on replacement wording, so the wording below is provided for human review.

**Gaps affecting the review**

- You stated that the material is medium-classified and this environment is approved for high.
- DORA Article 16 applicability remains unanswered. Legal/compliance must confirm whether the payment institution is exempted under PSD2. The Article 5–15 findings below are conditional on the standard framework applying; having 140 staff does not settle that exemption.
- The policy remains a draft. It has an owner, version and date, but no recorded approval or next review date.
- No implementation evidence accompanied the policy. Policy wording alone cannot establish whether recovery capabilities, tests or governance operate as required.
- DORA amendments and associated technical standards, including Delegated Regulation (EU) 2024/1774, were not reviewed. Other frameworks were not selected and are not reviewed. NIST appendices and figures are outside the supplied source.

**DORA comparison**

References below are to the supplied [DORA text](.agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md). Every point is for the COO to answer and **legal/compliance to review**.

| Policy passage | Gap or contradiction, expressed as an owner question |
|---|---|
| §2: “the marketing website is not” in scope | What documented assessment supports this exclusion, including its dependencies and potential ICT risks? Articles 6(2), 8(1) and 11(6)(a) cover assets, functions and testing more broadly than payment-service recovery alone. |
| §3: COO, BCM officer and IT manager roles | Where are management-body approval and oversight, resource allocation, independent ICT risk control, supplier oversight and independent review of recovery plans established? Articles 5(2)–(3), 6(4)–(7), 11(3). |
| §4: BIA every three years, covering payment services and customer support | How will the BIA assess severe disruption using quantitative and qualitative criteria, support processes, information assets, suppliers and interdependencies? How will annually reviewed classifications and risk scenarios feed it? Articles 8(1)–(2), 11(5). Article 11(5) does not itself prescribe an annual BIA. |
| §5: “tested every two years, by a desktop walk-through” | How will this be corrected against Article 11(6)(a): “at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions”? Where are cyber-attack, switchover and crisis-communication tests included? Article 11(6). |
| §6: IT manager sets system RTOs | How will recovery objectives address each function’s criticality, market impact and agreed service levels, and include RPOs? Article 12(6). |
| §§1–7: no backup or restoration requirements | Where are backup scope and frequency, protected and segregated restoration, redundancy, periodic restoration tests and data reconciliation specified? Article 12(1)–(4), (7). |
| §§1–7: no crisis or incident arrangements | Where are activation, containment, impact estimation, crisis management, accessible incident records, communications and regulatory-reporting interfaces documented? Articles 11(2), (7)–(8), 14, 17 and 19. |
| §7: policy review every three years | How will reviews incorporate tests, audits, supervisory findings and major incidents? Article 11(6) requires regular policy/plan review; Article 6(5) requires at least annual review of the wider ICT risk framework. |
| §§1–7: no training or lessons process | Where are compulsory staff and senior-management training, post-incident reviews and at least annual reporting of relevant findings to the management body established? Article 13(2), (5)–(6). |

**NIST SP 800-34 comparison**

References below are to the supplied [NIST text](.agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md). These are questions for the COO. NIST presents federal-system guidance that private organisations may use; its federal mandates should not automatically be treated as duties of this payment institution.

| Policy passage | Owner question |
|---|---|
| §§2–3: scope and roles | How will the policy establish senior-management support, recovery resources, coordination with related plans, and designated activation authority and succession? §§3.1, 4.1–4.2. |
| §§4, 6: BIA and IT-set RTOs | How will process owners validate tolerable downtime, resource dependencies, recovery priorities and acceptable data loss? How will §6 reflect §3.2.1: “with the process owners, leadership and business managers determine the acceptable downtime”? §§3.2.1–3.2.3. |
| §5: desktop walkthrough only | How will technical recovery tests validate backups, alternate platforms, connectivity and return to normal operations against explicit success criteria? What annual training and role-entry training will recovery personnel receive? §§3.5.1–3.5.2. |
| §§1–7: recovery controls absent | Where are preventive controls, backup and alternate-site strategies, notification, recovery sequencing and reconstitution validation documented? §§3.3–3.4, 4.2–4.4. |
| §7: three-year review | How will plans remain current after significant changes, with contacts checked more frequently and lessons incorporated? §3.6. |

**Proposed replacement policy text — draft for management review**

Retain the owner as Chief Operating Officer. Retain draft status. Leave the revised version, issue date, approval record and next review date for document control to complete.

1. **Purpose and scope.** This policy establishes business continuity and ICT response and recovery arrangements for payment services, card processing, customer support, both offices and their supporting functions, information assets, ICT assets and third-party dependencies. The asset and dependency inventory determines coverage and recovery priority. Any proposed exclusion, including the marketing website, requires a documented assessment of its business role, dependencies and ICT risks.

2. **Governance.** The management board approves and oversees this policy and associated ICT response and recovery plans, and allocates appropriate resources. The COO owns the policy; the BCM officer coordinates the programme; the IT manager maintains technical recovery arrangements. Controlled plans identify business owners, crisis-management and communications responsibilities, activation authority and successors. Independent ICT risk oversight and internal audit arrangements are documented separately.

3. **Business impact analysis.** The BIA assesses severe disruptions using quantitative and qualitative criteria and appropriate scenarios. It maps functions, support processes, information assets, resources, supplier dependencies and interdependencies. It establishes criticality, tolerable downtime, acceptable data loss and recovery priorities. The BCM officer reviews its currency at least annually and after material changes, incidents or relevant test findings. This annual BIA review is a proposed organisational control for management to adopt.

4. **Recovery objectives.** Business and system owners determine recovery requirements from the BIA. The IT manager assesses technical feasibility and dependencies. Controlled plans record approved RTOs and RPOs for functions and supporting systems, account for criticality and market impact, and support agreed service levels in extreme scenarios. Unachievable objectives are escalated for remediation and a documented decision by the responsible risk owner.

5. **Plans, backups and recovery.** Controlled plans specify activation criteria, notification, containment, recovery sequencing, alternate arrangements and return to normal operation. Backup procedures define data coverage, minimum frequency, protection and storage arrangements. Restoration arrangements provide secure segregation from source systems, suitable redundant capacity, periodic testing and validation of data integrity, including transaction reconciliation.

6. **Testing and training.** ICT continuity and response and recovery plans are tested at least annually and after substantive changes to ICT systems supporting critical or important functions. Testing includes cyber-attacks, switchovers, backup restoration, relevant supplier failures and crisis communications. Tests have explicit objectives and success criteria; results and corrective actions are recorded and followed through. Recovery personnel receive annual training and training when appointed; staff and senior management receive training appropriate to their responsibilities.

7. **Communications, review and assurance.** Crisis plans define internal and external communications and interfaces with incident classification and regulatory reporting procedures. Activation and recovery records remain readily accessible. The COO reviews this policy at least annually and following material changes, major incidents, tests, audits or supervisory findings. Lessons update plans and risk assessments. Associated plans undergo independent review, and management receives findings, capability limitations and corrective-action progress.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].  
The Chief Operating Officer answers these, legal or compliance the marked points.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/units/stages/govern.md .agents/skills/check-against-standards/literature/README.md .agents/skills/chec`
- command_execution: `/bin/bash -lc 'rg --files -g AGENTS.md; head -70 .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; head -70 .agents/skills`
- command_execution: `/bin/bash -lc "head -22 .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; rg -n '"'^### Article|''^### 3'"\\.|"'^### 4'"\\`
- command_execution: `/bin/bash -lc "sed -n '130,360p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md"`
- command_execution: `/bin/bash -lc "sed -n '111,165p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '224,286p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '167,201p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '697,730p' .agents/skills/check-`
