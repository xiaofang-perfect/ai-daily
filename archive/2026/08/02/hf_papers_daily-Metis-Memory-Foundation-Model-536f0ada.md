---
title: "Metis: Memory Foundation Model"
source: HuggingFace Daily Papers · 2026-08-01
url: https://arxiv.org/abs/2607.26760
date: 2026-08-02
published_at: 2026-08-01T12:00:00+00:00
tag: 论文研究
item_id: 536f0adab045a43a
---
# Computer Science > Computation and Language

  [Submitted on 29 Jul 2026]

    # Title:Metis: Memory Foundation Model

[View PDF](https://arxiv.org/pdf/2607.26760)

[HTML (experimental)](https://arxiv.org/html/2607.26760v1)

            Abstract:Recent advances in AI agents have increasingly internalized native capabilities into their underlying foundation models, giving rise to multimodal foundation models and large reasoning models. However, agent memory is still primarily implemented through external modules, leaving the native memory capability largely unexplored. In this paper, we take a first step toward this direction by introducing memory foundation models, which empower foundation models with native memory capabilities. We formalize native memory from two perspectives: a persistent and dynamically evolving memory state within the backbone, and native memory procedures that autonomously store and utilize information through model computation. We show that native memory offers advantages in architecture, end-to-end optimization, and efficiency. Based on this formulation, we propose Metis, the first prototype of memory foundation models. Metis introduces a new architecture that equips a foundation model with a native memory state, allowing historical information to be compressed into the model and accessed through memory attention. We construct large-scale memory-specific training data and introduce multiple optimization objectives to acquire these native memory procedures through mid-training. The online memory maintenance of Metis is gradient-free, and the memory update requires only a forward pass. At inference time, all learned model weights remain frozen, while the native memory states are autonomously transformed through standard forward computation. Through extensive experiments, we show that Metis exhibits native memory capabilities and further provide a detailed analysis of its strengths, limitations, and behaviors. To facilitate future research on memory foundation models, we release our project and model checkpoints.
    

[Full-text links:]

## Access Paper:

[view license](http://creativecommons.org/licenses/by-nc-sa/4.0/)

![license icon](https://arxiv.org/icons/licenses/by-nc-sa-4.0.png) 

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
