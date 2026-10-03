# check-against-standards baseline (no skill loaded), run1: Claude Code, guidance at 6d0d3fb

`claude -p --setting-sources project --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `ca18bb73-365b-45ac-a3d1-7f44b155b383`.

Files in the working folder: `bc-policy-draft.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I reviewed the draft (`bc-policy-draft.md`, v0.4) against **DORA (Regulation (EU) 2022/2554)**, which has applied to EU payment institutions since 17 January 2025, and its RTS on the ICT risk management framework (Delegated Regulation (EU) 2024/1774). The folder had no internal standard to check against, and the draft doesn't name a jurisdiction, so I assumed an EU-licensed institution. If you're UK-regulated, tell me and I'll check it against the FCA operational resilience rules (PS21/3) instead. Most of the gaps would be the same.

**My view: the draft shouldn't go to the board yet.** It falls short of DORA in several places.

## Must fix: these conflict with the regulation

| § | Draft says | Requirement | Fix |
|---|---|---|---|
| 5 | Plans tested **every two years** | DORA Art. 11(6)(a) requires testing **at least yearly**, and also after substantive changes to systems that support critical or important functions | Test annually and after material change |
| 5 | Testing is a **desktop walk-through** only | RTS 2024/1774 (testing article, Art. 25 in my reading) requires scenario-based tests, including cyber-attacks and switchover to redundant capacity, backups and facilities. Providers' plans must be included where relevant | Require real recovery and switchover tests. Walk-throughs can supplement them but not replace them |
| 7 | Policy reviewed **every three years** | DORA Art. 6(5) requires the framework, including this policy, to be reviewed **at least yearly** and after major ICT incidents or supervisory findings | Review annually and on those triggers |
| 3 / 7 | The COO owns the policy and the board isn't mentioned | DORA Art. 5(2)(e) says the **management body** approves, oversees and periodically reviews the business continuity policy and the response and recovery plans | Say the board approves it and receives test results and review outcomes |
| 6 | The IT manager sets RTOs for "all systems" | Recovery objectives should be set per **function**, come from the BIA, and reflect the risk tolerance the management body sets (Art. 6(8)) | Business owners propose RTOs and RPOs from the BIA, and the board approves them. RPOs are missing entirely |
| 4 | The BIA covers only payment services and the support desk | DORA Art. 11(5) requires the BIA to cover business functions, supporting processes, **third-party dependencies, information assets and their interdependencies** | Widen the scope and add a trigger to refresh it after material change. Every three years is too slow when testing is annual |

## Missing sections

- **Crisis communication** (Art. 14): internal, customers, regulator, media. Plans must be tested too (Art. 11(6)(b)).
- **ICT third-party providers** (Art. 28): the card processing platform is probably outsourced. You need provider continuity, plans that include providers, and exit strategies.
- **Backup and restoration** (Art. 12): backup policy, restoration testing and redundant capacity.
- **Policy contents** (Art. 11(2)): incident response and containment, preliminary impact estimation, and activation criteria for the plans.
- **Link to incident management and reporting** (Arts. 17–19), plus post-incident lessons learned (Art. 13).
- **Records** of activities before and during disruptions (Art. 11(8)).
- **Independent assurance**: internal audit review (Art. 6(6)) and a second-line control function with oversight (Art. 6(4)). At the moment the IT manager both owns the recovery plans and sets the targets, and nobody independent checks either.
- **Definitions**: "critical or important functions", RTO and RPO.

## Smaller points

- **Remove "(invented for this eval)" from the header** before the draft goes anywhere.
- §2: briefly justify excluding the website. For example, confirm it hosts no customer logins or service-status pages. Also say whether people, premises loss and data are in scope.
- §3: give the BCM officer a reporting line and authority to escalate. Name who declares a crisis and invokes the plans.

**Caveat:** I quoted the DORA article numbers from memory, and I'm least sure about the RTS article numbers. Have compliance or legal check the citations before the board sees them.

I can redraft the policy with these fixes, or turn this review into a one-page note for the board.

**Tool calls (stream-json):**

- Bash: `ls -la; cat bc-policy-draft.md`
