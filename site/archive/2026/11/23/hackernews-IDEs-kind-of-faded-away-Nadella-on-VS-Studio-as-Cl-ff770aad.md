---
title: "'IDEs kind of faded away' – Nadella on VS Studio, as Claude Code takes the lead"
source: Hacker News
url: https://www.windowslatest.com/2026/11/23/the-thing-that-hit-us-satya-nadella-admits-vs-code-faded-in-six-months-after-a-decade-on-top-because-of-claude-code-and-some-developers-say-theyve-stopped-opening-it/
date: 2026-11-23
published_at: 2026-11-22T23:13:10+00:00
tag: 行业动态
item_id: ff770aadfc4d1db8
---
![Satya Nadella explains why IDEs like VS Code faded in six months Satya Nadella explains why IDEs like VS Code faded in six months](https://www.windowslatest.com/wp-content/uploads/2026/11/Satya-Nadella-explains-why-IDEs-like-VS-Code-faded-in-six-months-696x392.jpg)

These past few days, I’ve been seeing a lot of people brag that they haven’t opened VS Code in months, including (or rather, especially) developers. Now, Microsoft’s CEO said that he is completely aware of it. **Satya Nadella** told **Gergely Orosz** of The Pragmatic Engineer that after Anthropic launched Claude Code, IDEs *“kind of faded away”* in about six months, which is a major pivot that Microsoft had no immediate answer to.

It’s no secret that Microsoft plays the long game, and they did spend over a decade to make VS Code the default home for developers. Nadella still sees a future for the IDE, and the latest VS Code updates show Redmond turning its editor into a place to manage AI agents.

## Satya Nadella says Claude Code changed coding faster than Microsoft expected

If you have never typed a single line of code and want to know what all of this is about: Visual Studio Code (VS Code) is Microsoft’s free code editor for Windows, macOS and Linux, used to write, debug and manage code, with extensions for almost any programming language. Visual Studio is a different product and is Microsoft’s full-blown IDE.

![A custom layout in VS Code](https://www.windowslatest.com/wp-content/uploads/2026/11/A-custom-layout-in-VS-Code.png)


### How VS Code became the developer’s default

- **April 2015**, Microsoft previewed VS Code at Build as a free, cross-platform editor.
- **November 2015**, it open-sourced VS Code and added extensions.
- **April 2016**, [VS Code 1.0](https://code.visualstudio.com/blogs/2016/04/14/vscode-1.0) launched with 2 million installs and over 500,000 monthly active developers.
- **June 2021**, GitHub Copilot brought AI code completions into VS Code.
- **2023**, Cursor, an AI-first fork of VS Code, started competing with Copilot.
- **February 2025**, Anthropic launched [Claude Code](https://www.anthropic.com/news/claude-3-7-sonnet), a terminal tool that edits files, runs tests and commits code.

Nadella said VS Code’s success was intentional, crediting the team for *“building in the open,”* where product managers read community feedback every day.

Then came AI. Nadella called Copilot’s early completions *“magical,”* and when Cursor forked the IDE and built a strong agent mode, *“we then caught up on the agent mode.”* One look at Claude Code and you know it’s a breakthrough product.

![Agents in VS Code](https://www.windowslatest.com/wp-content/uploads/2026/11/Agents-in-VS-Code.jpg)


*“The thing that hit us was obviously a great work that Anthropic did with their model, which then truly made the CLI as a form factor,”* Nadella said in the [Pragmatic Engineer interview](https://newsletter.pragmaticengineer.com/p/software-engineering-after-code-becomes). *“Code went from input to output… In six months or so… IDEs kind of faded away.”*

His million-dollar lesson is*: “Don’t be in love with what you built,”* which is the exact opposite of what we were taught from childhood.

Coming from the company that owns VS Code, GitHub and Copilot, that’s quite the admission, though Microsoft Distinguished Engineer **David Fowler** already said in September that [typing code is “absolutely over.”](https://www.windowslatest.com/2026/09/05/microsoft-distinguished-engineer-says-typing-code-is-absolutely-over-and-windows-11-is-already-being-built-that-way/)

## Developers say they don’t open VS Code anymore, but not everyone agrees

Orosz compared Microsoft’s playbook to *“Embrace, extend, extinguish,”* where the company made VS Code really good, open-sourced it, and made it easy to build your editor but too hard to build one as good as Microsoft’s. *“Claude Code destroyed this bulletproof strategy meant to work for decades… in less than 6 months,”* [he wrote on X](https://x.com/GergelyOrosz/status/2122493193677627453).

![Claude Code](https://www.windowslatest.com/wp-content/uploads/2026/11/Claude-Code.jpg)


He says it’s anecdotal, but the more I think about it, and the more I ask my developer friends, they agree that they don’t feel the need to open VS Code as they used to. Some deliberately keep it open with all the code visible just to get the *developer feel*. Orosz says that, when compared to a year ago, the 10 developers he knows at startups, himself included, don’t use an IDE to code anymore. To him, VS Code was a funnel for Azure and GitHub Copilot, which is *“where it made lots of money!”*

I saw a brutal reply by someone that said: *“10 years building the perfect moat and someone just walked around it in a terminal,”*

Of course, not everyone is convinced by AI, and they shouldn’t, yet. One developer still uses VS Code to fix generated code, clean up *“the slop”* and review changes, calling GitHub’s code review *“very crappy”* in comparison. Another one says he now opens it only for diffs, Markdown files and search.

In Stack Overflow’s 2026 Developer Survey, [70.9% of 13,193 respondents](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/) used VS Code, down from 75.9% in 2025, which is a massive drop. To no one’s surprise, Claude Code topped the coding agents category at 65.5%. So, VS Code still has the users, but it’s losing the time developers spend typing in it.

## Microsoft is turning VS Code into a control room for AI agents

*“I don’t say it’s a permanent shift,”* Nadella said, clarifying that with the company’s new decision engine models, *“there could be a rebirth even of an IDE.”* In his words, the new IDE is *“more about how do I really input the specs and the markdowns.”*

Microsoft seems to be on the right track. VS Code 1.146 added an agent inbox and model comparisons on November 11, and a week later, [VS Code 1.147](https://code.visualstudio.com/updates/v1_147) brought model routers that choose from your preferred models for each task, scheduled agent requests, and browser integration.

![Model Router in VS Code](https://www.windowslatest.com/wp-content/uploads/2026/11/Model-Router-in-VS-Code.jpg)


Considering our preferences with AI models, Microsoft’s router method is very interesting, to say the least. Nadella wants Copilot to *“have this router pick the models for the task.”* VS Code also lets you [choose between Copilot, Claude or Codex](https://code.visualstudio.com/docs/copilot/agents/overview) agents. **If you can’t beat Claude Code, you might as well host it.**

I’m not a developer, but Claude built me two native WinUI 3 apps this year; one was a media downloader and the other, a music player. Throughout the projects, I opened Visual Studio maybe just a few times to package the apps.

Someone still has to check the code, and one reply said: *“Money, auth, permissions, DB code? I read every line. That’s where my IDE still lives.”*

In a staggering admission, Nadella also told Orosz he [can’t promise things at Microsoft will stay unchanged](https://www.windowslatest.com/2026/11/19/asked-if-60000-exit-offers-mean-ai-layoffs-at-microsoft-satya-nadella-said-i-wish-i-could-just-sit-here-and-say-itll-all-be-the-same-i-cannot/) as AI rewires software engineering. Some developers will still keep opening VS Code, but going by the latest updates, even Microsoft doesn’t expect them to write much code in it.
