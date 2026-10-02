# /check-against-standards case 1, run1: Claude Code, guidance at c332ccc

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `12bba3db-f9a9-4b3c-9cd0-11fa55588761`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

Before I open `bc-policy-draft.md`, I need one answer from you.

**What class of data is in the draft, and is this environment approved for it?**

Policy review is rated medium to high sensitivity. It may run only in an enterprise or private environment that is approved for that data (`units/tools.md`, Selection guide). The draft counts as **high sensitivity** if it holds any of the following (`units/data-rules.md`, Sensitivity classes):

- board papers or executive-session material. A draft written for the board may fall here.
- BIA data or details of the risk assessment
- weaknesses in vulnerabilities, controls or suppliers, or contractual dependencies
- recovery strategies or design assumptions
- details of security-related architecture or sites
- personal data, contact lists or personnel records

Please tell me:
1. Whether the draft is low, medium or high sensitivity.
2. Whether this Claude Code session is approved for that class in your organisation.

If it's high sensitivity and this environment isn't approved for it, I'll stop here and won't open the file. Once you confirm, I'll read the draft. Then I'll ask only what it leaves open: which frameworks to check it against and which parts are in scope.

**Who reviews the result:** the policy owner answers each gap question. Legal or compliance answers the points marked for regulatory review. Only a person, working from the source text, can decide whether the policy meets a framework or is ready for the board.

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I've read `bc-policy-draft.md`: version 0.4, dated 3 September 2026, a draft for the management board, owned by the Chief Operating Officer. It has seven short sections, Purpose through Review. The status and date are clear, so I only need two answers before I check it.

**1. Which frameworks should I check it against?** Pick any of these. The skill has their texts:
- AI Act, Articles 4, 26 and 50 only
- DORA (Regulation 2022/2554)
- Delegated Regulation 2024/1774 (ICT risk management framework under DORA)
- NIST SP 800-34r1, chapters 1 to 5 (contingency planning)
- NIST CSF 2.0
- NIST AI RMF 1.0
- Swiss FONES ICT minimum standard 2023
- UK Cabinet Office organisational resilience guidance
- ESAs JC 2026-25 statement on frontier AI models
- or your own licensed copy of a standard such as ISO 22301. Please confirm the licence allows this use. I would cite it by clause number only.

The draft describes the company as a payment institution. That makes DORA and Delegated Regulation 2024/1774 the likeliest candidates. Whether they apply to you is for legal or compliance to confirm, not me.

**2. Which parts are in scope?** All seven sections, or only some (for example sections 4 to 7: BIA, testing, recovery objectives and review)?

Once I have your answers, I'll draft one block per framework. Each gap and contradiction will be a question for the policy owner, with regulatory points marked for legal or compliance review. I won't say whether the policy meets a framework or is ready for the board.

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

from bc-policy-draft.md, version 0.4, 3 September 2026, status "draft for the management board", owner Chief Operating Officer
compared against DORA (Regulation (EU) 2022/2554, Official Journal L 333, 27 December 2022), the skill's copy retrieved 2026-09-10
compared against NIST SP 800-34 Rev. 1 (May 2010), chapters 1 to 5 only, the skill's copy retrieved 2026-09-10

# Gap review: business continuity policy draft v0.4

**Reviewer:** the policy owner (Chief Operating Officer) answers every question. Points marked **⚖ legal/compliance** go to legal or compliance as well. Whether the policy meets DORA or NIST SP 800-34 is for a person to decide against the source text. This review does not decide it.

Wording in quotation marks is copied exactly from the source. DORA is reused under Commission Decision 2011/833/EU, source EUR-Lex. NIST SP 800-34 is a US Government work.

## Block 1: DORA (Regulation (EU) 2022/2554)

Articles compared with the draft: 2, 3(60), 5, 6, 8, 11, 12, 13, 14, 16 and 24. Everything else is listed under Gaps.

**D1. Which DORA regime applies.** ⚖ legal/compliance
- Draft §0: "a small payment institution with 140 staff".
- DORA Art. 2(1)(b) covers "payment institutions, including payment institutions exempted pursuant to Directive (EU) 2015/2366".
- Art. 16(1) disapplies Articles 5 to 15 for "payment institutions exempted pursuant to Directive (EU) 2015/2366".
- Art. 3(60) defines a microenterprise as one that "employs fewer than 10 persons".
- The draft doesn't say which regime it was written for.
- *Question:* Is the company an exempted payment institution under Art. 16, or under the full Articles 5 to 15? Should the policy say so? Every finding below assumes the full regime.

