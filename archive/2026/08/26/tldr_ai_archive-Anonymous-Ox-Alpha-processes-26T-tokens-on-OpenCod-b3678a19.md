---
title: "Anonymous Ox Alpha processes 26T tokens on OpenCode, breaks OpenRouter launch record"
source: TLDR AI · 2026-08-25
url: https://runtimewire.com/article/anonymous-ox-alpha-processes-26t-tokens-on-opencode-breaks-openrouter-launch-rec?utm_source=tldrai
date: 2026-08-26
published_at: 2026-08-25T12:00:00+00:00
tag: 行业动态
item_id: b3678a19a90889e9
---
# Anonymous Ox Alpha processes 26T tokens on OpenCode, breaks OpenRouter launch record

**Ox Alpha reached 327,000 users and 8.3 million sessions while its developer remained anonymous and OpenCode charged users nothing.**

        By [Ryan Merket](https://runtimewire.com/author/ryan-merket)
        · Published 
        
      

Primary source: [OpenCode on X](https://x.com/opencode/status/2091946582790766899)

## Why it matters

Ox Alpha reached OpenCode's No. 2 usage slot without a known developer or token price, showing how coding-agent distribution can manufacture model-scale demand almost overnight.

![A central, intricate paper-cut data hub representing OpenCode's Ox Alpha model processes information, surrounded by numerous small, interconnected user icons.](https://runtimewire.com/api/storage/uploads/hero-images/anonymous-ox-alpha-processes-26t-tokens-on-opencode-breaks-openrouter-launch-rec-b9b1de4a.png?w=1600&fmt=webp)

[Dax Raad (@thdxr)](https://x.com/thdxr)'s OpenCode said its users processed 26 trillion tokens through [Ox Alpha](https://runtimewire.com/models/stealth/ox-alpha) during the anonymous AI model's first four days, turning a free preview into one of the largest model trials on the coding agent.

The [August 24th disclosure](https://x.com/opencode/status/2091946582790766899) covered 327,000 unique users and 8,328,244 completed sessions, according to [OpenCode's usage dashboard](https://opencode.ai/data/unknown/ox-alpha). Ox Alpha ranked second among models tracked by OpenCode, behind [DeepSeek V4 Flash](https://runtimewire.com/models/azure/deepseek-v4-flash) at 33 trillion tokens and ahead of Xiaomi's [MiMo-V2.5](https://runtimewire.com/models/xiaomi/mimo-v2.5) at 12 trillion.

Raad created [OpenCode](https://github.com/anomalyco/opencode) as an open-source, terminal-based coding agent that could work across models rather than locking developers into one lab. He said in a [2025 interview with Baseten](https://www.baseten.co/blog/building-ai-agents-open-code-and-open-source-a-conversation-with-dax/) that maintaining compatibility across a constant stream of models was precisely where an open-source community could help. The OpenCode repository had passed 200,000 GitHub stars by August 24th.

### Free distribution did what free distribution does

OpenCode introduced Ox Alpha on August 20th as a stealth model with multimodal inputs, a one-million-token context window, near-unlimited usage and zero data retention through OpenCode's route. OpenCode also claimed it had secured capacity for as many as 100 trillion tokens per day.

Actual usage averaged about 6.5 trillion tokens per day over the first four days, or 6.5% of that advertised daily capacity. OpenCode recorded an average of 3.2 million tokens across each completed session and roughly 25 sessions for every unique user.

[OpenRouter separately reported](https://x.com/OpenRouter/status/2091912024922177562) that Ox Alpha generated 11.6 trillion tokens during its first three full days on that platform, making it the largest model launch in OpenRouter's history. The next-biggest launch generated 4.4 trillion tokens over the same opening period, and OpenRouter said Ox Alpha was on track to process nearly 6 trillion tokens that day.

Those figures describe aggregate session activity rather than prompt size. OpenCode's dashboard also says 93% of input tokens were served from cache, meaning the headline total combines fresh inputs with context reused during long coding sessions. The $0 spend shown on the dashboard reflects the price charged to users, rather than the underlying cost of supplying the inference.

The distribution strategy still worked. Ox Alpha captured 6.8% of observed OpenCode token volume within four days despite carrying no recognized lab name. Price, a large context window and placement inside a coding agent with an established developer base removed most of the friction that usually limits a model preview.

OpenCode's [Go documentation](https://dev.opencode.ai/docs/go/) lists Ox Alpha as free for a limited time, with no stated token prices or fixed usage allowance. The model is available through an [OpenAI-compatible endpoint](https://runtimewire.com/article/vlm-run-gateway-open-weight-ocr-models), making it possible for developers to substitute Ox Alpha into existing agent workflows with relatively little integration work.

### The anonymous provider is the catch

OpenCode's own model page identifies Ox Alpha's maker as "Unknown" and supplies no release, knowledge-cutoff or output-limit metadata. [OpenRouter's official listing](https://openrouter.ai/provider/stealth) says a third-party provider developed and operates Ox Alpha while remaining anonymous during the preview. OpenRouter lists a 1,048,576-token context window and charges $0 for input and output tokens.

The two distribution routes carry different data terms. OpenCode says prompts sent through its Go service have zero-day retention and are not used for model training. OpenRouter says the anonymous provider retains prompts and completions, although it does not use them for training. Developers handling proprietary repositories therefore need to check which endpoint is receiving their code rather than treating every free Ox Alpha route as interchangeable.

The early load also exposed integration problems. A [GitHub issue opened on August 23rd](https://github.com/anomalyco/opencode/issues/44300) reported that Ox Alpha requests containing tool definitions were failing through OpenCode's Zen and Go endpoints even while plain chat requests continued to work. Tool use is central to coding agents, which must read files, execute commands and edit repositories rather than simply generate text.

The preview fits the model-selection thesis behind OpenCode's Zen service. Raad has described Zen as a way to pool developer demand, test model deployments and negotiate inference rates using OpenCode's combined volume. Ox Alpha pushes that approach further: an unidentified lab gets millions of real coding sessions, while OpenCode gets a high-capacity model that can attract users without adding token charges during the preview.

The 26 trillion figure is a demand metric produced under zero-dollar pricing. Model quality remains a separate question, especially while Ox Alpha's developer, architecture and full evaluation record remain unidentified. The clearest result after four days is that OpenCode can direct enormous workloads toward a model when it controls both the coding interface and the price of access.
