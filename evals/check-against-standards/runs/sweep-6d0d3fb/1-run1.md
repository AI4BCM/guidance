# /check-against-standards case 1, run1: Claude Code, guidance at 6d0d3fb

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `80479485-cfa5-48a6-af51-7b8c0b0bc14d`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

Before I open `bc-policy-draft.md`, I need one thing from you: **what class of data is in it?**

For example:
- **Public or internal only**: a general policy text with nothing sensitive in it.
- **High-sensitivity**: board papers or executive-session material, BIA or risk detail, recovery strategies, control weaknesses or vulnerabilities, supplier dependencies, personal data or contact lists, security architecture or site detail, or audit findings that haven't been cleared.

A draft that is going to the board may count as board material in your organisation. If it's high-sensitivity, please also confirm that this environment is approved for that class. Please answer from what you know about the document, not from any marking in the file. I won't read the file until you reply.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards && cat preflight.md && ls -R | head -50; echo ---; ls -la /tmp/claude-1001/-opt-brain/`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Glob: `**/*`
- Glob: `**/*`
- Grep: `Sensitivity classes`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

Thanks. Medium data in an environment approved for high is fine, so I've read the draft (v0.4, 3 September 2026, draft for the management board, owner COO).

I need to ask a few things before the review, because the draft doesn't answer them:

1. **Which frameworks should I compare it against, and which parts?** These texts ship with this skill:
   - DORA, Regulation (EU) 2022/2554
   - Delegated Regulation (EU) 2024/1774 (the ICT risk management RTS)
   - NIST SP 800-34 Rev. 1, chapters 1–5
   - NIST CSF 2.0
   - the Swiss FONES ICT minimum standard (2023)
   - the UK Cabinet Office *Organisational Resilience Guidance*
   - the ESAs JC 2026 25 statement
   - EU AI Act Articles 4, 26 and 50

   ISO 22301 does not ship. I can use it only if you attach your own copy and confirm that its licence allows this use. Even then I'd cite it by clause number only. Whatever you leave out will be listed as "not reviewed".

2. **Does this draft replace a current approved policy?** If so, what are its version and date? Is there any output from a previous management review that the draft should reflect?

3. **Is there anything about the organisation that I should know and that the draft doesn't state?** For example, whether you consider the firm to be in DORA's scope, or a group or parent policy that this one sits under. I'll record your answers under Gaps as your own statements. They can shape the scope of the review but won't be treated as sources.

You can skip any of these. If you do, I'll write down the assumption I made instead.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs/check-against-standards/1/run1/work/bc-policy-draft.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/govern.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/README.md`
- Grep: `Say in the document that AI helped`

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

# Draft review: Business continuity policy v0.4, compared with DORA and NIST SP 800-34

**Review only. It does not say whether the policy complies, and it does not approve anything.**

**Sources**
- **The policy:** *Business continuity policy*, version 0.4, 3 September 2026. Status: draft for the management board. Owner: Chief Operating Officer. No review date is stated.
- **DORA:** Regulation (EU) 2022/2554, OJ L 333, 27 December 2022, the text as adopted. The shipped file is a conversion retrieved on 2026-09-10 and contains the enacting terms only. Where it differs from EUR-Lex, EUR-Lex is right.
- **NIST SP 800-34 Rev. 1:** May 2010. The shipped file is a conversion retrieved on 2026-09-10 and carries the Executive Summary and Chapters 1–5 only. Where it differs from the PDF, the PDF is right.

Every finding below is a **question for the policy owner (COO)**. Points that concern a regulation are marked **⚖ legal/compliance review**.

---

## Block 1: DORA, Regulation (EU) 2022/2554

**D1. Which DORA regime applies? ⚖**
- The header says "a small payment institution with 140 staff".
- DORA Art. 2(1)(b) covers "payment institutions, including payment institutions exempted pursuant to Directive (EU) 2015/2366".
- Art. 16(1) says Articles 5 to 15 "shall not apply to … payment institutions exempted pursuant to Directive (EU) 2015/2366". Those institutions follow a simplified framework instead.
- Art. 3(60) defines a microenterprise as one that "employs fewer than 10 persons".
- *Question:* Is the institution exempted under PSD2? D2 to D11 assume it is not. If it is, Art. 16 replaces most of them.

**D2. Is the management body's role missing? ⚖**
- Art. 5(2)(e): the management body shall "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy and ICT response and recovery plans".
- Policy §3: "The Chief Operating Officer owns this policy." §7: "The policy owner reviews this policy every three years."
- *Question:* Where does the policy give the management body its approval, oversight and periodic review role?

