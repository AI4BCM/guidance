# /check-against-standards case 1, run3: Claude Code, guidance at c332ccc

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `6759b43f-07ef-4459-8399-fb42ebbf1bc2`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

Before I open `bc-policy-draft.md`, one question. The skill's preflight requires me to ask it first and on its own.

**What class of data does the draft policy hold, and is this environment approved for it?**

The guidance treats the following as high sensitivity, which may only be used in an approved corporate or private environment:

- BIA data and risk assessment detail
- incident records and live crisis information
- personal data, contact lists and personnel records
- vulnerabilities and control weaknesses
- recovery strategies and design assumptions
- supplier weaknesses and contractual dependencies
- security-related architecture or site detail
- **board papers and executive-session material**
- audit findings not yet cleared by the audit owner

The draft is going to the board, so it may count as a board paper. Please confirm one of these:

- **(a)** It holds none of the above, for example a generic policy with no named people, weaknesses or site detail.
- **(b)** It holds high-sensitivity material, and this Claude Code environment is approved for that class by your organisation.

If neither is true, I'll stop here and won't read the file. Also, if the file contains any passwords, keys or access tokens, please remove them first. They don't belong in any tool.

**Who checks the output:** the policy owner answers each gap question I raise. Legal or compliance answers the points I mark for regulatory review. Whether the policy meets any framework stays a person's call, made against the source text. I'll give you a draft in the chat and won't edit or send anything.

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I've read `bc-policy-draft.md`: version 0.4, dated 3 September 2026, status "draft for the management board", owned by the Chief Operating Officer. Since this environment is approved for high-sensitivity data, a medium-class document is fine here.

Before I start, two things the draft doesn't settle:

1. **Which frameworks should I check it against?** Pick any from the list that ships with the skill:
   - DORA (Regulation 2022/2554)
   - Delegated Regulation 2024/1774 (the ICT risk management framework rules under DORA)
   - AI Act, Articles 4, 26 and 50 only
   - ESAs JC 2026-25 statement on frontier AI models
   - NIST SP 800-34r1, chapters 1 to 5
   - NIST CSF 2.0
   - NIST AI RMF 1.0
   - Swiss FONES ICT minimum standard 2023
   - UK Cabinet Office organisational resilience guidance

   You can also use your own copy of a licensed standard such as ISO 22301 if you confirm your licence allows it. In that case I'll cite it by clause number only. The draft describes a payment institution, which is why DORA and 2024/1774 may be relevant, but which frameworks apply is your call, not mine.

2. **Is the whole policy in scope?** That means sections 1–7: purpose, scope, roles, BIA, testing, recovery objectives and review. Or should I check only some of them?

Frameworks you don't pick will be listed as not reviewed. Once you answer, I'll return the gap questions for the policy owner as a draft in the chat, with regulatory points marked for legal or compliance review.

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

Source stamp:
- From "Business continuity policy", version 0.4, 3 September 2026, status "draft for the management board", owner Chief Operating Officer.
- Compared against DORA, Regulation (EU) 2022/2554, as adopted in OJ L 333 of 27 December 2022. The conversion shipped with the skill was retrieved on 10 September 2026.
- Compared against NIST SP 800-34 Rev. 1 (May 2010), Executive Summary and Chapters 1–5 only. The conversion shipped with the skill was retrieved on 10 September 2026.

**Reviewer:** the policy owner (COO) answers each question below, and legal or compliance answers the ones marked **[legal/compliance]**. Whether the policy meets DORA or NIST SP 800-34 is a decision for a person to make against the source text. Nothing below says it does or doesn't.

---

# Draft: gap questions on the BC policy v0.4

## Block 1: DORA (Regulation (EU) 2022/2554)

**Applicability, to settle first**

- **A1 [legal/compliance].** Policy header: "a small payment institution with 140 staff". DORA Art. 2(1)(b) covers "payment institutions, including payment institutions exempted pursuant to Directive (EU) 2015/2366". Under Art. 16(1), "Articles 5 to 15 of this Regulation shall not apply to … payment institutions exempted pursuant to Directive (EU) 2015/2366", which get a simplified framework instead.
  *Question for the policy owner:* is the company an authorised payment institution or an exempted one? Every Art. 5–15 finding below assumes it is authorised. If it is exempted, only Art. 16(1)(a)–(h) applies, and A2–A16 need re-reading against that article.
