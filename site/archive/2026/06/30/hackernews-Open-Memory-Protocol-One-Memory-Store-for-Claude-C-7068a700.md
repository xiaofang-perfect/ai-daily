---
title: "Open Memory Protocol – One Memory Store for Claude, ChatGPT, Curso"
source: Hacker News
url: https://github.com/SMJAI/open-memory-protocol
date: 2026-06-30
published_at: 2026-06-30T00:05:33+00:00
tag: 工具开源
item_id: 7068a700fb6c39ad
---
An open standard for portable, interoperable AI memory across tools, sessions, and devices.




Every AI tool remembers you differently — and only within its own walls.

- **Claude**knows what you told it yesterday. Cursor doesn't.
- **ChatGPT**learned your preferences. Your custom agent hasn't.
- **Copilot**saw your code style. Your terminal AI is starting from zero.

Every time you switch tools, your AI forgets you. You repeat yourself. Context is lost. The AI that was finally starting to *know* you resets to a stranger.

This is the **AI memory silo problem**. And it has the same solution as every silo problem before it: an open protocol.

**Open Memory Protocol** is a vendor-neutral specification for how AI tools store, retrieve, and share memory about users and their context.

It is:

- **A specification**— a precise definition of memory objects, storage format, and HTTP API
- **A reference server**— self-hostable, open-source, runs in Docker in one command
- **A set of SDKs**— TypeScript and Python libraries for building OMP-compatible tools
- **A set of adapters**— plug-ins for Claude (MCP), OpenAI, Cursor, and more

Any AI tool that implements OMP can instantly share memory with any other OMP-compatible tool.


Requirements:Node.js 22 or newer

`npx omp-server`Or with Docker:

`docker run -p 3456:3456 -v omp-data:/data ghcr.io/smjai/omp-server`Your server is now running at `http://localhost:3456`. Test it:

```
curl http://localhost:3456/v1/health
# {"status":"ok","version":"0.1","compliance":"OMP-Core","memories_count":0}
```
Find your Claude Desktop config file:

- **macOS:**- `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:**- `%APPDATA%\Claude\claude_desktop_config.json`
- **Windows (Store app):**- `%LOCALAPPDATA%\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\claude_desktop_config.json`

Add to it:

```
{
  "mcpServers": {
    "omp": {
      "command": "npx",
      "args": ["omp-mcp"],
      "env": {
        "OMP_SERVER": "http://localhost:3456",
        "OMP_API_KEY": "your-omp-key"
      }
    }
  }
}
```
To enable AI-powered memory extraction and compression, also set these on the server:

```
OMP_AI_PROVIDER=anthropic   # or "openai"
OMP_AI_API_KEY=sk-ant-...   # your Anthropic or OpenAI key
```
Without a system prompt, you have to ask Claude to use OMP tools manually. To make it automatic, create a **Project** in Claude Desktop and add this system prompt:

```
You have access to OMP memory tools (omp_remember, omp_recall, omp_list).
At the start of every conversation, use omp_recall to search for memories 
relevant to what the user is asking about.
Whenever the user shares anything worth remembering — preferences, decisions, 
projects, facts about themselves — automatically use omp_remember to save it 
without being asked.
Never tell the user you are saving a memory. Just do it silently.
```
This makes OMP invisible — Claude just remembers, automatically, across every session.

The **OMP Bridge browser extension** makes this seamless. No copying JSON, no manual steps.

**How it works:**

- Chat with ChatGPT about anything
- The extension silently saves your conversation to your OMP server every 2 minutes
- Open Claude.ai (or any other AI) to start a new chat
- A toast notification appears: **"Continue from ChatGPT? [topic]"**
- Click **"Continue in Claude"**— OMP generates a natural handoff brief and injects it
- Claude responds as if it was in the conversation the whole time

You can also save manually at any point: click the OMP Bridge extension icon → **"Save this conversation to OMP"**.

The handoff brief (AI-generated) looks like:

```
We were exploring MCP (Model Context Protocol) with ChatGPT — specifically what it
is, how it compares to function calling, and why it's more portable across providers.
I'm ready to go deeper on real-world implementations. Can you show me how to build
an MCP server from scratch?
```
**API — save and replay conversations programmatically:**

```
# Save a conversation
curl -X POST http://localhost:3456/v1/conversations \
  -H "Content-Type: application/json" \
  -d '{
    "model": "chatgpt",
    "topic": "MCP deep dive",
    "messages": [
      {"role": "user", "content": "Tell me about MCP"},
      {"role": "assistant", "content": "MCP stands for..."}
    ]
  }'
# Generate a handoff brief for another model
curl -X POST http://localhost:3456/v1/handoff \
  -H "Content-Type: application/json" \
  -d '{
    "conversation_id": "conv_abc123",
    "target_model": "claude"
  }'
# → { "brief": "We were exploring MCP with ChatGPT...", "topic": "...", "source_model": "chatgpt" }
```
```
curl -X POST http://localhost:3456/v1/memories \
  -H "Content-Type: application/json" \
  -d '{
    "content": "User prefers TypeScript over JavaScript and dislikes verbose comments",
    "type": "semantic",
    "source": { "tool": "claude" },
    "tags": ["preferences", "coding"]
  }'
```
`curl "http://localhost:3456/v1/memories/search?q=coding+preferences"````
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Claude    │     │   Cursor    │     │  Your Agent │
│  (MCP)      │     │  (SDK)      │     │  (REST API) │
└──────┬──────┘     └──────┬──────┘     └──────┬──────┘
       │                   │                   │
       └───────────────────┼───────────────────┘
                           │
                  ┌────────▼────────┐
                  │   OMP Server    │
                  │  (self-hosted)  │
                  │                 │
                  │  ┌───────────┐  │
                  │  │  SQLite   │  │
                  │  │  / Pgvec  │  │
                  │  └───────────┘  │
                  └─────────────────┘
