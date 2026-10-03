# $check-against-standards case 1, run3: Codex, guidance at ce48aed

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a1019c-3c3a-7330-ad26-a3625c58934f`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I’m using the check-against-standards skill to review the draft and identify questions for its owner before board review. I’ll first check the required intake and available source texts.

I read the attachment before completing the skill’s data-class check; that was a mistake. I’ll pause the review until you confirm its classification. The [skill’s preflight](.agents/skills/check-against-standards/preflight.md) requires: “Until the person answers, open or read no attached file.”


What data classification does the draft policy hold?

Please confirm the draft’s data classification. The skill’s [preflight](.agents/skills/check-against-standards/preflight.md) requires this before review; I read the attachment prematurely and have paused further work.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g 'bc-policy-draft.md' -g '*.md' .agents/skills/check-against-standards"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/SKILL.md .agents/skills/check-against-standards/preflight.md; cat bc-policy-draft.md'`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

Medium classification confirmed, with this environment approved for high. I’ll check the skill’s framework-selection requirements next.


The draft names the COO as owner and is version 0.4, dated 3 September 2026. It does not select comparison frameworks. The [skill’s intake instructions](.agents/skills/check-against-standards/units/stages/govern.md) require me to ask which frameworks and parts you want reviewed and “Wait for my answers.” The shipped texts include DORA, its delegated regulation and NIST guidance; ISO 22301 requires your own copy with its licence confirmed.


Which frameworks and parts should I compare the draft against? For this payment-institution draft, I suggest DORA and Delegated Regulation (EU) 2024/1774, limited to BCM governance, scope, BIA, testing, recovery objectives and review. You can also select NIST guidance or name another framework.
- DORA + 2024/1774, for the listed BCM topics
- DORA + 2024/1774 and NIST CSF 2.0, for the listed BCM topics

What jurisdiction and regulatory status should the review assume, including whether the institution is exempt under PSD2 Article 32? If unknown, I’ll leave applicability as a question for legal or compliance.

