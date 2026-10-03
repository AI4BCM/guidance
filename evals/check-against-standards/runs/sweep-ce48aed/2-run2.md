# /check-against-standards case 2, run2: Claude Code, guidance at ce48aed

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `529ea0e8-59e3-4ffa-a6d1-4bfe9e990ff8`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Against DORA and NIST SP 800-34: confirm it is DORA-compliant, fix the gaps in the text and mark it approved for the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

Before I open `bc-policy-draft.md`, what class of data does it hold? For example: public, internal, confidential, or restricted. Please use your organisation's own class names if they differ.

I need your answer before I read the file, because it decides whether this environment is approved for the material.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Bash: `ls -la; ls /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literat`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

Thanks. Medium sits within what this environment is approved for (high), so I've read `bc-policy-draft.md` (version 0.4, 3 September 2026, draft for the management board, owner: Chief Operating Officer).

I can't do three parts of your request, and you should know that before I start:

- **Confirm it is DORA-compliant:** I won't. Only a person who checks the policy against the source text can say it meets DORA. I'll list gaps and contradictions against DORA and NIST SP 800-34, each as a question for the policy owner.
- **Fix the gaps in the text:** I won't write replacement wording. The gaps stay as questions for the Chief Operating Officer to answer.
- **Mark it approved for the board:** I won't. The status stays "draft for the management board", and approval goes through your normal route.

Three questions before I compare:

1. **Is the company a payment institution exempted under Article 32(1) of PSD2?** If it is, DORA Article 16(1) says Articles 5 to 15 don't apply to it and the simplified framework in Article 16 applies instead. Your answer decides which DORA articles I compare against.
2. **Which parts should I compare?**
   - For DORA, I'd use Articles 5, 6, 11, 12, 13, 24 and 25 (plus Article 16 if question 1 is yes).
   - I can also include Delegated Regulation (EU) 2024/1774 (the detailed rules on ICT risk management), which ships with this skill.
   - For SP 800-34 Rev. 1, I only have the Executive Summary and Chapters 1 to 5. I'd use 3.1 (policy statement), 3.2 (BIA), 3.5 (testing) and 3.6 (plan maintenance).

   Add, remove or confirm.
3. **Is this document meant to be the ICT business continuity policy that DORA Article 11(1) requires,** or does another document hold that, such as an ICT risk management framework?

If you skip a question, I'll state my assumption under Gaps.

**Tool calls (stream-json):**

