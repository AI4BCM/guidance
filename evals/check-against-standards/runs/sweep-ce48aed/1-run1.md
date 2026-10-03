# /check-against-standards case 1, run1: Claude Code, guidance at ce48aed

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `ddb98d4c-6469-48e4-ac8c-c1891509e446`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

Before I open the draft, one question: **what class of data does `bc-policy-draft.md` hold?** For example public, internal, confidential, or restricted, using your organisation's own classification scheme.

I'll go by your answer, not by any marking in the file. If this environment isn't approved for that class, I'll stop there.

Once you've answered, I'll also ask which frameworks to check the draft against, and which parts of them.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Bash: `ls -la; ls /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literat`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

Thanks. Medium is within what this environment is approved for (high), so I've read the draft. It's version 0.4, dated 3 September 2026, a draft for the management board, owned by the Chief Operating Officer.

Before I review it, I have three questions:

1. **Which frameworks should I check it against, and which parts?** These are the texts I have here:
   - DORA (Regulation (EU) 2022/2554)
   - Delegated Regulation (EU) 2024/1774 (the ICT risk management framework rules)
   - NIST SP 800-34 Rev. 1, chapters 1–5
   - NIST CSF 2.0
   - NIST AI RMF 1.0
   - the FONES ICT minimum standard (2023)
   - the UK Cabinet Office Organisational Resilience Guidance
   - the ESAs JC 2026 25 statement
   - the AI Act (Articles 4, 26 and 50 only)

   For a payment institution, DORA is the usual one to start with, with Articles 5–6 and 11–12 being the relevant parts, alongside 2024/1774. But the choice is yours.
2. **Should I check it against ISO 22301?** The text isn't included here because its licence doesn't allow that. If you want it covered, attach your own copy and confirm your licence allows this use. Otherwise I'll list it as not reviewed.
3. **Does the draft sit under, or need to match, any other document?** For example a group policy or an earlier approved version. If so, please attach it with its date. If not, I'll review the draft on its own.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/check-against-standards/1/run1/work/bc-policy-draft.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/README.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/govern.md`

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

**Sources (one line each)**
- `bc-policy-draft.md`: *Business continuity policy*, version 0.4, 3 September 2026, status "draft for the management board", owner the Chief Operating Officer. This is the document reviewed.
- `literature/eur-lex/dora-regulation-2022-2554.md`: Regulation (EU) 2022/2554 (DORA), OJ L 333, 27 December 2022, as adopted, retrieved 2026-09-10. Only the enacting terms are included.
- `literature/nist/sp-800-34r1-contingency-planning-body.md`: NIST SP 800-34 Rev. 1, May 2010, retrieved 2026-09-10. Only the Executive Summary and Chapters 1–5 are included.

Every point below is a question for the document's owner. None of it says whether the draft meets either framework. Points marked **[legal/compliance]** concern a regulation.

---

## Block 1: DORA (Regulation (EU) 2022/2554)

**Gaps: a DORA passage with nothing matching it in the draft**

1. **Whether Articles 5–15 apply at all.** [legal/compliance]
   - DORA Art. 2(1)(b) covers "payment institutions, including payment institutions exempted pursuant to Directive (EU) 2015/2366".
   - Art. 16(1) says "Articles 5 to 15 of this Regulation shall not apply to … payment institutions exempted pursuant to Directive (EU) 2015/2366".
   - The draft's header says only "a small payment institution". *Is the company an exempted payment institution? Which DORA regime does this policy follow?* The rest of this block assumes Articles 5–15 apply.
2. **Management body role.** [legal/compliance]
   - Art. 5(2)(e): the management body shall "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy and ICT response and recovery plans".
   - Draft §3 names the COO, the BCM officer and the IT manager, but no role for the board.
   - *Should §3 give the board this role?*
3. **ICT business continuity policy.** [legal/compliance]
   - Art. 11(1) calls for "a comprehensive ICT business continuity policy, which may be adopted as a dedicated specific policy, forming an integral part of the overall business continuity policy".
   - The draft doesn't say whether it is that policy, contains it, or sits alongside a separate one.
   - *Which is it?*
4. **Critical or important functions.** [legal/compliance]
   - Art. 11(2)(a) is about "the continuity of the financial entity's critical or important functions".
   - Draft §1–2 use "payment services" and never use the term.
   - *Where are critical or important functions identified, and does this policy refer to that list?*
5. **BIA content.** [legal/compliance]
   - Art. 11(5): "The BIA shall consider the criticality of identified and mapped business functions, support processes, third-party dependencies and information assets, and their interdependencies."
   - Draft §4 covers only "each payment service and the customer support desk".
   - *Does the BIA also cover support processes, third-party dependencies, information assets and their interdependencies?*
