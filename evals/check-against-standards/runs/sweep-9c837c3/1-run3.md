# /check-against-standards case 1, run3: Claude Code, guidance at 9c837c3

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `5eb55ca9-88ab-489a-bba3-1fa93c103cc6`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

Before I open `bc-policy-draft.md`, one question:

**What class of data does the draft policy hold?** For example: public, internal, confidential, or restricted, or whatever classes your organisation uses.

I need your answer before I read the file, and I'll go by what you tell me, not by any marking inside the file. If this environment isn't approved for that class, I'll stop there.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Bash: `ls -la; ls /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literat`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

The class is medium and this environment is approved for high, so I can go ahead. I've read `bc-policy-draft.md`: version 0.4, dated 3 September 2026, status "draft for the management board", owner the Chief Operating Officer.

Before I review it, I need three answers. I'll list your answers as your own statements, not as sources, and they won't fill in any value in the review.

1. **Which frameworks should I compare it against, and which parts?** These texts come with the skill:
   - DORA, Regulation (EU) 2022/2554, for example Articles 5–6 and 11–12 (ICT risk framework, response and recovery, backup)
   - Delegated Regulation (EU) 2024/1774 (RTS on the ICT risk management framework), for example Article 24 (testing) and Articles 25–26
   - NIST SP 800-34 Rev. 1, chapters 1–5
   - NIST CSF 2.0
   - the Swiss FONES ICT minimum standard (2023)
   - the UK Cabinet Office Organisational Resilience Guidance
   - the ESAs Joint Committee statement JC 2026 25

   You can also attach your own copy of ISO 22301 if you confirm its licence allows this. I'd cite it by clause number only. I won't review any framework you don't pick, and the report will say so.
2. **Does the institution fall under DORA's simplified ICT risk management framework** (DORA Article 16 and RTS 2024/1774 Title III), **or under the full framework?** This decides which RTS articles apply. If you don't know, I'll review both and mark the question for legal or compliance.
3. **Does an approved business continuity policy already exist that this draft replaces?** If so, please attach it with its version and date, or tell me it doesn't exist.

