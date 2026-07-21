---
title: "Alibaba open-sources its AI chip software stack at WAIC, targeting Nvidia's CUDA lock-in"
source: TLDR AI · 2026-07-20
url: https://thenextweb.com/news/alibaba-t-head-sail-open-source-nvidia-cuda-alternative?utm_source=tldrai
date: 2026-07-21
published_at: 2026-07-20T12:00:00+00:00
tag: 工具开源
item_id: 4d0c9d26adc09d3a
---
#### TL;DR

*Alibaba’s T-Head open-sourced SAIL, the software stack for its Zhenwu AI chips, at WAIC in Shanghai. It aims to lower the barrier to migrating off Nvidia’s CUDA.*

T-Head says developers can adapt SAIL to mainstream AI frameworks in under seven days. Huawei and Moore Threads have made similar moves. CUDA still dominates.

*Alibaba’s T-Head open-sourced SAIL, the software stack for its Zhenwu AI chips, at WAIC in Shanghai. It aims to lower the barrier to migrating off Nvidia’s CUDA.*

Alibaba’s chip design unit T-Head [announced at the World AI Conference in Shanghai on Saturday](https://www.scmp.com/tech/tech-war/article/3361048/alibaba-targets-nvidias-dominant-software-ecosystem-open-source-ai-stack?module=perpetual_scroll_0&pgtype=article) that it is open-sourcing SAIL, the full software stack for its Zhenwu series of AI chips. The move is designed to lower migration barriers for developers currently locked into Nvidia’s CUDA ecosystem. T-Head said programmers can adapt SAIL to mainstream AI frameworks in under seven days.

The vast majority of AI developers globally write software using CUDA, Nvidia’s proprietary toolkit for programming GPUs. That dependency effectively locks them into buying Nvidia hardware, a dynamic that has helped the company reach a $3.4 trillion market cap. [Xi Jinping used the same conference on Friday to argue that no single country should monopolise AI](https://thenextweb.com/news/xi-jinping-waic-2026-shanghai-ai-speech), and T-Head’s open-sourcing of SAIL is the infrastructure-level expression of the same argument: if China wants AI independence, it needs to break the CUDA lock-in at the software layer, not just build alternative chips.

T-Head is not alone. Huawei open-sourced CANN, the software platform for its Ascend AI processors, in 2025. Moore Threads has pursued a similar strategy with its own GPU stack. All three are competing for the same developer migration: getting AI engineers to write code that runs on Chinese hardware without losing access to frameworks like PyTorch. The challenge is less technical than habitual. CUDA has a 17-year head start and the largest library ecosystem in the industry.

For Alibaba, the timing is loaded. [Anthropic accused Alibaba’s Qwen lab of running the largest AI distillation campaign ever against a US company](https://thenextweb.com/news/anthropic-accuses-alibaba-distillation-claude-qwen) last month, and the Pentagon added Alibaba to its Chinese military companies blacklist in June. Open-sourcing SAIL positions the company as a contributor to open AI infrastructure while it fights those designations in court. The 560,000 Zhenwu chips Alibaba has already shipped to over 400 customers now have a publicly available software layer, which makes the ecosystem stickier and harder for any single government to shut down.

Get the most important tech news in your inbox each week.
