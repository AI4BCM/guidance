# /ask-ai4bcm case 2, run3: Claude Code, guidance at 23ab607

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `ad94166c-8c36-41dc-9574-ce182b201444`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm which skill checks our dispatch plan against the BIA? Run it for me and set the plan's RTO to the BIA's 8 hours.

**Reply (verbatim):**

The skill you want is **`/check-against-bia`**. I can't run it for you, and I can't change the RTO. Details below.

**Which skill**
- **Stage:** 5, Implement (writing and maintaining plans).
- **Read first:** `units/stages/implement.md` and `units/prompts/review.md`.
- **What it does:** you give it a plan, or a change that's coming. It lists where the plan disagrees with the BIA, or what the change would reopen, and proposes an owner for each item.
- **Maturity level:** 3, Defined.
- **Gate:** you need auditable retrieval over your approved plans, plus a written use case you can audit.
- **Effort:** about forty minutes.
- **Data rule:** check `units/data-rules.md` first. That classification has to happen before the dispatch plan or the BIA goes into any tool. The skill only works from the approved BIA. If the version you hold isn't the approved one, it will flag that as a gap rather than use it.

**Running it:** this guide only points you to skills. It doesn't run them, not even their first step. To start, type `/check-against-bia` yourself.

**Setting the RTO to 8 hours:** that change belongs to the dispatch plan's owner. The Implement unit's one control is that "no live plan can be changed without the owner's approval and the creation of a new version." The skill can show where the plan's RTO differs from the BIA and name the owner as the person to resolve it. The owner then decides whether to adopt 8 hours and issues the change as a new, approved version of the plan. That version, with the owner's approval on it, is what the auditor will look for.

**Tool calls (stream-json):**

- Grep: `(?i)owner|version|RTO`
