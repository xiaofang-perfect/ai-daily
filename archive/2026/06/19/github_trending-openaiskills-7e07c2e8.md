---
title: "openai/skills"
source: GitHub Trending
url: https://github.com/openai/skills
date: 2026-06-19
published_at: 2026-06-19T07:03:05.076061+00:00
tag: 工具开源
item_id: 7e07c2e8573c27a6
---
Agent Skills are folders of instructions, scripts, and resources that AI agents can discover and use to perform at specific tasks. Write once, use everywhere.

Codex uses skills to help package capabilities that teams and individuals can use to complete specific tasks in a repeatable way. This repository catalogs skills for use and distribution with Codex.

Learn more:

Skills in [ .system](https://github.com/openai/skills/blob/main/skills/.system) are automatically installed in the latest version of Codex.

To install [curated](https://github.com/openai/skills/blob/main/skills/.curated) or [experimental](https://github.com/openai/skills/blob/main/skills/.experimental) skills, you can use the `$skill-installer` inside Codex.

Curated skills can be installed by name (defaults to `skills/.curated`):

```
$skill-installer gh-address-comments
```
For experimental skills, specify the skill folder. For example:

```
$skill-installer install the create-plan skill from the .experimental folder
```
Or provide the GitHub directory URL:

```
$skill-installer install https://github.com/openai/skills/tree/main/skills/.experimental/create-plan
```
After installing a skill, restart Codex to pick up new skills.

The license of an individual skill can be found directly inside the skill's directory inside the `LICENSE.txt` file.
