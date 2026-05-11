---
title: "addyosmani/agent-skills"
source: GitHub Trending
url: https://github.com/addyosmani/agent-skills
date: 2026-05-11
published_at: 2026-05-11T05:56:25.477838+00:00
tag: 工具开源
item_id: c987a254c8f86cb4
---
**Production-grade engineering skills for AI coding agents.**

Skills encode the workflows, quality gates, and best practices that senior engineers use when building software. These ones are packaged so AI agents follow them consistently across every phase of development.

```
DEFINE PLAN BUILD VERIFY REVIEW SHIP
┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐
│ Idea │ ───▶ │ Spec │ ───▶ │ Code │ ───▶ │ Test │ ───▶ │ QA │ ───▶ │ Go │
│Refine│ │ PRD │ │ Impl │ │Debug │ │ Gate │ │ Live │
└──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘
/spec /plan /build /test /review /ship
```


7 slash commands that map to the development lifecycle. Each one activates the right skills automatically.

| What you're doing | Command | Key principle |
|---|---|---|
| Define what to build | `/spec` |
Spec before code |
| Plan how to build it | `/plan` |
Small, atomic tasks |
| Build incrementally | `/build` |
One slice at a time |
| Prove it works | `/test` |
Tests are proof |
| Review before merge | `/review` |
Improve code health |
| Simplify the code | `/code-simplify` |
Clarity over cleverness |
| Ship to production | `/ship` |
Faster is safer |

Skills also activate automatically based on what you're doing — designing an API triggers `api-and-interface-design`

, building UI triggers `frontend-ui-engineering`

, and so on.

**Claude Code (recommended)**

**Marketplace install:**

```
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills
```



SSH errors?The marketplace clones repos via SSH. If you don't have SSH keys set up on GitHub, either[add your SSH key]or use the full HTTPS URL to force the HTTPS cloning:/plugin marketplace add https://github.com/addyosmani/agent-skills.git /plugin install agent-skills@addy-agent-skills

**Local / development:**

```
git clone https://github.com/addyosmani/agent-skills.git
claude --plugin-dir /path/to/agent-skills
```

**Cursor**

Copy any `SKILL.md`

into `.cursor/rules/`

, or reference the full `skills/`

