# /learn-bcm case 4b, run1: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `cbf59a1b-d5af-42fc-94a0-062172f8503c`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you teach me what a BIA asks for and then quiz me on it?

**Reply (verbatim):**

# Business Impact Analysis (BIA)

A BIA asks one central question: **if this activity stopped, how bad would it get, how quickly, and what would we need to restart it?**

It does not ask what might cause the disruption. That's the job of the risk assessment. The BIA works the same way whether the cause is a fire, a ransomware attack or a supplier going bankrupt. In ISO 22301 terms, the BIA (clause 8.2.2) and the risk assessment (8.2.3) are separate steps that feed the continuity strategy.

## What a BIA asks for

**1. Scope and context**
- Which products and services are in scope?
- Which activities (processes) deliver them, and who owns each one?

**2. Impact over time**
For each activity, the BIA asks what happens if it stops for 1 hour, 4 hours, 1 day, 3 days, 1 week, 2 weeks and 1 month. Impacts are scored against agreed categories, usually:
- Financial (lost revenue, penalties, extra costs)
- Operational (backlog, knock-on effects on other activities)
- Legal and regulatory (breaches, fines, licence risk)
- Contractual (SLA breaches)
- Reputational and customer
- Health, safety and environmental

Everyone scores against the same impact scale (for example 1–5 with defined thresholds), so results can be compared across departments.

**3. The key time and recovery figures**
| Term | Question it answers |
|---|---|
| **MTPD** (Maximum Tolerable Period of Disruption, also called MAO) | How long until the impact becomes unacceptable or threatens the organisation? |
| **RTO** (Recovery Time Objective) | How fast must we resume the activity? It must be **shorter than the MTPD**, to leave a safety margin. |
| **RPO** (Recovery Point Objective) | How much data can we afford to lose, measured in time back from the incident? |
| **MBCO** (Minimum Business Continuity Objective) | What is the minimum acceptable level of service while we're degraded? For example, "50% of orders processed". |

**4. Dependencies and resources**
What does the activity need to run, and how much of it is needed over time (day 1 vs. day 3 vs. week 2)?
- **People:** headcount and key skills, including single points of knowledge
- **IT:** applications, systems, data
- **Premises and equipment**
- **Information and vital records**
- **Suppliers and partners:** external dependencies
- **Internal dependencies:** upstream activities it relies on, and downstream ones that rely on it

**5. Other context**
- Peak periods or seasonality (month-end, tax season, holidays)
- Manual workarounds, and how long they can last
- Backlog: how long it takes to catch up after recovery

**6. Validation**
Top management reviews and signs off the results, especially the prioritisation. The outputs are a ranked list of prioritised activities, their RTOs and resource needs. Those drive the continuity strategy and plans.

---

# Quiz

I'll ask one question at a time and give feedback after each answer. There are 8 questions.

**Question 1:** A colleague says, "Let's start the BIA by listing the threats we face, like floods, cyberattacks and pandemics." What's wrong with that approach, and what should the BIA focus on instead?

**Tool calls (stream-json):**

- none
