---
title: "Introducing H3 Max by fal"
source: TLDR AI · 2026-08-28
url: https://blog.fal.ai/introducing-h3-max-by-fal/?utm_source=tldrai
date: 2026-08-29
published_at: 2026-08-28T12:00:00+00:00
tag: 产品发布
item_id: 1c328824905419fa
---
# Introducing H3 Max by fal

![Introducing H3 Max by fal](https://storage.ghost.io/c/0e/15/0e15ee8a-bd95-4b71-9258-950f77f4d196/content/images/size/w2000/2026/08/fal-glitch-dust-1080x1080-1787861178159.png) 

Announcing [H3 Max,](https://fal.ai/models/minimax/h3-max/image-to-video?ref=blog.fal.ai) a post-trained version of MiniMax H3 developed by fal Research and optimized for maximum speed by fal's inference team.

In our human preference evaluations, H3 Max ranks #1 across overall quality, prompt understanding, and aesthetics against leading video models. It does so while generating a 5-second video in under 3 seconds, which is roughly 35x the throughput of the official MiniMax H3 endpoint, and on average 15x faster than anything with comparable quality.

![](https://storage.ghost.io/c/0e/15/0e15ee8a-bd95-4b71-9258-950f77f4d196/content/images/2026/08/h3-max---benchmark---1---final--1-.png)

These results challenge a common tradeoff in generative video: that higher quality has to come at the cost of slower inference.

H3 Max is the result of working on both sides of that problem at once. We optimized the model for stronger real-world performance while co-designing the inference system around it to make sure faster than real-time is still possible. This required two capabilities that rarely sit under the same roof: frontier model research and deep inference optimization/kernel work.

## **Post-training H3 Max**

We started with the open-weights MiniMax H3 model and introduced substantial new data during post-training, with a particular focus on prompt adherence and visual quality. We aimed for a better model at much faster speed and after our work, the base model's core capabilities are intact with extremely low latency.

The MiniMax H3 team shared their perspective on H3 Max:

H3 Max combines SOTA video quality with a step-change in generation speed, making high-quality video generation practical across a much broader range of real-world applications. We’ve worked closely with fal since day one, and their expertise in generative AI infrastructure and bringing frontier models into production quickly and reliably makes them a natural partner for H3 Max.

Throughout post-training, we continuously evaluated checkpoints through head-to-head preference studies across three dimensions: overall quality, prompt understanding, and aesthetics. Evaluating these dimensions independently gave us a much clearer signal than optimizing against a single aggregate score.

The result is a model that meaningfully improves on the original H3 across the qualities people actually notice when generating video: understanding what you asked for and producing something you want to use.

## **Co-designing the inference engine**

With H3 Max, the research and inference work was deeply connected. Our inference team has spent the past four years optimizing diffusion and generative media workloads. For H3 Max, we applied those systems techniques while the model itself was still being developed, allowing decisions on the training and inference stack to inform each other. H3 Max was trained and served entirely on [__NVIDIA GB200 NVL72 systems__.](https://www.nvidia.com/en-us/data-center/gb200-nvl72/?ref=blog.fal.ai) On a per-chip basis, GB200s deliver up to 2x the performance of the previous-generation accelerators we used to train and serve our models.

The objective wasn't just a faster model, our team has also worked on maximizing the throughput while preserving the quality gains from post-training. That distinction shaped the entire optimization process.

There are ways to make a video model faster: reduce precision, remove sampling steps, or approximate expensive operations. Some produce impressive speedups while degrading the output. For H3 Max, an optimization only survived if the resulting model continued to hold its position in our internal quality evaluations.

## **Measuring quality**

Evaluating generative video is inherently difficult. Automated metrics capture only part of what makes one generation better than another, so our primary evaluation uses head-to-head human preferences.

We benchmarked H3 Max against twelve leading video models, including the official MiniMax H3 endpoint, Gemini Omni Flash, Wan 3.0, Seedance 2.5, Kling 3, and Veo 3.1.

Evaluators compared generations across three dimensions:

- Overall preference: which video they preferred as a whole
- Prompt understanding: which generation more faithfully followed the instruction
- Aesthetics: which generation was visually stronger

We aggregated these comparisons using Bayesian Elo ratings with 95% confidence intervals.

H3 Max ranks #1 across all three dimensions and wins the majority of head-to-head matchups against every model we tested, including the original H3.

![](https://storage.ghost.io/c/0e/15/0e15ee8a-bd95-4b71-9258-950f77f4d196/content/images/2026/08/data-src-image-1570af92-c3e9-4e1f-b09e-c4c43421213a.png)

The results hold up outside our own evaluations. In independent benchmarks from Artificial Analysis and Design Arena, H3 Max also ranks #1 against other video models.

![](https://storage.ghost.io/c/0e/15/0e15ee8a-bd95-4b71-9258-950f77f4d196/content/images/2026/08/data-src-image-ac7b2fc8-4f1c-4f71-b88e-c808e351e0c6.png)

On H3 Max, Design Arena noted:

MiniMax H3 Max by fal delivers the quality of MiniMax H3 at more than 50× the speed, according to Design Arena’s independent benchmarking, establishing a new speed–preference Pareto frontier.

![](https://storage.ghost.io/c/0e/15/0e15ee8a-bd95-4b71-9258-950f77f4d196/content/images/2026/08/data-src-image-cd20c665-9c2f-4f6a-8797-e98a3eded8f2.png)

## **Quality without the latency tradeoff**

The more interesting result is when we look at quality and speed together.

H3 Max generates a 5-second video in approximately 3 seconds. That's roughly 35x the throughput of the official H3 endpoint and faster than every other model in our comparison.

![](https://storage.ghost.io/c/0e/15/0e15ee8a-bd95-4b71-9258-950f77f4d196/content/images/2026/08/data-src-image-f29ec4bb-2dd2-4f4f-a91c-f422d48dbf82.png)

Typically, the frontier forces a choice: faster models occupy one end of the curve and higher-quality models occupy the other.

H3 Max moves the frontier.

It achieves the highest human-preference score in our evaluation while simultaneously delivering the highest throughput.

This is the advantage of treating model research and inference optimization as the same problem. Post-training gives us control over the quality of the model. Systems work gives us control over how efficiently that model executes. Co-designing the two means improvements don't have to come at each other's expense.

For generative media, this will increasingly matter. Models are getting larger and more computationally demanding at the same time that video generation is moving into interactive and high-volume production workloads.

A model isn't useful in production because it tops the benchmark in isolation. What matters is the frontier across quality, latency, and cost.

Our goal at fal is to push all three.

## **Try H3 Max**

H3 Max is available today on fal. Try it in the Playground, via [fal Agent](https://fal.ai/agent?ref=blog.fal.ai), or call it from the API.

For the first week, we're offering H3 Max at 50% off.

Try it now:

H3 Max was trained on fal Serverless, the same infrastructure available to developers and teams building their own models. [Learn more about fal Serverless](https://fal.ai/serverless?ref=blog.fal.ai).
