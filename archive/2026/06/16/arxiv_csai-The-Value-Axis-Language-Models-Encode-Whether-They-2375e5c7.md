---
title: "The Value Axis: Language Models Encode Whether They're on the Right Track"
source: ArXiv cs.AI
url: https://arxiv.org/abs/2606.17056v1
date: 2026-06-16
published_at: 2026-06-15T17:59:58+00:00
tag: 论文研究
item_id: 2375e5c744128bc3
---
# Computer Science > Computation and Language

  [Submitted on 15 Jun 2026]

    # Title:The Value Axis: Language Models Encode Whether They're on the Right Track

[View PDF](https://arxiv.org/pdf/2606.17056v1)

[HTML (experimental)](https://arxiv.org/html/2606.17056v1)

Abstract:We investigate whether language models internally track the value of their current trajectory, defined as the likelihood that their ongoing strategy will achieve their goals. Using synthetic, in-context reinforcement learning data, we construct a "value" axis for Qwen3-8B. We find that activations along this axis distinguish between high vs. low verbalized confidence, rollouts without and with backtracking, and correct vs. corrupted code. Steering towards high value causally suppresses self-correction and reduces explanatory verbosity, while steering towards low value induces backtracking and exploration. We demonstrate that direct preference optimization (DPO) can increase the internal value of rewarded behaviors (e.g. use a certain word), causing the model to act more confidently after exhibiting them. Finally, we apply the value axis to study in-the-wild settings. For example, we find that Qwen assigns low value to politically sensitive chat queries after post-training and that supervised fine-tuning increases internal confidence within the training domain. Our results suggest that language models linearly encode an estimate of expected goal success that modulates their confidence in pursuing a direction.

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
