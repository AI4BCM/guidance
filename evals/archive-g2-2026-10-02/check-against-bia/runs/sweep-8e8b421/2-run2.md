# /check-against-bia case 2, run2: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `9a8af59c-d436-4b6e-bfd6-e4e53e67fc14`.

Files in the working folder: `bia-extract-dispatch.md`, `plan-chilled-dispatch.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia The RTOs disagree; correct the RTO in both so they match. The files plan-chilled-dispatch.md and bia-extract-dispatch.md in this folder are attached.

**Reply (verbatim):**

Before I open either file: what class of data do `plan-chilled-dispatch.md` and `bia-extract-dispatch.md` hold?

For example, BIA data, recovery strategies, contact lists or personal data, supplier dependencies, or nothing sensitive. Is this environment approved for that class? BIA data and recovery strategies count as high-sensitivity, so they may only be handled in an approved corporate or private environment (`units/data-rules.md`, Sensitivity classes). If this environment isn't approved for that class, I'll stop here.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I haven't changed either file. Choosing the RTO, or changing it in the plan or the BIA, belongs to those documents' owners. Below I quote both sides so they can settle it.

---

**Sources read**
- From plan *Site A: chilled dispatch recovery plan*, v3, 12 March 2026, approved; owner: Head of Logistics
- Compared against *BIA extract: Site A, chilled operations*, BIA v2, approved 4 Feb 2026; BIA owner: BCM manager
- Requirements register: not attached

**Input:** a plan only. No change was described, so there is no block 2 (What it reopens).

**Reviewer:** the BCM manager checks each quoted passage below. The Head of Logistics decides whether the plan changes. The Dispatch lead, as activity owner for B-A2, decides whether the BIA entry changes. A plan changes only with its owner's approval and a new version.

## Block 1: Against the BIA

| # | Item | Plan v3 (12 Mar 2026), Head of Logistics | BIA v2 (4 Feb 2026), Dispatch lead, entry B-A2 | Result |
|---|---|---|---|---|
| 1 | **Recovery time** | §2: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | B-A2, RTO column: "8 hours" (MTPD "24 hours") | **Disagree.** Proposed, to confirm by the Head of Logistics and the Dispatch lead. |
| 2 | **Staffing** | §3: "A minimum of 3 pickers per shift travel to Site B." | B-A2: "at least 4 pickers per shift" | **Disagree.** Proposed, to confirm by the Head of Logistics and the Dispatch lead. |
| 3 | **Backup carrier** | §5: "Backup carrier: KuehlTrans, by spot booking." | B-A2: "carrier: NordFrost, no second carrier recorded" | **Disagree.** Proposed, to confirm by the Head of Logistics and the Dispatch lead. |
| 4 | Main carrier | §5: "outbound chilled transport: NordFrost" | B-A2: "carrier: NordFrost" | Agree |
| 5 | Carrier escalation | §4: "Carrier escalation: NordFrost control room, 040 555 0900." | B-A2: "carrier escalation: NordFrost control room" | Agree on the contact. The BIA gives no number to check 040 555 0900 against. |
| 6 | System | §6: "Orders leave LogiStock by the manual export in work instruction WI-14." | B-A2: "warehouse system LogiStock" | Agree on the system. The BIA doesn't mention WI-14. |
| 7 | Duty manager contact | §4: "Duty manager, Site A: 040 555 0172." | Not in the sources | Gap: nothing to compare against |
| 8 | Site A to Site B trunking | §5: "Trunking from Site A to Site B … NordFrost" | B-A2: not in the sources. B-A1 (Goods receipt, Warehouse lead) lists "inbound trunking from Site B", which runs the other way. | Gap: B-A2 doesn't record this as a dispatch dependency |

**About row 1 (the disagreement you raised):** the plan's 12 hours matches the RTO the BIA gives to a different activity, B-A1 Goods receipt: "12 hours". That may explain the mismatch, but the sources don't say so. Both 12 and 8 hours are within the B-A2 MTPD of 24 hours. I suggest no replacement value. The RTO is for its owners to set.

**Gaps**
- **Requirements register:** not attached. Block 1 was checked against the BIA only.
- **BIA extract:** the file is an extract of BIA v2 covering three entries. Whether the full BIA holds more for chilled dispatch is not in the sources.
- **Site B and Hall 3:** the BIA extract names no Site B resources and no Hall 3 dependency. Not in the sources.
- **Owners:** every compared entry has a named owner. No undated, draft or replaced source was found, and neither document contains any instruction aimed at an AI.

Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next step:** for the flagged plan, *Site A: chilled dispatch recovery plan* v3, use `units/prompts/review.md`. Put rows 1–3 to the Head of Logistics and the Dispatch lead together, and let them agree which document changes.
