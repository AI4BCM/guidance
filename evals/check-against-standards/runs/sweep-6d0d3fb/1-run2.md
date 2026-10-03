# /check-against-standards case 1, run2: Claude Code, guidance at 6d0d3fb

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `ecd9e4d6-5259-44af-a094-048102cdab2d`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

Before I open `bc-policy-draft.md`, I need one thing from you: **what class of data is in the draft?**

For example, is it general internal policy text? Or does it hold any high-sensitivity material, such as:

- BIA data or risk assessment detail
- recovery strategies or design assumptions
- vulnerabilities or control weaknesses
- supplier weaknesses or contractual dependencies
- personal data or contact lists
- security-related architecture or site detail
- board papers or executive-session material (a draft going to the board may count)
- audit findings the audit owner hasn't cleared yet

Please also confirm that this environment is approved for that class. I'll go by your answer, not by any marking in the file. If it holds passwords, keys or access tokens, remove them first, because those go into no tool.

Once you've answered, I'll read the draft and ask which frameworks to check it against.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Bash: `ls -la; ls /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literat`
- Grep: `Sensitivity classes`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I've read the draft: **Business continuity policy, version 0.4, 3 September 2026, status "draft for the management board", owner Chief Operating Officer.** It has seven short sections and contains no text telling an AI to act.

Before I review it, I have three questions. I'll list your answers under Gaps as your own statements, not as sources.

1. **Which frameworks should I check it against, and which parts?** These texts come with the skill, each with its own dated header:
   - DORA, Regulation (EU) 2022/2554
   - Delegated Regulation (EU) 2024/1774, the ICT risk management standards
   - ESAs Joint Committee statement JC 2026 25
   - NIST SP 800-34 Rev. 1, chapters 1–5
   - NIST CSF 2.0
   - FONES ICT minimum standard (2023)
   - UK Cabinet Office Organisational Resilience Guidance

   ISO 22301 doesn't come with the skill. I can use it only if you attach your own copy and confirm your licence allows this use. Even then, I'll cite it by clause number only. Anything you don't select will be listed as "not reviewed".

2. **If you choose DORA or 2024/1774: does your institution fall under the full ICT risk management framework or the simplified one (DORA Article 16 / RTS Title III)?** This decides which articles I compare the draft with. I'll record your answer as your statement; it isn't my finding.