directory. See [docs/cursor-setup.md](https://github.com/addyosmani/agent-skills/blob/main/docs/cursor-setup.md).

**Gemini CLI**

Install as native skills for auto-discovery, or add to `GEMINI.md`

for persistent context. See [docs/gemini-cli-setup.md](https://github.com/addyosmani/agent-skills/blob/main/docs/gemini-cli-setup.md).

**Install from the repo:**

`gemini skills install https://github.com/addyosmani/agent-skills.git --path skills`

**Install from a local clone:**

`gemini skills install ./agent-skills/skills/`

**Windsurf**

Add skill contents to your Windsurf rules configuration. See [docs/windsurf-setup.md](https://github.com/addyosmani/agent-skills/blob/main/docs/windsurf-setup.md).

**OpenCode**

Uses agent-driven skill execution via AGENTS.md and the `skill`

tool.

**GitHub Copilot**

Use agent definitions from `agents/`

as Copilot personas and skill content in `.github/copilot-instructions.md`

. See [docs/copilot-setup.md](https://github.com/addyosmani/agent-skills/blob/main/docs/copilot-setup.md).

**Kiro IDE & CLI **

Skills for Kiro reside under ".kiro/skills/" and can be stored under Project or Global level. Kiro also supports Agents.md. See Kiro docs at [https://kiro.dev/docs/skills/](https://kiro.dev/docs/skills/)

**Codex / Other Agents**

Skills are plain Markdown - they work with any agent that accepts system prompts or instruction files. See [docs/getting-started.md](https://github.com/addyosmani/agent-skills/blob/main/docs/getting-started.md).

The commands above are entry points. The pack includes 22 skills total — 21 lifecycle skills plus the `using-agent-skills`

meta-skill. Each skill is a structured workflow with steps, verification gates, and anti-rationalization tables. You can also reference any skill directly.

| Skill | What It Does | Use When |
|---|---|---|
|

| Skill | What It Does | Use When |
|---|---|---|
|

[spec-driven-development](https://github.com/addyosmani/agent-skills/blob/main/skills/spec-driven-development/SKILL.md)| Skill | What It Does | Use When |
|---|---|---|
|

| Skill | What It Does | Use When |
|---|---|---|
|

[test-driven-development](https://github.com/addyosmani/agent-skills/blob/main/skills/test-driven-development/SKILL.md)[context-engineering](https://github.com/addyosmani/agent-skills/blob/main/skills/context-engineering/SKILL.md)[source-driven-development](https://github.com/addyosmani/agent-skills/blob/main/skills/source-driven-development/SKILL.md)[doubt-driven-development](https://github.com/addyosmani/agent-skills/blob/main/skills/doubt-driven-development/SKILL.md)[frontend-ui-engineering](https://github.com/addyosmani/agent-skills/blob/main/skills/frontend-ui-engineering/SKILL.md)[api-and-interface-design](https://github.com/addyosmani/agent-skills/blob/main/skills/api-and-interface-design/SKILL.md)| Skill | What It Does | Use When |
|---|---|---|
|

[debugging-and-error-recovery](https://github.com/addyosmani/agent-skills/blob/main/skills/debugging-and-error-recovery/SKILL.md)| Skill | What It Does | Use When |
|---|---|---|
|

[code-simplification](https://github.com/addyosmani/agent-skills/blob/main/skills/code-simplification/SKILL.md)[security-and-hardening](https://github.com/addyosmani/agent-skills/blob/main/skills/security-and-hardening/SKILL.md)[performance-optimization](https://github.com/addyosmani/agent-skills/blob/main/skills/performance-optimization/SKILL.md)| Skill | What It Does | Use When |
|---|---|---|
|

[ci-cd-and-automation](https://github.com/addyosmani/agent-skills/blob/main/skills/ci-cd-and-automation/SKILL.md)[deprecation-and-migration](https://github.com/addyosmani/agent-skills/blob/main/skills/deprecation-and-migration/SKILL.md)[documentation-and-adrs](https://github.com/addyosmani/agent-skills/blob/main/skills/documentation-and-adrs/SKILL.md)*why*[shipping-and-launch](https://github.com/addyosmani/agent-skills/blob/main/skills/shipping-and-launch/SKILL.md)Pre-configured specialist personas for targeted reviews:

| Agent | Role | Perspective |
|---|---|---|
|

[test-engineer](https://github.com/addyosmani/agent-skills/blob/main/agents/test-engineer.md)[security-auditor](https://github.com/addyosmani/agent-skills/blob/main/agents/security-auditor.md)Quick-reference material that skills pull in when needed:

| Reference | Covers |
|---|---|
|

[security-checklist.md](https://github.com/addyosmani/agent-skills/blob/main/references/security-checklist.md)[performance-checklist.md](https://github.com/addyosmani/agent-skills/blob/main/references/performance-checklist.md)[accessibility-checklist.md](https://github.com/addyosmani/agent-skills/blob/main/references/accessibility-checklist.md)Every skill follows a consistent anatomy:

```
┌─────────────────────────────────────────────────┐
│ SKILL.md │
│ │
│ ┌─ Frontmatter ─────────────────────────────┐ │
│ │ name: lowercase-hyphen-name │ │
│ │ description: Guides agents through [task].│ │
│ │ Use when… │ │
│ └───────────────────────────────────────────┘ │
│ Overview → What this skill does │
│ When to Use → Triggering conditions │
│ Process → Step-by-step workflow │
│ Rationalizations → Excuses + rebuttals │
│ Red Flags → Signs something's wrong │
│ Verification → Evidence requirements │
└─────────────────────────────────────────────────┘
```


**Key design choices:**

**Process, not prose.**Skills are workflows agents follow, not reference docs they read. Each has steps, checkpoints, and exit criteria.**Anti-rationalization.**Every skill includes a table of common excuses agents use to skip steps (e.g., "I'll add tests later") with documented counter-arguments.**Verification is non-negotiable.**Every skill ends with evidence requirements - tests passing, build output, runtime data. "Seems right" is never sufficient.**Progressive disclosure.**The`SKILL.md`

is the entry point. Supporting references load only when needed, keeping token usage minimal.

```
agent-skills/
├── skills/ # 22 skills (21 lifecycle + 1 meta)
│ ├── idea-refine/ # Define
│ ├── spec-driven-development/ # Define
│ ├── planning-and-task-breakdown/ # Plan
│ ├── incremental-implementation/ # Build
│ ├── context-engineering/ # Build
│ ├── source-driven-development/ # Build
│ ├── doubt-driven-development/ # Build
│ ├── frontend-ui-engineering/ # Build
│ ├── test-driven-development/ # Build
│ ├── api-and-interface-design/ # Build
│ ├── browser-testing-with-devtools/ # Verify
│ ├── debugging-and-error-recovery/ # Verify
│ ├── code-review-and-quality/ # Review
│ ├── code-simplification/ # Review
│ ├── security-and-hardening/ # Review
│ ├── performance-optimization/ # Review
│ ├── git-workflow-and-versioning/ # Ship
│ ├── ci-cd-and-automation/ # Ship
│ ├── deprecation-and-migration/ # Ship
│ ├── documentation-and-adrs/ # Ship
│ ├── shipping-and-launch/ # Ship
│ └── using-agent-skills/ # Meta: how to use this pack
├── agents/ # 3 specialist personas
├── references/ # 4 supplementary checklists
├── hooks/ # Session lifecycle hooks
├── .claude/commands/ # 7 slash commands (Claude Code)
├── .gemini/commands/ # 7 slash commands (Gemini CLI)
└── docs/ # Setup guides per tool
```


AI coding agents default to the shortest path - which often means skipping specs, tests, security reviews, and the practices that make software reliable. Agent Skills gives agents structured workflows that enforce the same discipline senior engineers bring to production code.

Each skill encodes hard-won engineering judgment: *when* to write a spec, *what* to test, *how* to review, and *when* to ship. These aren't generic prompts - they're the kind of opinionated, process-driven workflows that separate production-quality work from prototype-quality work.

Skills bake in best practices from Google's engineering culture — including concepts from [Software Engineering at Google](https://abseil.io/resources/swe-book) and Google's [engineering practices guide](https://google.github.io/eng-practices/). You'll find Hyrum's Law in API design, the Beyonce Rule and test pyramid in testing, change sizing and review speed norms in code review, Chesterton's Fence in simplification, trunk-based development in git workflow, Shift Left and feature flags in CI/CD, and a dedicated deprecation skill treating code as a liability. These aren't abstract principles — they're embedded directly into the step-by-step workflows agents follow.

Skills should be **specific** (actionable steps, not vague advice), **verifiable** (clear exit criteria with evidence requirements), **battle-tested** (based on real workflows), and **minimal** (only what's needed to guide the agent).

See [docs/skill-anatomy.md](https://github.com/addyosmani/agent-skills/blob/main/docs/skill-anatomy.md) for the format specification and [CONTRIBUTING.md](https://github.com/addyosmani/agent-skills/blob/main/CONTRIBUTING.md) for guidelines.

MIT - use these skills in your projects, teams, and tools.
