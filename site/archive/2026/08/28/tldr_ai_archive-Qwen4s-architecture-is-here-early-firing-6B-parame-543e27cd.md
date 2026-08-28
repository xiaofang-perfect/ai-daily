---
title: "Qwen4's architecture is here early, firing 6B parameters out of 125B"
source: TLDR AI · 2026-08-27
url: https://thenextweb.com/news/qwen38-flash-next-qwen4-architecture-open-licence-ai-act?utm_source=tldrai
date: 2026-08-28
published_at: 2026-08-27T12:00:00+00:00
tag: 论文研究
item_id: 543e27cd75d5b55f
---
![Alibaba logo Alibaba logo](https://media.thenextweb.com/2026/07/alibaba-qwen-apple-intelligence-china-approved.avif) 

*Credit: Mfn*

Alibaba’s Qwen team has released Qwen3.8-Flash-Next, an open-weight preview of the architecture it intends to use for Qwen4, carrying 125B parameters but activating only 6B for each token. Its licence may not qualify for the EU AI Act’s open-source exemption.

Alibaba’s Qwen team has published the [architecture it plans to build Qwen4](https://www.unite.ai/qwen3-8-flash-next-previews-qwen4-architecture-with-6b-active-parameters/) on. Qwen3.8-Flash-Next carries 125B parameters and fires only 6B of them for each token it produces.

The claim is about cost rather than capability. The team says its concern is what architectural choices do to inference bills as agentic jobs with very long contexts become the normal workload.

The comparison it draws is with its own last model. Qwen3.7-Plus holds 397B parameters and activates 17B, so this one runs on roughly a third of the active compute.

Three of the four changes are conventional enough. A new sparse attention scheme works on micro-blocks instead of picking individual tokens, a gated residual mechanism controls what passes between layers, and the training recipe drops batch-size warmup entirely.

The fourth is the odd one. Rather than adding experts, the model bolts on 51B parameters as a separate embedding indexed by two and three-character fragments, which the team says costs less computation and is easier to offload onto memory-constrained accelerators.

That last phrase is worth reading twice. Designing for accelerators short of memory is what you do when you cannot buy the best chips, which is the position export controls have put Chinese labs in.

The numbers attached to all this are Alibaba’s own. TNW noted this month that the company called Qwen3.8 the world’s second-best model and [showed no proof](https://thenextweb.com/news/alibaba-qwen38-second-only-fable5-open-weight), and these scores again come from the team’s own harnesses.

Some of the choices are unusually candid. The model card says its Humanity’s Last Exam score was graded by GPT-4o rather than the benchmark’s own grader, which is disclosure rather than neutrality.

The licence is where Europe has a question. The weights sit on Hugging Face under a qwen-community licence, and TNW reported on 7 August that Alibaba [wants to charge](https://thenextweb.com/news/alibaba-charge-big-users-open-source-qwen) its largest commercial users.

The AI Act treats that distinction as load-bearing. Article 53(2) lifts two documentation duties for models under a free and open-source licence, and Recital 103 says components provided against a price or otherwise monetised should not get the exemption.

European firms are not waiting for the answer. Thomson Reuters [built its model](https://thenextweb.com/news/thomson-reuters-thomson-model-qwen-claude-cocounsel) on Qwen, and anyone who does inherits whatever the licence eventually becomes.

## Get the TNW newsletter

Get the most important tech news in your inbox each week.
