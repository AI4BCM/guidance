# /challenge-my-plan case 5b, run3: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `26ce317c-eca3-487a-88c0-04f78a00486a`.

Files in the working folder: `bia-extract-dispatch.md`, `option-paper-dispatch.md`, `supplier-record-nordfrost.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you ask me the hard questions about this recovery option before the steering group meets tomorrow? The files option-paper-dispatch.md, bia-extract-dispatch.md and supplier-record-nordfrost.md in this folder are attached.

**Reply (verbatim):**

I read all three files. The questions are ordered by how badly each one could hurt the paper tomorrow. The biggest problems are the first two groups, because the BIA and supplier record you attached already weaken them.

## 1. Can it actually be done in 8 hours?

- **Has anyone timed this, or is "within 8 hours" a target?** Lay out the timeline: Hall 3 is lost → someone decides to invoke → shift leaders are called → 140 km drive (about 2 hours in good conditions, longer at night or in winter) → Site B is set up → manual export → first chilled load leaves. When does the clock start, and what is left of the 8 hours by the time the leaders arrive?
- **Who can invoke the plan, and how fast?** If invoking needs a meeting, you lose an hour or two before anything moves.
- **Has any of this been tested?** Even a walkthrough on paper would count. If the answer is no, the honest wording is "aims for 8 hours, not tested."

## 2. NordFrost is the weak point, and the paper treats it as a strength

- **The BIA already flags NordFrost as a single dependency with no second carrier.** The option makes that dependency bigger. The supplier record says there is **no SLA for recovery support** and **nothing is known about NordFrost's own continuity plan**. So what supports the claim that NordFrost will move collections to Site B at a few hours' notice?
- **Has anyone asked NordFrost** whether they have vehicles and drivers to collect Site A's volume at Site B on top of Site B's normal volume?
- **"Serves both sites" is a common-mode failure, not a backup.** If NordFrost fails, both sites stop. What is the fallback carrier, if there is one?

## 3. The capacity and people assumptions

- **Who confirmed that Site B's cold room is "spare", and when?** Is it spare in Site B's peak season too? Has the Site B site manager signed up to give it away for this?
- **Two days' volume, then what?** The MTPD is 24 hours, so two days covers the first stretch. But losing Hall 3 is unlikely to be a 48-hour event. What happens on day 3, and in week 2?
- **Is it only the shift leaders who drive to Site B?** Who does the picking and loading? If it's Site B staff, what happens to Site B's own work? If it's Site A staff, are they in the plan, and are they contractually able to work 140 km away at short notice?
- **What if the incident also affects people,** such as injuries, evacuation, or a night shift with nobody available?

## 4. The systems link

- **Where does the "manual export" come from?** If Site A's warehouse system or its servers sit in or depend on Hall 3, the export may not be possible at all.
- **Who does the export, how long does it take, and has it been done once end to end?** That includes labels, order status, and routing back to customers.

## 5. The cost line will get challenged

"No additional cost" is very hard to defend. At minimum the paper leaves out:

- overtime, travel and accommodation
- NordFrost's extra mileage or surcharges, which aren't covered by any SLA
- Site B work that gets displaced
- the cost of keeping that cold room empty instead of using it

Saying "low cost, not yet estimated" is safer than "no cost."

## 6. Customers and product

- **Do deliveries from 140 km further away still meet customer delivery windows** and the product's chilled shelf life?
- **Is stock lost with Hall 3,** or is there stock in transit that has to be moved too?

## 7. What the steering group is really being asked

- **Only one option is presented.** What alternatives were considered and rejected? Examples: a second carrier, mobile refrigerated trailers at Site A, or a third-party cold store nearer to Site A. Without them, "choose this option" is really "approve this or nothing."
- **Would it be more defensible to ask for approval in principle, conditional on a test** and on a NordFrost commitment, rather than a final choice?
- **Who owns the residual risk** that NordFrost remains a single point of failure?
- **Is the paper current?** v1.2 is dated 14 Aug and the supplier record 2 May. Has anything changed since then?

---

**If you only prepare for three questions:**

1. "Show me the 8-hour timeline."
2. "What has NordFrost agreed to?"
3. "Why do you say this costs nothing?"

Do you have answers to those? If you tell me what you know, I can help you tighten the paper or draft a short set of conditions to attach to the decision.

**Tool calls (stream-json):**

- Bash: `ls -la && cat option-paper-dispatch.md bia-extract-dispatch.md supplier-record-nordfrost.md`
