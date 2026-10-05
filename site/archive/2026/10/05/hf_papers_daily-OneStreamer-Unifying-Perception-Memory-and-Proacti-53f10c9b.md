---
title: "OneStreamer: Unifying Perception, Memory, and Proactive Response in Streaming Video Interaction"
source: HuggingFace Daily Papers · 2026-10-04
url: https://arxiv.org/abs/2610.01762
date: 2026-10-05
published_at: 2026-10-04T12:00:00+00:00
tag: 论文研究
item_id: 53f10c9b3c57db41
---
# Computer Science > Computer Vision and Pattern Recognition

\[Submitted on 1 Oct 2026\]

# Title:OneStreamer: Unifying Perception, Memory, and Proactive Response in Streaming Video Interaction

[View PDF](https://arxiv.org/pdf/2610.01762)

[HTML (experimental)](https://arxiv.org/html/2610.01762v1)

Abstract:Streaming video LLMs must retain evidence before its relevance to future tasks is known and respond when sufficient evidence becomes available. The challenge is to form reusable factual memory without compromising real-time perception. We introduce OneStreamer, which jointly learns query-independent evidence recording and task response through a shared proactive generation process. Its Proactive Hierarchical Caption Memory (PHCM) produces time-grounded local-detail captions and summaries of completed events. Streaming caption targets supervise the interpretation of observed video prefixes during training. At inference, model-generated records complement a recent visual window, providing reusable factual context without revisiting historical visual features. Proactive State Transition Learning (PSTL) reduces the dominance of repeated waiting states by preserving supervision at all output anchors and selecting representative state-change and state-persistence tokens. We further develop a streaming data synthesis pipeline that aligns output content and timing with available evidence. Combining the resulting streaming captions and QA with cleaned open-source data yields OneStreamer-1M, a broad-coverage streaming video interaction dataset with over one million records spanning diverse tasks. Our 4B model achieves the best results among the compared methods across all eight evaluated streaming video understanding benchmarks. Ablations show that retaining generated captions improves historical QA without degrading real-time perception. PSTL also outperforms dense state supervision while supervising only 27.5% of annotated state tokens. Together, these results support proactive generation as a shared learning interface connecting perception, memory formation, and timely response in streaming video interaction.

[Full-text links:]

## Access Paper:

[view license](http://creativecommons.org/licenses/by/4.0/)

![license icon](https://arxiv.org/icons/licenses/by-4.0.png) 

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
