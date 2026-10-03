# /check-against-standards case 1, run2: Claude Code, guidance at 9c837c3

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `14ce5e7e-0de4-4fa3-983e-fdeb7091f78a`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

Before I open `bc-policy-draft.md`, I need one thing from you:

**What class of data does the draft policy contain?**

For example: does it include any of the following?
- BIA data or risk assessment detail
- recovery strategies or design assumptions
- vulnerabilities or control weaknesses
- supplier weaknesses or contractual dependencies
- security-related architecture or site detail
- personal data or contact lists
- **board papers or executive-session material.** A draft headed to the board may count as this.

Or is it internal policy text with none of those?

Your answer, not any marking in the file, decides whether this environment is approved for the material. I won't open or read the file until you reply. Also, if it holds any passwords, keys or access tokens, remove them before we go on. Those go into no tool.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Bash: `ls -la; ls /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literat`
- Grep: `Sensitivity classes`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I've read the draft (v0.4, 3 September 2026, draft for the management board, owner: Chief Operating Officer). Before I compare it, I need two answers. The policy doesn't say which frameworks it's meant to follow, and I won't guess.

**1. Which frameworks should I compare it against, and which parts?** These texts are available here:

| Framework | Possibly relevant parts |
|---|---|
| Regulation (EU) 2022/2554 (DORA) | e.g. Art. 5–6, 11, 12 (ICT risk management, ICT business continuity, backup and recovery) |
| Delegated Regulation (EU) 2024/1774 (RTS on ICT risk management framework) | e.g. the articles on ICT business continuity policy and testing |
| NIST SP 800-34 Rev. 1, ch. 1–5 | contingency planning |
| NIST CSWP 29 (CSF 2.0) | e.g. Govern / Recover functions |
| UK Cabinet Office, *Organisational Resilience Guidance* | — |
| FONES, *Minimum standard for improving ICT resilience* (2023) | — |

ISO 22301 isn't included here because its licence doesn't allow it. If you want it in the comparison, attach your own copy and confirm that your licence allows this use. I'll then cite it by clause number only.

**2. Is there anything else I should know before comparing?** For example, an earlier approved version of this policy, or management decisions that the draft has to reflect. "No" is a fine answer.

