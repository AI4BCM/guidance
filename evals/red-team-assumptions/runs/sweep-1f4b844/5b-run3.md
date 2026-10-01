# /red-team-assumptions case 5b, run3: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `a93bb4ea-06fe-40d8-be10-d7af949cf855`.

Files in the working folder: `bia-extract-dispatch.md`, `option-paper-dispatch.md`, `supplier-record-nordfrost.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** What does this option paper rely on that nobody has checked? The files option-paper-dispatch.md, bia-extract-dispatch.md and supplier-record-nordfrost.md in this folder are attached.

**Reply (verbatim):**

The paper rests on four assumptions in §3 and a cost claim in §4. None of them has supporting evidence in the three files. The only thing that's actually backed is the 8-hour target, which matches the approved BIA. The decision is due tomorrow, 2 Oct.

**What's backed up**
- **The 8-hour RTO.** It matches BIA v2, which top management approved on 4 Feb 2026.
- **NordFrost is a current supplier.** Its contract runs to 31 Dec 2027.

**What nobody has checked, most serious first**

1. **NordFrost's part in recovery (§3, bullet 3).** This is the weakest point, and the files actually point against it.
   - The supplier record says NordFrost has no SLA for recovery support. It also says there's no information on NordFrost's own continuity plan.
   - The BIA lists NordFrost as the only carrier: "no second carrier recorded."
   - So the plan depends on one carrier that has no obligation to help in a recovery. Nothing shows it can switch collections to Site B, 140 km away, within 8 hours.
   - Nothing in the files confirms the paper's claim that NordFrost already serves Site B.

2. **Whether the move can be done in 8 hours at all (§2).** There's no step-by-step timeline. The drive alone is about 2 hours, before anyone has called people out, done the system export, briefed the carrier or loaded the cold room. Nothing shows it has ever been tested or rehearsed.

3. **The cold room at Site B (§3, bullet 1).**
   - Nothing confirms the space is really spare, or that it will still be free on the day it's needed rather than full of Site B's own seasonal stock.
   - Nothing confirms it can hold the right temperature range for Site A's products.
   - "Two days' volume" quietly assumes Hall 3 is back within 48 hours. The paper doesn't say what happens if the outage runs longer.

4. **The warehouse system workaround (§3, bullet 4).**
   - The manual export has to come out of Site A's system. Nobody has checked whether that system, or the network it relies on, still works when Hall 3 is lost.
   - Nobody has said who does the export, how long it takes, or whether Site B's system can take Site A's product codes and customers.

5. **The staff (§3, bullet 2).**
   - Nothing confirms the shift leaders are available, contractually required to go, or willing to drive 140 km at short notice.
   - Nothing confirms they have access to Site B or have been trained on its system.
   - Only shift leaders are named. The paper doesn't say who does the picking and loading.

6. **"No additional cost" (§4).** This is a quote with no figures and no source. A 140 km move would plausibly bring overtime, travel, longer carrier routes and lost Site B capacity.

**Gaps the paper doesn't address**
- **Stock.** If Hall 3 is lost, its chilled stock is probably lost too. The paper doesn't say where the goods dispatched from Site B come from.
- **MTPD.** The BIA gives a 24-hour MTPD (maximum tolerable period of disruption), which the paper never mentions. If the 8-hour move slips, there's no fallback before that 24-hour limit.

**Before the steering group decides**, I'd want at least three things:
- Written confirmation from NordFrost that it can switch to Site B, and how fast.
- A check that the Site B cold room is genuinely free and suitable.
- A dry run of the system export with Hall 3 treated as down.

Without those, the steering group would be approving an idea rather than a recovery option that's been shown to work.

**Tool calls (stream-json):**

- Bash: `ls -la && for f in option-paper-dispatch.md bia-extract-dispatch.md supplier-record-nordfrost.md; do echo "=== $f"; cat -n "$f"; done`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/red-team-assumptions/5b/run3/work/option-paper-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/red-team-assumptions/5b/run3/work/bia-extract-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/red-team-assumptions/5b/run3/work/supplier-record-nordfrost.md`
