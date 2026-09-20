---
title: "DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression"
source: HuggingFace Daily Papers · 2026-09-19
url: https://arxiv.org/abs/2609.19969
date: 2026-09-20
published_at: 2026-09-19T12:00:00+00:00
tag: 论文研究
item_id: 70fb42fdcc103db9
---
# Computer Science > Computation and Language

  [Submitted on 17 Sep 2026]

    # Title:DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression

[View PDF](https://arxiv.org/pdf/2609.19969)

[HTML (experimental)](https://arxiv.org/html/2609.19969v1)

            Abstract:The widespread adoption of long-horizon agents has made model workloads increasingly input-heavy. Although prior work has substantially reduced the cost of long-context computation, prefill remains computationally expensive, and large KV caches continue to strain HBM and SSD capacity and data-transfer bandwidth. Together, these compute, storage, and bandwidth demands constitute the primary bottleneck to further lowering deployment costs. To address this challenge, we introduce DeepSeek-V4.1-Flash, a multimodal Mixture-of-Experts (MoE) model with 552B backbone parameters and support for contexts of up to one million tokens. With its Causal Encoder-Decoder (CED) architecture, the model activates 16B parameters per token during decode but only 8B parameters during prefill, substantially improving cost efficiency for agentic workloads. To push the limits of KV cache compression, DeepSeek-V4.1-Flash combines cross-layer KV cache reuse in Compressed Sparse Attention 2 (CSA2) with FP4 KV caching. These designs reduce its global KV cache footprint (always in HBM) to 890 bytes per token, roughly 1/4 of the corresponding footprint of DeepSeek-V4-Flash. Further, through a dedicated deployment optimization known as SWA Bounded Replay, DeepSeek-V4.1-Flash reduces its persistent KV cache footprint (always on SSD or in host memory) to roughly 1/8 of that of DeepSeek-V4-Flash. Despite its much smaller KV cache footprint, the model delivers substantially better performance than the baseline. In addition, we streamline the DeepSeek-V4 architecture and introduce several efficient architectural extensions. We pretrain DeepSeek-V4.1-Flash on a multimodal corpus comprising 45T tokens and conduct comprehensive post-training, yielding strong performance across diverse text-based and multimodal agentic scenarios. Model checkpoints are available at [this https URL](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash).
    

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