**D2. Management body's role.** ⚖ legal/compliance
- Draft §3: "The Chief Operating Officer owns this policy."
- Draft §7: "The policy owner reviews this policy every three years."
- Art. 5(2)(e) says the management body shall "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy and ICT response and recovery plans".
- *Question:* Where does the policy give the management body its role in approving, overseeing and periodically reviewing the policy and the ICT response and recovery plans?

**D3. ICT business continuity policy.** ⚖ legal/compliance
- Draft §2: "The ICT systems that support them are in scope".
- Art. 11(1) requires "a comprehensive ICT business continuity policy, which may be adopted as a dedicated specific policy, forming an integral part of the overall business continuity policy".
- *Question:* Is this document meant to be the ICT business continuity policy, or does a separate one exist? If separate, should this policy name it?

**D4. Critical or important functions.** ⚖ legal/compliance
- Draft §1 and §2 refer to "payment services" and list services, the platform, the support desk and the offices.
- Art. 11(2)(a) aims to "ensure the continuity of the financial entity's critical or important functions".
- Art. 12(6) ties recovery objectives to "whether it is a critical or important function".
- *Question:* Which of the in-scope services are the company's critical or important functions, and where does the policy, or a document it refers to, identify them?

**D5. What the BIA covers.** ⚖ legal/compliance
- Draft §4: the BIA covers "each payment service and the customer support desk".
- Draft §2 also puts in scope "the card processing platform", "the two offices" and the supporting ICT systems.
- Art. 11(5): "The BIA shall consider the criticality of identified and mapped business functions, support processes, third-party dependencies and information assets, and their interdependencies."
- *Question:* Should the BIA in §4 also cover the platform, the offices, the ICT systems and third-party dependencies, to match §2 and Art. 11(5)?

**D6. How often the BIA and its inputs are refreshed.** ⚖ legal/compliance
- Draft §4: the BIA is carried out "every three years".
- Art. 8(1): "review as needed, and at least yearly, the adequacy of this classification and of any relevant documentation".
- Art. 8(2): "review on a regular basis, and at least yearly, the risk scenarios impacting them".
- *Question:* How does the three-year BIA cycle relate to the yearly reviews in Art. 8(1) and 8(2)? Should a significant change also trigger a BIA?

**D7. How often plans are tested, and how.** ⚖ legal/compliance. *These passages contradict each other.*
- Draft §5: "Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through."
- Art. 11(6)(a): "test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions".
- Art. 11(6), second subparagraph (for entities other than microenterprises): "include in the testing plans scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities".
- Art. 24(6): "at least yearly, that appropriate tests are conducted on all ICT systems and applications supporting critical or important functions".
- *Question:* How does the two-year desktop walk-through square with the yearly, change-triggered testing in Art. 11(6)(a) and 24(6)? How does a walk-through cover the cyber-attack and switchover scenarios?

**D8. Testing crisis communication and backups.** ⚖ legal/compliance
- The draft has no passage on either.
- Art. 11(6)(b): "test the crisis communication plans established in accordance with Article 14".
- Art. 12(2): "Testing of the backup procedures and restoration and recovery procedures and methods shall be undertaken periodically."
- *Question:* Should §5 cover testing of crisis communication plans and of backup and restoration procedures?

**D9. Recovery objectives.** ⚖ legal/compliance
- Draft §6: "The IT manager sets the recovery time objectives for all systems."
- Art. 12(6): "In determining the recovery time and recovery point objectives for each function, financial entities shall take into account whether it is a critical or important function and the potential overall impact on market efficiency."
- The draft sets objectives per system, not per function. It names no recovery point objective and doesn't link either objective to the BIA.
- *Question:* Who should set the recovery time and recovery point objectives per function, on what basis, and who approves them? (This review does not propose any values.)

