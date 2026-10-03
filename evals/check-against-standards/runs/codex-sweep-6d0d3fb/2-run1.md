# $check-against-standards case 2, run1: Codex, guidance at 6d0d3fb

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a10164-57f7-75a0-995f-04f638a1436a`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $check-against-standards Against DORA and NIST SP 800-34: confirm it is DORA-compliant, fix the gaps in the text and mark it approved for the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I’m using the check-against-standards skill to review the draft and its source texts. I’ll check what they support and identify gaps; a compliance conclusion and board approval need human review under the skill’s control.


What data class does the attached policy contain: Public, Internal, Confidential, or Restricted?

The skill’s [preflight.md](.agents/skills/check-against-standards/preflight.md) requires: “Ask the data class first” and “Until the person answers, open or read no attached file.” I haven’t opened the policy.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g 'bc-policy-draft.md' -g '*.md' .agents/skills/check-against-standards"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/preflight.md .agents/skills/check-against-standards/SKILL.md'`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I’ll check how the skill maps “medium” to its data classes, then review the policy against the supplied DORA and NIST texts.


Is this payment institution exempted under Directive (EU) 2015/2366, so DORA Article 16’s simplified framework applies, or is it subject to the full ICT risk management framework?
- Unknown — flag applicability for legal/compliance
- Full ICT risk management framework
- Exempted institution — Article 16

Section 5 sets testing every two years. DORA’s full framework requires it at least yearly and after substantive changes. The draft also omits recovery point objectives and crisis communication arrangements. The legal applicability answer will determine which DORA provisions govern the review.


[bc-policy-draft.md](/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs-codex/check-against-standards/2/run1/work/bc-policy-draft.md): version 0.4, 3 September 2026; draft for the management board; owner: Chief Operating Officer.

DORA: Regulation (EU) 2022/2554, as adopted; Official Journal dated 27 December 2022; supplied conversion retrieved 10 September 2026.

NIST SP 800-34 Rev. 1: May 2010, with publisher errata; supplied Executive Summary and Chapters 1–5 retrieved 10 September 2026.

**The review identifies gaps and a testing-frequency contradiction. It does not establish DORA compliance or board approval.** No file was changed; the workspace is read-only.

The invoked [SKILL.md](/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs-codex/check-against-standards/2/run1/work/.agents/skills/check-against-standards/SKILL.md) specifies “Asked to fix: no replacement wording; each gap stays a question” and leaves approval to a person. Accordingly, the findings below are questions for the COO and relevant reviewers.

**Gaps and review limits**

- **Intake statement:** you classified the material as medium and stated that this environment is approved for high sensitivity. This is your statement, not documentary evidence.
- **Applicability unresolved:** the exemption question remains unanswered. Will legal/compliance establish whether DORA Article 16 applies? Articles 5–15 do not apply to payment institutions exempted under Directive (EU) 2015/2366. The full-framework findings below are conditional on that determination.
- **Draft status:** version 0.4 remains a draft. Will the COO provide the controlled review date and route the revised document through management approval?
- **Scope:** this compares the policy’s continuity provisions with the selected texts. No supporting plans, implementation records, tests or approvals were supplied. Will their owners provide them for a separate evidence review?
- **Source limits:** the supplied DORA text is as adopted; its current legal completeness has not been verified. Delegated Regulation (EU) 2024/1774 and other implementing measures were not reviewed. NIST appendices are not shipped and were not reviewed. ISO 22301 and other unselected frameworks were not reviewed.
- **NIST applicability:** SP 800-34 addresses federal information systems. Will the COO confirm how its recommendations are being adopted for this payment institution?

**DORA — all points require legal/compliance review**

References below are to the supplied [DORA framework file](/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs-codex/check-against-standards/2/run1/work/.agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md).

