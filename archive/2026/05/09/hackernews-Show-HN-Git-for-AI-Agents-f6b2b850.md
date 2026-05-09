---
title: "Show HN: Git for AI Agents"
source: Hacker News
url: https://github.com/regent-vcs/re_gent
date: 2026-05-09
published_at: 2026-05-08T14:15:36+00:00
tag: 工具开源
item_id: f6b2b8506a3ed220
---
![re_gent](/regent-vcs/re_gent/raw/main/assets/regent-logo-dark.png)

Version control for AI agent activity. Track what your agent did, which prompt wrote each line, and rewind when things break.

```
# Install via Homebrew (macOS/Linux)
brew tap regent-vcs/tap
brew install regent
# Or via Go
go install github.com/regent-vcs/regent/cmd/rgt@latest
# Initialize in your project
cd your-project
rgt init
# Work with Claude Code normally (every tool call is tracked)
# See what happened
rgt log
rgt blame src/file.go:42
```

That's it. Your agent activity is now auditable.

```
$ rgt log
Step a1b2c3d | 2 min ago | Tool: Edit
│ File: src/handler.go
│ Added error handling to request handler
│ + 5 lines, - 2 lines
Step d4e5f6g | 5 min ago | Tool: Write
│ File: tests/handler_test.go
│ Created unit tests for handler
│ + 23 lines
Step f8g9h0i | 8 min ago | Tool: Bash
│ Command: go mod tidy
│ Cleaned up dependencies
```

```
$ rgt blame src/handler.go:42
Line 42: func handleRequest(w http.ResponseWriter, r *http.Request) {
Step: a1b2c3d4e5f6
Session: claude-20260502-143021
Tool: Edit
Prompt: "Add error handling to the request handler"
```

```
$ rgt sessions
Active Sessions:
claude-20260502-143021 | 3 steps | Last: 2 min ago
claude-20260502-091534 | 7 steps | Last: 2 hours ago
$ rgt log --session claude-20260502-143021
# Filter history by session
```

```
$ rgt show a1b2c3d
Step a1b2c3d4e5f6
Parent: d4e5f6g7h8i9
Session: claude-20260502-143021
Time: 2026-05-02 14:30:21
Tool: Edit
File: src/handler.go
Changes:
+ func handleRequest(w http.ResponseWriter, r *http.Request) {
+ if r.Method != "GET" {
+ http.Error(w, "Method not allowed", 405)
+ return
+ }
- func handleRequest(w http.ResponseWriter, r *http.Request) {
Conversation:
User: "Add error handling to reject non-GET requests"
Assistant: "I'll add method validation to the handler..."
```

**The problem:** AI agents have no version control of their own.

You know this pain:

*"It was working five minutes ago"**"Why did you change that file?"**"Go back to before the refactor"*`/compact`

and pray- Copy-pasting code into a fresh chat

**The solution:** Three primitives that should already exist:

— what did this session do?`rgt log`

— which prompt wrote this line?`rgt blame`

— restore to any previous step (coming soon)`rgt rewind`


We gave agents write access to our codebases. We did not give ourselves git for it. re_gent fixes that.

re_gent stores agent activity in `.regent/`

(like `.git/`

):

```
.regent/
├── objects/ # Content-addressed blobs (BLAKE3)
├── refs/ # Session pointers (one per agent)
├── index.db # SQLite query index
└── config.toml
```


Every tool call creates a **Step**:

```
Step {
parent: <previous-step-hash>
tree: <workspace-snapshot>
transcript: <conversation-delta>
cause: {
tool_name: "Edit"
args: <what-changed>
result: <tool-output>
}
session_id: "claude-20260502-143021"
timestamp: "2026-05-02T14:30:21Z"
}
```

Steps form a **DAG**. Each session has its own branch. Common ancestors dedupe. You get git-level auditability for agent activity.

