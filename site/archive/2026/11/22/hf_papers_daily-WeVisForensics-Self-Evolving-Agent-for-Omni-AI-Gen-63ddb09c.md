---
title: "WeVisForensics: Self-Evolving Agent for Omni AI-Generated Video Detection"
source: HuggingFace Daily Papers · 2026-11-21
url: https://arxiv.org/abs/2611.21373
date: 2026-11-22
published_at: 2026-11-21T12:00:00+00:00
tag: 论文研究
item_id: 63ddb09cdbbd1e9f
---
# Computer Science > Computer Vision and Pattern Recognition

\[Submitted on 16 Nov 2026\]

# Title:WeVisForensics: Self-Evolving Agent for Omni AI-Generated Video Detection

[View PDF](https://arxiv.org/pdf/2611.21373)

[HTML (experimental)](https://arxiv.org/html/2611.21373v1)

Abstract:Recent advances in video generation call for reliable detection grounded in explicit forensic evidence. However, current methods primarily depend on single-pass chain-of-thought reasoning that overlooks brief or localized artifacts, or on predefined multi-agent workflows that offer limited flexibility in selecting relevant inspections. Even with adaptive investigation, optimizing the investigation policy alone does not directly improve the forensic capabilities of fixed experts. We introduce WeVisForensics, an agentic framework in which a main investigator agent coordinates a self-evolving library of forensic inspector sub-agents spanning visual and audio cues. The investigator learns which artifact type to examine, over which window, and when to conclude, and these interactions provide shared feedback for both levels of agents. Our dual-timescale policy optimization strategy, DTPO, closes this loop through fast reinforcement learning of the investigator and slower refinement of the inspectors, guided by annotated artifact intervals, to report subtle artifacts they once dismissed. Furthermore, we curate ForenCue-30K, combining role-specific forensic annotations and interaction trajectories to supervise individual inspections and their coordination, with an accompanying reinforcement-learning pool. Experiments show that WeVisForensics averages 95.2% detection accuracy across in-domain, out-of-domain and agentic benchmarks, 9.0% above the strongest prior detector, while grounding its verdicts in localized evidence.

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
