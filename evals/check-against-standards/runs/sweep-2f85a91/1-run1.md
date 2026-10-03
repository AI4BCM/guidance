# /check-against-standards case 1, run1: Claude Code, guidance at 2f85a91

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `de8e8598-12d5-46f3-81e5-8b2bcd5f051c`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

Before I start the review, I need to tell you about a mistake. The skill's preflight says my first message should only ask what class of data the draft holds, and that I shouldn't open any attached file until you answer. I opened `bc-policy-draft.md` in the same step as reading the preflight, so I've already seen its contents. I haven't analysed it and won't use any of it until you answer the two questions below.

**1. What class of data does the draft policy hold?** Please tell me yourself; I won't go by any marking in the file. Under `units/data-rules.md`, board papers and executive-session material count as high-sensitivity. A draft going to the board may fall into that class. High-sensitivity material can only be handled in an approved corporate or private environment, so please also confirm that this environment is approved for the class you give. If it isn't, I'll stop here.

**2. Which frameworks should I compare it against, and which parts?** These framework texts ship with the skill:
- **DORA**, Regulation (EU) 2022/2554, and **Delegated Regulation (EU) 2024/1774**
- **AI Act** (EU) 2024/1689, Articles 4, 26 and 50 only
- **NIST SP 800-34 Rev. 1**, chapters 1 to 5; **NIST CSF 2.0**; **NIST AI RMF 1.0**
- **FONES** (Swiss federal office) *Minimum standard for improving ICT resilience* (2023)
- **UK Cabinet Office** *Organisational Resilience Guidance*
- **ESAs** (EU supervisory authorities) Joint Committee statement JC 2026 25

**ISO 22301 doesn't ship** because of its licence. If you want it included, you'll need to attach your own copy and confirm that your licence allows this use. Otherwise I'll list it under Gaps as "not reviewed". I'll also list every framework you don't select as not reviewed.

Once I have your answers, I'll write the review here in the chat. I won't create or approve anything, and the final decisions stay with the policy owner and management.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Bash: `ls -la; cat bc-policy-draft.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/README.md`
- Bash: `sed -n '/Sensitivity classes/,/^## /p' /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/data-rules.md`
- Grep: `Sensitivity classes`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

Thanks. Medium-class data is fine here, since this environment is approved for high-sensitivity material.

I still need one answer before I start: **which frameworks should I compare the draft against, and which parts of each?** I won't choose them myself, because I can only review what you select. Every framework you don't select will be listed as "not reviewed", including ISO 22301 unless you attach a copy your licence allows me to use.

For a payment institution, DORA and its Delegated Regulation (EU) 2024/1774 are the usual candidates. Whether they apply to you, and which articles, is a question for your legal or compliance team. If you'd like those two, tell me which parts to use (for example, DORA Chapter II) or say "whole text". You can add any of the other shipped texts I listed earlier.

**Tool calls (stream-json):**

- none

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

# Review of the draft business continuity policy against DORA and NIST SP 800-34

**Sources**
- *Business continuity policy*, version 0.4, dated 3 September 2026. Status: draft for the management board. Owner: Chief Operating Officer.
- Regulation (EU) 2022/2554 (DORA), OJ L 333 of 27 December 2022, as adopted. Shipped conversion retrieved 2026-09-10 (`literature/eur-lex/dora-regulation-2022-2554.md`). EUR-Lex is authoritative.
- NIST SP 800-34 Rev. 1, May 2010, Executive Summary and Chapters 1 to 5 only. Shipped conversion retrieved 2026-09-10 (`literature/nist/sp-800-34r1-contingency-planning-body.md`). The PDF is authoritative.

This is a review only. A finding is a question for the policy owner until they answer it. Points marked **[L/C]** are for legal or compliance review. Nothing below says whether the draft meets either framework; only a person can decide that, against the source text.

---

## DORA, Regulation (EU) 2022/2554

**D0. Which regime applies? [L/C]** The draft calls the organisation "a small payment institution with 140 staff". Article 16(1) says "Articles 5 to 15 of this Regulation shall not apply to … payment institutions exempted pursuant to Directive (EU) 2015/2366", and it sets a simplified framework for them instead. Is the institution exempted under that Directive? Most of the findings below (D1 to D10) depend on the answer. With 140 staff the institution does not fall under Article 3(60)'s definition of "microenterprise" ("fewer than 10 persons"), so the exceptions DORA makes "other than microenterprises" would not apply.

