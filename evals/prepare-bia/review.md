Skill sha: eabbb94b5a24825e34acb7cb558b97877387095f
Stage unit: units/stages/analysis.md

| Unit item | Skill line | Verdict |
|---|---|---|
| One control | "A resource requirement drafted by AI is only a question for the activity owner. It goes into the register only when the owner confirms it." "Recovery fields stay empty in anything AI produces." (`prepare-bia/SKILL.md:14`) | carried |
| Method 1 | "**Fix the sources and their dates.** Ask the organiser, in one message, "at most three questions the attached material leaves open", from: the interviewee's role, what they know the organiser does not, what you need back, the interview's length. Confirm once, as a statement, that memory, past chats, project files, connectors and web search are off. Answers go under Gaps as "own statements, not sources", never a value; an entry only they support has Source `Gaps`, and any channel left on goes under Gaps." (`prepare-bia/SKILL.md:19`) | carried |
| Method 2 | "**Draft first.** Run the Task choice; sections in this order:" with the seven-item list and "A single supplier, carrier or person behind a resource is a question for the activity owner." (`prepare-bia/SKILL.md:22`, `:32`) | carried |
| Method 3 | "**Interview.** Tell the owner to "use the draft as the thing to correct, not the thing to confirm; record what it could not have known"." (`prepare-bia/SKILL.md:39`) | carried |
| Method 4 | "**Compare registers across sites.** Put each conflict "to the two owners, not to the model"." (`prepare-bia/SKILL.md:41`) | carried |
| Method 5 | "**Hand on with the confirmed and unconfirmed marks intact.** New entries are labelled "candidate, to confirm"; one the sources show confirmed keeps its mark." (`prepare-bia/SKILL.md:43`) | carried |
| Interview order 1, impacts over time | "1. impacts over time;" (`prepare-bia/SKILL.md:23`) | carried |
| Interview order 2, the MTPD | "2. the MTPD;" (`prepare-bia/SKILL.md:24`) | carried |
| Interview order 3, people with their skills, authorities and mandates | "3. people, "with the skills, authorities and mandates the work needs";" (`prepare-bia/SKILL.md:25`) | carried |
| Interview order 4, seats and buildings | "4. seats and buildings;" (`prepare-bia/SKILL.md:26`) | carried |
| Interview order 5, IT and applications, each with RTO and RPO | "5. IT and applications, "each with its RTO and its RPO";" (`prepare-bia/SKILL.md:27`) | carried |
| Interview order 6, suppliers and other third parties | "6. suppliers and other third parties;" (`prepare-bia/SKILL.md:28`) | carried |
| Interview order 7, dependencies as their own item | "7. dependencies, their own section: "up- and downstream relationships with other departments, each recorded with the RTO the relationship carries"." (`prepare-bia/SKILL.md:29`) | carried |
| MTPD, RTO and RPO stay empty | "Recovery fields stay empty in anything AI produces." plus the Task choice kept as written, whose Output leaves MTPD, RTO and RPO empty and a dependency's RTO too (`prepare-bia/SKILL.md:15`, `:50`) | carried |
| Task choice 1 | "[`../units/prompts/bia.md`](../units/prompts/bia.md), first in its Task line: "draft candidate activities, their resource requirements and interview questions for the site in the attached material". Keep its Intake, Output, Gaps and Cite." (`prepare-bia/SKILL.md:50`) | carried |
| For the auditor | "The register carries "the source, the interview it came from and the date behind each entry". Blank before the interview: the interview, the confirmation date and "the recovery times the owner set"." (`prepare-bia/SKILL.md:56`) | carried |
| Reviewer | "The activity owner confirms each requirement and sets MTPD and RTO. "Top management approves the BIA results." Name both." (`prepare-bia/SKILL.md:60`) | carried |
| Hand-over | "Before the preflight's AI-help sentence, write:" then "> After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA." (`prepare-bia/SKILL.md:44`, `:46`) | carried |

No row is weakened or missing, so no row needs the two texts side by side. Four rows turned on a judgement
rather than a word match, and the reasoning for each is recorded here.

**Method 1.** The unit's step has two halves: the sources with their dates, and the switched-off channels. The
channel half is carried and hardened past the unit: the skill has the organiser confirm memory, past chats,
project files, connectors and web search in one statement, and any channel left on goes under Gaps, which is
where the unit's warning (the model "may draw on it without saying so") lands in a reply a reader can see. The
dates half is instructed by the bolded heading and nowhere else in the step; it is then carried out by preflight
step 3, which the skill's first line runs ("Name each source's version and date" in one line per document at the
top of the draft, a document with neither going under Gaps), and by the Task choice's Output, kept, which opens
with the source documents and their dates. A manager running the skill fixes the dates, but through two other
files rather than this step's body, so it remains the thinner of the two halves and is worth watching in the next
sweep. The questions themselves now come with a cap, at most three, taken from the prompt's own Intake, with the
interview's length among the four candidates; asking fewer than the four listed is the prompt's rule, not a loss.

**Method 2.** The unit's step names four things in a parenthesis: activities, resource requirements, questions,
recovery fields blank. Three are in the Task choice the step tells the manager to run, word for word from the
prompt's Task line. The fourth is the one control at the top of the same file, unconditional and read before the
Method, plus preflight step 2 and the prompt's own Output. The step adds what the eval runs lost: the order as a
numbered list, dependencies as their own section, and a single supplier, carrier or person behind a resource as a
question for the activity owner rather than a finding. So the text the model receives drafts before interviewing
and leaves the recovery fields empty. "Draft first" is shorter than the unit's "Draft before interviewing", and
the step that follows is headed Interview, so the sequence the unit asks for is still on the page.

**Method 3.** The unit addresses the analyst: use the draft as the thing to correct, not the thing to confirm.
This skill stops at the pre-interview draft and runs no interview, so the only way it can carry the step is to
write the instruction into the draft, which it does, addressed to the activity owner. That is the right addressee:
the owner's confirmation is what puts an entry in the register, so the owner is the person whose rubber-stamping
the step guards against. The second half of the unit's sentence, record what it could not have known, is quoted
with it.

**For the auditor.** The unit's paragraph has a register half and a risk half. The skill carries the register half
and names which three fields are necessarily blank before any interview has happened, which is what the auditor
sees at the moment this skill's output exists. The risk half is out of scope by the unit's own words: this skill
runs the BIA draft, and "The BIA method does not cover risk assessment".
