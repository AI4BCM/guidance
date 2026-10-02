# /check-against-standards case 1, run2: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `4d1b5810-c916-46f9-b978-c95731bd3ad5`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

Before I go further, one question about the data. I'll also own a mistake: I opened `bc-policy-draft.md` before asking this, which the skill says I shouldn't do. I haven't analysed it or sent it anywhere, and I'll hold off on the review until you answer.

**What class of data is this draft, and is this environment approved for that class?**

The skill's data rules list **board papers** as high-sensitivity. High-sensitivity material may only be handled in an approved corporate or private environment. This draft is headed for the management board, so it may count as one, unless your organisation classes a draft policy differently.

- If this environment is approved for that class, or the draft is classed lower, tell me and I'll continue.
- If it isn't approved, I'll stop here and won't use what I've already read.

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

Thanks. Medium class in an environment approved for high is fine, so I'll go ahead.

The draft tells me what document this is: version 0.4, dated 3 September 2026, a draft for the management board, owned by the Chief Operating Officer. It doesn't say which frameworks to check it against, so I need two answers first:

1. **Which frameworks should I check it against?** These ship with the skill:
   - DORA (Regulation 2022/2554)
   - Delegated Regulation 2024/1774
   - AI Act, Articles 4, 26 and 50 only
   - NIST SP 800-34r1, chapters 1 to 5
   - NIST CSF 2.0
   - NIST AI RMF 1.0
   - Swiss FONES ICT minimum standard 2023
   - UK Cabinet Office organisational resilience guidance
   - ESAs JC 2026-25 statement on frontier AI models

   If you also want a licensed standard included, such as ISO 22301, attach your own copy and confirm the licence allows this use. I'll cite it by clause number only.
2. **Should I review all seven sections, or only some?**

**Who checks the output:** the COO, as policy owner, answers each question I raise. Legal or compliance answer the points I mark as regulatory. Only a person, reading the source text, can say whether the policy meets a framework. I'll return a draft here in the chat and won't change any file.

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

I've read your draft (v0.4) against DORA and NIST SP 800-34. **I can't tell you whether it's ready for the board or whether it meets either framework.** That decision belongs to the COO and, for DORA, to legal or compliance, working from the source texts. What I can give you is a list of gaps and contradictions, each written as a question for the COO.

**Sources used**
- Your draft, `bc-policy-draft.md`: version 0.4, 3 September 2026, a draft for the management board, owned by the COO.
- DORA, Regulation (EU) 2022/2554, Official Journal L 333, 27 December 2022, as adopted. This is the skill's copy, retrieved 10 September 2026, and it's a conversion; the EUR-Lex text is authoritative.
- NIST SP 800-34 Rev. 1, May 2010. Only the executive summary and chapters 1 to 5 are included, retrieved 10 September 2026; the PDF is authoritative.

**Who reviews this:** the COO answers each question. Legal or compliance answer every point marked ⚖️. I've changed nothing in the draft.

## Main points

- **Does DORA apply in full? Settle this first.** DORA covers payment institutions, but an exempted payment institution follows the simplified Article 16 rules instead of Articles 5 to 15. Most of the DORA findings below depend on this answer.
- **Three direct contradictions with DORA:**
  - Testing every two years, against DORA's "at least yearly".
  - A desktop walk-through only, while DORA requires cyber-attack and switchover scenarios.
  - Review every three years, against yearly review of the ICT risk framework.
- **Things DORA asks for that the draft doesn't mention:** the board's oversight role, a crisis management function, third-party providers, recovery point objectives (RPOs), crisis communication, regulatory reporting, independent audit of the recovery plans, and records kept during a disruption.
- **Gaps against NIST SP 800-34:** training, resources, backup frequency, a separate plan-maintenance schedule, and who has authority to activate the plans.
- **Inside the draft itself:** §2 brings the card processing platform, ICT systems and offices into scope, but the BIA in §4 covers only the payment services and the customer support desk.

## DORA

**Threshold question ⚖️**

**0. Do Articles 5 to 15 apply to you, or the simplified Article 16 rules?** Art. 2(1)(b) brings in "payment institutions, including payment institutions exempted pursuant to Directive (EU) 2015/2366". Art. 16(1) says Articles 5 to 15 "shall not apply to … payment institutions exempted pursuant to Directive (EU) 2015/2366".
- *Question:* Is the company an exempted payment institution under Article 32(1) of Directive 2015/2366?
- With 140 staff, DORA's microenterprise definition ("fewer than 10 persons", Art. 3(60)) doesn't appear to apply, so the provisions written for "other than microenterprises" would read on their face. Legal should confirm that reading.
- The findings below assume Articles 5 to 15 apply.