**Contradictions** (both passages quoted)

**D1. Testing frequency [L/C].**
- Draft §5: "Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through."
- DORA Art. 11(6)(a): "test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions".

How does the owner reconcile these two passages?

**D2. Test content [L/C].**
- Draft §5: "by a desktop walk-through."
- DORA Art. 11(6), second subparagraph: "shall include in the testing plans scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities".
- DORA Art. 24(4): "tests are undertaken by independent parties, whether internal or external."

Does the draft's test method leave room for cyber-attack scenarios, switchover tests and independent testers?

**D3. Review cycle [L/C].**
- Draft §7: "The policy owner reviews this policy every three years."
- DORA Art. 11(1) places the ICT business continuity policy "As part of the ICT risk management framework". Art. 6(5) says that framework is "reviewed at least once a year … as well as upon the occurrence of major ICT-related incidents".
- DORA Art. 11(6), last subparagraph: "regularly review their ICT business continuity policy … taking into account the results of tests … and recommendations stemming from audit checks or supervisory reviews".

Is this policy, or the ICT part of it, part of the ICT risk management framework? Should a review be triggered by incidents, tests or audits as well as by the calendar?

**Gaps** (a DORA passage with no counterpart in the draft)

**D4. Management body [L/C].** Art. 5(2)(e) says the management body shall "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy and ICT response and recovery plans". The draft's header says it is for the management board, but §3 names only the COO, the BCM officer and the IT manager. What role does the board have in the policy itself?

**D5. Recovery objectives [L/C].**
- Draft §6: "The IT manager sets the recovery time objectives for all systems."
- DORA Art. 12(6): "In determining the recovery time and recovery point objectives for each function, financial entities shall take into account whether it is a critical or important function".

The draft sets objectives per system, while Art. 12(6) speaks of each function. The draft does not mention recovery point objectives at all. Who agrees the objectives with the business functions that rely on them?

**D6. BIA content [L/C].** Draft §4 covers "each payment service and the customer support desk". Art. 11(5) says the BIA "shall consider the criticality of identified and mapped business functions, support processes, third-party dependencies and information assets, and their interdependencies", using "quantitative and qualitative criteria". Are support processes, third-party dependencies and information assets inside the BIA's scope? DORA gives no BIA frequency, so the draft's three-year cycle has no counterpart in DORA.

**D7. Critical or important functions [L/C].** Art. 11(2)(a) aims to "ensure the continuity of the financial entity's critical or important functions". The draft does not use this term or say how such functions are identified.

**D8. Scope exclusion [L/C].**
- Draft §2: "the marketing website is not" in scope.
- DORA Art. 11(6)(a): testing "in relation to ICT systems supporting all functions".

Does the exclusion hold for ICT testing?

**D9. Third parties [L/C].** Art. 11(4) asks for business continuity plans that are tested "notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers". The draft's scope does not mention third parties. Is the card processing platform, or any part of it, run by a third party?

**D10. Elements DORA requires that the draft does not mention [L/C].** In each case, is the element handled elsewhere, and if so, where?
- Crisis management function: Art. 11(7).
- Crisis communication plans and their testing: Art. 11(6)(b) and Art. 14.
- Backup policies and redundant ICT capacity: Art. 12(1) and (4).
- Independent internal audit of the response and recovery plans: Art. 11(3).
- Records of activities during disruption: Art. 11(8).
- Post-incident reviews: Art. 13(2).

---

## NIST SP 800-34 Rev. 1 (Executive Summary and Chapters 1 to 5)

**Contradictions**

**N1. Review and test frequency.** These passages come from NIST's *sample* policy statement in §3.1, not from a requirement.
- NIST §3.1: the plan "must be reviewed annually" and "The plan recovery capabilities and personnel shall be tested annually".
- Draft §5: "every two years".
- Draft §7: "every three years".

Does the owner want to depart from the sample, and why?

**N2. Who sets downtime?**
- Draft §6: "The IT manager sets the recovery time objectives for all systems."
- NIST §3.2.1: the coordinator "with the process owners, leadership and business managers determine the acceptable downtime". NIST also ties the RTO to the Maximum Tolerable Downtime: "the RTO must normally be shorter than the MTD".