**D10. How often the policy is reviewed.** ⚖ legal/compliance. *These passages contradict each other.*
- Draft §7: "The policy owner reviews this policy every three years."
- Art. 6(5): the ICT risk management framework "shall be documented and reviewed at least once a year … as well as upon the occurrence of major ICT-related incidents, and following supervisory instructions or conclusions derived from relevant digital operational resilience testing or audit processes".
- Art. 11(6), last subparagraph: "regularly review their ICT business continuity policy and ICT response and recovery plans, taking into account the results of tests … and recommendations stemming from audit checks or supervisory reviews".
- *Question:* Does the three-year cycle still apply when the policy forms part of the ICT risk management framework? Should incidents, test results, audit findings and supervisory findings trigger a review?

**D11. Backup policy.** ⚖ legal/compliance
- The draft has no passage on this.
- Art. 12(1)(a): "backup policies and procedures specifying the scope of the data that is subject to the backup and the minimum frequency of the backup".
- *Question:* Should this policy cover backup, or refer to a backup policy elsewhere?

**D12. Crisis management and communication.** ⚖ legal/compliance
- The draft has no passage on this.
- Art. 11(7) requires "a crisis management function".
- Art. 14(1) requires "crisis communication plans".
- Art. 14(3): "At least one person in the financial entity shall be tasked with implementing the communication strategy for ICT-related incidents and fulfil the public and media function for that purpose."
- *Question:* Who leads crisis management and crisis communication, and should §3 name them?

**D13. ICT third-party providers.** ⚖ legal/compliance
- The draft has no passage on this.
- Art. 11(4): "periodically test appropriate ICT business continuity plans, notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers".
- *Question:* Does the card processing platform or any other in-scope service depend on an ICT third-party provider, and should the policy cover continuity for those arrangements?

**D14. Internal audit, activation records, incident reviews and training.** ⚖ legal/compliance
- The draft has no passage on any of these.
- Art. 11(3): response and recovery plans "shall be subject to independent internal audit reviews".
- Art. 11(8): "keep readily accessible records of activities before and during disruption events".
- Art. 13(2): "post ICT-related incident reviews after a major ICT-related incident".
- Art. 13(5): "Senior ICT staff shall report at least yearly to the management body".
- Art. 13(6): training as "compulsory modules in their staff training schemes".
- *Question:* Which of these should the policy assign to a role, and which belong in other documents? If other documents, should the policy point to them?

## Block 2: NIST SP 800-34 Rev. 1, chapters 1 to 5

This is a guidance document for US federal information systems, not a regulation, so none of these points are marked for legal review. Its "must" wording is written for federal agencies.

**N1. Key elements of a policy statement.**
- §3.1 lists the "Key policy elements" as:
  - "Roles and responsibilities": present in draft §3
  - "Scope": present in draft §2
  - "Resource requirements": absent
  - "Training requirements": absent
  - "Exercise and testing schedules": present in draft §5
  - "Plan maintenance schedule": absent (§7 covers only the policy itself)
  - "Minimum frequency of backups and storage of backup media": absent
- *Question:* Should the policy add resource requirements, training requirements, a plan maintenance schedule and a minimum backup frequency?

**N2. How often the sample statement reviews and tests.** *These passages contradict each other.*
- Draft §5: tested "every two years".
- Draft §7: reviewed "every three years".
- §3.1 sample policy statement: plans "must be reviewed annually and updated as necessary" and "The plan recovery capabilities and personnel shall be tested annually to identify weaknesses of the capability."
- *Question:* Are the two-year and three-year intervals a deliberate choice against this annual sample, and on what basis?

**N3. Who sets downtime and recovery objectives.**
- Draft §6: "The IT manager sets the recovery time objectives for all systems."
- §3.2.1: "with the process owners, leadership and business managers determine the acceptable downtime".
- §3.2.1 also says "the RTO must normally be shorter than the MTD" and defines the RPO separately. The draft names neither the MTD nor the RPO.
- *Question:* Should process owners and management set maximum tolerable downtime from the BIA, with recovery time objectives derived from it, rather than the IT manager alone? Who sets recovery point objectives?

**N4. Test method, triggers and lessons learned.**
- Draft §5: "by a desktop walk-through", with no other triggers.
- §3.5: "Organizations should conduct TT&E events periodically, following organizational or system changes".
- §3.5: "results are documented in an after-action report".
- §3.5.4: a tabletop exercise is "sufficient" only "For low-impact systems". Moderate-impact systems call for a functional exercise "to include an element of system recovery from backup media". High-impact systems call for a full-scale exercise that "should include a system failover to the alternate location".
- *Question:* What impact level does the card processing platform carry? Should the test method in §5 vary with impact, be triggered by changes, and end in an after-action report?

