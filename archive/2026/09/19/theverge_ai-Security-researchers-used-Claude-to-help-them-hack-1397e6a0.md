---
title: "Security researchers used Claude to help them hack into OpenAI"
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/997444/openai-hack-claude-heif-heist
date: 2026-09-19
published_at: 2026-09-18T11:30:16-04:00
tag: 行业动态
item_id: 1397e6a00dca9fa6
---
A team of three independent security researchers at [Hacktron](https://www.hacktron.ai/blog/hacking-openai#versions-affected-and-patches) says it took [less than 72 hours](https://x.com/S1r1u5_/status/2100777801335095383?s=20) for them to hack into OpenAI employee accounts using Anthropic’s Claude Opus 4.8 and 5, [*The Wall Street Journal*](https://www.wsj.com/tech/ai/hackers-used-anthropics-claude-to-break-into-openai-b40ba883) reports. They were able to access OpenAI’s GitHub repository, called “Monorepo,” which reportedly contains “OpenAI’s algorithmic secrets,” according to *The Wall Street Journal*’s sources.

# Security researchers used Claude to help them hack into OpenAI

A three-person team of researchers used a corrupted image file and forum software to hack into OpenAI.

![STKS533_AI_AGENTS_HACKING_D](https://platform.theverge.com/wp-content/uploads/sites/2/2026/09/STKS533_AI_AGENTS_HACKING_D.png?quality=90&strip=all&crop=0.95588235294118%2C0%2C98.088235294118%2C100&w=2400)

![STKS533_AI_AGENTS_HACKING_D](https://platform.theverge.com/wp-content/uploads/sites/2/2026/09/STKS533_AI_AGENTS_HACKING_D.png?quality=90&strip=all&crop=0.95588235294118%2C0%2C98.088235294118%2C100&w=2400)

![Stevie Bonifield](https://platform.theverge.com/wp-content/uploads/sites/2/2025/10/STEVIE_BONIFIELD_BLURPLE.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=96)

They stopped short of accessing internal code in Monorepo themselves, but sent a pull request from an employee’s Codex account to prove they gained access. They were able to get in through Discourse, the third-party service that hosts OpenAI’s community forums, by exploiting an issue with the system it uses to process HEIF images. According to Hacktron, Claude Opus 5 launched in the evening on July 24th, and by 10AM the next day they had used it to achieve RCE on Discourse Cloud and accessed OpenAI’s instance.

Their HEIF Heist project took “only one or two days” to adapt to different companies, including OpenAI, Slack, Meta, GitHub Ent, Rails, Next.js, ImageMagick, [and others](https://x.com/rootxharsh/status/2100801820960620574), using less than $3,000 in tokens, and to their knowledge, was only detected by one target, Shopify. The vulnerabilities Hacktron reported to Discourse and OpenAI have since been fixed, and Hacktron says OpenAI paid it $6,500 for finding the bug, but as Hacktron CTO Mohan Pedhapati said to the *WSJ*, “I don’t think we are as strong as Chinese threat actors… We’re just three guys with Claude and Codex subscriptions.”

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.
