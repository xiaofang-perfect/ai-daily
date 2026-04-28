---
title: "Spike-driven Large Language Model"
source: ArXiv cs.AI
url: https://arxiv.org/abs/2604.16475v1
date: 2026-04-12
published_at: 2026-04-11T17:58:35+00:00
tag: 论文研究
item_id: 4e5f2843b43e69d2
---
# Computer Science > Neural and Evolutionary Computing

[Submitted on 11 Apr 2026]

# Title:Spike-driven Large Language Model

[View PDF](https://arxiv.org/pdf/2604.16475v1)

[HTML (experimental)](https://arxiv.org/html/2604.16475v1)

Abstract:Current Large Language Models (LLMs) are primarily based on large-scale dense matrix multiplications. Inspired by the brain's information processing mechanism, we explore the fundamental question: how to effectively integrate the brain's spiking-driven characteristics into LLM inference. Spiking Neural Networks (SNNs) possess spike-driven characteristics, and some works have attempted to combine SNNs with Transformers. However, achieving spike-driven LLMs with billions of parameters, relying solely on sparse additions, remains a challenge in the SNN field. To address the issues of limited representational capacity and sparsity in existing spike encoding schemes at the LLM level, we propose SDLLM, a spike-driven large language model that eliminates dense matrix multiplications through sparse addition operations. Specifically, we use the plug-and-play gamma-SQP two-step spike encoding method to ensure that the quantization process aligns with the model's semantic space, mitigating representation degradation caused by binary spikes. Furthermore, we introduce bidirectional encoding under symmetric quantization and membrane potential clipping mechanisms, leading to spike trains with no or low firing counts dominating, significantly reducing the model's spike firing rate, while halving the number of time steps. Experimental results show that SDLLM not only significantly reduces inference costs but also achieves state-of-the-art task performance under the spike-based paradigm. For example, compared to previous spike-based LLMs, SDLLM reduces energy consumption by 7x and improves accuracy by 4.2%. Our model provides inspiration for the architecture design of the next generation of event-driven neuromorphic chips.

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
