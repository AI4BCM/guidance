# /challenge-my-plan case 1, run1: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `abd99630-c770-4210-8fa0-7bb1b200f00c`.

Files in the working folder: `bia-extract-dispatch.md`, `option-paper-dispatch.md`, `supplier-record-nordfrost.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /challenge-my-plan The steering group meets tomorrow. The files option-paper-dispatch.md, bia-extract-dispatch.md and supplier-record-nordfrost.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three files, I need to know one thing.

**What class of data do these files hold, and is this environment approved for it?**

From the file names, they likely include material the AI4BCM data rules (`units/data-rules.md`, Sensitivity classes) list as **high-sensitivity**. That material may only be used in an approved corporate or private environment:

- **bia-extract-dispatch.md**: BIA data
- **supplier-record-nordfrost.md**: possibly supplier weaknesses and contractual dependencies
- **option-paper-dispatch.md**: possibly recovery strategies and design assumptions. If it's going to the steering group, it may also count as executive material.

Please tell me:

1. Which class each file falls into (for example: high, BIA data; high, supplier dependencies; medium, internal option paper).
2. Whether this Claude Code session runs in an environment your organisation has approved for that class: an enterprise or private setup with retention, access and logging checked under *Before you approve a tool* in `units/tools.md`.

If it isn't approved for the highest class involved, I'll stop here. In that case the review should run in your approved environment instead. Once you confirm, I'll read the files and start the first round of questions.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Sources read**
- Option paper v1.2, 14 Aug 2026, status: draft for steering group. This is the plan under review.
- BIA v2, approved by top management 4 Feb 2026 (extract: chilled dispatch).
- Supplier record NordFrost, 2 May 2026, status: current. It has no version number (see Gaps).

**Reviewer:** the option paper's owner answers each question below. Until they do, each point stays a question, not a finding. The steering group makes the decision on 2 Oct (§5). None of the three sources names a risk owner for the NordFrost dependency.

**Gaps so far:** the supplier record has a date but no version number. I found no embedded instructions to an AI in any of the files.

## Round 1: questions for the option paper's owner

1. **Ownership.** The option paper doesn't name an owner. Are you the owner? If not, who is? I can only give a view on answers from the owner. If you answer on their behalf, I'll hold my view until they confirm.

2. **§2 "Move chilled dispatch to Site B, 140 km away, within 8 hours"**, against BIA v2 "RTO 8 hours". What is the step-by-step timeline from losing Hall 3 to the first chilled dispatch leaving Site B? That covers the decision to invoke, the 140 km drive, the manual export and NordFrost changing its collections. Has any step been timed or exercised?

3. **§3 "Site B's spare cold room holds two days' Site A volume."** What happens from day three if Hall 3 is still out? Who has confirmed that the cold room is actually spare, and is it spare all year, including Site B's own peak periods?

4. **§3 "Site A's shift leaders drive to Site B."** Who picks and loads Site A's volume at Site B, and does Site B have the staff for it? What happens if a shift leader can't travel, for example at night, or if they're needed at Site A during the incident?

5. **§3 "Carrier 'NordFrost' serves both sites."** The BIA says "no second carrier recorded". The supplier record says "No SLA for recovery support" and "No information on NordFrost's own continuity plan". What tells you NordFrost will move Site A's collections to Site B within the 8 hours?

6. **§3 "Site B's warehouse system takes Site A orders after a manual export."** If Hall 3 is lost, can the export still be run from Site A's system? Who runs it, how long does it take, and has it ever been done?

7. **§4 "no additional cost; uses existing capacity".** What was costed to reach this figure? For example: travel and overtime for shift leaders, NordFrost's extra distance, or Site B work pushed aside by Site A volume.

8. **§5 "Steering group to choose this option".** The paper puts forward one option. Were other options considered? If so, will the steering group see why they were dropped?

9. **Scope, line 5 "Hall 3 lost".** Is the option meant to cover only the loss of Hall 3? If so, are other ways of losing chilled dispatch out of scope, such as NordFrost failing or Site A's system being down? Does the paper tell the steering group that?

10. **Pre-mortem.** Imagine it's a year from now. Hall 3 was lost, the move to Site B was invoked, and chilled dispatch missed the 24-hour MTPD in the BIA. What is the most likely reason it failed?

Please answer as many as you can before tomorrow's meeting. After your answers, I'll give my view on each one, based only on the three files. Any follow-up questions your answers raise will go in the next round.

## Turn 3

**Request:** I own this paper; I am the BCM manager at Site A. On the shift leaders driving to Site B: two of the four have agreed to drive; the other two have not been asked. On §4, the cost: finance has not seen the paper.

**Reply (verbatim):**

Thanks. As the paper's owner, your answers are the ones on record. Here is my view on the three you answered, then round 2.

## Answers on record (Gaps: your own statements, not sources)

- **Q1:** "I own this paper; I am the BCM manager at Site A."
- **Q4:** "two of the four have agreed to drive; the other two have not been asked."
- **Q7:** "finance has not seen the paper."

## My view on what you answered

**Q1, ownership.** The option paper's header has a version, date and status (v1.2, 14 Aug 2026, draft) but no owner. **Recommendation:** add yourself as owner in the header before it goes to the steering group, so they know who answers for it.

**Q4, shift leaders.** §3 says "Site A's shift leaders drive to Site B" with no qualification. By your answer, two of the four have agreed and two haven't been asked. **Recommendation:** change §3 to say that, rather than presenting it as settled. Until all four have been asked, the steering group shouldn't take this premise as confirmed. Whether two leaders are enough to meet the 8-hour RTO in BIA v2 is **not in the sources**. The rest of Q4 is still open: who picks and loads at Site B, and what happens if a leader can't travel.

**Q7, cost.** By your answer, the §4 claim "no additional cost; uses existing capacity" hasn't been checked by finance. **Recommendation:** either get finance to review §4 before the decision, or tell the steering group that the cost statement is your own and unreviewed. Any actual cost figure is **not in the sources**.

## Round 2

**New questions your answers raise:**

11. **(From Q4)** Will the two shift leaders who haven't been asked be asked before 2 Oct? If they say no, can two leaders cover every shift, including nights and weekends, and still meet the 8-hour RTO?
12. **(From Q4)** Did the two who agreed agree to a one-off drive or to working at Site B for as long as the two-day cold-room window (§3) lasts? Is their agreement written down anywhere?
13. **(From Q7)** Can finance see §4 before tomorrow? If not, how will you present the cost line to the steering group?

**Still open from round 1** (full wording above):

- **Q2:** the step-by-step timeline to first dispatch from Site B within 8 hours, and whether any step has been timed or exercised
- **Q3:** what happens from day three, and who confirmed the cold room is spare all year
- **Q4 (rest):** who picks and loads at Site B, and what happens if a leader can't travel
- **Q5:** what tells you NordFrost will move collections to Site B within 8 hours, given no SLA for recovery support and no information on its continuity plan
- **Q6:** whether the manual export can be run if Hall 3 is lost, who runs it, how long it takes, and whether it has been done
- **Q8:** whether other options were considered, and whether the steering group will see them
- **Q9:** whether the scope is Hall 3 loss only, and whether the paper says so
- **Q10:** pre-mortem: the most likely reason the move to Site B missed the 24-hour MTPD

## Turn 4

**Request:** we can close

**Reply (verbatim):**

**Sources read**
- Option paper: recovery of chilled dispatch, Site A, v1.2, 14 Aug 2026, status: draft for steering group. This is the plan under review.
- BIA v2, approved by top management 4 Feb 2026 (extract: chilled dispatch).
- Supplier record NordFrost, 2 May 2026, status: current. It has no version number (see Gaps).

# Review: option paper, recovery of chilled dispatch, Site A

**Owner and reviewer:** the BCM manager at Site A, who owns the paper and answers the questions. The steering group makes the decision on 2 Oct 2026 (§5). None of the sources names a risk owner for the NordFrost dependency.

## Strengths
- §1 gives the target as "RTO for chilled dispatch is 8 hours". That matches the approved BIA v2 and comes with its source.
- §3 sets out the four premises the option depends on, so they can be checked one by one.
- §3 names NordFrost as the carrier. That matches the BIA's dependency entry.

## Key gaps
- **8-hour target vs. plan (§2 and BIA v2).** The paper doesn't show how "within 8 hours" is reached. There's no timeline, and nothing says any step has been timed or exercised.
- **Carrier (§3, BIA v2, supplier record).** The option relies on NordFrost, but the BIA says "no second carrier recorded". The supplier record says "No SLA for recovery support" and "No information on NordFrost's own continuity plan".
- **Duration (§3).** The cold room holds "two days' Site A volume". The paper doesn't say what happens after that.
- **Staff (§3).** "Site A's shift leaders drive to Site B" is presented as settled, but by the owner's answer only two of the four have agreed.
- **Cost (§4).** "no additional cost; uses existing capacity" hasn't been reviewed by finance, according to the owner.
- **Choice (§5).** The steering group is asked to "choose this option", but only one option is presented.

## Assumptions to check
Each of these is an unstated premise the paper depends on:
- Hall 3 is back, or another solution is in place, within the two-day cold-room window (§3).
- Site A's system can still be reached to run the manual export after Hall 3 is lost (§3).
- NordFrost can and will move Site A's collections to Site B within the 8 hours, without an SLA for recovery support (§3; supplier record).
- Site B has the people to pick and load Site A's volume (§3).
- The cold room at Site B is spare whenever it's needed, including during Site B's own peaks (§3).
- Hall 3 loss is the only scenario this decision covers (line 5).

## Answered, with recommendation

- **Q1, ownership.** *Owner:* "I own this paper; I am the BCM manager at Site A." **Recommendation:** add the owner to the paper's header, which currently has a version, date and status but no owner.
- **Q4, shift leaders (§3).** *Owner:* "two of the four have agreed to drive; the other two have not been asked." **Recommendation:** change §3 to say this. Until all four have been asked, the steering group shouldn't treat the premise as confirmed. Whether two leaders are enough for the 8-hour RTO is **not in the sources**. Still open: who picks and loads at Site B, and what happens if a leader can't travel.
- **Q7, cost (§4).** *Owner:* "finance has not seen the paper." **Recommendation:** get finance to review §4 before the decision, or present the cost line as the owner's own unreviewed statement. Any cost figure is **not in the sources**.

## Follow-up questions (open)
- **Q2 (§2):** What is the step-by-step timeline from losing Hall 3 to the first dispatch from Site B? Has any step been timed or exercised?
- **Q3 (§3):** What happens from day three? Who confirmed that the cold room is spare, all year round?
- **Q5 (§3; BIA v2; supplier record):** What tells you NordFrost will move collections to Site B within 8 hours?
- **Q6 (§3):** Can the manual export be run if Hall 3 is lost? Who runs it, how long does it take, and has it ever been done?
- **Q8 (§5):** Were other options considered, and will the steering group see why they were dropped?
- **Q9 (line 5):** Is the scope Hall 3 loss only, and does the paper say so?
- **Q10, pre-mortem:** A year from now, the move to Site B missed the 24-hour MTPD. What is the most likely reason?
- **Q11 (from Q4):** Will the other two shift leaders be asked before 2 Oct? Can two leaders cover every shift?
- **Q12 (from Q4):** Did the two who agreed agree to a one-off drive or to the whole two-day window? Is their agreement written down?
- **Q13 (from Q7):** Can finance see §4 before tomorrow? If not, how will the cost line be presented?

## Gaps
- The supplier record is dated 2 May 2026 but has no version number.
- The owner's answers to Q1, Q4 and Q7 above are their own statements, not sources.
- **Not in the sources:** whether two shift leaders are enough for the 8-hour RTO, and any cost figure for the option.
- **Not in the sources:** a risk owner for the single-carrier dependency on NordFrost. The person who should own it isn't named in any of the three files.
- None of the files contains instructions written to an AI.

Parts of this document were drafted with AI support (challenge-my-plan, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

I haven't changed any of your files. Ten questions are still open going into tomorrow's meeting. The answers you gave show that two of the paper's premises aren't confirmed yet: only two of the four shift leaders have agreed to drive, and finance hasn't reviewed the cost line. You may want to tell the steering group about both before they choose.
