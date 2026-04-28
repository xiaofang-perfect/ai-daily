---
title: "Event Tensor: A Unified Abstraction for Compiling Dynamic Megakernel"
source: ArXiv cs.AI
url: https://arxiv.org/abs/2604.13327v2
date: 2026-04-15
published_at: 2026-04-14T22:19:51+00:00
tag: 论文研究
item_id: 45de2627308077b0
---
# Computer Science > Distributed, Parallel, and Cluster Computing

[Submitted on 14 Apr 2026 (

[v1](https://arxiv.org/abs/2604.13327v1)), last revised 21 Apr 2026 (this version, v2)]# Title:Event Tensor: A Unified Abstraction for Compiling Dynamic Megakernel

[View PDF](https://arxiv.org/pdf/2604.13327v2)

[HTML (experimental)](https://arxiv.org/html/2604.13327v2)

Abstract:Modern GPU workloads, especially large language model (LLM) inference, suffer from kernel launch overheads and coarse synchronization that limit inter-kernel parallelism. Recent megakernel techniques fuse multiple operators into a single persistent kernel to eliminate launch gaps and expose inter-kernel parallelism, but struggle to handle dynamic shapes and data-dependent computation in real workloads. We present Event Tensor, a unified compiler abstraction for dynamic megakernels. Event Tensor encodes dependencies between tiled tasks, and enables first-class support for both shape and data-dependent dynamism. Built atop this abstraction, our Event Tensor Compiler (ETC) applies static and dynamic scheduling transformations to generate high-performance persistent kernels. Evaluations show that ETC achieves state-of-the-art LLM serving latency while significantly reducing system warmup overhead.

## Submission history

From: Hongyi Jin [[view email](https://arxiv.org/show-email/b2d50985/2604.13327)]

**Tue, 14 Apr 2026 22:19:51 UTC (1,005 KB)**

[[v1]](https://arxiv.org/abs/2604.13327v1)**[v2]**Tue, 21 Apr 2026 00:31:44 UTC (1,005 KB)

### Current browse context:

cs.DC

### References & Citations

Loading...

# Bibliographic and Citation Tools

Bibliographic Explorer

*(*[What is the Explorer?](https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer))
Connected Papers

*(*[What is Connected Papers?](https://www.connectedpapers.com/about))
Litmaps

*(*[What is Litmaps?](https://www.litmaps.co/))
scite Smart Citations

*(*[What are Smart Citations?](https://www.scite.ai/))# Code, Data and Media Associated with this Article

alphaXiv

*(*[What is alphaXiv?](https://alphaxiv.org/))
CatalyzeX Code Finder for Papers

*(*[What is CatalyzeX?](https://www.catalyzex.com))
DagsHub

*(*[What is DagsHub?](https://dagshub.com/))
Gotit.pub

*(*[What is GotitPub?](http://gotit.pub/faq))
Hugging Face

*(*[What is Huggingface?](https://huggingface.co/huggingface))
ScienceCast

*(*[What is ScienceCast?](https://sciencecast.org/welcome))# Demos

# Recommenders and Search Tools

Influence Flower

*(*[What are Influence Flowers?](https://influencemap.cmlab.dev/))
CORE Recommender

*(*[What is CORE?](https://core.ac.uk/services/recommender))# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? [ Learn more about arXivLabs](https://info.arxiv.org/labs/index.html).
