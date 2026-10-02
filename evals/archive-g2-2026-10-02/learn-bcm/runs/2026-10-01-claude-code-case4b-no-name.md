# learn-bcm case4b-no-name, Claude Code 2.1.284, 2026-10-01

Files in the run folder: nothing attached. Command: `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed, later turns with `--resume`.

stream-json; (a) is evidenced by case 1 turn 1.

## Turn 1

Session `406b4b31-cae9-4705-90ea-d6374914e4e1`. Request:

```text
Can you teach me what a BIA asks for and then quiz me on it?
```

Tool calls: none

Final text:

````markdown
# What a Business Impact Analysis (BIA) asks for

A BIA answers one question: **if this activity stopped, how bad would it get, how fast, and what would we need to get it running again?** It looks at the effects of a disruption. It doesn't ask what causes disruptions, because that's the job of the risk assessment. ISO 22301 (clause 8.2.2) and ISO/TS 22317 describe the standard approach.

## 1. Scope: what are we analysing?
- **Products and services** the organisation delivers, starting with the ones that matter most.
- **Activities and processes** that deliver them. The BIA is usually done process by process, with each process owner interviewed.
- **Process owner** and a short description of what the process does.

## 2. Impact over time
This is the core of the BIA. For each activity it asks how the impact grows the longer the outage lasts, usually measured at set points such as 4h, 1 day, 3 days, 1 week and 1 month. Impact categories usually include:
- **Financial:** lost revenue, penalties, extra costs
- **Operational:** backlog, knock-on effects on other teams
- **Legal / regulatory / contractual:** breached SLAs, fines, licence risk
- **Reputational:** customer trust, media attention
- **Customer / stakeholder:** harm to the people you serve
- **Health, safety and environment**

Each category is scored against a shared impact scale, such as 1–5 with defined thresholds. The shared scale lets you compare scores across departments.

## 3. Time-based recovery objectives
| Term | Question it answers |
|---|---|
| **MTPD / MAO** (Maximum Tolerable Period of Disruption / Maximum Acceptable Outage) | After how long would the impact become unacceptable or threaten the organisation? |
| **RTO** (Recovery Time Objective) | How quickly must we resume the activity? It **must be shorter than the MTPD** to leave a safety margin. |
| **MBCO** (Minimum Business Continuity Objective) | What is the minimum level of output we must reach when we resume (e.g. 60% of orders, priority customers only)? |
| **RPO** (Recovery Point Objective) | How much data can we afford to lose, measured back in time (e.g. the last 4 hours of transactions)? |

## 4. Dependencies and resources
These are the things needed to deliver the activity at the MBCO:
- **People:** minimum headcount and key skills, including single points of failure ("only Maria knows how to do this")
- **Premises / facilities**, and whether the work can be done remotely
- **IT systems, applications and data**, each with its own RTO and RPO
- **Equipment and supplies**
- **Suppliers and third parties**, plus whether you have alternatives
- **Internal dependencies:** upstream activities you rely on and downstream activities that rely on you

## 5. Context and constraints
- **Peak periods and seasonality,** such as month-end or holidays. An outage during a peak hurts more.
- **Existing workarounds,** such as manual processes, and how long they can last.
- **Vital records** and where they're kept.

## 6. Outputs
- A **prioritised list of activities**, ordered by RTO.
- Resource requirements that feed into your continuity strategies and solutions.
- **Management sign-off.** Top management has to agree the priorities and objectives.

**A common trap:** the BIA does not ask how likely a disruption is. Likelihood belongs to the risk assessment. The BIA assumes the disruption has already happened and measures the consequences.

---

# Quiz time 🎯

I'll ask one question at a time and give feedback after each answer. There are 8 questions, getting harder as we go.

**Question 1:** A process owner says: *"If our payroll system goes down, we'd survive about 5 days before employees aren't paid and we breach employment law."* Which BIA term does that 5 days describe, and what does it tell you about the RTO?
````
