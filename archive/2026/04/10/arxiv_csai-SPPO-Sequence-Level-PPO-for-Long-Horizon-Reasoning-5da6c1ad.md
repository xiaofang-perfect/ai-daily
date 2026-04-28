---
title: "SPPO: Sequence-Level PPO for Long-Horizon Reasoning Tasks"
source: ArXiv cs.AI
url: https://arxiv.org/abs/2604.08865v1
date: 2026-04-10
published_at: 2026-04-10T01:58:21+00:00
tag: 论文研究
item_id: 5da6c1addb7b4c9e
---
# Computer Science > Artificial Intelligence

[Submitted on 10 Apr 2026]

# Title:SPPO: Sequence-Level PPO for Long-Horizon Reasoning Tasks

[View PDF](https://arxiv.org/pdf/2604.08865v1)

[HTML (experimental)](https://arxiv.org/html/2604.08865v1)

Abstract:Proximal Policy Optimization (PPO) is central to aligning Large Language Models (LLMs) in reasoning tasks with verifiable rewards. However, standard token-level PPO struggles in this setting due to the instability of temporal credit assignment over long Chain-of-Thought (CoT) horizons and the prohibitive memory cost of the value model. While critic-free alternatives like GRPO mitigate these issues, they incur significant computational overhead by requiring multiple samples for baseline estimation, severely limiting training throughput. In this paper, we introduce Sequence-Level PPO (SPPO), a scalable algorithm that harmonizes the sample efficiency of PPO with the stability of outcome-based updates. SPPO reformulates the reasoning process as a Sequence-Level Contextual Bandit problem, employing a decoupled scalar value function to derive low-variance advantage signals without multi-sampling. Extensive experiments on mathematical benchmarks demonstrate that SPPO significantly surpasses standard PPO and matches the performance of computation-heavy group-based methods, offering a resource-efficient framework for aligning reasoning LLMs.

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
