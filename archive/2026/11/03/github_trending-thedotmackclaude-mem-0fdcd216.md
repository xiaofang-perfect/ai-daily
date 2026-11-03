---
title: "thedotmack/claude-mem"
source: GitHub Trending
url: https://github.com/thedotmack/claude-mem
date: 2026-11-03
published_at: 2026-11-03T09:51:04.355717+00:00
tag: 工具开源
item_id: 0fdcd216f14a7990
---
[🇨🇳 中文](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.zh.md) •
  [🇹🇼 繁體中文](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.zh-tw.md) •
  [🇯🇵 日本語](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.ja.md) •
  [🇵🇹 Português](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.pt.md) •
  [🇧🇷 Português](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.pt-br.md) •
  [🇰🇷 한국어](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.ko.md) •
  [🇪🇸 Español](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.es.md) •
  [🇩🇪 Deutsch](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.de.md) •
  [🇫🇷 Français](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.fr.md) •
  [🇮🇱 עברית](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.he.md) •
  [🇸🇦 العربية](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.ar.md) •
  [🇷🇺 Русский](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.ru.md) •
  [🇵🇱 Polski](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.pl.md) •
  [🇨🇿 Čeština](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.cs.md) •
  [🇳🇱 Nederlands](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.nl.md) •
  [🇹🇷 Türkçe](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.tr.md) •
  [🇺🇦 Українська](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.uk.md) •
  [🇻🇳 Tiếng Việt](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.vi.md) •
  [🇵🇭 Tagalog](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.tl.md) •
  [🇮🇩 Indonesia](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.id.md) •
  [🇹🇭 ไทย](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.th.md) •
  [🇮🇳 हिन्दी](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.hi.md) •
  [🇧🇩 বাংলা](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.bn.md) •
  [🇵🇰 اردو](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.ur.md) •
  [🇷🇴 Română](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.ro.md) •
  [🇸🇪 Svenska](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.sv.md) •
  [🇮🇹 Italiano](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.it.md) •
  [🇬🇷 Ελληνικά](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.el.md) •
  [🇭🇺 Magyar](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.hu.md) •
  [🇫🇮 Suomi](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.fi.md) •
  [🇩🇰 Dansk](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.da.md) •
  [🇳🇴 Norsk](https://github.com/thedotmack/claude-mem/blob/main/docs/i18n/README.no.md)

#### Persistent memory compression system built for [Claude Code](https://claude.com/claude-code).

  
  

  
  

  

  


| ![Claude-Mem Preview](https://raw.githubusercontent.com/thedotmack/claude-mem/main/docs/public/cm-preview.gif)  |  | 

[Quick Start](https://github.com#quick-start) •
  [How It Works](https://github.com#how-it-works) •
  [Search Tools](https://github.com#mcp-search-tools) •
  [Documentation](https://github.com#documentation) •
  [Configuration](https://github.com#configuration) •
  [Troubleshooting](https://github.com#troubleshooting) •
  [License](https://github.com#license)

Claude-Mem seamlessly preserves context across sessions by automatically capturing tool usage observations, generating semantic summaries, and making them available to future sessions. This enables Claude to maintain continuity of knowledge about projects even after sessions end or reconnect.

Install claude-mem for Grok Bot:

`npx claude-mem install --ide grok-bot`
Grok Bot has no host hooks, so we watch the chat log files. Default is CMEM Pro, the hosted memory. Local observer is opt-in: `--provider host`. Installing this plugin does not install Cursor.

**Awareness push pilot (LFG + Orifice):** needle observations (`decision`, `bugfix`, `security_alert`, `sensitive`) are appended as dated `- YYYY-MM-DD [awareness] …` lines into that bot's `memory/log/YYYY-MM.md`. Grok Bot already re-reads the log from disk. This does not write `profile.md`, user-memory, or project memory. Disable with `CLAUDE_MEM_GROK_BOT_AWARENESS_ENABLED=false`.

Install with a single command:

`npx claude-mem install`
The installer sets everything up first, then asks you to sign in to claude-mem in your browser (email magic link — no card required). Signing in provisions a memory key for your account and unlocks the **claude-mem observer** with a **30 Day Free Trial**: memory runs off-plan, so you get up to 100% more usage from your plan. When the free trial ends, memory automatically falls back to your Anthropic plan unless you subscribe. After sign-in you pick your memory provider — the claude-mem observer, your own OpenRouter or Gemini key, or your Anthropic plan.

Prefer to skip the sign-in? Pass an explicit `--provider` flag, set `CLAUDE_MEM_ONLINE_OPTIN=false`, or run in CI/non-interactive shells — the installer completes without any account interaction.

Or install for OpenCode:

`npx claude-mem install --ide opencode`
This works with OpenCode 1.3.4 or later, including OpenCode 2. Restart OpenCode after installing.

Or install for **T3 Code** (Codex and Claude Code providers):

`npx claude-mem install --ide t3code`
The installer discovers T3 Code's enabled providers, registers native Claude-Mem plugins in their configured homes, and supports T3-managed Codex. Restart T3 Code, trust the provider's hooks when prompted, and start a new thread. See the [T3 Code integration guide](https://docs.claude-mem.ai/t3code-integration) for custom server settings, status, and removal.

Or install for Antigravity CLI ([setup guide](https://docs.claude-mem.ai/antigravity-cli/setup)):

`npx claude-mem install --ide antigravity`
Or install for OMP (Oh My Pi):

`npx claude-mem install --ide omp`
Or install the native Pi extension or DeepSeek Harness plugin:

```
npx claude-mem install --ide pi
npx claude-mem install --ide dsh --dsh-profile tui
```
Pi and DeepSeek Harness use the worker runtime. See [native harness setup](https://github.com/thedotmack/claude-mem/blob/main/docs/native-harness-integrations.md) for capture, recall, and troubleshooting.

Or install from the plugin marketplace inside Claude Code:

```
/plugin marketplace add thedotmack/claude-mem
/plugin install claude-mem
```
Restart Claude Code. Context from previous sessions will automatically appear in new sessions.

**Note:** Claude-Mem is also published on npm, but `npm install -g claude-mem` installs the **SDK/library only** — it does not register the plugin hooks or set up the worker service. Always install via `npx claude-mem install` or the `/plugin` commands above.


Install claude-mem as a persistent memory plugin on [OpenClaw](https://openclaw.ai) gateways with a single command:

`curl -fsSL https://install.cmem.ai/openclaw.sh | bash`
The installer handles dependencies, plugin setup, AI provider configuration, worker startup, and optional real-time observation feeds to Telegram, Discord, Slack, and more. See the [OpenClaw Integration Guide](https://docs.claude-mem.ai/openclaw-integration) for details.

**Key Features:**

- 🧠 **Persistent Memory** - Context survives across sessions
- 📊 **Progressive Disclosure** - Layered memory retrieval with token cost visibility
- 🔍 **Smart Search (Default)** - Query your project history with the three-step mem-search skill
- 🖥️ **Local My Work** - Live requests, progress, human handoffs and a saved review queue at the worker URL printed on startup. [Guide](https://docs.claude-mem.ai/usage/my-work). Memory, sessions and settings remain at `/viewer`.
- 👥 **TeamBrain** - An optional shared workspace beside My Work, with real team work lists, member attribution and linked findings. Each person chooses what to share; personal requests and review notes stay separate. [Set up a team](https://cmem.ai/teambrain/start).
- 💻 **Claude Desktop Skill** - Search memory from Claude Desktop conversations
- 🔒 **Privacy Control** - Use `<private>` tags to exclude sensitive content from storage
- 🖼️ **Screenshots (opt-in, off by default)** - Keep converted copies of tool screenshots under `~/.claude-mem/media-v1/`, upload them to cmem.ai only when Cloud Sync is on, and send them to the observer model only when image inference is separately enabled ([details](https://docs.claude-mem.ai/configuration#screenshots-and-images-opt-in))
- ⚙️ **Context Configuration** - Fine-grained control over what context gets injected
- 🤖 **Automatic Operation** - No manual intervention required
- 🔗 **Citations** - Reference past observations with IDs through the worker API or view all in the web viewer

📚 **[View Full Documentation](https://docs.claude-mem.ai/)** - Browse on official website

- **[Installation Guide](https://docs.claude-mem.ai/installation)** - Quick start & advanced installation
- **[Usage Guide](https://docs.claude-mem.ai/usage/getting-started)** - How Claude-Mem works automatically
- **[Search Tools](https://docs.claude-mem.ai/usage/search-tools)** - Query your project history with natural language
- **[Cloud Sync](https://docs.claude-mem.ai/cloud-sync)** - Back up your memories to cmem.ai — no daemon, the worker syncs on write

- **[Context Engineering](https://docs.claude-mem.ai/context-engineering)** - AI agent context optimization principles
- **[Progressive Disclosure](https://docs.claude-mem.ai/progressive-disclosure)** - Philosophy behind Claude-Mem's context priming strategy

- **[Overview](https://docs.claude-mem.ai/architecture/overview)** - System components & data flow
- **[Architecture Evolution](https://docs.claude-mem.ai/architecture-evolution)** - The journey from v3 to v5
- **[Hooks Architecture](https://docs.claude-mem.ai/hooks-architecture)** - How Claude-Mem uses lifecycle hooks
- **[Hooks Reference](https://docs.claude-mem.ai/architecture/hooks)** - Every hook entry explained
- **[Worker Service](https://docs.claude-mem.ai/architecture/worker-service)** - HTTP API & Bun management
- **[Database](https://docs.claude-mem.ai/architecture/database)** - SQLite schema & FTS5 search
- **[Search Architecture](https://docs.claude-mem.ai/architecture/search-architecture)** - Hybrid search with Chroma vector database

- **[Configuration](https://docs.claude-mem.ai/configuration)** - Environment variables & settings
- **[Development](https://docs.claude-mem.ai/development)** - Building, testing, contributing
- **[Troubleshooting](https://docs.claude-mem.ai/troubleshooting)** - Common issues & solutions

**Core Components:**

1. **Lifecycle Hooks** - SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop, SessionEnd. Each is one shell-free command, `claude-mem hook claude-code <event>`, run by a small launcher that the installer puts on PATH
2. **Smart Install** - Cached dependency checker (Setup hook on `claude --init` / `--maintenance`, plus `npx claude-mem install` / `repair`)
3. **Worker Service** - Local HTTP API with web viewer UI and search endpoints, managed by Bun
4. **SQLite Database** - Stores sessions, observations, summaries
5. **mem-search Skill** - Natural language queries with progressive disclosure
6. **Chroma Vector Database** - Hybrid semantic + keyword search for intelligent context retrieval

See [Architecture Overview](https://docs.claude-mem.ai/architecture/overview) for details.

Claude-Mem provides intelligent memory search through **4 MCP tools** following a token-efficient **3-layer workflow pattern**:

**The 3-Layer Workflow:**

1. **`search`** - Get compact index with IDs (\~50-100 tokens/result)
2. **`timeline`** - Get chronological context around interesting results
3. **`get_observations`** - Fetch full details ONLY for filtered IDs (\~500-1,000 tokens/result)

**How It Works:**

- Claude uses MCP tools to search your memory
- Start with `search` to get an index of results
- Use `timeline` to see what was happening around specific observations
- Use `get_observations` to fetch full details for relevant IDs
- **\~10x token savings** by filtering before fetching details

**Available MCP Tools:**

1. **`search`** - Search memory index with full-text queries, filters by type/date/project
2. **`timeline`** - Get chronological context around a specific observation or query
3. **`get_observations`** - Fetch full observation details by IDs (always batch multiple IDs)

**Example Usage:**

```
// Step 1: Search for index
search(query="authentication bug", type="bugfix", limit=10)
// Step 2: Review index, identify relevant IDs (e.g., #123, #456)
// Step 3: Fetch full details
get_observations(ids=[123, 456])
```
See [Search Tools Guide](https://docs.claude-mem.ai/usage/search-tools) for detailed examples.

- **Node.js**: 20.0.0 or higher
- **Claude Code**: Latest version with plugin support
- **Bun**: JavaScript runtime and process manager (auto-installed if missing)
- **uv**: Python package manager for vector search (auto-installed if missing)
- **SQLite 3**: For persistent storage (bundled)

If you see an error like:

`npm : The term 'npm' is not recognized as the name of a cmdlet`
Make sure Node.js and npm are installed and added to your PATH. Download the latest Node.js installer from [https://nodejs.org](https://nodejs.org) and restart your terminal after installation.

Claude Code hooks do not need Git Bash. Each hook runs `claude-mem` directly, and `npx claude-mem install` places that launcher at `%LOCALAPPDATA%\claude-mem\bin\claude-mem.exe` and adds the folder to your user Path. Restart your terminal or IDE afterwards so Claude Code picks up the new Path. If hooks report `Executable not found in $PATH: "claude-mem"`, run `npx claude-mem doctor` and see [Troubleshooting](https://docs.claude-mem.ai/troubleshooting#claude-mem-command-not-found-in-hooks).

Settings are managed in `~/.claude-mem/settings.json` (auto-created with defaults on first run). Configure AI model, worker port, data directory, log level, and context injection settings.

To include observations from every harness in Claude Code and Codex SessionStart context, set `"CLAUDE_MEM_SESSION_START_INCLUDE_ALL_SOURCES": "true"` in that file, or enable **Include all sources at session start** in the viewer settings. The default is `"false"`, which limits startup context to the current harness. The observation count limit still applies across the selected sources.

See the **[Configuration Guide](https://docs.claude-mem.ai/configuration)** for all available settings and examples.

Claude-Mem supports multiple workflow modes and languages via the `CLAUDE_MEM_MODE` setting.

This option controls both:

- The workflow behavior (e.g. code, chill, investigation)
- The language used in generated observations

Edit your settings file at `~/.claude-mem/settings.json`:

```
{
  "CLAUDE_MEM_MODE": "code--zh"
}
```
Modes are defined in `plugin/modes/`. To see all available modes locally:

`ls ~/.claude/plugins/marketplaces/thedotmack/plugin/modes/`
| Mode | Description | 
|---|---|
| `code` | Default English mode | 
| `code--zh` | Simplified Chinese mode | 
| `code--ja` | Japanese mode | 

Language-specific modes follow the pattern `code--[lang]` where `[lang]` is the ISO 639-1 language code (e.g., `zh` for Chinese, `ja` for Japanese, `es` for Spanish).

Note: `code--zh` (Simplified Chinese) is already built-in — no additional installation or plugin update is required.


See the **[Development Guide](https://docs.claude-mem.ai/development)** for build instructions, testing, and contribution workflow.

If experiencing issues, describe the problem to Claude and the troubleshoot skill will automatically diagnose and provide fixes.

See the **[Troubleshooting Guide](https://docs.claude-mem.ai/troubleshooting)** for common issues and solutions.

Create comprehensive bug reports with the automated generator:

```
cd ~/.claude/plugins/marketplaces/thedotmack
npm run bug-report
```
Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Update documentation
5. Submit a Pull Request against `main`

Releases ship from `main` and are published to npm.

See [Development Guide](https://docs.claude-mem.ai/development) for contribution workflow.

Claude-Mem is licensed under the Apache License 2.0.

We chose Apache-2.0 because durable agentic memory should be easy to embed in developer tools, local agents, MCP servers, enterprise systems, robotics stacks, and production agent harnesses.

See the [LICENSE](https://github.com/thedotmack/claude-mem/blob/main/LICENSE) file for full details. See [docs/license.md](https://github.com/thedotmack/claude-mem/blob/main/docs/license.md)
and [docs/ip-boundary.md](https://github.com/thedotmack/claude-mem/blob/main/docs/ip-boundary.md) for licensing scope and the
open/commercial boundary.

- **Documentation**: [docs/](https://github.com/thedotmack/claude-mem/blob/main/docs)
- **Issues**: [GitHub Issues](https://github.com/thedotmack/claude-mem/issues)
- **Repository**: [github.com/thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
- **Official X Account**: [@Claude\_Memory](https://x.com/Claude_Memory)
- **Official Discord**: [Join Discord](https://discord.com/invite/J4wttp9vDu)
- **Author**: Alex Newman ([@thedotmack](https://github.com/thedotmack))

**Built with Claude Agent SDK** | **Works with Claude Code** | **Made with TypeScript**

CMEM is a token created by a 3rd party but officially embraced by the creator of Claude-Mem (Alex Newman, @thedotmack). The token acts as a community catalyst for growth and a vehicle for bringing CMEM to the developers and knowledge workers that need it most.

Official BASE CA: 0x76b1967eec0ccaeb001bbbb2b40dc4badba31ba3
