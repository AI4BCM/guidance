# /check-against-standards case 1, run2: Claude Code, guidance at c332ccc

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `54a43b7f-f3f7-4e07-ad39-0a8e6a6d73e8`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

Before I open `bc-policy-draft.md`, I need one answer from you.

**What class of data does the draft hold, and is this environment approved for that class?**

Our data rules (`units/data-rules.md`, Sensitivity classes) say some material may only go into an approved corporate or private environment. That includes:

- board papers and executive-session material (this draft is going to the board, so it may already count)
- BIA data and risk assessment detail
- recovery strategies and design assumptions
- vulnerabilities and control weaknesses
- supplier weaknesses and contractual dependencies
- security-related architecture or site detail
- personal data and contact lists
- audit findings the audit owner hasn't cleared yet

Please tell me the class. If the draft holds any of the above, also confirm that this Claude Code session is an environment your organisation has approved for it. If it isn't approved, I'll stop here and won't read the file.

Once that's settled, I'll read the draft and ask you up to three questions about anything it leaves open. Those cover its status and date, which of the bundled frameworks to check it against, and which parts are in scope.

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I've read the draft. It's `bc-policy-draft.md`, version 0.4, dated 3 September 2026, a draft for the management board, owned by the Chief Operating Officer. That answers status and date, so I won't ask about them.

**Who reviews my output:** the policy owner (the COO) answers each gap question. Legal or compliance answers the ones I mark as regulatory. Only a person, checking against the source text, can say whether the policy meets a framework. I'll give you gaps and questions in the chat, not a verdict, and I won't change the file.

Three questions before I start:

1. **Which frameworks should I check the draft against?** These ship with the skill:
   - DORA (Regulation 2022/2554)
   - Delegated Regulation 2024/1774
   - NIST SP 800-34r1, chapters 1–5
   - NIST CSF 2.0
   - NIST AI RMF 1.0
   - AI Act, Articles 4, 26 and 50 only
   - Swiss FONES ICT minimum standard 2023
   - UK Cabinet Office organisational resilience guidance
   - ESAs JC 2026-25 statement on frontier AI models

   You can also use your own licensed copy of a standard, such as ISO 22301, if you confirm the licence allows it. I'd cite it by clause number only. As a payment institution, DORA and 2024/1774 are the obvious candidates, but which ones to use is your choice.
2. **Which parts are in scope?** All seven sections, or only some, such as BIA, testing and recovery objectives?
3. **If you pick DORA or 2024/1774: which regime does the institution fall under?** The full ICT risk management framework, or the simplified one in DORA Article 16 and Title III of 2024/1774? That decides which provisions I compare the draft against. If you don't know, I'll compare against both and flag it for legal or compliance.

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

I have the draft and the relevant parts of both frameworks open, and I'm writing up the findings now.

From `bc-policy-draft.md` version 0.4, 3 September 2026, a draft for the management board, owned by the COO. Compared against DORA, Regulation (EU) 2022/2554, retrieved 10 September 2026, and NIST SP 800-34 Rev. 1, May 2010, chapters 1–5, retrieved 10 September 2026.

**Reviewer:** the policy owner (COO) answers each question. Legal or compliance answers the ones marked ⚖. Only a person, checking against the source text, can say whether the policy meets either framework. This is a list of gaps, not a verdict.

---

## Block 1: DORA (`literature/eur-lex/dora-regulation-2022-2554.md`)

Every DORA point is marked ⚖ for legal or compliance review. The comparison assumes the full ICT risk management regime in Articles 5–15 (see Gaps).

### Contradictions (both passages quoted)

**D1. Testing frequency and method.** Policy §5 says: "Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through."
- Art. 11(6)(a): "test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions".
- Art. 11(6), second subparagraph: entities other than microenterprises "shall include in the testing plans scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities".
- Art. 24(6): "at least yearly, that appropriate tests are conducted on all ICT systems and applications supporting critical or important functions."
- → *COO:* how do you reconcile a two-yearly desktop walk-through with yearly testing that includes cyber-attack and switchover scenarios? ⚖

