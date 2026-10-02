# Codex

Sources: https://learn.chatgpt.com/docs/build-skills (reached from
https://developers.openai.com/codex/skills/), read 2026-10-02; the `skills` CLI 1.7.0, run 2026-10-02.

**Test tier: full eval.** Every skill is run on Codex in three cases (the job, never-alone, a
planted instruction), three runs each, plus a run without the skill. Results:
[`evals/results.md`](../evals/results.md).

## The short way

Inside the project you work in:

```
npx skills@latest add AI4BCM/guidance/skills
```

The CLI asks which skills and which clients; `-a codex` names Codex up front. It puts each package
you pick in `.agents/skills/<name>/`, where Codex looks, and records it in `skills-lock.json`;
`npx skills update` is meant to refresh it (not yet measured against the published repository). Add
`-g` to install for your user account instead of one project.

**Keep `/skills` at the end of the source.** The `skills` CLI looks at the repository root before
`skills/` and keeps the first skill of each name it finds, so `npx skills add AI4BCM/guidance`
installs the source folders from the root: `SKILL.md` and `agents/openai.yaml`, with no
`preflight.md`, no units and no literature (measured with 1.7.0 on 2026-10-02). With
`AI4BCM/guidance/skills` it reads the packages, and every file arrives.

## By hand, as folders

Copy the package folder `skills/<name>/` into one of the folders Codex scans:

```
$CWD/.agents/skills
$CWD/../.agents/skills
$REPO_ROOT/.agents/skills
$HOME/.agents/skills
/etc/codex/skills
```

## Using a skill

Type `$prepare-bia` (or another skill's name) in the Codex CLI or IDE extension; `/skills` lists
what Codex has found. Each package's `agents/openai.yaml` sets
`policy.allow_implicit_invocation: false`: Codex will not start the skill on its own, and naming it
still works.
