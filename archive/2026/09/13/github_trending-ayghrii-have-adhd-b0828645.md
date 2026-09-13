---
title: "ayghri/i-have-adhd"
source: GitHub Trending
url: https://github.com/ayghri/i-have-adhd
date: 2026-09-13
published_at: 2026-09-13T07:06:42.469082+00:00
tag: 工具开源
item_id: b08286459381f378
---
![i-have-adhd](https://github.com/ayghri/i-have-adhd/raw/main/logo.png)


  **ADHD-friendly outputs. No ADHD diagnosis needed!**

  

  **🇬🇧** ·
  [🇨🇳](https://github.com/ayghri/i-have-adhd/blob/main/.github/readme/README.zh-CN.md) ·
  [🇧🇷](https://github.com/ayghri/i-have-adhd/blob/main/.github/readme/README.pt-BR.md) ·
  [🇯🇵](https://github.com/ayghri/i-have-adhd/blob/main/.github/readme/README.ja.md) ·
  [🇻🇳](https://github.com/ayghri/i-have-adhd/blob/main/.github/readme/README.vi.md) ·
  [🇰🇷](https://github.com/ayghri/i-have-adhd/blob/main/.github/readme/README.ko.md) ·
  [🇹🇭](https://github.com/ayghri/i-have-adhd/blob/main/.github/readme/README.th.md)

Copy/paste into your CLI prompt:

```
Install the i-have-adhd skill/plugin from https://github.com/ayghri/i-have-adhd, refer to the repo's AGENTS.md for instructions.
```
Or 🔗 [check the installation instructions](https://github.com/ayghri/i-have-adhd/blob/main/INSTALL.md).

A skill for your coding assistant that stops it from burying the answer. Action first. Steps numbered. No "Hope this helps!"

|   |  `src/auth.ts``verifyToken` (lines 42–58) with the snippet below`npm test -- auth.spec.ts` | 

10 rules. Full text in [SKILL.md](https://github.com/ayghri/i-have-adhd/blob/main/skills/i-have-adhd/SKILL.md).

1. Lead with the next action.
2. Number multi-step tasks.
3. End with one concrete next step.
4. Suppress tangents.
5. Restate state every turn.
6. Specific time estimates (minutes, not "a bit").
7. Make wins visible.
8. Matter-of-fact errors.
9. Cap lists to 5 items.
10. No preamble. No recap. No closers.

Fork, edit `skills/i-have-adhd/SKILL.md`, then swap your copy in:

```
claude plugin uninstall i-have-adhd            # drop the upstream copy first:
claude plugin marketplace remove i-have-adhd   # fork and upstream share both names
claude plugin marketplace add <your-username>/i-have-adhd
claude plugin install i-have-adhd@i-have-adhd
```
Restart Claude Code, then re-invoke `/i-have-adhd`.

Loosely based on *The Adult ADHD Tool Kit* by J. Russell Ramsay and Anthony L. Rostain. Adapted for how an LLM should respond, not how a human should organize their day.

MIT.

Star ⭐ if it saved you one scroll past one "Great question!"
