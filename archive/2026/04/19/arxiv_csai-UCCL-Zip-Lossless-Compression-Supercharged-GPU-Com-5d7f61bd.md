---
title: "UCCL-Zip: Lossless Compression Supercharged GPU Communication"
source: ArXiv cs.AI
url: https://arxiv.org/abs/2604.17172v2
date: 2026-04-19
published_at: 2026-04-19T00:05:36+00:00
tag: 工具开源
item_id: 5d7f61bd7dac0e3d
---
# Computer Science > Distributed, Parallel, and Cluster Computing

[Submitted on 19 Apr 2026 (

[v1](https://arxiv.org/abs/2604.17172v1)), last revised 21 Apr 2026 (this version, v2)]# Title:UCCL-Zip: Lossless Compression Supercharged GPU Communication

[View PDF](https://arxiv.org/pdf/2604.17172v2)

[HTML (experimental)](https://arxiv.org/html/2604.17172v2)

Abstract:The rapid growth of large language models (LLMs) has made GPU communication a critical bottleneck. While prior work reduces communication volume via quantization or lossy compression, these approaches introduce numerical errors that can degrade convergence, accuracy, and stability. We present UCCL-Zip, a unified design that integrates lossless compression directly into GPU communication primitives. UCCL-Zip supports both point-to-point (P2P) and collective communication without modifying user-facing APIs or compromising numerical correctness. For P2P communication, Uzip-P2P employs a split-send pipeline that exposes transmissible data early and overlaps compression with communication, while preserving high GPU efficiency by operating on large data blocks. For collective communication, Uzip-NCCL integrates compression into NCCL's persistent kernel model via fused execution, eliminating redundant memory traffic and kernel launches. In real workloads, UCCL-Zip accelerates RL weight synchronization by up to 47.5% and reduces vLLM end-to-end inference latency by up to 10%, all without application changes.

## Submission history

From: Yang Zhou [[view email](https://arxiv.org/show-email/95b94cfb/2604.17172)]

**Sun, 19 Apr 2026 00:05:36 UTC (150 KB)**

[[v1]](https://arxiv.org/abs/2604.17172v1)**[v2]**Tue, 21 Apr 2026 04:46:04 UTC (1,718 KB)

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
