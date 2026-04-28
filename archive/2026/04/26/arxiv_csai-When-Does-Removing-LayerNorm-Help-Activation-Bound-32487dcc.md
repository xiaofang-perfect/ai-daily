---
title: "When Does Removing LayerNorm Help? Activation Bounding as a Regime-Dependent Implicit Regularizer"
source: ArXiv cs.AI
url: https://arxiv.org/abs/2604.23434v1
date: 2026-04-26
published_at: 2026-04-25T20:12:21+00:00
tag: 论文研究
item_id: 32487dcc6032b6c0
---
# Computer Science > Machine Learning

[Submitted on 25 Apr 2026]

# Title:When Does Removing LayerNorm Help? Activation Bounding as a Regime-Dependent Implicit Regularizer

[View PDF](https://arxiv.org/pdf/2604.23434v1)

[HTML (experimental)](https://arxiv.org/html/2604.23434v1)

Abstract:Dynamic Tanh (DyT) removes LayerNorm by bounding activations with a learned tanh(alpha x). We show that this bounding is a regime-dependent implicit regularizer, not a uniformly beneficial replacement. Across GPT-2-family models spanning 64M to 3.78B parameters and 1M to 118M tokens, with Llama and ViT cross-checks, DyT improves validation loss by 27.3% at 64M/1M but worsens it by 18.8% at 64M/118M; the 1M benefit vanishes with capacity (+1.7% at 3.78B), while the 118M penalty reaches +27.9%. The mechanism is measurable: 49% of DyT activations saturate at 1M versus 23% at 118M, and a 500-step saturation heuristic classifies DyT's sign with 75% raw in-sample accuracy on the 12-cell GPT-2 calibration set (AUC 0.75; 64% when adding Scale 5 stress cells), correctly labels 3/3 Llama checks, but only reaches 50% raw leave-one-scale-out accuracy. Three interventions support the bounding explanation: HardTanh reproduces the regime pattern, increasing alpha at 118M monotonically reduces DyT's penalty, and vanilla+dropout(p=0.5) matches DyT's data-rich loss. We also localize Llama-DyT collapse to SwiGLU gating, where saturation separates collapse from convergence in a 3-seed component ablation (r=0.94). Scope: all experiments are compute-limited (T/P < 1.84), below Chinchilla-optimal training.

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
