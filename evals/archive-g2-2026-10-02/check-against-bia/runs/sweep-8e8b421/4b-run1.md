# /check-against-bia case 4b, run1: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `9f4008f1-42af-4b03-83fb-d2c3ecc38631`.

Files in the working folder: `bia-extract-dispatch.md`, `plan-chilled-dispatch.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Does our dispatch plan still match the BIA? The files plan-chilled-dispatch.md and bia-extract-dispatch.md in this folder are attached.

**Reply (verbatim):**

No. The plan (v3, 12 March 2026) was written five weeks after the BIA (v2, 4 Feb 2026), but it doesn't match BIA entry B-A2 (Dispatch, chilled) on three points. One of them breaks the recovery objective.

**Mismatches**

| # | Topic | Plan | BIA B-A2 | Effect |
|---|---|---|---|---|
| 1 | Recovery time | Resume within **12 hours** (§2) | RTO **8 hours** | The plan's objective misses the RTO by 4 hours. It's still inside the 24-hour MTPD (the longest the business can tolerate the outage), but the BIA's 8 hours is the target top management approved. This is the most serious gap. |
| 2 | Staffing | At least **3 pickers** per shift (§3) | At least **4 pickers** per shift | Even if the timing were met, the plan sends fewer pickers than the BIA's minimum. |
| 3 | Backup carrier | KuehlTrans, by spot booking (§5) | NordFrost, "no second carrier recorded" | Unlike 1 and 2, the plan has more here than the BIA. Either the BIA is missing a dependency, or KuehlTrans was added to the plan without being checked. Spot booking also isn't guaranteed capacity. Someone needs to confirm KuehlTrans can actually handle chilled loads at short notice, then record it in the BIA. |

**What matches**
- NordFrost as the main carrier, with the NordFrost control room as escalation contact.
- LogiStock as the warehouse system. The plan's WI-14 manual export still needs LogiStock to be running, which fits the BIA's dependency list.

**Minor points to check**
- **Ownership:** the plan is owned by the Head of Logistics, while the BIA names the Dispatch lead as activity owner. That's not necessarily wrong, but the Dispatch lead should at least review or sign off the plan.
- **Site B:** the plan relies entirely on Site B, and neither document shows that Site B can provide 4 pickers per shift or the chilled capacity needed. The BIA extract doesn't cover Site B's resources, so I can't verify this.

**What to fix:** update plan §2 to "within 8 hours" and make sure the recovery steps can actually meet that. Raise §3 to at least 4 pickers per shift. Then align the carrier entry: either record KuehlTrans in the BIA once it's confirmed, or remove it from the plan.

**Tool calls (stream-json):**

- Bash: `ls -la && cat plan-chilled-dispatch.md && echo ======== && cat bia-extract-dispatch.md`