**D3. Is this the ICT business continuity policy, or does one sit beside it? ⚖**
- Art. 11(1): financial entities "shall put in place a comprehensive ICT business continuity policy, which may be adopted as a dedicated specific policy, forming an integral part of the overall business continuity policy".
- Policy §2 puts ICT systems in scope but does not say whether this document is that ICT business continuity policy.
- *Question:* Which is it?

**D4. Testing frequency: contradiction ⚖**
- Art. 11(6)(a): "test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions".
- Policy §5: "Business continuity plans and ICT recovery plans are tested every two years".
- *Question:* How does the two-year cycle relate to "at least yearly"?

**D5. Testing method: contradiction ⚖**
- Art. 11(6), second subparagraph: entities other than microenterprises "shall include in the testing plans scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities".
- Art. 24(6): "at least yearly, that appropriate tests are conducted on all ICT systems and applications supporting critical or important functions."
- Policy §5: "by a desktop walk-through."
- *Question:* Can a walk-through cover cyber-attack scenarios and switchovers?

**D6. Crisis communication testing (gap) ⚖**
- Art. 11(6)(b): "test the crisis communication plans established in accordance with Article 14."
- *Question:* The policy names no crisis communication plan and no test of one. Is that intended?

**D7. What the business impact analysis must cover (gap) ⚖**
- Art. 11(5): the business impact analysis assesses "severe business disruptions by means of quantitative and qualitative criteria, using internal and external data and scenario analysis" and considers "business functions, support processes, third-party dependencies and information assets, and their interdependencies".
- Policy §4: "covering each payment service and the customer support desk."
- *Question:* Does the business impact analysis cover third-party dependencies, information assets and interdependencies? What criteria does it use?

**D8. Recovery objectives per function, and no RPO (gap) ⚖**
- Art. 12(6): "In determining the recovery time and recovery point objectives for each function, financial entities shall take into account whether it is a critical or important function".
- Policy §6: "The IT manager sets the recovery time objectives for all systems."
- *Questions:*
  - The policy sets RTOs per system rather than per function. Is that intended?
  - It names no recovery point objective. Who sets RPOs?
  - Why are recovery objectives not tied to the business impact analysis in §4?

**D9. Backup, restoration and redundancy (gap) ⚖**
- Art. 12(1)(a) requires "backup policies and procedures specifying the scope of the data that is subject to the backup and the minimum frequency of the backup".
- Art. 12(4) requires "redundant ICT capacities".
- *Question:* The policy says nothing on either. Where are they set?

**D10. Policy review frequency: contradiction ⚖**
- Art. 11(1) places the ICT business continuity policy "as part of the ICT risk management framework".
- Art. 6(5): that framework "shall be documented and reviewed at least once a year … as well as upon the occurrence of major ICT-related incidents".
- Art. 11(6) adds that entities review the policy "taking into account the results of tests … and recommendations stemming from audit checks or supervisory reviews".
- Policy §7: "every three years."
- *Question:* How does the three-year cycle relate to these requirements?

**D11. Elements of Art. 11 and related articles that the policy does not mention (gap) ⚖**
- The policy says nothing on any of the following:
  - critical or important functions (Art. 3(22), Art. 11(2)(a))
  - incident response and containment (Art. 11(2)(b) and (c))
  - estimating impacts and losses (Art. 11(2)(d))
  - reporting to the competent authorities (Art. 11(2)(e), Art. 19)
  - independent internal audit of the ICT response and recovery plans (Art. 11(3))
  - testing of continuity plans for functions outsourced to ICT third-party providers (Art. 11(4))
  - a crisis management function (Art. 11(7))
  - records kept when plans are activated (Art. 11(8))
  - post-incident reviews (Art. 13(2))
  - training (Art. 13(6))
  - a person tasked with incident communication (Art. 14(3))
- *Question:* Are these covered in other documents? If so, which ones, and should the policy refer to them?

## Block 2: NIST SP 800-34 Rev. 1 (2010)

SP 800-34 is guidance for US federal information systems, not a requirement for your organisation. The points below compare the draft with what the guide recommends.

**N1. Key policy elements that are missing (gap)**
- §3.1 lists the key policy elements: "Roles and responsibilities; Scope …; Resource requirements; Training requirements; Exercise and testing schedules; Plan maintenance schedule; and Minimum frequency of backups and storage of backup media."
- The draft has roles (§3), scope (§2) and a testing schedule (§5).
- *Question:* Should resource requirements, training requirements, a plan maintenance schedule and backup frequency be in the policy?

