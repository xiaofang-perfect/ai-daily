---
title: "mattpocock/skills"
source: GitHub Trending
url: https://github.com/mattpocock/skills
date: 2026-06-21
published_at: 2026-06-21T06:48:14.953967+00:00
tag: 工具开源
item_id: f8f314103a3f5b64
---
My agent skills that I use every day to do real engineering - not vibe coding.

Developing real applications is hard. Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control and make bugs in the process hard to resolve.

These skills are designed to be small, easy to adapt, and composable. They work with any model. They're based on decades of engineering experience. Hack around with them. Make them your own. Enjoy.

If you want to keep up with changes to these skills, and any new ones I create, you can join ~60,000 other devs on my newsletter:

- Run the skills.sh installer:

`npx skills@latest add mattpocock/skills`- 
Pick the skills you want, and which coding agents you want to install them on. **Make sure you select**.`/setup-matt-pocock-skills`
- 
Run `/setup-matt-pocock-skills`in your agent. It will:- Ask you which issue tracker you want to use (GitHub, Linear, or local files)
- Ask you what labels you apply to tickets when you triage them (`/triage`uses labels)
- Ask you where you want to save any docs we create
 
- 
Bam - you're ready to go. 

I built these skills as a way to fix common failure modes I see with Claude Code, Codex, and other coding agents.

"No-one knows exactly what they want"

David Thomas & Andrew Hunt,

