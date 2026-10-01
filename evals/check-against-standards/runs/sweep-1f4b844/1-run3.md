# /check-against-standards case 1, run3: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `2a1aac85-2987-4f9d-a2ec-3e2190db128e`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

Before I open `bc-policy-draft.md`, I need one thing from you.

**What class of data is in the draft, and is this environment approved for it?**

Under the AI4BCM data rules, a draft policy review is usually **medium to high** sensitivity. It counts as **high** if it contains any of these:

- board papers or executive-session material (a draft headed for the board may already count as one)
- BIA or risk-assessment detail, recovery strategies or design assumptions
- vulnerabilities, control weaknesses, or supplier weaknesses and contractual dependencies
- personal data, contact lists, or details of security architecture or sites
- audit findings the audit owner hasn't cleared yet

High-sensitivity material may only go into an approved corporate or private environment. Please tell me the class, and confirm this environment is approved for it (retention, privacy terms and permissions). If it isn't approved, I'll stop here and won't read the file. Passwords, keys or tokens shouldn't be in the file whatever the answer.

Once you confirm, I'll read the draft. I'll then ask only what it leaves open: its status and date, which of the bundled frameworks to check it against (DORA, NIST CSF 2.0, the Swiss ICT minimum standard and others), and which parts are in scope.

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I've read `bc-policy-draft.md`, v0.4 of 3 September 2026, a draft for the management board owned by the Chief Operating Officer. It has seven short sections: purpose, scope, roles, BIA, testing, recovery objectives and review. It contains no instructions aimed at an AI.

**Reviewer:** the COO, as policy owner, answers each question I raise. Legal or compliance answers the ones I mark as regulatory. Whether the policy meets any framework is a person's call, made against the source text. I won't make it.

Three questions before I start:

1. **Which frameworks should I check it against?** These ship with the skill:
   - DORA (Regulation 2022/2554)
   - Delegated Regulation 2024/1774 (DORA ICT risk management detail)
   - NIST SP 800-34r1, chapters 1–5
   - NIST CSF 2.0
   - NIST AI RMF 1.0
   - AI Act, Articles 4, 26 and 50 only
   - Swiss FONES ICT minimum standard 2023
   - UK Cabinet Office organisational resilience guidance
   - ESAs JC 2026-25 statement on frontier AI models

   The draft calls the company a payment institution, but whether DORA applies to it is for legal or compliance to confirm, not me. Tell me if you'd like it included anyway. Frameworks you don't pick will be listed as "not reviewed".
2. **Do you also want it checked against a licensed standard, such as ISO 22301?** If so, attach your own copy and confirm the licence allows this use. I'd cite it by clause number only.
3. **Which parts are in scope?** All seven sections, or only some (for example, just testing and recovery objectives)?

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

I've read the draft and the two frameworks. Here is the review.

---

**Sources read**
- `bc-policy-draft.md`: Business continuity policy v0.4, 3 September 2026, status "draft for the management board", owner Chief Operating Officer. This is the document under review, not a current source.
- `dora-regulation-2022-2554.md`: Regulation (EU) 2022/2554 as adopted, OJ L 333 of 27 December 2022, retrieved 10 September 2026. It's a Markdown conversion, and EUR-Lex is authoritative.
- `sp-800-34r1-contingency-planning-body.md`: NIST SP 800-34 Rev. 1, May 2010, Executive Summary and chapters 1–5 only, retrieved 10 September 2026. The PDF is authoritative.

**Reviewer:** the COO, as policy owner, answers each question below. Legal or compliance answers the ones marked ⚖. Whether this policy meets DORA or SP 800-34 is for a person to decide against the source text, and this review doesn't say either way. The draft's status stays "draft for the management board".

Scope: all seven sections, against DORA and NIST SP 800-34r1.

---

## Block 1: DORA (Regulation 2022/2554)

Every point in this block is marked ⚖ for legal or compliance review.

**Applicability, before anything else**

1. ⚖ **Which DORA regime applies?** Art. 2(1)(b) brings in "payment institutions, including payment institutions exempted pursuant to Directive (EU) 2015/2366". Art. 16(1) says "Articles 5 to 15 of this Regulation shall not apply to … payment institutions exempted pursuant to Directive (EU) 2015/2366", which get the simplified framework instead. The policy (header) says only "a small payment institution with 140 staff". *Is the institution authorised or exempted? The answer decides whether points 2–16 or point 17 apply.*
2. ⚖ **Microenterprise status.** Many duties below apply only to "financial entities, other than microenterprises". Art. 3(60) defines a microenterprise as one that "employs fewer than 10 persons". *Can legal confirm that the full regime applies, given the policy's stated 140 staff?*

**Contradictions (both passages quoted)**

