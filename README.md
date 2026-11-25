# Universal RE Engine

[![Release](https://img.shields.io/github/v/release/mannarohitkumar21-art/universal-re-engine)](https://github.com/mannarohitkumar21-art/universal-re-engine/releases)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Portable](https://img.shields.io/badge/AI%20agents-universal-purple.svg)](#using-with-different-ai-agents)

**A portable, agent-neutral reverse-engineering skill and reconstruction workflow for authorized applications.**

Universal RE Engine helps AI coding agents analyze an application's source code, backend (when its source or authorized evidence is available), APIs, data models, architecture, and UI/UX. It creates a documented blueprint and a clean-room reconstruction plan.

> **Important:** This is a reusable skill/instruction toolkit, not a magical universal installer or an automatic app-cloning binary. Different AI products support different skill and instruction formats. The core Markdown instructions can be used across agents, but setup may differ.

## Download

### Latest ZIP
Go to **[Releases](https://github.com/mannarohitkumar21-art/universal-re-engine/releases/latest)** and download `Universal-RE-Engine-v1.0.0.zip` from the Assets section.

Direct release download (once v1.0.0 is published):

```text
https://github.com/mannarohitkumar21-art/universal-re-engine/releases/download/v1.0.0/Universal-RE-Engine-v1.0.0.zip
```

To download from a terminal:

```bash
curl -L -o Universal-RE-Engine-v1.0.0.zip \
  https://github.com/mannarohitkumar21-art/universal-re-engine/releases/download/v1.0.0/Universal-RE-Engine-v1.0.0.zip
```

Or with Git:

```bash
git clone https://github.com/mannarohitkumar21-art/universal-re-engine.git
cd universal-re-engine
```

## What it analyzes

| Area | Analysis |
|---|---|
| Source code | Languages, modules, classes, functions, dependencies, logic flows |
| Backend | Services, routes, middleware, auth, jobs, webhooks, schema — only when evidence/source is supplied |
| API | Observable/documented endpoints, request/response contracts, errors, integrations |
| Database | Supplied migrations, models, schema, indexes and relationships |
| UI/UX | Screens, layout hierarchy, components, design tokens, navigation, states and interactions |
| Architecture | System context, modules, trust boundaries, data-flow and sequence diagrams |
| Reconstruction | Feature-parity matrix, implementation plan, validation checklist |

## Quick setup

1. Download the ZIP from [GitHub Releases](https://github.com/mannarohitkumar21-art/universal-re-engine/releases/latest), or clone this repository.
2. Extract/open the folder in your AI coding agent's workspace.
3. Ask the agent to read `SKILL.md` and `agents/MASTER_AGENT.md`.
4. Add the authorized target project separately. Do not place secrets or production customer data in the analysis workspace.
5. Ask for analysis first. Reconstruction starts only after you explicitly request it.

Suggested first prompt:

```text
Read SKILL.md and agents/MASTER_AGENT.md.
Analyze the authorized application project in ./target-app.
Do not modify the target project.
First create the scope/inventory report, then analyze source code,
backend evidence, UI/UX, architecture, and produce the reconstruction plan.
Label each finding Observed, Inferred, Unknown, or Not applicable.
Do not invent hidden backend details or expose secrets.
```

## Using with different AI agents

The package is **agent-neutral at the instruction level**, not a guarantee of one-click installation in every AI product. Use the appropriate adapter below and follow the current product documentation for custom skills/instructions.

| AI agent | Recommended setup |
|---|---|
| ChatGPT / ChatGPT coding workspace | Upload/open this folder in the workspace. Ask it to read `SKILL.md` and `agents/MASTER_AGENT.md`. For persistent workflows, use the custom/project instruction mechanism available in your ChatGPT environment. See [`adapters/CHATGPT.md`](adapters/CHATGPT.md). |
| Claude / Claude Code | Add the folder to the project workspace and configure a custom skill/project instruction using the current Claude Code skill documentation. See [`adapters/CLAUDE.md`](adapters/CLAUDE.md). |
| OpenAI Codex | Make this folder available in the Codex workspace and reference `SKILL.md` from the supported project instructions/skill mechanism. See [`adapters/CODEX.md`](adapters/CODEX.md). |
| Gemini-based coding agents | Attach/add the folder to the workspace and provide `SKILL.md` as the primary instruction. See [`adapters/OTHER_AGENTS.md`](adapters/OTHER_AGENTS.md). |
| Other AI coding agents | If the agent can read Markdown files and inspect a workspace, it can follow the core workflow. Give it `SKILL.md` and the relevant role file under `agents/`. |

### Universal agent prompt

```text
Use this repository as your Universal RE Engine instruction pack.
Read SKILL.md, agents/MASTER_AGENT.md, and the relevant analyst files.
Follow the evidence labels and safety boundaries exactly.
Do not assume access to private backend source or remote services.
```

## Run the read-only inventory script

Requires Python 3.9+:

```bash
python scripts/project_inventory.py /path/to/authorized/project \
  --out reports/inventory.json
```

The script inventories filenames and project markers. It does not execute target project code.

## Repository structure

```text
.
├── SKILL.md
├── README.md
├── agents/
│   ├── MASTER_AGENT.md
│   ├── CODE_ANALYST.md
│   ├── BACKEND_ANALYST.md
│   ├── UI_UX_ANALYST.md
│   ├── ARCHITECTURE_ANALYST.md
│   └── RECONSTRUCTION_AGENT.md
├── adapters/
│   ├── CHATGPT.md
│   ├── CLAUDE.md
│   ├── CODEX.md
│   ├── OTHER_AGENTS.md
│   └── UNIVERSAL_AGENT_INSTRUCTIONS.md
├── config/settings.example.json
├── docs/
│   ├── INPUT_GUIDE.md
│   └── REPORT_TEMPLATES.md
└── scripts/project_inventory.py
```

## Expected analysis reports

- `reports/01_scope_and_inventory.md`
- `reports/02_source_code_analysis.md`
- `reports/03_backend_analysis.md`
- `reports/04_ui_ux_specification.md`
- `reports/05_architecture_and_data_flow.md`
- `reports/06_reconstruction_plan.md`
- `reports/07_validation_report.md`

## Safety, permission and technical limits

Use only apps, repositories, APIs, devices, and environments you own or are explicitly authorized to assess.

- An APK does not generally contain the complete original source code.
- Client-side inspection cannot reveal private server-side code, private databases, or hidden infrastructure.
- Analyze backend internals only when backend source, infrastructure configuration, schema, logs, or authorized documentation is supplied.
- Do not bypass authentication, access controls, DRM, anti-tamper, or certificate pinning without explicit authorization and a lawful, bounded test scope.
- Never reveal or reuse API keys, tokens, passwords, private user data, or customer records.
- Do not copy proprietary code, logos, or protected assets without permission. Prefer clean-room reimplementation and user-provided/licensed assets.
- The skill must label findings **Observed**, **Inferred**, **Unknown**, or **Not applicable**. It must never invent missing functionality or test results.

## Contributing

Issues and pull requests are welcome. Include reproducible steps, the agent/environment used, and sample data with secrets removed.

## License

See [`LICENSE`](LICENSE). The license applies to this repository's original toolkit files; it does not grant rights to third-party applications or assets analyzed with it.
