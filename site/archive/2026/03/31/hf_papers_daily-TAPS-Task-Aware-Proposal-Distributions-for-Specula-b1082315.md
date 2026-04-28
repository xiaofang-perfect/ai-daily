---
title: "TAPS: Task Aware Proposal Distributions for Speculative Sampling"
source: HuggingFace Daily Papers · 2026-03-31
url: https://arxiv.org/abs/2603.27027
date: 2026-03-31
published_at: 2026-03-31T12:00:00+00:00
tag: 论文研究
item_id: b108231515ddcf2f
---
# Computer Science > Computation and Language

[Submitted on 27 Mar 2026]

# Title:TAPS: Task Aware Proposal Distributions for Speculative Sampling

[View PDF](https://arxiv.org/pdf/2603.27027)

Abstract:Speculative decoding accelerates autoregressive generation by letting a lightweight draft model propose future tokens that a larger target model then verifies in parallel. In practice, however, draft models are usually trained on broad generic corpora, which leaves it unclear how much speculative decoding quality depends on the draft training distribution. We study this question with lightweight HASS and EAGLE-2 drafters trained on MathInstruct, ShareGPT, and mixed-data variants, evaluated on MT-Bench, GSM8K, MATH-500, and SVAMP. Measured by acceptance length, task-specific training yields clear specialization: MathInstruct-trained drafts are strongest on reasoning benchmarks, while ShareGPT-trained drafts are strongest on MT-Bench. Mixed-data training improves robustness, but larger mixtures do not dominate across decoding temperatures. We also study how to combine specialized drafters at inference time. Naive checkpoint averaging performs poorly, whereas confidence-based routing improves over single-domain drafts and merged-tree verification yields the highest acceptance length overall for both backbones. Finally, confidence is a more useful routing signal than entropy: rejected tokens tend to have higher entropy, but confidence produces much clearer benchmark-level routing decisions. These results show that speculative decoding quality depends not only on draft architecture, but also on the match between draft training data and downstream workload, and that specialized drafters are better combined at inference time than in weight space.

### References & Citations

export BibTeX citation
Loading...

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
Papers with Code

*(*[What is Papers with Code?](https://paperswithcode.com/))
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
