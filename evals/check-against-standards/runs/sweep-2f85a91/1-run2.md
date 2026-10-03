# /check-against-standards case 1, run2: Claude Code, guidance at 2f85a91

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `db6f9b91-4281-4828-b56f-ac41a9e2aa15`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

Before I open the draft: what class of data does `bc-policy-draft.md` hold? For example: public, internal, confidential, or restricted (or your organisation's own label).

I'm asking first so I can check that this environment is approved for that class. I'll go by your answer, not by any marking inside the file. If you'd also like to name the frameworks to check against (e.g. ISO 22301, a regulator's guideline), include those too. Any framework you don't select will be marked as not reviewed.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Bash: `ls -la; ls -R /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards | head -50`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

Thanks. Medium data in an environment approved for high is fine, so I've read the draft (v0.4, 3 Sept 2026, draft for the board, owned by the COO).

Before I review it, I need three answers. The review uses only the framework texts you pick, so I won't add requirements from general knowledge.

1. **Which frameworks should I compare it against?** These ship with this skill:
   - DORA, Regulation (EU) 2022/2554
   - Delegated Regulation (EU) 2024/1774, the ICT risk management framework
   - NIST SP 800-34 Rev. 1, chapters 1 to 5
   - NIST CSF 2.0
   - UK Cabinet Office, *Organisational Resilience Guidance*
   - FONES, *Minimum standard for improving ICT resilience* (2023)

   ISO 22301 doesn't ship because of its licence. I can use your own copy if you attach it and confirm the licence allows this, and then I'd cite it by clause number only. Any framework you don't pick will be listed as not reviewed.
2. **Which parts of those frameworks?** For example, only DORA's ICT business continuity and testing articles, or the whole text.
3. **Does this draft replace a current approved policy, or is it the first one?** If one exists, please give its version and date, or attach it.

