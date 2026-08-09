---
title: "google/skills"
source: GitHub Trending
url: https://github.com/google/skills
date: 2026-08-09
published_at: 2026-08-09T03:29:35.772382+00:00
tag: 工具开源
item_id: 6340b6a4b6de6999
---
This repository contains [Agent Skills](https://agentskills.io/home) for Google
products and technologies, including [Google Cloud](https://cloud.google.com).

Note

This repository is under active development.

`npx skills add google/skills`
From the `npx install` command, you can select the specific skills from this
repo to install.

This repo also bundles Google product plugins (Skills + MCP servers) for agent harnesses.

| Agent harness | Install | 
|---|---|
| **Claude Code** | `claude plugin marketplace add google/skills` , then`claude plugin install <plugin>@google-plugins` | 
| **Codex** | `codex plugin marketplace add google/skills` , then install from the`/plugins` browser | 
| **Antigravity CLI** | `agy plugin install https://github.com/google/skills/<plugin-path>` | 

If you need help or encounter issues with these skills, search for existing
issues or open a new one in the
[GitHub Issue Tracker](https://github.com/google/skills/issues).

We welcome contributions to improve our skills. You can help by:

- [Reporting bugs or inaccuracies](https://github.com/google/skills/issues) in
the skill Markdown files.
- Suggesting new skills to add to this repository (for example, Google technologies or recipes) by filing a feature request.

You are free to copy, modify, and distribute these skills under the terms of the
Apache 2.0 license. See the `LICENSE` file for details.
