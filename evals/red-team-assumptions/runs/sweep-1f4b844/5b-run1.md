# /red-team-assumptions case 5b, run1: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `8821d262-f0b7-4c8c-839d-d33b27938fb6`.

Files in the working folder: `bia-extract-dispatch.md`, `option-paper-dispatch.md`, `supplier-record-nordfrost.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** What does this option paper rely on that nobody has checked? The files option-paper-dispatch.md, bia-extract-dispatch.md and supplier-record-nordfrost.md in this folder are attached.

**Reply (verbatim):**

The one input that has been checked is the 8-hour recovery time target (RTO). It comes from BIA v2, which top management approved on 4 Feb 2026. Nothing in the three files supports any of the four §3 assumptions or the §4 cost claim, and the supplier record weakens the one about the carrier.

**What the option relies on without evidence**

1. **The 8-hour target is achievable.** The paper says the move happens "within 8 hours" but gives no timeline. Before Site B can dispatch, it needs: people driving 140 km, the cold room made ready, the order export run, and NordFrost sending trucks to a different site. Nobody has added those times up or tried it.

2. **Site B's spare cold room holds two days of Site A's volume.** No source is given: no capacity figure, no date, no sign-off from Site B. It also assumes the room will still be free when the incident happens, which may not be true in Site B's own busy periods. The paper also doesn't say what happens after two days.

3. **Site A's shift leaders drive to Site B.** No one has asked whether they're willing, whether their contracts allow it, or how they'd be reached outside working hours. The drive itself takes a large part of the 8 hours. The paper names only shift leaders, so it doesn't say who does the actual picking and dispatching.

4. **NordFrost serves both sites.** This is the weakest assumption, and the files work against it:
   - The supplier record says nothing about which sites NordFrost covers, so Site B coverage is unconfirmed.
   - The record says there is "no SLA for recovery support". Nothing obliges NordFrost to send trucks to Site B within 8 hours.
   - The record has "no information on NordFrost's own continuity plan".
   - The BIA says there is "no second carrier recorded". The whole option therefore depends on a single carrier that has made no commitment.

5. **Site B's warehouse system takes Site A orders after a manual export.** There's no sign this has been tested. Nothing says who runs the export, whether product codes and labels match between the two systems, or whether the export still works if Site A's systems were in or relied on Hall 3.

6. **"No additional cost; uses existing capacity."** This is quoted with no source. It leaves out staff travel and overtime, longer delivery runs, any extra charge from NordFrost (which has no recovery SLA), and the effect on Site B's own work. It also depends entirely on assumption 2 being true.

7. **An unstated one: the chilled stock is still available.** Hall 3 is the hall that's lost. The paper moves dispatch to Site B but doesn't say where the products come from or how they get there.

**Before the 2 Oct decision (tomorrow)**

The steering group should know that every item in §3 is an unchecked assumption, not an established fact. The quickest checks to do today:
- Get written confirmation from NordFrost that it covers Site B and will support a switch within 8 hours. This is the biggest gap.
- Get written confirmation from Site B of the cold room's capacity and availability.
- Run a trial of the order export.

If those can't be done in time, the group could approve the option on the condition that they're done by a set date, rather than adopting it as it stands.

I can also turn this into a one-page list of assumptions and who owns each check, to share with the steering group.

**Tool calls (stream-json):**

- Bash: `ls -la && cat option-paper-dispatch.md bia-extract-dispatch.md supplier-record-nordfrost.md`
