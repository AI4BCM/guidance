# /learn-bcm case 4b, run2: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `894ee78a-1fca-4298-aa74-c52fcb7b2b4e`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you teach me what a BIA asks for and then quiz me on it?

**Reply (verbatim):**

# What a Business Impact Analysis (BIA) asks for

A BIA answers one question: **if this activity stopped, how bad would it get, and how quickly?** It looks at the **impact** of a disruption, whatever caused it. Fire, ransomware and a supplier going bust all count the same. That's the main difference from a **risk assessment**, which looks at threats and how likely they are.

In a typical BIA questionnaire or workshop (ISO 22301 / ISO/TS 22317), each business unit is asked for the following.

## 1. Products, services and activities
- What do you deliver, and which activities support it?
- Who are the customers, internal and external?

## 2. Impact over time
Impact is scored at set time intervals, for example 1 hour, 4 hours, 1 day, 3 days, 1 week and 1 month, across these categories:
- **Financial:** lost revenue, penalties, extra costs
- **Operational:** backlog, knock-on effects on other teams
- **Legal / regulatory:** breaches, fines, licence risk
- **Reputational:** media attention, loss of customer trust
- **Customer / contractual:** missed SLAs
- **Health, safety and welfare**

Impact usually **gets worse over time**. The point where it becomes unacceptable is what drives the recovery targets.

## 3. Recovery objectives (the key numbers)
| Term | Meaning |
|---|---|
| **MTPD** (Maximum Tolerable Period of Disruption, also called MAO) | How long before the impact becomes unacceptable or threatens the organisation's survival |
| **RTO** (Recovery Time Objective) | The target time to resume the activity. It **must be shorter than the MTPD** |
| **RPO** (Recovery Point Objective) | How much data you can afford to lose, measured backwards from the disruption |
| **MBCO** (Minimum Business Continuity Objective) | The minimum acceptable level of service while you're disrupted, e.g. 50% of orders processed |

## 4. Dependencies and resources
- **People:** how many staff, which key skills, single points of knowledge
- **IT:** applications, systems and their own RTOs/RPOs
- **Data and vital records**
- **Premises and equipment**
- **Suppliers / third parties:** do their recovery times match yours?
- **Internal upstream and downstream dependencies:** who you rely on, and who relies on you

It also asks **how many resources you need over time**, for example 2 staff on day 1 and 6 by day 5.

## 5. Context
- **Peak periods and seasonality:** month-end, tax season, holidays
- **Workarounds:** manual alternatives, and how long they can be kept up
- **Backlog:** how long it takes to clear the build-up once you've recovered

**The output:** a ranked list of **prioritised activities** with their RTO, RPO, MTPD and resource needs. This feeds directly into continuity strategies and plans.

---

# Quiz time 🎯

I'll ask one question at a time and give feedback after each.

**Question 1:** A payroll team says: *"If we're down for 3 days, staff don't get paid and we breach employment law. That's the absolute limit."* They also say they want to be back up within 1 day.

Which of those figures is the **MTPD** and which is the **RTO**? Why does the order between them matter?

**Tool calls (stream-json):**

- none
