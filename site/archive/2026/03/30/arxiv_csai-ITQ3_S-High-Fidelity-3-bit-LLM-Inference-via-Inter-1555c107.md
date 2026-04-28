---
title: "ITQ3_S: High-Fidelity 3-bit LLM Inference via Interleaved Ternary Quantization with Rotation-Domain Smoothing"
source: ArXiv cs.AI
url: https://arxiv.org/abs/2603.27914v2
date: 2026-03-30
published_at: 2026-03-30T00:03:22+00:00
tag: 论文研究
item_id: 1555c107860c52d2
---
# Computer Science > Machine Learning

[Submitted on 30 Mar 2026 (

[v1](https://arxiv.org/abs/2603.27914v1)), last revised 31 Mar 2026 (this version, v2)]# Title:ITQ3_S: High-Fidelity 3-bit LLM Inference via Interleaved Ternary Quantization with Rotation-Domain Smoothing

[View PDF](https://arxiv.org/pdf/2603.27914v2)

[HTML (experimental)](https://arxiv.org/html/2603.27914v2)

Abstract:We present ITQ3_S (Interleaved Ternary Quantization -- Specialized), a novel 3-bit weight quantization format for LLMs integrating TurboQuant (TQ), a rotation-domain strategy based on the Fast Walsh-Hadamard Transform (FWHT). Conventional 3-bit methods suffer precision loss from heavy-tailed weight distributions and inter-channel outliers. ITQ3_S pre-rotates the weight space via FWHT before quantization, spreading outlier energy across the vector and inducing a near-Gaussian distribution amenable to uniform ternary coding.

We derive a rigorous dequantization procedure fusing a 256-point Inverse FWHT into the CUDA shared-memory loading stage, ensuring reconstruction error is bounded exclusively by the ternary quantization grid with no additional error from the transform inversion. For any weight vector $\mathbf{w} \in \mathbb{R}^{256}$, the reconstruction satisfies $\|\hat{\mathbf{w}} - \mathbf{w}\|_2 \leq \epsilon_q$, strictly smaller than uniform 3-bit baselines that do not exploit rotation-induced distribution normalization.

TurboQuant lacks a native CUDA kernel, precluding direct deployment; naively composing TQ with existing weight quantizers introduces domain mismatch errors that accumulate across layers, degrading quality below standard 3-bit baselines. ITQ3_S resolves this by co-designing the FWHT rotation and quantization kernel as a unified pipeline grounded in the IQ3_S weight format, with the inverse transform fused into the CUDA MMQ kernel.

Empirically, on the NVIDIA RTX 5090 (Blackwell), ITQ3_S achieves perplexity competitive with FP16 while delivering throughput exceeding 1.5x that of 4-bit alternatives via optimized DP4A and Tensor Core scheduling. Our results establish ITQ3_S as a practical, mathematically grounded solution for high-fidelity LLM deployment on consumer hardware.

## Submission history

From: Edward J. Yoon [[view email](https://arxiv.org/show-email/db7740a3/2603.27914)]

**Mon, 30 Mar 2026 00:03:22 UTC (12 KB)**

[[v1]](https://arxiv.org/abs/2603.27914v1)**[v2]**Tue, 31 Mar 2026 03:02:45 UTC (12 KB)

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