```
Every tool reads and writes to a single OMP server you control. One memory store. All tools. Zero silos.

OMP defines:

- **Memory Object**— the canonical schema for a memory (content, type, source, tags, timestamps, optional embedding)
- **Memory Types**—- `episodic`(events),- `semantic`(facts/preferences),- `procedural`(how-to knowledge)
- **REST API**— standard CRUD + semantic search endpoints
- **Authentication**— bearer token, per-tool API keys
- **Export/Import**— portable JSON format for moving memories between servers

Read the full specification: [SPEC.md](https://github.com/SMJAI/open-memory-protocol/blob/main/SPEC.md)

```
{
  "id": "mem_01j9xk2p3q4r5s6t",
  "content": "User is building a fintech startup, prefers clean architecture, dislikes over-engineering",
  "type": "semantic",
  "source": {
    "tool": "claude",
    "session_id": "sess_abc123",
    "timestamp": "2026-06-29T12:00:00Z"
  },
  "tags": ["profile", "preferences", "engineering"],
  "created_at": "2026-06-29T12:00:00Z",
  "updated_at": "2026-06-29T12:00:00Z",
  "expires_at": null
}
```
| Tool | Status | Install | 
|---|---|---|
| Claude (MCP) | ✅ Available | `npx omp-mcp` | 
| Browser Extension | ✅ Available | [Load unpacked](https://github.com/SMJAI/open-memory-protocol/blob/main/adapters/browser-extension)— Chrome/Edge/Brave | 
| OpenAI Assistants | 🙋 Help wanted | [Open issue](https://github.com/SMJAI/open-memory-protocol/issues) | 
| Cursor | 🙋 Help wanted | [Open issue](https://github.com/SMJAI/open-memory-protocol/issues) | 
| Copilot / VS Code | 🙋 Help wanted | [Open issue](https://github.com/SMJAI/open-memory-protocol/issues) | 
| Gemini | 🙋 Help wanted | [Open issue](https://github.com/SMJAI/open-memory-protocol/issues) | 
| Custom (REST) | ✅ Available | Any HTTP client | 

The browser extension brings OMP to the **web versions** of every AI tool with zero setup on their side.

**What it does:**

- Shows a floating 🧠 button on Claude.ai, ChatGPT, Gemini, and Perplexity
- Displays your OMP memories from your server
- One click to inject your memories into any chat — the AI instantly knows your context
- Works cross-model: inject the same memories into ChatGPT that Claude saved

**Install (Chrome / Edge / Brave):**

```
cd adapters/browser-extension
npm install && npm run build
```
Then open `chrome://extensions` → Enable **Developer mode** → **Load unpacked** → select the `adapters/browser-extension` folder.

**Want to build one?** An adapter is typically 100–200 lines — read [ CONTRIBUTING.md](https://github.com/SMJAI/open-memory-protocol/blob/main/CONTRIBUTING.md) and use 

[as a template.](https://github.com/SMJAI/open-memory-protocol/blob/main/adapters/claude-mcp)

`adapters/claude-mcp`The OMP API is plain REST — any HTTP client works out of the box. Typed SDKs are on the roadmap.

**Want to build one?** Python, Go, Rust, and Ruby SDKs are all needed. See [ CONTRIBUTING.md](https://github.com/SMJAI/open-memory-protocol/blob/main/CONTRIBUTING.md).

```
# Save a memory
curl -X POST http://localhost:3456/v1/memories \
  -H "Content-Type: application/json" \
  -d '{"content":"User prefers TypeScript","type":"semantic","source":{"tool":"myapp","timestamp":"2026-06-30T00:00:00Z"}}'
# Search memories
curl -X POST http://localhost:3456/v1/memories/search \
  -H "Content-Type: application/json" \
  -d '{"q":"TypeScript","limit":5}'
```
Your memories are yours. They should not be locked inside a company's database, used to train models without your consent, or lost when you switch tools.

OMP is designed on these principles:

- **Self-hosted first**— you run the server, you own the data
- **Vendor neutral**— no company controls the standard
- **Privacy by design**— memories never leave your server unless you export them
- **Portable**— import/export your full memory in one command

- v0.1 — Core spec, reference server, MCP adapter
- v0.2 — AI memory extraction, conversation compression, MCP resources + prompts
-  v0.3 — Cross-model conversation handoff (browser extension + `/v1/conversations`+`/v1/handoff`)
- v0.4 — Semantic search with embeddings, pgvector support
- v0.5 — Memory namespacing (per-project memories)
- v0.6 — Multi-user support, access control
- v1.0 — Stable spec, submitted to open standards body

OMP is community-driven. We need:

- **Adapter builders**— connect your favourite AI tool
- **SDK contributors**— Go, Rust, Java SDKs welcome
- **Spec reviewers**— read- [SPEC.md](https://github.com/SMJAI/open-memory-protocol/blob/main/SPEC.md)and open issues
- **Early adopters**— try it and report what breaks

See [CONTRIBUTING.md](https://github.com/SMJAI/open-memory-protocol/blob/main/CONTRIBUTING.md) to get started.

- **GitHub Discussions**— questions, ideas, feedback
- **Issues**— bugs and spec clarifications

Apache 2.0 — free to use, modify, and distribute. See [LICENSE](https://github.com/SMJAI/open-memory-protocol/blob/main/LICENSE).

Built by [SMJAI](https://github.com/SMJAI) and contributors.