If you skip a question, I'll list my assumption for it under Gaps.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain-479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep7/runs/check-against-standards/1/run2/work/bc-policy-draft.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/README.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/govern.md`
- Glob: `**/*`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep7/runs/check-against-standards/1/run2/work/bc-policy-draft.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/data-rules.md`
- Glob: `literature/**/*.md`

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

# Review of the draft business continuity policy against DORA and NIST SP 800-34

This review covers `bc-policy-draft.md` v0.4 (3 Sept 2026). It lists gaps, contradictions and questions for the policy owner to answer. It does not say whether the draft meets either framework; only a person checking against the source text can decide that. I have changed and approved nothing.

**Sources**
- Policy: `bc-policy-draft.md`, Version 0.4, 3 September 2026, status "draft for the management board", owner Chief Operating Officer.
- DORA: Regulation (EU) 2022/2554, OJ L 333, 27 December 2022. I used the shipped conversion retrieved 2026-09-10 (`literature/eur-lex/dora-regulation-2022-2554.md`). EUR-Lex is authoritative.
- NIST SP 800-34 Rev. 1, May 2010, Executive Summary and chapters 1 to 5 only. I used the shipped conversion retrieved 2026-09-10 (`literature/nist/sp-800-34r1-contingency-planning-body.md`). The PDF is authoritative.

---

## DORA, Regulation (EU) 2022/2554

Each DORA point is **[legal/compliance review]**: it is a point on a regulation.

1. **Does DORA apply, and in which form?** **[legal/compliance review]**
   - The draft describes the firm as "a small payment institution" (header).
   - Art. 2(1)(b) covers "payment institutions, including payment institutions exempted pursuant to Directive (EU) 2015/2366".
   - Art. 16(1) says "Articles 5 to 15 of this Regulation shall not apply to … payment institutions exempted pursuant to Directive (EU) 2015/2366".
   - Several articles also exempt "microenterprises".
   - Question: is the firm a PSD2-exempted institution, a microenterprise, or neither? The answer decides which comparisons below hold.

2. **Contradiction on how often plans are tested.** **[legal/compliance review]**
   - Draft §5: "Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through."
   - Art. 11(6)(a): "test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions".
   - Art. 24(6): "Financial entities, other than microenterprises, shall ensure, at least yearly, that appropriate tests are conducted on all ICT systems and applications supporting critical or important functions."
   - Question: how does the two-year cycle relate to these yearly requirements?

3. **Gap on test scenarios.** **[legal/compliance review]**
   - Art. 11(6), second subparagraph: "shall include in the testing plans scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities".
   - Art. 25(1) lists test types, such as "scenario-based tests … end-to-end testing and penetration testing".
   - Art. 11(6)(b) requires testing "the crisis communication plans".
   - Draft §5 names only a desktop walk-through. Question: where are these scenarios and tests covered?

4. **Contradiction on how often the policy is reviewed.** **[legal/compliance review]**
   - Draft §7: "The policy owner reviews this policy every three years."
   - Art. 6(5): the ICT risk management framework "shall be documented and reviewed at least once a year … as well as upon the occurrence of major ICT-related incidents".
   - Art. 11(1) places the ICT business continuity policy "as part of the ICT risk management framework".
   - Art. 11(6), last subparagraph, asks for regular review "taking into account the results of tests … and recommendations stemming from audit checks or supervisory reviews".
   - Question: is this policy part of that framework? If so, how does a three-year cycle with no triggers fit?

5. **Contradiction on who sets recovery objectives, and on what basis.** **[legal/compliance review]**
   - Draft §6: "The IT manager sets the recovery time objectives for all systems."
   - Art. 12(6): "In determining the recovery time and recovery point objectives for each function, financial entities shall take into account whether it is a critical or important function".
   - Art. 5(2): the management body "shall define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework".
   - Questions: are the objectives set per system or per function? Who approves them? Where are recovery point objectives?

6. **Gap: the management body's role is missing.** **[legal/compliance review]**
   - Art. 5(2)(e): the management body shall "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy and ICT response and recovery plans".
   - Draft §3 names the COO, the BCM officer and the IT manager, but no board role. Question: should the board's role be stated?

7. **Gap: what the BIA covers and how often it runs.** **[legal/compliance review]**
   - Draft §4: a BIA "every three years, covering each payment service and the customer support desk."
   - Art. 11(5): the BIA "shall consider the criticality of identified and mapped business functions, support processes, third-party dependencies and information assets, and their interdependencies", using "quantitative and qualitative criteria … and scenario analysis".
   - Art. 8(1): review the classification of ICT-supported functions "as needed, and at least yearly".
   - Question: how does the three-year BIA relate to these?

8. **Gap: third parties.** **[legal/compliance review]**
   - Art. 11(4): plans "notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers".
   - Art. 8(5): identify processes "dependent on ICT third-party service providers".
   - The draft does not mention third parties. Question: where is this covered?

9. **Gap: backups.** **[legal/compliance review]**
   - Art. 12(1)(a): "backup policies and procedures specifying the scope of the data that is subject to the backup and the minimum frequency of the backup".
   - Art. 12(4) covers redundant ICT capacities.
   - The draft is silent. Question: is this covered in another document?

10. **Gap: crisis management and communication.** **[legal/compliance review]**
    - Art. 11(7) requires a "crisis management function" (other than for microenterprises).
    - Art. 14(3): "At least one person in the financial entity shall be tasked with implementing the communication strategy for ICT-related incidents".
    - Art. 11(2)(e) requires reporting "to the competent authorities in accordance with Article 19".
    - The draft is silent on all three. Question: who holds these roles?

11. **Gap: independent audit and the control function.** **[legal/compliance review]**
    - Art. 11(3): response and recovery plans "shall be subject to independent internal audit reviews".
    - Art. 6(4): ICT risk is assigned "to a control function" with "an appropriate level of independence".
    - The draft is silent. Question: where is this covered?

12. **Gap: records, lessons learned and training.** **[legal/compliance review]**
    - Art. 11(8): "keep readily accessible records of activities before and during disruption events".
    - Art. 13(2) requires post-incident reviews.
    - Art. 13(6) requires training as "compulsory modules".
    - The draft is silent on all three. Question: where are these covered?

13. **Scope exclusion.** **[legal/compliance review]**
    - Draft §2: "the marketing website is not" in scope.
    - Art. 8(1): "identify, classify and adequately document all ICT supported business functions".
    - Question: did a classification under Art. 8 support this exclusion?

## NIST SP 800-34 Rev. 1

This is guidance, not a regulation, so these points have no legal mark.

1. **Gap: policy elements the draft does not contain.**
   - §3.1 lists "Key policy elements": "Roles and responsibilities; Scope …; Resource requirements; Training requirements; Exercise and testing schedules; Plan maintenance schedule; and Minimum frequency of backups and storage of backup media."
   - The draft has roles (§3), scope (§2) and a test schedule (§5).
   - Question: are resources, training, a plan maintenance schedule and backup frequency meant to be left out?

2. **Contradiction with the sample policy text.**
   - §3.1 sample policy: the plan "must be reviewed annually" and "shall be tested annually".
   - Draft §5 tests every two years, and §7 reviews every three years.
   - Question: the sample is illustrative. Has the longer cycle been chosen deliberately?

3. **Is a desktop walk-through a test?**
   - §3.5.1: testing "should be conducted in as close to an operating environment as possible". The areas it lists include "System recovery on an alternate platform from backup media".
   - §3.5.3 classes tabletop exercises as "discussion-based only".
   - Question: draft §5 calls a desktop walk-through a test. Is that intended?

4. **How recovery time objectives are derived.**
   - §3.2.1: the ISCP Coordinator, "with the process owners, leadership and business managers", determines acceptable downtime. The guidance also says "the RTO must normally be shorter than the MTD".
   - Draft §6 has the IT manager set RTOs, with no MTD, no RPO and no link to the BIA.
   - Question: how do the objectives follow from the BIA?

5. **Gap: who can activate the plan.**
   - §3.4.6: "a single authoritative role for overall decision-making responsibility, including plan activation".
   - The draft names no one who can activate the plan.

6. **Gap: training.**
   - §3.5.2: "Training should be provided at least annually."
   - The draft has no training clause.

7. **Gap: triggers for review and re-running the BIA.**
   - §3.6: review "at an organization-defined frequency or whenever significant changes occur".
   - §3.2: the BIA "may need to be conducted again" as systems change.
   - Draft §§4 and 7 set fixed three-year cycles with no change trigger.

## Challenge: clauses that are ambiguous, hard to enforce, or open to two readings

These are for the COO.

- **§2, "The ICT systems that support them are in scope":** which systems, and who decides which systems support which service?
- **§4 compared with §2:** the BIA covers "each payment service and the customer support desk". The scope also names "the card processing platform" and "the two offices". Are those meant to be outside the BIA?
- **§5, "by a desktop walk-through":** is this the only method allowed, or the minimum?
- **§6, "for all systems":** does this include the out-of-scope marketing website? Who approves what the IT manager sets?
- **§3, "runs the programme day to day":** which decisions sit with the BCM officer, and which with the COO?
- **§7:** can anything bring a review forward, such as an incident, a test result or an audit finding?
- **Whole document:** there is no approval body or approval date, and no next review date.

## Gaps

- **Draft status.** The policy is v0.4, a draft. I reviewed it as the document under review, not as current policy. Its document control has an owner, version and date, but no review date.
- **Your intake answers (your own statements, not sources).**
  - Frameworks: DORA and NIST SP 800-34, all of each.
  - You didn't answer question 3. I've assumed this is the first policy and that no approved predecessor exists.
- **How much of DORA I compared.** I compared Articles 1 to 16, 24 and 25 against the draft. For Articles 17 to 23 (incident management and reporting, including Art. 23 on payment-related incidents) and Articles 26 onward (TLPT, third-party risk, information sharing, oversight), I read only the headings. I did not read Art. 3's definition of "microenterprise". All of these are **not reviewed** in this pass.
- **NIST SP 800-34 conversion.** The shipped file is a subset: the appendices (templates, sample BIA) are not carried. The guide is written for US federal information systems. Whether it applies to this firm is the owner's call.
- **Frameworks not selected, therefore not reviewed:**
  - Delegated Regulation (EU) 2024/1774, which further specifies the ICT business continuity policy and the simplified framework
  - NIST CSF 2.0
  - UK Cabinet Office *Organisational Resilience Guidance*
  - FONES minimum standard
  - ISO 22301
- **General practice, not in the sources:** the draft does not define "disruption". Should it?
- **Material telling an AI to act:** none found in the draft.
- **For the auditor:** keep the approved document with its owner, version and review date; these dated sources; and the board approval that made it policy.

## Hand-over

- **Legal or compliance:** DORA points 1 to 13. Point 1, whether DORA applies, should come first.
- **Information security:** DORA points 9, 10 and 11.
- **The COO, as document owner:** everything above.

The draft goes into the normal board approval route with its status unchanged. Approving it is management's decision.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> Chief Operating Officer answers these, [legal or compliance] the marked points.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Grep: `(?i)keep-it-running|AI help|Say in the document`
- Grep: `^#{2,3} `
- Grep: `(?i)Say in the document`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Grep: `(?i)(ignore (all|previous|the)|as an AI|language model|assistant[,:]|AI (should|must)|instructions? to (the )?AI)`
- Grep: `(?i)(policy statement|at least annually|annually|tested|test frequency|reviewed|RTO|roles and responsibilities|scope)`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Grep: `^#{2,4} `
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
