---
title: "Ulterior Motives: Detecting Misaligned Reasoning in Continuous Thought Models"
source: ArXiv cs.AI
url: https://arxiv.org/abs/2604.23460v1
date: 2026-04-26
published_at: 2026-04-25T22:43:15+00:00
tag: 论文研究
item_id: e0da32572c4a91d8
---
# Computer Science > Artificial Intelligence

[Submitted on 25 Apr 2026]

# Title:Ulterior Motives: Detecting Misaligned Reasoning in Continuous Thought Models

[View PDF](https://arxiv.org/pdf/2604.23460v1)

[HTML (experimental)](https://arxiv.org/html/2604.23460v1)

Abstract:Chain-of-Thought (CoT) reasoning has emerged as a key technique for eliciting complex reasoning in Large Language Models (LLMs). Although interpretable, its dependence on natural language limits the model's expressive bandwidth. Continuous thought models address this bottleneck by reasoning in latent space rather than human-readable tokens. While they enable richer representations and faster inference, they raise a critical safety question: how can we detect misaligned reasoning in an uninterpretable latent space? To study this, we introduce MoralChain, a benchmark of 12,000 social scenarios with parallel moral/immoral reasoning paths. We train a continuous thought model with backdoor behavior using a novel dual-trigger paradigm - one trigger that arms misaligned latent reasoning ([T]) and another that releases harmful outputs ([O]). We demonstrate three findings: (1) continuous thought models can exhibit misaligned latent reasoning while producing aligned outputs, with aligned and misaligned reasoning occupying geometrically distinct regions of latent space; (2) linear probes trained on behaviorally-distinguishable conditions ([T][O] vs [O]) transfer to detecting armed-but-benign states ([T] vs baseline) with high accuracy; and (3) misalignment is encoded in early latent thinking tokens, suggesting safety monitoring for continuous thought models should target the "planning" phase of latent reasoning.

### Current browse context:

cs.AI

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
