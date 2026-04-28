---
title: "Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model"
source: TLDR AI · 2026-04-23
url: https://simonwillison.net/2026/Apr/22/qwen36-27b/?utm_source=tldrai
date: 2026-04-24
published_at: 2026-04-23T12:00:00+00:00
tag: 产品发布
item_id: c6657fc63f2ccbe6
---
22nd April 2026 - Link Blog

** Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model** (

[via](https://news.ycombinator.com/item?id=47863217)) Big claims from Qwen about their latest open weight model:

Qwen3.6-27B delivers flagship-level agentic coding performance, surpassing the previous-generation open-source flagship Qwen3.5-397B-A17B (397B total / 17B active MoE) across all major coding benchmarks.


On Hugging Face [Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B/tree/main) is 807GB, this new [Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B/tree/main) is 55.6GB.

I tried it out with the 16.8GB Unsloth [Qwen3.6-27B-GGUF:Q4_K_M](https://huggingface.co/unsloth/Qwen3.6-27B-GGUF) quantized version and `llama-server`

using this recipe by [benob on Hacker News](https://news.ycombinator.com/item?id=47863217#47865140), after first installing `llama-server`

using `brew install llama.cpp`

:

```
llama-server \
-hf unsloth/Qwen3.6-27B-GGUF:Q4_K_M \
--no-mmproj \
--fit on \
-np 1 \
-c 65536 \
--cache-ram 4096 -ctxcp 2 \
--jinja \
--temp 0.6 \
--top-p 0.95 \
--top-k 20 \
--min-p 0.0 \
--presence-penalty 0.0 \
--repeat-penalty 1.0 \
--reasoning on \
--chat-template-kwargs '{"preserve_thinking": true}'
```


On first run that saved the ~17GB model to `~/.cache/huggingface/hub/models--unsloth--Qwen3.6-27B-GGUF`

.

Here's [the transcript](https://gist.github.com/simonw/4d99d730c840df594096366db1d27281) for "Generate an SVG of a pelican riding a bicycle". This is an *outstanding* result for a 16.8GB local model:

![Bicycle has spokes, a chain and a correctly shaped frame. Handlebars are a bit detached. Pelican has wing on the handlebars, weirdly bent legs that touch the pedals and a good bill. Background details are pleasant - semi-transparent clouds, birds, grass, sun.](https://static.simonwillison.net/static/2026/Qwen3.6-27B-GGUF-Q4_K_M.png)


Performance numbers reported by `llama-server`

:

- Reading: 20 tokens, 0.4s, 54.32 tokens/s
- Generation: 4,444 tokens, 2min 53s, 25.57 tokens/s

For good measure, here's [Generate an SVG of a NORTH VIRGINIA OPOSSUM ON AN E-SCOOTER](https://gist.github.com/simonw/95735fe5e76e6fdf1753e6dcce360699) (run previously [with GLM-5.1](https://simonwillison.net/2026/Apr/7/glm-51/)):

![Digital illustration in a neon Tron-inspired style of a grey cat-like creature wearing cyan visor goggles riding a glowing cyan futuristic motorcycle through a dark cityscape at night, with its long tail trailing behind, silhouetted buildings with yellow-lit windows in the background, and a glowing magenta moon on the right.](https://static.simonwillison.net/static/2026/qwen3.6-27b-possum.jpg)


That one took 6,575 tokens, 4min 25s, 24.74 t/s.

## Recent articles

[Tracking the history of the now-deceased OpenAI Microsoft AGI clause](https://simonwillison.net/2026/Apr/27/now-deceased-agi-clause/)- 27th April 2026[DeepSeek V4 - almost on the frontier, a fraction of the price](https://simonwillison.net/2026/Apr/24/deepseek-v4/)- 24th April 2026[Extract PDF text in your browser with LiteParse for the web](https://simonwillison.net/2026/Apr/23/liteparse-for-the-web/)- 23rd April 2026