3. ⚖ **How often plans are tested.** The policy (§5) says: "Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through." DORA Art. 11(6)(a) says: "test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions". Art. 24(6) adds: "at least yearly, that appropriate tests are conducted on all ICT systems and applications supporting critical or important functions." *How does the two-year cycle square with these, and what triggers a test after a substantive change?*
4. ⚖ **What kind of test.** The policy (§5) names "a desktop walk-through" only. Art. 11(6), second subparagraph, requires testing plans to include "scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities". Art. 24(4) says "tests are undertaken by independent parties, whether internal or external". *Which test types, scenarios and testers will the policy require?*
5. ⚖ **How often the policy is reviewed.** The policy (§7) says: "The policy owner reviews this policy every three years." Art. 11(6), last subparagraph, says: "Financial entities shall regularly review their ICT business continuity policy … taking into account the results of tests … and recommendations stemming from audit checks or supervisory reviews". Art. 6(5) says the ICT risk management framework (which Art. 11(1) says includes the ICT business continuity policy) "shall be documented and reviewed at least once a year … as well as upon the occurrence of major ICT-related incidents". *Is a three-year cycle intended, and what triggers an earlier review?*

**Gaps (DORA passage with no counterpart in the policy)**

6. ⚖ **Role of the management body.** Art. 5(2)(e) says the management body shall "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy and ICT response and recovery plans". §3 names the COO as owner but gives the board no role. *Should the policy state the board's approval, oversight and review role?*
7. ⚖ **ICT business continuity policy.** Art. 11(1) asks for "a comprehensive ICT business continuity policy, which may be adopted as a dedicated specific policy, forming an integral part of the overall business continuity policy". *Is this document meant to be that policy, or is there a separate one? If separate, how does this policy reference it?*
8. ⚖ **Critical or important functions.** Art. 11(2)(a) speaks of ensuring "the continuity of the financial entity's critical or important functions" (definition in Art. 3(22)). §2 lists services and sites but doesn't say which functions are critical or important, or how that is decided. *Where is this determined?*
9. ⚖ **What the BIA covers.** Art. 11(5) says the BIA assesses "severe business disruptions by means of quantitative and qualitative criteria, using internal and external data and scenario analysis" and considers "business functions, support processes, third-party dependencies and information assets, and their interdependencies". §4 covers "each payment service and the customer support desk" and says nothing on criteria, third parties, ICT assets or interdependencies. *Should §4 name these?* DORA gives no BIA frequency in Art. 11(5), but Art. 8(1) and 8(2) require yearly review of the classification of functions and of risk scenarios. *How does the three-year BIA cycle relate to these?*
10. ⚖ **Recovery objectives.** §6 says: "The IT manager sets the recovery time objectives for all systems." Art. 12(6) says: "In determining the recovery time and recovery point objectives for each function, financial entities shall take into account whether it is a critical or important function and the potential overall impact on market efficiency." *Should objectives be set per function rather than per system? Where do recovery point objectives sit? How are both tied to the BIA (Art. 11(5): ICT assets "designed and used in full alignment with the BIA")?* Who sets these values is for the owners to decide. This review doesn't propose any.
11. ⚖ **Backup and restoration.** Art. 12(1)–(4) requires backup policies "specifying the scope of the data … and the minimum frequency of the backup", restoration procedures, periodic testing, segregated restore systems and redundant ICT capacity. The policy is silent. *Is this covered elsewhere, and should the policy refer to it?*
12. ⚖ **ICT third-party providers.** Art. 11(4) asks for plans "notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers". Art. 5(2)(h) has the management body approve the policy on ICT third-party services. "The card processing platform" is in scope (§2), but the policy doesn't say who runs it. *Are any in-scope services provided by third parties, and how does the policy cover them?*
13. ⚖ **Crisis management and communication.** Art. 11(7) requires "a crisis management function". Art. 11(2)(e) and Art. 14 require communication actions and crisis communication plans, and Art. 14(3) says "At least one person … shall be tasked with implementing the communication strategy". Art. 11(6)(b) requires those plans to be tested. The policy has no counterpart. *Where are these set?*
14. ⚖ **Incident response and reporting.** Art. 11(2)(b)–(e) asks for response, containment, impact estimation and reporting "to the competent authorities in accordance with Article 19". Art. 11(8) asks for "readily accessible records of activities before and during disruption events". The policy is silent. *Should it refer to the incident process and its records?*
15. ⚖ **Independent audit of the plans.** Art. 11(3) says ICT response and recovery plans "shall be subject to independent internal audit reviews". *Should §3 or §5 say who audits the plans the IT manager owns?*
16. ⚖ **Learning, reporting and training.** Art. 13(2) asks for post-incident reviews. Art. 13(5) says "Senior ICT staff shall report at least yearly to the management body". Art. 13(6) makes awareness and resilience training compulsory for all staff and senior management. The policy is silent on all three. *Are these covered elsewhere?*
17. ⚖ **Only if Art. 16 applies (see point 1).** Art. 16(1)(f) requires "business continuity plans and response and recovery measures, which include, at least, back-up and restoration measures". Art. 16(1)(g) requires testing "on a regular basis". Art. 16(1)(e) requires identifying "key dependencies on ICT third-party service providers". Art. 16(2) requires review "periodically and upon the occurrence of major ICT-related incidents". *Would the policy then need to cover backup, third-party dependencies and incident-triggered review?*

---

## Block 2: NIST SP 800-34 Rev. 1 (chapters 1–5)

