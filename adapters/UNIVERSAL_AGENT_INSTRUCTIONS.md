# Universal agent setup

The package is agent-neutral at its core. To use it:
1. Make the package folder available in the agent's workspace.
2. Tell the agent: "Read `SKILL.md` and `agents/MASTER_AGENT.md`. Follow the workflow and safety rules exactly."
3. If the agent supports reusable skills, install/copy the package according to that product's current skill documentation.
4. If it supports project-level instructions only, paste the core role and workflow from `SKILL.md` into the project instructions and keep the remaining files available as references.
5. If it supports sub-agents, assign the role files in `agents/`; otherwise ask it to perform them sequentially.

No single ZIP format can force every AI product to load a skill automatically. The portable Markdown core makes the workflow reusable; each platform may need a small installation step.
