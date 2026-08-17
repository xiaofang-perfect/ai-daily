---
title: "LLMRouter: Unified Infrastructure for Developing, Evaluating, and Deploying LLM Routers"
source: HuggingFace Daily Papers · 2026-08-16
url: https://arxiv.org/abs/2608.06867
date: 2026-08-17
published_at: 2026-08-16T12:00:00+00:00
tag: 论文研究
item_id: 650329bc8a5459de
---
# Computer Science > Computation and Language

  [Submitted on 7 Aug 2026]

    # Title:LLMRouter: Unified Infrastructure for Developing, Evaluating, and Deploying LLM Routers

[View PDF](https://arxiv.org/pdf/2608.06867)

[HTML (experimental)](https://arxiv.org/html/2608.06867v1)

            Abstract:No single large language model (LLM) is optimal across all queries and budget constraints, making model routing essential for cost-effective deployment. Existing routers adopt diverse formulations and implementations, making fair comparison and extension difficult. We present a unified formulation of LLM routing as a sequential decision process characterized by five components: context encoders, model encoders, scoring functions, decision rules, and learning signals, covering single-turn, multi-turn, and personalized routing. Based on this formulation, we develop an automated pipeline for constructing routing supervision and evaluating routers jointly on response quality and inference cost. The resulting benchmark, xRouteBench, spans generic LLM, memory-augmented, vision, time-series, and personalized routing tasks. We further introduce LLMRouter, an open-source modular infrastructure with more than 16 representative routers. Our empirical study shows that learned routers outperform the strongest fixed-model baseline by 14.6% relatively, lightweight routers become more competitive under tight cost constraints, and user-conditioned routing consistently improves personalization.
    

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

            Bibliographic Explorer 

        *(*[What is the Explorer?](https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer))
            Connected Papers 

        *(*[What is Connected Papers?](https://www.connectedpapers.com/about))
            Litmaps 

        *(*[What is Litmaps?](https://www.litmaps.co/))
            scite Smart Citations 

        *(*[What are Smart Citations?](https://www.scite.ai/))
# Code, Data and Media Associated with this Article

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

        *(*[What is ScienceCast?](https://sciencecast.org/welcome))
# Demos

# Recommenders and Search Tools

              Influence Flower 

          *(*[What are Influence Flowers?](https://influencemap.cmlab.dev/))
              CORE Recommender 

          *(*[What is CORE?](https://core.ac.uk/services/recommender))
# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? [**Learn more about arXivLabs**](https://info.arxiv.org/labs/index.html).