**Contradictions (both passages quoted)**

**1. Testing frequency and method ⚖️**
- Draft §5: "tested every two years, by a desktop walk-through."
- Art. 11(6)(a): "test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly". For entities other than microenterprises, testing must include "scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities".
- Art. 24(6): "at least yearly, that appropriate tests are conducted on all ICT systems and applications supporting critical or important functions". Art. 24(4) says tests are "undertaken by independent parties".
- *Question for the COO:* How does a two-yearly desktop walk-through square with these texts? Who carries out the tests?

**2. Policy review cycle ⚖️**
- Draft §7: "reviews this policy every three years."
- Art. 6(5): the ICT risk management framework "shall be documented and reviewed at least once a year … as well as upon the occurrence of major ICT-related incidents". Art. 11(1) puts the ICT business continuity policy "as part of the ICT risk management framework".
- Art. 11(6), last paragraph: review should take into account "the results of tests … and recommendations stemming from audit checks or supervisory reviews".
- *Question:* Is this policy part of that framework? If it is, how does a three-year cycle with no event triggers fit?

**Gaps (DORA text with nothing matching it in the draft)**

**3. Board role ⚖️ (Art. 5(2)(e))**
- DORA: the management body shall "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy and ICT response and recovery plans".
- §3 gives ownership to the COO and §7 gives review to the policy owner. The board appears nowhere.
- *Question:* What role does the board take after it approves the policy?

**4. Relation to an ICT business continuity policy ⚖️ (Art. 11(1))**
- DORA: "a comprehensive ICT business continuity policy, which may be adopted as a dedicated specific policy, forming an integral part of the overall business continuity policy".
- *Question:* Is this document that ICT policy, or does a separate one exist? If separate, how are the two linked?

**5. What the policy's arrangements must achieve ⚖️ (Art. 11(2)(a)–(e))**
- DORA lists aims including "ensure the continuity of the financial entity's critical or important functions", "estimate preliminary impacts, damages and losses", and "set out communication and crisis management actions … and report to the competent authorities in accordance with Article 19".
- §1 says "keeps its payment services running through a disruption and recovers them afterwards". It doesn't use the term critical or important functions, and doesn't mention communication, crisis management or reporting to the authorities.
- *Question:* Which of these aims should the policy state, and where are the others covered?

**6. What the BIA covers ⚖️ (Art. 11(5))**
- DORA: the BIA "shall consider the criticality of identified and mapped business functions, support processes, third-party dependencies and information assets, and their interdependencies", "using internal and external data and scenario analysis".
- §4 covers "each payment service and the customer support desk". §2's scope also includes the card processing platform, the ICT systems and both offices, but the BIA doesn't mention them.
- Art. 11(5) sets no frequency. Art. 8(1) and 8(2), however, require the classification of functions and the risk scenarios to be reviewed "at least yearly".
- *Questions:* Should the BIA cover everything in §2's scope and the third-party dependencies? How does the three-year BIA cycle relate to those yearly reviews?

**7. Recovery objectives ⚖️ (Art. 12(6))**
- DORA: "In determining the recovery time and recovery point objectives for each function, financial entities shall take into account whether it is a critical or important function … Such time objectives shall ensure that, in extreme scenarios, the agreed service levels are met."
- §6: "The IT manager sets the recovery time objectives for all systems." That sets objectives per system rather than per function, leaves out RPOs, and gives no criteria for setting them.
- *Question:* Who sets RTOs and RPOs, for which functions, and on what basis? I haven't proposed any values; those belong to their owners.

**8. Crisis management function ⚖️ (Art. 11(7))**
- DORA: entities other than microenterprises "shall have a crisis management function".
- §3 names no such function.
- *Question:* Who holds it?

**9. Crisis communication ⚖️ (Art. 11(6)(b), Art. 14)**
- DORA requires testing of crisis communication plans, and Art. 14(3) says "at least one person … shall be tasked with implementing the communication strategy".
- The draft doesn't mention this.
- *Question:* Who holds this, and where is it covered?

**10. Third-party ICT providers ⚖️ (Art. 11(4), Art. 5(3))**
- DORA requires plans to be tested "notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers", and a role "to monitor the arrangements concluded with ICT third-party service providers".
- The draft doesn't mention third parties at all.
- *Question:* Do any providers support the card processing platform? Where are they covered?

**11. Independent audit of recovery plans ⚖️ (Art. 11(3))**
- DORA: ICT response and recovery plans "shall be subject to independent internal audit reviews".
- *Question:* Should the policy say who audits the IT manager's plans?