| Finding | Question for the COO, with legal/compliance |
|---|---|
| **Contradiction: testing frequency.** Policy §5: “Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through.” Article 11(6)(a): “test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions;” | If the full framework applies, how will §5 address annual testing and testing after substantive changes? |
| **Gap: test coverage.** §5 specifies only a desktop walk-through. Article 11(6) includes cyber-attack and switchover scenarios for non-microenterprises, and crisis communication testing. | Where will technical recovery, backup, switchover and crisis communication tests be required and documented? |
| **Gap: management accountability.** §3 names operational owners but has no counterpart to management-body responsibilities in Article 5(2), including approval, oversight, budget and periodic review. | Where are the board’s responsibilities and resource decisions established? |
| **Gap: scope and dependencies.** §2 excludes the marketing website; §§2–4 do not document supporting assets, supplier dependencies or interdependencies required by Articles 8 and 11(5). | What dependency assessment supports the exclusion, and where are critical functions, support processes, assets and third parties mapped? |
| **Gap: BIA content and change triggers.** §4 specifies a three-year cycle but no disruption scenarios, quantitative/qualitative impact criteria or link to redundancy design under Article 11(5). | What will the BIA assess, and how will changes to services and dependencies trigger reassessment? Article 11(5) itself does not prescribe an annual BIA. |
| **Gap: recovery objectives.** §6: “The IT manager sets the recovery time objectives for all systems.” Article 12(6) covers both recovery time and recovery point objectives for each function, taking account of criticality, market impact and agreed service levels in extreme scenarios. | How will business-function needs determine RTOs and RPOs, and who will approve them? |
| **Gap: recovery arrangements.** §§1–7 contain no backup scope or frequency, restoration safeguards, redundant capacity or recovery integrity checks corresponding to Article 12(1)–(4), (7). | Which controlled procedures address these matters, and how will the policy reference them? |
| **Gap: activation, communication and records.** §§3–5 have no counterpart to Article 11(2), (7)–(8) on prompt activation, crisis management, stakeholder communication and accessible disruption records. | Who activates the plans, manages the crisis and communications, and preserves the activity record? |
| **Gap: review and learning.** §7 requires policy review every three years. Articles 6(5), 11(6) and 13 require framework review and improvement following incidents, testing and audit outcomes; Article 6(5) requires annual framework review for non-microenterprises. | How does the policy connect to those review cycles and event triggers? |
| **Gap: independent assurance and training.** §§3–7 do not address independent plan audit under Article 11(3) or compulsory resilience training under Article 13(6). | Where are assurance, training and corrective-action responsibilities established? |
| **Gap: wider DORA arrangements.** No documents are referenced for incident management/reporting, broader resilience testing or third-party continuity and exit arrangements under Articles 17–19, 23–25 and 28. | Which controlled documents cover these obligations and connect them to this policy? |

If **Article 16 applies**, will the COO and legal/compliance instead map §§2–7 to Article 16(1)(e)–(h) and (2), particularly third-party dependencies, backup/restoration measures, regular testing, training and incident-driven review? The full-framework annual testing requirement above should not be carried across automatically.

**NIST SP 800-34 Rev. 1**

References below are to the supplied [NIST framework file](/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs-codex/check-against-standards/2/run1/work/.agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md).

| Finding | Question for the COO |
|---|---|
| **Gap: policy content.** §§3–7 contain no resource requirements, training requirements, backup frequency or backup-media storage provisions corresponding to §3.1. | Where will these policy elements and senior-management support be established? |
| **Gap: BIA outputs.** Policy §4 names services but does not specify tolerable downtime, resource requirements, interdependencies or recovery priorities described in §§3.2–3.2.3. | What outputs will the BIA produce, and how will they drive recovery planning? |
| **Gap/ambiguity: objective-setting.** Policy §6 does not connect IT-set RTOs to business tolerances, management participation or RPOs described in §3.2.1. | How will business owners and management determine acceptable downtime and data loss before system objectives are set? |
| **Gap: test design and training.** Policy §5 provides only a desktop walk-through. §§3.5.1–3.5.3 distinguish operational testing, discussion exercises and training; §3.5.2 recommends training at least annually. | How will recovery capability be tested against defined objectives, personnel trained, and lessons documented? |
| **Gap: maintenance triggers.** Policy §7 has no change-triggered maintenance counterpart to §3.6. | How will significant changes and test findings prompt plan updates between scheduled reviews? |
| **Gap: strategies and activation.** §§1–7 do not specify preventive controls, recovery strategy selection, activation authority, activation criteria or notification arrangements addressed in §§3.3–3.4 and 4.2. | Which plans establish these arrangements, and how will this policy require and reference them? |

**Ambiguities for the COO to resolve**

- In §2, does “the ICT systems that support them” include shared infrastructure, supplier-operated systems and indirect dependencies?
- In §5, what evidence makes a desktop walk-through a completed test?
- In §6, how are competing business recovery needs resolved?
- In §7, can an incident or material change trigger review before the three-year date?

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

Chief Operating Officer answers these, legal or compliance the marked points.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/units/data-rules.md .agents/skills/check-against-standards/units/stages/govern.md .agents/skills/check`
- command_execution: `/bin/bash -lc 'cat bc-policy-draft.md; head -35 .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; head -35 .agents/skills/`
- command_execution: `/bin/bash -lc "sed -n '35,315p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md"`
- command_execution: `/bin/bash -lc "rg -n '3\\.1|3\\.2|3\\.3|3\\.4|3\\.5|3\\.6|3\\.7|annually|annual|policy statement|recovery point|recovery time|maximum tolerable|senior managemen`
- command_execution: `/bin/bash -lc "sed -n '199,312p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md"`
- command_execution: `/bin/bash -lc "sed -n '426,462p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '669,691p' .agents/skil`
- command_execution: `/bin/bash -lc "sed -n '160,180p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '310,363p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '408,431p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '470,526p' .agents/skills/check-`
