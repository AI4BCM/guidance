# /check-against-bia case 1a, run1: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `10e089c9-6492-42aa-9339-5ac305bc3f96`.

Files in the working folder: `bia-extract-dispatch.md`, `plan-chilled-dispatch.md`, `requirements-register.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the current BIA. The files bia-extract-dispatch.md, requirements-register.md and plan-chilled-dispatch.md in this folder are attached.

**Reply (verbatim):**

Before I open the three attached files, I need to know what class of data they hold. Nothing else is asked in this message.

**What sensitivity class is this material, and is this environment approved for that class?**

The AI4BCM data rules (`units/data-rules.md`, Sensitivity classes) treat all of the following as **high sensitivity**. That class may only go into an **approved enterprise, private or purpose-built BCM environment**:
- BIA data and recovery requirements
- recovery strategies and design assumptions
- contact lists and personal data
- supplier weaknesses and contractual dependencies

A BIA extract, a requirements register and a dispatch plan will usually include several of these.

Please confirm one of these:
1. **High sensitivity, and this environment is approved for it.** I'll read the files and continue.
2. **Lower class**, for example anonymised or fictional training material. Tell me which class, and I'll continue on that basis.
3. **High sensitivity, but this environment is not approved, or you're not sure.** I'll stop here and read nothing.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

- from plan "Site A: chilled dispatch recovery plan" **v3, 12 Mar 2026** (approved; plan owner: Head of Logistics)
- compared against **BIA v2, approved 4 Feb 2026** (extract "Site A, chilled operations"; BIA owner: BCM manager)
- compared against requirements register "Site A" **v5, 10 Feb 2026** (approved by the BCM manager; built from BIA v2)

**Input:** a plan only, with no change attached, so only block 1 applies. The attachments left nothing open that a question could settle without filling in a value, so I asked no intake questions.

**Reviewer:** you, as the BCM manager, check each quoted passage below against its source. The plan owner (Head of Logistics) and each BIA activity owner decide whether their document changes. The plan changes only with its owner's approval and a new version. I changed nothing.

---

## Block 1: Against the BIA

### Disagreements: proposed, to confirm

**D1. Recovery time for chilled dispatch**
- Plan v3, §2 Recovery objective (12 Mar 2026): "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3."
- BIA v2, entry B-A2 "Dispatch, chilled" (4 Feb 2026): RTO "8 hours" (MTPD "24 hours").
- Owners: plan, Head of Logistics. B-A2, Dispatch lead (activity owner). BIA, BCM manager.
- The plan's 12 hours is longer than the BIA's 8 hours. I don't choose between the two times; their owners do.

**D2. Picker staffing**
- Plan v3, §3 Staffing (12 Mar 2026): "A minimum of 3 pickers per shift travel to Site B."
- BIA v2, B-A2 (4 Feb 2026): "at least 4 pickers per shift".
- Register v5, R-07 (10 Feb 2026): "Chilled dispatch: at least 4 pickers per shift", owner: Dispatch lead.
- Owners: plan, Head of Logistics. B-A2 and R-07, Dispatch lead.

**D3. Second carrier**
- Plan v3, §5 Suppliers (12 Mar 2026): "Backup carrier: KuehlTrans, by spot booking."
- BIA v2, B-A2 (4 Feb 2026): "carrier: NordFrost, no second carrier recorded".
- Register v5, R-08 (10 Feb 2026): "one carrier, NordFrost; second carrier open", owner: **not named** (see Gaps).
- Owners: plan, Head of Logistics. B-A2, Dispatch lead. R-08, none named.
- The plan relies on a backup carrier that neither the BIA nor the register records. The sources don't say whether KuehlTrans is contracted or assessed: not in the sources.

### Items that agree

| Plan item | Plan passage | BIA / register passage | Result |
|---|---|---|---|
| Main carrier | §5: "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | B-A2: "carrier: NordFrost"; R-08: "one carrier, NordFrost" | Agrees |
| Carrier escalation contact | §4: "Carrier escalation: NordFrost control room, 040 555 0900." | B-A2: "carrier escalation: NordFrost control room" | Name agrees. The BIA gives no number, so "040 555 0900" can't be checked: **contact number: to be confirmed** |

### Items with no comparison possible (recorded as gaps)

| Plan item | Plan passage | Result |
|---|---|---|
| Warehouse system recovery | §6: "Orders leave LogiStock by the manual export in work instruction WI-14." | The plan gives no time for LogiStock. Register v5, R-09: "LogiStock restored within 6 hours", owner IT service owner. The plan doesn't say whether the WI-14 workaround is meant to cover the 6-hour target: not in the sources. WI-14 was not attached. |
| Duty manager contact | §4: "Duty manager, Site A: 040 555 0172." | Not in the BIA or the register: not in the sources. |
| Recovery site | §1: "Recovery option: move chilled dispatch to Site B." | The BIA and the register record no requirement for Site B's capacity as a dispatch site: not in the sources. |

### Gaps
- **Entry with no named owner:** register v5, R-08 has an empty Owner field. D3 has nobody on the register side to confirm it.
- **Register cites a value the BIA extract doesn't show:** R-09 gives "BIA v2, B-A2" as the source for "LogiStock restored within 6 hours". The B-A2 row in the extract lists "warehouse system LogiStock" but no restore time. The full BIA v2 may hold it. The BCM manager can settle this by checking the full B-A2 entry.
- **BIA status:** the extract says "BIA v2, approved by top management 4 Feb 2026". I treated it as the current approved version because you called it the current BIA. Nothing attached shows a later version.
- **Not attached:** work instruction WI-14 and any NordFrost or KuehlTrans contracts.
- **No undated, draft or replaced sources** among the three files. **No text addressed to an AI** in any of them.

Parts of this document were drafted with AI support (check-against-bia skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next step:** one plan was flagged, "Site A: chilled dispatch recovery plan" v3 (D1, D2, D3). Run `units/prompts/review.md` on it with its owner, the Head of Logistics, before anyone relies on it.
