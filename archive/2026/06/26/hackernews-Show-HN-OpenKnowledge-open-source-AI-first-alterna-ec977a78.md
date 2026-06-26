---
title: "Show HN: OpenKnowledge – open source AI-first alternative to Obsidian/Notion"
source: Hacker News
url: https://github.com/inkeep/open-knowledge
date: 2026-06-26
published_at: 2026-06-25T16:04:46+00:00
tag: 工具开源
item_id: ec977a7840b2adbf
---
OpenKnowledge is a beautiful, local-first markdown editor and LLM wiki with integrations for Claude, Codex, and other harnesses.

![OpenKnowledge editor with an AI agent drafting a launch recap](https://github.com/inkeep/open-knowledge/raw/main/assets/hero.webp)


Available as [macOS app](https://github.com/inkeep/open-knowledge/releases/latest/download/Open-Knowledge-arm64.dmg) or [Web app/CLI](https://openknowledge.ai/docs/get-started/quickstart#ok-install-web-app-linux-windows-intel-mac) for Linux, Windows, Intel Mac.

Key highlights:

- Full **WYSIWYG**so that editing markdown files feels like editing a Google Doc or Notion page.
- Collaborative **AI-editing**with**Claude, Codex, and Cursor desktop apps**. Can be used with any harness/agent via MCP/CLI.
- Out-of-the-box **MCP**,**skills**, and**agentic search**for LLM Wikis, agent second brains, and spec-driven development.
- No-code **Team Sharing**and**Auto-sync**powered by git/GitHub under the hood.

Docs for general usage: [https://openknowledge.ai/docs](https://openknowledge.ai/docs).

**macOS:** download the desktop app — open the DMG, drag **OpenKnowledge** to **Applications**, and launch it. [Latest release](https://github.com/inkeep/open-knowledge/releases/latest).

**Linux, Windows, Intel Mac:** run the same editor as a local web app via the CLI ([Node.js 24+](https://nodejs.org) required):

```
npm install -g @inkeep/open-knowledge
cd your-project
ok init          # scaffold the project + wire up Claude Code, Cursor, and Codex
ok start --open  # serve the web editor and open it in your browser
```
Public pull requests are welcome. When a public PR opens here, automation mirrors it into the internal monorepo for review and merge.

See [CONTRIBUTING.md](https://github.com/inkeep/open-knowledge/blob/main/CONTRIBUTING.md) for details.

OpenKnowledge is licensed under the [GNU General Public License v3.0 or later](https://github.com/inkeep/open-knowledge/blob/main/LICENSE) (`GPL-3.0-or-later`).