**12. Records during a disruption ⚖️ (Art. 11(8))**
- DORA: "keep readily accessible records of activities before and during disruption events".
- *Question:* Who keeps them?

**13. Backup and redundancy ⚖️ (Art. 12(1)(a), 12(4))**
- DORA requires "backup policies and procedures specifying the scope of the data … and the minimum frequency of the backup", and "redundant ICT capacities".
- *Question:* Should this policy refer to where these are set?

**14. Lessons learned and training ⚖️ (Art. 13(2), 13(6))**
- DORA requires post-incident reviews that feed "within the ICT business continuity policy", and compulsory digital operational resilience training.
- *Question:* Should the policy require either one?

## NIST SP 800-34 Rev. 1

This is US federal guidance, not a regulation, so nothing here is marked for legal review. Its §1.2 says it doesn't "address continuity of mission/business processes", so it applies mainly to the ICT recovery side of your policy. §3.1 lists the key elements a policy should contain.

**1. Training (§3.1, §3.5.2)**
- Gap: §3.1 lists "Training requirements", and §3.5.2 says "Training should be provided at least annually."
- *Question:* Who is trained, and how often?

**2. Resources (§3.1, §3.4.5)**
- Gap: "Resource requirements" is a key element in §3.1.
- *Question:* Should the policy commit a budget or resources?

**3. Backups (§3.1, §3.4.2)**
- Gap: §3.1 lists "Minimum frequency of backups and storage of backup media".
- *Question:* Where is this set?

**4. Plan maintenance (§3.1, §3.6)**
- §7 covers reviewing the policy, but nothing covers reviewing the plans themselves. §3.6 says plans are reviewed "at an organization-defined frequency or whenever significant changes occur". The sample policy statement in §3.1 says "reviewed annually".
- *Question:* What schedule and triggers apply to the plans?

**5. Testing depth (§3.5.4)**
- §5 relies on a desktop walk-through. §3.5.4 says "For low-impact systems, a tabletop exercise … is sufficient". Moderate-impact systems call for a functional exercise "to include an element of system recovery from backup media". High-impact systems call for a full-scale exercise with "system failover to the alternate location". The sample policy statement says capabilities "shall be tested annually".
- *Question:* What impact level does the card processing platform carry, and does a walk-through match it?

**6. Who sets recovery objectives (§3.2.1)**
- NIST has the coordinator work "with the process owners, leadership and business managers" to determine acceptable downtime. MTD is "the total amount of time the system owner/authorizing official is willing to accept". It also defines RPO.
- §6 gives RTOs to the IT manager alone, with no MTD or RPO.
- *Question:* Who signs off downtime tolerances on the business side?

**7. Plan activation (§3.4.6)**
- NIST calls for "a single authoritative role for overall decision-making responsibility, including plan activation".
- §3 names no one.
- *Question:* Who activates the plans?

**8. When the BIA is redone (§3.6)**
- NIST: "When a significant change occurs, the BIA should be updated."
- §4 has a fixed three-year cycle with no trigger.
- *Question:* Should a significant change trigger a new BIA?

**9. Links to other plans (§3.1)**
- NIST says plans "should be coordinated with related organization-wide policies and programs, including information system security, physical security, human resources".
- *Question:* Should the policy name the documents it links to?

## General practice, not in the sources

- **Next review date.** The draft carries an owner, a version and a date, but no next review date. *Question:* Should one be added?
- **Marketing website exclusion.** §2 excludes the website without giving a reason. *Question:* Should the exclusion be justified?

## Gaps in this review

- **Your answers, used as my starting point:** data class medium, in an environment approved for high; frameworks DORA and NIST SP 800-34; all of sections 1 to 7 in scope. I made no assumptions beyond these.
- **Your draft is version 0.4, a draft.** I've reported on it only. Nothing here treats it as current policy.
- **Missing parts of the sources:** the NIST appendices aren't in the skill's copy. That includes the templates and Appendix E on contingency-planning controls, so I haven't reviewed against them.
- **Not reviewed:** the AI Act (Articles 4, 26, 50), NIST CSF 2.0, NIST AI RMF 1.0, the Swiss FONES ICT minimum standard, UK Cabinet Office guidance, ESAs JC 2026-25, and Delegated Regulation 2024/1774.
- **Worth adding:** if DORA applies in full, consider adding Delegated Regulation 2024/1774 to a second review. DORA Art. 15(d) mandates rules that "specify further the components of the ICT business continuity policy", and that regulation is where those rules are set.
- **Not in the sources:** whether your other documents (ICT recovery plans, backup policy, crisis communication plan) already cover the gaps above. Attach them for a second review.

> Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