SP 800-34r1 is guidance for US federal information systems, not a regulation, so nothing here is marked ⚖. Its references to FIPS 199 and federal continuity (COOP) are federal context. Whether to adopt it at all is the owner's choice.

**Key policy elements (§3.1)**

§3.1 lists "Roles and responsibilities; Scope …; Resource requirements; Training requirements; Exercise and testing schedules; Plan maintenance schedule; and Minimum frequency of backups and storage of backup media."

18. **Present in part:** roles (policy §3), scope (§2), and the testing schedule (§5). **Absent:** resource requirements, training requirements, a plan maintenance schedule (§7 covers only review of the policy itself) and backup frequency and storage. *Should the policy add the four missing elements?*

**Contradictions**

19. **Testing frequency against the sample statement.** SP 800-34 §3.1 includes a sample policy statement: "The plan recovery capabilities and personnel shall be tested annually". The same sample says the plan "must be reviewed annually". The policy (§5 and §7) says "every two years" for testing and "every three years" for review. It's a sample, not a requirement. *Is the longer cycle a deliberate choice, and where is the reason recorded?*
20. **Who sets recovery times.** The policy (§6) says: "The IT manager sets the recovery time objectives for all systems." SP 800-34 §3.2.1 says the coordinator, "with the process owners, leadership and business managers determine the acceptable downtime". It defines MTD as "the total amount of time the system owner/authorizing official is willing to accept". *Should business owners and leadership be part of setting RTOs, and who sets MTD and RPO?*

**Gaps**

21. **What the BIA produces.** §3.2 gives three steps: recovery criticality with MTD, RTO and RPO; resource requirements; and "recovery priorities for system resources". §3.6 says "When a significant change occurs, the BIA should be updated". Policy §4 gives only a fixed three-year cycle. *Should §4 name its outputs and a trigger for updates after a change?*
22. **Test depth and lessons learned.** §3.5.4 says "For low-impact systems, a tabletop exercise … is sufficient". For moderate-impact systems it calls for a functional exercise with "an element of system recovery from backup media", and for high-impact systems a full-scale exercise with "a system failover to the alternate location". Policy §5 sets a desktop walk-through for everything. §3.5 also says "results are documented in an after-action report". *Does the organisation rate its systems by impact, and should test depth follow that rating? Where do test results and corrective actions go?*
23. **Training.** §3.5.2 says: "Training should be provided at least annually. Personnel newly appointed to ISCP roles should receive training shortly thereafter." The policy is silent. *Should it set training requirements?*
24. **Authority to activate plans.** §3.4.6 calls for "a single authoritative role for overall decision-making responsibility, including plan activation", with designated alternates for team leaders. Policy §3 names owners but no activation authority and no deputies. *Who can activate the plans, and who stands in for them?*
25. **Plan maintenance.** §3.6 says the plan "should be reviewed for accuracy and completeness at an organization-defined frequency or whenever significant changes occur", and covers version control and a record of changes. *Should the policy set this for the BC and ICT recovery plans?*
26. **Links to other policies.** §3.1 says contingency plans "should be coordinated with related organization-wide policies and programs, including information system security, physical security, human resources, system operations, and emergency preparedness functions". The policy names none. *Which related policies should it reference?*

---

## General practice, not in the sources

27. *General practice, not in the sources:* the policy has an owner, a version and a date, but no next review date, approval record or change history. *Should these be added before it goes to the board?*
28. *General practice, not in the sources:* §2 excludes "the marketing website" but gives no reason. *Is the exclusion recorded with its reason, and has anyone checked whether customers or payment flows depend on that site?*
29. *General practice, not in the sources:* the policy uses terms such as "disruption" and "recovery time objectives" without defining them. *Should it define its terms or point to a glossary?*

---

## Gaps in this review

- **Your answers, which I've treated as your statements, not as sources:** frameworks are DORA and NIST SP 800-34; scope is all of the policy. You didn't answer the question about a licensed standard (such as ISO 22301), so I've assumed none was selected and none was checked.
- **Not reviewed** (bundled but not selected): Delegated Regulation 2024/1774, the AI Act (Arts 4, 26, 50), NIST CSF 2.0, NIST AI RMF 1.0, the Swiss FONES ICT minimum standard, the UK Cabinet Office organisational resilience guidance, and the ESAs JC 2026-25 statement. ⚖ DORA Art. 15(d) provides for technical standards that will "specify further the components of the ICT business continuity policy". I haven't checked whether the bundled Delegated Regulation 2024/1774 is that standard or what it adds. Legal may want it selected before the board meeting.
- The DORA file is the text as adopted in 2022. I didn't check for later amendments; that's not in the sources.
- The SP 800-34 appendices (BIA template, plan templates, TT&E detail) aren't in the bundled file, so they weren't reviewed.
- The draft contains no instructions aimed at an AI, so there was nothing to escalate to information security.

This is a set of questions for the owner, not text for the policy, so it doesn't carry the AI-disclosure sentence. If any of this goes into the board paper, add the sentence from `keep-it-running.md` with skill `check-against-standards`, version `2026.11.0`.