**D2. Policy review cycle.** Policy §7 says: "The policy owner reviews this policy every three years."
- Art. 6(5): the ICT risk management framework "shall be documented and reviewed at least once a year … as well as upon the occurrence of major ICT-related incidents, and following supervisory instructions or conclusions derived from relevant digital operational resilience testing or audit processes."
- Art. 11(1): the ICT business continuity policy is part of that framework.
- Art. 11(6), last subparagraph: the policy is reviewed "taking into account the results of tests … and recommendations stemming from audit checks or supervisory reviews."
- → *COO:* is this policy part of the framework that Art. 6(5) requires to be reviewed yearly? If so, what replaces the three-year cycle, and what triggers an earlier review? ⚖

**D3. Who reviews.** Policy §7 gives review to "The policy owner" (the COO).
- Art. 5(2)(e): the management body shall "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy and ICT response and recovery plans".
- → *COO:* should §3 and §7 give the management body its approval and periodic review role, rather than leaving review with the COO alone? ⚖

**D4. Recovery objectives.** Policy §6 says: "The IT manager sets the recovery time objectives for all systems."
- Art. 12(6): "In determining the recovery time and recovery point objectives for each function, financial entities shall take into account whether it is a critical or important function and the potential overall impact on market efficiency."
- Art. 5(2)(d): the management body sets "the appropriate risk tolerance level of ICT risk".
- The policy sets objectives per system, by one IT role, with no recovery point objective and no link to the BIA in §4. DORA speaks of objectives per function.
- → *COO:* who sets recovery time and recovery point objectives per function, on what basis, and who approves them? ⚖

### Gaps (a provision with no counterpart in the draft)

**D5. Is this the ICT business continuity policy?** Art. 11(1) requires "a comprehensive ICT business continuity policy, which may be adopted as a dedicated specific policy, forming an integral part of the overall business continuity policy".
- → *COO:* is this draft that policy, or does a separate ICT policy exist? If it is separate, what is its version and date? ⚖

**D6. Critical or important functions.** Art. 11(2)(a) aims to "ensure the continuity of the financial entity's critical or important functions". Art. 8(1) requires entities to identify and classify "all ICT supported business functions".
- The draft speaks of "payment services" and never identifies critical or important functions.
- → *COO:* where are the critical or important functions identified, and should the policy refer to them? ⚖

**D7. What the policy's arrangements must cover.** Art. 11(2)(b)–(e) lists: incident response, containment plans, preliminary impact estimation, and "communication and crisis management actions … and report to the competent authorities in accordance with Article 19."
- None of these appears in the draft.
- → *COO:* where does the policy require each of them? ⚖

**D8. BIA content and frequency.** Policy §4 says: "every three years, covering each payment service and the customer support desk."
- Art. 11(5) requires "quantitative and qualitative criteria, using internal and external data and scenario analysis" and consideration of "third-party dependencies and information assets, and their interdependencies".
- Art. 8(1) and 8(2) require yearly review of classification and risk scenarios.
- Internally, §2 includes "the card processing platform" and "the two offices", but §4 does not name them in the BIA's coverage.
- → *COO:* should the BIA cover third parties, information assets and both offices, and run more often than every three years or on change? ⚖

**D9. Third parties.** Art. 11(4) requires testing of continuity plans "notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers".
- Other relevant provisions: Art. 28(2) (strategy on ICT third-party risk), Art. 28(8) (exit strategies) and Art. 5(3) (a role to monitor third-party arrangements).
- The draft says nothing about third parties.
- → *COO:* is the card processing platform, or any other in-scope service, provided by a third party? Where does the policy deal with third-party continuity and exit? ⚖

**D10. Backup, restoration and redundancy.** Art. 12(1)–(4) requires:
- backup policies "specifying the scope of the data … and the minimum frequency of the backup"
- restoration on segregated systems
- tested backup procedures
- redundant ICT capacities for entities other than microenterprises

  Art. 12(7) adds data-integrity checks on recovery. None appears in the draft.
