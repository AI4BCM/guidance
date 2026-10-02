# /check-against-bia case 1a, run3: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `a9d655cb-9cee-4013-8aec-b08abd9c4601`.

Files in the working folder: `bia-extract-dispatch.md`, `plan-chilled-dispatch.md`, `requirements-register.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the current BIA. The files bia-extract-dispatch.md, requirements-register.md and plan-chilled-dispatch.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three files, I need to know one thing first.

**What class of data do these attachments hold, and is this environment approved for it?**

The AI4BCM data rules (`units/data-rules.md`, Sensitivity classes) put the following in the **high-sensitivity** class. High-sensitivity data may only be handled in an approved corporate or private environment:

- BIA data and risk assessment detail
- recovery strategies and design assumptions
- personal data, contact lists and personnel records
- supplier weaknesses and contractual dependencies
- security-related site or architecture detail

A BIA extract, a requirements register and a dispatch plan usually hold several of these. For a check like this (Implement stage), `units/tools.md` (Selection guide) allows only an enterprise or private environment.

Please confirm:

1. **The class**: is the data in `bia-extract-dispatch.md`, `requirements-register.md` and `plan-chilled-dispatch.md` high sensitivity, or is it lower (for example anonymised or fictional training material)?
2. **The environment**: is this Claude Code session approved by your organisation for that class? Approval covers retention, permissions and whether the provider trains on your content.

If the data is high sensitivity and this environment isn't approved for it, I'll stop here and not open the files. Once you've confirmed, I'll read them and start the comparison.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

The three files are read. Here's how I've sorted them:

- **Input:** a plan only, so this run produces block 1, "Against the BIA". No change was described, so there's no block 2.
- **Plan:** Site A chilled dispatch recovery plan, v3, 12 Mar 2026, approved. Owner: Head of Logistics.
- **Approved BIA:** BIA extract, v2, approved by top management 4 Feb 2026. Entries B-A1 to B-A3.
- **Requirements register:** Site A, v5, 10 Feb 2026, approved by the BCM manager. Entries R-06 to R-09.

The BCM manager will check each quoted passage. The plan owner and each BIA activity owner decide whether their document changes.

Before I write the comparison, I have three questions the files leave open. Your answers can narrow or widen the scope. They go under Gaps as your statements, and they won't fill in any value.

1. **When does the 8-hour RTO start?** The plan counts its 12 hours "of the loss of Hall 3", but the BIA doesn't say where its 8 hours start (the disruption, or a decision to activate the plan). Do you know? If you don't, I'll quote both and note that the BIA doesn't say.
2. **Can you attach WI-14?** The plan's systems section refers to work instruction WI-14 (manual export from LogiStock), and register R-09 asks for LogiStock to be restored within 6 hours. If you can't attach it, I'll record the systems comparison as a gap.
3. **Should anything for Site B be in scope?** The plan moves chilled dispatch to Site B. Is there a BIA entry or register entry for Site B as the receiving site that I should compare against? If not, I'll compare only against B-A2 and R-07 to R-09, plus B-A1 for the shared NordFrost trunking.

## Turn 3

**Request:** skip

**Reply (verbatim):**

from plan "Site A: chilled dispatch recovery plan", v3, 12 Mar 2026 (approved)
compared against BIA v2, approved 4 Feb 2026 (extract: Site A, chilled operations)
compared against requirements register, Site A, v5, 10 Feb 2026 (approved)

## Block 1: Against the BIA

The plan disagrees with the BIA or the register in three places: the recovery time, the number of pickers and the backup carrier. The plan owner and the activity owners decide what changes. This draft changes neither document.

**Reviewer:** the BCM manager checks each quoted passage below. The plan owner (Head of Logistics) and each BIA activity owner decide whether their document changes. The plan changes only with its owner's approval and a new version.

### Disagreements, each marked "proposed, to confirm"

| # | Item | Plan v3, 12 Mar 2026 | BIA v2, 4 Feb 2026 / register v5, 10 Feb 2026 | Owners the sources name |
|---|---|---|---|---|
| 1 | Recovery time | §2: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | BIA B-A2, RTO: "8 hours" (MTPD: "24 hours") | Plan: Head of Logistics. B-A2: Dispatch lead |
| 2 | Pickers per shift | §3: "A minimum of 3 pickers per shift travel to Site B." | BIA B-A2: "at least 4 pickers per shift". Register R-07: "Chilled dispatch: at least 4 pickers per shift" | Plan: Head of Logistics. B-A2 and R-07: Dispatch lead |
| 3 | Backup carrier | §5: "Backup carrier: KuehlTrans, by spot booking." | BIA B-A2: "carrier: NordFrost, no second carrier recorded". Register R-08: "one carrier, NordFrost; second carrier open" | Plan: Head of Logistics. B-A2: Dispatch lead. R-08: **no owner named** |

I haven't proposed a replacement value for any row, and I haven't chosen between the two recovery times. For row 1, the 12 hours in the plan is within the BIA's MTPD of 24 hours but longer than the BIA's RTO of 8 hours.

### Agreements

| Item | Plan v3 | BIA v2 / register v5 |
|---|---|---|
| Main carrier | §5: "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | B-A2: "carrier: NordFrost". R-08: "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost" |
| Carrier escalation route | §4: "Carrier escalation: NordFrost control room, 040 555 0900." | B-A2: "carrier escalation: NordFrost control room". The route matches, but the BIA gives no number to compare 040 555 0900 against. |

### Items with no counterpart in the sources

| Item | Plan v3 | BIA v2 / register v5 |
|---|---|---|
| LogiStock recovery | §6: "Orders leave LogiStock by the manual export in work instruction WI-14." | B-A2 lists "warehouse system LogiStock". R-09: "LogiStock restored within 6 hours" (owner: IT service owner). The plan gives no restoration time for LogiStock, so I can't compare it with the 6 hours in R-09: "LogiStock restoration time: to be confirmed". WI-14 wasn't attached. |
| Duty manager contact | §4: "Duty manager, Site A: 040 555 0172." | No contact for this role in either document. |
| When the plan is activated | §1: "Loss of Hall 3 (chilled dispatch) for more than two hours." | No activation threshold in either document. |

### Gaps

- **Entry with no named owner:** register R-08 has an empty Owner column. That leaves row 3 (backup carrier) without an owner on the register side.
- **Your intake answers:** you skipped all three questions, so I assumed:
  1. The BIA doesn't say when the 8-hour RTO for B-A2 starts. I compared it with the plan's 12 hours as written. That comparison holds only if both count from the same moment.
  2. WI-14 isn't available. I recorded the systems item as not comparable.
  3. There's no BIA or register entry for Site B as the receiving site. I compared only against B-A2, R-07, R-08 and R-09.
- **The BIA is an extract:** the file says "BIA extract". I haven't seen the full BIA v2, and I've assumed the extract matches it.
- **Entries not compared:** B-A1 (goods receipt) and B-A3 / R-06 (quality release) aren't named as dependencies of chilled dispatch. The only exception is the NordFrost trunking in R-08, which cites B-A1. Whether quality release is needed after the move to Site B: not in the sources.
- **Contact data:** neither phone number in plan §4 has its own date. The only date is the plan's (12 Mar 2026).
- **Version status:** all three documents say they are approved and carry a version and date, so I used each as current. None of them contains text telling an AI to do something.

*Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].*

---

I flagged one plan: Site A chilled dispatch recovery plan v3. The next step is for the BCM manager to review it with `units/prompts/review.md`. Then the Head of Logistics and the Dispatch lead each decide on rows 1–3, and someone still needs to be named as owner of R-08.