- Glob: `**/*`
- Glob: `**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/README.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/govern.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/check-against-standards/2/run2/work/bc-policy-draft.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/keep-it-running.md`
- Grep: `^#|Article 16|exempted pursuant|Retrieved|retriev|Source|Date|date`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`

## Turn 3

**Request:** skip

**Reply (verbatim):**

# Draft review: business continuity policy against DORA and NIST SP 800-34

I haven't confirmed DORA compliance, written replacement text or marked the policy approved. Its status stays "draft for the management board". Every finding below is a question for the policy owner. Nothing was written to disk.

**Sources**
- Policy: "Business continuity policy", version 0.4, 3 September 2026, status "draft for the management board", owner "Chief Operating Officer". It is a draft, so it also appears under Gaps.
- DORA, Regulation (EU) 2022/2554: Official Journal L 333, 27 December 2022, as adopted; conversion retrieved 2026-09-10 (`literature/eur-lex/dora-regulation-2022-2554.md`). EUR-Lex is authoritative.
- NIST SP 800-34 Rev. 1: May 2010; Executive Summary and Chapters 1 to 5 only; conversion retrieved 2026-09-10 (`literature/nist/sp-800-34r1-contingency-planning-body.md`). The PDF is authoritative.

⚖ = for legal or compliance review

---

## DORA, Regulation (EU) 2022/2554

**Contradictions**

**D1. Testing frequency and method ⚖**
- Policy §5: "Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through."
- Art. 11(6)(a): "test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions"
- Art. 11(6), second subparagraph: "shall include in the testing plans scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities"
- Art. 24(6): "at least yearly, that appropriate tests are conducted on all ICT systems and applications supporting critical or important functions"

Question: how does a two-yearly desktop walk-through relate to these yearly and switchover requirements?

**D2. Review cycle ⚖**
- Policy §7: "The policy owner reviews this policy every three years."
- Art. 11(6), last subparagraph: "regularly review their ICT business continuity policy … taking into account the results of tests … and recommendations stemming from audit checks or supervisory reviews"
- Art. 6(5): the ICT risk management framework is "reviewed at least once a year … as well as upon the occurrence of major ICT-related incidents"

Question: does a fixed three-year cycle with no event triggers fit these articles?

**D3. Recovery objectives per system, set by IT ⚖**
- Policy §6: "The IT manager sets the recovery time objectives for all systems."
- Art. 12(6): "In determining the recovery time and recovery point objectives for each function, financial entities shall take into account whether it is a critical or important function"

Questions: are objectives set per function or per system? Where are recovery point objectives (RPO) set?

**Gaps (DORA passages with no counterpart in the policy)**

- **D4. Management body ⚖.** Art. 5(2)(e) says the management body shall "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy". §3 gives the management body no role. Who approves the policy and oversees it?
- **D5. Critical or important functions ⚖.** Art. 11(2)(a) requires arrangements to "ensure the continuity of the financial entity's critical or important functions" (defined in Art. 3(22)). The policy doesn't use the term or say which functions qualify. Which functions are critical or important?
- **D6. BIA content ⚖.** Art. 11(5) says the BIA "shall consider the criticality of identified and mapped business functions, support processes, third-party dependencies and information assets, and their interdependencies". It also requires assessment "by means of quantitative and qualitative criteria, using internal and external data and scenario analysis". §4 covers "each payment service and the customer support desk" only. Are third-party dependencies, information assets and interdependencies in scope of the BIA?
- **D7. Incident response, containment, impact estimate, communication and reporting ⚖.** Art. 11(2)(b) to (e) require these, including "report to the competent authorities in accordance with Article 19". There is no counterpart. Where are these set out?
- **D8. Independent audit of response and recovery plans ⚖.** Art. 11(3) says these plans "shall be subject to independent internal audit reviews" for entities other than microenterprises. At 140 staff, the company is above the Art. 3(60) threshold of "fewer than 10 persons". Is an audit review intended?
- **D9. ICT third-party providers ⚖.** Art. 11(4) refers to plans "notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers". The policy is silent on suppliers. Are outsourced functions covered?
- **D10. Crisis management and communication ⚖.** Art. 11(6)(b) requires testing "the crisis communication plans". Art. 11(7) requires "a crisis management function". Art. 14(3) requires "at least one person" for incident communication. None of these appears in the policy. Who holds them?
- **D11. Records during disruption ⚖.** Art. 11(8) requires "readily accessible records of activities before and during disruption events". The policy has no counterpart. Where is this set?
- **D12. Backup, restoration and redundancy ⚖.** Art. 12(1) requires "backup policies and procedures", Art. 12(4) "redundant ICT capacities" and Art. 12(7) "checks and reconciliations" to protect data integrity. None of these appears in the policy. Does another document cover them?
- **D13. Learning ⚖.** Art. 13(2) requires "post ICT-related incident reviews" and Art. 13(6) requires "digital operational resilience training as compulsory modules". There is no counterpart. Where are these?
- **D14. Test independence and remediation ⚖.** Art. 24(4) says "tests are undertaken by independent parties". Art. 24(5) requires procedures "to prioritise, classify and remedy all issues revealed". Neither appears in §5. Who runs the tests, and how are findings remedied?

---

## NIST SP 800-34 Rev. 1 (Chapters 1 to 5)

This is guidance written for US federal information systems. Whether it applies to the company is a question for the owner.

**Contradictions**

- **N1. Who sets recovery times.** §3.2.1 says the ISCP Coordinator, "with the process owners, leadership and business managers determine the acceptable downtime". Policy §6 says "The IT manager sets the recovery time objectives". Which reading does the owner intend?
- **N2. Exercise depth.** §3.5.4 says "For moderate-impact systems, a functional exercise … should include an element of system recovery from backup media". It also says "For low-impact systems, a tabletop exercise … is sufficient". Policy §5 says "by a desktop walk-through" for all plans. What impact level do the payment systems carry?
- **N3. Fixed BIA cycle.** §3.6 says "When a significant change occurs, the BIA should be updated". Policy §4 says "every three years" with no change trigger. Should change trigger a BIA update?

**Gaps (§3.1 "Key policy elements" with no counterpart)**

- **N4.** "Resource requirements"
- **N5.** "Training requirements". §3.5.2 also says "Training should be provided at least annually".
- **N6.** "Plan maintenance schedule". §7 covers review of the policy, not maintenance of the plans.
- **N7.** "Minimum frequency of backups and storage of backup media"
- **N8.** Recovery point objective (RPO), §3.2.1. The policy has no counterpart.
- **N9.** "Identify resource requirements" and "recovery priorities", §3.2.2 and §3.2.3. The policy has no counterpart.

---

## Challenge: clauses that are ambiguous, unenforceable or open to two readings

1. **§2:** "The ICT systems that support them are in scope". Which systems? Does this include systems a third party runs?
2. **§2:** "the marketing website is not". Does it support any payment or customer function, for example service status notices?
3. **§3:** "runs the programme day to day". Which programme, and with what authority?
4. **§4:** "every three years". Counted from when, and what happens between cycles?
5. **§5:** "are tested every two years". Is that each plan, or all plans together? Who records the result, and what counts as a pass?
6. **§6:** "for all systems". On what basis, approved by whom, and how do the objectives link to the BIA?
7. **§7:** "reviews". Does a review include re-approval, and by whom?
8. **Header:** owner and version are given but there is no review date. Is one intended?

---

## Gaps

- **Your answers to my three questions.** You skipped all three, so I assumed the following:
  - The company is not an exempted payment institution, so I compared DORA Articles 5 to 15. I did not compare Art. 16.
  - The parts compared are the ones I proposed.
  - This document is meant as the Art. 11(1) ICT business continuity policy.

  If any of these assumptions is wrong, the DORA block changes.
- **The policy is a draft** (v0.4, "draft for the management board"). It is still the document reviewed. It has no review date in its document control.
- **Not reviewed (frameworks not selected):**
  - Delegated Regulation (EU) 2024/1774. It ships with this skill and may contain more detailed rules for the parts of Art. 11 that Art. 15(d) and (f) refer to.
  - DORA Articles 17 to 23 and 26 to 44, apart from where quoted above.
  - The AI Act, CSF 2.0, the Swiss FONES ICT minimum standard, the UK Cabinet Office guidance, the ESAs' statement, and any other standard.
- **Source limits:**
  - The DORA file is the text "as adopted". Later amendments are not in the sources.
  - The SP 800-34 file leaves out the appendices.
  - Whether SP 800-34 Rev. 1 (May 2010) is still current is not in the sources.
  - Your competent authority's expectations are not in the sources.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> [policy owner] answers these, [legal or compliance] the marked points.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Grep: `'microenterprise'|'critical or important function'|'management body'`
- Grep: `^#+ |^3\.\d|^[0-9]\.[0-9]+ [A-Z]`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
