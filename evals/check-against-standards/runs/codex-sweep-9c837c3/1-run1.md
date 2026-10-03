# $check-against-standards case 1, run1: Codex, guidance at 9c837c3

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a1013b-5e56-7150-9a2a-fcb50dbf3a94`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I’m using the check-against-standards skill to review the draft and frame findings as questions for its owner. I’ll first check the intake requirements and available source texts.

What data class does the draft policy contain: public, internal, confidential, or restricted?

The skill’s [preflight.md](.agents/skills/check-against-standards/preflight.md) requires: “Until the person answers, open or read no attached file.” I’ll wait for your data classification before opening the policy.

What data class does the draft contain: **public, internal, confidential, or restricted**?

The skill’s [preflight.md](.agents/skills/check-against-standards/preflight.md) says: “Until the person answers, open or read no attached file.” I need your classification before opening the policy.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g 'bc-policy-draft.md' -g '*.md' .agents/skills/check-against-standards"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/SKILL.md .agents/skills/check-against-standards/preflight.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/units/data-rules.md .agents/skills/check-against-standards/units/stages/govern.md .agents/skills/check`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I’ll use your stated classification of medium and approval for high-sensitivity material. I’ll read the draft now and check which framework choices and review scope still need your input.

Which frameworks and parts should I compare against? Available options include DORA (EU 2022/2554), Delegated Regulation EU 2024/1774, NIST SP 800-34 Rev. 1, NIST CSF 2.0, and UK Organisational Resilience Guidance. For this payment-institution policy, I suggest the BCM and ICT continuity provisions of DORA and EU 2024/1774. ISO 22301 requires your own copy with its licence confirmed.
- DORA and EU 2024/1774 — BCM and ICT continuity provisions
- NIST SP 800-34 Rev. 1 — contingency planning provisions
- DORA, EU 2024/1774 and NIST SP 800-34 — BCM and ICT continuity provisions

For a DORA review, has legal or compliance established whether the institution uses the ordinary ICT risk-management framework or the simplified framework under Article 16?
- Not established — flag applicability for legal/compliance
- Ordinary ICT risk-management framework
- Simplified framework under Article 16

The policy is **v0.4, dated 3 September 2026, draft for the management board**, owned by the **Chief Operating Officer**.

Please select the frameworks and review scope. I suggest **DORA and EU 2024/1774’s BCM and ICT continuity provisions**. For DORA, please also confirm whether the ordinary or Article 16 simplified framework applies; “not established” is a valid answer.

The skill’s [governance intake](.agents/skills/check-against-standards/units/stages/govern.md) requires comparison against “the frameworks the document owner selects” and says “Wait for my answers.” Those choices are needed before the comparison.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat bc-policy-draft.md'`

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

I’ll compare the policy against DORA and NIST SP 800-34 Rev. 1 across the supplied texts. I’ll flag DORA applicability for legal or compliance, since “all of it” sets the review scope but doesn’t establish which regulatory regime applies.

The testing clause is a key issue to resolve: it specifies a desktop walk-through every two years, while DORA’s ordinary regime specifies annual continuity testing and cyber-attack and switchover scenarios. NIST also distinguishes discussion exercises from technical recovery tests. I’m checking the remaining governance, recovery and supplier provisions before drafting the owner’s questions.

Policy: [bc-policy-draft.md](/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs-codex/check-against-standards/1/run1/work/bc-policy-draft.md), version 0.4, 3 September 2026; **draft for the management board**; owner: Chief Operating Officer.
DORA: [Regulation (EU) 2022/2554, as adopted](/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs-codex/check-against-standards/1/run1/work/.agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md), Official Journal dated 27 December 2022; retrieved 10 September 2026.
NIST: [SP 800-34 Rev. 1](/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs-codex/check-against-standards/1/run1/work/.agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md), May 2010, with errata identified in its header; retrieved 10 September 2026.

**Draft review — questions for the Chief Operating Officer.** The main issues to resolve before board consideration concern testing, business impact analysis, recovery objectives and management accountability. This review does not determine compliance. All DORA points below are marked for **legal or compliance review**.

### DORA

Articles 5–15 findings are conditional on the ordinary ICT risk-management framework applying; Article 16 applicability remains unresolved.

**Contradiction**

- **Testing frequency — policy §5; DORA Article 11(6)(a).** The policy specifies “tested every two years”; DORA specifies “at least yearly” and testing following substantive changes to systems supporting critical or important functions. **Will the COO reconcile these schedules and include change-triggered testing if this provision applies?**

**Gaps**

- **Testing content — policy §5; DORA Articles 11(6), 24(4)–(6), 25(1).** The policy specifies “a desktop walk-through.” DORA calls for “scenarios of cyber-attacks and switchovers” and appropriate yearly tests of systems supporting critical or important functions, with independent testers and remediation arrangements. **Where will the COO specify these activities, test independence and follow-up, beyond the walk-through?**

