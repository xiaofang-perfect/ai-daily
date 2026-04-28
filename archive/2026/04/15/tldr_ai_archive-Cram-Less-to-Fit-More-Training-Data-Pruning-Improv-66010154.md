---
title: "Cram Less to Fit More: Training Data Pruning Improves Memorization of Facts"
source: TLDR AI · 2026-04-14
url: https://machinelearning.apple.com/research/cram-less?utm_source=tldrai
date: 2026-04-15
published_at: 2026-04-14T12:00:00+00:00
tag: 论文研究
item_id: 660101541eb00ca9
---
[content type paper](https://machinelearning.apple.com/research/)published April 2026

Cram Less to Fit More: Training Data Pruning Improves Memorization of Facts

AuthorsJiayuan Ye, Vitaly Feldman, Kunal Talwar

Cram Less to Fit More: Training Data Pruning Improves Memorization of Facts

AuthorsJiayuan Ye, Vitaly Feldman, Kunal Talwar

This paper was accepted at the Workshop on Navigating and Addressing Data Problems for Foundation Models at ICLR 2026.

Large language models (LLMs) can struggle to memorize factual knowledge in their parameters, often leading to hallucinations and poor performance on knowledge-intensive tasks. In this paper, we formalize fact memorization from an information-theoretic perspective and study how training data distributions affect fact accuracy. We show that fact accuracy is suboptimal (below the capacity limit) whenever the amount of information contained in the training data facts exceeds model capacity. This is further exacerbated when the fact frequency distribution is skewed (e.g. a power law). We propose data selection schemes based on the training loss alone that aim to limit the number of facts in the training data and flatten their frequency distribution. On semi-synthetic datasets containing high-entropy facts, our selection method effectively boosts fact accuracy to the capacity limit. When pretraining language models from scratch on an annotated Wikipedia corpus, our selection method enables a GPT2-Small model (110m parameters) to memorize 1.3X more entity facts compared to standard training, matching the performance of a 10X larger model (1.3B parameters) pretrained on the full dataset.

Trade-offs in Data Memorization via Strong Data Processing Inequalities

June 27, 2025[research area Methods and Algorithms](https://machinelearning.apple.com/research/?domain=Methods%20and%20Algorithms), [research area Privacy](https://machinelearning.apple.com/research/?domain=Privacy)[conference COLT](https://machinelearning.apple.com/research/?event=COLT)

Recent research demonstrated that training large language models involves memorization of a significant fraction of training data. Such memorization can lead to privacy violations when training on sensitive user data and thus motivates the study of data memorization’s role in learning. In this work, we develop a general approach for proving lower bounds on excess data memorization, that relies on a new connection between strong data processing…

Improving Human Annotation Effectiveness for Fact Collection by Identifying the Most Relevant Answers

February 13, 2023[research area Data Science and Annotation](https://machinelearning.apple.com/research/?domain=Data%20Science%20and%20Annotation), [research area Knowledge Bases and Search](https://machinelearning.apple.com/research/?domain=Knowledge%20Bases%20and%20Search)[conference EMNLP](https://machinelearning.apple.com/research/?event=EMNLP)

This paper was accepted at the Workshops on Data Science with Human in the Loop at EMNLP 2022

Identifying and integrating missing facts is a crucial task for knowledge graph completion to ensure robustness towards downstream applications such as question answering. Adding new facts to a knowledge graph in real world system often involves human verification effort, where candidate facts are verified for accuracy by human annotators. This process…
