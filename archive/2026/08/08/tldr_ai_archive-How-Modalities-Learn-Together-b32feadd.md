---
title: "How Modalities Learn Together"
source: TLDR AI · 2026-08-07
url: https://arxiv.org/abs/2608.05000?utm_source=tldrai
date: 2026-08-08
published_at: 2026-08-07T12:00:00+00:00
tag: 论文研究
item_id: b32feadd21da21d0
---
# Computer Science > Computer Vision and Pattern Recognition

  [Submitted on 5 Aug 2026 (

    [v1](https://arxiv.org/abs/2608.05000v1)), last revised 6 Aug 2026 (this version, v2)]
# Title:Towards Physics of Multimodal Pretraining: Knowledge Flow, Modality Synergy, Early Unification, and Recipes

[View PDF](https://arxiv.org/pdf/2608.05000)

[HTML (experimental)](https://arxiv.org/html/2608.05000v2)

            Abstract:Vision offers a critical axis for advancing foundation models, driving a shift towards natively unified multimodal pretraining. Despite this momentum, the design space and the fundamental mechanisms of how modalities interact during unified training remain underexplored. We provide empirical clarity through a systematic exploration of multimodal pretraining. Our controlled experiments on both synthetic and large-scale real-world datasets yield four key insights into the physics of multimodal pretraining: (i) Knowledge Flow: We disentangle how language, visual understanding, and visual generation transfer knowledge across modalities, revealing distinct patterns of influence and asymmetry; (ii) Synergy vs. Competition: We show that data "complexity" largely determines whether modalities are synergistic, identify architectural choices that promote synergy: such as shared attention and normalization with modality-specific feed-forward layers, and find that these behaviors generalize across different visual tokenizer designs; (iii) Early Unification: Unifying modalities from the very early stages and training them jointly is shown to be more effective than late alignment or sequential training. This process uncovers a vision laziness phenomenon, where delayed integration leads models to rely on language priors; (iv) Recipes: We derive efficient pretraining recipes that achieve strong generative performance using only 5% of the compute budget. These core findings are subsequently validated at scale by training multiple 13.5B MoE models on 2T tokens. We hope this study provides a principled foundation for understanding and scaling multimodal pretraining.
    

## Submission history

From: Junlin Han [
[view email](https://arxiv.org/show-email/8ef0bb22/2608.05000)]

**Wed, 5 Aug 2026 16:09:25 UTC (5,027 KB)**

[\[v1\]](https://arxiv.org/abs/2608.05000v1)
**[v2]**Thu, 6 Aug 2026 17:18:02 UTC (5,025 KB)

### Current browse context:

cs.CV

  
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
