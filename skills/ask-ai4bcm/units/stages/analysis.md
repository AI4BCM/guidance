<!-- meta: unit=stages/analysis pp=3 version=2026.09 cites=4.1,4.2,4.4,4.5,4.6 -->
# Analysis: Business Impact and Risk

## Situation

Analysis is the stage that runs on what nobody has written down yet. The blank page comes before the first interview: someone must produce a candidate activity list, a set of resource requirements and a set of questions. AI moves that starting line. It drafts from what your other sites already know; it cannot know what only the acquired site's staff know.

Analysis also involves some of the most sensitive material in BCM. Live BIA and risk data goes into an approved environment or nowhere.

## Typical AI uses

- drafting candidate activities, their resource requirements and the interview guide from existing site data
- summarising interviews into impacts, resource requirements, assumptions and unresolved points
- comparing requirements registers across sites to surface shared suppliers
- naming where two teams' recovery assumptions contradict
- summarising public threat developments for a person's risk review, and clustering risks, issues and recurring themes
- re-opening affected BIA and risk records when a system, supplier or site changes

The capability and environment for each use are in the selection guide in `tools.md`.

## Minimum controls

The one control that matters: **a drafted resource requirement is a question for the owner, never an entry in the register.** It stays unconfirmed until an owner of the activity says otherwise.

- **AI may test whether a proposed RTO is consistent with impact criteria; it does not set it.** The same holds for MTPD.
- The draft names its source data and that data's date. An out-of-date inventory yields a confident, current-looking, wrong BIA.
- Recovery fields stay empty in anything AI produces, so a blank is visibly a blank, not an inherited guess.

## Method

1. Fix the sources you will attach, and their dates. What you do not attach is not in the answer. Whether the model filled the gap or left it out, the output looks the same.
2. Draft before interviewing — activities, resource requirements, questions, recovery fields blank.
3. Interview. Use the draft as the thing to correct, not the thing to confirm; record what it could not have known.
4. Compare registers across sites; put every conflict to the two owners, not to the model.
5. Hand the register on with the confirmed and unconfirmed marks intact, so the next stage can see which entries were drafted and never challenged.

The outcome of a BIA is a list of requirements. A requirement names what the activity needs in order to run, and states nothing about what the organisation has today.

Requirements come in four classes. Once the impacts and the MTPD are settled, the interview covers people, with the skills, authorities and mandates the work needs; then seats and buildings; then IT and applications, each with its RTO and its RPO; then suppliers and other third parties.

Dependencies are a separate item and keep the narrower meaning of up- and downstream relationships with other departments, each recorded with the RTO the relationship carries, so that a relationship one department records appears in the other department's BIA.

The five-stage BIA workflow — identification of scope, structured interview, conversion to the standardised template, listing the requirements, consolidation and handover — is specified in `workflow-design.md`.

## Risk assessment

The BIA method above does not cover the risk half of this stage. Risk assessment with AI support has a public half and an internal half, and the data rule draws the line between them. Public threat, regulatory and incident reporting may be gathered in any approved tool because it says nothing about your organisation; the moment relevance is judged against your own records, the work is high-sensitivity and moves to the approved environment.

| | Risk assessment with AI support |
|---|---|
| Inputs | public threat, regulatory and incident reporting for the sector and the regions you operate in; the approved risk register, the requirements register and the BIA output, each with its date |
| Capability | the two rows of the `tools.md` selection guide that carry it, public research in any approved tool and threat relevance in the approved environment |
| Output | a relevance note per threat that states how certain the public evidence is, links each point to the public source and to the internal record it touches, and ends in questions or themes for the risk owner |
| Review boundary | a person assesses the threat, decides the treatment and accepts the risk; a model proposes relevance and does not rate a risk, accept it or change a risk record |

When a system, supplier, site or process changes, the comparison runs the other way. A workflow over approved source systems flags the risk and BIA records the change touches and hands them to their owners for review, on the checklist in `workflow-design.md`; the record itself changes only through the normal approval route.

## Prompts

The task prompt is `prompts/bia.md`, whose first task line is the pre-interview draft the case below runs; its review line names who confirms each requirement and who sets the recovery fields. The risk-assessment relevance note uses the same six-element pattern from `prompts/README.md`, with the threat evidence and the risk register as its sources and the table above as its output.

## Case example

**Prompt.** Draft the activities, resource requirements and interview questions for the acquired site. Leave recovery times blank.

**Response.** Fourteen candidate activities, drawn from the four existing sites. Resource requirements listed per activity in the four classes. Thirty-one interview questions. RTO and MTPD fields empty as instructed.

**What changed.** The interview guide existed before the first interview. The interviews then added what the draft could not have known: the site slaughters wild boar, seasonally, and it is cash-relevant.

## Level

Level 2, Team-level structured use. The pre-interview draft needs no connector: it works from the sources you attach, so what it takes is agreed tools, a written data rule, a named reviewer and the normal approval route. Write down the method and the dates of those sources as you go, so a reviewer can see what the draft was built from. BIA support and threat relevance over connected records are Level 3, Connected and governed use, where retrieval reaches the live inventory, the draft can be regenerated when the inventory changes, and all five self-check questions in `levels.md` answer yes with evidence.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
