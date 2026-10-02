# /check-against-bia case 1b-variant, run3: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `1cc5aab5-7aaf-4cc4-ae25-43d44deb22a8`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `requirements-register.md`.
Variant of 1b: only the change notice, the BIA and the register attached.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia New contract trunking supplier from january, what does it touch? The files change-trunking-supplier.md, bia-extract-dispatch.md and requirements-register.md in this folder are attached.

**Reply (verbatim):**

I haven't opened the three files yet. Before I do, I need to know what class of data they hold.

**What sensitivity class is in `change-trunking-supplier.md`, `bia-extract-dispatch.md` and `requirements-register.md`? And is this environment approved for that class?**

A BIA extract and a supplier change usually count as high-sensitivity under the AI4BCM data rules. They may include BIA data, supplier dependencies or contractual terms, contact details, or recovery strategies and their assumptions. Data in that class may only be handled in an approved corporate or private environment.

- **If this environment is approved for that class**, confirm it and I'll read the files and continue the check.
- **If it isn't approved, or you're not sure**, I'll stop here. You can then run the check in an approved environment, or attach versions with the sensitive details removed.

Passwords, keys and access tokens go into no tool, approved or not. If any of the files contain them, take them out first.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read all three files. Before I write the draft, I have three questions about things the files leave open. Your answers will only shape the scope. They won't supply any value in the draft.

1. **Plans to search:** None of the files is a plan. Can you attach the plans the carrier change could touch? Likely ones are the Site A chilled dispatch plan, the goods-receipt plan, and any transport or carrier-escalation procedure. If you'd rather not, I'll check only the BIA and register entries and write "plans: coverage unknown, none attached".
2. **Other documents:** Do you want to attach contact lists, the escalation route, or the NordFrost or Polar Haul contract or service terms? Anything you don't attach goes under **Coverage unknown**.
3. **Inbound trunking:** The change notice says chilled trunking "between Site A and Site B" moves to Polar Haul. Does that include inbound trunking from Site B into Site A? BIA entry B-A1 relies on that inbound leg. If you skip this, I'll assume "between" means both directions, so B-A1 is in scope, and record that as my assumption.

## Turn 3

**Request:** None to hand.

**Reply (verbatim):**

From change notice "Change notice: chilled trunking carrier", dated 15 Sep 2026, no version (status: planned, approved by the procurement board)
Compared against BIA v2, approved 4 Feb 2026 (extract "Site A, chilled operations")
Compared against requirements register v5, 10 Feb 2026 (status: approved by the BCM manager)

**Reviewer:** the BCM manager who asked for this check checks each quoted passage below. Each BIA activity owner, and the register entry's owner once someone is named, decides whether their entry changes. A plan changes only with its owner's approval and a new version.

You gave me a change and no plan, so this draft has only block 2. There is no block 1 (checking a plan against the BIA).

---

## Block 2: What the change reopens

**The change**, quoted from the change notice (15 Sep 2026): "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul, under a new contract. NordFrost's control room will no longer handle Site A loads from that date."

| Entry | Line it touches, quoted | Source and date | Owner the sources name | Status |
|---|---|---|---|---|
| BIA B-A1, Goods receipt, chilled | "carrier: NordFrost, inbound trunking from Site B" | BIA v2, B-A1, approved 4 Feb 2026 | Warehouse lead | proposed, to confirm (rests on the assumption in Gaps) |
| BIA B-A2, Dispatch, chilled | "carrier: NordFrost, no second carrier recorded" | BIA v2, B-A2, approved 4 Feb 2026 | Dispatch lead | proposed, to confirm |
| BIA B-A2, Dispatch, chilled | "carrier escalation: NordFrost control room" | BIA v2, B-A2, approved 4 Feb 2026 | Dispatch lead | proposed, to confirm |
| Register R-08 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | Requirements register v5, R-08, 10 Feb 2026 | owner: to be confirmed (the column is blank) | proposed, to confirm |

I propose no replacement values. Whether each line now reads Polar Haul, and what the carrier escalation becomes, is for the owners above to decide.

**Searched and not touched:**
- BIA B-A3 (Quality release)
- Register R-06, R-07 and R-09

R-07 and R-09 come from B-A2, but their lines ("at least 4 pickers per shift", "LogiStock restored within 6 hours") don't mention the carrier.

**Plans:** coverage unknown, none attached.

### Gaps
- **R-08 has no owner.** The Owner column is empty, so nobody is named to confirm the change to this entry.
- **The change notice has no version.** It is dated 15 Sep 2026 and its status is "planned". I used it as the description of the change, not as a statement of the current state. The current carrier is NordFrost until 1 Jan 2027.
- **Inbound trunking is my assumption.** You didn't say whether the change covers trunking from Site B into Site A. I've assumed "between Site A and Site B" means both directions, which is why B-A1 is in the table. That's my assumption, not something the sources say.
- **No other documents were available.** You said no plans or other documents are to hand. This is your statement, not a source.
- **NordFrost's future role:** not in the sources. The notice doesn't say whether NordFrost stays on as a second or fallback carrier, and the register lists a second carrier as "open".
- **Polar Haul's escalation contact or control room:** not in the sources.

### Coverage unknown
The change could touch these kinds of document, but none were attached:
- the Site A chilled dispatch and goods-receipt continuity plans, and any transport or logistics plan
- carrier escalation routes and the contact lists that hold NordFrost control-room details
- supplier contracts and service terms for NordFrost and for Polar Haul
- the Site B BIA entries and plans for the other end of the trunking leg
- the risk register entries on carrier dependency
- the approved continuity strategy for chilled transport

---

**Next step:** no plans were attached, so none are flagged yet. When the Site A plans become available, run this check again with them attached. For each plan it flags, use `units/prompts/review.md`.

> Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