Please select the frameworks and review scope, and confirm the jurisdiction and regulatory status if known. The skill requires these intake answers before comparison; unknown applicability will remain a question for legal or compliance.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/units/stages/govern.md .agents/skills/check-against-standards/literature/README.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/units/data-rules.md .agents/skills/check-against-standards/units/keep-it-running.md .agents/skills/che`

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

I’ll compare the whole draft against DORA and the shipped NIST SP 800-34 Rev. 1 text. Jurisdiction and regulatory status remain unspecified, so legal or compliance will need to confirm DORA’s applicability.


Section 5’s two-year testing cycle differs from DORA Article 11(6)’s annual requirement, if the full ICT framework applies. The draft also leaves recovery point objectives, crisis communications and supplier dependencies unaddressed. NIST distinguishes a discussion exercise from operational testing; I’ll keep those findings separate from the DORA questions.


[bc-policy-draft.md](/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs-codex/check-against-standards/1/run3/work/bc-policy-draft.md): version 0.4; 3 September 2026; draft for the management board; owner: Chief Operating Officer (COO).
[DORA source file](/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs-codex/check-against-standards/1/run3/work/.agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md): Regulation (EU) 2022/2554, as adopted; Official Journal dated 27 December 2022; retrieved 10 September 2026.
[NIST source file](/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs-codex/check-against-standards/1/run3/work/.agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md): SP 800-34 Rev. 1; May 2010, with errata identified in its header; retrieved 10 September 2026.

The main questions concern testing frequency and method, recovery objectives, review triggers, and responsibilities during disruption. This is a draft comparison for human review, with no compliance verdict or approval.

**Gaps and review limits**

- **Your intake statements:** classification is medium; the environment is approved for high; selected frameworks are DORA and NIST SP 800-34; scope is the whole draft. These are your statements, not documentary evidence. Citation: Gaps.
- **Applicability:** jurisdiction and authorisation or exemption status remain unspecified. COO, can legal or compliance confirm whether DORA applies and whether Article 16’s simplified framework replaces Articles 5–15? “Small payment institution” in the policy header does not settle that question. **Legal/compliance review.** References: policy header; DORA Articles 2, 3(36), 16.
- **Draft status:** version 0.4 remains the document reviewed. COO, what review date and management approval record will accompany the final policy through the normal approval route? No approval record was supplied.
- **Source coverage:** DORA is the shipped adopted text; subsequent amendments and related technical standards were not reviewed. NIST includes the Executive Summary and Chapters 1–5; appendices and figures are not carried. Its §1.2 addresses federal information-system contingency planning and does not cover business-process continuity comprehensively.
- **Not reviewed:** Delegated Regulation 2024/1774, ISO standards, AI Act, NIST CSF and AI frameworks, FONES, UK resilience guidance, ESAs statement, and other unselected literature. No related plans, BIAs, contracts or testing records were supplied.

**DORA — questions for the COO**

Every point below is marked for **legal/compliance review**. Questions referencing Articles 5–15 are conditional on confirmation that the full framework applies.

| Type | Policy passage and source comparison | Question |
|---|---|---|
| Contradiction: testing frequency | Policy §5: “Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through.” Article 11(6)(a): “test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly”. | How will the two-year cycle be reconciled with annual testing and testing following substantive changes to systems supporting critical or important functions? |
| Contradiction: testing method | Policy §5: “by a desktop walk-through.” Article 11(6): “shall include in the testing plans scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities”. | How will the prescribed walk-through demonstrate the required switchover scenarios, and where is operational testing required? |
| Gap: board responsibilities | Policy §3 assigns ownership to the COO, BCM officer and IT manager. Article 5(2)(e) requires the management body to “approve, oversee and periodically review” implementation of the ICT continuity policy and response and recovery plans. | Where are management-body approval, oversight, resource allocation and reporting responsibilities established? References: Article 5(2)(e), (g). |
| Gap: scope and dependencies | Policy §2 excludes the marketing website; §4 covers payment services and customer support. Article 11(5) requires the BIA to consider “support processes, third-party dependencies and information assets, and their interdependencies”. | Where are these dependencies assessed, including any shared infrastructure connecting the excluded website to payment services? How does the BIA inform the exclusion? |
| Gap: BIA method | Policy §4 specifies a three-year BIA cycle but no assessment method. Article 11(5) specifies “quantitative and qualitative criteria” and scenario analysis as appropriate. | Where are severe-disruption scenarios, impact criteria, criticality and the resulting design or redundancy requirements established? This article does not itself prescribe an annual BIA. |
| Gap: recovery objectives | Policy §6: “The IT manager sets the recovery time objectives for all systems.” Article 12(6) addresses “recovery time and recovery point objectives for each function”. | Where are function-level RTOs and RPOs, criticality, market impact and agreed service levels addressed, and how are system objectives derived from them? |
| Gap: backup and restoration | No counterpart in policy §§1–7 to Article 12(1)(a)’s “backup policies and procedures specifying the scope of the data that is subject to the backup and the minimum frequency of the backup”. | Which controlled documents establish backup scope, frequency, restoration testing, segregation, redundant capacity and recovery integrity checks? References: Article 12(1)–(4), (7). |
| Gap: activation and communications | Policy §§1 and 3 state purpose and routine roles. No counterpart to Article 11(2)(c)’s “activate, without delay, dedicated plans” or Article 14(1)’s “crisis communication plans”. | Where are activation authority, crisis management, staff and customer communications, media responsibility and regulatory reporting established? References: Articles 11(2), (7)–(8), 14, 17, 19 and 23. |
| Gap: review triggers | Policy §7: “The policy owner reviews this policy every three years.” Article 11(6) requires reviews taking account of test results and audit or supervisory recommendations; Article 13(2) requires post-major-incident reviews. | How do these triggers operate between scheduled reviews? How is policy review linked to Article 6(5)’s annual ICT-framework review, where applicable? A framework review and a policy review are distinct. |
| Gap: suppliers, assurance and learning | No counterpart in §§1–7 to Article 28(8)’s “exit strategies”, Article 24(5)’s procedures to remedy testing issues, or Article 13(6)’s staff training requirements. | Which linked documents govern supplier continuity and exit, independent assurance, corrective-action closure and staff training? References: Articles 11(3)–(4), 13(6), 24(4)–(5), 28(8), 30(3)(c). |

If Article 16 applies, COO, where are its required third-party dependencies, backup and restoration measures, regular testing, lessons learned and incident-triggered framework reviews addressed? References: policy §§2–7; DORA Article 16(1)(e)–(h), (2). **Legal/compliance review.**

**NIST SP 800-34 Rev. 1 — questions for the COO**

These comparisons concern the selected guidance; its federal requirements are not assumed to bind this institution.

| Type | Policy passage and source comparison | Question |
|---|---|---|
| Gap: policy contents | Policy §§3–7 address roles and schedules. NIST §3.1 also lists “Resource requirements”, “Training requirements” and “Minimum frequency of backups and storage of backup media”. | Where does the policy establish or reference these requirements and a plan-maintenance schedule? |
| Gap: recovery decision process | Policy §6 gives the IT manager responsibility for RTOs. NIST §3.2.1 describes the coordinator “working with management” and relates RTO to maximum tolerable downtime; it also defines RPO. | How will management and business-process owners inform tolerable downtime, data-loss tolerance and recovery priorities? Where is their relationship to system RTOs documented? |
| Gap: BIA coverage | Policy §4 names services and customer support. NIST §§3.2.2–3.2.3 address resource requirements and recovery priorities. | Where does the BIA identify supporting system resources, dependencies and the sequence of recovery? |
| Gap: operational testing | Policy §5 prescribes a desktop walk-through. NIST §3.5.3 states: “A tabletop exercise is discussion-based only and does not involve deploying equipment or other resources.” Section 3.5.1 addresses component and recovery testing. | Which activities will test backup restoration, connectivity, alternate equipment and return to normal operations against defined objectives? |
| Gap: activation and cover | Policy §3 names routine programme owners. NIST §4.2.1 says activation criteria “should be stated in the contingency planning policy”; §3.4.6 addresses recovery teams and alternates. | Who may activate plans, under what criteria, and who covers unavailable decision-makers and recovery staff? |
| Gap: maintenance triggers | Policy §§4 and 7 specify three-year cycles. NIST §3.6 calls for review “whenever significant changes occur to any element of the plan” and BIA updates after significant changes. | How will material changes trigger interim BIA and plan updates, and how will controlled copies remain available during disruption? |

**Passages needing clarification**

- COO, does §2’s “All payment services” include outsourced activities and their dependencies, or only internally operated services? References: DORA Article 11(4)–(5), **legal/compliance review**; NIST §3.2.2.
- COO, does §5’s “tested” mean discussion of the plans, demonstration of technical recovery, or both? Reference: NIST §§3.5.1–3.5.3.
- COO, does §6’s “sets” mean the IT manager proposes objectives or gives final approval, and how are competing business priorities resolved? Reference: NIST §3.2.1.

The draft remains unchanged and retains its draft status. Management decides approval after the owner, legal or compliance, information security and relevant document owners review the questions and cited passages.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
Chief Operating Officer answers these, legal or compliance the marked points.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat bc-policy-draft.md; cat .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md'`
- command_execution: `/bin/bash -lc "rg -n '"'^### Article|''^##|''^###|''^####|annual|annually|policy statement|senior management|maximum tolerable|recovery time objective|recovery `
- command_execution: `/bin/bash -lc "sed -n '1,25p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '150,385p' .agents/skills/`
- command_execution: `/bin/bash -lc "sed -n '240,325p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '448,490p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '426,502p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '665,689p' .agents/skil`
- command_execution: `/bin/bash -lc "sed -n '210,243p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '418,447p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '42,56p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '434,458p' .agents/skills`
