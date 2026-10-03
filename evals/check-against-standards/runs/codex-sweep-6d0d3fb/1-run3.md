# $check-against-standards case 1, run3: Codex, guidance at 6d0d3fb

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a10160-d09a-7f12-aff4-fd43a29301e9`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I’m using the check-against-standards skill to review the draft and raise questions for its owner before board submission. I’ll first read the intake requirements and available sources.

What data classification does the draft hold: public, internal, confidential, or high-sensitivity?

The skill’s [preflight.md](.agents/skills/check-against-standards/preflight.md) requires: “Until the person answers, open or read no attached file.” I haven’t opened the draft.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g 'bc-policy-draft.md' -g '*.md' .agents/skills/check-against-standards"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/SKILL.md .agents/skills/check-against-standards/preflight.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/units/data-rules.md'`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I’ll use your medium classification and confirmation that this environment is approved for high-sensitivity data. I’ll read the draft and check what review scope still needs to be selected.

The draft is version 0.4, dated 3 September 2026, owned by the Chief Operating Officer.

Before comparison, please confirm:

1. Which frameworks should I use? For a payment institution, DORA and Delegated Regulation (EU) 2024/1774 are available options. ISO 22301 needs your licensed copy and confirmation that its licence permits this use.
2. Should I review the whole draft or selected sections?
3. Which jurisdiction applies, and is the institution authorised, exempted, or subject to a simplified regime?

