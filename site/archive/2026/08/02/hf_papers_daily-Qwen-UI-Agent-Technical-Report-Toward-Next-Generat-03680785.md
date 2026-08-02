---
title: "Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric Foundation GUI Agents"
source: HuggingFace Daily Papers · 2026-08-01
url: https://arxiv.org/abs/2607.28227
date: 2026-08-02
published_at: 2026-08-01T12:00:00+00:00
tag: 论文研究
item_id: 03680785b7dfb2c7
---
# Computer Science > Artificial Intelligence

  [Submitted on 30 Jul 2026]

    # Title:Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric Foundation GUI Agents

[View PDF](https://arxiv.org/pdf/2607.28227)

[HTML (experimental)](https://arxiv.org/html/2607.28227v1)

            Abstract:GUI agents have the potential to become a general purpose executor over existing digital devices. To advance them toward real-world use, we envision agents that operate reliably on real devices, execute workflows across platforms, combine GUI interaction with CLI execution, complete long-horizon tasks, proactively initiate useful services, and autonomously improve their capabilities with minimal human effort. Guided by this vision, we present Qwen-UI-Agent, a real-world centric foundation GUI agent spanning mobile, computer-use, web, and DeepSearch environments. Qwen-UI-Agent combines diverse sandbox environments with a large-scale real-device mobile runtime. Its unified action space interleaves GUI operations with CLI execution and generates batched actions in a single model turn. An AutoResearch-style data flywheel uses agents to construct tasks and environments, diagnose failures, and plan subsequent iterations. Online RL supports training on trajectories exceeding 100 turns, with over 10,000 concurrent environments accelerating rollout. A lightweight harness layer supports proactive service initiation and stateful workflows across mobile and computer.

Across a broad suite of evaluations, Qwen-UI-Agent sets state-of-the-art performance on mobile-use benchmarks while delivering competitive performance on computer- and browser-use tasks against frontier models, including Opus 4.8, Gemini 3.1 Pro, and GPT-5.6 Sol. On mobile use, it achieves 82.1% on MobileWorld, 92.2% on MobileWorld-Real, and 97.5% on AndroidDaily. On computer use, it achieves 79.5% on OSWorld-Verified and a 40.0% partial-progress score on OSWorld-v2. On browser use and GUI grounding, it achieves 73.6% on WebArena and 81.5% on ScreenSpot-Pro, respectively.

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
