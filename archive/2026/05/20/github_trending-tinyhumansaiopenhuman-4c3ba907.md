---
title: "tinyhumansai/openhuman"
source: GitHub Trending
url: https://github.com/tinyhumansai/openhuman
date: 2026-05-20
published_at: 2026-05-20T06:04:39.057791+00:00
tag: 工具开源
item_id: 4c3ba907f3c3ce55
---
**OpenHuman is your Personal AI super intelligence. Private, Simple and extremely powerful.**

[Discord](https://discord.tinyhumans.ai/) •
[Reddit](https://www.reddit.com/r/tinyhumansai/) •
[X/Twitter](https://x.com/intent/follow?screen_name=tinyhumansai) •
[Docs](https://tinyhumans.gitbook.io/openhuman/) •
[Follow @senamakel (Creator)](https://x.com/intent/follow?screen_name=senamakel)

🇺🇸 [English](https://github.com/tinyhumansai/openhuman/blob/main/README.md) | 🇨🇳 [简体中文](https://github.com/tinyhumansai/openhuman/blob/main/README.zh-CN.md) | 🇯🇵 [日本語](https://github.com/tinyhumansai/openhuman/blob/main/README.ja-JP.md) | 🇰🇷 [한국어](https://github.com/tinyhumansai/openhuman/blob/main/README.ko.md) | 🇩🇪 [Deutsch](https://github.com/tinyhumansai/openhuman/blob/main/README.de.md)


Early Beta: Under active development. Expect rough edges.

To install or get started, either download from the website over at [tinyhumans.ai/openhuman](https://tinyhumans.ai/openhuman?utm_source=github&utm_medium=readme) or run

```
# Download DMG, EXEs over at https://tinyhumans.ai/openhuman or run in from your terminal
# For macOS or Linux x64
curl -fsSL https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.sh | bash
# For Windows
irm https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.ps1 | iex
```

OpenHuman is an open-source agentic assistant designed to integrate with you in your daily life. Each bullet links to the deeper writeup in the [docs](https://tinyhumans.gitbook.io/openhuman/).

-
**Simple, UI-first & Human**A clean desktop experience and short onboarding paths take you from install to a working agent in a few clicks — no config-first setup, no terminal required. The agent has[a face](https://tinyhumans.gitbook.io/openhuman/features/mascot): a desktop mascot that speaks, reacts to its surroundings,[joins your Google Meets](https://tinyhumans.gitbook.io/openhuman/features/mascot/meeting-agents)as a real participant, remembers you across weeks, and keeps thinking in the background even when you've stopped typing. -
: plug into Gmail, Notion, GitHub, Slack, Stripe, Calendar, Drive, Linear, Jira and the rest of your stack with[118+ third-party integrations](https://tinyhumans.gitbook.io/openhuman/features/integrations)with[auto-fetch](https://tinyhumans.gitbook.io/openhuman/features/obsidian-wiki/auto-fetch)**one-click OAuth**. Every connection is exposed to the agent as a typed tool, and every twenty minutes the core walks each active connection and pulls fresh data into the[memory tree](https://tinyhumans.gitbook.io/openhuman/features/integrations/auto-fetch). No prompts, no polling loops you have to write, so the agent already has tomorrow's context this morning. -
: a local-first knowledge base built from your data and your activity. Everything you connect is canonicalized into ≤3k-token Markdown chunks, scored, and folded into hierarchical summary trees stored in[Memory Tree](https://tinyhumans.gitbook.io/openhuman/features/memory-tree)+[Obsidian Wiki](https://tinyhumans.gitbook.io/openhuman/features/obsidian-wiki)**SQLite on your machine**. The same chunks land as`.md`

files in an Obsidian-compatible vault you can open, browse and edit, inspired by Karpathy's[obsidian-wiki workflow](https://x.com/karpathy/status/2039805659525644595). -
**Batteries included**: web search, a web-fetch[scraper](https://tinyhumans.gitbook.io/openhuman/features/native-tools), a full coder toolset (filesystem, git, lint, test, grep), and[native voice](https://tinyhumans.gitbook.io/openhuman/features/voice)(STT in, ElevenLabs TTS out, mascot lip-sync, live Google Meet agent) are wired in by default.[Model routing](https://tinyhumans.gitbook.io/openhuman/features/model-routing)sends each task to the right LLM (reasoning, fast, or vision) under one subscription. No "install a plugin to read files" friction.[Optional local AI via Ollama](https://tinyhumans.gitbook.io/openhuman/features/model-routing/local-ai)for on-device workloads. -
: every tool call, scrape result, email body, and search payload is run through a token compression layer before it touches any LLM Model. HTML is converted to Markdown, long URLs are shortened, and verbose tool output is deduped and summarized via a configurable rule overlay etc... CJK, emoji, and other multi-byte text are preserved grapheme-by-grapheme — never stripped. You get the same information but at a fraction of the tokens. Reducing cost & latency by up to 80%.[Smart token compression (TokenJuice)](https://tinyhumans.gitbook.io/openhuman/features/token-compression) -
and[Messaging channels](https://tinyhumans.gitbook.io/openhuman/features/integrations#messaging-channels): inbound/outbound across the channels you already use, with workflow data that stays on device, encrypted locally, treated as yours.[privacy & security](https://tinyhumans.gitbook.io/openhuman/features/privacy-and-security)

New contributor? Start with [ CONTRIBUTING.md](https://github.com/tinyhumansai/openhuman/blob/main/CONTRIBUTING.md) for the fork/PR workflow and local validation commands, or use the copy-paste AI-agent prompt in

[. The short path is:](https://github.com/tinyhumansai/openhuman/blob/main/CONTRIBUTING-BEGINNERS.md#optional-let-an-ai-coding-agent-guide-you)

`CONTRIBUTING-BEGINNERS.md`

- Install Git, Node.js 24+, pnpm 10.10.0, Rust 1.93.0 (
`rustfmt`

+`clippy`

), CMake, Ninja, ripgrep, and the platform desktop build prerequisites. - Fork and clone the repo, then run
`git submodule update --init --recursive`

before`pnpm install`

so the vendored Tauri/CEF sources are present. - Use
`pnpm dev`

for web-only UI work,`pnpm --filter openhuman-app dev:app`

for the desktop shell, and focused checks such as`pnpm typecheck`

,`pnpm format:check`

, and`cargo check -p openhuman --lib`

before opening a PR.

Deeper docs: [Architecture](https://tinyhumans.gitbook.io/openhuman/developing/architecture) · [Getting Set Up](https://tinyhumans.gitbook.io/openhuman/developing/getting-set-up) · [Cloud Deploy](https://github.com/tinyhumansai/openhuman/blob/main/gitbooks/features/cloud-deploy.md).

OpenHuman is the first agent harness that gets to know you in minutes. Inspired by [Karpathy's LLM Knowledgebase](https://x.com/karpathy/status/2039805659525644595). Most agents start cold. Hermes learns by watching you work; OpenClaw waits for plugins to ferry context in. Either way, you spend days or weeks before the agent knows enough about your stack to be genuinely useful.

OpenHuman summarizes and compresses all your documents, emails & chats; and creates a memory graph that lets your agent remember everything about you.


OpenHuman skips the wait. Connect your accounts, let [auto-fetch](https://tinyhumans.gitbook.io/openhuman/features/integrations/auto-fetch) pull data locally on a 20-minute loop, and then have [Memory Trees](https://tinyhumans.gitbook.io/openhuman/features/memory-tree) compress everything into Markdown files stored intelligently in a [Karpathy-style Obsidian wiki](https://tinyhumans.gitbook.io/openhuman/features/obsidian-wiki).

In just one sync pass, the agent has full (compressed) context of your inbox, your calendar, your repos, your docs, your messages. No training period. No "give it a few weeks.". It becomes you, controlled by you.

Already self-host [agentmemory](https://github.com/rohitg00/agentmemory) across other coding agents? OpenHuman ships an optional `Memory`

backend that proxies to it — set `memory.backend = "agentmemory"`

in `config.toml`

and the same durable store powers OpenHuman alongside Claude Code, Cursor, Codex, and OpenCode. See the [agentmemory backend](https://tinyhumans.gitbook.io/openhuman/features/obsidian-wiki/agentmemory-backend) page for setup.

High-level comparison (products evolve, so verify against each vendor). OpenHuman is built to **minimize vendor sprawl**, keep **workflow knowledge on-device**, and give the agent a **persistent memory** of your data, not only chat.

| Claude Cowork | OpenClaw | Hermes Agent | OpenHuman | |
|---|---|---|---|---|
Open-source |
🚫 Proprietary | ✅ MIT | ✅ MIT | ✅ GNU |
Simple to start |
✅ Desktop + CLI | ✅ Clean UI, minutes | ||
Cost |
✅ One sub + TokenJuice | |||
Memory |
✅ Chat-scoped | ✅ Self-learning | 🚀 Memory Tree + Obsidian vault, optional
|

**Integrations****Auto-fetch****API sprawl****Model routing****Native tools***Building toward AGI and artificial consciousness? Star the repo and help others find the path.*

Show some love and end up in the hall of fame. Contributors get free merch and special access to our [Discord](https://discord.tinyhumans.ai/).
