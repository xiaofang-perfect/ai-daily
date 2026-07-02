---
title: "Meituan launches LongCat-2.0 1.6T parameter model on APIs"
source: TLDR AI · 2026-07-01
url: https://www.testingcatalog.com/meituan-launches-longcat-2-0-1-6t-parameter-model-on-apis/?utm_source=tldrai
date: 2026-07-02
published_at: 2026-07-01T12:00:00+00:00
tag: 产品发布
item_id: ad3de32c9bed9475
---
![Google Preferred Source](https://www.testingcatalog.com/assets/images/google_preferred_source_badge_light_en.png?v=ee33689612) 

        Meituan has unveiled LongCat-2.0, marking a significant advancement in its LongCat model family following the earlier LongCat-2.0-Preview. This new model is designed as a 1.6 trillion-parameter Mixture-of-Experts system, with approximately 48 billion parameters active per token. It is aimed at agentic coding, tool use, long-context work, automated workflows, and the execution of complex instructions.

LongCat-2.0 features a 1 million-token context window and a maximum output length of 128K tokens via the LongCat API Platform. Developers can access it through OpenAI-compatible and Anthropic-compatible API formats, with support for Claude Code, OpenClaw, OpenCode, Kilo Code, and Codex-style workflows.

Introducing LongCat-2.0 🐱

— Meituan LongCat (@Meituan_LongCat)

1.6T parameters · MoE with ~48B active · 1M context

The full model behind Owl Alpha on[@OpenRouter](https://x.com/OpenRouter?ref_src=twsrc%5Etfw&ref=testingcatalog.com)— now available.

Built for agentic coding from the ground up:

◆ LongCat Sparse Attention (LSA) — scales efficiently for 1M-context tokens

◆…[pic.twitter.com/zum2SdZ0Z2](https://t.co/zum2SdZ0Z2?ref=testingcatalog.com)[June 30, 2026](https://x.com/Meituan_LongCat/status/2071783587205308721?ref_src=twsrc%5Etfw&ref=testingcatalog.com)

The company reports that the full training run and deployment were conducted on AI ASIC superpods, with pretraining across more than 35 trillion tokens. LongCat also introduced LongCat Sparse Attention for long-horizon tasks and trained the model on hundreds of billions of tokens of 1M-context data, positioning the system for large repositories, long documents, and multi-step agent tasks.

The release is publicly available via the API, and billing is now active. The pay-as-you-go pricing structure currently supports LongCat-2.0 at:

- $0.75 per 1M uncached input tokens
- $0.015 per 1M cached input tokens
- $2.95 per 1M output tokens

Lower limited-time prices are also listed by LongCat. Token packs are valid for 30 days, and cache hits do not count against token-pack usage.

This release is not yet a full weights drop. The GitHub repository is public under an MIT license, but both the repository and Hugging Face model card indicate that model weights are forthcoming. This makes the launch a hybrid release for now: usable through the API and documented in public repositories, while the downloadable model weights remain pending.

Some of you guessed right. 👀

— Meituan LongCat (@Meituan_LongCat)

Owl Alpha on[@OpenRouter](https://x.com/OpenRouter?ref_src=twsrc%5Etfw&ref=testingcatalog.com)— that's us.

Since going live, it has reached Top 3 globally by daily volume — and #1 on Hermes Agent, #2 on Claude Code, #3 on OpenClaw by monthly volume.

Thank you to everyone who tested and used Owl Alpha during stealth…[pic.twitter.com/e86L9x3hFI](https://t.co/e86L9x3hFI?ref=testingcatalog.com)[June 29, 2026](https://x.com/Meituan_LongCat/status/2071624742701080606?ref_src=twsrc%5Etfw&ref=testingcatalog.com)

LongCat-2.0 is also linked to Owl Alpha, the previously undisclosed model running on OpenRouter. LongCat’s official account describes LongCat-2.0 as the full model behind Owl Alpha, while OpenRouter lists Owl Alpha as a 1.05M-context agentic model with tool-use, code-generation, automated workflow, and complex instruction-following capabilities. OpenRouter’s free-models page lists Owl Alpha at 3.74T tokens, indicating the model had already seen significant developer usage before the reveal.

Meituan, the company behind LongCat, describes the project as a family of large language models designed to make AI useful in physical-world scenarios. The team has already released LongCat-Flash-Chat, LongCat-Video, LongCat-Image, LongCat-Next, and other AI projects, positioning LongCat-2.0 as the new flagship language model in a broader multimodal and agent-focused portfolio.