The [skill’s intake instructions](.agents/skills/check-against-standards/units/stages/govern.md) require review against “the framework texts I select” and say to “Wait for my answers.” Your selection fixes the review scope.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat bc-policy-draft.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/units/stages/govern.md .agents/skills/check-against-standards/literature/README.md .agents/skills/chec`

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

I’ll review all seven sections against DORA and NIST SP 800-34, with separate findings for each. Jurisdiction and regulatory status remain unanswered, so I’ll leave DORA applicability for legal or compliance to confirm.

The main questions concern biennial testing, the reliance on desktop walk-throughs, recovery objectives set only by IT, and review intervals without change or incident triggers. DORA gives explicit annual testing requirements; NIST makes exercise depth depend on system impact. I’ll distinguish direct contradictions from missing detail and keep the DORA points conditional on the applicable regime.

Policy reviewed: [bc-policy-draft.md](/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs-codex/check-against-standards/1/run3/work/bc-policy-draft.md), version 0.4, 3 September 2026; draft for the management board; owner: Chief Operating Officer.
DORA source: [dora-regulation-2022-2554.md](.agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md), Regulation (EU) 2022/2554, as adopted; Official Journal dated 27 December 2022; retrieved 10 September 2026.
NIST source: [sp-800-34r1-contingency-planning-body.md](.agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md), Revision 1, May 2010, with publisher errata; retrieved 10 September 2026; Executive Summary and Chapters 1–5 only.

**Draft review for the policy owner**

The clearest contradiction concerns testing every two years. Further questions concern practical recovery testing, business involvement in recovery objectives, board accountability, and reviews triggered by changes or incidents. These are questions for human review, with no compliance or approval verdict. References below use the two framework files identified above.

**Gaps in intake and sources**

- Your statements: data classification is medium; this environment is approved for high-sensitivity material; selected frameworks are DORA and NIST SP 800-34; scope is the whole draft. These are intake statements, not framework evidence.
- Jurisdiction and authorisation/exemption status were not supplied. Assumption: DORA is selected for comparison, but its legal applicability remains unresolved. **COO and legal/compliance:** which jurisdiction and regulatory status apply, and does Article 16’s simplified regime replace Articles 5–15? Being described as small does not settle this. *(Policy header; DORA Articles 2, 4 and 16; Gaps.)*
- The policy remains a draft dated 3 September 2026. **COO:** what review date and management approval record will accompany it through the normal approval route? This review leaves its draft status unchanged.
- Only the policy was supplied. **COO:** which controlled plans, procedures or policies would settle the omissions below? Absence from this draft does not establish absence from the organisation.
- The DORA source is the as-adopted text, without a supplied check for subsequent amendments. NIST’s appendices and figures are not carried. **COO and legal/compliance:** which source editions and authoritative texts will the human reviewer confirm before relying on this review?
- Not selected and **not reviewed**: Delegated Regulation (EU) 2024/1774, the AI Act, NIST CSF 2.0 and AI RMF, FONES ICT resilience guidance, UK Organisational Resilience Guidance and the ESAs statement. ISO 22301 was not selected or supplied with licence confirmation and is **not reviewed**.

**DORA comparison**

Every point in this block is marked for **legal or compliance review**. Points citing Articles 5–15 depend on confirmation that the ordinary regime applies.

| Type and policy passage | Question for the Chief Operating Officer | Reference |
|---|---|---|
| **Contradiction — §5:** “Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through.” Article 11(6)(a) requires testing “at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions”. | How will the two-year schedule be reconciled with annual and change-triggered testing? Article 24(6) also requires appropriate annual tests for ICT systems and applications supporting critical or important functions. | Policy §5; DORA Articles 11(6)(a), 24(6). |
| **Gap — §5:** testing is described only as a desktop walk-through. Article 11(6) names “scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities”. | Where will practical switchover, backup and cyber-attack scenarios be specified, alongside crisis communication testing, independent testers and remediation of findings? | Policy §5; DORA Articles 11(6), 24(4)–(5), 25(1). |
| **Gap — §3:** the COO, BCM officer and IT manager are named, without board duties. Article 5(2) says the management body shall “define, approve, oversee and be responsible for the implementation” of ICT risk arrangements. | Where are management-body approval, oversight, reporting, budget responsibilities and independent review of ICT response and recovery plans established? | Policy §3; DORA Articles 5(2), 11(3). |
| **Gap/ambiguity — §2:** “the marketing website is not.” Article 8(1) covers “all ICT supported business functions”. | What documented classification and dependency assessment supports this exclusion, and where is the website covered within the wider ICT risk framework? Does this exclusion mean only exclusion from this BC policy? | Policy §2; DORA Articles 6(2), 8(1), 8(4). |
| **Gap — §4:** BIA covers payment services and customer support. Article 11(5) also identifies “support processes, third-party dependencies and information assets, and their interdependencies”. | Where are severe disruption scenarios, quantitative and qualitative impacts, supporting processes, dependencies and the resulting ICT design requirements addressed? | Policy §4; DORA Article 11(5). |
| **Gap/ambiguity — §§4, 7:** BIA and policy review are scheduled every three years. Article 6(5) requires the ICT risk framework to be reviewed “at least once a year”; Article 11(6) links policy and plan review to tests, audits and supervisory reviews. | How do these three-year cycles connect to annual framework and classification reviews, major incidents, changes and test findings? Article 11(5) does not itself specify an annual BIA cycle. | Policy §§4, 7; DORA Articles 6(5), 8(1)–(3), 11(6), 13(2)–(3). |
| **Gap/ambiguity — §6:** “The IT manager sets the recovery time objectives for all systems.” Article 12(6) addresses “recovery time and recovery point objectives for each function”. | Who establishes function-level recovery objectives, acceptable data loss and business criticality, and how do system objectives support agreed service levels under extreme scenarios? | Policy §6; DORA Article 12(6). |
| **Gap — §§1, 3, 5, 6:** no counterpart for documented backup scope/frequency, secure restoration, redundant capacity or recovery reconciliation. | Which controlled documents establish these arrangements, who owns them, and how will their testing be linked to this policy? | Policy §§1, 3, 5, 6; DORA Article 12(1)–(4), (7). |
| **Gap — §§1, 3:** no counterpart for crisis activation, communication ownership or disruption records. | Where are activation and containment procedures, crisis management responsibilities, internal/external communications, regulatory reporting interfaces and accessible disruption records defined? | Policy §§1, 3; DORA Article 11(2), (7)–(8), Article 14. |
| **Gap — §§2–5:** outsourced services and supplier failure are not addressed explicitly. | Which third-party dependencies support payment services, and where are continuity arrangements, supplier oversight and tested exit/transition plans linked to this policy? | Policy §§2–5; DORA Articles 8(5), 11(4), 28(8). |
| **Gap — §§3, 5, 7:** no training or lessons-to-improvement counterpart. | Where are staff and management training, post-incident learning and annual management reporting on relevant findings established? | Policy §§3, 5, 7; DORA Article 13(2), (5)–(6). |

**NIST SP 800-34 comparison**

NIST §1.2 presents guidance for federal organisations and limits its coverage principally to information-system contingency planning. **COO:** which recommendations will the institution adopt, and how will it document that adaptation? Its federal terminology and obligations do not automatically become requirements for this payment institution.

| Type and policy passage | Question for the Chief Operating Officer | Reference |
|---|---|---|
| **Gap — §§1–3:** purpose, scope and three roles are stated. NIST’s key policy elements include “Resource requirements”, “Training requirements”, “Plan maintenance schedule” and “Minimum frequency of backups and storage of backup media”. | Where will these elements and senior-management support be established or referenced? | Policy §§1–3; NIST §3.1. |
| **Gap — §4:** a service-level BIA is scheduled every three years. NIST describes identifying system components, supported processes, resource requirements and recovery priorities, including reconsideration as system design changes. | How will the BIA connect each supporting system to business impacts, recovery resources, dependencies and priorities, and what changes trigger reassessment between scheduled reviews? | Policy §4; NIST §§3.2–3.2.3. |
| **Gap/ambiguity — §6:** “The IT manager sets the recovery time objectives for all systems.” NIST says the coordinator works “with the process owners, leadership and business managers” to determine acceptable downtime. | How will business owners and management establish maximum tolerable downtime and acceptable data loss, and participate in determining RTOs and RPOs? | Policy §6; NIST §3.2.1. |
| **Contradiction in testing approach — §5:** testing is “by a desktop walk-through”. NIST §3.5.1 says testing “should be conducted in as close to an operating environment as possible”; §3.5.3 says a tabletop “does not involve deploying equipment or other resources”. | Is the walk-through intended as one exercise within a wider testing programme, or the entire programme? How will actual recovery procedures and component operability be tested? | Policy §5; NIST §§3.5.1, 3.5.3. |
| **Gap — §5:** no system impact classification or exercise criteria are stated. NIST §3.5.4 recommends functional exercises for moderate-impact systems and full-scale functional exercises for high-impact systems. | Which impact levels and exercise depths will be adopted, and what supports the chosen frequency? The annual testing wording in §3.1 is a sample policy; §3.5.4 uses an organisation-defined frequency. | Policy §5; NIST §§3.1, 3.5.4. |
| **Gap — §§3, 5:** no training schedule, alternate personnel or activation authority is stated. NIST says training “should be provided at least annually”. | Who can activate recovery, who covers unavailable personnel, and how will role-specific training prepare them? | Policy §§3, 5; NIST §§3.4.6, 3.5.2. |
| **Gap — §7:** policy review is specified, but plan maintenance is not. NIST calls for plan review at an organisation-defined frequency “or whenever significant changes occur to any element of the plan”. | Who maintains the recovery plans, contact details and supporting documents, and how will changes and exercise lessons trigger updates? | Policy §§5, 7; NIST §§3.5, 3.6. |

The COO’s answers should be checked with the BCM officer, IT manager, information security and relevant document owners. Legal or compliance should resolve the marked regulatory points against the source text. Management retains the approval decision; the draft proceeds through the normal approval route with its status unchanged.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
Chief Operating Officer answers these, legal or compliance the marked points.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md'`
- command_execution: `/bin/bash -lc "python - <<'PY'
from pathlib import Path
p=Path('.agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md')
s=p.rea`
- command_execution: `/bin/bash -lc "rg -n '"'^#|annually|annual|policy|RTO|RPO|MTD|senior management'"' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingenc`
- command_execution: `/bin/bash -lc "sed -n '1,68p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '426,502p' .agents/skills/`
- command_execution: `/bin/bash -lc "python3 - <<'PY'
from pathlib import Path
s=Path('.agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md').read_t`
- command_execution: `/bin/bash -lc "python3 - <<'PY'
from pathlib import Path
p=Path('.agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md')
s=p.re`
- command_execution: `/bin/bash -lc "sed -n '1,60p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; rg -n '"'^### 3.6|''^### 3.7|''^#`
- command_execution: `/bin/bash -lc "sed -n '434,450p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '744,780p' .agents/skil`
