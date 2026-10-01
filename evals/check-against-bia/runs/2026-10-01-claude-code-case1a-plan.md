# check-against-bia case1a-plan: Claude Code 2.1.284, 2026-10-01

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed; later turns with `--resume`.

Files in the working folder: `bia-extract-dispatch.md`, `plan-chilled-dispatch.md`, `requirements-register.md`.


## Turn 1

**Request:** /check-against-bia check the dispatch plan against the current BIA. Attached: bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md

**Reply (verbatim):**

Before I open the three attachments, I need one answer from you.

**What class of data do these files hold, and is this environment approved for it?**

The three files are a BIA extract, a requirements register and a recovery plan. Under `units/data-rules.md` (Sensitivity classes), all three probably count as **high-sensitivity**. That class covers BIA data, recovery strategies and design assumptions, supplier dependencies, and contact lists, which a dispatch plan usually includes. `units/tools.md` (Selection guide) says high-sensitivity data may only be worked on in an enterprise, private or purpose-built BCM environment.

Please confirm one of these:
- **High, and this Claude Code session is an approved corporate or private environment for that class.** I'll go ahead.
- **High, but this environment isn't approved for it.** I'll stop here and won't read the files.
- **A lower class** (for example, sanitised or fictional test data). Tell me which, and I'll go ahead.

**Reviewer:** you, as the BCM manager who asked, check every quoted passage in the draft. The plan owner and each BIA activity owner decide whether their own document changes. A plan only changes with its owner's approval and a new version.

Once you confirm, I'll treat this as a plan check (block 1, "Against the BIA"). Nothing you've said describes a change, so there won't be a "What it reopens" block unless you tell me there's a change to check too. You'll get a draft in this chat, and I won't edit any file.


## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Thanks. That confirms the class is high and this environment is approved for it, so I've read the three attachments.

Before I write the comparison, I have up to three questions the files leave open. Your answers can narrow the scope, but none of them will be used to fill in a value. I'll list them under Gaps as your statements, not as sources.

1. **Is BIA v2 (approved 4 Feb 2026) still the current approved BIA?** Or is a later version approved or in draft? You asked to check against "the current BIA", and the extract only says v2.
2. **Is the extract the whole BIA entry for B-A2 (Dispatch, chilled)?** The requirements register's R-09 says "LogiStock restored within 6 hours" and cites "BIA v2, B-A2". The B-A2 row in the extract names LogiStock but gives no recovery time for it. I'd like to know whether the full BIA has text the extract leaves out.
3. **Is plan v3 (12 Mar 2026) the plan's current version, with no later draft?**

If you skip any of these, I'll assume, in order:
1. BIA v2 is current.
2. The extract is the complete B-A2 entry, so the register's 6-hour figure has no source in what you attached.
3. Plan v3 is current.

Each assumption will appear under Gaps.


## Turn 3

**Request:** I can't answer those: skip them all and go ahead on your assumptions.

**Reply (verbatim):**

Compared against **BIA v2**, approved by top management on 4 Feb 2026 (extract: Site A, chilled operations)
From **requirements register v5**, 10 February 2026, approved by the BCM manager, built from BIA v2
From **plan "Site A: chilled dispatch recovery plan" v3**, 12 March 2026, approved, owned by the Head of Logistics

## Block 1: Against the BIA

The plan disagrees with the BIA or the register in three places: the recovery time, the picker numbers and the backup carrier. It agrees on NordFrost and its escalation route. Most of its other values don't appear in the BIA at all.

Every row is **proposed, to confirm**. I quote both sides and don't choose either value.

### Disagreements

