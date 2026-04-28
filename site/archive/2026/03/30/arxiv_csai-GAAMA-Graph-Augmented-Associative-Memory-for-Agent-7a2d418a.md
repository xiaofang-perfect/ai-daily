---
title: "GAAMA: Graph Augmented Associative Memory for Agents"
source: ArXiv cs.AI
url: https://arxiv.org/abs/2603.27910v1
date: 2026-03-30
published_at: 2026-03-29T23:33:38+00:00
tag: 论文研究
item_id: 7a2d418a96df068e
---
# Computer Science > Artificial Intelligence

[Submitted on 29 Mar 2026]

# Title:GAAMA: Graph Augmented Associative Memory for Agents

[View PDF](https://arxiv.org/pdf/2603.27910v1)

[HTML (experimental)](https://arxiv.org/html/2603.27910v1)

Abstract:AI agents that interact with users across multiple sessions require persistent long-term memory to maintain coherent, personalized behavior. Current approaches either rely on flat retrieval-augmented generation (RAG), which loses structural relationships between memories, or use memory compression and vector retrieval that cannot capture the associative structure of multi-session conversations. There are few graph based techniques proposed in the literature, however they still suffer from hub dominated retrieval and poor hierarchical reasoning over evolving memory. We propose GAAMA, a graph-augmented associative memory system that constructs a concept-mediated hierarchical knowledge graph through a three-step pipeline: (1)~verbatim episode preservation from raw conversations, (2)~LLM-based extraction of atomic facts and topic-level concept nodes, and (3)~synthesis of higher-order reflections. The resulting graph uses four node types (episode, fact, reflection, concept) connected by five structural edge types, with concept nodes providing cross-cutting traversal paths that complement semantic similarity. Retrieval combines cosine-similarity-based $k$-nearest neighbor search with edge-type-aware Personalized PageRank (PPR) through an additive scoring function. On the LoCoMo-10 benchmark (1,540 questions across 10 multi-session conversations), GAAMA achieves 78.9\% mean reward, outperforming a tuned RAG baseline (75.0\%), HippoRAG (69.9\%), A-Mem (47.2\%), and Nemori (52.1\%). Ablation analysis shows that augmenting graph-traversal-based ranking (Personalized PageRank) with semantic search consistently improves over pure semantic search on graph nodes (+1.0 percentage point overall).

### Current browse context:

cs.AI

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