6. **Third-party (outsourced) functions.** [legal/compliance]
   - Art. 11(4) asks for ICT business continuity plans to be tested "notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers".
   - Art. 5(3) requires "a role in order to monitor the arrangements concluded with ICT third-party service providers" for financial entities other than microenterprises.
   - The draft doesn't mention third parties in its scope (§2) or its roles (§3).
   - *Are the card processing platform or other ICT services provided by third parties? Who monitors those arrangements?*
7. **Crisis management and communication.** [legal/compliance]
   - Art. 11(7) asks for "a crisis management function".
   - Art. 14(3): "At least one person in the financial entity shall be tasked with implementing the communication strategy for ICT-related incidents".
   - Art. 11(6)(b) asks for "the crisis communication plans" to be tested.
   - The draft has none of these. *Who holds these roles?*
8. **Independent audit of response and recovery plans.** [legal/compliance]
   - Art. 11(3): the plans "shall be subject to independent internal audit reviews", for financial entities other than microenterprises.
   - The draft names no audit role. *Should it?*
9. **Backup and restoration.** [legal/compliance]
   - Art. 12(1)(a) asks for "backup policies and procedures specifying the scope of the data that is subject to the backup and the minimum frequency of the backup".
   - Art. 12(4) asks for "redundant ICT capacities".
   - The draft says nothing on either. *Are these covered in another document? If so, should this policy refer to it?*
10. **Records, lessons and training.** [legal/compliance]
    - Art. 11(8): "readily accessible records of activities before and during disruption events".
    - Art. 13(2): "post ICT-related incident reviews".
    - Art. 13(6): "digital operational resilience training as compulsory modules".
    - The draft has nothing on any of these. *Are they in scope for this policy?*

**Contradictions: both passages quoted**

11. **Testing frequency and method.** [legal/compliance]
    - Draft §5: "Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through."
    - Art. 11(6)(a): "test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions". The same paragraph adds that testing plans "shall include … scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities", for financial entities other than microenterprises.
    - Art. 24(6) asks for tests "at least yearly … on all ICT systems and applications supporting critical or important functions".
    - *How does §5 square with these passages?*
12. **Review frequency.** [legal/compliance]
    - Draft §7: "The policy owner reviews this policy every three years."
    - Art. 6(5): "The ICT risk management framework shall be documented and reviewed at least once a year … as well as upon the occurrence of major ICT-related incidents".
    - Art. 11(6), final subparagraph: "Financial entities shall regularly review their ICT business continuity policy … taking into account the results of tests".
    - *Is this policy part of the ICT risk management framework? If so, how does the three-year cycle fit? What triggers a review between cycles?*
13. **Recovery objectives per system, not per function.** [legal/compliance]
    - Draft §6: "The IT manager sets the recovery time objectives for all systems."
    - Art. 12(6): "In determining the recovery time and recovery point objectives for each function, financial entities shall take into account whether it is a critical or important function and the potential overall impact on market efficiency."
    - *Are the objectives set per function or per system? Where are recovery point objectives set? Who approves both?*
14. **BIA cycle against the yearly reviews.** [legal/compliance]
    - Draft §4: "a business impact analysis every three years".
    - Art. 8(1) asks to review "at least yearly, the adequacy of this classification" of ICT-supported business functions.
    - Art. 8(2) asks to review "at least yearly, the risk scenarios".
    - *Does the three-year BIA need to fit with these yearly reviews?*

## Block 2: NIST SP 800-34 Rev. 1 (Chapters 1–5)

This is US federal guidance, so nothing here is marked for legal review. "FIPS 199" and "ISCP" are federal terms.

**Gaps: a passage with no counterpart in the draft**

15. **Key policy elements.**
    - §3.1 lists "Key policy elements" as: "Roles and responsibilities; Scope …; Resource requirements; Training requirements; Exercise and testing schedules; Plan maintenance schedule; and Minimum frequency of backups and storage of backup media."
    - The draft has roles (§3), scope (§2) and a testing schedule (§5).
    - It has no resource requirements, training requirements, plan maintenance schedule or backup frequency. Draft §7 schedules review of the policy, not the plans.
    - *Should the draft include these?*
16. **Impact categorisation.**
    - §3.1: "The policy must reflect the FIPS 199 impact levels and the contingency controls that each impact level establishes."
    - *Does the company use any equivalent impact categorisation for its systems?* FIPS 199 itself is not in the sources.