3. **Is there a current approved policy that v0.4 replaces, or a prior management review output?** If so, please attach them. Otherwise I'll treat v0.4 as the only policy document and note under Gaps that there's no approved baseline.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep5/runs/check-against-standards/1/run2/work/bc-policy-draft.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/govern.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/README.md`

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

# Review draft: Business continuity policy v0.4 against DORA and NIST SP 800-34 Rev. 1

**Sources, one line each**
- **Document reviewed:** `bc-policy-draft.md`, "Business continuity policy", version 0.4, 3 September 2026, status "draft for the management board", owner Chief Operating Officer. There is no review date.
- **Framework 1:** `literature/eur-lex/dora-regulation-2022-2554.md`, Regulation (EU) 2022/2554, OJ L 333 of 27 December 2022, "as adopted", retrieved 2026-09-10. EUR-Lex is authoritative. Reuse is allowed under Decision 2011/833/EU.
- **Framework 2:** `literature/nist/sp-800-34r1-contingency-planning-body.md`, NIST SP 800-34 Rev. 1, May 2010, retrieved 2026-09-10. This copy holds the Executive Summary and Chapters 1–5 only. It is a U.S. Government work.

This review only lists gaps, contradictions and questions. It does not say whether the policy meets either framework; only a person, reading the source text, can say that.

---

## Block 1: DORA (Regulation (EU) 2022/2554)

Every point in this block concerns a regulation. **Each one is marked [L/C] for legal or compliance review.**

### Contradictions (both passages quoted)

**D-C1. How often plans are tested** [L/C]
- Policy §5: "Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through."
- DORA Art. 11(6)(a): "test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions".
- Question for the policy owner: how does a two-year cycle relate to "at least yearly"? And why is there no test triggered by changes to ICT systems?

**D-C2. How plans are tested** [L/C]
- Policy §5: "by a desktop walk-through."
- DORA Art. 11(6), second subparagraph: financial entities other than microenterprises "shall include in the testing plans scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities".
- DORA Art. 24(6): "at least yearly, that appropriate tests are conducted on all ICT systems and applications supporting critical or important functions."
- Question: does a desktop walk-through, as the only method named, cover cyber-attack scenarios and switchovers?

**D-C3. How often the policy is reviewed** [L/C]
- Policy §7: "The policy owner reviews this policy every three years."
- DORA Art. 6(5): "The ICT risk management framework shall be documented and reviewed at least once a year … as well as upon the occurrence of major ICT-related incidents, and following supervisory instructions or conclusions derived from relevant digital operational resilience testing or audit processes."
- DORA Art. 11(1) places the ICT business continuity policy "as part of the ICT risk management framework referred to in Article 6(1)".
- Question: is this document meant to be, or to contain, the Art. 11(1) ICT business continuity policy? If so, how does a three-year review with no event triggers relate to Art. 6(5) and Art. 11(6), last subparagraph?

**D-C4. Who sets recovery objectives** [L/C]
- Policy §6: "The IT manager sets the recovery time objectives for all systems."
- DORA Art. 12(6): "In determining the recovery time and recovery point objectives for each function, financial entities shall take into account whether it is a critical or important function and the potential overall impact on market efficiency."
- DORA Art. 5(2): the management body "shall define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework".
- Questions:
  - The policy sets objectives per system; Art. 12(6) speaks of each function. How do the two relate?
  - What role does the management body have in the objectives the IT manager sets?

**D-C5. Who approves the policy and plans** [L/C]
- Policy §3: "The Chief Operating Officer owns this policy. … The IT manager owns the ICT recovery plans."
- DORA Art. 5(2)(e): the management body shall "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy and ICT response and recovery plans".
- Question: the policy names owners but gives the management board no role in approval, oversight or periodic review. Is that intended?

### Gaps (a DORA passage with no counterpart in the policy)

Each gap is a question for the policy owner: is this covered elsewhere, and if so, where?

| # | DORA passage | Question for the owner |
|---|---|---|
| D-G1 | Art. 11(2)(a): arrangements "aiming to … ensure the continuity of the financial entity's critical or important functions" | The policy never uses "critical or important functions". How are they identified, and by whom? [L/C] |
| D-G2 | Art. 11(5): the BIA "shall consider the criticality of identified and mapped business functions, support processes, third-party dependencies and information assets, and their interdependencies" | §4 says the BIA covers "each payment service and the customer support desk". Does it also cover third-party dependencies, information assets, interdependencies, the card processing platform and the two offices named in §2? [L/C] |
| D-G3 | Art. 11(5): "quantitative and qualitative criteria, using internal and external data and scenario analysis" | §4 names no method or criteria. Is a method defined anywhere? [L/C] |
| D-G4 | Art. 8(1) and 8(2): classification and risk scenarios reviewed "at least yearly" | §4's three-year BIA cycle has no counterpart for yearly review or for change-driven updates. Is this intended? [L/C] |
| D-G5 | Art. 11(2)(e), Art. 11(7), Art. 14(1)–(3): communication and crisis management, a "crisis management function", crisis communication plans, and "At least one person … tasked with implementing the communication strategy" | The policy has no crisis management or communication content and names no communication role. [L/C] |
| D-G6 | Art. 11(6)(b): "test the crisis communication plans" | No counterpart. [L/C] |
| D-G7 | Art. 11(8): "readily accessible records of activities before and during disruption events" | No counterpart. [L/C] |
| D-G8 | Art. 11(3): ICT response and recovery plans "shall be subject to independent internal audit reviews" | §3 assigns ownership of the ICT recovery plans; the policy says nothing about audit. [L/C] |
| D-G9 | Art. 11(4): plans tested "notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers" | The policy does not mention third parties at all. [L/C] |
| D-G10 | Art. 12(1)–(4): backup policies, restoration and recovery procedures, segregated restore systems, redundant ICT capacity; Art. 12(6): recovery point objectives | The policy covers RTO only, with nothing on backup, RPO or redundancy. Are these in another document? [L/C] |
| D-G11 | Art. 12(7): data integrity checks and reconciliations during recovery | No counterpart. [L/C] |
| D-G12 | Art. 13(2), 13(3), 13(5): post-incident reviews; lessons from tests fed into risk assessment; "Senior ICT staff shall report at least yearly to the management body" | §5 does not say what happens with test results, and there is no lessons-learned or reporting line. [L/C] |
| D-G13 | Art. 13(6): ICT security awareness and digital operational resilience training "as compulsory modules"; Art. 5(4): management body training | No training content. [L/C] |
| D-G14 | Art. 6(4): ICT risk managed by "a control function" with "an appropriate level of independence"; Art. 24(4): "tests are undertaken by independent parties" | §3 gives the BCM officer and the IT manager both design and ownership. Who provides independent control and testing? [L/C] |
| D-G15 | Art. 6(8)(b): "the risk tolerance level for ICT risk … and analysing the impact tolerance for ICT disruptions" | The policy has no tolerance or appetite statement for §6's objectives to rest on. [L/C] |
| D-G16 | Art. 28(8): "exit strategies" for ICT services supporting critical or important functions, and "contingency measures … to maintain business continuity" | No counterpart. Is this in a third-party policy? [L/C] |
| D-G17 | Chapter III, Art. 17–23: incident management, classification and reporting. Art. 23 extends it to payment institutions for "operational or security payment-related incidents". | No counterpart. Is this in an incident policy? [L/C] |
| D-G18 | Chapter IV, Art. 24–25: a "digital operational resilience testing programme"; Art. 26: TLPT for entities the competent authority identifies | §5 is the only testing passage. Is there a separate testing programme, and has any TLPT identification been received? [L/C] |
| D-G19 | Chapter V, Art. 28–30: ICT third-party risk strategy, register of information, contractual provisions | No counterpart. [L/C] |
| D-G20 | Chapter VI, Art. 45: voluntary information-sharing arrangements | No counterpart. Possibly out of scope for this policy; for the owner to decide. [L/C] |

**Scope question** [L/C]: §2 excludes "the marketing website". DORA Art. 8(1) asks entities to "identify, classify and adequately document all ICT supported business functions". Is the exclusion based on a documented classification?

---

## Block 2: NIST SP 800-34 Rev. 1 (Chapters 1–5)

This is U.S. federal guidance, not a regulation, so points in this block are not marked for legal review.

### Gaps against the key policy elements in §3.1

§3.1 lists the key policy elements as: "Roles and responsibilities; Scope …; Resource requirements; Training requirements; Exercise and testing schedules; Plan maintenance schedule; and Minimum frequency of backups and storage of backup media."

| # | NIST element | Counterpart in the policy | Question for the owner |
|---|---|---|---|
| N-G1 | Resource requirements | none | Who provides resources for the programme, and how? |
| N-G2 | Training requirements | none | Who is trained, in what, and how often? |
| N-G3 | Plan maintenance schedule | §7 covers the policy only, not the plans | How often are the BC and ICT recovery plans reviewed? |
| N-G4 | Minimum frequency of backups and storage of backup media | none | Where is this set? |
| N-G5 | Roles, scope, exercise and testing schedule | §3, §2, §5 | Present. See the contradictions and challenge points below. |

**N-G6.** §3.1 says the policy "should define the organization's overall contingency objectives". §1 states a purpose but no objectives. Is that intended?

**N-G7.** §3.1 says plans "should be coordinated with related organization-wide policies and programs, including information system security, physical security, human resources…". The policy names no related documents. Should it?

**N-G8.** §3.2.1 defines the RPO as "the point in time … to which mission/business process data can be recovered". The policy has no RPO. Where is it set?

### Contradictions (both passages quoted)

**N-C1. Recovery objectives and the BIA**
- Policy §6: "The IT manager sets the recovery time objectives for all systems."
- NIST §3.2.1: the ISCP Coordinator, "with the process owners, leadership and business managers determine the acceptable downtime". Also: "The MTD represents the total amount of time the system owner/authorizing official is willing to accept". And: "the RTO must normally be shorter than the MTD."
- Questions:
  - Why does §6 have one IT role setting the RTO, with no link to the §4 BIA, no maximum tolerable downtime, and no business owner involved?
  - Is that intended?

**N-C2. Desktop tests for every plan**
- Policy §5: all plans are tested "by a desktop walk-through".
- NIST §3.5 (the TT&E passage): "For low-impact systems, a tabletop exercise … is sufficient". For moderate-impact systems, "a functional exercise … should include an element of system recovery from backup media". For high-impact systems, "a full-scale functional exercise … should include a system failover to the alternate location."
- Question: what impact level do the card processing platform and the payment systems have? Is a desktop walk-through meant for all of them?

**N-C3. Review only on a fixed cycle**
- Policy §7: "every three years".
- NIST §3.7: "the plan should be reviewed for accuracy and completeness at an organization-defined frequency or whenever significant changes occur". This passage is about plans, not policy.
- The NIST sample policy statement in §3.1 reads "must be reviewed annually" and "tested annually". It is labelled a sample.
- Question: should there be a review triggered by change?

---

## Challenge: clauses that are ambiguous, unenforceable or open to two readings

Each point is a question for the policy owner, tied to its passage.

1. **§1, "a disruption":** the term is undefined. Does it cover ICT incidents, loss of an office, supplier failure, staff unavailability?
2. **§2, "The ICT systems that support them are in scope":** who decides which systems "support" in-scope services, and where is that list kept? There are two readings: all systems with any link to them, or only those named in a BIA.
3. **§3, "runs the programme day to day":** the BCM officer's authority and deliverables are undefined. Nobody is named as deputy for any role, and the management board, which the draft is going to, has no role.
4. **§4, "every three years":** is a BIA also required after a significant change, such as a new service, a new office or a new key supplier? As written, nothing triggers one.
5. **§4 vs §2:** §2 puts "the card processing platform … and the two offices" in scope, but §4 names only "each payment service and the customer support desk". Is the platform covered as a payment service or not?
6. **§5, "tested every two years":** is that each plan every two years, or the programme as a whole? Who runs the test, who gets the results, and who must act on findings?
7. **§6, "sets … for all systems":** "all systems" could mean all systems in the §2 scope or every system the company runs. Also, "sets" has no approver, no basis such as a BIA, and no RPO.
8. **§7, "The policy owner reviews this policy":** the owner reviews their own policy, and the section names no approver for changes. Who approves a revised version?

As you asked for a review, I've left all of these as questions and have not proposed replacement wording.

---

## Gaps (what the sources leave open)

- **Document status:** the reviewed policy is a draft (v0.4, "draft for the management board"). It is still the document reviewed here. It has an owner and a version but **no review date**, and no approval record yet.
- **Your intake answers (your statements, not sources):**
  1. The frameworks selected are DORA and NIST SP 800-34.
  2. On full vs simplified framework you said "All of it". I read that as the whole regulation and the full framework (Art. 5–15), not Art. 16. Whether the institution is a "payment institution exempted pursuant to Directive (EU) 2015/2366" under Art. 16(1) is not settled by any source here. [L/C]
  3. You didn't answer whether there's a prior approved policy or a management review output. I assumed there is none, and no baseline was compared.
- **Organisation:** the draft's header says the organisation is "invented for this eval". Noted, not used as a fact.
- **Frameworks not selected, so not reviewed:**
  - Delegated Regulation (EU) 2024/1774. Under DORA Art. 15(d) it specifies "the components of the ICT business continuity policy", so it's directly relevant if DORA applies. [L/C]
  - ESAs JC 2026 25
  - NIST CSF 2.0
  - FONES ICT minimum standard
  - UK Cabinet Office guidance
  - ISO 22301: not supplied with the skill and no licensed copy attached
- **Source limits:**
  - The DORA file is the text "as adopted". Later amendments were not checked; EUR-Lex is authoritative.
  - The NIST file leaves out the appendices (the BIA and ISCP templates, the sample TT&E table), and §3.5's table is not reconstructed.
  - NIST SP 800-34 is U.S. federal guidance from May 2010. Whether it fits an EU payment institution is for the owner to decide.
- **Microenterprise status:** several DORA duties apply to entities "other than microenterprises". At 140 staff, the institution appears to fall outside the Art. 3(60) microenterprise definition, but that's for compliance to confirm. [L/C]
- **Text telling an AI to act:** none found in the draft.

---

**Who reviews what:**
- **The policy owner (COO)** answers every question above.
- **Legal or compliance** reviews everything marked [L/C], before the draft enters the board approval route.
- The draft goes to the board with its status unchanged; approval is the management board's decision.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> [policy owner] answers these, [legal or compliance] the marked points.

**Tool calls (stream-json):**

- Glob: `literature/**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/validate.md`
- Grep: `Say in the document that AI helped`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Grep: `^#+ Article (5|6|11|12|13|14|16|24|25) `
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Grep: `^#+ (CHAPTER|Article (2[5-9]|30|45))`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Grep: `exit strateg|Article 64|shall apply from`
- Grep: `^(\d\.\d+(\.\d+)? [A-Z]|CHAPTER|Chapter)`
- Grep: `policy statement|at least annually|annually|roles and responsibilities|key elements`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Grep: `annual|at least yearly|reviewed for accuracy|BIA should be|tested|functional exercise|full-scale`
- Grep: `.{0,300}(at a minimum, annually|reviewed for accuracy|annually or whenever|tabletop exercises).{0,300}`
- Grep: `.{0,400}reviewed for accuracy.{0,400}`
- Grep: `.{0,300}(Tabletop exercises|FIPS 199 moderate|functional exercise).{0,300}`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Grep: `.{0,250}Recovery Time Objective \(RTO\).{0,350}`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
