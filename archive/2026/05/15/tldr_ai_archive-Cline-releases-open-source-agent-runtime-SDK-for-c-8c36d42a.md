---
title: "Cline releases open-source agent runtime SDK for coding agents"
source: TLDR AI · 2026-05-14
url: https://www.testingcatalog.com/cline-releases-open-source-agent-runtime-sdk-for-coding-agents/?utm_source=tldrai
date: 2026-05-15
published_at: 2026-05-14T12:00:00+00:00
tag: 工具开源
item_id: 8c36d42ac6c4035e
---
Cline has shipped `@cline/sdk`

, an open-source agent runtime that now powers every Cline surface and is available for any team to build on. Rather than layering new capabilities onto an architecture that had grown inseparable from its IDE host, the team rebuilt the core agent loop as a standalone, portable SDK and migrated their own CLI and Kanban on top of it. The VS Code and JetBrains extensions are in the process of following.

Introducing the Cline SDK. We rebuilt the Cline harness for our extension and CLI from scratch using all the lessons learned since creating one of the world's first coding agents in 2024, and are open sourcing it for others to build with today.

— Cline (@cline)

npm i @cline/sdk

🧵[pic.twitter.com/GbqWo4yiA6][May 13, 2026]

The SDK is a layered TypeScript stack in which each layer has a single responsibility. `@cline/shared`

carries foundational types and utilities. `@cline/llms`

owns the provider layer, covering Anthropic, OpenAI, Google, AWS Bedrock, Mistral, LiteLLM, and any OpenAI-compatible endpoint, with provider logic kept entirely out of the agent loop so switching providers is a config change, not a code change. `@cline/agents`

runs the stateless agentic loop, handling iteration, tool orchestration, and event emission. `@cline/core`

sits above that, managing stateful orchestration: session lifecycle, persistence, and config discovery. App surfaces, the CLI, VS Code, and JetBrains connect to the runtime at the top without owning it. Teams can install the full stack via `npm install @cline/sdk`

or pull individual packages for a smaller surface.

![Cline SDK](https://storage.ghost.io/c/2a/1b/2a1b1782-8506-4d7d-bf53-ad3fb52e2a0f/content/images/2026/05/Copy-of-Introducing-Cline-SDK_-the-upgraded-agent-runtime-and-we-rebuilt-Cline-upon-it-docx-Google-Docs-05-13-2026_01_42_AM.jpg)

The rebuild changes what is possible for long-running work. Sessions no longer die with a UI restart. A session can move across surfaces. The agent loop stays stateless and reusable, while the runtime around it becomes durable and portable. The improved harness also rewrote prompts, tightened context management, and rethought how tools are surfaced to the model. Terminal benchmark results reflect those gains: Cline CLI running claude-opus-4.7 scores 74.2% on Terminal Bench 2.0, compared to 69.4% for Claude Code on the same model. On open-weight models, Cline CLI reaches 55.1% with kimi-k2.6, ahead of OpenCode at 37.1% on the same run.

Try the new Cline CLI, now rebuilt on the SDK with a new TUI, agent teams, scheduled jobs, and connectors:

— Cline (@cline)

npm i -g cline

To build your own agent use:

npm i @cline/sdk

…or give your agent the Cline SDK skill:

npx skills add cline/sdk-skill[https://t.co/hbEHGGpIPO][May 13, 2026]

The SDK ships with agent teams and subagents natively. A session can delegate to specialist agents, track progress, and exchange handoff notes, all inside the same core runtime, without a separate orchestration layer. Plugins let teams add domain-specific behavior without forking: a plugin can register tools, observe lifecycle events, add rules, and shape what the agent sees. Scheduled CRON jobs, checkpointing, web search, and MCP connectors are native. With the new CLI, experimental connector channels let agents surface directly to Telegram, WhatsApp, Slack, and other platforms through a setup wizard accessible via `cline connect`

.


**SPONSORED**Test the Cline SDK out for yourself!

[Take me there!](https://docs.cline.bot/sdk?ref=testingcatalog.com)

Cline is the open-source project behind the SDK, crediting itself as the first real agentic coding experience, originally built on agentic tool calling with Claude Sonnet 3.5 before Claude Code, Codex, and the broader wave of coding agents arrived. The platform now serves over 7 million developers. Cline CLI 2.0 launched earlier in 2026 with terminal-first execution and headless CI support, and Cline Kanban followed as a visual orchestration layer for running multiple agents in parallel across a git repo. The SDK release is the infrastructure move underlying all of it: every prior Cline surface becomes a product built on a shared, open foundation rather than a standalone artifact. The project is available at `npm install @cline/sdk`

, with documentation at docs.cline.bot/sdk.