I'll record your answers under Gaps as your own statements, not as sources. They can shape the scope but won't supply any values in the review.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-against-standards/1/run2/work/bc-policy-draft.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/README.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/govern.md`
- Glob: `literature/**/*.md`
- Grep: `Say in the document that AI helped`

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

I've finished the comparison. The review is below, and I haven't changed or recorded anything.

---

**Sources**
- Document reviewed: *Business continuity policy*, version 0.4, 3 September 2026. Status: draft for the management board. Owner: Chief Operating Officer. Data class: medium (your answer).
- Regulation (EU) 2022/2554 (DORA), OJ L 333, 27 December 2022, as adopted. Shipped conversion retrieved 2026-09-10 (`literature/eur-lex/dora-regulation-2022-2554.md`). Reuse authorised with acknowledgement; EUR-Lex is authoritative.
- NIST SP 800-34 Rev. 1, May 2010, Executive Summary and Chapters 1–5 only. Shipped conversion retrieved 2026-09-10 (`literature/nist/sp-800-34r1-contingency-planning-body.md`). U.S. Government work; the PDF is authoritative.

## Block 1: DORA (Regulation (EU) 2022/2554)

⚖ = for legal or compliance review. Every point in this block concerns a regulation, so every point carries the mark.

**Contradictions (both passages quoted)**

1. ⚖ **Testing frequency.** Draft §5: "tested every two years, by a desktop walk-through." DORA Art. 11(6)(a): "test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly". *Question for the owner:* how does a two-year cycle relate to the yearly test in Art. 11(6)(a)?
2. ⚖ **Test type.** Draft §5: "by a desktop walk-through." Art. 11(6), second subparagraph: entities other than microenterprises "shall include in the testing plans scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities". *Question:* does the policy intend to allow only walk-throughs?
3. ⚖ **Review frequency.** Draft §7: "reviews this policy every three years." Art. 6(5): the ICT risk management framework "shall be documented and reviewed at least once a year … as well as upon the occurrence of major ICT-related incidents". Art. 11(1) places the ICT business continuity policy "as part of the ICT risk management framework". Art. 11(6), last subparagraph, also requires regular review "taking into account the results of tests … and recommendations stemming from audit checks or supervisory reviews". *Question:* is a three-year cycle with no event triggers the intended review regime?
4. ⚖ **Who sets recovery objectives.** Draft §6: "The IT manager sets the recovery time objectives for all systems." Art. 12(6): "In determining the recovery time and recovery point objectives for each function, financial entities shall take into account whether it is a critical or important function". Art. 5(2)(d) gives the management body responsibility for "the determination of the appropriate risk tolerance level of ICT risk". *Question:* should objectives be set per system or per function, and by whom? Where are recovery point objectives?

**Gaps (a passage with no counterpart in the draft)**

5. ⚖ **Management body's role.** Art. 5(2)(e): the management body shall "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy and ICT response and recovery plans". Draft §3 names the COO, the BCM officer and the IT manager, but gives the board no role. *Question:* should the policy state the board's approval and oversight role?
6. ⚖ **Critical or important functions.** Art. 11(2)(a) is aimed at ensuring "the continuity of the financial entity's critical or important functions". The draft does not use the term or say how these functions are identified. *Question:* where are they defined?
7. ⚖ **BIA content.** Art. 11(5): the BIA covers "severe business disruptions", uses "quantitative and qualitative criteria, using internal and external data and scenario analysis", and considers "third-party dependencies and information assets, and their interdependencies". Draft §4 names the frequency and coverage only. *Question:* should the policy set the BIA's criteria and coverage?
8. ⚖ **Third-party dependencies.** Art. 11(4) asks for plans "notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers". Art. 28(8) requires exit strategies for such services. The draft says nothing on third parties. *Question:* is this deliberately left to another policy?
9. ⚖ **Crisis management and communication.** Art. 11(7) requires "a crisis management function". Art. 14(1) requires "crisis communication plans". Art. 11(6)(b) requires testing of those plans. Art. 14(3) requires that "At least one person … be tasked with implementing the communication strategy". None of these appear in the draft. *Question:* where are they covered?
10. ⚖ **Backup and restoration.** Art. 12(1) requires documented "backup policies and procedures specifying the scope of the data … and the minimum frequency of the backup", plus "restoration and recovery procedures and methods". Art. 12(4) requires "redundant ICT capacities" for entities other than microenterprises. Neither appears in the draft. *Question:* is this covered elsewhere, and should the policy refer to it?
11. ⚖ **Independent audit of recovery plans.** Art. 11(3) says ICT response and recovery plans "shall be subject to independent internal audit reviews". Draft §3 gives plan ownership to the IT manager and mentions no audit. *Question:* who audits these plans?
12. ⚖ **Records during disruption.** Art. 11(8) requires "readily accessible records of activities before and during disruption events". The draft has no counterpart. *Question:* should it have one?
13. ⚖ **Lessons and training.** Art. 13(2) requires "post ICT-related incident reviews" that identify improvements "within the ICT business continuity policy". Art. 13(6) makes "digital operational resilience training" compulsory for "all employees and … senior management staff". The draft has no counterpart for either. *Question:* where are these covered?
14. ⚖ **Testing programme.** Art. 24(4) requires "tests are undertaken by independent parties". Art. 24(6) requires "at least yearly, that appropriate tests are conducted on all ICT systems and applications supporting critical or important functions". Draft §5 names no tester and gives a two-year cycle. *Question:* how does §5 relate to Art. 24?
15. ⚖ **Scope exclusion.** Draft §2 says "the marketing website is not" in scope. Art. 8(1) requires entities to "identify, classify and adequately document all ICT supported business functions". *Question:* on what basis was the website excluded, and is that exclusion recorded?

DORA Chapters VI to IX and Articles 31–44 are mainly about authorities, oversight of critical ICT third-party providers, penalties and amendments. I read them and drew no finding from them for this policy.

## Block 2: NIST SP 800-34 Rev. 1 (guidance, not regulation)

**Contradictions (both passages quoted)**

16. **Who sets recovery time objectives.** Draft §6: "The IT manager sets the recovery time objectives". SP 800-34 §3.2.1: the coordinator "with the process owners, leadership and business managers determine the acceptable downtime". The MTD "represents the total amount of time the system owner/authorizing official is willing to accept". The RTO must keep the MTD from being exceeded. *Question:* should business owners and leadership set or approve downtime limits, with the IT manager deriving RTOs from them? Should the policy name MTD and RPO?
17. **Test depth.** Draft §5: "by a desktop walk-through." §3.5.4: "For low-impact systems, a tabletop exercise … is sufficient". "For moderate-impact systems, a functional exercise" should be held. "For high-impact systems, a full-scale functional exercise" should be held, including "a system failover to the alternate location". *Question:* is a walk-through meant to apply to every system, including the card processing platform?
18. **Annual cycle in the sample policy.** Draft §5 says "every two years" and §7 says "every three years". The §3.1 *sample* policy statement says plans "must be reviewed annually" and "shall be tested annually". *Question:* the sample is illustrative rather than a requirement. Is the longer cycle a deliberate choice?

**Gaps**

19. **Key policy elements.** §3.1 lists "Roles and responsibilities; Scope …; Resource requirements; Training requirements; Exercise and testing schedules; Plan maintenance schedule; and Minimum frequency of backups and storage of backup media." The draft has roles, scope and a test schedule. It has no counterpart for resources, training, plan maintenance or backups. *Question:* should these four be added?
20. **Training.** §3.5.2: "Training should be provided at least annually. Personnel newly appointed to ISCP roles should receive training shortly thereafter." The draft has no counterpart. *Question:* should it?
21. **BIA triggers.** §3.6: "When a significant change occurs, the BIA should be updated". Draft §4 says only "every three years". *Question:* should change trigger a BIA?
22. **Plan maintenance.** §3.6: plans reviewed "at an organization-defined frequency or whenever significant changes occur". Draft §7 covers review of the policy only, not the plans. *Question:* who reviews plans, and how often?
23. **Activation authority.** §3.4.6 calls for "a single authoritative role for overall decision-making responsibility, including plan activation". The draft names no one. *Question:* who activates the plans?
24. **Test results.** §3.5: "results are documented in an after-action report, and Lessons Learned corrective actions are captured". The draft has no counterpart. *Question:* should it?
25. **Senior management involvement.** §3.1: "senior management … must support a contingency program and be included in the process to develop the program policy". *Question:* how was senior management involved beyond the COO's ownership?

## Challenge: wording that is ambiguous, unenforceable or open to two readings

26. **§1 vs §2.** §1 says "keeps its payment services running", but §2's scope also covers customer support and the two offices. *Question:* is the purpose narrower than the scope by design?
27. **§2.** "The ICT systems that support them are in scope." It isn't stated which systems, or who decides. *Question:* where is the list, and who maintains it?
28. **§3.** "runs the programme day to day." The programme isn't defined, and neither is the officer's authority over plan owners. *Question:* what can the BCM officer require of others?
29. **§5.** "are tested every two years" can mean every plan every two years, or a rolling programme. The policy doesn't say who tests, who reviews results or who fixes findings. *Question:* which reading is meant?
30. **§6.** "for all systems" could include the website that §2 excludes. The RTOs have no stated basis (BIA) and no approver. *Question:* on what basis are RTOs set, and who approves them?
31. **§7.** "reviews" doesn't say who approves changes, and the header gives no next review date. *Question:* who approves revisions?
32. **Whole draft.** There is no monitoring, reporting to the board, or consequence for non-compliance, which makes the policy hard to enforce. *Question:* how will the board know the policy is followed?

## Gaps (what the sources leave open)

- **Status of the reviewed document.** It is a draft (v0.4, 3 September 2026, "draft for the management board"). I reviewed it as the document in front of me, not as approved policy. Owner: Chief Operating Officer. Review date: none given in the header.
- **Intake answers (your statements, not sources):** "DORA and NIST SP 800-34" and "All of it". I read these as covering both frameworks in full, as far as the shipped texts go.
- **SP 800-34 appendices (BIA template, plan templates) are not in the shipped file.** Not reviewed. SP 800-34 uses FIPS 199 impact levels, which the draft does not assign. Without them, findings 17 and 18 can't be settled.
- ⚖ **Which DORA regime applies:** Art. 2(1)(b), the Art. 16 simplified framework, and the microenterprise carve-outs in Art. 11(6), 12(4) and 24. The draft says "a small payment institution with 140 staff". Whether it is exempted is not in the sources. Legal or compliance to confirm, because several findings above depend on it.
- **Frameworks not selected, so not reviewed:** Delegated Regulation (EU) 2024/1774 (DORA Art. 15(d)–(f) delegates "the components of the ICT business continuity policy" and its testing to the RTS), NIST CSF 2.0, the UK Cabinet Office guidance, FONES, the AI Act, and ISO 22301 (not shipped; your own licensed copy would be needed).
- **What would settle the open points:** the critical or important functions list, the BIA method, third-party, backup, crisis communication and incident policies (if they exist elsewhere), and the board's terms of reference. None was attached, so none of it was reviewed.
- **Material telling an AI to act:** none found in the draft.

This review states no conclusion that the draft complies with or meets either framework. Only a person, checking against the source text, can say that. The draft goes into the normal board approval route with its status unchanged, and the policy decisions stay with management.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

The Chief Operating Officer answers these, legal or compliance the marked points.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Grep: `^#{2,3} `
- Grep: `^(#|\d\.\d* [A-Z]|[1-5]\.[0-9]+(\.[0-9]+)? )`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Grep: `Recovery Time Objective|RTO defines|business process owner`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