**Technical details:** See [POC.md](https://github.com/regent-vcs/re_gent/blob/main/POC.md) for the complete specification.

```
brew tap regent-vcs/tap
brew install regent
```

This installs both `regent`

and `rgt`

commands (they're identical) and automatically sets up shell completions for bash, zsh, and fish.

`go install github.com/regent-vcs/regent/cmd/rgt@latest`

This installs the `rgt`

command.

**Shell Completion (manual setup):**

```
# Bash
rgt completion bash > /usr/local/etc/bash_completion.d/rgt
# Zsh
rgt completion zsh > "${fpath[1]}/_rgt"
# Fish
rgt completion fish > ~/.config/fish/completions/rgt.fish
```

```
git clone https://github.com/regent-vcs/regent
cd regent
go build -o rgt ./cmd/rgt
sudo mv rgt /usr/local/bin/
# Optionally create a symlink: sudo ln -s /usr/local/bin/rgt /usr/local/bin/regent
```

For shell completion, follow the "Via Go Install" instructions above.

Download pre-built binaries from [GitHub Releases](https://github.com/regent-vcs/regent/releases)

Get inline blame annotations directly in your editor:

**Installation Options:**

```
# 1. From VSIX (Recommended)
# Download the latest .vsix from:
# https://github.com/regent-vcs/vscode-regent/releases
# Then in VS Code: Extensions > ... > Install from VSIX...
# 2. From VS Code Marketplace (Coming Soon)
# Search for "re_gent Blame"
# 3. From source (Development)
git clone https://github.com/regent-vcs/vscode-regent
cd vscode-regent
npm install && npm run compile
# Press F5 in VS Code to launch Extension Development Host
```

**Features:**

- Inline blame annotations showing which step modified each line
- Hover tooltips with full step context (timestamp, tool name, arguments)
- Session timeline view in the sidebar
- One-click access to conversation history
- Direct SQLite integration—no subprocess overhead

**Requirements:** re_gent CLI must be installed and `rgt init`

run in your project.

**Available Now:**

| Command | Description |
|---|---|
`rgt init` |
Initialize `.regent/` in current directory |
`rgt log` |
Show step history (supports `--session` , `-n` , `--since` ) |
`rgt sessions` |
List all active sessions |
`rgt status` |
Show current repository state |
`rgt show <step>` |
Display full context for a step (tool call + conversation) |
`rgt blame <path>[:<line>]` |
Show per-line provenance for a file |
`rgt cat <hash>` |
Inspect any object by hash (debug) |
`rgt version` |
Print version information |
`rgt completion` |
Generate shell completion scripts |

**Coming Soon:**

| Command | Description |
|---|---|
`rgt rewind <step>` |
Non-destructive time-travel |
`rgt gc` |
Garbage collection |
`rgt fork <step>` |
Create a new session from a step |

**Content-Addressed Storage**— BLAKE3 hashing, automatic deduplication**Fast Queries**— SQLite index, sub-10ms lookups**Per-Session DAG**— Concurrent agents, no conflicts**Conversation Tracking**— Survives`/compact`

and`/clear`

**Hook-Driven**— Transparent Claude Code integration**Concurrency-Safe**— CAS refs, ACID transactions**Gitignore-Compatible**—`.regentignore`

support

| Git | re_gent | |
|---|---|---|
Tracks code |
✅ | ✅ |
Tracks agent activity |
❌ | ✅ |
Blame with prompt |
❌ | ✅ |
Conversation history |
❌ | ✅ |
Concurrent sessions |
✅ separate branches | |
Purpose |
Developer VCS | Agent audit trail |

**re_gent complements git, doesn't replace it.** Use both.

**Active Development**

- ~7.8k LOC Go implementation
- Core functionality: init, log, sessions, status, show, blame —
**COMPLETE** - Hook integration (Claude Code) —
**COMPLETE** - Used daily by contributors
- Not yet v1.0

**Honest assessment:** Production-quality code at POC-level feature completeness. We're building in public.

Contributions are welcome! re_gent is built in public and we actively review PRs.

**Quick Start:**

- Read
[QUICK_START.md](https://github.com/regent-vcs/re_gent/blob/main/.github/QUICK_START.md)for a 5-minute setup guide - Check
[good first issues](https://github.com/regent-vcs/regent/labels/good%20first%20issue) - Full guidelines:
[CONTRIBUTING.md](https://github.com/regent-vcs/re_gent/blob/main/CONTRIBUTING.md)

**Before opening a PR:**

- Tests pass:
`go test ./...`

and`go test -race ./...`

- Linter passes:
`golangci-lint run`

- Code formatted:
`go fmt ./...`

- PR template filled out

**Important files:**

[CONTRIBUTING.md](https://github.com/regent-vcs/re_gent/blob/main/CONTRIBUTING.md)— Full contribution guide[SUPPORT.md](https://github.com/regent-vcs/re_gent/blob/main/SUPPORT.md)— Support and help resources[TESTING.md](https://github.com/regent-vcs/re_gent/blob/main/TESTING.md)— Testing guide and strategy[CLAUDE.md](https://github.com/regent-vcs/re_gent/blob/main/CLAUDE.md)— Project context and architecture[POC.md](https://github.com/regent-vcs/re_gent/blob/main/POC.md)— Technical specification

[cobra](https://github.com/spf13/cobra)— CLI framework[blake3](https://lukechampine.com/blake3)— BLAKE3 hashing[go-diff](https://github.com/sergi/go-diff)— Myers diff[modernc.org/sqlite](https://modernc.org/sqlite)— Pure Go SQLite

Built by contributors
