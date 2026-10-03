# /check-against-standards case 1, run3: Claude Code, guidance at 2f85a91

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `845e65ad-02f2-4543-9c23-55d639ec03b2`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I haven't opened `bc-policy-draft.md` yet. This skill needs to know what kind of data the file contains before it reads anything.

**What class of data does the draft policy contain?** For example:

- **High sensitivity:** board papers or executive-session material, Business Impact Analysis (BIA) or risk assessment detail, recovery strategies and design assumptions, control weaknesses or vulnerabilities, supplier weaknesses or contractual dependencies, security architecture or site detail, personal data or contact lists, or audit findings the audit owner hasn't cleared yet. This class can only be handled in an environment your organisation has approved for it.
- **Internal or lower sensitivity:** a policy text with none of the material above.

The file's own marking doesn't count; I'll go by your answer. Since this draft is going to the board, please also confirm that this environment is approved for that class of data.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards && cat preflight.md && ls -R | head -50 && cat literature/README.md; echo ----; ls -la`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Glob: `*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/README.md`
- Grep: `Sensitivity classes`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I've read the draft: version 0.4, dated 3 September 2026, status "draft for the management board", owned by the Chief Operating Officer. Before I compare it with anything, I need you to choose which frameworks to use. I won't pick them for you.

**1. Which frameworks, and which parts of them, should I compare the draft with?** These are the texts that ship with this skill:

| Framework | File |
|---|---|
| DORA, Regulation (EU) 2022/2554 (for example Articles 5, 11 and 12 on governance, response and recovery, and backup) | `eur-lex/dora-regulation-2022-2554.md` |
| Delegated Regulation (EU) 2024/1774, the DORA technical standard on managing ICT risk (for example Articles 24 to 26 on ICT business continuity) | `eur-lex/delegated-regulation-2024-1774.md` |
| NIST SP 800-34 Rev. 1, contingency planning, chapters 1 to 5 | `nist/sp-800-34r1-contingency-planning-body.md` |
| NIST CSF 2.0 | `nist/cswp-29-csf-2-0.md` |
| UK Cabinet Office, *Organisational Resilience Guidance* | `uk-cabinet-office/organisational-resilience-guidance.md` |
| FONES (Swiss Federal Office for National Economic Supply), *Minimum standard for improving ICT resilience* (2023) | `swiss-fones/minimum-standard-ict-resilience-2023.md` |
| AI Act Articles 4, 26 and 50, NIST AI RMF, and the ESAs statement JC 2026 25 | these cover AI and are probably not relevant to this policy |

The draft describes a payment institution, so DORA and the 2024/1774 standard are the obvious candidates. Whether DORA actually applies to you is a question for legal or compliance, not for me. You can select either way.

**2. Should ISO 22301 be included?** ISO's licence doesn't allow the text to ship with this skill, so I can only use it if you attach your own copy and confirm the licence allows this use. I would cite it by clause number only. If you don't attach it, ISO 22301 will be listed as "not reviewed".