- **Board accountability — policy §3; DORA Article 5(2)(a), (e), (g).** DORA gives the management body “the ultimate responsibility” for ICT risk and responsibilities for approving, overseeing and periodically reviewing continuity arrangements and allocating resources. The policy names operational owners but gives no counterpart for these management-body duties. **How will the COO distinguish delegated work from board responsibility, approval, oversight and budgeting?**

- **Scope and dependencies — policy §§2, 4; DORA Articles 8(1), (4)–(6), 11(5).** DORA requires identification of “all ICT supported business functions” and a BIA considering “support processes, third-party dependencies and information assets, and their interdependencies.” **Where will the COO require dependency mapping and explain the exclusion of the marketing website, including any shared infrastructure or communications dependency?**

- **BIA method — policy §4; DORA Article 11(5).** The source calls for “quantitative and qualitative criteria,” internal and external data, and scenario analysis as appropriate. These have no counterpart in §4. **Will the COO specify how impacts, criticality and dependencies determine recovery priorities and redundancy?** Article 11(5) does not itself prescribe a fixed BIA refresh interval.

- **Recovery objectives — policy §6; DORA Article 12(6).** DORA addresses “recovery time and recovery point objectives for each function,” taking criticality and market impact into account. The policy addresses only system RTOs set by IT. **How will the COO connect system targets to function-level RTOs, RPOs and agreed service levels?**

- **Backups and restoration — policy §§3, 6; DORA Article 12(1)–(4), (7).** Source provisions cover “backup policies and procedures,” restoration testing, segregated restoration systems, redundant capacity and data-integrity checks. No counterpart appears in the policy. **Which controlled documents will the COO identify for backup scope and frequency, secure restoration, redundancy and reconciliation of recovered payment data?**

- **Activation and crisis communications — policy §§1, 3; DORA Articles 11(2), (7)–(8), 14.** DORA calls for plans activated “without delay,” a crisis-management function, accessible disruption records and “crisis communication plans.” **Where will the COO establish activation authority, escalation, communications responsibility and recording of response activities?**

- **Incident handling and reporting — policy §§1, 3; DORA Articles 17–19, 23.** DORA requires an incident-management process and states that financial entities “shall report major ICT-related incidents” to the relevant authority; Article 23 extends the chapter to payment-related incidents. **Which policy or procedure will the COO reference for logging, classification, escalation, client communications and regulatory reporting, including non-ICT payment incidents?**

- **Suppliers — policy §§2–4; DORA Articles 28–30, 42(3).** DORA requires a “register of information,” “exit strategies” for critical or important ICT services, contractual continuity provisions and consideration of risks communicated through supervisory oversight. **Where will the COO connect supplier oversight, concentration and subcontracting risks, supplier recovery obligations, tested exit arrangements and supervisory risk notifications to continuity planning?**

- **Review, assurance and learning — policy §7; DORA Articles 6(4)–(7), 11(3), (6), 13.** The policy specifies review “every three years.” DORA’s ordinary framework calls for framework review “at least once a year,” independent control and audit arrangements, post-incident learning and staff training. **How will the COO distinguish policy review from framework and plan reviews, and provide event-triggered updates, assurance, corrective-action tracking and training?** These review objects differ, so the three-year policy interval alone is not treated as a direct contradiction.

- **Wider ICT framework — policy §§1–3; DORA Articles 6(8), 7–10.** DORA addresses a “digital operational resilience strategy,” resilient systems, protection controls and prompt detection of anomalies and single points of failure. **Which companion documents will the COO identify for these provisions, including ICT risk tolerance and resilience metrics?**

- **Advanced testing — policy §5; DORA Articles 26–27.** Article 26 requires selected entities to conduct TLPT “at least every 3 years,” subject to its exclusions and competent-authority identification. **Has the institution been identified for TLPT and, if so, where will the COO reference its programme and tester requirements?**

### NIST SP 800-34 Rev. 1

This is guidance for federal information systems. Its use here is a selected comparison reference; its federal mandates and impact categories are not assumed to bind this payment institution.

**Contradiction / wording to reconcile**

- **Walk-through versus technical testing — policy §5; NIST §§3.5.1, 3.5.3–3.5.4.** The policy specifies “a desktop walk-through.” NIST says “Each information system component should be tested to confirm the accuracy of individual recovery procedures” and distinguishes discussion exercises from technical testing. **Will the COO distinguish the walk-through from recovery testing and select exercise depth according to system impact?** NIST’s programme guidance uses an organisation-defined frequency; this review does not infer a universal annual testing obligation from its sample policy.

**Gaps**

