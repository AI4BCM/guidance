# GitHub Copilot

Sources: https://docs.github.com/en/copilot/concepts/agents/about-agent-skills and
https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills, both read
2026-10-02; the `skills` CLI 1.7.0, run 2026-10-02.

**Test tier: smoke test.** About 12 runs by the maintainer, not the full eval. Results:
[`evals/results.md`](../evals/results.md).

## Copilot may start a skill you did not name

Copilot reads neither `disable-model-invocation` nor `policy.allow_implicit_invocation`. Its
documentation says it decides when to use a skill from your prompt and the skill's description. So
a skill can open while you are asking about something else, which it cannot do in Claude Code or
Codex. When one does, it still runs its preflight first: it asks what class of data your material
holds, and it writes nothing. If you want a skill only on request, install it only when you need
it, or disable it with `/skills` in the Copilot CLI (`copilot skill disable <name>` from a
terminal).

## With the `skills` CLI (recommended)

Inside the repository you work in:

```
npx skills@latest add AI4BCM/guidance/skills -a github-copilot
```

The CLI puts each package you pick in `.agents/skills/<name>/`, which Copilot reads; add `-g` to
install for your user account instead of one repository. Keep `/skills`
at the end of the source: without it the CLI installs the root source folders, which arrive without
`preflight.md` and the units ([codex.md](codex.md) has the measurement).

## By hand, as folders

Copy the package folder `skills/<name>/` into one of:

```
.github/skills    .claude/skills    .agents/skills    (in a repository)
~/.copilot/skills    ~/.agents/skills                 (for you, in every project)
```

`copilot skill add <DIRECTORY>` adds one from a path. In a running CLI session, `/skills reload`
picks up a new one and `/skills info <name>` shows where it came from.

## Using a skill

Name it in your prompt with a slash: `Use /prepare-bia for tomorrow's interview with Logistics.`
Copilot reads skills in the cloud agent, Copilot code review, the Copilot CLI, the Copilot app, and
agent mode in Visual Studio Code and JetBrains IDEs. Skills in `.github/skills` are also available
to Copilot code review.
