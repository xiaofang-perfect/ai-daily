---
title: "Prefix Sliding for efficient test-time scaling"
source: ArXiv cs.AI
url: https://arxiv.org/abs/2608.26070v1
date: 2026-08-27
published_at: 2026-08-26T17:37:15+00:00
tag: 论文研究
item_id: f8956eaf1ae41ac4
---
# Computer Science > Computation and Language

  [Submitted on 26 Aug 2026]

    # Title:Prefix Sliding for efficient test-time scaling

[View PDF](https://arxiv.org/pdf/2608.26070v1)

[HTML (experimental)](https://arxiv.org/html/2608.26070v1)

            Abstract:Test-time scaling uses extra test-time compute to improve performance, such as letting language models reason longer when solving a problem. As models keep the entire reasoning trace in memory via full attention, hard tasks that need long thinking can be prohibitively expensive. However, we find most intermediate reasoning tokens lose importance as the model continues reasoning. This calls into question whether retaining them is worth the cost. Based on this insight, we propose Prefix Sliding, which discards tokens during reasoning that are not part of the prefix or the window of the last few thousand tokens. The prefix has key instructions and tools available to the model, while the most recent tokens are the current reasoning the model is working on. This caps the total memory requirement regardless of how long the model reasons, allowing for efficient long-horizon test-time scaling. Without training, Prefix Sliding can make existing models 3x faster while maintaining performance. Training with Prefix Sliding using reinforcement learning can achieve better performance by enabling scaling to reasoning traces beyond a hundred thousand tokens. Ablations show Prefix Sliding outperforms summarizing intermediate tokens or vanilla sliding window. Our code is at [this https URL](https://github.com/Muennighoff/prefix-sliding)
    

## Submission history

From: Niklas Muennighoff [
[view email](https://arxiv.org/show-email/32be7f34/2608.26070)]

**[v1]**Wed, 26 Aug 2026 17:37:15 UTC (1,666 KB)

### Current browse context:

cs.CL

  
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
