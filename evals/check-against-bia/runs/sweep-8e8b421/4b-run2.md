# /check-against-bia case 4b, run2: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `4fa77215-1abe-451c-beb4-158ec2a58175`.

Files in the working folder: `bia-extract-dispatch.md`, `plan-chilled-dispatch.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Does our dispatch plan still match the BIA? The files plan-chilled-dispatch.md and bia-extract-dispatch.md in this folder are attached.

**Reply (verbatim):**

**No, it doesn't match.** The plan covers BIA entry **B-A2 (Dispatch, chilled)**. It conflicts with that entry in three places, and two of those mean the plan falls short of what the BIA requires.

**Conflicts**

| # | Item | Plan (v3, 12 Mar 2026) | BIA B-A2 (v2, 4 Feb 2026) | Effect |
|---|---|---|---|---|
| 1 | Recovery time | Within **12 hours** (§2) | RTO **8 hours** | The plan misses the RTO by 4 hours. It's still inside the 24-hour MTPD, but it doesn't meet the objective top management approved. |
| 2 | Pickers per shift | Minimum **3** (§3) | At least **4** | The plan staffs Site B below what the BIA says the activity needs. |
| 3 | Backup carrier | **KuehlTrans** by spot booking (§5) | "**No second carrier recorded**" | Either the BIA is out of date or the plan relies on a carrier the BIA doesn't know about. Spot booking also isn't a guaranteed arrangement, so it may not hold up in a real incident. |

**What matches**
- The main carrier is NordFrost in both.
- Carrier escalation goes to the NordFrost control room in both.
- Both name LogiStock as the warehouse system. The plan adds the manual export in WI-14.

**Worth checking**
- **Owners:** the plan is owned by the Head of Logistics, but the BIA names the Dispatch lead as activity owner. That's fine if it's intended, but the Dispatch lead should at least confirm the plan.
- **Things the BIA doesn't record:** the plan depends on Site B, on Site A → Site B trunking and on WI-14. None of these appear in the BIA's resources and dependencies for B-A2.
- **Reliance on one carrier:** NordFrost appears in the plan both for trunking and for outbound transport. In the BIA it also handles chilled goods receipt (B-A1). One NordFrost failure would therefore hit receipt and dispatch together. That's another reason to settle the second-carrier question.
- **What I couldn't check:** the phone numbers in §4 can't be checked against the BIA, because it doesn't list any.

**What to do next**
1. **Recovery time:** either get Site B dispatch running within 8 hours, or take a case for a longer RTO to the BIA owner (the BCM manager) and top management. The plan shouldn't quietly use 12 hours.
2. **Staffing:** raise §3 to at least 4 pickers per shift.
3. **Backup carrier:** decide whether KuehlTrans is a real backup carrier. If it is, record it in the BIA and consider a framework agreement instead of spot booking. If it isn't, take it out of the plan.

Note that the BIA extract is marked **high sensitivity**. Keep that in mind if you pass these findings on.

**Tool calls (stream-json):**

- Bash: `ls -la && cat plan-chilled-dispatch.md && echo ======== && cat bia-extract-dispatch.md`
