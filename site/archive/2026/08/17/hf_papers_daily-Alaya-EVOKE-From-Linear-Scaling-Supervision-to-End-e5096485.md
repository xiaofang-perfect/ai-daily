---
title: "Alaya-EVOKE: From Linear-Scaling Supervision to Endless World"
source: HuggingFace Daily Papers · 2026-08-16
url: https://arxiv.org/abs/2608.13546
date: 2026-08-17
published_at: 2026-08-16T12:00:00+00:00
tag: 论文研究
item_id: e50964857e56c0b1
---
# Computer Science > Computer Vision and Pattern Recognition

  [Submitted on 13 Aug 2026]

    # Title:Alaya-EVOKE: From Linear-Scaling Supervision to Endless World

[View PDF](https://arxiv.org/pdf/2608.13546)

[HTML (experimental)](https://arxiv.org/html/2608.13546v1)

            Abstract:Interactive world models must support persistent memory, responsive interaction, and long-horizon generation, yet these requirements place conflicting demands on the model. Maintaining history in the denoiser context or key-value cache incurs growing cost, forcing a trade-off between session length and retained memory, while low-latency interaction relies on few-step generation whose capabilities are bounded by its teacher. Evoke addresses both limitations by externalizing persistent world state and redesigning the teacher for long-horizon interactive generation. Scene geometry is maintained in an external, camera-indexed world state bank, from which only view-relevant information is retrieved, keeping the denoiser context bounded as the session grows. Rather than treating the teacher as a fixed generator, we design it for long-horizon supervision: its sparse attention combines chunk-wise grouping, retrieval of selected distant frames, and a linear-attention global state, yielding linear growth in memory and compute while enabling supervision over long horizons. Such supervision exposes content drift that stays locally plausible within short windows, while per-chunk conditioning enables prompt changes and event control throughout the sequence. A 30-second distribution-matching objective, applied under self-forced rollouts, transfers both capabilities to a three-step student that uses no classifier-free guidance, improving resistance to long-term drift while preserving responsive conditioning. With bounded context and recurrent external memory, Evoke supports open-ended, continuously evolving generation; on a single H200 at $384\times 640$, each $1.5\,\mathrm{s}$ chunk is generated in $2.11\,\mathrm{s}$. As a three-step world model, Evoke achieves state-of-the-art performance on WBench while remaining competitive on VBench-Long and VBench-2.0.
    

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