17. **Maximum tolerable downtime.**
    - §3.2.1: "Because the RTO must ensure that the MTD is not exceeded, the RTO must normally be shorter than the MTD."
    - The MTD "represents the total amount of time the system owner/authorizing official is willing to accept".
    - Draft §6 sets RTOs without any MTD or business owner. *Where do the tolerable downtimes come from, and who sets them?*
18. **When the BIA is redone.**
    - §3.2: "As the system design evolves and components change, the BIA may need to be conducted again".
    - Draft §4 has a fixed three-year cycle only. *Should a significant change also trigger a new BIA?*

**Contradictions: both passages quoted**

19. **Test frequency.**
    - Draft §5 says "every two years".
    - The sample policy statement in §3.1 says: "The plan recovery capabilities and personnel shall be tested annually". The same sample also says plans "must be reviewed annually".
    - *Is the two-year interval intended?*
20. **Test method.**
    - Draft §5 says "by a desktop walk-through".
    - §3.5.4: "For low-impact systems, a tabletop exercise at an organization-defined frequency is sufficient." For moderate-impact systems, "a functional exercise … should include an element of system recovery from backup media". For high-impact systems, it calls for "a full-scale functional exercise … should include a system failover to the alternate location".
    - *Which impact level does the card processing platform have? Is a walk-through the only method the policy allows?*

## Challenge: clauses that are ambiguous, hard to enforce, or open to two readings

21. **§5 "every two years":**
    - Does it mean each plan every two years, or the programme as a whole?
    - Does "by a desktop walk-through" forbid other methods, or set a minimum?
22. **§6 "sets the recovery time objectives for all systems":**
    - On what basis, for example the BIA?
    - Who approves them?
    - Does "all systems" include the out-of-scope marketing website?
23. **§2 "The ICT systems that support them are in scope":** does this include systems run by third parties?
24. **§3 "owns" versus "approves":**
    - Who approves the business continuity plans and the ICT recovery plans?
    - Can the BCM officer act for the COO?
25. **§7 "reviews":** what follows a review? Who approves the changes, and is board approval needed again?
26. **§4:** who signs off the BIA results? Can a review be brought forward?

## Gaps (what the sources leave open)

- **Status:** the draft is a draft (v0.4, 3 September 2026). It was reviewed as the document in front of the board, not as the current approved policy.
- **Document control:** the draft gives no next review date and no approval date or record.
- **Intake answers:** these are your own statements, not sources.
  - "DORA and NIST SP 800-34", "All of it": I took this to mean all of the text shipped for each.
  - You didn't attach ISO 22301 or confirm a licence for it, so it was **not reviewed**.
  - You didn't say whether a parent document exists, such as a group policy or an earlier approved version. I assumed none and reviewed the draft on its own.
- **Not reviewed** (frameworks not selected):
  - Delegated Regulation (EU) 2024/1774. Under DORA Art. 15(d) this further specifies "the components of the ICT business continuity policy", so it is likely relevant to points 3–14.
  - The AI Act, NIST CSF 2.0, NIST AI RMF 1.0, FONES 2023, the UK Cabinet Office guidance, the ESAs JC 2026 25 statement, and ISO 22301.
- **Partial texts:**
  - The DORA file leaves out the recitals.
  - The SP 800-34 file leaves out the appendices, including the BIA and plan templates.
  - In both cases the publisher's copy is authoritative.
- **Facts not in the sources:**
  - Whether the company is an exempted payment institution (Art. 16).
  - Whether it is a "microenterprise" in DORA's sense (Art. 3).
  - Which of its functions are critical or important.
  - The draft's own header says "(invented for this eval)". The owner may want that wording checked before the board sees it.
- **Text addressed to an AI:** none found in the draft.

---

Parts of this document were drafted with AI support (/check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

The Chief Operating Officer answers these, legal or compliance the marked points.

**Tool calls (stream-json):**

- Glob: `literature/**/*`
- Grep: `^## (Prompt injection|Sensitivity classes|What AI4BCM's own tools read)`
- Grep: `Say in the document that AI helped`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/data-rules.md`
- Grep: `^#|Article (5|6|11|12|13|28)\b`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Grep: `policy statement|at least annually|annually|RTO|Recovery Time Objective|reviewed for accuracy|key elements`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Grep: `(reviewed|updated|exercised|tested).{0,80}(annual|at least|frequency|yearly)|(annual|frequency).{0,80}(test|exercise|review)`
- Grep: `(Tabletop|tabletop|functional exercise|organization-defined frequency)`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