- **A2 [legal/compliance].** Art. 3(60) defines a microenterprise as one that "employs fewer than 10 persons". With 140 staff, the "other than microenterprises" duties apply, including Art. 11(3), 11(6) second subparagraph, 11(7) and 24.
  *Question:* does legal or compliance agree with this reading?

**Gaps: DORA passages with no counterpart in the policy**

- **A3 [legal/compliance]. Who approves and oversees the policy.** Policy §3 says "The Chief Operating Officer owns this policy." Art. 5(2)(e) says the management body shall "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy and ICT response and recovery plans". The policy names the management board only in its status line.
  *Question:* should the policy say that the management board approves it, oversees it and reviews its implementation, and say how often?
- **A4 [legal/compliance]. ICT business continuity policy.** Under Art. 11(1), the ICT business continuity policy may be "a dedicated specific policy, forming an integral part of the overall business continuity policy". Policy §2 brings the supporting ICT systems into scope but doesn't say whether this document is that ICT policy or sits above one.
  *Question:* is this document the ICT business continuity policy, or does a separate one exist that it should refer to?
- **A5 [legal/compliance]. Critical or important functions.** Art. 11(2)(a) aims to "ensure the continuity of the financial entity's critical or important functions". Art. 8(1) asks the company to "identify, classify and adequately document all ICT supported business functions". Policy §2 and §4 list services but don't identify which are critical or important.
  *Question:* where is that identification made, and should the policy point to it?
- **A6 [legal/compliance]. What the BIA must cover.** Policy §4 covers "each payment service and the customer support desk". Art. 11(5) requires the BIA to "consider the criticality of identified and mapped business functions, support processes, third-party dependencies and information assets, and their interdependencies", and to use "quantitative and qualitative criteria, using internal and external data and scenario analysis".
  *Question:* should §4 name these elements, especially third-party dependencies and information assets?
- **A7 [legal/compliance]. Third-party ICT providers.** The policy doesn't mention ICT third-party service providers. Art. 11(4) asks for testing of ICT business continuity plans "notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers". Art. 5(3) asks for a role "to monitor the arrangements concluded with ICT third-party service providers". Art. 28(2) asks for a strategy on ICT third-party risk.
  *Question:* does the card processing platform or any other in-scope service depend on third parties, and how should the policy cover them?
- **A8 [legal/compliance]. Response and recovery plans, and internal audit.** Policy §3 says "The IT manager owns the ICT recovery plans." Art. 11(3) says those plans "shall be subject to independent internal audit reviews".
  *Question:* should the policy name the internal audit review and who carries it out?
- **A9 [legal/compliance]. Crisis management function.** Art. 11(7) says entities other than microenterprises "shall have a crisis management function". Policy §3 names only the COO, the BCM officer and the IT manager.
  *Question:* who is the crisis management function, and who has authority to activate the plans?
- **A10 [legal/compliance]. Crisis communication.** Art. 14(1) requires "crisis communication plans", Art. 14(3) asks that "At least one person … be tasked with implementing the communication strategy for ICT-related incidents", and Art. 11(6)(b) requires those plans to be tested. The policy doesn't mention communication.
  *Question:* should the policy name the communication role and the plan, and include the plan in testing?
- **A11 [legal/compliance]. Incident reporting to the authority.** Art. 11(2)(e) links the continuity arrangements to reporting "to the competent authorities in accordance with Article 19". Art. 1(1)(a)(iii) covers reporting of "major operational or security payment-related incidents" by payment institutions. The policy doesn't mention reporting.
  *Question:* should the policy say who reports, or point to the incident procedure that does?
- **A12 [legal/compliance]. Backup and restoration.** Art. 12(1) requires "backup policies and procedures specifying the scope of the data that is subject to the backup and the minimum frequency of the backup". Art. 12(4) requires "redundant ICT capacities". The policy covers neither.
  *Question:* where are these set, and should the policy refer to them?
- **A13 [legal/compliance]. Records during disruption and reviews after incidents.** Art. 11(8) asks for "readily accessible records of activities before and during disruption events". Art. 13(2) asks for "post ICT-related incident reviews after a major ICT-related incident". Neither appears in the policy.
  *Question:* should the policy require both?
