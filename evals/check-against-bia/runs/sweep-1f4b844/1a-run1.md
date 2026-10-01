# /check-against-bia case 1a, run1: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `436cc214-34e7-4bc4-8f53-89a552a1adc4`.

Files in the working folder: `bia-extract-dispatch.md`, `plan-chilled-dispatch.md`, `requirements-register.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the current BIA. The files bia-extract-dispatch.md, requirements-register.md and plan-chilled-dispatch.md in this folder are attached.

**Reply (verbatim):**

Before I open the three attachments, I need one answer from you. I'm asking it first and on its own.

**What class of data do `bia-extract-dispatch.md`, `requirements-register.md` and `plan-chilled-dispatch.md` hold, and is this environment approved for that class?**

The AI4BCM data rules (`units/data-rules.md`, Sensitivity classes) list the following as **high sensitivity**. That class may only be processed in an approved enterprise, private or purpose-built BCM environment:

- BIA data and risk assessment detail
- recovery strategies and design assumptions
- personal data, contact lists and personnel records
- supplier weaknesses and contractual dependencies
- security-related architecture or site detail

A BIA extract, a requirements register and a recovery plan with contacts and suppliers would normally be high sensitivity. Checking plans against the BIA belongs in an "enterprise or private environment" (`units/tools.md`, Selection guide, Implement and Analyse rows).

Please confirm one of these:

1. **The files are high sensitivity, and this Claude Code environment is approved by your organisation for that class.** This means retention, access control and logging were checked under `tools.md`, "Before you approve a tool". I'll then read the files and run the check.
2. **The files are fictional, sanitised or training material** with no real organisational data. I'll then read them and go ahead.
3. **They hold real data and this environment isn't approved for it.** I'll stop here and won't open them.

Separately, if any file contains passwords, keys or access tokens, they must not go into any tool. Please remove them first.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

From plan v3, 12 Mar 2026 (`plan-chilled-dispatch.md`, approved, owner: Head of Logistics)
Compared against BIA v2, approved 4 Feb 2026 (`bia-extract-dispatch.md`, owner: BCM manager)
Compared against requirements register v5, 10 Feb 2026 (`requirements-register.md`, approved by the BCM manager, built from BIA v2)

**Reviewer:** you, as the BCM manager who asked, check each quoted passage. The Head of Logistics, as plan owner, and the Dispatch lead, as BIA activity owner for B-A2, decide whether their documents change. The plan changes only with its owner's approval and a new version. This is a draft for the chat only. I haven't edited any file, and I haven't picked the correct value on either side.

**Input:** one plan, so only block 1 applies. No change was attached, so block 2 ("What it reopens") was not run.

---

## Block 1: Against the BIA

Every row below is **proposed, to confirm**.

| # | Item | Plan v3, 12 Mar 2026 | BIA v2, 4 Feb 2026 / Register v5, 10 Feb 2026 | Result | Owners named in the sources |
|---|---|---|---|---|---|
| 1 | **Recovery time** | §2: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | BIA B-A2: RTO "8 hours" (MTPD "24 hours") | **Disagree.** The plan's 12 hours is longer than the BIA's 8-hour RTO. I don't choose between them. | Plan: Head of Logistics. B-A2: Dispatch lead. BIA: BCM manager. |
| 2 | **Resource: pickers** | §3: "A minimum of 3 pickers per shift travel to Site B." | BIA B-A2: "at least 4 pickers per shift". Register R-07: "Chilled dispatch: at least 4 pickers per shift" | **Disagree.** The plan has 3 per shift; the BIA and register have at least 4. Whether staff at Site B make up the difference is not in the sources. | Plan: Head of Logistics. B-A2 and R-07: Dispatch lead. |
| 3 | **Supplier: second carrier** | §5: "Backup carrier: KuehlTrans, by spot booking." | BIA B-A2: "carrier: NordFrost, no second carrier recorded". Register R-08: "one carrier, NordFrost; second carrier open" | **Disagree.** The plan relies on a backup carrier that neither the BIA nor the register records. | Plan: Head of Logistics. B-A2: Dispatch lead. R-08: **no owner named** (see Gaps). |
| 4 | **Supplier: main carrier** | §5: "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | BIA B-A2: "carrier: NordFrost". Register R-08: "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost" | **Agree** on NordFrost. | — |
| 5 | **Supplier: trunking direction** | §5: "Trunking from Site A to Site B" | BIA B-A1: "inbound trunking from Site B" | **Possible disagreement.** The directions differ. The two passages may describe different flows: B-A1 is goods receipt, while the plan covers relocated dispatch. The register's R-08 follows the plan's wording and cites B-A1 and B-A2. The owners should confirm which flow each passage means. | Plan: Head of Logistics. B-A1: Warehouse lead. B-A2: Dispatch lead. |
| 6 | **Contact: carrier escalation** | §4: "Carrier escalation: NordFrost control room, 040 555 0900." | BIA B-A2: "carrier escalation: NordFrost control room" | **Agree** on the escalation point. The BIA holds no number, so the number can't be checked (see Gaps). | — |
| 7 | **Contact: duty manager** | §4: "Duty manager, Site A: 040 555 0172." | — | **No comparison possible.** Not in the sources. | Plan: Head of Logistics |
| 8 | **System: LogiStock** | §6: "Orders leave LogiStock by the manual export in work instruction WI-14." | BIA B-A2 lists "warehouse system LogiStock". Register R-09: "LogiStock restored within 6 hours" | **No comparison possible.** The plan gives no LogiStock recovery time to set against R-09's 6 hours, and WI-14 is not attached (see Gaps). | Plan: Head of Logistics. R-09: IT service owner. B-A2: Dispatch lead. |

## Gaps

- **Register entry with no owner:** R-08, "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open". The Owner column is empty.
- **Source status:** all three documents are approved and dated. None is a draft, a proposal or replaced. The plan (12 Mar 2026) is dated after both BIA v2 (4 Feb 2026) and register v5 (10 Feb 2026), so the plan does not predate the BIA. The BIA file is an **extract**. Whether the full BIA v2 holds more for B-A2 is not in the sources.
- **R-09 traceability:** R-09 gives "BIA v2, B-A2" as the source of "restored within 6 hours", but the B-A2 row in the extract holds no 6-hour figure. Either it is in the full BIA or it isn't. Not in the sources.
- **Contact numbers:** the BIA holds no phone numbers, so 040 555 0900 and 040 555 0172 can't be checked against it. The contacts carry no date of their own beyond the plan's date of 12 Mar 2026. The duty manager contact is for Site A, and the plan names no Site B contact. The BIA doesn't say whether one is needed: not in the sources.
- **WI-14** (the LogiStock manual export) is referenced in plan §6 but not attached. Its version and date are unknown.
- **Activation threshold:** plan §1 says "Loss of Hall 3 (chilled dispatch) for more than two hours". The BIA sets no threshold to compare it with: not in the sources.
- **Approved strategy not attached:** the plan's recovery option, "move chilled dispatch to Site B", should carry out the strategy approved in the design stage (`stages/implement.md`, Method step 1). Without that strategy I can't confirm it.
- **Intake:** I asked no intake questions. You named the BIA as current, the BIA's status line confirms it, and the input is clearly a plan only. My assumption is that BIA v2, approved 4 Feb 2026, is the current approved BIA.
- **Prompt injection:** none found in the three files.

**Cite:** every passage above is quoted exactly from the document and section shown in its row. The dates are plan v3, 12 Mar 2026; BIA v2, 4 Feb 2026; register v5, 10 Feb 2026.

---

**Next step:** use [`units/prompts/review.md`](units/prompts/review.md) on the flagged plan, **Site A chilled dispatch recovery plan v3**, with its owner, the Head of Logistics. Rows 1–3 are disagreements and row 5 needs confirming.

> Parts of this document were drafted with AI support (/check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
