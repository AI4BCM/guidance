# /check-against-standards case 1, run1: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `c8785514-5587-42af-a3b7-9fe7bd1f2c00`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

Before I open `bc-policy-draft.md`, I need to ask one thing.

**What class of data is in the draft, and is this environment approved for it?**

The guidance lists these as high-sensitivity. They may only be handled in an approved corporate or private environment:

- BIA data and risk assessment detail
- incident records and live crisis information
- personal data, contact lists and personnel records
- vulnerabilities and control weaknesses
- recovery strategies and design assumptions
- supplier weaknesses and contractual dependencies
- security-related architecture or site detail
- **board papers and executive-session material**
- audit findings not yet cleared by the audit owner

A policy on its way to the board may already count as a board paper. Please tell me:

1. whether the draft contains any of the above, and
2. if it does, whether your organisation has approved this Claude Code environment for that class.

If it holds high-sensitivity material and this environment isn't approved, I'll stop here. You could then run the check in an approved environment, or attach a version with that material removed. Passwords, keys and access tokens must not go into any tool, approved or not.

Once you've answered, I'll read the draft and ask only what it leaves open. That will be which frameworks to check it against and which parts are in scope.

The policy owner will answer the gap questions I raise, and legal or compliance will answer any I mark for regulatory review. Whether the policy meets a framework stays a person's decision, made against the source text.

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I've read the draft. It's version 0.4, dated 3 September 2026, a draft for the management board, owned by the Chief Operating Officer. It has seven sections: purpose, scope, roles, business impact analysis, testing, recovery objectives and review.

The policy owner will answer each gap question I raise, and legal or compliance will answer the ones I mark as regulatory. Whether the policy meets any framework stays a person's call, made against the source text.

Three questions before I start:

1. **Which frameworks should I check it against?** I can use these:
   - DORA (Regulation 2022/2554)
   - Delegated Regulation 2024/1774 (ICT risk management tools)
   - EU AI Act, Articles 4, 26 and 50 only
   - ESAs JC 2026-25 statement on frontier AI models
   - NIST SP 800-34r1, chapters 1 to 5
   - NIST CSF 2.0
   - NIST AI RMF 1.0
   - Swiss FONES ICT minimum standard 2023
   - UK Cabinet Office organisational resilience guidance

   Since the draft describes a payment institution, DORA and Delegated Regulation 2024/1774 are the obvious candidates, but I'll only use the ones you pick. If you also want me to use your own copy of a licensed standard such as ISO 22301, please confirm the licence allows it. I'd then cite it by clause number only, without quoting it.
2. **Which parts are in scope?** Should I review all seven sections, or only some of them?
3. **Does the draft depend on another document?** It may assume something set out elsewhere, such as a group policy, a separate ICT risk framework or a recovery plan. If so, tell me what it is and I'll record it as your statement, not as a source.

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

From bc-policy-draft.md, version 0.4, dated 3 September 2026, status "draft for the management board", owner Chief Operating Officer.
Compared against DORA, Regulation (EU) 2022/2554, as adopted (Official Journal L 333, 27 December 2022), retrieved 10 September 2026.
Compared against NIST SP 800-34 Rev. 1, May 2010, chapters 1 to 5 only, retrieved 10 September 2026.

# Gap review of the business continuity policy (draft)

This is a review of a draft. It lists gaps and contradictions as questions; it does not judge whether the policy complies with or meets DORA or NIST SP 800-34. Only a person can say that, against the source text.

**Who answers:** the Chief Operating Officer, as policy owner, answers every question. Legal or compliance also answers every point marked **⚖ L/C**. Every DORA point carries that mark because DORA is a regulation. A person, not this review, decides whether the policy meets a framework.

**Intake (your answers):** frameworks are DORA and NIST SP 800-34; all seven sections are in scope. You skipped question 3, so I've assumed the policy stands alone. Any controls held in other documents (an ICT risk management framework, an incident policy, a third-party policy) are unknown to this review.

---

## Block 1: DORA (Regulation (EU) 2022/2554)

### Applicability first

1. **Which DORA regime applies?** ⚖ L/C. Art. 2(1)(b) brings in "payment institutions, including payment institutions exempted pursuant to Directive (EU) 2015/2366". If the company is an *exempted* payment institution, Art. 16(1) disapplies Articles 5 to 15 and applies the simplified framework instead. The findings below assume full Articles 5 to 15. *Policy owner and legal: is the company an authorised or an exempted payment institution?*
2. **Size category.** ⚖ L/C. With 140 staff the company is not a "microenterprise" (Art. 3(60), "fewer than 10 persons"). That means the "other than microenterprises" duties below apply. *Please confirm, and confirm whether it is a "medium-sized enterprise" under Art. 3(64), which depends on turnover.*

