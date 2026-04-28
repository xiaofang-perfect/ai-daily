---
title: "[AINews] The Claude Code Source Leak"
source: TLDR AI · 2026-04-02
url: https://www.latent.space/p/ainews-the-claude-code-source-leak?utm_source=tldrai
date: 2026-04-03
published_at: 2026-04-02T12:00:00+00:00
tag: 行业动态
item_id: a29d585bc973bf37
---
# [AINews] The Claude Code Source Leak

### The accidental "open sourcing" of Claude Code brings a ton of insights.

OpenAI’s [Largest Fundraise in Human History](https://www.latent.space/p/ainews-openai-closes-110b-raise-from) closed today, [growing by a few billion](https://openai.com/index/accelerating-the-next-phase-ai/), but disclosing some cool numbers like $24B ARR (growing 4x faster than Google/Meta in their heyday), and also had a “soft IPO” with $3B of investment from rich people and inclusion in [ETFs from ARK Invest](https://www.bloomberg.com/news/articles/2026-03-31/ark-etfs-to-add-openai-stake-as-retail-investors-chase-tech-boom), although ChatGPT WAU growth seem to has stalled out - they STILL have not crossed the 1B WAU mark targeted for end 2025. Codex also worryingly has [not announced a new milestone for March](https://x.com/swyx/status/2027613757787279730?s=20).

By far the biggest news of the day is [the Claude Code source leak](https://news.ycombinator.com/item?id=47584540), in itself not particularly damaging for Anthropic, but surely embarrassing and also somewhat educational - Christmas come early for Coding Agent nerds. You can read the many many tweets and posts covering the 500k LOC codebase, and you can [browse multiple hosted forks of the source](https://deepwiki.com/Sachin1801/claude-code).

There are fun curiosities, such as the [full verb list](https://x.com/wesbos/status/2038958747200962952?s=20), or [Capybara/Mythos v8](https://x.com/scaling01/status/2038948989257630166?s=20), or [the /buddy April Fools feature](https://x.com/trq212/status/2039201498996035924?s=46), or Boris’ [confirmed WTF counter](https://x.com/Rahatcodes/status/2038995503141065145?s=20), or creating the cursed “[Claude Codex](https://x.com/LexnLin/status/2038991257582604618?s=20)”, or the [dozen other unreleased features](https://x.com/amaan8429/status/2038924254570545298?s=20), but most serious players are commenting on a few things. Sebastian Raschka probably has [a good list of the top 6](https://x.com/rasbt/status/2038980345316413862?s=20):

Putting Repo state in Context (eg recent commits, git branch info)

Aggressive cache reuse

Custom Grep/Glob/LSP (standard in industry)

Claude code has

[less than 20 tools](https://x.com/jpschroeder/status/2038960058499768427)default on (up to[60+ total](https://x.com/mal_shaik/status/2038918662489510273)): AgentTool, BashTool, FileReadTool, FileEditTool, FileWriteTool, NotebookEditTool, WebFetchTool, WebSearchTool, TodoWriteTool, TaskStopTool, TaskOutputTool, AskUserQuestionTool, SkillTool, EnterPlanModeTool, ExitPlanModeV2Tool, SendMessageTool, BriefTool, ListMcpResourcesTool, and ReadMcpResourceTool.

File read deduplication/tool result sampling

Structured Session Memory (more on this)

Subagents


## Memory

Claude Code’s Memory has a [3 layer design](https://x.com/himanshustwts/status/2038924027411222533?s=20) with 1) a MEMORY.md that is just an index to other knowledge, 2) topic files loaded on demand, and 3) full session transcripts that can be searched. There’s also an “autoDream” mode for “sleep” - merging memories, deduping, pruning, removing contradictions.

A [deeper analysis from mem0](https://x.com/ellen_in_sf/status/2039098050837463504) finds 8 phases:

And there are 5 kinds of Compaction:

## Subagents use Prompt Caching

A key feature [of CC](https://x.com/_rajanagarwal/status/2039009685085303225?s=20): they use the KV cache to create a fork-join model for their subagents, meaning they contain the full context and don’t have to repeat work. In other words: [Parallelism is basically free](https://x.com/mal_shaik/status/2038918662489510273).

## The 5 level Permission System

## The 2 Types of Plan mode

[here](https://x.com/DharmiKumbhani/status/2038917827462308308?s=20):

## Resilience/Retry

## Other Unreleased/Internal Features

Including [an employee-only gate](https://x.com/iamfakeguru/status/2038965567269249484?s=20) and an [employee TUI](https://x.com/cheatyyyy/status/2038987747944546781), but also a bunch of [other stuff in development](https://x.com/RoundtableSpace/status/2038960753458438156?s=20) including ULTRAPLAN and [KAIROS](https://x.com/itsolelehmann/status/2039018963611627545?s=20):

![](https://substackcdn.com/image/fetch/$s_!cG_C!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3642b10-1f7e-49a0-af0d-986b24180a1c_1600x1084.png)


![](https://substackcdn.com/image/fetch/$s_!cG_C!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3642b10-1f7e-49a0-af0d-986b24180a1c_1600x1084.png)

[were recently shipped](https://x.com/himanshustwts/status/2038941583148810701?s=20)

And internal [MAGIC DOCS](https://x.com/mattyp/status/2038988217102266669):

AI News for 3/23/2026-3/24/2026. We checked 12 subreddits,

[544 Twitters]and no further Discords.[AINews’ website]lets you search all past issues. As a reminder,[AINews is now a section of Latent Space]. You can[opt in/out]of email frequencies!

**AI Twitter Recap**

**Top Story: Claude Code source leak — architecture discoveries, Anthropic’s response, and competitor reactions**

**What happened**

Claude Code had substantial source artifacts exposed via shipped source maps / package contents, which triggered rapid public reverse-engineering, mirroring, and derivative ports. The discussion quickly shifted from “embarrassing leak” to “what does this reveal about state-of-the-art agent harness design?” Multiple observers highlighted that the leak exposed orchestration logic rather than model weights, including autonomous modes, memory systems, planning/review flows, and model-specific control logic. Public forks proliferated; one post claimed **32.6k stars and 44.3k forks** on a fork before legal fear led to a Python conversion effort using Codex ([Yuchenj_UW](https://x.com/Yuchenj_UW/status/2038996920845430815)). Later commentary put the exposed code volume at **500k+ lines** ([Yuchenj_UW](https://x.com/Yuchenj_UW/status/2039029676040220682)). Anthropic then moved to contain redistribution via **DMCA takedowns** according to several posters ([dbreunig](https://x.com/dbreunig/status/2039007097376108979), [BlancheMinerva](https://x.com/BlancheMinerva/status/2039114452088295821)). Separately, a Claude Code team member announced a product feature during the fallout — easier local/web GitHub credential setup via `/web-setup`

([catwu](https://x.com/_catwu/status/2039027712288075812)) — implying normal product operations continued. The leak also created a live security hazard: attackers quickly registered suspicious npm packages such as `color-diff-napi`

and `modifiers-napi`

to target people trying to compile the leaked code ([Butanium_](https://x.com/Butanium_/status/2039079715823128964)).

**Facts vs. opinions**

**What is reasonably factual from the tweets:**

## Keep reading with a 7-day free trial

Subscribe to Latent.Space to keep reading this post and get 7 days of free access to the full post archives.
