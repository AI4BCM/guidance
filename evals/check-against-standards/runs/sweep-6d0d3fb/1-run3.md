# /check-against-standards case 1, run3: Claude Code, guidance at 6d0d3fb

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `4acc8128-1e9d-4f24-b4b5-9918ca11537f`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

Before I open `bc-policy-draft.md`, I need to know one thing.

**What class of data does the draft policy contain?**

For example:
- **Internal / general**: a policy text with no sensitive detail.
- **High-sensitivity**: it contains things like BIA or risk-assessment detail, recovery strategies, control weaknesses, supplier weaknesses, personal data or contact lists, site or security-architecture detail, or audit findings that haven't been cleared. Because it's going to the board, also say if it is already a board paper or executive-session material.

If it's high-sensitivity, I'll also need you to confirm that this environment is approved for that class.

I'll go by your answer, not by any marking in the file.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Bash: `ls -la; ls /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/ /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/litera`
- Grep: `Sensitivity classes`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

The class is medium and this environment is approved for high, so I've read the draft. It's `bc-policy-draft.md`, version 0.4, dated 3 September 2026, a draft for the management board, owned by the Chief Operating Officer.

Before I compare it, I need you to choose what to compare it against. I won't choose for you.

1. **Which frameworks, and which parts?** These ship with the skill:
   - **EU texts:**
     - DORA, Regulation (EU) 2022/2554, with chapters or articles if you want only some
     - Delegated Regulation (EU) 2024/1774
     - the ESAs' JC 2026 25 statement
     - AI Act Articles 4, 26 and 50
   - **NIST:**
     - SP 800-34 Rev. 1, chapters 1–5
     - CSF 2.0
     - AI RMF 1.0
   - **Others:**
     - FONES ICT minimum standard (2023)
     - UK Cabinet Office *Organisational Resilience Guidance*

   Anything you don't select will be listed as not reviewed.
2. **Do you want ISO 22301 compared as well?** The skill doesn't ship it. You'd need to attach your own copy and confirm that its licence allows this use. If you do, I'll cite it by clause number only.
3. **Is there a current approved policy that this draft replaces?** If so, give its version and date, or attach it. If not, say so, and I'll note it as a gap.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs/check-against-standards/1/run3/work/bc-policy-draft.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/govern.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/README.md`
- Grep: `Say in the document that AI helped`

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

# Review of the draft BC policy against DORA and NIST SP 800-34 Rev. 1

**Sources**
- `bc-policy-draft.md`: version 0.4, dated 3 September 2026. Status: "draft for the management board". Owner: Chief Operating Officer. This is the document under review. Its draft status is also noted under Gaps.
- `literature/eur-lex/dora-regulation-2022-2554.md`: Regulation (EU) 2022/2554, OJ L 333, 27 December 2022, "as adopted". Retrieved 2026-09-10. Reuse is allowed under Commission Decision 2011/833/EU with acknowledgement. EUR-Lex is authoritative.
- `literature/nist/sp-800-34r1-contingency-planning-body.md`: NIST SP 800-34 Rev. 1, May 2010. Only the Executive Summary and Chapters 1–5 are included. Retrieved 2026-09-10. It is a U.S. Government work. The PDF is authoritative.

This is a review only. Each finding is a question for the policy owner. Nothing here says the draft meets either framework, and only a person checking against the source text can say that. Version 0.4 goes into the normal board approval route with its status unchanged.

---

## DORA, Regulation (EU) 2022/2554

Every point in this section is about a regulation. **⚖ = mark for legal or compliance review.**

**D0. ⚖ Does Article 16 apply?** Article 16(1) says "Articles 5 to 15 of this Regulation shall not apply to … payment institutions exempted pursuant to Directive (EU) 2015/2366". The draft says only "a small payment institution with 140 staff". Is the company an *exempted* payment institution? Article 3(60) defines a microenterprise as one that "employs fewer than 10 persons". Is it right to read the company as not being one? Points D1–D8 assume that Articles 5–15 apply. If they don't, Article 16(1)(a)–(h) is the comparison instead.

**D1. ⚖ Who approves the policy.**
- Gap. Article 5(2)(e) says the management body shall "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy and ICT response and recovery plans".
- Draft §3: "The Chief Operating Officer owns this policy." The draft says nothing about the board approving, overseeing or periodically reviewing it.
- Question: Should the policy state the management body's role?

