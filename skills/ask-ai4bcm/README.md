# `/ask-ai4bcm`

`/ask-ai4bcm` is the router into this guidance. You invoke it; it is never invoked by
a model on its own. It routes and nothing else — given a situation it names the unit
to read, the prompt to use and the maturity level the work needs, then stops, leaving
the running to you and to the task prompts in `prompts/`. [`SKILL.md`](SKILL.md) is the
single source for that routing, and every client reads that one file.

`agents/openai.yaml` carries the same contract for the clients that read it:
`policy.allow_implicit_invocation: false`. Installing it, by plugin, by the `skills` CLI or by
hand in each of the four clients: [`install/`](https://github.com/AI4BCM/guidance/blob/main/install/README.md).