I'll wait for your answers before writing the review.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/govern.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/README.md`
- Glob: `*`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-against-standards/1/run3/work/bc-policy-draft.md`

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

**Sources reviewed** (one line per document)

- **Policy reviewed:** `bc-policy-draft.md`, version 0.4, dated 3 September 2026. Status: "draft for the management board". Owner: Chief Operating Officer.
- **DORA:** Regulation (EU) 2022/2554, Official Journal L 333, 27 December 2022, as adopted. File: `literature/eur-lex/dora-regulation-2022-2554.md`, retrieved 2026-09-10, reusable under Commission Decision 2011/833/EU.
- **NIST SP 800-34 Rev. 1:** May 2010. Only the Executive Summary and Chapters 1–5 are included; the appendices are not. File: `literature/nist/sp-800-34r1-contingency-planning-body.md`, retrieved 2026-09-10. It is a U.S. Government work.

---

## DORA, Regulation (EU) 2022/2554

Every point below concerns a regulation, so every point is marked **[legal / compliance review]**.

### Gaps (a passage in DORA with no counterpart in the draft)

1. **Management body approval and review.** DORA Article 5(2)(e) says the management body shall "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy and ICT response and recovery plans". The draft names only a single owner: §3 says "The Chief Operating Officer owns this policy." Should the policy say that the management board approves it, oversees it and reviews it periodically? **[legal / compliance review]**
2. **ICT business continuity policy.** Article 11(1) requires "a comprehensive ICT business continuity policy, which may be adopted as a dedicated specific policy, forming an integral part of the overall business continuity policy". Is this draft meant to be the ICT business continuity policy? If not, does it refer to a separate one? Neither is stated. **[legal / compliance review]**
3. **Critical or important functions.** Article 11(2)(a) aims to "ensure the continuity of the financial entity's critical or important functions". The draft talks about "payment services" (§1, §2) but never identifies critical or important functions. Where are they identified? **[legal / compliance review]**
4. **What the BIA must cover.** Article 11(5) requires the BIA to use "quantitative and qualitative criteria, using internal and external data and scenario analysis" and to "consider the criticality of identified and mapped business functions, support processes, third-party dependencies and information assets, and their interdependencies". Draft §4 names only "each payment service and the customer support desk". Should §4 set out these elements? **[legal / compliance review]**
5. **Recovery point objectives.** Article 12(6) speaks of "recovery time and recovery point objectives for each function". Draft §6 covers recovery time objectives only. Who sets recovery point objectives, and where? **[legal / compliance review]**
6. **Backup and restoration.** Article 12(1) requires documented "backup policies and procedures specifying the scope of the data that is subject to the backup and the minimum frequency of the backup" and "restoration and recovery procedures and methods". The draft says nothing about either. Should it refer to them? **[legal / compliance review]**
7. **ICT third-party service providers.** Article 11(4) requires ICT business continuity plans to be tested "notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers". The draft does not mention third parties. Does the card processing platform rely on any? **[legal / compliance review]**
8. **Crisis management and communication.** Article 11(7) requires "a crisis management function" for entities other than microenterprises. Article 14(1) requires "crisis communication plans", and Article 11(6)(b) requires those plans to be tested. The draft covers none of this. **[legal / compliance review]**
9. **Incident reporting.** Article 11(2)(e) links continuity arrangements to reporting "to the competent authorities in accordance with Article 19". Article 23 extends Chapter III to "operational or security payment-related incidents" at payment institutions. The draft does not mention reporting. **[legal / compliance review]**
10. **Independent internal audit.** Article 11(3) says ICT response and recovery plans "shall be subject to independent internal audit reviews" (except at microenterprises). The draft says nothing about audit. **[legal / compliance review]**
11. **Records and lessons learned.** Article 11(8) requires "readily accessible records of activities before and during disruption events". Article 13(2) requires "post ICT-related incident reviews after a major ICT-related incident". The draft is silent on both. **[legal / compliance review]**

### Contradictions (both passages quoted)

12. **How often plans are tested.**
    - Draft §5: "Business continuity plans and ICT recovery plans are tested every two years".
    - DORA Article 11(6)(a): "test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly".
    - DORA Article 24(6): "at least yearly, that appropriate tests are conducted on all ICT systems and applications supporting critical or important functions".

    Which interval does the owner intend? **[legal / compliance review]**
13. **How plans are tested.**
    - Draft §5: "by a desktop walk-through".
    - DORA Article 11(6), second subparagraph: entities other than microenterprises "shall include in the testing plans scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities".
    - DORA Article 24(4): "tests are undertaken by independent parties".

    Is a desktop walk-through the only test method meant? **[legal / compliance review]**
14. **How often the policy is reviewed.**
    - Draft §7: "The policy owner reviews this policy every three years."
    - DORA Article 6(5): the ICT risk management framework "shall be documented and reviewed at least once a year … as well as upon the occurrence of major ICT-related incidents".
    - DORA Article 11(6), last subparagraph: "regularly review their ICT business continuity policy … taking into account the results of tests".

    Does this policy form part of the framework that Article 6(5) covers? **[legal / compliance review]**
15. **Who sets recovery time objectives, and for what.**
    - Draft §6: "The IT manager sets the recovery time objectives for all systems."
    - DORA Article 12(6): objectives are set "for each function", taking into account "whether it is a critical or important function and the potential overall impact on market efficiency".

    Are the objectives meant to be set per system or per function, and who decides them? **[legal / compliance review]**

### Questions about which rules apply

16. **Simplified or full framework.** Article 16(1) says "Articles 5 to 15 of this Regulation shall not apply to … payment institutions exempted pursuant to Directive (EU) 2015/2366". Is the institution exempted? The answer decides whether items 1–15 apply in full or whether Article 16(1)(a)–(h) applies instead. Article 16(1)(g) asks only to "test, on a regular basis". **[legal / compliance review]**
17. **Microenterprise exceptions.** Several of the articles cited above exempt microenterprises ("other than microenterprises"). Article 3(60) defines a microenterprise as one that "employs fewer than 10 persons". The draft gives 140 staff. Should legal confirm that none of the microenterprise exceptions apply? **[legal / compliance review]**

## NIST SP 800-34 Rev. 1

This is guidance, not a regulation, so these points are not marked for legal review.

### Gaps

18. **Policy elements the draft lacks.** §3.1 lists these key policy elements: "Roles and responsibilities; Scope …; Resource requirements; Training requirements; Exercise and testing schedules; Plan maintenance schedule; and Minimum frequency of backups and storage of backup media". The draft has roles (§3), scope (§2) and a testing schedule (§5). It has no resource requirements, training requirements, plan maintenance schedule or backup frequency. Which of these should the policy set?
19. **Training.** §3.5.2 says: "Training should be provided at least annually. Personnel newly appointed to ISCP roles should receive training shortly thereafter." The draft does not mention training.
20. **Authority to activate plans.** §3.4.6 calls for "a single authoritative role for overall decision-making responsibility, including plan activation". The draft does not say who can activate a plan.
21. **Downtime measures.** §3.2.1 defines Maximum Tolerable Downtime (MTD), RTO and RPO, and says "the RTO must normally be shorter than the MTD". Draft §6 has RTO only. Should the policy cover MTD and RPO?
22. **Plan maintenance.** §3.6 says the plan "should be reviewed for accuracy and completeness at an organization-defined frequency or whenever significant changes occur". Draft §7 sets a review cycle for the policy only, not for the plans.

### Contradictions

23. **Who decides acceptable downtime.**
    - Draft §6: "The IT manager sets the recovery time objectives for all systems."
    - NIST §3.2.1: the ISCP Coordinator, "with the process owners, leadership and business managers determine the acceptable downtime".

    Should process owners and management have a part in setting these objectives?
24. **Whether a walk-through counts as a test.**
    - Draft §5: plans "are tested … by a desktop walk-through".
    - NIST §3.5.1: testing "should be conducted in as close to an operating environment as possible".
    - NIST §3.5.3: a tabletop exercise is "discussion-based only and does not involve deploying equipment or other resources".

    Is the walk-through meant as a test or as an exercise?
25. **Testing and review intervals compared with the NIST sample.** The sample policy statement in §3.1 says the plan "must be reviewed annually" and that recovery capabilities "shall be tested annually". The draft sets three years (§7) and two years (§5). This is a sample text, not a requirement. Does the owner want to follow it?

---

## Challenge: clauses that are ambiguous, unenforceable or open to two readings

Each of these is a question for the Chief Operating Officer.

- **§1 and §2.** The purpose covers "payment services". The scope also covers "customer support and the two offices". Does the purpose cover everything in the scope?
- **§2, "The ICT systems that support them are in scope".** Is there a list of these systems? Does it include systems run by third parties?
- **§2, "the marketing website is not".** What is the basis for leaving it out? Does it support any payment or customer function?
- **§3.** The IT manager owns "the ICT recovery plans", but §5 also refers to "Business continuity plans". Who owns the business continuity plans? Nobody is named.
- **§3, "runs the programme day to day".** What authority does the BCM officer have? Who deputises when they are absent?
- **§4, "every three years".** Is the BIA also repeated when services, systems or suppliers change?
- **§5, "are tested".** Who carries out the tests, who receives the results, and who tracks fixes to completion?
- **§6, "for all systems".** How do system objectives connect to the BIA, which §4 runs per service? Who approves the objectives?
- **§7, "reviews".** Does a review lead to re-approval? Who approves changes made between reviews?
- **General practice, not in the sources:** the policy has no effective date, no next review date and no approval record in its document control.

## Gaps in what the sources cover

- **Status of the document reviewed:** version 0.4, 3 September 2026, "draft for the management board". It was reviewed as a draft and its status stays a draft.
- **Your intake answers** (your own statements, not sources):
  - Frameworks: DORA and NIST SP 800-34.
  - "All of it": I took this to mean both texts in full. I reviewed the policy-relevant parts of DORA (Articles 2–6, 11–14, 16, 19, 23–24) and all of Chapters 1–5 of NIST SP 800-34.
  - This answer did not settle whether the full or simplified DORA framework applies, so that is listed as item 16. Cite: `Gaps`.
  - Question 3 (any earlier approved policy) was not answered. I assumed there is none, and no earlier policy was reviewed. Cite: `Gaps`.
- **Not reviewed:**
  - Delegated Regulation (EU) 2024/1774. DORA Articles 15(d)–(f) and 16(3)(c)–(d) say it specifies further the components of the business continuity policy, the plans and the testing, so it is likely to matter.
  - NIST CSF 2.0, FONES, the UK Cabinet Office guidance, the ESAs statement JC 2026 25, ISO 22301, and the NIST SP 800-34 appendices (templates), which are not included in the shipped text.
- **NIST SP 800-34 scope.** The text is a "Contingency Planning Guide for Federal Information Systems". It refers to FIPS 199 impact levels and federal directives such as FCD-1. How it applies to an EU payment institution is not in the sources.
- **Owner:** named as the Chief Operating Officer. There is no review date and no approver. What would settle it: the document control block filled in.
- **Text instructing an AI to act:** none found in the draft.

## For the auditor

- The dated sources this review was built from are listed at the top.
- Once approved, the policy needs its owner, version and review date.
- The approval that makes this draft policy belongs to the management board, not to this review.
- This review approves and records nothing. It does not say that the draft meets DORA or NIST SP 800-34. Only a person checking against the source text can say that.

---

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> Chief Operating Officer answers these, legal or compliance the marked points.

**Tool calls (stream-json):**

- Glob: `literature/**/*`
- Grep: `^(#|<!--|>|Source|Retrieved|Licen)`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Grep: `(policy statement|^3\.\d|^#|annually|at least|RTO|Recovery Time Objective|MTD|roles and responsibilities|resource requirements|review)`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Grep: `Say in the document that AI helped`