I'll record your answers under Gaps as your own statements, not as sources. Any framework you don't select will also be listed there as "not reviewed".

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep7/runs/check-against-standards/1/run3/work/bc-policy-draft.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/govern.md`
- Glob: `literature/*/*.md`

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

# Review of draft business continuity policy v0.4 against DORA and NIST SP 800-34 Rev. 1

**Sources used, with version and date**
- `bc-policy-draft.md`: *Business continuity policy*, version 0.4, 3 September 2026. Status: draft for the management board. Owner: Chief Operating Officer. No review date (see Gaps).
- `literature/eur-lex/dora-regulation-2022-2554.md`: Regulation (EU) 2022/2554, OJ L 333, 27 December 2022, as adopted. Retrieved and converted 2026-09-10. Reuse is allowed under Decision 2011/833/EU, and EUR-Lex is the authoritative text.
- `literature/nist/sp-800-34r1-contingency-planning-body.md`: NIST SP 800-34 Rev. 1, May 2010, Executive Summary and Chapters 1 to 5 only. Retrieved and converted 2026-09-10. A U.S. Government work. The PDF is the authoritative text.

This is a list of review findings, not a judgement on whether the policy meets either framework. Each point is a question for the policy owner. Points on DORA, which is a regulation, are marked **[legal/compliance]**.

---

## Block 1: DORA, Regulation (EU) 2022/2554

**D1. Management body approval and oversight** [legal/compliance]
- Draft §3: "The Chief Operating Officer owns this policy." Draft §7: "The policy owner reviews this policy every three years."
- DORA Art. 5(2)(e): the management body shall "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy and ICT response and recovery plans".
- Question: The draft gives the management board no role in approving, overseeing or periodically reviewing the policy. Is that role meant to sit in another document, or should this policy assign it?

**D2. Review frequency** [legal/compliance] (contradiction)
- Draft §7: "The policy owner reviews this policy every three years."
- DORA Art. 6(5): "The ICT risk management framework shall be documented and reviewed at least once a year … as well as upon the occurrence of major ICT-related incidents, and following supervisory instructions or conclusions derived from relevant digital operational resilience testing or audit processes." Art. 11(1) places the ICT business continuity policy "as part of the ICT risk management framework". Art. 11(6) adds that entities "shall regularly review their ICT business continuity policy … taking into account the results of tests".
- Question: How does a three-year cycle with no event triggers fit with these review requirements?

**D3. Testing frequency and method** [legal/compliance] (contradiction)
- Draft §5: "Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through."
- DORA Art. 11(6)(a): test the plans "at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions". The same paragraph says that entities other than microenterprises "shall include in the testing plans scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities". Art. 11(6)(b) requires testing of crisis communication plans. Art. 24(4) requires tests to be "undertaken by independent parties, whether internal or external".
- Question: How does a two-yearly desktop walk-through relate to these requirements? Should the policy say who carries out the tests? Whether the 140-staff institution counts as a microenterprise under Art. 3(60) is a question for legal or compliance.

**D4. What the business impact analysis (BIA) covers** [legal/compliance] (gap)
- Draft §4: the BIA is carried out "every three years, covering each payment service and the customer support desk".
- DORA Art. 11(5): the BIA covers "exposures to severe business disruptions" and uses "quantitative and qualitative criteria … internal and external data and scenario analysis". It "shall consider the criticality of identified and mapped business functions, support processes, third-party dependencies and information assets, and their interdependencies". Art. 8(1) requires the classification of functions and assets to be reviewed "as needed, and at least yearly".
- Question: The draft names neither the method nor third-party dependencies, information assets or interdependencies. Where are these defined? Is a three-year cycle for the BIA meant to sit alongside a yearly review of the classification?

**D5. Who sets recovery objectives, and for what** [legal/compliance] (contradiction)
- Draft §6: "The IT manager sets the recovery time objectives for all systems."
- DORA Art. 12(6): "In determining the recovery time and recovery point objectives for each function, financial entities shall take into account whether it is a critical or important function". Art. 5(2)(d) gives the management body responsibility for "the determination of the appropriate risk tolerance level of ICT risk". Art. 6(8)(b) refers to "analysing the impact tolerance for ICT disruptions".
- Question: The draft sets objectives per system rather than per function, mentions no recovery point objectives (RPOs), and gives the decision to the IT manager alone. Is that the intended allocation?

**D6. Critical or important functions** [legal/compliance] (gap)
- Draft §2 lists services in scope but never uses the term or names which functions are critical or important.
- DORA Art. 11(2)(a): arrangements aim to "ensure the continuity of the financial entity's critical or important functions". The term is defined in Art. 3(22).
- Question: Where are the critical or important functions identified?

**D7. Backup** [legal/compliance] (gap)
- The draft does not mention backups.
- DORA Art. 12(1)(a): "backup policies and procedures specifying the scope of the data that is subject to the backup and the minimum frequency of the backup". Art. 12(2) requires periodic testing of backup and restoration.
- Question: Does a separate backup policy exist, and should this policy refer to it?

**D8. Crisis management and communication** [legal/compliance] (gap)
- The draft does not mention them.
- DORA Art. 11(7): entities other than microenterprises "shall have a crisis management function". Art. 11(2)(e) covers communication and crisis management actions and reporting to competent authorities.
- Question: Who holds the crisis management function, and which document covers communication?

**D9. ICT third-party service providers** [legal/compliance] (gap)
- The draft does not mention them.
- DORA Art. 11(4): test business continuity plans "notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers". Art. 5(3) requires a role to monitor those arrangements.
- Question: Are outsourced services, for example around the card processing platform, covered by this policy or by another one?

**D10. Independent audit of recovery plans** [legal/compliance] (gap)
- The draft does not mention audit.
- DORA Art. 11(3): ICT response and recovery plans "shall be subject to independent internal audit reviews" (entities other than microenterprises).
- Question: Should the policy name the internal audit review?

**D11. Learning, training and records** [legal/compliance] (gap)
- The draft does not mention them.
- DORA Art. 13(2) requires post-incident reviews. Art. 13(6) makes ICT security awareness and digital operational resilience training compulsory for all staff. Art. 11(8) requires entities to "keep readily accessible records of activities before and during disruption events".
- Question: Where are these covered?

**D12. Marketing website excluded from scope** [legal/compliance]
- Draft §2: "the marketing website is not" in scope.
- DORA Art. 8(1): entities "shall identify, classify and adequately document all ICT supported business functions … and their roles and dependencies in relation to ICT risk".
- Question: What is the exclusion based on? Does the website share infrastructure or dependencies with the in-scope systems?

---

## Block 2: NIST SP 800-34 Rev. 1 (Chapters 1 to 5)

**N1. Key policy elements the draft does not include** (gap)
- NIST §3.1 lists these key policy elements: "Roles and responsibilities; Scope …; Resource requirements; Training requirements; Exercise and testing schedules; Plan maintenance schedule; and Minimum frequency of backups and storage of backup media."
- The draft covers roles (§3), scope (§2) and a testing schedule (§5). It says nothing about resource requirements, training, a plan maintenance schedule (§7 covers only the policy), or backup frequency and storage.
- Question: Should these be in the policy, or where are they set?

**N2. Testing frequency compared with NIST's sample statement**
- Draft §5: "tested every two years".
- The sample policy statement in NIST §3.1 says: "The plan recovery capabilities and personnel shall be tested annually". It also says plans "must be reviewed annually and updated as necessary". NIST presents this as a sample, not a fixed requirement. §3.5 says the frequency is organisation-defined.
- Question: What is the basis for choosing two years?

**N3. Desktop walk-through for every plan**
- Draft §5: "by a desktop walk-through".
- NIST §3.5.4: "For low-impact systems, a tabletop exercise at an organization-defined frequency is sufficient." For moderate-impact systems "a functional exercise … should include an element of system recovery from backup media". For high-impact systems the exercise "should include a system failover to the alternate location".
- Question: Have the in-scope systems been given impact levels? Does one test method fit all of them?

**N4. Who sets recovery time objectives (RTOs)** (contradiction)
- Draft §6: "The IT manager sets the recovery time objectives for all systems."
- NIST §3.2.1: acceptable downtime is determined by the coordinator "with the process owners, leadership and business managers". Maximum tolerable downtime (MTD) is what "the system owner/authorizing official is willing to accept". It also says "the RTO must normally be shorter than the MTD". The draft mentions neither MTD nor RPO.
- Question: Where do the business owners take part, and where are MTD and RPO set?

**N5. Plan activation authority** (gap)
- The draft does not say who can activate the plans.
- NIST §3.4.6 calls for "a single authoritative role for overall decision-making responsibility, including plan activation".
- Question: Who has the authority to activate the plans?

**N6. Training** (gap)
- The draft does not mention training.
- NIST §3.5.2: "Training should be provided at least annually. Personnel newly appointed to ISCP roles should receive training shortly thereafter."

---

## Questions on clause wording (for the policy owner)

These clauses are ambiguous, hard to enforce, or open to two readings. I have not proposed new wording.

1. **§1** "keeps its payment services running": running at what level? Full service, or a minimum level? Nothing in the draft lets anyone check whether this was achieved.
2. **§2** "The ICT systems that support them are in scope": who decides which systems these are, and where are they listed?
3. **§3** "runs the programme day to day": which decisions can the BCM officer take without the Chief Operating Officer?
4. **§4** "covering each payment service and the customer support desk": §2 also puts the card processing platform and the two offices in scope. Does the BIA cover those too? The clause can be read either way.
5. **§4** "every three years": is the BIA redone after a major change or incident?
6. **§5** "tested every two years": does each plan get tested every two years, or the whole set together? Who tests, who approves the results, and where are they recorded?
7. **§6** "for all systems": does this include systems outside the §2 scope? Who approves the objectives the IT manager sets?
8. **§7** "reviews": does a review lead to re-approval, and by whom? What happens to the policy between reviews if something changes?

## Gaps

- **Draft status.** This is a draft (v0.4, "draft for the management board"). I treated it as evidence of what is proposed, not as current policy.
- **No review date** in the document control. The header gives the owner and version only.
- **ISO 22301.** You answered "All of it", but no copy is attached and the licence for this use hasn't been confirmed. ISO 22301 was **not reviewed**. If you meant "all parts of DORA and NIST SP 800-34", I compared the draft with both texts in full as shipped.
- **Frameworks not selected, and so not reviewed:** Delegated Regulation (EU) 2024/1774, NIST CSF 2.0, UK Cabinet Office *Organisational Resilience Guidance*, FONES minimum standard (2023), AI Act Articles 4, 26 and 50, NIST AI RMF, and ESAs JC 2026 25. The 2024/1774 standard sets out the detail of DORA's ICT business continuity articles, so leaving it out leaves the most specific rules unreviewed.
- **Limits of the source copies.** The NIST file has no appendices (the plan and BIA templates). The DORA file is the text as adopted, and later amendments were not checked.
- **Whether DORA applies, and microenterprise status.** Whether DORA applies (Art. 2(1)(b), payment institutions) and whether the institution falls outside the "other than microenterprises" exceptions are questions for legal or compliance. I haven't assumed either.
- **Your own statements** (not sources): you said "DORA and NIST SP 800-34" and "All of it". The header describes the organisation as "invented for this eval".
- **Text addressed to an AI:** none found in the draft.

Before the draft goes into the board's approval route, take these points to legal, compliance, information security and the policy owner. Send it to the board with its status unchanged. Approval is the board's decision.

---

> Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> Chief Operating Officer answers these, [legal or compliance] the marked points.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Grep: `^### Article (5|6|11|12|13|24|25) `
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Grep: `(annual|at least|policy statement|key policy elements|Roles and responsibilities|Testing schedule|Plan maintenance|Frequency)`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Grep: `^#+ 3\.[5-7]|^#+ 3\.4`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Grep: `Say in the document that AI helped`
