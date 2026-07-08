---
title: "Hy3"
source: TLDR AI · 2026-07-07
url: https://simonwillison.net/2026/Jul/6/hy3/?utm_source=tldrai
date: 2026-07-08
published_at: 2026-07-07T12:00:00+00:00
tag: 工具开源
item_id: ad3c6f79a74ecde9
---
6th July 2026 - Link Blog

** tencent/Hy3**. New Apache 2.0 licensed model from Tencent in China:

Hy3 is a 295B-parameter Mixture-of-Experts (MoE) model with 21B active parameters and 3.8B MTP layer parameters, developed by the Tencent Hy Team. Following the Hy3 Preview launch in late April, we gathered feedback from 50+ products and scaled up post-training with higher quality data. Today, we introduce Hy3, which outperforms similar-size models and rivals flagship open-source models with 2-5x parameters. It also shows significant gains in utility across various products and productivity tasks.


The full-sized model is 598GB on Hugging Face, and the FP8 quantized one [is 300GB](https://huggingface.co/tencent/Hy3-FP8/tree/main). The context length is 256K.

It's available for free [on OpenRouter until July 21st](https://openrouter.ai/tencent/hy3:free). I had it "Generate an SVG of a pelican riding a bicycle" there and got this:

![Flat-style cartoon illustration  of a white pelican with a large orange beak riding a red bicycle across a pale blue background, its long orange legs stretched down to the pedals, with gray horizontal motion lines behind it suggesting speed.](https://static.simonwillison.net/static/2026/hy3-pelican.png)


## Recent articles

- [sqlite-utils 4.0, now with database schema migrations](https://simonwillison.net/2026/Jul/7/sqlite-utils-4/)- 7th July 2026
- [sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)](https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/)- 5th July 2026
- [Have your agent record video demos of its work with shot-scraper video](https://simonwillison.net/2026/Jun/30/shot-scraper-video/)- 30th June 2026