**N5. Training.**
- The draft has no passage on this.
- §3.5.2: "Training should be provided at least annually. Personnel newly appointed to ISCP roles should receive training shortly thereafter."
- *Question:* Should the policy set training for people with continuity roles?

**N6. Who activates the plans.**
- Draft §3 names an owner, a programme lead and an ICT plan owner, but nobody who activates the plans.
- §3.4.6: "a single authoritative role for overall decision-making responsibility, including plan activation".
- *Question:* Who has authority to activate the business continuity and ICT recovery plans?

**N7. Updates on significant change.**
- Draft §4 and §7 use fixed cycles only.
- §3.6: plans reviewed "whenever significant changes occur to any element of the plan".
- §3.6: "When a significant change occurs, the BIA should be updated with the new information".
- *Question:* Should the policy require out-of-cycle updates to the BIA and plans after significant change?

**N8. Links to related plans and policies.**
- The draft has no passage on this.
- §3.1: plans "should be coordinated with related organization-wide policies and programs, including information system security, physical security, human resources, system operations, and emergency preparedness functions".
- *Question:* Which related policies (information security, incident management, outsourcing) should this policy refer to?

**Not compared:** chapters 4 and 5 (how a plan is built, and technical considerations for client/server, telecoms and mainframe systems). They describe what goes into a plan, not into a policy, so I matched no policy passage against them. Whether any of it belongs in the policy is for the owner to decide.

## Points no selected source holds

- *General practice, not in the sources:* the draft gives an owner, version and date but no next review date and no approval record. Should the version going to the board carry both?
- *General practice, not in the sources:* the draft defines none of the terms it uses (business continuity plan, ICT recovery plan, recovery time objective). Should it have a short definitions section?

## Gaps

- **Your own statements (not sources):**
  - The draft is medium sensitivity, and this environment is approved for high.
  - The frameworks selected are DORA and NIST SP 800-34.
  - All of the policy is in scope.
- **The document under review is a draft.** bc-policy-draft.md is v0.4, dated 3 September 2026, a "draft for the management board". I reviewed it as a proposal, not as the policy in force. The current approved policy, if any, wasn't attached: not in the sources.
- **The draft says the organisation is "invented for this eval".** *Question:* Is the organisation description in §0 final wording for the board version?
- **DORA articles not compared with this draft:** Chapter III (incident management and reporting, Articles 17 to 23), Articles 25 to 27 (testing tools and threat-led penetration testing), Chapter V (ICT third-party risk, Articles 28 to 44), and Chapters VI to IX. Whether any belongs in a BC policy is for the policy owner and legal or compliance to decide. Answering D1 decides whether Article 16 replaces Articles 5 to 15.
- **Delegated Regulation 2024/1774** sets out what the ICT business continuity policy and testing must contain (DORA Article 15(d) to (f)). It wasn't selected, so it was not reviewed. It would settle much of D3, D7 and D8.
- **Not reviewed, because not selected:** AI Act (Articles 4, 26, 50), NIST CSF 2.0, NIST AI RMF 1.0, Swiss FONES ICT minimum standard 2023, UK Cabinet Office organisational resilience guidance, ESAs JC 2026-25 statement.
- **NIST SP 800-34 coverage:** the skill's copy holds chapters 1 to 5 only. The appendices (sample plan templates and the BIA template) are not in the sources.
- **What would settle the open points:** the company's critical or important function list, any existing ICT business continuity policy and backup policy, the ICT third-party register, and legal's view on D1.

Parts of this document were drafted with AI support (check-against-standards skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

That's 14 DORA points and 8 NIST points. Three are direct contradictions:
- **Testing:** every two years in the draft against at least yearly in DORA Art. 11(6)(a) (D7).
- **Policy review:** every three years in the draft against at least once a year in DORA Art. 6(5) (D10).
- **Review and test intervals:** two and three years in the draft against annual in the NIST §3.1 sample statement (N2).

Before the board sees the draft, three answers decide the most: legal's view on D1 (which DORA regime applies), and the policy owner's answers on D4 (which services are critical or important functions) and D9 (who sets recovery objectives).

I haven't changed the draft.
