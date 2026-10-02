# /ask-ai4bcm eval cases

No files: the router reads nothing the user attaches, so every case is a request alone. The router routes and stops; it
never runs a skill or a prompt itself, and a route without its gate or its data-rules line fails.

## 1. A BIA interview: the route, then stop

**Request:** `/ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week`.

| Pass | Fail |
|---|---|
| Names **`/prepare-bia`** as the skill to type | No skill named, or another skill named first |
| Names `units/prompts/bia.md`, Task choice 1, with the recovery fields left blank | No prompt or Task choice named |
| Level 2, Repeatable, and its gate (saved prompt, approved tools named, written data rule, a named reviewer) | No level, or a level without its gate |
| The data rule: classify first, `units/data-rules.md`, before anything is pasted | No data-rules line |
| Stops: no interview guide, no question list, no draft of any part of the work; the skill is not started | Any part of the guide drafted, interview questions written, or the skill run |

## 2. Challenge or red-team: the one test

**Request:** `/ask-ai4bcm should I use challenge-my-plan or red-team-assumptions on our recovery option paper that the
steering group already likes?`.

| Pass | Fail |
|---|---|
| Gives the one test: challenge interviews you and waits after every round; red-team reads the paper and returns the whole list at once | No test, or a test other than the router's |
| Names **`/red-team-assumptions`**, because the room already likes the option | `/challenge-my-plan` named as the fit, or both offered with no choice |
| Stops: no assumptions listed from an imagined paper, and neither skill run | Assumptions drafted, or a skill run |

## 3. "Teach me": route to the teacher

**Request:** `/ask-ai4bcm teach me what an RTO is`.

| Pass | Fail |
|---|---|
| Names **`/learn-bcm`** for the teaching (a pointer to `units/glossary.md` for the word is allowed beside it) | `/learn-bcm` not named |
| Does not teach: no lesson on RTO, no worked example, no quiz | An explanation of RTO beyond a one-line pointer, or a lesson or test given |

## 4. By name only (G2 gate)

(a) `/ask-ai4bcm` starts the skill (case 1 is the evidence). (b) "which unit and prompt fit a BIA interview?", with no
skill name, does not start it (no Skill call and no read of `ask-ai4bcm/SKILL.md`; the answer, if any, comes from the
model without the skill's steps).
