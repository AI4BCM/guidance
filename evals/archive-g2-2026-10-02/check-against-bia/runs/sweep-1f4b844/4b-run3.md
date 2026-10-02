# /check-against-bia case 4b, run3: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `c9f3b98a-51d4-4b36-bfcf-3dcc44ef87b8`.

Files in the working folder: `bia-extract-dispatch.md`, `plan-chilled-dispatch.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Does our dispatch plan still match the BIA? The files plan-chilled-dispatch.md and bia-extract-dispatch.md in this folder are attached.

**Reply (verbatim):**

No. The plan doesn't match BIA entry B-A2 (Dispatch, chilled) on two requirements, and the two documents disagree on the backup carrier. The plan (v3, 12 Mar 2026) is newer than the BIA (v2, 4 Feb 2026), so it doesn't look like the BIA changed after the plan was written.

**Where they don't match**

| Point | Plan | BIA B-A2 | Problem |
|---|---|---|---|
| Recovery time | Resume within **12 h** (§2) | RTO **8 h** (MTPD 24 h) | The plan aims 4 hours later than the BIA's target. 12 h is still inside the 24 h maximum, but it doesn't meet the RTO. |
| Staffing | At least **3 pickers** per shift (§3) | At least **4 pickers** per shift | The plan staffs below what the BIA says is needed. |
| Second carrier | Backup **KuehlTrans, by spot booking** (§5) | "No second carrier recorded" | Either the BIA is out of date or the backup is weaker than the plan suggests. A spot booking isn't a contract, so it may not be there when you need it. Settle it one way and record it in both documents. |

**Where they match**
- The warehouse system is LogiStock in both. The plan also names the manual export (WI-14).
- The main carrier is NordFrost in both, and the escalation contact is the NordFrost control room in both. The BIA has no phone numbers, so I couldn't check 040 555 0900.

**Worth a look, though not strictly mismatches**
- **Owner:** the plan is owned by the Head of Logistics, while the BIA's activity owner is the Dispatch lead. Make sure the Dispatch lead has reviewed or agreed the plan.
- **Site B:** the plan depends on Site B, but B-A2 doesn't list it as a resource. B-A1 (Goods receipt) already relies on inbound trunking from Site B, so check that Site B can handle both at once.
- **NordFrost:** the plan uses NordFrost for both the Site A to Site B trunking and the outbound transport. That makes the backup carrier question above more important.

**To bring them back in line:** change §2 to 8 hours (or show that it can be met), raise §3 to 4 pickers, and have the BCM manager update B-A2 if KuehlTrans really is the backup carrier.

I can write this up as a short page to share with the plan and BIA owners if that would help.

**Tool calls (stream-json):**

- Bash: `ls -la && cat plan-chilled-dispatch.md && echo ======= && cat bia-extract-dispatch.md`
