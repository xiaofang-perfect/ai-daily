---
title: "Rethinking Generalization in Reasoning SFT: A Conditional Analysis on Optimization, Data, and Model Capability"
source: HuggingFace Daily Papers · 2026-04-12
url: https://arxiv.org/abs/2604.06628
date: 2026-04-13
published_at: 2026-04-12T12:00:00+00:00
tag: 论文研究
item_id: d1e369b11e56d53e
---
# Computer Science > Artificial Intelligence

[Submitted on 8 Apr 2026]

# Title:Rethinking Generalization in Reasoning SFT: A Conditional Analysis on Optimization, Data, and Model Capability

[View PDF](https://arxiv.org/pdf/2604.06628)

Abstract:A prevailing narrative in LLM post-training holds that supervised finetuning (SFT) memorizes while reinforcement learning (RL) generalizes. We revisit this claim for reasoning SFT with long chain-of-thought (CoT) supervision and find that cross-domain generalization is not absent but conditional, jointly shaped by optimization dynamics, training data, and base-model capability. Some reported failures are under-optimization artifacts: cross-domain performance first degrades before recovering and improving with extended training (a dip-and-recovery pattern), so shorttraining checkpoints can underestimate generalization. Data quality and structure both matter: low-quality solutions broadly hurt generalization,while verified long-CoT traces yield consistent cross-domain gains. Model capability is essential: stronger models internalize transferable procedural patterns (e.g., backtracking) even from a toy arithmetic game, while weaker ones imitate surface verbosity. This generalization is asymmetric, however: reasoning improves while safety degrades, reframing the question from whether reasoning SFT generalizes to under what conditions and at what cost.

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
