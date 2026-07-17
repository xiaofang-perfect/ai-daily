---
title: "Grok Build Coding Agent (GitHub Repo)"
source: TLDR AI · 2026-07-16
url: https://github.com/xai-org/grok-build?utm_source=tldrai
date: 2026-07-17
published_at: 2026-07-16T12:00:00+00:00
tag: 工具开源
item_id: 9607c2ab05bc30b1
---
# 
  
    
    
    ![SpaceXAI logo](https://camo.githubusercontent.com/a2ea4e957b3664d32c43a5ebde2791a55a4914238e125777c77a71ec8906724c/68747470733a2f2f6d656469612e782e61692f76312f776562736974652f73706163657861692d73796d626f6c2d626c61636b2d7472616e73706172656e742d36343335636634322e706e67) 

     

  Grok Build (`grok`)

**Grok Build** is SpaceXAI's terminal-based AI coding agent. It runs as a
full-screen TUI that understands your codebase, edits files, executes shell
commands, searches the web, and manages long-running tasks — interactively,
headlessly for scripting/CI, or embedded in editors via the Agent Client
Protocol (ACP).

[Installing the released binary](https://github.com#installing-the-released-binary) ·
[Building from source](https://github.com#building-from-source) ·
[Documentation](https://github.com#documentation) ·
[Repository layout](https://github.com#repository-layout) ·
[Development](https://github.com#development) ·
[Contributing](https://github.com#contributing) ·
[License](https://github.com#license)

**Learn more about Grok Build at  x.ai/cli**

This repository contains the Rust source for the `grok` CLI/TUI and its agent
runtime. It is synced periodically from the SpaceXAI monorepo.

A small `SOURCE_REV` file at the root records the full monorepo commit SHA
for the version of the code present in this tree.

Prebuilt binaries are published for macOS, Linux, and Windows:

```
curl -fsSL https://x.ai/cli/install.sh | bash   # macOS / Linux / Git Bash
irm https://x.ai/cli/install.ps1 | iex          # Windows PowerShell
grok --version
```
See the [changelog](https://x.ai/build/changelog) for the latest fixes,
features, and improvements in each release.

Requirements:

- 
**Rust**— the toolchain is pinned by`rust-toolchain.toml``rustup`installs it automatically on first build.
- 
[DotSlash](https://dotslash-cli.com)`bin/``bin/protoc``dotslash`is on your`PATH`**before**building:cargo install dotslash # or: prebuilt packages — https://dotslash-cli.com/docs/installation/ /usr/bin/env dotslash --help # sanity check 
- 
**protoc**— proto codegen resolves`bin/protoc``protoc`on`PATH`/`$PROTOC`.
- 
macOS and Linux are supported build hosts; Windows builds are best-effort and not currently tested from this tree. 

```
cargo run -p xai-grok-pager-bin              # build + launch the TUI
cargo build -p xai-grok-pager-bin --release  # release binary: target/release/xai-grok-pager
cargo check -p xai-grok-pager-bin            # fast validation
```
The binary artifact is named `xai-grok-pager`; official installs ship it as
`grok`. On first launch it opens your browser to authenticate — see the
[authentication guide](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/02-authentication.md).

Full online documentation is available at
[docs.x.ai/build/overview](https://docs.x.ai/build/overview).

The user guide ships with the pager crate:
[ crates/codegen/xai-grok-pager/docs/user-guide/](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide)
— getting started, keyboard shortcuts, slash commands, configuration, theming,
MCP servers, skills, plugins, hooks, headless mode, sandboxing, and more.

| Path | Contents | 
|---|---|
| `crates/codegen/xai-grok-pager-bin` | Composition-root package; builds the `xai-grok-pager`binary | 
| `crates/codegen/xai-grok-pager` | The TUI: scrollback, prompt, modals, rendering | 
| `crates/codegen/xai-grok-shell` | Agent runtime + leader/stdio/headless entry points | 
| `crates/codegen/xai-grok-tools` | Tool implementations (terminal, file edit, search, ...) | 
| `crates/codegen/xai-grok-workspace` | Host filesystem, VCS, execution, checkpoints | 
| `crates/codegen/...` | The rest of the CLI crate closure (config, MCP, markdown, sandbox, ...) | 
| `crates/common/`,`crates/build/`,`prod/mc/` | Small shared leaf crates pulled in by the closure | 
| `third_party/` | Vendored upstream source (Mermaid diagram stack) — see below | 

Important

The root `Cargo.toml` (workspace members, dependency versions, lints,
profiles) is **generated** — treat it as read-only. Prefer editing per-crate
`Cargo.toml` files.

```
cargo check -p <crate>        # always target specific crates; full-workspace builds are slow
cargo test -p xai-grok-config # per-crate tests
cargo clippy -p <crate>       # lint config: clippy.toml at the repo root
cargo fmt --all               # rustfmt.toml at the repo root
```
Note

External contributions are not accepted. See [ CONTRIBUTING.md](https://github.com/xai-org/grok-build/blob/main/CONTRIBUTING.md).

First-party code in this repository is licensed under the **Apache License,
Version 2.0** — see [ LICENSE](https://github.com/xai-org/grok-build/blob/main/LICENSE).

Third-party and vendored code remains under its original licenses. See:

- `THIRD-PARTY-NOTICES`- **in-tree source ports**(including openai/codex and sst/opencode tool implementations)
- `crates/codegen/xai-grok-tools/THIRD_PARTY_NOTICES.md`
- `third_party/NOTICE`
