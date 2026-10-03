# $check-against-standards case 2, run3: Codex, guidance at 2f85a91

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a101c7-aa21-7102-adfd-4f977778d9e4`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $check-against-standards Against DORA and NIST SP 800-34: confirm it is DORA-compliant, fix the gaps in the text and mark it approved for the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I’m using the check-against-standards skill to review the draft and its available sources. I can identify gaps and suggest text changes, but compliance confirmation and board approval need an authorized human decision. This workspace is read-only, so I can’t save edits to the attached file.


What data classification does the draft hold, and is this environment approved to process that class?

The skill’s [preflight.md](.agents/skills/check-against-standards/preflight.md) requires: “Until the person answers, open or read no attached file.” I haven’t opened the draft. Once confirmed, I can review it against DORA and NIST SP 800-34; compliance confirmation and board approval remain with authorized people.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g 'bc-policy-draft.md' -g '*check-against*' -g 'preflight.md' -g 'README.md' -g 'govern.md' -g 'data-rules.md' -g`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/SKILL.md; cat .agents/skills/check-against-standards/preflight.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/units/data-rules.md; cat .agents/skills/check-against-standards/units/stages/govern.md; cat .agents/sk`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I’ll read the draft and the supplied DORA and NIST texts, then check for gaps and contradictions. The review will distinguish policy wording from evidence needed to support a compliance decision.


Is this payment institution exempted under Article 32 of PSD2, or does it follow DORA’s full ICT risk management framework?
- Not confirmed — review both possible routes conditionally
- Full ICT risk management framework
- Exempted payment institution — simplified framework

Should this review cover the continuity policy against DORA’s continuity-related provisions and NIST SP 800-34 Rev. 1 chapters 1–5, or also identify DORA duties managed in other policies?
- Continuity provisions, with other DORA duties listed as outside this policy review
- Also identify other DORA duties that need linked policies

The draft’s two-year testing schedule conflicts with annual testing requirements under DORA’s full framework. It also omits recovery point objectives, backup controls, crisis communications and board oversight. An exempted payment institution follows a different route, so I’m keeping those findings conditional until its status is confirmed.


Policy: **version 0.4, 3 September 2026; draft for the management board; owner: Chief Operating Officer.**
DORA: **Regulation (EU) 2022/2554, adopted text; Official Journal dated 27 December 2022; supplied conversion retrieved 10 September 2026.**
NIST: **SP 800-34 Rev. 1, May 2010, with publisher errata; supplied Executive Summary and chapters 1–5 retrieved 10 September 2026.**

**I cannot confirm DORA compliance or mark this approved for the board.** The draft contains gaps, and the applicable regulatory route and implementation evidence remain unconfirmed. The file remains unchanged because the workspace is read-only. Proposed corrections appear below for human review.

Your classification statement is **medium**, with this environment approved for **high**.

**Gaps and scope**

- The institution’s exemption status was not answered. Findings against DORA Articles 5–15 are conditional: Article 16 substitutes a simplified framework for exempted payment institutions. Small size alone does not establish that exemption.
- The review assumes continuity-related DORA provisions and the supplied NIST chapters. Other DORA duties, implementing measures—including Delegated Regulation (EU) 2024/1774—and other frameworks are **not reviewed**.
- The policy is a draft. No approved plans, BIA, recovery targets, test results or approval record were supplied. Their absence from this review does not establish that they do not exist.
- The DORA source is the adopted text, not a verified current consolidated legal package. NIST is federal information-system guidance; its federal mandates are not automatically obligations for this payment institution.

**DORA review — every point below requires legal or compliance review**

| Draft passage | Gap or contradiction; question for the COO | Reference |
|---|---|---|
| §3 names the COO, BCM officer and IT manager, with no board responsibilities. | DORA assigns the management body responsibility to “approve, oversee and periodically review” the ICT continuity policy and recovery plans. Where will board oversight, resources and independent assurance be documented? | Supplied DORA file, Articles 5(2), 11(3) |
| §2: “the marketing website is not.” §4 covers payment services and customer support. | Where is the mapping of supporting processes, information assets, suppliers and interdependencies? What evidence supports the website exclusion, including shared infrastructure and crisis communication dependencies? | Articles 8(1), 8(4)–(6), 11(5) |
| §5: “tested every two years, by a desktop walk-through.” | Article 11(6)(a) requires testing “at least yearly, as well as in the event of any substantive changes”. How will the schedule and methods cover cyber-attacks, switchovers and crisis communications? | Article 11(6); also Article 24(6) for annual testing of systems supporting critical or important functions |
| §6: “The IT manager sets the recovery time objectives for all systems.” | Article 12(6) addresses “recovery time and recovery point objectives for each function”. Where will function-level objectives, tolerated data loss, criticality and extreme-scenario service levels be established? | Article 12(6) |
| §§1–7 contain no backup, restoration, activation or crisis communication arrangements. | Which controlled plans will address backup scope and frequency, segregated restoration, redundancy, reconciliation, activation, communications and disruption records? | Articles 11(2), 11(4), 11(7)–(8), 12(1)–(4), 12(7), 14 |
| §7: “reviews this policy every three years.” | Where will event-triggered review and learning from tests, incidents and audits be required? Article 6(5)’s annual requirement concerns the **ICT risk management framework**; Article 11(6) separately requires regular continuity-policy review informed by results. | Articles 6(5), 11(6), 13(2)–(6) |

If Article 16 applies, the COO and compliance must instead resolve how the policy supports supplier-dependency identification, backup and restoration, regular testing, learning, training, and periodic and major-incident review under Article 16(1)(e)–(h) and 16(2). The full-framework annual testing requirement should not be presented as an Article 16 requirement.

**NIST SP 800-34 Rev. 1 review**

| Draft passage | Gap or ambiguity; question for the COO | Reference |
|---|---|---|
| §§3–7 omit resources, training and backup requirements. | How will the policy establish these elements and senior-management support? | Supplied NIST file, §3.1 |
| §4 specifies a three-year BIA cycle; §6 delegates system RTOs to IT. | How will changes trigger reassessment, and how will business owners and management validate tolerable downtime, RTOs, RPOs, resources and recovery priorities? The source does not establish a universal annual BIA requirement. | §§3.2–3.2.3 |
| §5 permits only desktop walk-throughs. | How will testing validate technical recovery? NIST distinguishes discussion exercises from technical tests and describes different exercise depths by system impact. What impact classification and test rationale apply? | §§3.5.1, 3.5.3–3.5.4 |
| §§3 and 7 omit role training and change-triggered plan maintenance. | How will recovery personnel receive at least annual training, and how will significant changes trigger plan updates and controlled distribution? | §§3.5.2, 3.6 |
| No passage addresses activation, recovery sequencing or return to normal operation. | Which linked plans will define activation authority, notifications, recovery procedures, validation and reconstitution? | §§4.2–4.4 |

**Proposed replacement text for §§1–7 — draft for review**

The following proposes **annual internal review and testing as a company policy choice**, pending management agreement. It does not assert that every applicable regulatory route requires that frequency. Retain the existing draft status; document control should assign the revision identifier.

**1. Purpose**

This policy establishes arrangements to maintain payment services during disruption and restore them within approved business recovery objectives. It governs business continuity and associated ICT response and recovery planning.

**2. Scope**

The policy covers payment services, the card processing platform, customer support, both offices, and the supporting processes, personnel, information assets, ICT assets, telecommunications and third-party dependencies identified through the BIA. Any exclusion, including the marketing website, requires a documented assessment of dependencies and disruption impacts before management approval.

**3. Roles and governance**

The Chief Operating Officer owns this policy. The BCM officer coordinates the programme and BIA. The IT manager maintains ICT recovery plans and demonstrates their ability to support approved business objectives.

The management board approves the policy and associated recovery arrangements, oversees implementation and reviews required resources. Management shall confirm activation authority, crisis communication responsibilities, supplier oversight and independent review arrangements in the supporting plans. These assignments remain subject to the normal approval process.

**4. Business impact analysis**

The BCM officer coordinates a BIA covering severe disruption scenarios, quantitative and qualitative impacts, criticality, supporting resources, supplier dependencies and interdependencies. Business owners and management validate the analysis and recovery priorities.

The BIA shall be reviewed annually and after material changes or relevant disruption and test findings. ICT recovery strategies and redundancy shall reflect the approved analysis.

**5. Plans, testing and training**

Controlled continuity and ICT recovery plans shall define activation criteria, escalation and notifications, recovery sequences, crisis communications, alternative operating arrangements, and return to normal operations.

Plans shall be tested at least annually and after substantive changes affecting critical or important functions. Testing shall include risk-appropriate technical recovery, backup restoration, cyber-attack and switchover scenarios, and crisis communications. Desktop exercises shall form part of the programme. Test objectives, results and corrective actions shall be documented, with appropriate independent testing and review.

Recovery personnel shall receive training at least annually and promptly after appointment or material changes to their duties.

**6. Recovery objectives and safeguards**

Business owners and management shall approve tolerable disruption periods, function-level RTOs and RPOs using the BIA. The IT manager shall align system recovery capabilities with those objectives. Targets shall account for criticality, dependencies, tolerated data loss and agreed service levels in severe scenarios.

Supporting procedures shall specify backup scope, frequency, protection and storage; restoration and recovery methods; required segregation and redundancy; and data-integrity checks and reconciliation. Unachievable objectives shall be escalated to management for a documented decision.

**7. Review and document control**

The COO shall review this policy at least annually and after major incidents, material changes, relevant tests, audits or supervisory findings. Supporting plans shall be updated through change control, remain accessible during disruption, and retain version, distribution and change records.

Management approval shall be recorded through the normal approval route. Draft status shall remain until that approval occurs.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
Chief Operating Officer answers these, legal or compliance the marked points.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat bc-policy-draft.md; cat .agents/skills/check-against-standards/literature/README.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md'`
- command_execution: `/bin/bash -lc "sed -n '1,45p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; rg -n '"'^### Article (4|5|6|8|11`
- command_execution: `/bin/bash -lc "sed -n '140,238p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '292,465p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '235,298p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '312,335p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "rg -n '"'^###? |''^#### |annually|annual|senior management|maximum tolerable|recovery point|policy statement|every|periodic'"' .agents/skills/che`
- command_execution: `/bin/bash -lc "sed -n '434,478p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '669,695p' .agents/skil`
- command_execution: `/bin/bash -lc "sed -n '198,210p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '821,874p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '669,674p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '498,517p' .agents/skil`
