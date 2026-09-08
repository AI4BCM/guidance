# `/ask-ai4bcm`

`/ask-ai4bcm` is the router into this guidance. You invoke it; it is never invoked by
a model on its own. It routes and nothing else — given a situation it names the unit
to read, the prompt to use and the maturity level the work needs, then stops, leaving
the running to you and to the task prompts in `prompts/`. `SKILL.md` is the single
source for that routing, served verbatim with the release tag to Claude, Codex,
Copilot and GPT alike; it follows in T7.
