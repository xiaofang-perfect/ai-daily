---
title: "mattpocock/skills"
source: GitHub Trending
url: https://github.com/mattpocock/skills
date: 2026-04-28
published_at: 2026-04-28T09:50:48.803635+00:00
tag: 工具开源
item_id: f8f314103a3f5b64
---
My agent skills that I use every day to do real engineering - not vibe coding.

Developing real applications is hard. Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control and make bugs in the process hard to resolve.

These skills are designed to be small, easy to adapt, and composable. They're based on decades of engineering experience. Hack around with them. Make them your own. Enjoy.

If you want to keep up with changes to these skills, and any new ones I create, you can join ~60,000 other devs on my newsletter:

- Run the skills.sh installer:

`npx skills@latest add mattpocock/skills`

-
Pick the skills you want, and which coding agents you want to install them on.

-
Bam - you're ready to go.


I built these skills as a way to fix common failure modes I see with Claude Code, Codex, and other coding agents.

**The Problem**. The most common failure mode in software development is misalignment. You think the dev knows what you want. Then you see what they've built - and you realize it didn't understand you at all.

This is just the same in the AI age. There is a communication gap between you and the agent. The fix for this is a **grilling session** - getting the agent to ask you detailed questions about what you're building.

**The Fix** is to use:

`/grill-me`

- for non-code uses`/grill-with-docs`

- same as`/grill-me`

, but adds more goodies (see below)

These are my most popular skills. They help you align with the agent before you get started, and think deeply about the change you're making. Use them *every* time you want to make a change.

**The Problem**: At the start of a project, devs and the people they're building the software for (the domain experts) are usually speaking different languages.

The domain experts are speaking their language, and the devs are trying to translate it into code. They're often talking past each other.

I felt exactly the same tension with my agents. Agents are usually dropped into a project and asked to figure out the jargon as they go. This leads to incredible verbosity. Agents use 20 words where 1 will do.

**The Fix** for this is a shared language. It's a document that helps agents decode the jargon used in the project.

## Example

Here's an example [ CONTEXT.md](https://github.com/mattpocock/course-video-manager/blob/076a5a7a182db0fe1e62971dd7a68bcadf010f1c/CONTEXT.md), from my

`course-video-manager`

repo. Which one is easier to read?**BEFORE**: "There's a problem when a lesson inside a section of a course is made 'real' (i.e. given a spot in the file system)"**AFTER**: "There's a problem with the materialization cascade"

This concision pays off session after session.

This is built into `/grill-with-docs`

. It's a grilling session, but with two extra abilities:

- It interrogates your shared language as you go, saving it in
`CONTEXT.md`

- It surfaces hard-to-explain decisions in ADR's (architectural decision records)

It's hard to explain how powerful this is.

Tip

A shared language has many other benefits than reducing verbosity:

**Variables, functions and files are named consistently**, using the shared language- As a result, the
**codebase is easier to navigate**for the agent - The agent also
**spends fewer tokens on thinking**, because it has access to a more concise language

Skills I use daily for code work.

— Disciplined diagnosis loop for hard bugs and performance regressions: reproduce → minimise → hypothesise → instrument → fix → regression-test.[diagnose](https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnose/SKILL.md)— Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates[grill-with-docs](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md)`CONTEXT.md`

and ADRs inline.— Triage GitHub issues through a label-based state machine.[github-triage](https://github.com/mattpocock/skills/blob/main/skills/engineering/github-triage/SKILL.md)— Find deepening opportunities in a codebase, informed by the domain language in[improve-codebase-architecture](https://github.com/mattpocock/skills/blob/main/skills/engineering/improve-codebase-architecture/SKILL.md)`CONTEXT.md`

and the decisions in`docs/adr/`

.— Test-driven development with a red-green-refactor loop. Builds features or fixes bugs one vertical slice at a time.[tdd](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md)— Break any plan, spec, or PRD into independently-grabbable GitHub issues using vertical slices.[to-issues](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-issues/SKILL.md)— Turn the current conversation context into a PRD and submit it as a GitHub issue. No interview — just synthesizes what you've already discussed.[to-prd](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-prd/SKILL.md)— Tell the agent to zoom out and give broader context or a higher-level perspective on an unfamiliar section of code.[zoom-out](https://github.com/mattpocock/skills/blob/main/skills/engineering/zoom-out/SKILL.md)

General workflow tools, not code-specific.

— Ultra-compressed communication mode. Cuts token usage ~75% by dropping filler while keeping full technical accuracy.[caveman](https://github.com/mattpocock/skills/blob/main/skills/productivity/caveman/SKILL.md)— Get relentlessly interviewed about a plan or design until every branch of the decision tree is resolved.[grill-me](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md)— Create new skills with proper structure, progressive disclosure, and bundled resources.[write-a-skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/write-a-skill/SKILL.md)

Tools I keep around but rarely use.

— Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, etc.) before they execute.[git-guardrails-claude-code](https://github.com/mattpocock/skills/blob/main/skills/misc/git-guardrails-claude-code/SKILL.md)— Migrate test files from[migrate-to-shoehorn](https://github.com/mattpocock/skills/blob/main/skills/misc/migrate-to-shoehorn/SKILL.md)`as`

type assertions to @total-typescript/shoehorn.— Create exercise directory structures with sections, problems, solutions, and explainers.[scaffold-exercises](https://github.com/mattpocock/skills/blob/main/skills/misc/scaffold-exercises/SKILL.md)— Set up Husky pre-commit hooks with lint-staged, Prettier, type checking, and tests.[setup-pre-commit](https://github.com/mattpocock/skills/blob/main/skills/misc/setup-pre-commit/SKILL.md)