The draft names no MTD and no RPO. Who sets the MTD, and who agrees it?

**Gaps**

**N3. Key policy elements.** NIST §3.1 lists the "Key policy elements". The draft has roles and responsibilities (§3), scope (§2), a testing schedule (§5) and a maintenance schedule (§7). It has no counterpart for these three:
- "Resource requirements"
- "Training requirements"
- "Minimum frequency of backups and storage of backup media"

Are these intended for this policy or for another document?

**N4. Training.** NIST §3.5.2 says: "Training should be provided at least annually." The draft does not mention training.

**N5. Coordination with other plans.** NIST §3.1 says plans "should be coordinated with related organization-wide policies and programs, including information system security, physical security, human resources". The draft names no related policies. Which ones does it connect to?

---

## Challenge (clauses that are ambiguous, impossible to enforce, or open to two readings)

Each of these is a question for the policy owner. I am not proposing replacement wording.

- **§1, "a disruption".** The term is not defined. Does it cover any disruption, or only one above a threshold?
- **§2, "The ICT systems that support them".** Which systems count? Does this include systems operated by third parties?
- **§3, "runs the programme day to day".** What authority does the BCM officer have? Who stands in if the COO, the BCM officer or the IT manager is unavailable? This question is general practice, not in the sources.
- **§4, "every three years".** Is a BIA also due after a major change? The draft gives only a calendar trigger.
- **§5, "tested … by a desktop walk-through".** Is a walk-through the only method allowed, or the minimum? Who runs the tests, and who receives the results?
- **§6, "for all systems".** Does this include systems outside the §2 scope? Who approves the objectives the IT manager sets?
- **§7, "reviews this policy".** Who approves a revised version?

---

## Gaps

- **Draft status.** The policy is version 0.4, dated 3 September 2026, a "draft for the management board". I reviewed it as the current text, and its status is unchanged by this review. Owner: Chief Operating Officer.
- **Your intake answers**, which are your statements and not sources:
  - The data class is medium, and this environment is approved for high-sensitivity data.
  - The frameworks to use are DORA and NIST SP 800-34, all of each.
- **What "all of it" covered.** For SP 800-34, only the Executive Summary and Chapters 1 to 5 ship. The appendices (BIA template, plan templates, control descriptions) were not reviewed. For DORA, I compared the draft with the ICT risk management, testing and governance articles and found no counterpart for the rest.
- **Sources SP 800-34 relies on.** SP 800-34 is written for US federal systems and relies on FIPS 199 impact levels. FIPS 199 is not in the sources.
- **Frameworks not selected, and therefore not reviewed:**
  - Delegated Regulation (EU) 2024/1774. DORA Art. 15(d) and (e) say that technical standards will "specify further the components of the ICT business continuity policy" and its testing; this Delegated Regulation is a shipped text of that kind, so it would settle some of the questions above.
  - AI Act, Articles 4, 26 and 50
  - NIST CSF 2.0
  - NIST AI RMF 1.0
  - FONES ICT minimum standard
  - UK Cabinet Office *Organisational Resilience Guidance*
  - ESAs statement JC 2026 25
  - ISO 22301, which does not ship with the skill
- **Instructions aimed at an AI.** I found none in the draft.

---

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

The Chief Operating Officer answers these, legal or compliance the marked points.

**Tool calls (stream-json):**

- Glob: `literature/{eur-lex,nist}/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/govern.md`
- Grep: `Say in the document that AI helped`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Grep: `^### Article (2|4|5|6|8|11|12|13|14|24|25|26|28) `
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Grep: `^\(60\)|'microenterprise'|^### Article 16 |^1\. Articles 5 to 15`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Grep: `(policy statement|key policy elements|at least annually|reviewed annually|Roles and responsibilities|Testing schedules|Plan maintenance schedule|Frequency of ba`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Grep: `(Tabletop exercises|Functional exercises|reviewed for accuracy and completeness at least|at least annually)`
- Grep: `.{300}at least annually.{300}|.{200}Tabletop exercises.{400}`
- Grep: `.{0,250}at least annually.{0,250}`
- Grep: `.{0,200}Tabletop exercises.{0,300}`
- Grep: `[^.]{0,200}at least annually[^.]{0,200}\.`
- Grep: `^#{2,4} 3\.`
