---
title: "Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction"
source: HuggingFace Daily Papers · 2026-05-10
url: https://arxiv.org/abs/2605.05242
date: 2026-05-11
published_at: 2026-05-10T12:00:00+00:00
tag: 论文研究
item_id: 5cc2b3ac3e74c691
---
# Computer Science > Information Retrieval

[Submitted on 3 May 2026]

# Title:Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction

[View PDF](https://arxiv.org/pdf/2605.05242)

Abstract:Modern retrieval systems, whether lexical or semantic, expose a corpus through a fixed similarity interface that compresses access into a single top-k retrieval step before reasoning. This abstraction is efficient, but for agentic search, it becomes a bottleneck: exact lexical constraints, sparse clue conjunctions, local context checks, and multi-step hypothesis refinement are difficult to implement by calling a conventional off-the-shelf retriever, and evidence filtered out early cannot be recovered by stronger downstream reasoning. Agentic tasks further exacerbate this limitation because they require agents to orchestrate multiple steps, including discovering intermediate entities, combining weak clues, and revising the plan after observing partial evidence. To tackle the limitation, we study direct corpus interaction (DCI), where an agent searches the raw corpus directly with general-purpose terminal tools (e.g., grep, file reads, shell commands, lightweight scripts), without any embedding model, vector index, or retrieval API. This approach requires no offline indexing and adapts naturally to evolving local corpora. Across IR benchmarks and end-to-end agentic search tasks, this simple setup substantially outperforms strong sparse, dense, and reranking baselines on several BRIGHT and BEIR datasets, and attains strong accuracy on BrowseComp-Plus and multi-hop QA without relying on any conventional semantic retriever. Our results indicate that as language agents become stronger, retrieval quality depends not only on reasoning ability but also on the resolution of the interface through which the model interacts with the corpus, with which DCI opens a broader interface-design space for agentic search.

### Additional Features

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

*(*[What is CORE?](https://core.ac.uk/services/recommender))# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? [ Learn more about arXivLabs](https://info.arxiv.org/labs/index.html).
