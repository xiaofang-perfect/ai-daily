---
title: "Google adds subagents to Gemini CLI to handle parallel coding tasks"
source: TLDR AI · 2026-04-21
url: https://tessl.io/blog/google-adds-subagents-to-gemini-cli-to-handle-parallel-coding-tasks/?utm_source=tldrai
date: 2026-04-21
published_at: 2026-04-21T12:00:00+00:00
tag: 产品发布
item_id: 22961137c519ae3b
---
[Back to articles](https://tessl.io/blog/)Google adds subagents to Gemini CLI to handle parallel coding tasks

20 Apr 20266 minute read

![](https://cdn.sanity.io/images/ojuglg5y/production/36fe1421691d23b40158a0bc9c78ca4c1932c6fb-1456x816.png?w=1456&auto=format)

[Back to articles](https://tessl.io/blog/)

# Google adds subagents to Gemini CLI to handle parallel coding tasks

20 Apr 20266 minute read

![](https://cdn.sanity.io/images/ojuglg5y/production/36fe1421691d23b40158a0bc9c78ca4c1932c6fb-1456x816.png?w=1456&auto=format)

AI coding agents might be able to take on more complex work, but they still tend to work through tasks one at a time. And that can become a huge bottleneck once tasks start to stack up.

Google is addressing that with a new “[subagents](https://geminicli.com/docs/core/subagents/)” feature in its [Gemini CLI](https://tessl.io/blog/gemini-cli/), introducing [a way to split work across multiple specialised agents](https://developers.googleblog.com/subagents-have-arrived-in-gemini-cli/) within the same environment.

Subagents are defined with their own instructions, tools, and context. The main agent can delegate parts of a task to them, allowing work to be broken down and handled in parallel. Rather than one agent working through everything step by step, tasks can be distributed and executed at the same time.

For example, a developer could tell Gemini CLI that the backend for an analytics API is done and ask it to update the frontend, tests, and documentation, with subagents then spun up for each part of the job — a frontend specialist, a unit test agent, and a docs writer.

## Delegating work inside the CLI

The setup is designed to handle tasks that would otherwise overload a single agent session. A developer can create subagents for specific roles — such as code review, testing, or documentation — and call on them when needed.

Each subagent runs with its own context, allowing the main agent to hand off work and receive results without carrying everything in a single thread. That keeps tasks more contained and avoids long chains of instructions building up in one session.

This approach has been present in other tools for some time. Claude Code, for example, has [supported subagents for a while](https://code.claude.com/docs/en/sub-agents), using a similar model of role-based delegation within a coding workflow.

## Parallel execution and context separation

A key part of the feature is that subagents can run at the same time, allowing different parts of a task to be processed in parallel.

Each subagent also operates in its own working space, so instructions and outputs remain separate. That reduces the risk of tasks interfering with one another, which can happen in longer, more complex sessions.

Together, this allows larger pieces of work to be broken down and handled without losing track of what each part is doing.

This also extends to running multiple instances of the same subagent at once. A developer can, for example, run a frontend-focused agent across several packages in parallel, with each instance analysing a different part of the codebase at the same time.

It’s worth noting that in Gemini CLI, this coordination happens within a single session, with subagents spun up to handle parts of a task before returning control to the main agent.

Other systems are exploring a more extensive setup. Claude Code, for example, offers “[agent teams](https://code.claude.com/docs/en/agent-teams)” that coordinate work across multiple sessions, rather than keeping everything tied to one session. That approach can support longer-running tasks, but adds more overhead in how those agents are defined and managed.

## How to use subagents in Gemini CLI

Gemini CLI comes with a set of built-in subagents that can be used straight away, each geared toward a specific type of task. These include a “generalist” agent that can handle a wide range of coding and command-line tasks, a CLI-focused agent that can answer questions about how the tool works, and a codebase-focused agent for exploring architecture, dependencies, and debugging issues.

Developers can also create their own subagents by defining them in a Markdown file with YAML frontmatter, followed by plain-text instructions describing the agent’s role and behaviour. These files can be stored locally or alongside a project to share across a team.

The system will automatically route tasks to these subagents when it decides one is a better fit. That means routine or well-defined work can be handled without needing to specify which agent should take it on.

Developers can also take direct control. By using the @ syntax followed by a subagent’s name, tasks can be explicitly assigned to a specific role — for example, asking a frontend-focused agent to review an interface, or a codebase-focused agent to map out part of a system. Each subagent then handles the task within its own context, separate from the main session.

To see which subagents are available at any point, the CLI provides a simple /agents command, which lists the current set of configured agents.

## Resources

## Related Articles

## More by Paul Sawers

![](https://cdn.sanity.io/images/ojuglg5y/production/a102da8f0a183ecc75fee2f06ef664cd64d6970b-1456x816.png?w=1456&auto=format)


![](https://cdn.sanity.io/images/ojuglg5y/production/a102da8f0a183ecc75fee2f06ef664cd64d6970b-1456x816.png?w=1456&auto=format)

### Anthropic postmortem shows how small changes compounded into Claude Code failure

28 Apr 2026

Paul Sawers

![](https://cdn.sanity.io/images/ojuglg5y/production/cb09e9f6c6f95a3fd5ba0272e92eabb3a6be15c6-1456x816.png?w=1456&auto=format)


![](https://cdn.sanity.io/images/ojuglg5y/production/cb09e9f6c6f95a3fd5ba0272e92eabb3a6be15c6-1456x816.png?w=1456&auto=format)

### As SpaceX deal looms, Cursor partners with Chainguard to secure open-source dependencies in AI-built code

27 Apr 2026

Paul Sawers

![](https://cdn.sanity.io/images/ojuglg5y/production/e7ebfde51f63c31708d8d07fa0b7e318674eca72-1456x816.png?w=1456&auto=format)


![](https://cdn.sanity.io/images/ojuglg5y/production/e7ebfde51f63c31708d8d07fa0b7e318674eca72-1456x816.png?w=1456&auto=format)

### Replit launches “Security Agent” to scan and fix vulnerabilities in AI-built apps

22 Apr 2026

Paul Sawers

![](https://cdn.sanity.io/images/ojuglg5y/production/14589dc0fbd99d11967d93e74c48886a88f86404-1456x816.png?w=1456&auto=format)


![](https://cdn.sanity.io/images/ojuglg5y/production/14589dc0fbd99d11967d93e74c48886a88f86404-1456x816.png?w=1456&auto=format)

### Cloudflare introduces “Agent Memory” to help AI agents remember across sessions

20 Apr 2026

Paul Sawers

![](https://cdn.sanity.io/images/ojuglg5y/production/54e62c0ec3a60fd2ddb693f1395faeb670fbc2b5-1456x816.png?w=1456&auto=format)


![](https://cdn.sanity.io/images/ojuglg5y/production/54e62c0ec3a60fd2ddb693f1395faeb670fbc2b5-1456x816.png?w=1456&auto=format)

### Anthropic adds 'routines' to Claude Code for scheduled agent tasks

16 Apr 2026

Paul Sawers
