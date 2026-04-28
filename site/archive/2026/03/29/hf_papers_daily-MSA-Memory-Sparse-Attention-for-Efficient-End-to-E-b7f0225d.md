---
title: "MSA: Memory Sparse Attention for Efficient End-to-End Memory Model Scaling to 100M Tokens"
source: HuggingFace Daily Papers · 2026-03-28
url: https://arxiv.org/abs/2603.23516
date: 2026-03-29
published_at: 2026-03-28T12:00:00+00:00
tag: 论文研究
item_id: b7f0225d66c02311
---
# Computer Science > Computation and Language

[Submitted on 6 Mar 2026 (

[v1](https://arxiv.org/abs/2603.23516v1)), last revised 13 Apr 2026 (this version, v2)]# Title:MSA: Memory Sparse Attention for Efficient End-to-End Memory Model Scaling to 100M Tokens

[View PDF](https://arxiv.org/pdf/2603.23516)

[HTML (experimental)](https://arxiv.org/html/2603.23516v2)

Abstract:Long-term memory is a cornerstone of human intelligence. Enabling AI to process lifetime-scale information remains a long-standing pursuit in

the field. Due to the constraints of full-attention architectures, the effective context length of large language models (LLMs) is typically

limited to 1M tokens. Existing approaches, such as hybrid linear attention, fixed-size memory states (e.g., RNNs), and external storage

methods like RAG or agent systems, attempt to extend this limit. However, they often suffer from severe precision degradation and rapidly

increasing latency as context length grows, an inability to dynamically modify memory content, or a lack of end-to-end optimization. These

bottlenecks impede complex scenarios like large-corpus summarization, Digital Twins, and long-history agent reasoning, while limiting memory

capacity and slowing inference. We present Memory Sparse Attention (MSA), an end-to-end trainable, efficient, and massively scalable memory

model framework. Through core innovations including scalable sparse attention and document-wise RoPE, MSA achieves linear complexity in both

training and inference while maintaining exceptional stability, exhibiting less than 9% degradation when scaling from 16K to 100M tokens.

Furthermore, KV cache compression, combined with Memory Parallel, enables 100M-token inference on 2xA800 GPUs. We also propose Memory

Interleaving to facilitate complex multi-hop reasoning across scattered memory segments. MSA significantly surpasses frontier LLMs,

state-of-the-art RAG systems, and leading memory agents in long-context benchmarks. These results demonstrate that by decoupling memory

capacity from reasoning, MSA provides a scalable foundation to endow general-purpose models with intrinsic, lifetime-scale memory.

## Submission history

From: Runkai Chen [[view email](https://arxiv.org/show-email/26bcb16c/2603.23516)]

**Fri, 6 Mar 2026 02:29:54 UTC (383 KB)**

[[v1]](https://arxiv.org/abs/2603.23516v1)**[v2]**Mon, 13 Apr 2026 03:01:02 UTC (383 KB)

Current browse context:

cs.CL

### References & Citations

export BibTeX citation
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