### Contradictions (both passages quoted)

3. **How often plans are tested.** ⚖ L/C
   - Policy §5: "Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through."
   - Art. 11(6)(a): "test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions".

   *Will the policy owner change the interval and add the change trigger, or explain how the two-year cycle is meant to sit with Art. 11(6)(a)?*
4. **What kind of test.** ⚖ L/C
   - Policy §5: "by a desktop walk-through".
   - Art. 11(6), second subparagraph: for non-microenterprises, testing plans must include "scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities".

   *Does the policy intend to allow only walk-throughs, or should it name cyber-attack and switchover scenarios?*
5. **How often the policy is reviewed.** ⚖ L/C
   - Policy §7: "The policy owner reviews this policy every three years."
   - Art. 6(5): the ICT risk management framework is "documented and reviewed at least once a year, or periodically in the case of microenterprises, as well as upon the occurrence of major ICT-related incidents".
   - Art. 11(1) makes the ICT business continuity policy part of that framework.

   *Is this policy the ICT business continuity policy under Art. 11(1)? If so, how will annual and incident-triggered review be met?*
6. **Who reviews it.** ⚖ L/C
   - Policy §7 gives review to "The policy owner" (the COO).
   - Art. 5(2)(e): the management body must "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy and ICT response and recovery plans".

   *Should the policy state the management board's approval and periodic review role, not only the COO's?*
7. **Who sets recovery objectives.** ⚖ L/C
   - Policy §6: "The IT manager sets the recovery time objectives for all systems."
   - Art. 12(6): "In determining the recovery time and recovery point objectives for each function, financial entities shall take into account whether it is a critical or important function and the potential overall impact on market efficiency."
   - Art. 6(8)(b) puts "analysing the impact tolerance for ICT disruptions" in the strategy that the management body approves (Art. 5(2)(d)).

   *Are objectives meant to be set per system by IT, or per function, from the BIA and the approved tolerance? Who sets recovery point objectives? The policy does not mention them.*

### Gaps (a DORA passage with no counterpart in the policy)

8. **Critical or important functions.** ⚖ L/C. Art. 11(2)(a) requires arrangements to "ensure the continuity of the financial entity's critical or important functions". The policy never uses the term, and does not say who identifies those functions or how. *Where is this done?*
9. **What the BIA covers.** ⚖ L/C. Art. 11(5) says the BIA "shall consider the criticality of identified and mapped business functions, support processes, third-party dependencies and information assets, and their interdependencies", "by means of quantitative and qualitative criteria, using internal and external data and scenario analysis". Policy §4 covers "each payment service and the customer support desk". *Should the BIA scope name third-party dependencies, information assets and the criteria?* See also question 24.
10. **How often the BIA and classification are refreshed.** ⚖ L/C. Policy §4 says "every three years". Art. 8(1) requires a review "as needed, and at least yearly" of the classification of ICT-supported business functions and assets. Art. 11(5) sets no BIA interval. *Is the three-year BIA meant to sit beside a yearly classification review, and is that written anywhere?*
11. **Response and recovery plans: audit.** ⚖ L/C. Art. 11(3) says these plans "shall be subject to independent internal audit reviews". The policy is silent. *Who audits them?*
12. **Crisis management and communication.** ⚖ L/C. Art. 11(7) requires a "crisis management function". Art. 11(2)(e) and Art. 14 require crisis communication plans and communication policies. Art. 14(3) says "At least one person in the financial entity shall be tasked with implementing the communication strategy for ICT-related incidents and fulfil the public and media function". Art. 11(6)(b) requires testing "the crisis communication plans". §3 (Roles) names none of these. *Where are they assigned?*
13. **Records during disruption.** ⚖ L/C. Art. 11(8) says entities "shall keep readily accessible records of activities before and during disruption events". The policy is silent. *Who keeps them?*
14. **Backup, restoration and redundancy.** ⚖ L/C. Art. 12(1)(a) requires "backup policies and procedures specifying the scope of the data that is subject to the backup and the minimum frequency of the backup". Art. 12(2) requires periodic testing of backup and restoration. Art. 12(3) requires segregated restore systems. Art. 12(4) requires non-microenterprises to "maintain redundant ICT capacities". Art. 12(7) requires integrity checks and reconciliations on recovery. The policy is silent on all of these. *Are they held in another document? If so, which one?*
15. **Testing programme and independent testers.** ⚖ L/C. Art. 24(1) requires a "digital operational resilience testing programme". Art. 24(4) says "tests are undertaken by independent parties, whether internal or external". Art. 24(6) says "at least yearly, that appropriate tests are conducted on all ICT systems and applications supporting critical or important functions". *Does §5 refer to that programme, and who runs the tests?*
16. **TLPT.** ⚖ L/C. Under Art. 26(1) and (8), threat-led penetration testing applies only where the competent authority has identified the entity. *Has it been identified?*
17. **ICT third parties.** ⚖ L/C. The policy says nothing about suppliers. Several DORA articles do:
    - Art. 11(4): test plans "notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers".
    - Art. 28(8): "exit strategies" and "appropriate contingency measures in place to maintain business continuity".
    - Art. 30(3)(c): contracts must require providers "to implement and test business contingency plans".
    - Art. 5(3): a role to monitor these arrangements.

    The card processing platform (§2) may depend on a provider. *How does the policy cover outsourced functions, or which policy does?*
