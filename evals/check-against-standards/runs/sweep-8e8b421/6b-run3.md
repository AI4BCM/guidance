# /check-against-standards case 6b, run3: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `6b765da6-6036-4a37-83e3-1b32d5a8c395`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you review our draft business continuity policy against DORA and tell us what is missing? The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I reviewed the draft against DORA, Regulation (EU) 2022/2554. The draft is a short, general business continuity outline. Three of its seven sections set rules that conflict with explicit DORA requirements, and several required elements are missing altogether.

**Check first:** a payment institution is in scope under Art. 2(1)(b). Only payment institutions exempted under PSD2 can use the simplified regime in Art. 16. At 140 staff you are very likely a fully authorised payment institution, so the full Art. 5–15 requirements apply. Everything below assumes that.

## A. Sections that conflict with DORA

| Draft says | DORA requires | Reference |
|---|---|---|
| §5: plans tested **every two years**, **desktop walk-through only** | ICT business continuity plans and ICT response and recovery plans tested **at least yearly**, and after substantive changes. Systems supporting critical or important functions also need yearly tests. Tests should include severe but plausible scenarios: cyber-attacks, switching to redundant capacity, restoring backups, and a third-party provider failing. A walk-through alone will not do. | Art. 11(6), Art. 24(6), Art. 25(1); RTS 2024/1774 |
| §7: policy reviewed **every three years** | The ICT risk management framework, which includes this policy, is reviewed **at least once a year**. It is also reviewed after major ICT incidents, supervisory instructions, and test or audit findings. | Art. 6(5), Art. 11(1) |
| §4: business impact analysis (BIA) **every three years**, covering only services and the support desk | The BIA must cover exposure to severe disruptions. It uses quantitative and qualitative criteria and scenarios. It covers critical or important functions, supporting processes, **third-party dependencies, information assets and how they depend on each other**. It needs refreshing at least as often as the yearly framework review, and after major changes. | Art. 11(5), Art. 8 |
| §6: **IT manager alone** sets recovery time objectives (RTOs) | Each function needs both an RTO and a **recovery point objective (RPO)**, which the draft never mentions. They must reflect whether the function is critical or important and the wider impact, and must keep agreed service levels in extreme scenarios. They should come from the BIA and be set by the business. | Art. 12 |
| §3/§7: **COO owns and approves** | The **management body** defines, approves and oversees the ICT business continuity policy and the ICT response and recovery plans, and remains responsible for them. The COO can be the operational owner, but the policy must say the board approves it. | Art. 5(2)(e) |

## B. Required elements that are missing

1. **ICT business continuity content.** Art. 11(1) requires a comprehensive ICT business continuity policy, and Art. 11(2) lists what it must do: keep critical or important functions running; respond to and contain ICT incidents; activate the dedicated plans without delay; make an early estimate of impact, damage and losses; and set out communication and crisis management. The draft names "ICT recovery plans" but says nothing about any of this.
2. **Identifying critical or important functions.** Scope is set by a list of services, not by identifying and mapping critical or important functions and the ICT assets behind them. Art. 8 requires that mapping and an inventory of those assets.
3. **Backups, restoration and redundancy (Art. 12).** These are not mentioned at all. The policy needs a backup policy covering scope and frequency, restoration procedures, backups kept on systems separated from the source, redundant ICT capacity, integrity checks when recovering, and periodic tests of backup restores.
4. **Crisis management function (Art. 11(7)).** When it is activated, who leads it, and how decisions are escalated.
5. **Crisis communication (Art. 14).** Communication plans for staff, clients, counterparties, the public and authorities, and at least one named person responsible for communication about ICT incidents. Art. 11(6) also requires these plans to be tested.
6. **ICT third-party providers (Art. 28).** Nothing on what you depend on from them. That is a large gap for a card processing platform, which is often partly outsourced. The policy needs third-party failure scenarios, links to exit strategies (Art. 28(8)), and confirmation that providers' own continuity arrangements are tested.
7. **Link to incident management and reporting (Art. 17–19).** Plans should be triggered by ICT incident classification. Major ICT incidents must be reported to the competent authority.
8. **Records and costs.** Keep readily accessible records of activity before and during a disruption (Art. 11(8)). Be able to report estimated costs and losses of major ICT incidents to the competent authority on request (Art. 11(10)).
9. **Learning from incidents and tests (Art. 13).** Reviews after incidents and tests, with lessons fed back into the plans and the BIA.
10. **Independent oversight.** Internal audit must regularly review the framework, and the ICT response and recovery plans must be subject to independent internal audit (Art. 6(6), Art. 11(4)). The policy should also name an independent ICT risk control function (Art. 6(4)). §3 has neither.
11. **Management body training (Art. 5(4))** and the ICT continuity awareness and training programme for staff (Art. 13(6)).

## C. Smaller points
- **Marketing website out of scope.** That is fine if the BIA supports it. But if the site is a channel for telling customers about an outage, it falls within crisis communication.
- **Make the policy communicable.** The detailed technical standard (RTS, Delegated Regulation 2024/1774, Articles 24–26) expects the policy to be documented, communicated internally and given resources. It should set out these elements in more detail than DORA does.
- **Threat-led penetration testing (Art. 26)** applies only if your competent authority designates you. Probably not relevant, but worth stating in the policy.

**Suggested priority:** fix the testing, review and BIA intervals, add board approval and RPOs, then add the Art. 11/12/14 content. Those are the gaps a supervisor would raise first.

I wrote this from my knowledge of the regulation, not from the official texts, so check the article and paragraph numbers against the published regulation and RTS before this goes to the board. I can also turn this into a shareable gap-analysis page or redraft the policy to close these gaps.

**Tool calls (stream-json):**

- Bash: `ls -la; cat bc-policy-draft.md`
