---
title: "Trained on Tokens, Calibrated on Concepts: The Emergence of Semantic Calibration in LLMs"
source: TLDR AI · 2026-03-25
url: https://machinelearning.apple.com/research/trained-on-tokens?utm_source=tldrai
date: 2026-03-26
published_at: 2026-03-25T12:00:00+00:00
tag: 论文研究
item_id: 610a03283dcf0233
---
[content type paper](https://machinelearning.apple.com/research/)published March 2026

Trained on Tokens, Calibrated on Concepts: The Emergence of Semantic Calibration in LLMs

AuthorsPreetum Nakkiran, Arwen Bradley, Adam Goliński, Eugene Ndiaye, Michael Kirchhof, Sinead Williamson

Trained on Tokens, Calibrated on Concepts: The Emergence of Semantic Calibration in LLMs

AuthorsPreetum Nakkiran, Arwen Bradley, Adam Goliński, Eugene Ndiaye, Michael Kirchhof, Sinead Williamson

Large Language Models (LLMs) often lack meaningful confidence estimates for their outputs. While base LLMs are known to exhibit next-token calibration, it remains unclear whether they can assess confidence in the actual meaning of their responses beyond the token level. We find that, when using a certain sampling-based notion of semantic calibration, base LLMs are remarkably well-calibrated: they can meaningfully assess confidence in open-domain question-answering tasks, despite not being explicitly trained to do so. Our main theoretical contribution establishes a mechanism for why semantic calibration emerges as a byproduct of next-token prediction, leveraging a recent connection between calibration and local loss optimality. The theory relies on a general definition of “B-calibration,” which is a notion of calibration parameterized by a choice of equivalence classes (semantic or otherwise). This theoretical mechanism leads to a testable prediction: base LLMs will be semantically calibrated when they can easily predict their own distribution over semantic answer classes before generating a response. We state three implications of this prediction, which we validate through experiments: (1) Base LLMs are semantically calibrated across question-answering tasks, (2) RL instruction-tuning systematically breaks this calibration, and (3) chain-of-thought reasoning breaks calibration. To our knowledge, our work provides the first principled explanation of when and why semantic calibration emerges in LLMs.

A Unifying Theory of Distance from Calibration

June 13, 2023[research area Fairness](https://machinelearning.apple.com/research/?domain=Fairness), [research area Methods and Algorithms](https://machinelearning.apple.com/research/?domain=Methods%20and%20Algorithms)[conference ACM STOC](https://machinelearning.apple.com/research/?event=ACM%20STOC)

We study the fundamental question of how to define and measure the distance from calibration for probabilistic predictors. While the notion of perfect calibration is well-understood, there is no consensus on how to quantify the distance from perfect calibration. Numerous calibration measures have been proposed in the literature, but it is unclear how they compare to each other, and many popular measures such as Expected Calibration Error (ECE)…

The Calibration Generalization Gap

October 18, 2022[research area Methods and Algorithms](https://machinelearning.apple.com/research/?domain=Methods%20and%20Algorithms)[Workshop at ICML](https://machinelearning.apple.com/research/?event=ICML%20Workshop)

This paper was accepted at the Workshop on Distribution-Free Uncertainty Quantification at ICML 2022.

Calibration is a fundamental property of a good predictive model: it requires that the model predicts correctly in proportion to its confidence. Modern neural networks, however, provide no strong guarantees on their calibration— and can be either poorly calibrated or well-calibrated depending on the setting. It is currently unclear which…
