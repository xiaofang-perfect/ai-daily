---
title: "Moebius: 0.2B Lightweight Image Inpainting Framework with 10B-Level Performance"
source: HuggingFace Daily Papers · 2026-06-21
url: https://arxiv.org/abs/2606.19195
date: 2026-06-22
published_at: 2026-06-21T12:00:00+00:00
tag: 论文研究
item_id: 5c80050bf3ecf7a6
---
# Computer Science > Computer Vision and Pattern Recognition

  [Submitted on 17 Jun 2026]

    # Title:Moebius: 0.2B Lightweight Image Inpainting Framework with 10B-Level Performance

[View PDF](https://arxiv.org/pdf/2606.19195)

[HTML (experimental)](https://arxiv.org/html/2606.19195v1)

Abstract:While 10B-level industrial foundation models have pushed the boundaries of image inpainting, their prohibitive computational costs severely hinder practical deployment. Constructing a highly optimized task-specific specialist offers a promising solution; however, extreme structural compression inevitably triggers a severe representation bottleneck. To conquer this, we propose Moebius, a highly efficient lightweight inpainting framework. We systematically reconstruct the diffusion backbone by introducing the Local-$\lambda$ Mix Interaction ($L\lambda MI$) block. Comprising Local-$\lambda$ and Interactive-$\lambda$ modules, it elegantly summarizes spatial contexts and global semantic priors into fixed-size linear matrices, preserving complex latent interactions while drastically shedding parameters. Furthermore, to unlock the full representational capacity of this highly compact architecture, we synergistically pair it with an adaptive multi-granularity distillation strategy. Operating strictly within the latent space to avoid expensive pixel-space decoding, this strategy dynamically balances multiple gradient-based losses to achieve high-fidelity alignment. Extensive experiments across natural and portrait benchmarks demonstrate that this optimal synergy enables Moebius to rival or even surpass the generation quality of the 10B-level industrial generalist FLUX.1-Fill-Dev. Remarkably, Moebius achieves this using less than 2\% of the parameters (0.22B vs. 11.9B) while delivering a $>15\times$ acceleration in total inference time, setting a new efficiency standard for high-fidelity inpainting. Project page at[this https URL](https://hustvl.github.io/Moebius).

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
