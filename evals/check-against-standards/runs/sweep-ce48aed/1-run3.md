# /check-against-standards case 1, run3: Claude Code, guidance at ce48aed

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `e67013b6-50f5-4418-bb25-ce4b0d1bf93e`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

Before I open the draft, I need one thing from you.

**What class of data does `bc-policy-draft.md` contain?** For example: public, internal, confidential, or restricted, or whatever classes your organisation uses.

Please go by what you know about the content, not by any label printed in the file. I'll check your answer against the sensitivity classes this guidance allows for this environment, and only then read the draft.

When you reply, it would also help to say which frameworks you want the draft compared against (for example ISO 22301 or a national or sector standard) and which parts of them. If you have your own copy of a licensed standard, tell me whether its licence lets you use it this way.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Bash: `ls -la; ls -R /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

Thanks. That's medium-class data, and this environment is approved for high, so we can go ahead. I've read `bc-policy-draft.md` (v0.4, 3 September 2026, draft for the management board, owned by the Chief Operating Officer). It contains no text that tries to instruct an AI.

The draft leaves three things open. I need your answers before I compare it against anything:

1. **Which frameworks should I compare it against, and which parts?** These texts ship with the skill:
   - DORA, Regulation (EU) 2022/2554
   - Delegated Regulation (EU) 2024/1774 (the ICT risk management rules)
   - EU AI Act, Articles 4, 26 and 50
   - NIST SP 800-34 Rev. 1, chapters 1 to 5
   - NIST CSF 2.0
   - NIST AI RMF 1.0
   - FONES ICT minimum standard (2023)
   - UK Cabinet Office Organisational Resilience Guidance
   - ESAs JC 2026 25 statement

   ISO 22301 doesn't ship with the skill. I can use it only if you attach your own copy and confirm its licence allows this. Even then I'd cite it by clause number only, without quoting it.

2. **Which country is the institution licensed in, and does DORA apply to it?** The draft calls it a payment institution but doesn't say where it's licensed. That decides whether the EU texts are binding or just a reference point.

3. **Is there an approved policy that this draft replaces, or other dated material it was built from?** For example, an earlier policy version, an organisation chart or the last management review output. If not, I'll record that it was built from no other sources.

I'll list your answers under Gaps as your own statements, not as sources. They can shape what I review, but they won't fill in any values. If you skip a question, I'll write down the assumption I made instead.

**Tool calls (stream-json):**

- Glob: `**/*`
- Glob: `**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/govern.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/README.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/check-against-standards/1/run3/work/bc-policy-draft.md`

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

Sources compared:

- **Document reviewed:** `bc-policy-draft.md`, "Business continuity policy", version 0.4, 3 September 2026. Status: draft for the management board. Owner: Chief Operating Officer. Its header gives no review date.
- **DORA:** Regulation (EU) 2022/2554, Official Journal L 333, 27 December 2022, as adopted. This is the shipped conversion, retrieved 2026-09-10 (`literature/eur-lex/dora-regulation-2022-2554.md`). Where the two differ, EUR-Lex is authoritative.
- **NIST SP 800-34 Rev. 1:** May 2010, Executive Summary and chapters 1 to 5 only. Shipped conversion retrieved 2026-09-10 (`literature/nist/sp-800-34r1-contingency-planning-body.md`). The PDF is authoritative.

# Draft review of the BC policy (v0.4) against DORA and NIST SP 800-34

Everything below is a question for the document owner, the Chief Operating Officer. This review does not say whether the draft meets either framework. Only a person reading the source text can say that. Points marked **⚖** concern a regulation and go to legal or compliance.

## Block 1: DORA (Regulation (EU) 2022/2554)

### Contradictions

| # | Draft passage | DORA passage | Question for the owner |
|---|---|---|---|
| D1 ⚖ | §5: "tested every two years, by a desktop walk-through." | Art. 11(6)(a): "test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions". The second subparagraph adds, for entities other than microenterprises: "scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities". Art. 24(6): "at least yearly, that appropriate tests are conducted on all ICT systems and applications supporting critical or important functions." | How does a two-yearly desktop walk-through relate to yearly testing and to switchover and cyber-attack scenarios? |
| D2 ⚖ | §7: "The policy owner reviews this policy every three years." | Art. 6(5): the ICT risk management framework "shall be documented and reviewed at least once a year … as well as upon the occurrence of major ICT-related incidents, and following supervisory instructions or conclusions derived from relevant digital operational resilience testing or audit processes." Art. 11(1) makes the ICT business continuity policy part of that framework. | Is this policy part of the ICT risk management framework, and if so, how does a three-year review cycle with no event triggers relate to Art. 6(5)? |
| D3 ⚖ | §6: "The IT manager sets the recovery time objectives for all systems." | Art. 12(6): "In determining the recovery time and recovery point objectives for each function, financial entities shall take into account whether it is a critical or important function and the potential overall impact on market efficiency." | The draft sets objectives per system, while Art. 12(6) speaks of each function. The draft names no recovery point objectives. Which applies here, and who sets the RPOs? |

### Gaps (DORA passages with no counterpart found in the draft)

| # | DORA passage | Draft section | Question for the owner |
|---|---|---|---|
| G1 ⚖ | Art. 5(2)(e): the management body shall "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy and ICT response and recovery plans" | §3, §7 | The draft names only the COO as owner and reviewer. What role does the management board have in approving, overseeing and reviewing this policy? |
| G2 ⚖ | Art. 11(1): an ICT business continuity policy "forming an integral part of the overall business continuity policy" | §1, §2 | Is this the overall business continuity policy, the ICT business continuity policy, or both? Where is the other one? |
| G3 ⚖ | Art. 11(2)(a): "ensure the continuity of the financial entity's critical or important functions" (defined in Art. 3(22)) | §1, §2 | The draft speaks of "payment services". Have the critical or important functions been identified, and where are they recorded? |
| G4 ⚖ | Art. 11(2)(e), Art. 11(7), Art. 14: communication and crisis management actions, a crisis management function, crisis communication plans, and "At least one person … tasked with implementing the communication strategy" | none | Where are crisis management and crisis communication covered, and by whom? |
| G5 ⚖ | Art. 11(3): ICT response and recovery plans "shall be subject to independent internal audit reviews" (other than microenterprises) | §3 names the IT manager as plan owner | Who audits the ICT recovery plans, and how often? |
| G6 ⚖ | Art. 11(4) and Art. 28(8): plans for functions "outsourced or contracted through arrangements with ICT third-party service providers"; exit strategies | none | The draft does not mention third-party providers, such as the card processing platform's providers. Where is this covered? |
| G7 ⚖ | Art. 11(5): the BIA covers "the criticality of identified and mapped business functions, support processes, third-party dependencies and information assets, and their interdependencies", using "quantitative and qualitative criteria … and scenario analysis" | §4 | §4 covers payment services and the support desk. Does the BIA also cover third-party dependencies, information assets, the card platform and the two offices listed in §2? |
| G8 ⚖ | Art. 11(8): "readily accessible records of activities before and during disruption events" | none | Who keeps these records, and where? |
| G9 ⚖ | Art. 12(1)–(4), (7): backup policies, restoration procedures, segregated restore systems, redundant ICT capacity, data integrity checks after recovery | none | Is this covered in another policy, and if so, which one? |
| G10 ⚖ | Art. 13(2), (5), (6): post-incident reviews; senior ICT staff report "at least yearly to the management body"; compulsory resilience training | none | Where are lessons learned, yearly reporting to the board and training covered? |
| G11 ⚖ | Art. 17, 19, 23: incident management and reporting, which Art. 23 extends to "operational or security payment-related incidents" at payment institutions | none | Is incident classification and reporting deliberately out of scope here and covered by another policy? |
| G12 ⚖ | Art. 24(4): tests "undertaken by independent parties, whether internal or external"; Art. 24(5): procedures to "prioritise, classify and remedy all issues revealed" | §5 | Who carries out the tests, and how are findings tracked to closure? |
| G13 ⚖ | Art. 2(1)(b), Art. 16(1): exempted payment institutions fall under the simplified framework of Art. 16 instead of Arts 5–15. Several duties apply only to entities "other than microenterprises" (Art. 3(60): fewer than 10 persons). Art. 26: TLPT applies to entities identified by the competent authority. | header ("small payment institution with 140 staff") | Which regime applies: the full regime, the Art. 16 simplified regime, or TLPT identification? Legal or compliance should settle this before the board reads the policy. |
| G14 ⚖ | Art. 8(1): identify and classify "all ICT supported business functions" | §2: "the marketing website is not" in scope | Was the exclusion of the marketing website based on an identification or classification, and where is that recorded? |

### Passages not turned into questions

You asked me to compare against all of DORA. Arts 15, 18(3), 20–22, 26(9)–(11), 31–44 and 46–64 address the ESAs, competent authorities, critical ICT providers, or amendments to other acts. I read them and raised no question about the policy. That choice is open to the owner's review.

## Block 2: NIST SP 800-34 Rev. 1 (not a regulation, so no ⚖ marks)

| # | SP 800-34 passage | Draft section | Question for the owner |
|---|---|---|---|
| N1 | §3.1, key policy elements: "Roles and responsibilities; Scope …; Resource requirements; Training requirements; Exercise and testing schedules; Plan maintenance schedule; and Minimum frequency of backups and storage of backup media" | §2, §3 and §5 correspond to scope, roles and testing | The draft has no counterpart for resource requirements, training requirements, a plan maintenance schedule (§7 covers the policy only), or backup frequency and storage. Should it? |
| N2 | §3.1 sample policy statement (given as a sample, not a requirement): plans "must be reviewed annually" and capabilities "shall be tested annually" | §5 ("every two years"), §7 ("every three years") | Both differ from the sample's yearly cycle. Is that intended? |
| N3 | §3.2.1: the coordinator, "with the process owners, leadership and business managers determine the acceptable downtime"; RTO must normally be shorter than MTD; RPO defined | §6: "The IT manager sets the recovery time objectives for all systems." | Should business owners and leadership take part in setting downtime and RTOs? Should §6 link RTOs to the BIA in §4 and name MTD and RPO? |
| N4 | §3.5.4: a tabletop is "sufficient" for low-impact systems; moderate-impact systems call for "a functional exercise … to include an element of system recovery from backup media"; high-impact systems call for "a full-scale functional exercise … [with] a system failover to the alternate location" | §5: a desktop walk-through for all plans | What impact level do the payment and card systems have, and does one desktop format fit all of them? |
| N5 | §3.5.2: training "should be provided at least annually" | none | Is training covered anywhere? |
| N6 | §3.6: "When a significant change occurs, the BIA should be updated"; §3.5: tests and exercises "following organizational or system changes" | §4, §5 (fixed intervals only) | Should change-driven triggers sit alongside the fixed intervals? |
| N7 | §3.4.6: "a single authoritative role for overall decision-making responsibility, including plan activation" | §3 | Who activates the plans? |

SP 800-34 §1.2 states that the guide "does not address continuity of mission/business processes". This block therefore covers only the ICT side of the policy.

## Challenge: clauses that are ambiguous, unenforceable, or open to two readings

1. **§2:** "The ICT systems that support them are in scope." Does "them" mean every item listed (including the offices and customer support) or only the payment services?
2. **§3:** "runs the programme day to day." The "programme" is not defined. Who approves plans, and who can activate them?
3. **§4:** "every three years." Counted from when? §4 omits the card processing platform and the two offices that §2 puts in scope. Was that deliberate?
4. **§5:** "tested … by a desktop walk-through." The draft doesn't say who runs the test, what counts as a pass, or who receives the results. As written, nobody can check whether it was done properly.
5. **§6:** "all systems." Does this include systems outside the scope, such as the marketing website? "Sets" gives no basis (such as the BIA) and no approval step.
6. **§7:** The draft names no approving body for the policy, even though its status is "draft for the management board". It also doesn't say what the review produces or who receives it.
7. **§1 vs §2:** The purpose mentions only payment services. The scope adds customer support and offices. Which one governs?
8. **Header:** The document control has an owner and version but no review date.

## Gaps (what the sources leave open)

- **Your intake answers, recorded as your statements and not as sources.** Frameworks: "DORA and NIST SP 800-34". "All of it": I took this to mean all parts of both texts as shipped. I didn't get an answer on the country of licence or whether DORA applies. I assumed DORA may apply and marked every DORA point for legal or compliance. You skipped question 3, so I assumed the draft was built from no other dated sources: no prior policy, organisation chart or management review output.
- **The draft is a draft.** I reviewed it as written. It is not a current approved policy, it has no review date, and nothing in the sources shows the management review or other sources it was built from.
- **Frameworks not selected, so not reviewed:**
  - Delegated Regulation (EU) 2024/1774. This one matters here: DORA Art. 15(d) delegates "the components of the ICT business continuity policy" to it.
  - EU AI Act (Arts 4, 26, 50)
  - NIST CSF 2.0
  - NIST AI RMF 1.0
  - FONES ICT minimum standard
  - UK Cabinet Office Organisational Resilience Guidance
  - ESAs JC 2026 25 statement
  - ISO 22301, which doesn't ship with the skill; no licensed copy was attached
  - National payment-services law and EBA guidelines: not in the sources
- **Source limits.** DORA is the text as adopted, and any later amendments are not in the sources. SP 800-34 is from 2010, written for US federal systems, and its appendices (including the plan and BIA templates) are not carried.
- **Planted text:** I found no passage in the draft that instructs an AI.

## Before approval

Take these questions to legal, compliance, information security and the document owner before the draft enters the board's approval route. The draft keeps its status (draft, v0.4) until the board decides. Final policy decisions stay with management.

> Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

The Chief Operating Officer answers these, legal or compliance the marked points.

**Tool calls (stream-json):**

- Grep: `^#|^Article|^\*\*Article`
- Grep: `^#`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Grep: `Say in the document that AI helped`
