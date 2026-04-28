---
title: "Google's TurboQuant AI-compression algorithm can reduce LLM memory usage by 6x"
source: TLDR AI · 2026-03-26
url: https://arstechnica.com/ai/2026/03/google-says-new-turboquant-compression-can-lower-ai-memory-usage-without-sacrificing-quality/?utm_source=tldrai
date: 2026-03-27
published_at: 2026-03-26T12:00:00+00:00
tag: 论文研究
item_id: 0795693d13bfc8e6
---
Even if you don’t know much about the inner workings of generative AI models, you probably know they need a lot of memory. Hence, it is currently almost impossible to buy a measly stick of RAM [without getting fleeced](https://arstechnica.com/gadgets/2025/12/for-just-a-couple-of-months-in-the-middle-of-2025-it-was-an-ok-time-to-build-a-pc/). Google Research recently [revealed TurboQuant](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/), a compression algorithm that reduces the memory footprint of large language models (LLMs) while also boosting speed and maintaining accuracy.

TurboQuant is aimed at reducing the size of the key-value cache, which Google likens to a “digital cheat sheet” that stores important information so it doesn’t have to be recomputed. This cheat sheet is necessary because, as we say all the time, LLMs don’t actually know anything; they can do a good impression of knowing things through the use of vectors, which map the semantic meaning of tokenized text. When two vectors are similar, that means they have conceptual similarity.

High-dimensional vectors, which can have hundreds or thousands of embeddings, may describe complex information like the pixels in an image or a large data set. They also occupy a lot of memory and inflate the size of the key-value cache, bottlenecking performance. To make models smaller and more efficient, developers employ quantization techniques to [run them at lower precision](https://arstechnica.com/gadgets/2025/12/the-npu-in-your-phone-keeps-improving-why-isnt-that-making-ai-better/). The drawback is that the outputs get worse—the quality of token estimation goes down. With TurboQuant, Google’s early results show an 8x performance increase and 6x reduction in memory usage in some tests *without* a loss of quality.

## Angles and errors

Applying TurboQuant to an AI model is a two-step process. To achieve high-quality compression, Google has devised a system called PolarQuant. Usually, vectors in AI models are encoded using standard XYZ coordinates, but PolarQuant converts vectors into polar coordinates in a Cartesian system. On this circular grid, the vectors are reduced to two pieces of information: a radius (core data strength) and a direction (the data’s meaning).
