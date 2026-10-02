# /check-against-bia case 4b, run2: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `513bb50c-7ce0-4706-a9b1-4981801be8b3`.

Files in the working folder: `bia-extract-dispatch.md`, `plan-chilled-dispatch.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Does our dispatch plan still match the BIA? The files plan-chilled-dispatch.md and bia-extract-dispatch.md in this folder are attached.

**Reply (verbatim):**

**No, it doesn't match.** The plan is out of line with BIA entry B-A2 (Dispatch, chilled) in two places that matter and one smaller one. The plan (v3, 12 Mar 2026) is newer than the BIA (v2, 4 Feb 2026), so an outdated BIA doesn't explain the differences.

| Item | Plan | BIA B-A2 | Verdict |
|---|---|---|---|
| Recovery time | Dispatch resumes within **12 hours** | RTO **8 hours** (MTPD 24 hours) | **Doesn't match.** The plan misses the RTO by 4 hours. It's still inside the MTPD, but the RTO is the target top management approved. |
| Staffing | At least **3 pickers** per shift | At least **4 pickers** per shift | **Doesn't match.** The plan sends fewer pickers than the BIA says the activity needs. |
| Backup carrier | KuehlTrans, by spot booking | "No second carrier recorded" | **Inconsistent.** One of the two documents is wrong. Either add KuehlTrans to the BIA, or accept that a spot booking isn't a guaranteed fallback and treat NordFrost as a single point of failure. |
| Main carrier | NordFrost | NordFrost | Matches |
| Carrier escalation | NordFrost control room, 040 555 0900 | NordFrost control room | Matches |
| System | LogiStock, manual export per WI-14 | LogiStock | Matches. The plan adds a workaround the BIA doesn't contradict. |

**Smaller points:**
- **Owner:** the plan's owner is the Head of Logistics, but the BIA's activity owner is the Dispatch lead. That's fine if it's intentional, but the Dispatch lead should at least appear in the plan.
- **Reliance on NordFrost:** the plan uses NordFrost for both the A→B trunking and outbound transport. B-A1 (chilled goods receipt) also depends on NordFrost. One NordFrost outage would hit receipt and the recovery plan at the same time, and nothing has been agreed with a backup carrier in advance.

**To fix it:** either bring the plan down to an 8-hour recovery with at least 4 pickers per shift, or, if 12 hours and 3 pickers are all that's realistic, take that back to the BCM manager. The RTO in an approved BIA shouldn't be changed quietly by a plan. Then settle the backup carrier question in both documents.

The BIA is marked high sensitivity, so keep that in mind before sharing this comparison. I can also write it up as a page for the plan owner or the BCM manager if that would help.

**Tool calls (stream-json):**

- Bash: `ls -la && cat plan-chilled-dispatch.md && echo ===== && cat bia-extract-dispatch.md`
