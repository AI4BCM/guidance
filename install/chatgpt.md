# ChatGPT

Sources: [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt), read
2026-10-02 in a browser (the help centre answers HTTP 403 to `curl` from some networks);
[Build skills](https://learn.chatgpt.com/docs/build-skills.md) and
[Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins.md), read 2026-10-02;
[Package your plugin](https://developers.openai.com/plugins/build/plugins.md) and
[Importing and syncing plugin marketplaces from GitHub](https://help.openai.com/en/articles/20001504-importing-and-syncing-plugin-marketplaces-from-github),
read 2026-09-10.

**Test tier: smoke test.** About 12 runs by the maintainer, not the full eval. Results:
[`evals/results.md`](../evals/results.md).

## Who can install skills in ChatGPT

The help centre: "Skills are available to eligible ChatGPT Business, Enterprise, Healthcare, and Edu
users, subject to workspace settings and product availability." An administrator can also turn
skills, or skill uploading, off for your role. On a Free, Go, Plus or Pro account there is no skill
route in ChatGPT itself; read the guidance's units directly, or use Codex ([codex.md](codex.md)).

## Route A: upload one skill

For one person, or a workspace with no GitHub connection.

1. Take `<name>.zip` for the skill you want. The maintainer builds them with
   `python3 tools/build_chatgpt_package.py --zips <folder>`; each holds the package folder
   `<name>/` with `SKILL.md`, `preflight.md`, `units/` and `literature/` inside.
2. In ChatGPT, open **Plugins**, then the **Skills** tab, select **Create**, then **Upload from your
   computer**, and pick the zip. An administrator can use **+ (Add skill)** on the admin **Skills**
   page to put it in front of the workspace instead.
3. ChatGPT scans an uploaded skill first. Most are available when the scan ends; some are marked
   **Needs Review**. Review it yourself as well: it came from outside your organisation.

The help centre does not say which file format the upload takes. A zip with the skill folder at its
root is what these files are; the first upload in the maintainer's smoke test confirms it or
corrects this page.

## Route B: import the plugin from GitHub

For a workspace administrator who wants all ten skills, kept current. ChatGPT re-reads the
repository daily. A portable plugin finds skills only under `skills/<name>/`, which is where the
packages are.

1. **Workspace settings > Plugins**, **Add**, then **Import marketplace**.
2. **Source**: `https://github.com/AI4BCM/guidance`, with no branch or folder after it. Leave
   **Path** empty: the catalogue is `.claude-plugin/marketplace.json` at the root.
3. **Branch, tag, or commit**: empty to follow the default branch, or a release tag to pin the
   wording your organisation reviewed.
4. **Import marketplace**, and authorise GitHub access.
5. Open the imported `ai4bcm-guidance` plugin and set its **Installation policy**. Import does not
   read a policy from the repository, so until you set one nobody has the plugin.

The package declares no MCP server: a plugin that declares one is labelled Desktop only and loses
ChatGPT on the web.

## Using a skill

Name it with `@`, for example `@prepare-bia`. Each package's `agents/openai.yaml` sets
`policy.allow_implicit_invocation: false`, which the build-skills page documents for Codex; whether
ChatGPT honours it is one of the smoke test's checks.

## What has not been run

Neither route has been run in a Business, Enterprise, Healthcare or Edu workspace from this
repository's build machine. What is checked is the files: `tools/check_installs.py` builds the ten
zips from a fresh clone, extracts them, and finds each skill byte for byte its package, with
`preflight.md` and `units/`.