- **A14 [legal/compliance]. Training.** Art. 13(6) makes "ICT security awareness programmes and digital operational resilience training" compulsory for all staff. Art. 5(4) requires training for members of the management body. The policy says nothing about training.
  *Question:* should it?
- **A15 [legal/compliance]. Who carries out tests and how findings are fixed.** Art. 24(4) asks that "tests are undertaken by independent parties, whether internal or external". Art. 24(5) asks for procedures "to prioritise, classify and remedy all issues revealed". Policy §5 names neither.
  *Question:* who runs the tests, and how are findings tracked to closure?
- **A16 [legal/compliance]. Feeding test results into review.** Art. 11(6), last subparagraph, says the policy is reviewed "taking into account the results of tests … and recommendations stemming from audit checks or supervisory reviews". Policy §7 gives a calendar trigger only.
  *Question:* should §7 add test results, audit findings and supervisory findings as triggers for review?

**Contradictions: both passages quoted**

- **A17 [legal/compliance]. How often plans are tested.** Policy §5: "Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through." Art. 11(6)(a): "test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly". Art. 24(6): "at least yearly, that appropriate tests are conducted on all ICT systems and applications supporting critical or important functions."
  *Question:* how does the two-year cycle fit with these yearly provisions?
- **A18 [legal/compliance]. What kind of test.** Policy §5: "by a desktop walk-through." Art. 11(6), second subparagraph: entities other than microenterprises "shall include in the testing plans scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities".
  *Question:* does a desktop walk-through cover cyber-attack scenarios and switchovers, or does §5 need other test types?
- **A19 [legal/compliance]. How often the policy is reviewed.** Policy §7: "The policy owner reviews this policy every three years." Art. 6(5): "The ICT risk management framework shall be documented and reviewed at least once a year … as well as upon the occurrence of major ICT-related incidents". Art. 11(1) places the ICT business continuity policy "As part of the ICT risk management framework".
  *Question:* how does the three-year cycle fit with the yearly review and the review after major incidents? Policy §7 also has the policy owner reviewing it, while Art. 5(2)(e) gives periodic review to the management body. Who reviews it?
- **A20 [legal/compliance]. Who sets recovery objectives, and on what basis.** Policy §6: "The IT manager sets the recovery time objectives for all systems." Art. 12(6): "In determining the recovery time and recovery point objectives for each function, financial entities shall take into account whether it is a critical or important function". DORA sets them per function, while §6 sets them per system, gives them to the IT manager alone and leaves out RPO.
  *Question:* who should set RTO and RPO, per function or per system, and from which BIA results?
- **A21 [legal/compliance]. How often the BIA and classification are reviewed.** Policy §4: "a business impact analysis every three years". Art. 8(1): "review as needed, and at least yearly, the adequacy of this classification". Art. 8(3) requires a risk assessment "upon each major change".
  *Question:* does the three-year BIA cycle sit alongside a yearly classification review, and is there a trigger for change?

**DORA provisions with no counterpart, left unresolved for the owner**
- Arts. 6–10: the ICT risk management framework, strategy, protection and detection.
- Arts. 17–23: incident management and reporting.
- Art. 26: TLPT, which depends on identification by the authority.
- Arts. 28–30: third-party risk, the register and contract terms.
- Art. 45: information sharing.

A policy wouldn't normally hold these provisions in full, but the document doesn't say where they live.

*Question:* should the policy refer to the documents that cover them?

Arts. 31–44 and 46 onwards concern authorities and critical ICT third-party providers, so they are noted as not applying to the content of this policy. This is subject to legal confirmation.

## Block 2: NIST SP 800-34 Rev. 1 (Chapters 1–5)

This is US federal guidance for information systems, not a regulation, so none of these points is marked for legal review.

**Gaps against the key policy elements in §3.1** ("Key policy elements are as follows")

- **N1. Resource requirements.** The policy doesn't mention resources.
  *Question:* should it say who funds and resources the programme?
- **N2. Training requirements.** The policy doesn't mention training. §3.5.2 says "Training should be provided at least annually."
  *Question:* should the policy set training for people who have roles in the plans?
- **N3. Plan maintenance schedule.** Policy §7 schedules review of the policy, not maintenance of the plans. §3.6 asks for review "at an organization-defined frequency or whenever significant changes occur".
  *Question:* who maintains the BC and ICT recovery plans, and when?
