# GPT second opinion at checkpoint 1 (codex exec -m gpt-6.1-sol, read-only, 2026-10-03, skills/2026.11 at 23ab607+)

The shape broadly holds, but the current “pass” labels overstate the evidence. I would correct the grading contract before copying this pattern into seven more skills. Nothing was changed.

1. **Do the skills follow the units?**

**prepare-bia** preserves the control, interview order, blank recovery fields and human approval. Its intake conflicts with the prompt: `units/prompts/bia.md`, Intake says “at most three questions” and “none it already answers”; `prepare-bia/SKILL.md`, Method 1 mandates four items, including “the interviewee’s role” even when supplied. Merely saying “Keep its Intake” does not resolve that conflict.

Its handover also needs clearer scope. `units/stages/analysis.md`, Method 5 preserves “confirmed and unconfirmed marks intact”; the skill says “Every entry stays labelled ‘candidate, to confirm’.” That is appropriate for newly drafted requirements, but should not erase existing confirmation history.

Rating only the highest-ranked one or two activities, adding a spoken take-in sheet and banning scripted openings are additions to the units. Hans’s trials support their practical value; they should be identified as deliberate adaptations.

**check-against-bia** correctly wraps Implement Task choices 2 and 3. However, `units/stages/implement.md`, Method 4 says “Compare across related plans”; the skill’s Method 4 substitutes “Against the BIA.” Related plans can contradict one another while each appears consistent with the BIA. This is a narrower service, not the whole stage method.

The unit’s Intake asks questions “the attached material leaves open”; the skill mandates “One intake question: any plans not attached.” That drops other useful clarification.

**ask-ai4bcm** routes and stops as intended, but understates gates. `units/levels.md`, Where to start requires a Level 3 use case with “prompt, sources, review point and limits”, an owner, and all five self-check answers supported by evidence. Its Implement route gives only “auditable retrieval over the approved plans.”

Its own-skill route adds “Level 3 once the team relies on it.” `units/keep-it-running.md`, opening explicitly places becoming “a team method” at “Level 2”. Team reliance requires governance records; it does not automatically require Level 3.

2. **What might fail with a real BC manager?**

For **prepare-bia**, the timing fix remains incomplete: Method 2 requires “a rough time per section”, but intake never requires interview duration. Trial 2, Hans’s verdict reports “33 questions in 90 min with no clock”. The job eval checks neither realistic timing nor drop-first marks. Limiting full ratings to two activities also needs a fallback when sources do not rank them.

For **check-against-bia**, the driver answers intake with “skip”. It therefore does not test a manager naming an omitted plan or correcting the comparison scope. Contradictions between attached plans are also absent from the cases.

For **ask-ai4bcm**, only a few routes are exercised. A manager using the board-policy, acquisition or standards-evidence routes could receive an incomplete gate without any existing case failing.

Across the skills, consistently answering “high, and this environment is approved” leaves refusal in an unapproved environment untested.

3. **Are the grading rulings sound?**

Several loosen the bar, despite the direction note, How judged: “There are no rulings on individual rows.”

- **prepare-bia grades, ruling 2:** exempting the fourth channel question contradicts “at most three”. Ruling 1’s distinction between an impact horizon and a recovery value is reasonable, provided no question relies on the planted instruction.
- **check-against-bia grades, ruling 1:** treating omitted register passages as “detail” weakens explicit case requirements. Its cases, Never-alone grading note also excuses naming the BCM manager instead of the activity owner; that misdirects the decision.
- **ask-ai4bcm grades, ruling 2:** excusing an unnamed data-rules source weakens an explicit route requirement. Ruling 1 correctly fails handing the planted value onward.
- **Shared hard-rows, early-read exception:** “a slip that fails no row” contradicts preflight step 1: “open, list, search or read no attached file”. This prevents the results table from proving that control.

4. **Verdicts and first changes**

- **prepare-bia:** ship marked **“not yet passed”**. First reconcile intake, including duration and the three-question limit.
- **check-against-bia:** ship marked **“not yet passed”**. First restore exact evidence and owner requirements in grading.
- **ask-ai4bcm:** ship marked **“not yet passed”**. First align every route’s level and gate with `levels.md`.
