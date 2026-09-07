---
title: "Terminal-Universe: Turning Agent Trajectories into Scalable Terminal Environments"
source: HuggingFace Daily Papers · 2026-09-06
url: https://arxiv.org/abs/2609.04148
date: 2026-09-07
published_at: 2026-09-06T12:00:00+00:00
tag: 论文研究
item_id: 78618fc57091d85f
---
# Computer Science > Artificial Intelligence

  [Submitted on 3 Sep 2026]

    # Title:Terminal-Universe: Turning Agent Trajectories into Scalable Terminal Environments

[View PDF](https://arxiv.org/pdf/2609.04148)

[HTML (experimental)](https://arxiv.org/html/2609.04148v1)

            Abstract:As terminal-based code agents become prevalent, agent trajectories have accumulated at scale, while realistic, executable environments remain scarce. However, environments are what agent post-training actually requires: each can be re-queried into many verifiable tasks and provides execution feedback, whereas a trajectory is a single frozen demonstration. Rather than generating environments from scratch, we observe that the tool-execution history in existing trajectories exposes the structure and contents of the environments in which they ran, making it possible to reconstruct those environments from the trajectories themselves. Thus, we introduce Terminal-Universe, a framework which turns each trajectory into a reusable environment and explores it for synthesizing new tasks and continued interactions. Specifically, Terminal-Universe replays the file operations recorded in a trajectory to restore each file before the agent modified it, yielding a partial workspace; a completion agent then supplies the missing files and dependencies. On this recovered workspace, we both reconstruct the original intent task and synthesize entirely new ones. Besides, we also scale the tasks along two complementary axes: breadth and depth. For breadth, we mine directional dependency relations between related environments and synthesize cross-workspace queries spanning multiple codebases, as developers routinely do in real-world development. For depth, we extend the initial single-turn query into a multi-round session that captures iterative user feedback and requirement refinement via a user agent. Applied to public terminal agent trajectories, Terminal-Universe produces 37.3k task-sufficient environments. Supervised fine-tuning of Qwen3.5-27B on this corpus improves single-round performance on Terminal-Bench 2.1 by 11.9 points and multi-round performance on EvoCode-Bench v2 MT@4 by 13.8 points.
    

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