18. **Incident management and reporting.** ⚖ L/C. Art. 17 requires an incident management process. Art. 19 requires reporting major ICT-related incidents. Art. 23 extends these to "operational or security payment-related incidents" for payment institutions. Art. 11(2)(e) links continuity to reporting "in accordance with Article 19". The policy is silent. *Where is the link to incident classification and reporting?*
19. **Learning from tests and incidents.** ⚖ L/C. Art. 11(6), last subparagraph, requires review of the policy "taking into account the results of tests carried out ... and recommendations stemming from audit checks or supervisory reviews". Art. 13(2) requires post-incident reviews. Art. 13(5) says "Senior ICT staff shall report at least yearly to the management body". The policy has no feedback loop. *Should §7 name these as review inputs?*
20. **Training.** ⚖ L/C. Art. 13(6) makes awareness and resilience training "compulsory modules" for "all employees and to senior management staff". Art. 5(4) requires management body members to follow "specific training on a regular basis". The policy is silent. *Is this held elsewhere?*
21. **Independent control function.** ⚖ L/C. Art. 6(4): non-microenterprises "shall assign the responsibility for managing and overseeing ICT risk to a control function" with "an appropriate level of independence". §3 names the COO, the BCM officer and the IT manager, but no control function. *How does this policy relate to that function?*
22. **The marketing website.** ⚖ L/C. §2 puts "the marketing website" out of scope. *Does it support any critical or important function under Art. 3(22), for example customer notices during an outage under Art. 19(3)? If not, is that exclusion recorded with its reason?*

### DORA provisions checked, with no separate finding

- **Art. 7 (systems), Art. 9 (protection), Art. 10 (detection):** these are ICT security duties, and the policy addresses none of them. They are only a gap if this policy is meant to hold them. *Please confirm where they sit.* ⚖ L/C
- **Art. 8(2) to (7), Art. 25, Art. 27, Art. 29, Art. 30(1)–(2) and (4):** these are risk identification, testing method, tester and contract-level duties, with no counterpart in the policy. Same question as above. ⚖ L/C
- **Art. 45:** voluntary information sharing. No finding.
- **Arts. 31–44 and 46–64:** these cover the oversight framework, the authorities, and transitional and amending provisions. They place no duty on the entity's policy, so they were not reviewed.

---

## Block 2: NIST SP 800-34 Rev. 1, chapters 1 to 5

This is guidance, not a regulation, so these points carry no legal mark. Note §1.2: the guide covers information-system contingency plans and "Nor does this document address continuity of mission/business processes." It therefore speaks only to the ICT side of the policy.

### Contradictions

23. **How often plans are tested and reviewed.**
    - Policy §5 says "every two years" and §7 says "every three years".
    - The §3.1 sample policy statement: plans "must be reviewed annually" and "The plan recovery capabilities and personnel shall be tested annually".

    This is a *sample* statement, not a fixed requirement. *Will the owner keep the longer intervals? If so, should the policy record the reason?*
24. **The BIA leaves out what the policy scopes in.**
    - Policy §2 puts "the card processing platform" and "the two offices" in scope.
    - §4's BIA covers only "each payment service and the customer support desk".
    - NIST §3.2.2: the BIA should identify resources including "facilities, personnel, equipment, software, data files, system components, and vital records".

    *Is the platform and are the offices meant to be in the BIA?* (This is also an internal inconsistency in the policy.)
25. **Who sets recovery objectives.**
    - Policy §6: "The IT manager sets the recovery time objectives for all systems."
    - NIST §3.2.1: the coordinator should "with the process owners, leadership and business managers determine the acceptable downtime". NIST defines MTD, RTO and RPO and ties RTO to MTD ("the RTO must normally be shorter than the MTD").

    *Who sets the maximum tolerable downtime and the recovery point objectives? How do §4 (BIA) and §6 (objectives) connect?*
26. **Exercise depth.**
    - Policy §5: "by a desktop walk-through".
    - NIST §3.5.4: "For low-impact systems, a tabletop exercise ... is sufficient". For moderate-impact systems, "a functional exercise ... should include an element of system recovery from backup media". High-impact systems need a full-scale exercise with "a system failover to the alternate location".

    *What impact level does the owner assign to the card processing platform? Does a walk-through match that level?*