[The Pragmatic Programmer](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

**The Problem**. The most common failure mode in software development is misalignment. You think the dev knows what you want. Then you see what they've built - and you realize it didn't understand you at all.

This is just the same in the AI age. There is a communication gap between you and the agent. The fix for this is a **grilling session** - getting the agent to ask you detailed questions about what you're building.

**The Fix** is to use:

- `/grill-me`
- `/grill-with-docs`- `/grill-me`

These are my most popular skills. They help you align with the agent before you get started, and think deeply about the change you're making. Use them *every* time you want to make a change.

With a ubiquitous language, conversations among developers and expressions of the code are all derived from the same domain model.

Eric Evans,

[Domain-Driven-Design](https://www.amazon.co.uk/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

**The Problem**: At the start of a project, devs and the people they're building the software for (the domain experts) are usually speaking different languages.

I felt the same tension with my agents. Agents are usually dropped into a project and asked to figure out the jargon as they go. So they use 20 words where 1 will do.

**The Fix** for this is a shared language. It's a document that helps agents decode the jargon used in the project.

## Example

Here's an example [ CONTEXT.md](https://github.com/mattpocock/course-video-manager/blob/076a5a7a182db0fe1e62971dd7a68bcadf010f1c/CONTEXT.md), from my 

`course-video-manager` repo. Which one is easier to read?- **BEFORE**: "There's a problem when a lesson inside a section of a course is made 'real' (i.e. given a spot in the file system)"
- **AFTER**: "There's a problem with the materialization cascade"

This concision pays off session after session.

This is built into [ /grill-with-docs](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md). It's a grilling session, but that helps you build a shared language with the AI, and document hard-to-explain decisions in ADR's.

It's hard to explain how powerful this is. It might be the single coolest technique in this repo. Try it, and see.

Tip

A shared language has many other benefits than reducing verbosity:

- **Variables, functions and files are named consistently**, using the shared language
- As a result, the **codebase is easier to navigate**for the agent
- The agent also **spends fewer tokens on thinking**, because it has access to a more concise language

"Always take small, deliberate steps. The rate of feedback is your speed limit. Never take on a task that’s too big."

David Thomas & Andrew Hunt,

[The Pragmatic Programmer](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

**The Problem**: Let's say that you and the agent are aligned on what to build. What happens when the agent *still* produces crap?

It's time to look at your feedback loops. Without feedback on how the code it produces actually runs, the agent will be flying blind.

**The Fix**: You need the usual tranche of feedback loops: static types, browser access, and automated tests.

For automated tests, a red-green-refactor loop is critical. This is where the agent writes a failing test first, then fixes the test. This helps give the agent a consistent level of feedback that results in far better code.

I've built a 

`/tdd` skillFor debugging, I've also built a 

`/diagnosing-bugs`"Invest in the design of the system

every day."Kent Beck,

[Extreme Programming Explained](https://www.amazon.co.uk/Extreme-Programming-Explained-Embrace-Change/dp/0321278658)

"The best modules are deep. They allow a lot of functionality to be accessed through a simple interface."

John Ousterhout,

[A Philosophy Of Software Design](https://www.amazon.co.uk/Philosophy-Software-Design-2nd/dp/173210221X)

**The Problem**: Most apps built with agents are complex and hard to change. Because agents can radically speed up coding, they also accelerate software entropy. Codebases get more complex at an unprecedented rate.

**The Fix** for this is a radical new approach to AI-powered development: caring about the design of the code.

This is built in to every layer of these skills:

- `/to-prd`

And crucially, [ /improve-codebase-architecture](https://github.com/mattpocock/skills/blob/main/skills/engineering/improve-codebase-architecture/SKILL.md) helps you rescue a codebase that has become a ball of mud. I recommend running it on your codebase once every few days.

Software engineering fundamentals matter more than ever. These skills are my best effort at condensing these fundamentals into repeatable practices, to help you ship the best apps of your career. Enjoy.

These split on one axis — who can invoke them. **User-invoked** skills are reachable only when you type them (e.g. `/grill-me`); their job is to orchestrate. **Model-invoked** skills can be invoked by you *or* reached for automatically by the agent when the task fits; they hold the reusable discipline. A user-invoked skill may invoke model-invoked skills, but never another user-invoked one.

Skills I use daily for code work.

**User-invoked**

- [ask-matt](https://github.com/mattpocock/skills/blob/main/skills/engineering/ask-matt/SKILL.md)
- [grill-with-docs](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md)- `CONTEXT.md`and ADRs inline.
- [triage](https://github.com/mattpocock/skills/blob/main/skills/engineering/triage/SKILL.md)
- [improve-codebase-architecture](https://github.com/mattpocock/skills/blob/main/skills/engineering/improve-codebase-architecture/SKILL.md)
- [setup-matt-pocock-skills](https://github.com/mattpocock/skills/blob/main/skills/engineering/setup-matt-pocock-skills/SKILL.md)
- [to-issues](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-issues/SKILL.md)
- [to-prd](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-prd/SKILL.md)
- [prototype](https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/SKILL.md)

**Model-invoked**

- [diagnosing-bugs](https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnosing-bugs/SKILL.md)
- [tdd](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md)
- [domain-modeling](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md)- `CONTEXT.md`and ADRs inline.
- [codebase-design](https://github.com/mattpocock/skills/blob/main/skills/engineering/codebase-design/SKILL.md)

General workflow tools, not code-specific.

**User-invoked**

- [grill-me](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md)
- [handoff](https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md)
- [teach](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/SKILL.md)
- [writing-great-skills](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md)

**Model-invoked**

- [grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md)- `grill-me`and- `grill-with-docs`.

Tools I keep around but rarely use.

- [git-guardrails-claude-code](https://github.com/mattpocock/skills/blob/main/skills/misc/git-guardrails-claude-code/SKILL.md)
- [migrate-to-shoehorn](https://github.com/mattpocock/skills/blob/main/skills/misc/migrate-to-shoehorn/SKILL.md)- `as`type assertions to @total-typescript/shoehorn.
- [scaffold-exercises](https://github.com/mattpocock/skills/blob/main/skills/misc/scaffold-exercises/SKILL.md)
- [setup-pre-commit](https://github.com/mattpocock/skills/blob/main/skills/misc/setup-pre-commit/SKILL.md)
