Skill sha: c65da4bbcfbe393c6001a22a4891ece98caacab0
Stage unit: units/stages/analysis.md

| Unit item | Skill line | Verdict |
|---|---|---|
| One control | "A resource requirement drafted by AI is only a question for the activity owner. It goes into the register only when the owner confirms it." "Recovery fields stay empty in anything AI produces." (`prepare-bia/SKILL.md:14`) | carried |
| Method 1 | "**Fix the sources you will attach, and their dates.** The prompt's Intake asks the organiser, in one message, what the material leaves open: the interviewee's role, what they know the organiser does not, what you need back, and the impact criteria if none are attached, and that memory, past chats, project files, connectors and web search are switched off. Their answers go under Gaps as "own statements, not sources", never a value or a Source entry; any channel left on goes under Gaps too, since "the model may draw on it without saying so"." (`prepare-bia/SKILL.md:19`) | carried |
| Method 2 | "**Draft before interviewing (activities, resource requirements, questions, recovery fields blank).** Run the Task choice, then order the guide as seven numbered sections" … "MTPD, RTO and RPO stay empty. A single supplier, carrier or person behind a resource is a question for the activity owner, not a finding." (`prepare-bia/SKILL.md:24`, `:35`) | carried |
| Method 3 | "**Interview.** Tell the owner to "use the draft as the thing to correct, not the thing to confirm; record what it could not have known"." (`prepare-bia/SKILL.md:37`) | carried |
| Method 4 | "**Compare registers across sites.** Name each conflict between the attached sites and put it "to the two owners, not to the model"." (`prepare-bia/SKILL.md:39`) | carried |
| Method 5 | "**Hand the register on with the confirmed and unconfirmed marks intact.** Every entry stays labelled "candidate, to confirm"." (`prepare-bia/SKILL.md:41`) | carried |
| Interview order 1, impacts over time | "1. impacts over time;" (`prepare-bia/SKILL.md:26`) | carried |
| Interview order 2, the MTPD | "2. the MTPD;" (`prepare-bia/SKILL.md:27`) | carried |
| Interview order 3, people with their skills, authorities and mandates | "3. people, "with the skills, authorities and mandates the work needs";" (`prepare-bia/SKILL.md:28`) | carried |
| Interview order 4, seats and buildings | "4. seats and buildings;" (`prepare-bia/SKILL.md:29`) | carried |
| Interview order 5, IT and applications, each with RTO and RPO | "5. IT and applications, "each with its RTO and its RPO";" (`prepare-bia/SKILL.md:30`) | carried |
| Interview order 6, suppliers and other third parties | "6. suppliers and other third parties;" (`prepare-bia/SKILL.md:31`) | carried |
| Interview order 7, dependencies as their own item | "7. dependencies, as their own section: "up- and downstream relationships with other departments, each recorded with the RTO the relationship carries"." (`prepare-bia/SKILL.md:32`) | carried |
| Task choice 1 | "[`../units/prompts/bia.md`](../units/prompts/bia.md), first in its Task line: "draft candidate activities, their resource requirements and interview questions for the site in the attached material". Keep its Intake, Output, Gaps and Cite as written." (`prepare-bia/SKILL.md:48`) | carried |
| For the auditor | "The register carries "the source, the interview it came from and the date behind each entry". In the pre-interview draft three fields stay blank: the interview, the confirmation date and "the recovery times the owner set"." (`prepare-bia/SKILL.md:54`) | carried |
| Reviewer | "The activity owner confirms each requirement and sets MTPD and RTO. "Top management approves the BIA results." Name both in the draft." (`prepare-bia/SKILL.md:59`) | carried |
| Hand-over | "> After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA." written "Just before the preflight's AI-help sentence" (`prepare-bia/SKILL.md:44`, `:42`) | carried |

Every row is carried, so there is no weakened or absent row to write up. Four rows needed a judgement rather
than a word match, and the reasoning is recorded here.

**Method 1.** The unit's step has two halves. The off state is carried in the skill's own words: the unit works
from "memory, past chats, project files, connectors and web search switched off", and the skill asks the organiser
for all five, project files included, with the Gaps note as the fallback for any left on and the unit's own reason
("the model may draw on it without saying so"). The other half, the sources and their dates, is carried by the
heading quoted verbatim, by the preflight the skill runs first (step 3, "Name each source's version and date") and
by the Task choice's Output, kept as written, which opens with the source documents and their dates.

**Task choice 1.** The prompt's Intake allows "at most three questions the attached material leaves open", and the
skill's Method 1 lists four items plus the switched-off confirmation. They fit: the interviewee's role and what
they know the organiser does not are one question, what you need back is the second, the impact criteria the third
and conditional, and the channel confirmation is not a question about the material. A manager running the skill
sends one message within the Intake's limit, which is what the eval case asks for.

**Method 3.** The unit addresses the analyst: use the draft as the thing to correct, not the thing to confirm. The
skill, which stops at the pre-interview draft, can only carry the step by writing that instruction into the draft,
and it addresses the activity owner. That is the right addressee for this skill: the owner is the person whose
confirmation puts an entry in the register, so the owner is the person whose rubber-stamping the step guards
against (IMDA section 2.2.2, cited in the unit's own source list for this rule).

**For the auditor.** The unit's paragraph has a register half and a risk half. The skill carries the register half
and names which three of those fields are necessarily blank before any interview. The risk half is deliberately
out of scope: this skill runs the BIA draft, and the unit itself puts risk outside the BIA method ("The BIA method
does not cover risk assessment").
