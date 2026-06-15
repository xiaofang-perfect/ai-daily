---
title: "MiniMax Sparse Attention"
source: HuggingFace Daily Papers · 2026-06-14
url: https://arxiv.org/abs/2606.13392
date: 2026-06-15
published_at: 2026-06-14T12:00:00+00:00
tag: 论文研究
item_id: b88efc1144b223f4
---
# Computer Science > Artificial Intelligence

  [Submitted on 11 Jun 2026 (

    [v1](https://arxiv.org/abs/2606.13392v1)), last revised 12 Jun 2026 (this version, v2)]# Title:MiniMax Sparse Attention

[View PDF](https://arxiv.org/pdf/2606.13392)

[HTML (experimental)](https://arxiv.org/html/2606.13392v2)

Abstract:Ultra-long-context capability is becoming indispensable for frontier LLMs: agentic workflows, repository-scale code reasoning, and persistent memory all require the model to jointly attend over hundreds of thousands to millions of tokens, yet the quadratic cost of softmax attention makes this untenable at deployment scale. We introduce MiniMax Sparse Attention (MSA), a blockwise sparse attention built upon Grouped Query Attention (GQA). A lightweight Index Branch scores key-value blocks and independently selects a Top-k subset for each GQA group, enabling group-specific sparse retrieval while maintaining efficient block-level execution; the Main Branch then performs exact block-sparse attention over only the selected blocks. Designed around a principle of simplicity and scalability, MSA is deliberately streamlined, making it straightforward to deploy efficiently across a broad range of GPUs. To translate sparsity into practical speedups, we co-design MSA with a GPU execution path that uses exp-free Top-k selection and KV-outer sparse attention to improve tensor-core utilization under block-granular access. On a 109B-parameter model with native multimodal training, MSA performs on par with GQA while reducing per-token attention compute by 28.4x at 1M context. Paired with our co-designed kernel, MSA achieves 14.2x prefill and 7.6x decoding wall-clock speedups on H800. Our inference kernel is available at:[this https URL](https://github.com/MiniMax-AI/MSA). A production-grade natively multimodal model powered by MSA has been publicly released at:[this https URL](https://huggingface.co/MiniMaxAI/MiniMax-M3).

## Submission history

From: Xunhao Lai [[view email](https://arxiv.org/show-email/9711fda3/2606.13392)]

**Thu, 11 Jun 2026 14:23:41 UTC (3,976 KB)**

[[v1]](https://arxiv.org/abs/2606.13392v1)**[v2]**Fri, 12 Jun 2026 09:42:25 UTC (3,976 KB)

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
