---
title: "MiniMax promises M3 weights after 1M-context model launch"
source: TLDR AI · 2026-06-03
url: https://www.implicator.ai/minimax-promises-m3-weights-after-1m-context-model-launch/?utm_source=tldrai
date: 2026-06-04
published_at: 2026-06-03T12:00:00+00:00
tag: 工具开源
item_id: 995aac411be80ded
---
MiniMax [released M3](https://www.minimax.io/blog/minimax-m3?ref=implicator.ai) on Monday and said model weights and a technical report will follow within 10 days, leaving developers with API access before local inspection. The Shanghai company is offering M3 through MiniMax Code, token plans and an API, while its [M3 model page](https://www.minimax.io/models/text/m3?ref=implicator.ai) lists a 1M-token context window and a guaranteed 512,000-token minimum for API use. In MiniMax's description, MiniMax Sparse Attention, or MSA, uses a pre-filtering step to pick relevant key-value blocks before the full attention calculation.

Key Takeaways

- MiniMax released M3 with a 1M-token context window and native multimodal input.
- The company reports 59.0% on SWE-Bench Pro and 74.2% on MCP Atlas.
- Standard API pricing lists $0.60 per million input and $2.40 per million output.
- MarketWatch reported a 16% Hong Kong share drop after the STAR Market disclosure.

AI-generated summary, reviewed by an editor. [More on our AI guidelines](https://www.implicator.ai/about/).

## The release is API-first

MiniMax's final section says the report and weights will be released over the next 10 days on Hugging Face and GitHub.

MiniMax calls M3 the first open-weight model to combine frontier coding, native multimodality and a 1M-token context window. By Monday afternoon, the public material consisted of the launch post, model page and API documentation, not a downloadable M3 checkpoint. The methodology notes also cite internal infrastructure, Mini-SWE-Agent, Claude Code scaffolding and MiniMax scoring choices for different tests.

## Benchmark claims start with coding

MiniMax listed 59.0% on SWE-Bench Pro, 66.0% on Terminal-Bench 2.1 and 74.2% on MCP Atlas in its launch material. In a company-run Hopper test, M3 worked on FP8 matrix multiplication for about 24 hours, made 147 benchmark submissions and 1,959 tool calls, then raised hardware use from 7.6% to 71.3%.

## MSA handles long context

According to the launch post, MSA partitions cached keys and values into blocks and reads each selected block once through a "KV outer gather Q" operator design. MiniMax says that design cuts per-token compute at a 1-million-token context length to one-twentieth of its previous-generation model.

The API page lists Anthropic-compatible and OpenAI-compatible endpoints. It also lists image and video inputs with text output, which puts M3 in the same product lane as coding agents that need repository text, screenshots, diagrams and long tool histories in one session.

Track the AI model race daily

Strategic AI news from San Francisco. No hype, no "AI will change everything" throat clearing. Just what moved, who won, and why it matters. Daily at 6am PST.

No spam. Unsubscribe anytime.

## Pricing meets STAR filing

MiniMax lists standard API pricing up to 512,000 input tokens at $0.60 per million input and $2.40 per million output. [VentureBeat cited](https://venturebeat.com/technology/minimax-m3-debuts-eclipsing-gpt-5-5-and-gemini-3-1-pro-on-key-benchmark-performance-for-just-5-10-of-the-cost?ref=implicator.ai) lower first-week rates from MiniMax and platform partners, while MiniMax's own subscription plans start at $20 a month for about 1.7 billion M3 tokens.

Know someone who'd find this useful? [✉️ Email it to a friend in one click](mailto:?subject=A%20newsletter%20I%20think%20you%27d%20like&body=Hey%2C%20this%20is%20one%20of%20the%20newsletters%20I%27m%20currently%20reading.%20It%27s%20free%20and%20I%20can%20recommend%20it.%20(And%20yes%2C%20this%20email%20was%20created%20automatically%2C%20but%20honestly%2C%20implicator.ai%20is%20good....)%0A%0ASubscribe%20free%3A%20https%3A%2F%2Fwww.implicator.ai%2Fsubscribe%2F%3Futm_source%3Dnewsletter%26utm_medium%3Dforward%26utm_campaign%3Demail_forward), or they can [subscribe free here](https://www.implicator.ai/subscribe/?utm_source=newsletter&utm_medium=forward&utm_campaign=forward_to_colleague).

[MarketWatch wrote](https://www.marketwatch.com/story/minimax-plans-shanghai-listing-releases-new-ai-model-2nd-update-2f96666f?ref=implicator.ai) Monday that MiniMax shares fell 16% in Hong Kong after the company released M3 and disclosed plans for a Shanghai STAR Market listing. The report cited a listing-guidance agreement with Citic Securities and a filing with the Shanghai bureau of the China Securities Regulatory Commission.

## Weights remain pending

[South China Morning Post wrote](https://www.scmp.com/tech/tech-trends/article/3355529/minimax-debuts-ai-model-built-long-and-complex-coding-tasks?ref=implicator.ai) that MiniMax did not disclose M3's model size or the compute infrastructure used for training. The missing figures limit comparison with models whose parameter counts, chip clusters and training budgets are public.

Developers can test M3 now through MiniMax Code, subscription plans and API access. The next dated check is the 10-day release window MiniMax set for the technical report and weights, which points to roughly June 11.

Frequently Asked Questions

## What is MiniMax M3?

MiniMax M3 is the Shanghai company's new model for coding agents, long-context work and multimodal inputs. MiniMax says it supports a 1M-token context window and image and video input with text output.

## Is MiniMax M3 open-weight now?

MiniMax markets M3 as open-weight, but the draft treats that as a pledge. The company says it will publish model weights and a technical report within 10 days of launch.

## What is MiniMax Sparse Attention?

MiniMax Sparse Attention is the architecture MiniMax says lets M3 handle long context efficiently. It filters relevant key-value blocks and avoids full attention across every context token.

## How much does MiniMax M3 cost?

MiniMax lists standard pricing up to 512,000 input tokens at $0.60 per million input and $2.40 per million output. Subscription plans start at $20 a month.

## Why did MiniMax shares fall?

MarketWatch reported that MiniMax shares fell 16% in Hong Kong after the M3 release and disclosure of plans for a Shanghai STAR Market listing.

AI-generated summary, reviewed by an editor. [More on our AI guidelines](https://www.implicator.ai/about/).

[Alibaba Ships Qwen3.6-27B, an Open-Weight Coding Model That Beats Its 397B MoEAlibaba on Wednesday released Qwen3.6-27B, a dense 27-billion-parameter open-weight model under Apache 2.0 that tops its own 397B-parameter predecessor on every major agentic coding benchmark. The mod](https://www.implicator.ai/alibaba-ships-qwen3-6-27b-an-open-weight-coding-model-that-beats-its-397b-moe/)![](https://www.implicator.ai/content/images/2026/04/2026-04-22-17.37.35-qwen-27b-dense@2x.webp)


![](https://www.implicator.ai/content/images/2026/04/2026-04-22-17.37.35-qwen-27b-dense@2x.webp)

[Kimi K2.6 did not release a coding model. It opened the control room.On Monday, Moonshot AI put a familiar label on a less familiar move. Kimi K2.6 arrived as an open-source coding model, with a benchmark table, a Hugging Face page, a coding CLI, and the usual claims a](https://www.implicator.ai/kimi-k2-6-did-not-release-a-coding-model-it-opened-the-control-room/)![](https://www.implicator.ai/content/images/2026/04/2026-04-20-10.01.59-kimi_k2_6@2x.webp)


![](https://www.implicator.ai/content/images/2026/04/2026-04-20-10.01.59-kimi_k2_6@2x.webp)

[Cursor Acknowledges Kimi K2.5 as Composer 2 Base After Developer Spots Model IDCursor, the AI coding platform valued at $29.3 billion, publicly acknowledged on March 20 that its new Composer 2 model started from Moonshot AI's open-weight Kimi K2.5. The acknowledgment came less t](https://www.implicator.ai/cursor-acknowledges-kimi-k2-5-as-composer-2-base-after-developer-spots-model-id/)![](https://www.implicator.ai/content/images/2026/03/2026-03-21-14.32.20-peeled_label@2x.webp)


![](https://www.implicator.ai/content/images/2026/03/2026-03-21-14.32.20-peeled_label@2x.webp)
