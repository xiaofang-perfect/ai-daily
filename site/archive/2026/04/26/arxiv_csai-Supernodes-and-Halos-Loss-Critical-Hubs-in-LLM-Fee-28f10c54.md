---
title: "Supernodes and Halos: Loss-Critical Hubs in LLM Feed-Forward Layers"
source: ArXiv cs.AI
url: https://arxiv.org/abs/2604.23475v1
date: 2026-04-26
published_at: 2026-04-26T00:00:41+00:00
tag: 论文研究
item_id: 28f10c5482f71229
---
# Computer Science > Machine Learning

[Submitted on 26 Apr 2026]

# Title:Supernodes and Halos: Loss-Critical Hubs in LLM Feed-Forward Layers

[View PDF](https://arxiv.org/pdf/2604.23475v1)

[HTML (experimental)](https://arxiv.org/html/2604.23475v1)

Abstract:We study the organization of channel-level importance in transformer feed-forward networks (FFNs). Using a Fisher-style loss proxy (LP) based on activation-gradient second moments, we show that loss sensitivity is concentrated in a small set of channels within each layer. In Llama-3.1-8B, the top 1% of channels per layer accounts for a median of 58.7% of LP mass, with a range of 33.0% to 86.1%. We call these loss-critical channels supernodes. Although FFN layers also contain strong activation outliers, LP-defined supernodes overlap only weakly with activation-defined outliers and are not explained by activation power or weight norms alone. Around this core, we find a weaker but consistent halo structure: some non-supernode channels share the supernodes' write support and show stronger redundancy with the protected core. We use one-shot structured FFN pruning as a diagnostic test of this organization. At 50% FFN sparsity, baselines that prune many supernodes degrade sharply, whereas our SCAR variants explicitly protect the supernode core; the strongest variant, SCAR-Prot, reaches perplexity 54.8 compared with 989.2 for Wanda-channel. The LP-concentration pattern appears across Mistral-7B, Llama-2-7B, and Qwen2-7B, remains visible in targeted Llama-3.1-70B experiments, and increases during OLMo-2-7B pretraining. These results suggest that LLM FFNs develop a small learned core of loss-critical channels, and that preserving this core is important for reliable structured pruning.

### References & Citations

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
ScienceCast

*(*[What is ScienceCast?](https://sciencecast.org/welcome))# Demos

# Recommenders and Search Tools

Influence Flower

*(*[What are Influence Flowers?](https://influencemap.cmlab.dev/))
CORE Recommender

*(*[What is CORE?](https://core.ac.uk/services/recommender))
IArxiv Recommender

*(*[What is IArxiv?](https://iarxiv.org/about))# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? [ Learn more about arXivLabs](https://info.arxiv.org/labs/index.html).