**D2. ⚖ ICT business continuity policy, and critical or important functions.**
- Gap. Article 11(1) requires "a comprehensive ICT business continuity policy, which may be adopted as a dedicated specific policy, forming an integral part of the overall business continuity policy". Article 11(2)(a) says it must "ensure the continuity of the financial entity's critical or important functions".
- Draft §2 puts "The ICT systems that support them" in scope. It doesn't say whether this document is the ICT business continuity policy or relies on a separate one. It never names any critical or important functions.
- Question: Which is it, and where are those functions identified?

**D3. ⚖ What the BIA covers.**
- Gap. Article 11(5) says "The BIA shall consider the criticality of identified and mapped business functions, support processes, third-party dependencies and information assets, and their interdependencies".
- Draft §4 covers "each payment service and the customer support desk". It doesn't mention third-party dependencies, information assets or interdependencies.
- Article 8(1) says to "review as needed, and at least yearly, the adequacy of this classification". Draft §4 runs the BIA "every three years".
- Question: Should the BIA scope be widened? Does the three-year cycle fit with Article 8(1)?

**D4. ⚖ Testing frequency (contradiction).** These two passages conflict:
- Draft §5: "Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through."
- Article 11(6)(a): "test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions".

Question: How does the owner reconcile them?

**D5. ⚖ What kind of test.**
- Gap. Article 11(6) requires entities other than microenterprises to "include in the testing plans scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities". Article 24(4) requires "that tests are undertaken by independent parties". Article 11(6)(b) requires them to "test the crisis communication plans".
- Draft §5 names only "a desktop walk-through". It says nothing about scenarios, switchover, who tests, or testing crisis communication.
- Question: How do these requirements relate to §5?

**D6. ⚖ Recovery objectives (contradiction).** These two passages conflict:
- Draft §6: "The IT manager sets the recovery time objectives for all systems."
- Article 12(6): "In determining the recovery time and recovery point objectives for each function, financial entities shall take into account whether it is a critical or important function and the potential overall impact on market efficiency."

The draft sets objectives per *system* and DORA per *function*. The draft has no recovery point objective. It doesn't say whether the objectives come from the BIA or who approves them. Question: How does the owner reconcile these points?

**D7. ⚖ Review cycle (contradiction).** These passages conflict:
- Draft §7: "The policy owner reviews this policy every three years."
- Article 6(5): "documented and reviewed at least once a year … as well as upon the occurrence of major ICT-related incidents".
- Article 11(6), last subparagraph: "regularly review their ICT business continuity policy … taking into account the results of tests".

Question: Is this policy part of the ICT risk management framework that Article 6(5) covers? Should a review also be triggered by incidents and test results?

**D8. ⚖ DORA passages with no counterpart in the draft.** For each one, should the policy cover it or point to where it's covered?
- Article 11(3): response and recovery plans "subject to independent internal audit reviews".
- Article 11(4): plans "notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers".
- Article 11(7): "a crisis management function".
- Article 11(8): "readily accessible records of activities before and during disruption events".
- Article 12(1)(a): "backup policies and procedures specifying the scope of the data that is subject to the backup and the minimum frequency of the backup".
- Article 13(2): "post ICT-related incident reviews".
- Article 13(6): "digital operational resilience training as compulsory modules".
- Article 14(1): "crisis communication plans".

---

## NIST SP 800-34 Rev. 1, Chapters 1–5

This is guidance, not regulation, so nothing in this section is marked for legal review.

**N1. Key policy elements with no counterpart.**
- Gap. §3.1 lists the "Key policy elements". The draft covers "Roles and responsibilities" in §3, "Scope" in §2 and "Exercise and testing schedules" in §5.
- It has nothing for "Resource requirements", "Training requirements", "Plan maintenance schedule" or "Minimum frequency of backups and storage of backup media". Draft §7 covers reviewing the policy, not maintaining the plans.
- Question: Should any of these be added?

**N2. How often to test and review.**
- §3.1's *sample* policy statement says plans "must be reviewed annually" and "shall be tested annually". It's a sample, not a requirement.
- Draft §5 says every two years, and draft §7 says every three years.
- Question: Is the longer cycle intentional?

