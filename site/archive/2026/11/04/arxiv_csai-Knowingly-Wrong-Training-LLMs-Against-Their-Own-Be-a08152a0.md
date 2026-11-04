---
title: "Knowingly Wrong: Training LLMs Against Their Own Beliefs can Induce Misalignment"
source: ArXiv cs.AI
url: https://arxiv.org/abs/2611.05287v1
date: 2026-11-04
published_at: 2026-11-03T18:02:21+00:00
tag: 论文研究
item_id: a08152a0aa8a7c97
---
# Computer Science > Computation and Language

\[Submitted on 3 Nov 2026\]

# Title:Knowingly Wrong: Training LLMs Against Their Own Beliefs can Induce Misalignment

[View PDF](https://arxiv.org/pdf/2611.05287v1)

[HTML (experimental)](https://arxiv.org/html/2611.05287v1)

Abstract:Fine-tuning a large language model (LLM) on harmful data in a narrow domain, such as bad medical advice, can make it broadly misaligned. How realistic this risk is remains unclear, since models are very rarely fine-tuned on explicitly harmful data in practice. In this work, we show that fine-tuning on data the model believes to be false but that has no harmful content, can also induce broad misalignment. Across mathematics, trivia, cooking and sports, the more strongly the model disbelieves the answers it is trained on, the more misaligned it becomes. In mathematics, misaligned answers rise from 4% to over 60% as the training answers become more wrong, with little loss of general capability. After fine-tuning, the model states the wrong answers but its multiple-choice probabilities still prefer the true ones, which suggests that misalignment comes from this internal inconsistency. We then study a more realistic setting, where a single fact is updated, as in knowledge editing or continual learning. The same relationship holds and the more the model still believes the true fact after training on the false one, the more misaligned it becomes. When we frame the same false fact as part of a coherent story, the model comes to believe it more deeply and becomes less misaligned than when we instruct it to assert the false fact. Content filters and persona vectors cannot tell these two framings apart, even though they lead to different levels of misalignment. These results suggest a risk for model updates, where training a model that does not adopt the new fact as true can induce misalignment even when the data looks harmless.

## Submission history

From: Ariana Villegas Suarez \[
[view email](https://arxiv.org/show-email/fc3f4a0c/2611.05287)\]

**\[v1\]**Tue, 3 Nov 2026 18:02:21 UTC (452 KB)

[Full-text links:]

## Access Paper:

[view license](http://creativecommons.org/licenses/by/4.0/)

![license icon](https://arxiv.org/icons/licenses/by-4.0.png) 

### Additional Features

### Current browse context:

cs.CL

### References & Citations

Loading...

### Bookmark

![BibSonomy](https://arxiv.org/static/browse/0.3.4/images/icons/social/bibsonomy.png) 

![Reddit](https://arxiv.org/static/browse/0.3.4/images/icons/social/reddit.png) 

# Bibliographic and Citation Tools

Bibliographic Explorer *([What is the Explorer?](https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer))*

Connected Papers *([What is Connected Papers?](https://www.connectedpapers.com/about))*

Litmaps *([What is Litmaps?](https://www.litmaps.co/))*

scite Smart Citations *([What are Smart Citations?](https://www.scite.ai/))*

# Code, Data and Media Associated with this Article

alphaXiv *([What is alphaXiv?](https://alphaxiv.org/))*

CatalyzeX Code Finder for Papers *([What is CatalyzeX?](https://www.catalyzex.com))*

DagsHub *([What is DagsHub?](https://dagshub.com/))*

Gotit.pub *([What is GotitPub?](http://gotit.pub/faq))*

Hugging Face *([What is Huggingface?](https://huggingface.co/huggingface))*

ScienceCast *([What is ScienceCast?](https://sciencecast.org/welcome))*

# Demos

# Recommenders and Search Tools

Influence Flower *([What are Influence Flowers?](https://influencemap.cmlab.dev/))*

CORE Recommender *([What is CORE?](https://core.ac.uk/services/recommender))*

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? [**Learn more about arXivLabs**](https://info.arxiv.org/labs/index.html).
