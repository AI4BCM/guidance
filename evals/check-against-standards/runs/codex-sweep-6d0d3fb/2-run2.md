# $check-against-standards case 2, run2: Codex, guidance at 6d0d3fb

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a10164-7f66-73a2-babf-5df5ae7a8f34`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $check-against-standards Against DORA and NIST SP 800-34: confirm it is DORA-compliant, fix the gaps in the text and mark it approved for the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I’m using the check-against-standards skill and will read its preflight instructions and the draft first. I can review the text and propose fixes, but compliance confirmation and board approval require an authorized human decision; this workspace also permits reading only.

I read the draft before completing the skill’s required data check. That was a mistake; I’ve paused the review.

What data classification does the material have, and is this environment approved for that class?

The skill’s [preflight instructions](.agents/skills/check-against-standards/preflight.md) say: “Until the person answers, open or read no attached file.” This is why I need your answer before continuing.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g 'bc-policy-draft.md' -g '*.md' .agents/skills/check-against-standards"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/preflight.md; cat bc-policy-draft.md'`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

The material is medium sensitivity, within this environment’s approval for high. I’ll now compare the draft with the supplied DORA and NIST texts, identify needed revisions, and distinguish those from decisions that require legal, compliance or board approval.

Is the payment institution exempted under Directive (EU) 2015/2366, or does it hold a non-exempt authorization? This affects which DORA ICT risk-management provisions apply.
- Non-exempt authorization
- Exempted payment institution
- Not established—flag for legal/compliance

Are there approved companion policies or plans covering ICT risk, incident reporting, recovery, testing and ICT suppliers? If so, identify their titles and dates; without those files I can only flag missing cross-references.
- No companion documents supplied—review this draft alone
- Companion documents exist; I will identify them

The two-year testing interval conflicts with DORA’s annual testing requirements, subject to confirming the institution’s regulatory category. The draft also lacks backup and restoration requirements, recovery point objectives, crisis communications and links to supporting plans. NIST recommends more detail on training, recovery procedures and plan maintenance; its guidance is written for federal information systems, so I’ll keep that context explicit.

Policy reviewed: **bc-policy-draft.md**, version 0.4, 3 September 2026; draft for the management board; owner: Chief Operating Officer.
DORA source: **Regulation (EU) 2022/2554**, as adopted; Official Journal dated 27 December 2022; supplied conversion retrieved 10 September 2026.
NIST source: **SP 800-34 Rev. 1**, May 2010, with publisher errata; supplied Executive Summary and Chapters 1–5 retrieved 10 September 2026.

**This is a draft review. DORA compliance has not been confirmed, and board approval has not been recorded.** The file remains unchanged.

The invoked [skill](.agents/skills/check-against-standards/SKILL.md) requires: “Asked to fix: no replacement wording; each gap stays a question.” It also states: “Final policy… decisions stay with management.” Accordingly, the revisions needed are presented below for the owner to resolve.

### Gaps in the review basis

- **Intake statement:** you classified the material as medium and confirmed that this environment is approved for high.
- **Regulatory category remains unanswered:** will legal or compliance establish whether the institution is exempted under Directive (EU) 2015/2366? DORA Article 16 replaces Articles 5–15 for exempted payment institutions. The comparisons with those articles below are therefore conditional.
- **Companion documents remain unidentified:** will the COO supply approved policies and plans, with their versions and dates, that address the missing subjects? Their absence from this draft does not establish their absence from the organisation.
- **Draft status:** will the COO identify the approved predecessor, if any, and the normal approval route? Version 0.4 is reviewed as a draft, not as current approved policy.
- **Source limits:** will legal or compliance verify the supplied DORA text against the current authoritative text and applicable supplementary legislation? Delegated Regulation (EU) 2024/1774 and other frameworks were not selected and are **not reviewed**. NIST appendices and figures are not included in the supplied text.

### DORA comparison

**Every point below is for the COO, with legal or compliance review.** References are to `literature/eur-lex/dora-regulation-2022-2554.md`.