- **N4. "Minimum frequency of backups and storage of backup media".** The policy has no counterpart.
  *Question:* should it set a minimum, or point to where one is set?
- **N5. Scope by organisation function.** §3.1 asks for scope covering "organization functions (i.e., telecommunications, legal, media relations)". Policy §2 lists services, offices and ICT systems.
  *Question:* are telecommunications, legal and media relations in or out of scope?
- **N6. Senior management involvement.** §3.1 says "senior management, most likely the CIO, must support a contingency program and be included in the process to develop the program policy."
  *Question:* who in senior management, other than the COO, took part in drafting?

**Contradictions or tensions: both passages quoted**

- **N7. Who sets recovery objectives.** Policy §6: "The IT manager sets the recovery time objectives for all systems." §3.2.1: the ISCP Coordinator, "with the process owners, leadership and business managers determine the acceptable downtime". MTD "represents the total amount of time the system owner/authorizing official is willing to accept", and "the RTO must normally be shorter than the MTD".
  *Question:* should RTOs follow from a tolerable downtime set by business owners, and who sets that?
- **N8. Test depth.** Policy §5: "by a desktop walk-through." §3.5.4: "For low-impact systems, a tabletop exercise … is sufficient". Moderate-impact systems call for "a functional exercise" that includes "system recovery from backup media", and high-impact systems a full-scale exercise with "a system failover to the alternate location".
  *Question:* what impact level does each in-scope system have, and is a desktop walk-through enough for each?
- **N9. Plan activation authority.** §3.4.6 calls for "a single authoritative role for overall decision-making responsibility, including plan activation". Policy §3 doesn't name who activates.
  *Question:* who does?
- **N10. BIA update on change.** Policy §4 sets a fixed three-year cycle. §3.6 says "When a significant change occurs, the BIA should be updated".
  *Question:* should §4 add a trigger for change?
- **N11. Lessons from tests.** §3.5 says "results are documented in an after-action report, and Lessons Learned corrective actions are captured".
  *Question:* should policy §5 require an after-action report and corrective actions?

**Unresolved:** Chapter 4 covers plan development (activation, recovery and reconstitution phases), and Chapter 5 covers technical considerations by platform. Both speak to plan content, which isn't in the attachments.

*Question:* do the ICT recovery plans that the IT manager owns cover these points? That can't be checked from the policy.

## Points not in the selected sources

- **G1 (general practice, not in the sources).** The policy has an owner, a version and a date but no next review date and no approval record.
  *Question:* should those be added before it goes to the board?
- **G2 (general practice, not in the sources).** Policy §1 speaks of "a disruption" but doesn't define one or say what triggers the policy.
  *Question:* should it define what counts as a disruption?

## Gaps

- **Document under review:** v0.4, 3 September 2026, status "draft for the management board". It's a draft, so it isn't treated as current policy.
- **Your answers, recorded as your own statements and not as sources:**
  - Data class: medium. This environment is approved for high.
  - Frameworks: DORA and NIST SP 800-34.
  - Scope: the whole policy, §§1–7.
- **Not settled by the sources:**
  - Whether the company is authorised or exempted under Directive (EU) 2015/2366 (see A1). Its authorisation record would settle it.
  - Impact levels per system (N8). Not in the sources.
  - Which functions are critical or important (A5). Not in the sources.
- **Contents of the policy:** the policy describes the organisation as "invented for this eval". If it is used for a real entity, the applicability findings (A1, A2) depend on that entity's real status.
- **Not reviewed:**
  - Delegated Regulation 2024/1774. DORA Art. 15(d) says further rules will "specify further the components of the ICT business continuity policy referred to in Article 11(1)", so selecting it may add findings.
  - AI Act Arts. 4, 26 and 50.
  - NIST CSF 2.0.
  - NIST AI RMF 1.0.
  - Swiss FONES ICT minimum standard.
  - UK Cabinet Office guidance.
  - ESAs JC 2026-25.
  - Any licensed standard.
- **Instructions aimed at an AI** in the attached file: none found.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

This is a chat draft and I haven't changed `bc-policy-draft.md`. Before the board sees the policy, legal or compliance needs to answer A1, whether the company is authorised or exempted. That answer decides whether A2–A21 apply as written.
