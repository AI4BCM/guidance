<!-- meta: unit=stages/analysis pp=3 version=2026.09 cites=4.1,4.2,4.4,4.5,4.6 -->
# Analysis: Business Impact and Risk

## Situation

Analysis is the stage that runs on what nobody has written down yet. The blank page comes before the first interview: someone must produce a candidate activity list, a dependency structure and a set of questions. AI moves that starting line. It drafts from what your other sites already know; it cannot know what only the acquired site's staff know.

Analysis also involves some of the most sensitive material in BCM. Live BIA and risk data goes into an approved environment or nowhere.

## Typical AI uses

- drafting candidate activities, per-activity dependencies and the interview guide from existing site data
- summarising interviews into impacts, dependencies, assumptions and unresolved points
- comparing dependency registers across sites to surface shared suppliers
- naming where two teams' recovery assumptions contradict
- re-opening affected BIA entries when a system, supplier or site changes

## Minimum controls

The one control that matters: **a drafted dependency is a question for the owner, never an entry in the register.** It stays unconfirmed until an owner of the activity says otherwise.

- **AI may test whether a proposed RTO is consistent with impact criteria; it does not set it.** The same holds for MTPD.
- The draft names its source data and that data's date. An out-of-date inventory yields a confident, current-looking, wrong BIA.
- Recovery fields stay empty in anything AI produces, so a blank is visibly a blank, not an inherited guess.

## Method

1. Fix the sources you will attach, and their dates. What you do not attach is not in the answer. Whether the model filled the gap or left it out, the output looks the same.
2. Draft before interviewing — activities, dependencies, questions, recovery fields blank.
3. Interview. Use the draft as the thing to correct, not the thing to confirm; record what it could not have known.
4. Compare registers across sites; put every conflict to the two owners, not to the model.
5. Hand the register on with the confirmed and unconfirmed marks intact, so the next stage can see which entries were drafted and never challenged.

The five-stage BIA workflow — scope, interviews, mapping, draft, handover — is specified in `workflow-design.md`.

## Prompts

```
Role: you are supporting a BCM professional preparing a business impact analysis.
Task: draft candidate activities, their dependencies, and interview questions for the site described in the attached material.
Sources: use only the attached activity lists, system inventory and supplier records. Do not supply values from general knowledge.
Output: a table of activities with dependencies, then a numbered question list.
Gaps: leave recovery time fields empty. List separately what you could not determine and what source would settle it.
Cite: name the source document for each dependency.
```

## Case example

**Prompt.** Draft the activities, dependencies and interview questions for the acquired site. Leave recovery times blank.

**Response.** Fourteen candidate activities, drawn from the four existing sites. Dependencies listed per activity. Thirty-one interview questions. RTO and MTPD fields empty as instructed.

**What changed.** The interview guide existed before the first interview. The interviews then added what the draft could not have known: the site slaughters wild boar, seasonally, and it is cash-relevant.

## Level

Level 3, Connected and governed use. The draft is only worth interviewing against if the method and sources are written down: it can then be regenerated when the inventory changes, and a reviewer can see what it was built from. Level 1 or 2 produces a plausible list nobody can re-derive.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
