---
title: "NVIDIA Introduces Hardware-Aware LLM Compression"
source: TLDR AI · 2026-11-10
url: https://arxiv.org/abs/2611.08290?utm_source=tldrai
date: 2026-11-11
published_at: 2026-11-10T12:00:00+00:00
tag: 论文研究
item_id: 43a152452c0d5502
---
# Computer Science > Machine Learning

\[Submitted on 5 Nov 2026\]

# Title:AutoCompress: Automated Hardware-Guided Model Compression

[View PDF](https://arxiv.org/pdf/2611.08290)

[HTML (experimental)](https://arxiv.org/html/2611.08290v1)

Abstract:LLM pruning must preserve quality while meeting hardware- and workload-specific constraints on latency, throughput, and memory. Existing pruning workflows often target parameter counts, requiring practitioners to manually select model sizes that meet latency, throughput, and GPU memory limits. However, parameter count alone does not predict these metrics, which depend on the model architecture, workload, hardware, and serving engine. We introduce AutoCompress, a hardware-guided compression framework that directly incorporates such constraints into differentiable architecture search. AutoCompress jointly optimizes global and per-layer structure to produce heterogeneous architectures, guided by serving-engine cost models validated against end-to-end latency, throughput, and memory measurements. We evaluate AutoCompress on long-context local coding, batched datacenter serving, and latency-sensitive in-game interaction. Compared to the state-of-the-art Minitron pruning framework, AutoCompress improves average accuracy across eight benchmarks by 6.57, 2.35, and 0.57 percentage points on RTX 5070, RTX 5080, and H100, respectively. AutoCompress also compresses Nemotron 3.5 Super from 120B to 74B parameters for single-B200 BF16 serving at 128K context, retaining 95% of its mean benchmark score.

[Full-text links:]

## Access Paper:

[view license](http://creativecommons.org/licenses/by/4.0/)

![license icon](https://arxiv.org/icons/licenses/by-4.0.png) 

### Additional Features

### References & Citations

Loading...

### Bookmark

![BibSonomy](https://arxiv.org/static/browse/0.3.4/images/icons/social/bibsonomy.png) 

![Reddit](https://arxiv.org/static/browse/0.3.4/images/icons/social/reddit.png) 

# Bibliographic and Citation Tools

Bibliographic Explorer *([What is the Explorer?](https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer))*

Connected Papers *([What is Connected Papers?](https://www.connectedpapers.com/about))*

Litmaps *([What is Litmaps?](https://www.litmaps.co/))*

scite Smart Citations *([What are Smart Citations?](https://www.scite.ai/))*

# Code, Data and Media Associated with this Article

alphaXiv *([What is alphaXiv?](https://alphaxiv.org/))*

CatalyzeX Code Finder for Papers *([What is CatalyzeX?](https://www.catalyzex.com))*

DagsHub *([What is DagsHub?](https://dagshub.com/))*

Gotit.pub *([What is GotitPub?](http://gotit.pub/faq))*

Hugging Face *([What is Huggingface?](https://huggingface.co/huggingface))*

ScienceCast *([What is ScienceCast?](https://sciencecast.org/welcome))*

# Demos

# Recommenders and Search Tools

Influence Flower *([What are Influence Flowers?](https://influencemap.cmlab.dev/))*

CORE Recommender *([What is CORE?](https://core.ac.uk/services/recommender))*

IArxiv Recommender
              *([What is IArxiv?](https://iarxiv.org/about))*

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? [**Learn more about arXivLabs**](https://info.arxiv.org/labs/index.html).
