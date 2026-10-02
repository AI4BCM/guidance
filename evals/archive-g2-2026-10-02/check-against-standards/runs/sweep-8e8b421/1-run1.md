# /check-against-standards case 1, run1: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `1bbaff58-0f49-40cc-8286-b114d5ce3507`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

Before I open `bc-policy-draft.md`, I need to know how sensitive it is. This environment has to be approved for that level of data before I read the file.

**What class of data does the draft policy contain?** In particular, does it include any of these?

- board papers or executive-session material (since it's going to the board, it may already count as one)
- vulnerabilities or control weaknesses
- recovery strategies or design assumptions
- BIA data or risk assessment detail
- supplier weaknesses or contractual dependencies
- security-related architecture or site detail
- personal data, contact lists or personnel records

If it holds any of these, it counts as high-sensitivity. Please also confirm that this Claude Code environment is approved for that class of data. If the policy holds none of them, tell me that and I'll go ahead. If the environment isn't approved for its class, I'll stop here and won't read the file.

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

Thanks. I've read `bc-policy-draft.md`, version 0.4, dated 3 September 2026, status "draft for the management board", owner the Chief Operating Officer. It doesn't contain any embedded instructions.

**Who reviews this:** the COO, as policy owner, answers each question I raise. Legal or compliance answer the ones I mark as regulatory. Only a person, checking against the source text, can say whether the policy meets a framework. My output will be a draft in this chat, and I won't change the file.

I need three answers before I start:

1. **Which frameworks should I check the policy against?** These are the ones I have with me:
   - DORA (Regulation 2022/2554)
   - Delegated Regulation 2024/1774 (DORA ICT risk management framework)
   - AI Act, Articles 4, 26 and 50 only
   - NIST SP 800-34r1, chapters 1 to 5 (contingency planning)
   - NIST CSF 2.0
   - NIST AI RMF 1.0
   - Swiss FONES ICT minimum standard 2023
   - UK Cabinet Office organisational resilience guidance
   - ESAs JC 2026-25 statement on frontier AI models
2. **Do you want me to use a licensed standard, such as ISO 22301?** If so, please attach your own copy and confirm that its licence allows you to use it here. I'd refer to it by clause number only and wouldn't quote it.
3. **Which parts of the policy are in scope?** It could be all seven sections, or only some of them, for example sections 4 to 6 (business impact analysis, testing and recovery objectives).

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

From bc-policy-draft.md v0.4, dated 3 September 2026, status "draft for the management board", owner Chief Operating Officer. I compared it against DORA, Regulation (EU) 2022/2554, as adopted in OJ L 333 on 27 December 2022 (copy retrieved 10 September 2026). I also compared it against NIST SP 800-34 Rev. 1, May 2010 (copy retrieved 10 September 2026), using the Executive Summary and Chapters 1 to 5 only.

**Reviewer:** the COO, as policy owner, answers each question below. Legal or compliance answer every question marked **[L/C]**. Whether the policy meets DORA or SP 800-34 is a decision for a person to make against the source text. This review doesn't make that call.

---

## DORA (Regulation 2022/2554)

**Applicability [L/C].** The policy says the company is "a small payment institution with 140 staff". Payment institutions are covered under Art. 2(1)(b). Art. 16(1) says that "Articles 5 to 15 of this Regulation shall not apply to … payment institutions exempted pursuant to Directive (EU) 2015/2366". At 140 staff the company isn't a microenterprise under Art. 3(60), which means "employs fewer than 10 persons".
→ *For the COO and legal/compliance:* is the company an exempted payment institution? If it is, the simplified framework in Art. 16 applies and several of the points below change.

### Gaps

1. **Board role [L/C].** Section 3 names the COO, the BCM officer and the IT manager, but no role for the board. Art. 5(2)(e) says the management body shall "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy and ICT response and recovery plans".
   → Should section 3 give the management board this approval, oversight and review role?
2. **ICT business continuity policy [L/C].** Art. 11(1) asks for "a comprehensive ICT business continuity policy, which may be adopted as a dedicated specific policy, forming an integral part of the overall business continuity policy". The draft doesn't say whether it is that policy, contains it, or refers to a separate one.
   → Which is it?
3. **Critical or important functions [L/C].** Art. 11(2)(a) aims to "ensure the continuity of the financial entity's critical or important functions", a term defined in Art. 3(22). Section 2 lists services and sites, but nothing in the policy identifies the critical or important functions.
   → Where is that identification made, and should the policy refer to it?
4. **What the BIA covers [L/C].** Art. 11(5) says "The BIA shall consider the criticality of identified and mapped business functions, support processes, third-party dependencies and information assets, and their interdependencies", using "quantitative and qualitative criteria … and scenario analysis". Section 4 covers "each payment service and the customer support desk". It doesn't mention the card processing platform, the offices, third parties or ICT assets, although section 2 puts these in scope.
   → Should section 4 cover everything that section 2 puts in scope, including third-party dependencies?
5. **ICT backup and redundancy [L/C].** Art. 12(1)(a) requires "backup policies and procedures specifying the scope of the data that is subject to the backup and the minimum frequency of the backup". Art. 12(4) requires firms to "maintain redundant ICT capacities". The policy doesn't mention backup or redundancy.
   → Should it, or should it point to the document that covers them?
6. **Independent audit of ICT recovery plans [L/C].** Art. 11(3) says ICT response and recovery plans "shall be subject to independent internal audit reviews". Section 3 assigns the plans to the IT manager and says nothing about audit.
   → Who audits the ICT recovery plans?
7. **Third parties and exit [L/C].** Art. 11(4) requires testing of ICT business continuity plans "notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers". Art. 28(8) says "financial entities shall put in place exit strategies". The draft doesn't mention suppliers.
   → Should the policy cover ICT third-party dependencies and exit?
8. **Crisis management and communication [L/C].** Art. 11(7) requires "a crisis management function". Art. 11(6)(b) requires firms to "test the crisis communication plans established in accordance with Article 14". Art. 14(3) says "At least one person in the financial entity shall be tasked with implementing the communication strategy for ICT-related incidents". The draft has no crisis role and no communication plan.
   → Who holds these roles, and should the policy name them?
9. **Records, lessons and training [L/C].** Art. 11(8) requires firms to "keep readily accessible records of activities before and during disruption events". Art. 13(2) requires "post ICT-related incident reviews". Art. 13(6) requires "ICT security awareness programmes and digital operational resilience training as compulsory modules". The policy covers none of these.
   → Are they covered elsewhere, or should this policy cover them?
10. **Incident management and reporting [L/C].** Art. 17(1) and Art. 23 apply incident management and reporting to "operational or security payment-related incidents" at payment institutions. The draft doesn't mention incidents.
    → Is there a separate incident policy that this one should refer to?

### Contradictions

11. **How often and how plans are tested [L/C].** Section 5 says: "Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through."
    Art. 11(6)(a) requires firms to "test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions". Firms that aren't microenterprises must also include "scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities". Art. 24(6) adds that firms must ensure "at least yearly, that appropriate tests are conducted on all ICT systems and applications supporting critical or important functions". Art. 24(4) requires that "tests are undertaken by independent parties, whether internal or external".
    → How should section 5 set the test frequency, the test types, the triggers for extra tests and who runs the tests?
12. **Who sets recovery objectives, and for what [L/C].** Section 6 says: "The IT manager sets the recovery time objectives for all systems."
    Art. 12(6) says: "In determining the recovery time and recovery point objectives for each function, financial entities shall take into account whether it is a critical or important function and the potential overall impact on market efficiency."
    → Are objectives set per system or per function? Who sets them, and from what input? The policy doesn't mention recovery point objectives (RPO); where are those set? Setting the values themselves stays with their owners.
13. **How often the policy is reviewed [L/C].** Section 7 says: "The policy owner reviews this policy every three years."
    Art. 6(5) says the ICT risk management framework is "reviewed at least once a year" and "as well as upon the occurrence of major ICT-related incidents". Art. 11(6) says firms "shall regularly review their ICT business continuity policy … taking into account the results of tests … and recommendations stemming from audit checks or supervisory reviews". If this draft is, or contains, the ICT business continuity policy (see point 2), the two passages don't match.
    → What review cycle and triggers should section 7 set?
14. **How often the BIA is done [L/C].** Section 4 says the BIA is done "every three years". Art. 8(1) says firms shall "review as needed, and at least yearly, the adequacy of this classification" of ICT-supported functions and assets. Art. 8(2) says firms shall review the risk scenarios "at least yearly".
    → Does a three-year BIA cycle work alongside these yearly reviews?

---

## NIST SP 800-34 Rev. 1, Chapters 1 to 5

**Applicability.** The guide is titled "Contingency Planning Guide for Federal Information Systems". In section 3.1 it says "The policy must reflect the FIPS 199 impact levels". The draft has no system impact levels.
→ Is SP 800-34 being used as a reference or as a target? How should its federal categorisation translate to this company's systems?

### Gaps

15. **Policy elements (3.1).** Section 3.1 lists key policy elements. Four of them have no counterpart in the draft: "Resource requirements", "Training requirements", "Plan maintenance schedule" and "Minimum frequency of backups and storage of backup media".
    → Should the policy cover each of these?
16. **Plan activation (3.4.6).** Section 3.4.6 calls for "a single authoritative role for overall decision-making responsibility, including plan activation". Section 3 of the draft names no one with authority to activate a plan.
    → Who decides to activate a plan?
17. **Alternate site (3.4.3).** Section 3.4.3 says "for all FIPS 199 moderate- or high-impact systems, the plan should include a strategy to recover and perform system operations at an alternate facility for an extended period". The draft names two offices but no alternate-site strategy.
    → Should it have one?
18. **Training (3.5.2).** Section 3.5.2 says "Training should be provided at least annually." The draft doesn't mention training.
    → Should the policy set a training requirement?
19. **Plan maintenance (3.6).** Section 3.6 says plans should be "reviewed for accuracy and completeness at an organization-defined frequency or whenever significant changes occur to any element of the plan". Section 7 of the draft sets a review only for the policy itself.
    → Who reviews the plans, how often, and what triggers an extra review?

### Contradictions

20. **Who sets recovery objectives (3.2.1).** Section 6 of the draft says: "The IT manager sets the recovery time objectives for all systems."
    Section 3.2.1 says the coordinator, "with the process owners, leadership and business managers determine the acceptable downtime", and that "the RTO must normally be shorter than the MTD". The draft defines no maximum tolerable downtime (MTD) and no recovery point objective (RPO).
    → Should the business process owners take part in setting RTOs, and where are the MTD and RPO set?
21. **BIA triggers (3.6).** Section 4 of the draft says the BIA is done "every three years". Section 3.6 says "When a significant change occurs, the BIA should be updated".
    → Should the policy add a change trigger for the BIA?
22. **Test types (3.5, 3.5.4).** Section 5 of the draft says plans are tested "every two years, by a desktop walk-through".
    Section 3.5.4 says "For low-impact systems, a tabletop exercise at an organization-defined frequency is sufficient". For moderate-impact systems, "a functional exercise … should be conducted". High-impact systems need a full-scale exercise that "should include a system failover to the alternate location". Section 3.5 adds that TT&E events (tests, training and exercises) should also follow "organizational or system changes". The sample policy statement in section 3.1, which is an example rather than a requirement, reads: "The plan recovery capabilities and personnel shall be tested annually".
    → Should the type and frequency of tests depend on how critical each system is?

---

## General practice, not in the sources

23. The draft has no next review date and no approval record, only a version number and a status. Should it get both before it goes to the board?
24. Section 2 excludes the marketing website without giving a reason. Should the reason be recorded, and does the website support any payment or customer service?
25. Sections 3 to 6 name no deputies for the BCM officer or the IT manager. Who acts when one of them isn't available?

---

## Coverage by policy section

| Draft section | DORA | SP 800-34 |
|---|---|---|
| 1 Purpose | 3 | — |
| 2 Scope | 3, 4, 7 | applicability note |
| 3 Roles | 1, 6, 8 | 16 |
| 4 BIA | 4, 14 | 21 |
| 5 Testing | 11 | 22 |
| 6 Recovery objectives | 12 | 20 |
| 7 Review | 13 | 19 |
| Not addressed in the draft | 2, 5, 9, 10 | 15, 17, 18 |

## Gaps in this review

- **Your answers, as you gave them.** These are your statements, not sources:
  - Frameworks: "DORA and NIST SP 800-34".
  - "All of it". I've read this as all seven sections of the policy being in scope. If you meant something else, tell me.
  - You didn't answer the question about a licensed standard, so I've assumed none was used. ISO 22301 and similar standards were not reviewed.
- **The policy is a draft** (v0.4, "draft for the management board"). I reviewed it as written. None of its sections is in force yet.
- **Not reviewed:** AI Act Arts. 4, 26 and 50; Delegated Regulation 2024/1774; NIST CSF 2.0; NIST AI RMF 1.0; Swiss FONES 2023; UK Cabinet Office guidance; ESAs JC 2026-25.
  - DORA Art. 15(d) to (f) and Art. 16(3) hand the detailed content of the ICT business continuity policy, the testing and the plans to regulatory technical standards. Delegated Regulation 2024/1774 is the technical standard that holds that detail. Legal/compliance may want it reviewed before the board meeting.
- **DORA coverage.** I compared the policy against the provisions of Chapters II to V of DORA that bear on business continuity: Arts. 5, 6, 8, 11 to 14, 16, 17, 23, 24 and 28. The rest of the Regulation (classification and reporting detail, TLPT, the oversight framework, and the chapters on authorities and penalties) is about supervision or is out of the policy's reach. I list it here as not compared.
- **SP 800-34 coverage.** Appendices A to G (templates, BIA template, controls) aren't in the shipped copy, so they were not reviewed.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

Next step: send the questions marked **[L/C]** to legal/compliance, starting with the applicability question, because it decides which DORA articles apply at all. The COO answers the rest before the draft goes to the board. I haven't edited the policy file.
