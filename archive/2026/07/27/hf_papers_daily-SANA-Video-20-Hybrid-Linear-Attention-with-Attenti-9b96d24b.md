---
title: "SANA-Video 2.0: Hybrid Linear Attention with Attention Residuals for Efficient Video Generation"
source: HuggingFace Daily Papers · 2026-07-26
url: https://arxiv.org/abs/2607.21553
date: 2026-07-27
published_at: 2026-07-26T12:00:00+00:00
tag: 论文研究
item_id: 9b96d24b103dd916
---
# Computer Science > Computer Vision and Pattern Recognition

  [Submitted on 23 Jul 2026]

    # Title:SANA-Video 2.0: Hybrid Linear Attention with Attention Residuals for Efficient Video Generation

[View PDF](https://arxiv.org/pdf/2607.21553)

[HTML (experimental)](https://arxiv.org/html/2607.21553v1)

Abstract:We introduce SANA-Video 2.0, a hybrid video diffusion transformer instantiated at 5B and 14B scales under a unified architecture. Designed to generate high-quality video up to 720p on a single GPU, SANA-Video 2.0 matches full-softmax video DiTs in quality while retaining the favorable long-sequence scaling of linear attention. To avoid quadratic attention throughout, Hybrid Linear-Softmax Attention combines gated linear attention for O(N)-dominated mixing with periodic gated-softmax anchors at a 3:1 ratio, restoring the full-rank token interactions that pure linear attention lacks. To propagate these refreshed representations across depth, Block Attention Residuals (AttnRes) route completed block summaries into later linear layers, enabling anchor-feature reuse and boosting deep-layer effective rank by ~12%. Through from-scratch training, SANA-Video 2.0 learns the complete hybrid directly rather than linearizing pretrained models, with reduced-resolution proxy studies establishing 25% softmax as the optimal quality-efficiency trade-off. With 40-step sampling, SANA-Video 2.0 achieves a VBench score of 84.30 in 13.2s at 480p on a single H100, remaining competitive with far larger softmax video DiTs at a fraction of the latency. Its compiled DiT forward pass is 3.2x faster than a matched full-softmax baseline at 720p/60s, a gap that expands with video duration. Furthermore, full-stack Sol-Engine optimization (kernel fusion, caching, and sparse attention) accelerates this hardware-friendly backbone by a further 3.58x, bringing the 5B pipeline to 13.06s at 720p/5s and making it 120x faster than Wan 2.2-A14B on one H100. Overall, our hybrid design recovers softmax-level expressiveness at substantially reduced cost, unlocking scalable long, high resolution video generation.

[Full-text links:]

## Access Paper:

[view license](http://creativecommons.org/licenses/by-nc-nd/4.0/)

![license icon](https://arxiv.org/icons/licenses/by-nc-nd-4.0.png) 

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
