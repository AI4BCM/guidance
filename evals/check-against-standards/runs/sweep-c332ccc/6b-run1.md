# /check-against-standards case 6b, run1: Claude Code, guidance at c332ccc

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `4ec1908d-4370-446c-943a-47dba3316ecf`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you review our draft business continuity policy against DORA and tell us what is missing? The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I compared your draft (v0.4, 36 lines) with DORA (Regulation (EU) 2022/2554) and its RTS on the ICT risk management framework (Delegated Regulation (EU) 2024/1774). The draft is a reasonable general outline, but it falls well short of DORA. Most of what DORA asks for is missing, and three of the six substantive sections set intervals or ownership that DORA doesn't allow.

## First, check which regime applies

Payment institutions that are *exempted* under PSD2 can use DORA's simplified framework (Art. 16), which asks much less. A fully authorised payment institution with 140 staff normally can't, so I've reviewed against the full regime (Arts. 5–14). The draft should state which regime applies.

## Where the draft breaks DORA's rules

| Draft section | What it says | What DORA requires |
|---|---|---|
| §5 Testing | Every **two years**, desktop walk-through only | At least **once a year**, and after any substantive change to ICT systems supporting critical or important functions. Tests must include **cyber-attack** scenarios and **switchovers** between primary and redundant infrastructure, backups and facilities (Art. 11(6); RTS Art. 25). A desktop walk-through alone can't show that a switchover works. |
| §7 Review | Every **three years** by the policy owner | The ICT risk management framework, which includes this policy, is reviewed **at least once a year**. It is also reviewed after major ICT incidents, supervisory instructions, or test and audit findings (Art. 6(5), Art. 11(6)). |
| §6 Recovery objectives | IT manager sets RTOs **per system** | Recovery time **and recovery point** objectives must be set **per function**. They must reflect whether the function is critical or important, and must hold in extreme scenarios (Art. 12(6)). They should come from the impact analysis and be approved by the business, not set by IT alone. |
| §3 Roles / approval | COO owns the policy; the board isn't mentioned in the text | The **management body** must approve the ICT business continuity policy and the response and recovery plans, review them regularly, and stays ultimately responsible (Art. 5(2)(e)). |
| §4 Impact analysis | Every three years; covers payment services and support desk only | It must cover exposure to severe disruptions using quantitative and qualitative criteria and scenario analysis. It must also consider business functions, supporting processes, **third-party dependencies, information assets and their interdependencies**, and ICT redundancy must follow from it (Art. 11(5)). DORA doesn't fix a frequency, but three years is hard to defend when the rest of the framework is reviewed every year. |

## What's missing entirely

1. **Critical or important functions.** Nearly every DORA obligation depends on this concept, and the draft never uses it. It should define them, or point to where they are identified and mapped under Art. 8.
2. **An identifiable ICT business continuity policy.** DORA wants a dedicated ICT policy that sits within the ICT risk management framework (Art. 11(1)). It can live inside a wider business continuity policy, but it has to be clearly visible as such.
3. **ICT response and recovery plans:**
   - A requirement to have them, kept separate from the business continuity plans.
   - An **independent internal audit review** of them (Art. 11(3)).
   - The scenarios they must cover (RTS Art. 26): cyber-attack, insider threat, power or telecoms failure, natural disaster or pandemic, data loss or corruption, loss of premises, and failure of a key ICT third-party provider.
4. **Activation and deactivation criteria and escalation.** The draft doesn't say when the plans are triggered, who decides, or how the event is contained and its first impacts and losses estimated (Art. 11(2); RTS Art. 24).
5. **A crisis management function** with clear procedures for internal and external crisis communications (Art. 11(7), Art. 14).
6. **A link to incident reporting.** The policy should connect to classifying major ICT incidents and reporting them to your national authority (Arts. 18–19).
7. **Backup, restoration and redundancy:**
   - Backup scope and minimum frequency, based on how critical and confidential the data is.
   - Restoring onto systems that are physically and logically separate from the source.
   - Regular testing of backups.
   - Redundant ICT capacity.
   - Integrity checks and reconciliations after recovery (Art. 12).
8. **ICT third-party providers.** The policy should cover business continuity plans for critical or important functions that are outsourced (Art. 11(4)). It should include providers in testing and link to exit strategies (Art. 28(8)). The draft only mentions "ICT systems".
9. **Records.** Records of what was done before and during each disruption must be readily accessible (Art. 11(8)).
10. **Costs and losses.** You must be able to give the authority, on request, an estimate of the total annual costs and losses from major ICT incidents (Art. 11(10)).
11. **Learning and evolving.** The policy should require post-incident reviews and use of test lessons, and feed them back into the plans. It should report test deficiencies to the management body and cover staff training (Art. 13; RTS Art. 25).
12. **Separation of duties.** The IT manager owns the recovery plans and sets the RTOs, and no one checks either. DORA expects independent oversight by an ICT risk control function and internal audit (Art. 6(4), Art. 6(6)).

## Smaller points

- **Scope (§2):** give a reason for leaving out the marketing website. Make sure it isn't used for customer communications during a crisis and doesn't support a critical function.
- **Purpose (§1):** state the objectives, the time period covered, and how ICT continuity relates to overall business continuity (RTS Art. 24).
- **Roles (§3):** name deputies for each role and confirm the programme has enough resources.

**How sure I am:** the DORA article references come from the Level 1 text and I'm confident in them. For the RTS I've cited whole articles, not individual points, because I'm less sure of the exact paragraph numbers. Please check the references against the Official Journal text, and against any guidance from your national authority, before this goes to the board.

I can also turn this into a shareable gap-analysis page, or a redlined v0.5 of the policy, if that would help.

**Tool calls (stream-json):**

- Bash: `ls -la; wc -l bc-policy-draft.md; cat bc-policy-draft.md`
