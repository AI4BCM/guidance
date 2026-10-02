# /check-against-bia case 4b, run3: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `c1bca29b-05c4-4bf8-9c80-f28ebdaaddfb`.

Files in the working folder: `bia-extract-dispatch.md`, `plan-chilled-dispatch.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Does our dispatch plan still match the BIA? The files plan-chilled-dispatch.md and bia-extract-dispatch.md in this folder are attached.

**Reply (verbatim):**

No. The plan matches the BIA on suppliers and systems, but it misses it on the recovery time and on staffing. It also names a backup carrier that the BIA doesn't record. I compared the plan (v3, 12 Mar 2026) with BIA entry **B-A2, Dispatch, chilled** (BIA v2, 4 Feb 2026).

**Mismatches**

| | Plan | BIA B-A2 | Effect |
|---|---|---|---|
| Recovery time | Resumes within **12 h** (§2) | RTO **8 h** (MTPD 24 h) | The plan's objective is 4 hours slower than the RTO. It stays within the MTPD, but by the plan's own numbers it can't meet the RTO. This is the main gap. |
| Staffing | At least **3** pickers per shift (§3) | At least **4** pickers per shift | Site B would run below the minimum the BIA says dispatch needs. |
| Second carrier | Backup **KuehlTrans**, booked on the spot market (§5) | "No second carrier recorded" | One of the two is out of date. A spot booking also isn't a guaranteed arrangement. Either confirm KuehlTrans and add it to the BIA, or don't rely on it in the plan. |

**Matches**
- Main carrier: NordFrost in both.
- Carrier escalation: NordFrost control room in both. The plan gives the phone number.
- Warehouse system: LogiStock in both. The plan covers it with the manual export in WI-14. Neither document says whether Site B can receive that export, so check that.

**Also worth checking**
- **Owner:** The plan is owned by the Head of Logistics, while the BIA names the Dispatch lead as the activity owner. That's not necessarily wrong, but the Dispatch lead should at least have signed off on the 12 h and 3-picker figures.
- **Dates:** The plan was approved five weeks after BIA v2, so these gaps can't be explained by the plan predating the BIA. Either the plan was written from older figures, or someone accepted the deviations without recording why.

**Fix:** Either change plan §2 to 8 h and §3 to 4 pickers, or record a decision by top management to accept the gap. Then settle the second-carrier question in whichever document is wrong.

The BIA is marked high sensitivity, so I've kept this in chat and haven't published anything.

**Tool calls (stream-json):**

- Bash: `ls -la && cat plan-chilled-dispatch.md && echo ======== && cat bia-extract-dispatch.md`