- → *COO:* does the policy refer to a backup policy, or should it set these requirements? ⚖

**D11. Independent audit.** Art. 11(3) says ICT response and recovery plans "shall be subject to independent internal audit reviews". Art. 6(6) requires the framework to be "subject to internal audit by auditors on a regular basis". The draft is silent.
- → *COO:* what does the policy say about internal audit? ⚖

**D12. Crisis management and communication.**
- Art. 11(7) requires "a crisis management function".
- Art. 14(1) requires "crisis communication plans".
- Art. 14(3) says "At least one person … shall be tasked with implementing the communication strategy".
- Art. 11(6)(b) requires testing of the crisis communication plans.

  §3 names none of these roles.
- → *COO:* who holds the crisis management function and the communication role? ⚖

**D13. Independent control function.** Art. 6(4) requires a "control function" for ICT risk with "an appropriate level of independence". §3 names the COO, the BCM officer and the IT manager, and the IT manager both owns and sets recovery.
- → *COO:* where does the independent control function sit relative to these roles? ⚖

**D14. Incident management and reporting.**
- Art. 17(1) requires "an ICT-related incident management process".
- Art. 19(1) requires reporting of major ICT-related incidents.
- Art. 23 extends Chapter III to "operational or security payment-related incidents" at payment institutions.

  The draft is silent.
- → *COO:* should the policy link continuity to the incident process and to reporting duties? ⚖

**D15. Records, lessons learned and training.**
- Art. 11(8): "readily accessible records of activities before and during disruption events".
- Art. 13(2): post-incident reviews.
- Art. 13(5): yearly reporting to the management body.
- Art. 13(6): compulsory training "applicable to all employees and to senior management staff".

  None appears in the draft.
- → *COO:* where are these required? ⚖

**D16. Testing programme.** Art. 24(1), (4) and (5) require a testing programme, testing "by independent parties", and procedures to "remedy all issues revealed". Art. 25(1) lists test types. The draft has only §5.
- → *COO:* does a separate testing programme exist, and should the policy refer to it? ⚖

**D17. Out-of-scope website.** §2 says "the marketing website is not" in scope. Art. 8(1) covers "all ICT supported business functions", and Art. 11(6)(a) covers testing of "ICT systems supporting all functions".
- → *COO:* is this exclusion consistent with those provisions? Does the website share infrastructure with in-scope systems? ⚖

**Unresolved (stated, not compared):**
- Art. 26 (TLPT) applies only if the competent authority identifies the entity, and the sources don't say whether it has.
- Chapters V Section II to IX are addressed mainly to authorities and the ESAs, so I did not compare them as policy requirements.
- Art. 45 (information sharing) is voluntary.

---

## Block 2: NIST SP 800-34 Rev. 1, chapters 1–5 (`literature/nist/sp-800-34r1-contingency-planning-body.md`)

This is guidance, not regulation, so these points carry no legal mark. Per §1.3, it is written for federal systems but "may be used by private and commercial organizations".

### Contradictions

**N1. Testing frequency and depth.** Policy §5 calls for a desktop walk-through every two years.
- The sample policy statement in §3.1 says: "The plan recovery capabilities and personnel shall be tested annually".
- §3.5.4 says a tabletop is "sufficient" only "For low-impact systems". Moderate-impact systems need "a functional exercise" that includes "system recovery from backup media". High-impact systems need a "full-scale functional exercise" with "a system failover to the alternate location".
- → *COO:* which impact level do the payment platform and card processing systems have, and is one desktop method enough for all of them?

**N2. Who sets recovery objectives.** Policy §6 has the IT manager setting RTOs alone.
- §3.2.1 says the coordinator should, "with the process owners, leadership and business managers determine the acceptable downtime". It also says "the RTO must normally be shorter than the MTD".
- → *COO:* who sets the maximum tolerable downtime, and how are RTOs tied to it and to the BIA?

