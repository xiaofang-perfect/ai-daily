---
title: "Liquid AI reveals 8B-A1B MoE trained on 38T"
source: Hacker News
url: https://www.liquid.ai/blog/lfm2-5-8b-a1b
date: 2026-05-30
published_at: 2026-05-29T16:19:54+00:00
tag: 产品发布
item_id: ef396d435eff78d5
---
Today, we're releasing **LFM2.5-8B-A1B**, an edge model built for fast, reliable tool calling on consumer hardware.

It builds on our[ LFM2-8B-A1B](https://www.liquid.ai/blog/lfm2-8b-a1b-an-efficient-on-device-mixture-of-experts) release from October 2025, with an expanded 128K context window, scaled-up pretraining (from 12T to 38T tokens), and large-scale reinforcement learning. We also doubled its vocabulary to improve tokenization efficiency for non-Latin languages. The result is a model that chains tool calls, achieves tasks, and fits comfortably even on an entry-level laptop.

The base (LFM2.5-8B-A1B-Base) and post-trained (LFM2.5-8B-A1B) models are available today on [Hugging Face](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B) and our [Playground](https://playground.liquid.ai/chat?model=LFM2.5-8B-A1B). Check out our [docs](https://docs.liquid.ai) on how to run and fine-tune them locally.

![](https://cdn.prod.website-files.com/67cb8aa6e9184b6e44813189/6a17874a7db7a603d7eb3627_lfm2_5_8b_a1b_benchmarks.png)

**AA-Omniscience Index (higher is better) rewards correct answers and penalizes hallucinations. Scores range from -100 to 100. See more results on*


*Artificial Analysis**.*

## Highlights

**On-device personal assistant.**Designed to power real-life applications, chaining tool calls, and following complex instructions on all devices.**Compressed performance.**Competitive with much larger dense and MoE models on instruction following and agentic tasks.**Unmatched throughput.**Fastest in its size class on both CPU and GPU inference, with day-one support for llama.cpp, MLX, vLLM, and SGLang.

## What changed since LFM2-8B-A1B

Compared to LFM2-8B-A1B, this new version expands the **context window from 32,768 to 128,000 tokens**. This allows the model to process longer documents and reason for longer. Its vocabulary size was also scaled up from 65,536 to 128,000 to **tokenize non-Latin scripts more efficiently**. We see particularly strong compression gains in Hindi, Thai, Vietnamese, Indonesian, and Arabic. The rest of the architecture follows the same combination of MoE, GQA, and gated short convolution blocks as LFM2-8B-A1B, as shown in the following figure.

![](https://cdn.prod.website-files.com/67cb8aa6e9184b6e44813189/68e51171bca5238ee2deb74b_LFM2%20architecture%20chart%20(6).png)


Unlike its predecessor, LFM2.5-8B-A1B is a **reasoning-only model**, producing an explicit chain of thought before its final answer. We adopted this strategy because MoE models generally run in compute-bound settings, where a smaller number of active parameters makes each reasoning token cheap. This provides a significant quality boost without compromising speed.

Thanks to reasoning and scaled-up training, this new version performs significantly better:

## Training highlights

**Tokenizer expansion. **LFM2-8B-A1B was originally trained with a 65K BPE tokenizer optimized for our initial language coverage. To better support non-Latin scripts in LFM2.5, we doubled the vocabulary to 128K by extending the existing tokenizer in place rather than retraining the model from scratch.. We continued BPE merge training from the original merges on a multilingual corpus, which keeps most existing token IDs as identity mappings and makes every new token decompose deterministically into a sequence of original sub-tokens. We initialize the new embedding rows as the mean of their sub-token decompositions and copy the shared rows unchanged. We then recover quality through a brief two-stage adaptation: embedding-only training, followed by full-model continued pretraining.

The table below reports chars/token, roughly how much text each token carries: higher is better, and the new tokenizer is more efficient in all 16 languages

**Context extension.** We first extended the context window to 32K through a 2T token midtraining phase focused on reasoning, math, tool-use, and longer documents. We then extended the context to 128K by increasing the RoPE base θ and running an additional 400B token midtraining stage focused on long-document and long-trajectory data.

**Doom loops.** We added a targeted preference optimization stage to reduce doom loops in long reasoning traces. This stage identifies tokens that tend to trigger looping behavior in specific contexts, then redistributes probability mass toward plausible alternatives, while leaving the rest of the next-token distribution largely intact. During RL, we also added a lightweight shaping reward that discourages excessive use of common loop-inducing restart words like “Wait…”. We'll share more details on the full pipeline, objective, and empirical results in a dedicated blog post.

**Hallucinations.** Because of their small number of parameters, edge models have a limited knowledge capacity, which leads to more hallucinations. To mitigate hallucinations, we added a targeted RL stage that uses an avg@k-based reward over a diverse knowledge dataset. The goal is to reinforce abstention on queries beyond reliable knowledge while preserving existing knowledge. This produces a sharper knowledge boundary and clearer expression of uncertainty.

## Benchmarks

We evaluated LFM2.5-8B-A1B across benchmarks covering knowledge, instruction following, math, and agentic workflows. The model is competitive with both dense alternatives with a similar total number of parameters and much larger MoEs.

The avg@k-based reward enables LFM2.5-8B-A1B to achieve a significantly lower hallucination rate while maintaining reasonable accuracy. It also leads on instruction following benchmarks, matching bigger MoEs like Gemma 4-26B at a fraction of the active parameter count.

### Math and agentic workflows

On agentic benchmarks, LFM2.5-8B-A1B is competitive with bigger models and particularly strong on Tau2-Telecom. As agentic harnesses are becoming the main way to consume models, LFM2.5-8B-A1B is a first step towards powering on-device, fully private agents.

## Sparse Inference, Everywhere

LFM2.5-8B-A1B ships with day-one support across the inference ecosystem:

**LEAP**— Liquid's Edge AI Platform for iOS and Android deployment**llama.cpp**— GGUF checkpoints for efficient edge inference**MLX**— Optimized inference for Apple Silicon**vLLM**— GPU-accelerated serving for production throughput**SGLang**— GPU-accelerated serving for production throughput**ONNX**— Cross-platform inference across diverse accelerators

**CPU inference.** LFM2.5-8B-A1B ships with day-one llama.cpp support and runs on everyday consumer hardware.

![](https://cdn.prod.website-files.com/67cb8aa6e9184b6e44813189/6a1788594d077d0205e0e94a_lfm2_5_8b_a1b_cpu_inference.png)

On both laptop-class chips, it is the fastest model we tested at reading in prompts and generating answers, decoding 253 tokens/s on an M5 Max and 146 on a Ryzen AI Max+ 395 while staying under 6 GB. It even holds ~30 tokens/s on a phone, so a capable assistant runs instantly and privately on your own device.

**GPU inference.** We support inference via vLLM and SGLang via active contributions to these codebases. We measure output throughput (total output tokens divided by wall time) on a single NVIDIA H100 SXM5 GPU using a sustained-load setting: at each concurrency level, we continuously maintain the target number of in-flight requests, replacing each completed request immediately.

![](https://cdn.prod.website-files.com/67cb8aa6e9184b6e44813189/6a1788bd6e860fb6f2bc1740_lfm2_5_8b_a1b_gpu_inference.png)

We benchmark each model with SGLang 0.5.12, 1,024 input tokens, up to 256 output tokens, in BF16, averaging 3 runs per concurrency level. LFM2.5-8B-A1B is the fastest model in its size class, reaching 18.5K output tokens per second at high concurrency, over 1.6B tokens per day on a single H100.

## Local Cowork: see it run

Our open-source desktop agent demo, [LocalCowork](https://github.com/Liquid4All/cookbook/tree/main/examples/localcowork), now runs on LFM2.5-8B-A1B. The setup is the same one we used for [LFM2-24B-A2B demo](https://www.liquid.ai/blog/no-cloud-tool-calling-agents-consumer-hardware-lfm2-24b-a2b) in March: a single laptop, 67 tools across 13 MCP servers, no cloud, no API keys, no data leaving the machine. Tool selection is faster and noticeably more reliable across the same tool menu.

The point of the demo is not the individual tools. It is that the **tool-dispatch loop feels interactive** on consumer hardware: ask, propose, confirm, run, repeat, all in well under a second per dispatch, with full audit trails and your data never leaving the device.


## Get Started

With LFM2.5, we're delivering on our vision of AI that runs anywhere. These models are:

**Open-weight**— Download, fine-tune, and deploy without restrictions**Fast from day one**— Native support for llama.cpp, MLX, vLLM, SGLang across Apple, AMD, Intel, Qualcomm, and Nvidia hardware**A complete family**— From base models for customization to specialized audio and vision variants, one architecture covers diverse use cases

The on-device agentic future starts here. We can't wait to see what you build.
