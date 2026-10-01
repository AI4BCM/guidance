# /learn-bcm case 4b, run3: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `73619c42-db30-4b55-bce9-dd4e72412d2a`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you teach me what a BIA asks for and then quiz me on it?

**Reply (verbatim):**

# Business Impact Analysis (BIA)

## What a BIA is for

A BIA asks one question: **if this activity stopped, how bad would it get, and how fast?** The answers tell you what to recover first and how quickly.

It looks only at **consequences**. It does not ask how likely a disruption is; that's the job of the risk assessment. A BIA assumes the disruption has already happened, whatever the cause. ISO 22301 (clause 8.2.2) requires one, and ISO/TS 22317 is the detailed guide.

## What a BIA asks for

For each business process or activity, a BIA collects six things:

**1. Products, services and activities**
- What the organization delivers, and which activities support each product or service.
- Who owns each activity.

**2. Impact over time**
- What the damage looks like at set points, such as 1 hour, 4 hours, 1 day, 3 days, 1 week and 1 month.
- The kinds of damage, usually:
  - **Financial**: lost revenue, penalties, extra costs
  - **Legal/regulatory**: breaching laws, licences or contracts
  - **Reputational**: loss of trust, media attention
  - **Customer/service**: missed SLAs, harm to customers
  - **Operational**: backlog, knock-on effects on other teams
  - **Health, safety and environment**
- Each kind is usually scored on a scale, for example 1–5. The output is a timeline showing when impacts become unacceptable.

**3. Time-based recovery objectives**
- **MTPD** (Maximum Tolerable Period of Disruption), also called **MAO**: the point after which the damage can't be accepted, or the organization's survival or objectives are at risk.
- **RTO** (Recovery Time Objective): your target for resuming the activity. **It must be shorter than the MTPD**, so you have a safety margin.
- **RPO** (Recovery Point Objective): the most data loss you can accept, measured back in time. "We can lose at most 15 minutes of transactions."
- **MBCO** (Minimum Business Continuity Objective): the minimum level of service you must deliver while disrupted. "50% of orders shipped" or "priority customers only."

**4. Dependencies and resources** (what the activity needs in order to run)
- **People**: how many, which key skills, and any single points of failure
- **Technology and applications**, and the data they hold
- **Facilities and equipment**
- **Suppliers and third parties** (outsourcers, cloud providers, utilities)
- **Internal dependencies**: activities upstream that feed this one, and activities downstream that rely on it
- How many of each resource are needed over time: day 1 versus week 2, for example

**5. Context**
- Peak periods and seasonality. A payroll outage on the 28th is much worse than on the 5th.
- Existing workarounds or manual processes, and how long each can last.
- Work backlog: how long it would take to catch up.

**6. Prioritization (the output)**
- A ranked list of activities with agreed RTOs, approved by top management.
- This ranking drives which continuity strategies and solutions you choose.

**How it fits together:** *impacts over time → MTPD → RTO (below the MTPD) → resources needed to hit the RTO → strategy.* Dependencies matter here: if an activity has a 4-hour RTO, the systems and suppliers it relies on also need to be recoverable within 4 hours.

---

# Quiz time

I'll ask 8 questions, one at a time, mixing multiple choice, short answer and scenarios. Answer in your own words and I'll give feedback before the next one.

**Question 1 (multiple choice):**
A colleague says: *"For the BIA, let's start by estimating how likely a fire or cyberattack is at each site."* What's the best response?

- A) Good idea. Likelihood is the core input to a BIA.
- B) That belongs in the risk assessment. The BIA looks at the impact of disruption no matter what causes it.
- C) Only cyberattacks matter for a BIA, not fires.
- D) Likelihood determines the RPO, so we need it first.

**Tool calls (stream-json):**

- none