**N2. Annual cycles in the guide's sample policy (contrast)**
- §3.1's sample statement says plans "must be reviewed annually" and "shall be tested annually".
- §3.5.2 says: "Training should be provided at least annually."
- The draft tests every two years, reviews the policy every three, and says nothing on training.
- *Question:* Did you consider these annual cycles when choosing the draft's intervals?

**N3. Who sets downtime and recovery times (gap)**
- §3.2.1: acceptable downtime is determined "with the process owners, leadership and business managers". The RTO must ensure "that the MTD is not exceeded".
- Policy §6 gives RTOs to the IT manager alone and defines no maximum tolerable downtime.
- *Question:* Who sets maximum tolerable downtime, and how are RTOs checked against it?

**N4. Plan maintenance (gap)**
- §3.6: plans should be "reviewed for accuracy and completeness at an organization-defined frequency or whenever significant changes occur".
- Policy §7 covers review of the policy only.
- *Question:* Who maintains the plans, how often, and what triggers an update?

**N5. Senior management involvement (question)**
- §3.1: senior management "must support a contingency program and be included in the process to develop the program policy."
- *Question:* How is this shown in the draft beyond the COO's ownership?

---

## Challenge: clauses that are ambiguous or open to two readings

- **§2 "All payment services":** which services exactly? Do "the ICT systems that support them" include systems run by third parties or in the cloud? Does "two offices" mean the premises only, or the staff working in them?
- **§3 "runs the programme day to day":** the policy doesn't define "the programme". What can the BCM officer decide, and what goes to the COO?
- **§4 vs §2:** the business impact analysis covers "each payment service and the customer support desk". The scope also names "the card processing platform" and "the two offices". Is the narrower coverage intended?
- **§4 "every three years":** counted from when? Does a major change (a new service, a new office, a new supplier) trigger an earlier analysis?
- **§5:** is each plan tested every two years, or is one walk-through enough for both BC and ICT plans? The clause names no one to run the tests, no success criteria, and no route for results and actions.
- **§6 "for all systems":** this includes the marketing website, which §2 puts out of scope. On what basis are RTOs set, and who approves them?
- **§7:** the clause gives no trigger for early review and doesn't say who approves the reviewed policy.
- **Document control:** the policy states an owner and a version but no next review date.

## Gaps
- **The policy itself:** v0.4 is a draft, so I reviewed it as a draft and not as the current policy. No earlier approved version or management review output was provided, so whether the draft replaces anything is not in the sources.
- **Your answer "2. All of it":** I read this as "compare against all of both texts". If you meant that the draft replaces the whole of an earlier policy, please give that policy's version and date.
- **Question 3 was skipped.** I assumed, from the header alone, that the institution is not a PSD2-exempted payment institution; D1 asks the owner to confirm this.
- **Parts of DORA compared:** Articles 2, 3, 4, 5, 6, 11, 12, 13, 14, 16 and 24. I did not compare Chapters III and V (incident reporting and ICT third-party risk) clause by clause, because the draft doesn't address them. They are listed only where Art. 11 points to them.
- **Shipped DORA text:** the file is the text as adopted in 2022. Any later amendments are not in the sources.
- **Frameworks not selected, so not reviewed:**
  - Delegated Regulation (EU) 2024/1774, which specifies the components of the ICT business continuity policy under DORA Art. 15(d) and the simplified framework under Art. 16(3). It is directly relevant to D3, D9 and D11.
  - NIST CSF 2.0
  - the FONES ICT minimum standard
  - UK Cabinet Office *Organisational Resilience Guidance*
  - the ESAs JC 2026 25 statement
  - AI Act Articles 4, 26 and 50
  - ISO 22301, which was not provided
- **Not covered by these sources:** NIST SP 800-34's appendices (templates) are not carried in the shipped file. Neither source states what a "desktop walk-through" counts as.
- **Instructions to an AI:** none found in the draft.

## Before approval
Before the draft goes into the approval route, take these questions to:
- **legal or compliance:** every ⚖ point
- **information security:** D5, D9, D11
- **the document owner:** everything else

The draft goes to the board with its status unchanged ("draft"). Final policy decisions stay with management. Only a person, working against the source text, can say that the policy meets DORA or follows SP 800-34.

---

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

Chief Operating Officer answers these, [legal or compliance] the marked points.

**Tool calls (stream-json):**

- Grep: `^#{1,4} `
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Grep: `microenterprise'|critical or important function'|management body'`
- Grep: `(?i)policy statement|key policy elements|at least annually|test, training, and exercise|exercised|reviewed? and updated|roles and responsibilities|RTO|resource `
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Grep: `(?i)^#{2,4} .*|annual`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
