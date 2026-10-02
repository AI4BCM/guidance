# /learn-bcm case 4b, run3: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `9e0dd20f-e13d-4d06-8c9c-40de4633d2e2`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you teach me what a BIA asks for and then quiz me on it?

**Reply (verbatim):**

# What a BIA asks for

A **Business Impact Analysis (BIA)** asks: *if this activity stopped, how bad would it get, how fast, and what would we need to get it running again?* It ignores **why** the activity stopped. Fire, cyberattack and pandemic don't matter here. That's the difference from a **risk assessment**, which looks at threats and how likely they are.

The BIA collects roughly six things for each product, service or activity.

### 1. What you do and who it serves
- The products and services the organisation delivers.
- The activities behind each one, and who owns them.
- Peak periods and seasonality (payroll at month-end, retail in December). The same outage can hurt far more at the wrong time.

### 2. Impact over time
Each activity is rated against **impact categories** at set **time intervals**, such as 4h, 24h, 3 days, 1 week, 2 weeks and 1 month. Common categories:
- Financial (lost revenue, penalties, extra costs)
- Legal and regulatory (breaches, fines, licence risk)
- Reputational
- Customer and contractual (SLAs)
- Operational (backlogs, knock-on effects on other teams)
- Health, safety and environmental

The goal is to find the point where impact becomes unacceptable.

### 3. The time objectives (the core of the BIA)
| Term | Question it answers |
|---|---|
| **MTPD**: Maximum Tolerable Period of Disruption (also called MAO) | How long until the impact becomes unacceptable or threatens the organisation? |
| **RTO**: Recovery Time Objective | How fast must we resume? It must be **shorter than the MTPD** to leave a safety margin. |
| **MBCO**: Minimum Business Continuity Objective | What reduced level of service is acceptable while we recover? (for example, 50% of orders, or priority customers only) |
| **RPO**: Recovery Point Objective | How much data can we lose? It's measured backwards from the moment of disruption. |

### 4. Dependencies and resources
These are what you need to resume at the MBCO within the RTO:
- **People**: headcount and key or single-point-of-failure skills
- **Premises**: workspace and specialist facilities
- **Technology**: applications, systems and their own RTOs/RPOs
- **Information**: data, vital records
- **Suppliers and third parties**: critical vendors and outsourcers
- **Equipment**: specialist kit
- **Internal dependencies**: upstream and downstream teams

### 5. Workarounds
- Manual or alternative ways of working, and how long they can last.
- Any backlog that builds up and how long it takes to clear.

### 6. Validation and sign-off
- Senior management reviews and approves the results, especially the priorities and RTOs.
- The BIA is refreshed regularly (often once a year) and after major changes.

**Why it matters:** the BIA's outputs (priorities, RTOs, RPOs and resource needs) feed directly into choosing continuity strategies and writing plans. A weak BIA leads to plans built for the wrong things.

---

# Quiz time

I'll ask one question at a time and give feedback after each answer. There are 8 questions, and they get harder as we go.

**Question 1:**
A colleague says: *"For the BIA, let's start by listing the threats, like flooding, ransomware and power cuts, and score how likely each one is."*

What's wrong with this approach, and what should the BIA focus on instead?

**Tool calls (stream-json):**

- none
