---
title: "Anthropic launches advisor tool for Claude Platform API users"
source: TLDR AI · 2026-04-10
url: https://www.testingcatalog.com/anthropic-launches-advisor-tool-for-claude-platform-api-users/?utm_source=tldrai
date: 2026-04-11
published_at: 2026-04-10T12:00:00+00:00
tag: 产品发布
item_id: 733954cf5d7bc20d
---
Anthropic has unveiled the advisor tool on the Claude Platform, providing developers with the ability to use Opus as an advisor alongside Sonnet or Haiku as executors. This strategy allows agents to access advanced reasoning capabilities while maintaining operational costs at the level of the more efficient executor models. The advisor tool is now available publicly through the Claude Platform API and can be activated with a simple configuration in the Messages API request. The primary audience includes developers and organizations building AI agents that require both cost management and high-level reasoning.

We're bringing the advisor strategy to the Claude Platform.

— Claude (@claudeai)

Pair Opus as an advisor with Sonnet or Haiku as an executor, and get near Opus-level intelligence in your agents at a fraction of the cost.[pic.twitter.com/fRkegyMs5t][April 9, 2026]

The advisor tool works by allowing Sonnet or Haiku to handle tasks independently. When these executors encounter complex decision points, they call upon Opus for guidance. Opus reviews the shared context and returns a plan or corrective feedback, after which the executor resumes its task. This approach contrasts with traditional systems where a large model orchestrates and delegates tasks to smaller agents. Instead, the advisor tool allows the executor to escalate only when necessary, keeping most operations at a lower cost. Technical evaluations show improvements in benchmarks such as SWE-bench Multilingual, BrowseComp, and Terminal-Bench 2.0. For example, Haiku with an Opus advisor more than doubled its standalone benchmark score while costing significantly less than running Sonnet alone.

![Claude](https://storage.ghost.io/c/2a/1b/2a1b1782-8506-4d7d-bf53-ad3fb52e2a0f/content/images/2026/04/69d7a8216b96ea826922fcfd_ca657f5f.png)

Anthropic, the company behind Claude, focuses on developing advanced AI systems that prioritize reliability and efficiency. This release underscores the company’s commitment to helping developers deploy intelligent agents at scale without incurring the high costs typically associated with frontier-level models.
