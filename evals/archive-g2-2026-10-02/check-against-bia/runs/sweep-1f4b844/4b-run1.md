# /check-against-bia case 4b, run1: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `3c979db0-2f75-48f4-9b79-74c94d9fae40`.

Files in the working folder: `bia-extract-dispatch.md`, `plan-chilled-dispatch.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Does our dispatch plan still match the BIA? The files plan-chilled-dispatch.md and bia-extract-dispatch.md in this folder are attached.

**Reply (verbatim):**

**No.** The plan matches the BIA on systems and the escalation contact, but it misses the BIA's recovery time and staffing minimum for chilled dispatch (entry B-A2). The plan (v3, 12 Mar 2026) was approved five weeks after the BIA (v2, 4 Feb 2026), so an older BIA doesn't explain the differences.

**Conflicts with the BIA**

| | BIA B-A2 | Plan | Problem |
|---|---|---|---|
| Recovery time | RTO **8 hours** (MTPD 24 hours) | Resume within **12 hours** (§2) | The plan's target is 4 hours later than the RTO. It is still inside the 24-hour MTPD, but it doesn't meet the RTO. |
| Staffing | **At least 4** pickers per shift | **At least 3** pickers per shift (§3) | The plan has fewer pickers than the BIA requires. |

**Differences to sort out (not failures in the plan)**

- **Second carrier:** The BIA says "no second carrier recorded," but the plan names KuehlTrans as a backup (§5). Either the BIA needs updating, or the backup isn't reliable enough to record. KuehlTrans is "spot booking" only, with no contract, so check that they can actually provide chilled capacity at short notice before counting on them.
- **Site B isn't in the BIA:** The whole recovery option depends on Site B and on NordFrost trunking from Site A to Site B. Neither appears in B-A2's dependencies. NordFrost also covers outbound transport and goods receipt (B-A1), so one carrier failure would affect everything.
- **Owners:** The plan owner is the Head of Logistics, while the BIA's activity owner is the Dispatch lead. That's fine if it's intended, but the Dispatch lead should sign off on the plan.

**What matches**

- LogiStock is covered by the manual export in WI-14 (§6).
- The carrier escalation contact is the same: the NordFrost control room.
- The 2-hour trigger (§1) fits comfortably within an 8-hour RTO.

**Recommended fix:** Change §2 to 8 hours or less and §3 to at least 4 pickers. If 8 hours can't be reached through Site B, take that to the BCM manager. Then either the BIA's RTO gets formally revisited or the recovery option needs rethinking; the plan shouldn't quietly diverge from the BIA. Also ask the BCM manager to add KuehlTrans and the Site B dependency to B-A2 in the next BIA update.

**Tool calls (stream-json):**

- Bash: `ls -la && cat plan-chilled-dispatch.md && echo ======= && cat bia-extract-dispatch.md`
