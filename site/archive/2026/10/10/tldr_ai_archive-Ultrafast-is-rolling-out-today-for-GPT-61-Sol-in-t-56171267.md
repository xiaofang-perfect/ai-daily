---
title: "Ultrafast is rolling out today for GPT-6.1 Sol in the API, Codex, and ChatGPT Work"
source: TLDR AI · 2026-10-09
url: https://threadreaderapp.com/thread/2108262812489531498.html?utm_source=tldrai
date: 2026-10-10
published_at: 2026-10-09T12:00:00+00:00
tag: 产品发布
item_id: 561712671b69ef39
---
**This Thread may be Removed Anytime!**

Twitter may remove this content at anytime! Save it as PDF for later use!

1. Follow [@ThreadReaderApp](https://twitter.com/threadreaderapp) to mention us!
2. From a Twitter thread mention us with a keyword "unroll"

`@threadreaderapp unroll`
          [Practice here](https://twitter.com/threadreaderapp/status/1054877865362112513) first or read more on our [help page](https://threadreaderapp.com/help)!

GPT-Live-1 is now available in the API.


Bring ChatGPT’s natural back-and-forth to your app, with voice agents that listen while they speak and work with the models and harness you choose.

GPT-Live-1 finally makes conversations fluid.


It distinguishes speech from background noise, so café chatter doesn’t have to stop the conversation ☕


You can even add a detail you just thought of or change direction mid-conversation without waiting for the model to finish its speaking turn.

GPT-Live-1 handles listening and speaking in one model, cutting out extra handoffs so the conversation moves fasterrrrrrr 🏎️


And you can keep talking while your backend model handles reasoning and tool calls.

We’re having way too much fun working through your feedback.


(Please, keep it coming.)


Keyboard shortcuts are now customizable.


Set Codex up around how you actually work, then tweak shortcuts from settings instead of adapting to our defaults.

Git actions are easier to reach.


We moved key git controls back into the review flow, so common actions like commit, push, branch, PR creation, and PR status are closer to where you’re already working.

Improved thread panel.


Related context and controls now load and behave more cleanly from the thread header: summaries, local state, Git context, sources, and more.

Today we’re announcing Open Responses: an open-source spec for building multi-provider, interoperable LLM interfaces built on top of the original OpenAI Responses API.


✅ Multi-provider by default

✅ Useful for real-world workflows

✅ Extensible without fragmentation


Build agentic systems without rewriting your stack for every model: [openresponses.org](http://openresponses.org)

Builders are already using Open Responses 👀


GPT-5.2-Codex is now available in the Responses API—the same model available in Codex.


It’s strong at complex long-running tasks like building new features, refactoring code, and finding bugs.


Plus, it’s the most cyber-capable model yet, helping to find and understand codebase vulnerabilities.


[platform.openai.com/docs/models/gp…](https://platform.openai.com/docs/models/gpt-5.2-codex)

Check out our prompting guide to get the most out of Codex models: [cookbook.openai.com/examples/gpt-5…](https://cookbook.openai.com/examples/gpt-5/codex_prompting_guide)

Here’s what our customers are saying about GPT-5.2-Codex in the API 👇



🆕 Codex now officially supports skills


Skills are reusable bundles of instructions, scripts, and resources that help Codex complete specific tasks.


You can call a skill directly with $.skill-name, or let Codex choose the right one based on your prompt.

Following the [agentskills.io](http://agentskills.io) standard, a skill is just a folder: [SKILL.md](http://SKILL.md) for instructions + metadata, with optional scripts, references, and assets.


We’re looking forward to collaborating on the standard so it’s easy to share and use skill across different tools.
![Screenshot of a folder tree layout for a skill](/images/1px.png)


You can install scripts for just yourself in (\~/.codex/skills), or for everyone working on a project in (repo\_path/.codex/skills).


We’ve also bundled a few handy system skills with Codex, such as plan, skill-creator, and skill-installer.


[developers.openai.com/codex/skills](https://developers.openai.com/codex/skills)
![Screenshot of the Codex CLI with the skill selector open](/images/1px.png)


You can now get more Codex usage from your plan and credits with three updates today:


1️⃣ GPT-5-Codex-Mini — a more compact and cost-efficient version of GPT-5-Codex

2️⃣ 50% higher rate limits for ChatGPT Plus, Business, and Edu

3️⃣ Priority processing for ChatGPT Pro and Enterprise

GPT-5-Codex-Mini allows roughly 4x more usage than GPT-5-Codex, at a slight capability tradeoff due to the more compact model.


Available in the CLI and IDE extension when you sign in with ChatGPT, with API support coming soon. ![Image](/images/1px.png)


Select GPT-5-Codex-Mini for easier tasks or to extend usage when you’re close to hitting rate limits.


Codex will also suggest switching to it when you reach 90% of your limits, so you can work longer without interruptions. ![Image](/images/1px.png)