**N3. BIA cycle.** Policy §4 sets a fixed three-year cycle. §3.6 says: "When a significant change occurs, the BIA should be updated with the new information".
- → *COO:* should a significant change trigger a BIA update?

### Gaps (against §3.1 "Key policy elements")

**N4. Missing policy elements.** §3.1 lists "Roles and responsibilities; Scope … ; Resource requirements; Training requirements; Exercise and testing schedules; Plan maintenance schedule; and Minimum frequency of backups and storage of backup media."
- The draft covers roles (§3), scope (§2) and testing schedule (§5).
- It has nothing on resource requirements, training requirements, a plan maintenance schedule (§7 covers only the policy itself), or backup frequency and storage.
- → *COO:* should the policy add these four elements?

**N5. Scope by function.** §3.1 describes scope "as applies to common platform types and organization functions (i.e., telecommunications, legal, media relations)". §2 doesn't mention these functions.
- → *COO:* are they in scope?

**N6. RPO and MTD.** §3.2.1 defines MTD, RTO and RPO. The draft names only recovery time objectives.
- → *COO:* should the policy require RPO and MTD too?

**N7. Authority to activate.** §3.4.6 calls for "a single authoritative role for overall decision-making responsibility, including plan activation". It says a senior management official "has the ultimate authority to activate the plan". §3 names no one with activation authority.
- → *COO:* who activates the plans?

**N8. Lessons learned.** §3.5 says results are "documented in an after-action report, and Lessons Learned corrective actions are captured". The draft is silent.
- → *COO:* should the policy require after-action reports?

**N9. Training.** §3.5.2 says "Training should be provided at least annually." The draft is silent.
- → *COO:* what training does the policy require?

**N10. Coordination with other plans.** §3.1 says plans should be "coordinated with related organization-wide policies and programs, including information system security, physical security, human resources". The draft names none.
- → *COO:* which related policies should it refer to?

**N11. Plan content.** Chapter 4 describes the activation and notification, recovery and reconstitution phases. Chapter 5 covers backup, alternate sites and high availability. These are plan-level, and the draft has no counterpart.
- → *COO:* should the policy require plans to contain these phases, or does that sit in a lower-level standard?

---

## Gaps

- **Your answers (your statements, not sources):** frameworks are DORA and NIST SP 800-34; scope is all seven sections.
- **Question 3 (which DORA regime applies) was skipped.** I assumed the full Articles 5–15 regime. The draft says the institution has "140 staff", which puts it above the "fewer than 10 persons" in Art. 3(60), so the "other than microenterprises" provisions were applied.
  - If the institution is a "payment institution exempted pursuant to Directive (EU) 2015/2366", Art. 16(1) disapplies Articles 5–15. Then points (a)–(h) of Art. 16(1) apply instead, including "(g) test, on a regular basis" and Art. 16(2) "reviewed periodically". D1–D4 and D10–D13 would then need to be re-read against Art. 16. ⚖
  - What would settle it: the authorisation status, confirmed by legal or compliance.
- **The document under review is a draft:** version 0.4, 3 September 2026, for the management board. It was reviewed as a draft, not as current policy.
- **Not reviewed:** AI Act (Arts 4, 26, 50), Delegated Regulation 2024/1774, NIST CSF 2.0, NIST AI RMF 1.0, Swiss FONES ICT minimum standard, UK Cabinet Office guidance, ESAs JC 2026-25. 2024/1774 is the delegated act DORA Art. 15 points to for further BC policy components. It was not selected, so I didn't use it.
- **NIST SP 800-34 appendices** (templates, BIA template, control summary) aren't carried in the bundled file, so I didn't compare against them.
- **Not in the sources:** whether the card processing platform is outsourced; the systems' FIPS 199-style impact levels; whether a separate ICT continuity policy, backup policy or testing programme exists. The COO's answers to D5, D9, D10, D16 and N1 would settle these.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next step:** take D1–D17 to legal or compliance and the full list to the COO before the draft goes to the board. I haven't changed the draft file.
