---
title: "CSAttention: Centroid-Scoring Attention for Accelerating LLM Inference"
source: ArXiv cs.AI
url: https://arxiv.org/abs/2604.08584v1
date: 2026-03-30
published_at: 2026-03-30T01:42:29+00:00
tag: 论文研究
item_id: 6fccd19b9ddb0a9e
---
# Computer Science > Machine Learning

[Submitted on 30 Mar 2026]

# Title:CSAttention: Centroid-Scoring Attention for Accelerating LLM Inference

[View PDF](https://arxiv.org/pdf/2604.08584v1)

[HTML (experimental)](https://arxiv.org/html/2604.08584v1)

Abstract:Long-context LLMs increasingly rely on extended, reusable prefill prompts for agents and domain Q&A, pushing attention and KV-cache to become the dominant decode-time bottlenecks. While sparse attention reduces computation and transfer costs, it often struggles to maintain accuracy at high sparsity levels due to the inherent distribution shift between Queries and Keys. We propose Centroid-Scoring Attention (CSAttention), a training-free sparse attention method optimized for high-throughput serving of reusable contexts. CSAttention adopts a storage-for-computation strategy tailored to the offline-prefill/online-decode setting: it front-loads computation into a one-time offline prefill phase that can be amortized across multiple queries, while aggressively optimizing per-step decoding latency. Specifically, CSAttention constructs query-centric lookup tables during offline prefill, whose size remains fixed during decoding, and enables online decoding to replace full-context scans with efficient table lookups and GPU-friendly score accumulation. Extensive experiments demonstrate that CSAttention achieves near-identical accuracy to full attention. Under high sparsity (95%) and long-context settings (32K-128K), CSAttention consistently outperforms state-of-the-art sparse attention methods in both model accuracy and inference speed, achieving up to 4.6x inference speedup over the most accurate baseline at a context length of 128K.

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

*(*[What is CORE?](https://core.ac.uk/services/recommender))
IArxiv Recommender

*(*[What is IArxiv?](https://iarxiv.org/about))# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? [ Learn more about arXivLabs](https://info.arxiv.org/labs/index.html).
