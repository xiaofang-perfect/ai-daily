---
title: "SafeAnchor: Preventing Cumulative Safety Erosion in Continual Domain Adaptation of Large Language Models"
source: ArXiv cs.AI
url: https://arxiv.org/abs/2604.17691v1
date: 2026-04-20
published_at: 2026-04-20T01:13:36+00:00
tag: 论文研究
item_id: 95cbbe248502ba83
---
# Computer Science > Machine Learning

[Submitted on 20 Apr 2026]

# Title:SafeAnchor: Preventing Cumulative Safety Erosion in Continual Domain Adaptation of Large Language Models

[View PDF](https://arxiv.org/pdf/2604.17691v1)

[HTML (experimental)](https://arxiv.org/html/2604.17691v1)

Abstract:Safety alignment in large language models is remarkably shallow: it is concentrated in the first few output tokens and reversible by fine-tuning on as few as 100 adversarial examples. This fragility becomes critical in real-world deployment, where models undergo sequential adaptation across domains such as medicine, law, and code, causing safety guardrails to erode cumulatively. Yet all existing safety-preserving methods target only single-task fine-tuning, leaving the multi-domain sequential setting entirely unaddressed.

We introduce SafeAnchor, a framework that anchors safety in place throughout continual adaptation. SafeAnchor first identifies low-rank safety subspaces in LoRA parameter space via Fisher Information eigendecomposition, then constrains domain-specific gradient updates to the orthogonal complement of these subspaces, and finally monitors for residual safety drift with threshold-triggered corrective replay. Evaluated on Llama-2-7B-Chat and Mistral-7B-Instruct across a three-domain pipeline and eight benchmarks, SafeAnchor retains 93.2% of original safety alignment, outperforming all baselines by 18-42 points, while matching unconstrained fine-tuning to within 1.5 points on domain tasks.

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
