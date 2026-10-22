---
title: "LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data"
source: ArXiv cs.AI
url: https://arxiv.org/abs/2610.30132v1
date: 2026-10-22
published_at: 2026-10-21T17:59:14+00:00
tag: 论文研究
item_id: 1f6fd6255ada1806
---
# Computer Science > Computation and Language

\[Submitted on 21 Oct 2026\]

# Title:LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data

[View PDF](https://arxiv.org/pdf/2610.30132v1)

[HTML (experimental)](https://arxiv.org/html/2610.30132v1)

Abstract:Reinforcement learning (RL) is an effective way to strengthen the long-context reasoning of large language models (LLMs), but it needs training data that are long, diverse, challenging, and verifiable. Human annotation of such data is expensive, naturally occurring data are too scarce to sustain RL, and existing synthesis methods depend on external corpora or stronger teacher models, which become harder to obtain as the trained models get stronger. Recently, RL from zero data, in which a model learns from tasks it proposes itself, has achieved excellent performance, but existing methods target short-context tasks. Therefore, we propose $\textbf{LongZero}$, a method that lets an LLM improve its own long-context reasoning without any external data. Instead of writing questions and answers over existing documents, LongZero first has the model synthesize the question and answer with its supporting evidence in a compact structured form, and only then separately expands the evidence into a long multi-document context. LongZero combines these self-written multi-hop reasoning tasks with self-written multi-round retrieval tasks and trains the model with GRPO. We evaluate LongZero on two LLMs across five long-context reasoning benchmarks and compare it with RL on data synthesized from external corpora. Experimental results show that LongZero can generalize to real tasks, and outperforms both baselines, suggesting a viable and promising path to improving long-context reasoning of LLMs.

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

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? [**Learn more about arXivLabs**](https://info.arxiv.org/labs/index.html).
