# ChatGPT

Sources: [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt), read
2026-10-02 in a browser (the help centre answers HTTP 403 to `curl` from some networks);
[Build skills](https://learn.chatgpt.com/docs/build-skills.md) and
[Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins.md), read 2026-10-02;
[Package your plugin](https://developers.openai.com/plugins/build/plugins.md) and
[Importing and syncing plugin marketplaces from GitHub](https://help.openai.com/en/articles/20001504-importing-and-syncing-plugin-marketplaces-from-github),
read 2026-09-10.

**Test tier: smoke test.** About 12 runs by the maintainer, not the full eval.

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
5. Open the imported `ai4bcm-guidance` plugin and check its **Installation policy**. Import does not
   read a policy from the repository: a newly imported plugin starts as **Available**, which lets
   eligible members install it, and **Installed** puts it in front of them. Review it before anyone
   uses it (help centre search result, 2026-11-01; the article answers 403 from the build machine).

The package declares no MCP server, so nothing in it needs the desktop app.

## Using a skill

Name it with `@`, for example `@prepare-bia`. Each package's `agents/openai.yaml` sets
`policy.allow_implicit_invocation: false`, which the build-skills page documents for Codex; whether
ChatGPT honours it is one of the smoke test's checks.

## What has not been run

Neither route has been run in a Business, Enterprise, Healthcare or Edu workspace from this
repository's build machine. What is checked is the files: `tools/check_installs.py` builds the ten
zips from a fresh clone, extracts them, and finds each skill byte for byte its package, with
`preflight.md` and `units/`.

## On a plan without skills

Sources, read 2026-11-01 from the help centre's search results only (every article answered HTTP 403
from the build machine, so none was opened):
[Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt),
[Uploading files](https://help.openai.com/en/articles/8555545-uploading-files-and-audio-to-chatgpt),
[Creating and editing GPTs](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts) and
[Custom GPT retirement](https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq).
The plugins article and the July 2026 release notes speak of personal skills on paid plans other
than Free and Go, and the pricing page lists skills on Free; the skills article above says
Business, Enterprise, Healthcare and Edu. This page follows the skills article until a run settles
it.

On Free, Go, Plus or Pro, give ChatGPT the text instead of the skills:

- **A project.** Projects are on every plan. Create one, add the .md file from
  <https://ai4bcm.org/guidance> to its files (about 140 KB; if it is refused, rename it `.txt`), and add an instruction such as *Answer
  from the AI4BCM guidance in this project and name the unit each answer comes from.* A Free
  project holds 5 files, Go and Plus 25, Pro 40.
- **One chat.** Attach the .md file to the chat and ask. Free accounts can upload 3 files a day.
- **Not a custom GPT.** Personal accounts can no longer create GPTs, and OpenAI retires custom GPTs
  on 11 December 2026.

Neither a project nor an attached file carries the preflight. The task skills ask the data class
before they start; without them, that question is yours (`units/data-rules.md`).