- **Policy content and resources — policy §§3, 5; NIST §3.1.** Listed policy elements include “Resource requirements,” “Training requirements” and “Minimum frequency of backups and storage of backup media.” **Where will the COO establish or reference these elements and senior-management support?**

- **Business-led recovery targets — policy §§4, 6; NIST §§3.2.1–3.2.3.** NIST says to work “with the process owners, leadership and business managers” to determine acceptable downtime, then establish MTD, RTO, RPO and recovery priorities. **How will the COO obtain business input and approval rather than leave all system RTO decisions solely with IT?**

- **BIA refresh — policy §4; NIST §§3.2, 3.6.** NIST states: “When a significant change occurs, the BIA should be updated with the new information.” **Will the COO add change-triggered updates alongside the three-year cycle?**

- **Recovery strategies and security — policy §§2, 3, 6; NIST §§3.3–3.4, 5.1–5.4.** NIST links strategies to “disruption impacts and allowable downtimes identified in the BIA.” The policy has no counterpart for strategy selection. **Where will the COO require BIA-led backup, alternate-processing, telecommunications and equipment arrangements, preventive controls and preservation of security during recovery?**

- **Training and test follow-up — policy §§3, 5; NIST §§3.5–3.5.2.** NIST recommends training “at least annually” and documented after-action reports and corrective actions. **Where will the COO require role training, test objectives, success criteria and tracked improvements?**

- **Plan lifecycle — policy §§3, 7; NIST §§3.6, 4.1–4.5.** NIST says activation criteria “should be stated in the contingency planning policy” and describes activation, notification, recovery and reconstitution. **Which plans will the COO reference for activation authority and succession, out-of-hours notification, recovery sequencing, validation before return to normal, controlled distribution and change-triggered maintenance?**

### Gaps and review boundaries

- **Intake statements — Gaps:** You classified the material as medium, stated that this environment is approved for high, and selected DORA and NIST SP 800-34, “All of it.” These are your statements, not framework evidence. Your response did not establish the DORA regime; no exemption is assumed.
- **Applicability — policy header; DORA Articles 2, 4, 16 — legal/compliance review:** **Will the COO obtain confirmation of jurisdiction, authorisation and exemption status, and applicable proportionality?** Calling the institution “small” does not establish eligibility for Article 16.
- **Document status — policy header and §7:** Version 0.4 remains a draft dated 3 September 2026; no completed approval or review record was supplied. **Will the COO confirm the approval route and document-control dates before board submission?**
- **Source coverage:** DORA’s supplied text contains the enacting terms as adopted, without recitals; amendments and a current consolidated text were not checked. NIST’s supplied text contains the Executive Summary and Chapters 1–5; appendices and figures are **not reviewed**. **Will the COO have reviewers check the authoritative, current sources and any omitted material needed for their decisions?**
- **Whole-framework scope:** DORA includes authority and critical-provider oversight provisions, optional information sharing, enforcement and amendments beyond this policy’s content. NIST §1.2 excludes full business-process continuity from its scope. **Which companion documents will the COO provide where this policy cannot answer the selected texts?**
- **Frameworks not selected — not reviewed:** EU 2024/1774, the AI Act, NIST CSF, AI RMF and Generative AI Profile, FONES, UK resilience guidance, the ESAs AI statement, and the other shipped AI guidance. ISO 22301 was not selected or supplied with licence confirmation.

The COO should take these questions to document owners, information security, legal and compliance. The policy remains a draft and enters the normal approval route with its status unchanged; management retains the decisions.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. ______ reviewed it on ______.

Chief Operating Officer answers these, legal or compliance the marked points.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'wc -l .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md .agents/skills/check-against-standards/literature/ni`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md'`
- command_execution: `/bin/bash -lc "rg -n '"'^#|''^Source:|''^Publication|''^Reuse:|''^Date|''^Version|''^Retrieved'"' .agents/skills/check-against-standards/literature/nist/sp-800-`
- command_execution: `/bin/bash -lc "sed -n '186,449p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md"`
- command_execution: `/bin/bash -lc "sed -n '1,45p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '180,325p' .agents/skills/`
- command_execution: `/bin/bash -lc "sed -n '137,190p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '235,335p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '426,514p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '659,778p' .agents/skil`
- command_execution: `/bin/bash -lc "sed -n '190,235p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '337,394p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '450,502p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '659,695p' .agents/skil`
- command_execution: `/bin/bash -lc "sed -n '498,539p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '367,394p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '502,565p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '821,949p' .agents/skil`
- command_execution: `/bin/bash -lc "python - <<'PY'
from pathlib import Path
p=Path('.agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md')
s=p.rea`
- command_execution: `/bin/bash -lc "sed -n '50,56p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '514,547p' .agents/skills`
- command_execution: `/bin/bash -lc "python3 - <<'PY'
from pathlib import Path
s=Path('.agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md').read_t`