| # | Topic | Plan v3 (Head of Logistics) | BIA v2 / register v5 | Owners the sources name |
|---|---|---|---|---|
| 1 | **Recovery time** | §2, 12 Mar 2026: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | BIA v2, B-A2, 4 Feb 2026, RTO column: "8 hours" (same row, MTPD: "24 hours") | Plan: Head of Logistics. B-A2: Dispatch lead. BIA: BCM manager |
| 2 | **Staffing** | §3, 12 Mar 2026: "A minimum of 3 pickers per shift travel to Site B." | BIA v2, B-A2, 4 Feb 2026: "at least 4 pickers per shift". Register v5, R-07, 10 Feb 2026: "Chilled dispatch: at least 4 pickers per shift" | Plan: Head of Logistics. B-A2 and R-07: Dispatch lead |
| 3 | **Backup carrier** | §5, 12 Mar 2026: "Backup carrier: KuehlTrans, by spot booking." | BIA v2, B-A2, 4 Feb 2026: "carrier: NordFrost, no second carrier recorded". Register v5, R-08, 10 Feb 2026: "one carrier, NordFrost; second carrier open" | Plan: Head of Logistics. B-A2: Dispatch lead. R-08: **no owner named** |

### Where they agree

| Topic | Plan v3 | BIA v2 / register v5 |
|---|---|---|
| Main carrier | §5: "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | B-A2: "carrier: NordFrost". R-08: "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost" |
| Carrier escalation route | §4: "Carrier escalation: NordFrost control room, 040 555 0900." | B-A2: "carrier escalation: NordFrost control room". The BIA holds no phone number, so the number can't be compared (see Gaps). |
| System named | §6: "Orders leave LogiStock by the manual export in work instruction WI-14." | B-A2: "warehouse system LogiStock". The two only agree on the name (see Gaps). |

### Gaps

**Plan values the BIA and register don't cover:**
- **Activation threshold:** §1 says "Loss of Hall 3 (chilled dispatch) for more than two hours." The BIA and register have nothing on this.
- **Recovery location:** §1 says "Recovery option: move chilled dispatch to Site B." B-A2 doesn't mention Site B. The approved strategy that the plan should carry out wasn't attached, so I couldn't check whether Site B is that strategy.
- **Duty manager contact:** §4 lists "Duty manager, Site A: 040 555 0172". The BIA and register have nothing on this, and no contact list was attached.
- **NordFrost control room number:** §4 gives "040 555 0900". The BIA and register have no number, and there's no dated contact list to check it against.
- **LogiStock recovery time:** register R-09 says "LogiStock restored within 6 hours" (owner: IT service owner). The plan sets no restore time for LogiStock, only "the manual export in work instruction WI-14". WI-14 wasn't attached.
- **Trunking direction:** BIA B-A1 says "inbound trunking from Site B". The plan and R-08 say "from Site A to Site B". All three name NordFrost as the carrier. I'm recording this as a gap, not a disagreement, because B-A1 is goods receipt and not the dispatch entry.

**Source problems:**
- **R-06 to R-09 appear to cite text the BIA extract doesn't contain.** R-09 cites "BIA v2, B-A2" for the 6-hour figure, but the B-A2 row in the extract gives no restore time for LogiStock. Under assumption 2 below, the 6-hour figure has no BIA source in what you attached. It's for the BCM manager and the IT service owner to settle.
- **R-08 has no named owner.**
- No prompt-injection text was found in the attachments.

**Your answers to the intake questions:**
- You couldn't answer the three intake questions and asked me to go ahead on my assumptions. That's your statement, not a source. The assumptions were:
  1. BIA v2 is the current approved BIA.
  2. The extract is the complete B-A2 entry.
  3. Plan v3 is current, with no later draft.
- If any of these turns out to be wrong, re-run the comparison against the right version.

---

**Reviewer:** you, as the BCM manager who asked, check each quoted passage against its source. The Head of Logistics (plan owner) and the Dispatch lead (B-A2 activity owner) decide whether their documents change. Since R-08 has no owner, someone needs to be named before the carrier question can be settled. The plan only changes with its owner's approval and a new version.

I didn't edit any of the three files.

> Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

**Next step:** the chilled dispatch recovery plan v3 is flagged. Run it through [`units/prompts/review.md`](units/prompts/review.md) with its owner.
