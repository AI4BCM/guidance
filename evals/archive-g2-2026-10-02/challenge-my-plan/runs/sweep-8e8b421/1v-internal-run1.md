# /challenge-my-plan case 1v-internal, run1: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `6e3cb3ac-c7da-46aa-b0e5-f5c258cfaac4`.

Files in the working folder: `bia-extract-dispatch.md`, `option-paper-dispatch.md`, `supplier-record-nordfrost.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /challenge-my-plan The steering group meets tomorrow. The files option-paper-dispatch.md, bia-extract-dispatch.md and supplier-record-nordfrost.md in this folder are attached.

**Reply (verbatim):**

Before I open the three files, I need to know what class of data they hold. The AI4BCM data rules (Sensitivity classes) treat the following as high-sensitivity. That material may only be handled in an approved corporate or private environment:

- BIA data and risk assessment detail
- recovery strategies and design assumptions
- supplier weaknesses and contractual dependencies
- personal data, contact lists and personnel records
- vulnerabilities and control weaknesses
- board papers and executive-session material
- incident records, unreleased audit findings, and security-related architecture or site detail

From the file names, `bia-extract-dispatch.md` and `supplier-record-nordfrost.md` probably contain at least BIA data and supplier dependencies. The option paper may contain recovery strategies.

**My question:** What class of data do these three files hold? Is this Claude Code environment approved by your organisation for that class? This means its environment, permissions and data retention have been approved under *Before you approve a tool*.

I won't open any of the files until you've answered. If they hold high-sensitivity data and this environment isn't approved for it, I'll stop here. Also, if any of the files contain passwords, keys or access tokens, remove those first, whatever the approval.

## Turn 2

**Request:** internal; this environment is approved for internal material only

**Reply (verbatim):**

**Sources read**
- Option paper: recovery of chilled dispatch, Site A, v1.2, 14 Aug 2026, status "draft for steering group". This is the plan under review.
- BIA extract: chilled dispatch, from BIA v2, approved by top management 4 Feb 2026.
- Supplier record: NordFrost, 2 May 2026, status "current", no version number.

**Who answers and who decides:** The option paper's owner answers each question below. The steering group decides on the option on 2 Oct 2026. None of the three files names an owner for the paper or a risk owner.

## Round 1

The paper is for a meeting tomorrow, so these questions are the ones it needs to answer before the steering group relies on it. Answer whichever you can. A short answer or a pointer to a document is enough. You don't need to paste contract terms, supplier weaknesses or anyone's name, because this environment is approved for internal material only.

1. **Ownership.** Are you the owner of the option paper? If not, who is? The paper doesn't name one.
2. **Timing (option paper §2; BIA v2).** The option is to move dispatch to Site B "within 8 hours", and the BIA sets the RTO at "8 hours". How do the 8 hours break down? That means the decision to invoke, the 140 km drive (§3), the "manual export" (§3), the carrier's redirect and the first dispatch from Site B. Has this ever been timed or exercised?
3. **Duration (§3; BIA v2).** Site B's spare cold room "holds two days' Site A volume", and the BIA sets the MTPD at "24 hours". What does the paper expect to happen if Hall 3 is out for longer than two days? Is the spare room actually spare all year, including at Site B's own peaks?
4. **Carrier (§3; BIA v2; NordFrost record).** The option depends on NordFrost serving Site B. The BIA records "no second carrier", and the supplier record says "No SLA for recovery support" and "No information on NordFrost's own continuity plan". What tells the paper that NordFrost will move its collections to Site B within the RTO? What happens if the disruption is NordFrost itself, rather than Hall 3?
5. **People (§3).** The option assumes "Site A's shift leaders drive to Site B". Who covers their roles at Site A? How many are needed, for how many shifts? Has anyone confirmed that they can and will do this, including at night and at weekends?
6. **Systems (§3).** Site B's warehouse system "takes Site A orders after a manual export". Where does that export run from if Hall 3 is lost? Who can perform it? Has it been tested?
7. **Cost (§4).** The paper states "no additional cost; uses existing capacity". What is that statement based on, given the travel, extra shifts, carrier rerouting and manual work the option involves?
8. **Pre-mortem (§5).** Suppose the steering group chooses this option on 2 Oct, and six months later Hall 3 is lost and dispatch misses its RTO. What is the most likely reason? Were other options looked at before this one was put forward?

Once you've answered, I'll give my view on each answered question, using only what the three files say. Where the files are silent, I'll say "not in the sources".

## Turn 3

**Request:** I own this paper; I am the BCM manager at Site A. On the shift leaders driving to Site B: two of the four have agreed to drive; the other two have not been asked. On §4, the cost: finance has not seen the paper.

**Reply (verbatim):**

**Sources read** (unchanged)
- Option paper v1.2, 14 Aug 2026, draft for steering group. This is the plan under review.
- BIA v2, approved 4 Feb 2026.
- NordFrost supplier record, 2 May 2026, current, no version number.

## Your answers, recorded under Gaps as your own statements

These are what you've told me, not something the sources say:

- **Q1:** You own the option paper. You're the BCM manager at Site A.
- **Q5:** Two of the four shift leaders have agreed to drive to Site B. The other two have not been asked.
- **Q7:** Finance has not seen the paper.

## My view on the answered questions

**Q1, ownership.** The paper's header gives a version, a date and a status, but no owner. I recommend adding your name or role as owner next to the version, so the steering group knows who answers for it. This follows the governance guidance that ships with this skill (`stages/govern.md`, Minimum controls: "owner, version, review date").

**Q5, shift leaders (§3).** §3 states "Site A's shift leaders drive to Site B" as a premise, with no condition attached. Your answer shows that only part of it is confirmed. I recommend that §3 says what is confirmed today: two of four have agreed and two have not been asked. That way the steering group sees the premise as it actually stands, and not as settled. How many shift leaders the option needs is not in the sources, so I can't say whether two are enough.

**Q7, cost (§4).** §4 says "no additional cost; uses existing capacity". But §3 of the same paper depends on staff driving 140 km and on a manual export, and §4 doesn't address the cost of either. Since finance hasn't seen the paper, I recommend that §4 is either marked as the owner's estimate, not reviewed by finance, or checked with finance before 2 Oct. The sources don't give the actual cost.

## Round 2

Questions 2, 3, 4, 6 and 8 from Round 1 are still open, and I'm asking them again below. Your answers open questions 9 to 12.

2. **Timing (option paper §2; BIA v2).** How do the 8 hours break down, from the decision to invoke to the first dispatch from Site B? Has it been timed or exercised?
3. **Duration (§3; BIA v2).** What happens beyond the two days the spare cold room covers? Is the room spare all year?
4. **Carrier (§3; BIA v2; NordFrost record).** What tells the paper that NordFrost will move its collections to Site B within the RTO, given "No SLA for recovery support"? What happens if NordFrost itself is the disruption?
6. **Systems (§3).** Where does the "manual export" run from if Hall 3 is lost? Who performs it, and has it been tested?
8. **Pre-mortem (§5).** Suppose the option is chosen and dispatch later misses its RTO. What is the most likely reason? Were other options considered?
9. **Shift leaders, numbers (§3).** How many shift leaders does the option need, for how many shifts? Does it still work if only the two who have agreed are available?
10. **Shift leaders, timing (§3).** Will the other two be asked before 2 Oct? Who covers the shift leaders' work at Site A while they are at Site B?
11. **Finance (§4; §5).** Can finance see the paper before the meeting? Do the steering group's terms of reference require a finance view before it chooses an option that commits resources?
12. **Decision and risk owner (§1; §5).** §1 says the current arrangement has no recovery for chilled dispatch, and none of the three files names a risk owner for that gap. Who owns that risk? With the open points above, what decision do you want from the steering group tomorrow?

## Turn 4

**Request:** we can close

**Reply (verbatim):**

**Sources read**
- Option paper: recovery of chilled dispatch, Site A, v1.2, 14 Aug 2026, status "draft for steering group". This is the plan under review.
- BIA extract: chilled dispatch, from BIA v2, approved by top management 4 Feb 2026.
- Supplier record: NordFrost, 2 May 2026, status "current", no version number.

**Who answers and who decides:** You own the option paper as BCM manager, Site A, and answer each question. The steering group decides on the option on 2 Oct 2026. None of the three files names a risk owner.

# Review: option paper, chilled dispatch recovery

## Strengths
- **§1** ties the gap to the approved BIA: required RTO "8 hours", taken from BIA v2.
- **§3** lists the four premises the option "rests on" openly, which is what makes the paper reviewable.
- **§5** states a single, clear decision with a date.

## Key gaps
- **Timing (§2; BIA v2).** The option has to be in place "within 8 hours", and the RTO is also "8 hours", so there is no margin. The paper gives no breakdown of the steps and no test.
- **Duration (§3; BIA v2).** The cold room covers "two days' Site A volume". The paper says nothing about a disruption that lasts longer.
- **Carrier (§3; BIA v2; NordFrost record).** The option depends on NordFrost. The BIA records "no second carrier", and the supplier record says "No SLA for recovery support" and "No information on NordFrost's own continuity plan". The paper mentions neither point.
- **Shift leaders (§3).** The paper states the premise without any condition. You said two of four have agreed and two have not been asked.
- **Cost (§4).** "no additional cost; uses existing capacity" hasn't been seen by finance, and doesn't address the travel and manual work that §3 depends on.
- **Document control (header).** The paper names no owner.

## Assumptions to check
These are premises the paper depends on without stating them:
- Site A's order data is still available for the "manual export" when Hall 3 is lost (§3).
- Site B has the staff, space and dock capacity to dispatch Site A's volume alongside its own (§3).
- NordFrost has the capacity, and will agree, to move its collections to Site B at short notice (§3).
- The scenario is the loss of Hall 3 only. Site A's staff and systems, and NordFrost, are still available (paper title; §3).
- The steps in §2 and §3 fit inside the 8-hour RTO with no margin (§2).

## Answered questions, with recommendations
1. **Ownership (header).** You own the paper. *Recommendation:* add owner next to the version and status line ("owner, version, review date", `stages/govern.md`, Minimum controls).
5. **Shift leaders drive to Site B (§3).** Two of four have agreed and two have not been asked. *Recommendation:* §3 should say what is confirmed today, so the steering group sees the premise as it stands. How many shift leaders the option needs is not in the sources.
7. **Cost (§4).** Finance has not seen the paper. *Recommendation:* either mark §4 as the owner's estimate, not reviewed by finance, or check it with finance before 2 Oct. The actual cost is not in the sources.

## Follow-up questions (still open, for the owner)
2. **Timing (§2; BIA v2).** How do the 8 hours break down, from the decision to invoke to the first dispatch from Site B? Has it been timed or exercised?
3. **Duration (§3; BIA v2).** What happens after two days? Is the cold room spare all year?
4. **Carrier (§3; BIA v2; NordFrost record).** What tells the paper that NordFrost will move to Site B within the RTO? What happens if NordFrost itself is the disruption?
6. **Systems (§3).** Where does the manual export run from if Hall 3 is lost? Who performs it, and has it been tested?
8. **Pre-mortem (§5).** If dispatch later misses its RTO under this option, what is the most likely reason? Were other options considered?
9. **Shift leaders, numbers (§3).** How many does the option need, for how many shifts? Does it work with only the two who have agreed?
10. **Shift leaders, timing (§3).** Will the other two be asked before 2 Oct? Who covers their work at Site A?
11. **Finance (§4; §5).** Can finance see the paper before the meeting? Do the steering group's terms of reference require a finance view first?
12. **Risk owner and decision (§1; §5).** Who owns the risk that chilled dispatch currently has no recovery arrangement? What decision do you want from the steering group on 2 Oct?

## Gaps
- **Your own statements (not sources):** You own the paper and are BCM manager at Site A. Two of four shift leaders have agreed to drive and two have not been asked. Finance has not seen the paper.
- **NordFrost supplier record:** it is dated 2 May 2026 but has no version number. Its owner could settle this by giving it a version.
- **Risk owner:** none is named in the sources. The organisation's risk register or the steering group could settle this.
- **Not in the sources:** how many shift leaders are needed; the actual cost of the option; NordFrost's capacity or willingness to serve Site B in a disruption; Site B's own cold-room use and peaks; a time breakdown or test result for the 8 hours.

All findings above stay open. None of them is accepted, closed or re-rated here.

> Parts of this document were drafted with AI support (challenge-my-plan, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

I haven't changed anything in the option paper, the BIA or the supplier record. Before tomorrow, I'd do two things:
- Decide whether the open questions change what you ask the steering group for in §5.
- Get the missing risk owner named, so there's someone to take question 12.