### Gaps (NIST §3.1 "Key policy elements" and related sections)

27. **Resource requirements.** NIST §3.1 lists "Resource requirements" as a policy element, and the policy has none. *Should it say who funds and resources the programme?*
28. **Training requirements.** NIST §3.1 lists "Training requirements". §3.5.2 says "Training should be provided at least annually." The policy is silent.
29. **Plan maintenance schedule.** NIST §3.1 lists "Plan maintenance schedule". §3.6 says plans are reviewed "at an organization-defined frequency or whenever significant changes occur", and "When a significant change occurs, the BIA should be updated". §7 covers only the policy itself, every three years, with no change trigger. *Who maintains the plans, how often, and what triggers an off-cycle update?*
30. **Backups.** NIST §3.1 lists "Minimum frequency of backups and storage of backup media". §3.4.2 says "Policies should specify the minimum frequency and scope of backups". The policy is silent.
31. **Scope by function.** NIST §3.1 says scope applies to "common platform types and organization functions (i.e., telecommunications, legal, media relations)". §2 lists services and sites but not these functions. *Are telecoms, legal and media relations in scope?*
32. **Plan activation authority.** NIST §3.4.6 calls for "a single authoritative role for overall decision-making responsibility, including plan activation". §3 names no one who activates a plan. *Who does?* Also: who owns the business continuity plans? §3 names an owner only for the ICT recovery plans.
33. **Senior management in the policy.** NIST §3.1 says senior management "must support a contingency program and be included in the process to develop the program policy". *Is the board's role in shaping the policy, not just approving it, recorded anywhere?*
34. **Preventive controls and alternate sites.** NIST §3.3 (preventive controls) and §3.4.3 (alternate sites) have no counterpart. With two offices, *does the policy intend to say whether each office serves as the other's alternate?*
35. **After-action reports.** NIST §3.5: "results are documented in an after-action report, and Lessons Learned corrective actions are captured". §5 says nothing about recording or acting on test results.
36. **Related plans.** NIST §3.1 and §2.2 say contingency plans are coordinated with other plans, such as crisis communications and cyber incident response. The policy names only "Business continuity plans and ICT recovery plans". *Which other plans exist, and how does this policy relate to them?*

### NIST provisions checked, with no separate finding

- **Chapter 4 (plan structure: activation, recovery and reconstitution phases) and Chapter 5 (platform-specific technical measures):** these describe what a plan contains, not a policy. The policy does not say what a plan must contain. *Should it?*
- **Chapter 2:** background; it feeds questions 33 and 36.

---

## Points no selected text holds (general practice, not in the sources)

37. **Approval record and next review date.** The policy has an owner and a version, but no approval record and no next review date. *Should it carry both once the board decides?*
38. **Definitions.** "Disruption", "business continuity plan" and "ICT recovery plan" are used but not defined. *Should the policy define them?*
39. **Non-compliance and exceptions.** The policy does not say what happens when a plan is not tested on time, or who can grant an exception. *Should it?*

---

## Gaps in this review

- **Other documents (assumed absent):** you skipped question 3, so the policy was read on its own. Many DORA findings may be closed by an ICT risk management framework, an incident policy or a third-party policy that already exists. Sending those documents would settle it.
- **Payment institution status:** this decides whether Articles 5 to 15 or the simplified Article 16 apply (question 1). Not in the sources; legal or compliance settles it.
- **Draft status:** the policy is a draft, version 0.4, dated 3 September 2026. It was reviewed as a draft and is not treated as current policy.
- **Text versions:** the DORA file is the text as adopted in December 2022, not a consolidated version. Legal should confirm against the current text on EUR-Lex. The NIST file is a conversion of chapters 1 to 5 only, with tables shown as raw text. The PDF and EUR-Lex are authoritative.
- **Not reviewed:**
  - Delegated Regulation 2024/1774, which further specifies the Art. 11 business continuity policy components under Art. 15(d) and is likely relevant
  - the AI Act (Articles 4, 26 and 50)
  - NIST CSF 2.0 and NIST AI RMF 1.0
  - Swiss FONES ICT minimum standard
  - UK Cabinet Office guidance
  - ESAs JC 2026-25
  - any licensed standard, such as ISO 22301
- **No embedded instructions:** the policy contained nothing addressed to an AI.

*Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].*

---

**Before the board:** the biggest open questions are 1 (which DORA regime applies), 3 to 7 (contradictions on testing, review and recovery objectives) and 17 to 18 (third parties and incident reporting). They are the most likely to change the text. Send questions 1 to 22 to legal or compliance before the policy enters the board pack. I've edited and recorded nothing; the draft is as you left it.
