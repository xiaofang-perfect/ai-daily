---
title: "Evaluating CUDA Tile for AI Workloads on Hopper and Blackwell GPUs"
source: ArXiv cs.AI
url: https://arxiv.org/abs/2604.23466v1
date: 2026-04-26
published_at: 2026-04-25T23:13:47+00:00
tag: 论文研究
item_id: 045e7571819546bb
---
# Computer Science > Machine Learning

[Submitted on 25 Apr 2026]

# Title:Evaluating CUDA Tile for AI Workloads on Hopper and Blackwell GPUs

[View PDF](https://arxiv.org/pdf/2604.23466v1)

[HTML (experimental)](https://arxiv.org/html/2604.23466v1)

Abstract:NVIDIA's CUDA Tile (CuTile) introduces a Python-based, tile-centric abstraction for GPU kernel development that aims to simplify programming while retaining Tensor Core and Tensor Memory Accelerator (TMA) efficiency on modern GPUs. We present the first independent, cross-architecture evaluation of CuTile against established approaches such as cuBLAS, Triton, WMMA, and raw SIMT on three NVIDIA GPUs spanning Hopper and Blackwell: H100 NVL, B200, and RTX PRO 6000 Blackwell Server Edition. We benchmark representative AI workloads, including GEMM, fused multi-head attention, and end-to-end LLM inference in BF16/FP16 precision, to assess both performance and portability.

Our results show that CuTile effectiveness is strongly workload- and architecture-dependent. On datacenter-class Blackwell (B200), CuTile achieves up to 1007 TFLOP/s for fused attention, outperforming FlashAttention-2 by 2.5x while requiring only 60 lines of Python kernel code. For GEMM, CuTile reaches 52-79% of cuBLAS performance in 22 lines of code (versus 123 for WMMA), making it a practical replacement for hand-written CUDA kernels but not yet for vendor-optimized libraries. However, the same CuTile attention kernel achieves only 53% of FlashAttention-2 throughput on RTX PRO 6000 (sm_120), exposing significant cross-architecture optimization gaps. In contrast, Triton sustains 62-101% of cuBLAS performance across all tested platforms without architecture-specific tuning, demonstrating substantially stronger portability.

### Current browse context:

cs.LG

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