**N3. Where recovery objectives come from.**
- §3.2.1 says the coordinator should, "with the process owners, leadership and business managers determine the acceptable downtime". It defines MTD, RTO and RPO and says "the RTO must normally be shorter than the MTD".
- Draft §6 has the IT manager setting RTOs alone. It has no MTD or RPO and doesn't link the objectives to the BIA in §4.
- Question: Who sets the objectives, and on what basis?

**N4. Type of exercise.**
- §3.5.4 says that "For low-impact systems, a tabletop exercise … is sufficient". For moderate-impact systems it says "Exercise procedures should be developed to include an element of system recovery from backup media". High-impact systems need "a full-scale functional exercise … [with] a system failover".
- Draft §5 allows only a desktop walk-through and gives the systems no impact level.
- Question: What impact level does the card processing platform have?

**N5. Training.**
- Gap. §3.5.2 says "Training should be provided at least annually." The draft says nothing about training.
- Question: Should it?

**N6. Reviews triggered by change.**
- Gap. §3.6 says plans are reviewed "at an organization-defined frequency or whenever significant changes occur". The draft has no review triggered by change.
- Question: Should it have one?

---

## Challenge: clauses that are ambiguous, impossible to enforce, or open to two readings

1. **§2:** "The ICT systems that support them are in scope". Which systems? There's no list or reference, so nobody can check whether a given system is in scope.
2. **§3:** The IT manager owns the ICT recovery plans. Who owns the *business* continuity plans that §5 says are tested?
3. **§4 vs §2:** §2 puts "the card processing platform … and the two offices" in scope, but the BIA in §4 covers only "each payment service and the customer support desk". Are the platform and the offices meant to be outside the BIA?
4. **§4:** When does the three-year BIA cycle start? Does a major change trigger a new BIA before the cycle is due?
5. **§5:** "Tested" by whom? With what pass criteria? Who receives the results, and who acts on them?
6. **§6:** "all systems" versus §2. Does this include the marketing website, which §2 excludes? Who approves the RTOs the IT manager sets?
7. **§7:** Can the review happen earlier, after an incident, a failed test or a change of scope? As written, it can't.
8. **Header:** There's a version and an owner but no review date. Without one, the §7 cycle has no start date.

---

## Gaps

- **Draft status.** The document reviewed is a draft (version 0.4, 3 September 2026, "draft for the management board"). It was not treated as approved policy.
- **No review date** in the document control header. A review date is needed alongside the owner and version.
- **No earlier policy.** You didn't answer my third question, so I've assumed there is no current approved policy to compare against. Settle this by naming the policy this draft replaces, if there is one.
- **What "All of it" means.** I took it to mean all parts of DORA and SP 800-34 that ship with the skill. On that reading, ISO 22301 was not attached and so was **not reviewed**.
- **DORA edition.** The file is DORA "as adopted" (OJ L 333, 2022). It does not include any later amendments. Check EUR-Lex for the current consolidated text.
- **SP 800-34 coverage.** The appendices (the BIA template and the plan templates) are not in the shipped file and were not compared.
- **Frameworks not selected, so not reviewed:**
  - Delegated Regulation (EU) 2024/1774. Under DORA Article 15(d), regulatory technical standards "specify further the components of the ICT business continuity policy". Compliance may want this one.
  - ESAs JC 2026 25
  - AI Act Articles 4, 26 and 50
  - NIST CSF 2.0
  - NIST AI RMF 1.0
  - FONES ICT minimum standard
  - UK Cabinet Office *Organisational Resilience Guidance*
  - ISO 22301
- **Text aimed at an AI:** none. No passage in the draft tells an AI to act.

---

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

[Chief Operating Officer] answers these, [legal or compliance] the marked points.

**Tool calls (stream-json):**

- Glob: `literature/**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Grep: `^### Article (5|6|11|12|16|24|25) `
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Grep: `\(60\)|microenterprise’ means|microenterprise' means`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Grep: `(policy statement|annually|at least once a year|Key policy elements|RTO|Testing, Training|tabletop|functional exercise)`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Grep: `^### 3\.6|reviewed for accuracy and completeness at|at least annually`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