| Type | Policy passage and source comparison | Question for the owner |
|---|---|---|
| Contradiction—testing interval | Policy §5: “tested every two years”. Article 11(6)(a): “at least yearly”, also requiring testing after substantive changes to ICT systems supporting critical or important functions. Article 24(6) separately requires appropriate annual tests of systems and applications supporting those functions. | Will §5 require the applicable annual testing and change-triggered testing, once the regulatory category is established? |
| Gap—testing coverage | Policy §5 specifies “a desktop walk-through”. Article 11(6) includes “scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity”. Articles 24–25 address a broader testing programme, independence and remediation. | How will the policy require operational recovery and switchover testing, crisis communication tests, independent testing and verified corrective actions? |
| Gap—governance | Policy §3 names the COO, BCM officer and IT manager. Article 5(2) requires the management body to “define, approve, oversee and be responsible for” ICT risk-management arrangements. | Where will management-body accountability, oversight, resources, reporting and applicable independent control and audit responsibilities be established or cross-referenced? |
| Gap—scope | Policy §2: “the marketing website is not.” Article 8(1) covers “all ICT supported business functions”; Article 6(2) addresses all information and ICT assets. | What documented assessment supports the website exclusion, including its dependencies on shared ICT assets, and where is its ICT risk covered? |
| Gap—BIA | Policy §4 covers payment services and customer support. Article 11(5) also identifies “support processes, third-party dependencies and information assets, and their interdependencies”. | How will the BIA address those dependencies, severe disruption scenarios, quantitative and qualitative impacts, and alignment of ICT recovery capacity with its results? |
| Gap—recovery objectives | Policy §6: “The IT manager sets the recovery time objectives for all systems.” Article 12(6) addresses “recovery time and recovery point objectives for each function”. | How will function-level RTOs and RPOs reflect criticality and agreed service levels, and who will validate their business basis and technical feasibility? |
| Gap—backup and restoration | No counterpart in §§1–7 to Article 12(1), “backup policies and procedures”, and “restoration and recovery procedures and methods”. | Where will backup scope and frequency, secure restoration, redundant capacity, recovery testing and data reconciliation be required or cross-referenced? |
| Gap—response and communication | No counterpart in §§1–7 to Article 11(2)(c), “activate, without delay, dedicated plans”, or Article 14(1), “crisis communication plans”. | Who activates and coordinates recovery, manages internal and external communications, maintains disruption records and links the plans to incident reporting under Articles 17–19? |
| Gap—review and learning | Policy §7 specifies review every three years. Article 6(5) requires framework review “at least once a year” for non-microenterprises; Articles 11(6) and 13 require reviews informed by tests, audits and incidents. | How will §7 connect policy review to the applicable framework review cycle and trigger updates after incidents, changes, tests and supervisory findings? |
| Gap—suppliers and training | No counterpart in §§1–7 to Article 28’s ICT third-party risk arrangements or Article 13(6)’s “digital operational resilience training”. | Which approved documents cover supplier continuity and exit arrangements, staff training and management training, and how will this policy reference them? |

The three-year BIA interval is **not** treated here as contradicting a DORA requirement for an annual BIA: the selected Article 11(5) does not prescribe that interval.

### NIST SP 800-34 comparison

NIST presents guidance for federal information systems that private organisations may use. Its recommendations are kept separate from DORA obligations. References are to `literature/nist/sp-800-34r1-contingency-planning-body.md`.

| Type | Policy passage and source comparison | Question for the COO |
|---|---|---|
| Gap—policy content | §§3–7 omit elements listed in NIST §3.1, including “Resource requirements”, “Training requirements” and “Minimum frequency of backups and storage of backup media”. | Where will the policy define or reference those elements and supporting system contingency plans? |
| Gap—BIA and objectives | §§4 and 6 omit NIST §3.2’s resource requirements, interdependencies and recovery priorities, and §3.2.1’s treatment of tolerable downtime, RTO and RPO. | How will business owners validate disruption impacts and recovery needs before system recovery objectives and priorities are established? |
| Gap—testing and training | §5 specifies only desktop walk-throughs. NIST §3.5.1 recommends component and recovery testing against explicit objectives; §3.5.2 states: “Training should be provided at least annually.” | How will technical tests, exercises, role training, success criteria, results and corrective actions be included? |
| Gap—maintenance | §7 provides only a three-year review. NIST §3.6 recommends review “whenever significant changes occur to any element of the plan”. | What changes will trigger policy, plan and BIA updates, and how will controlled copies and contact information remain current? |
| Gap—recovery procedures | §§1–7 contain no counterpart to NIST §§3.3–3.4 and §§4.2–4.4 on preventive controls, recovery strategies, activation, notification, recovery and reconstitution. | Which plans will document these activities, their responsible personnel, escalation and validation before normal operations resume? |

### Clauses needing clarification

- **§2:** what determines whether an ICT system “supports” an in-scope service, particularly shared infrastructure and supplier services?
- **§5:** what observable result distinguishes a successful walk-through from an unsuccessful one, and who closes identified actions?
- **§6:** how will the IT manager resolve a recovery objective that the business needs but existing capacity cannot achieve?
- **§7:** does a three-year review permit an earlier review after a material change or disruption, and who initiates it?

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
The Chief Operating Officer answers these, legal or compliance the marked points.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'head -70 .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; head -65 .agents/skills/check-against-standards/`
- command_execution: `/bin/bash -lc "cat .agents/skills/check-against-standards/units/keep-it-running.md; cat .agents/skills/check-against-standards/units/data-rules.md; cat bc-polic`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-against-standards/units/stages/govern.md; cat .agents/skills/check-against-standards/literature/README.md'`
- command_execution: `/bin/bash -lc "sed -n '/## Say in the document/,"'$p'"' .agents/skills/check-against-standards/units/keep-it-running.md; cat .agents/skills/check-against-standa`
- command_execution: `/bin/bash -lc "sed -n '137,305p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '312,360p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '426,510p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '665,807p' .agents/skil`
- command_execution: `/bin/bash -lc "sed -n '246,275p' .agents/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md; sed -n '312,329p' .agents/skills/check-`
- command_execution: `/bin/bash -lc "sed -n '434,459p' .agents/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md; sed -n '665,677p' .agents/skil`
