---
title: "LaDiR: Latent Diffusion Enhances LLMs for Text Reasoning"
source: TLDR AI · 2026-04-30
url: https://machinelearning.apple.com/research/ladir?utm_source=tldrai
date: 2026-05-01
published_at: 2026-04-30T12:00:00+00:00
tag: 论文研究
item_id: bfbfb6befbbda71c
---
[content type paper](https://machinelearning.apple.com/research/)published April 2026

LaDiR: Latent Diffusion Enhances LLMs for Text Reasoning

AuthorsHaoqiang Kang†, Yizhe Zhang, Nikki Lijing Kuang†, Nicklas Majamaki†, Navdeep Jaitly, Yi-An Ma†, Lianhui Qin†

LaDiR: Latent Diffusion Enhances LLMs for Text Reasoning

AuthorsHaoqiang Kang†, Yizhe Zhang, Nikki Lijing Kuang†, Nicklas Majamaki†, Navdeep Jaitly, Yi-An Ma†, Lianhui Qin†

Large Language Models (LLMs) demonstrate their reasoning ability through chain-of-thought (CoT) generation. However, LLM’s autoregressive decoding may limit the ability to revisit and refine earlier tokens in a holistic manner, which can also lead to inefficient exploration for diverse solutions. In this paper, we propose LaDiR (Latent Diffusion Reasoner), a novel reasoning framework that unifies the expressiveness of continuous latent representation with the iterative refinement capabilities of latent diffusion models for an existing LLM. We first construct a structured latent reasoning space using a Variational Autoencoder (VAE) that encodes text reasoning steps into blocks of thought tokens, preserving semantic information and interpretability while offering compact but expressive representations. Subsequently, we utilize a latent diffusion model that learns to denoise a block of latent thought tokens with a blockwise bidirectional attention mask, enabling longer horizon and iterative refinement with adaptive test-time compute. This design allows efficient parallel generation of diverse reasoning trajectories, allowing the model to plan and revise the reasoning process holistically. We conduct evaluations on a suite of mathematical reasoning and planning benchmarks. Empirical results show that LaDiR consistently improves accuracy, diversity, and interpretability over existing autoregressive, diffusion-based, and latent reasoning methods, revealing a new paradigm for text reasoning with latent diffusion.

- † University of California, San Diego

Thinking into the Future: Latent Lookahead Training for Transformers

March 25, 2026[research area Methods and Algorithms](https://machinelearning.apple.com/research/?domain=Methods%20and%20Algorithms)[Workshop at ICLR](https://machinelearning.apple.com/research/?event=ICLR%20Workshop)

This paper was accepted at the Workshop on Latent & Implicit Thinking – Going Beyond CoT Reasoning 2026 at ICLR.

Autoregressive language models trained with next-token prediction generate text by sampling one discrete token at a time. Although very scalable, this objective forces the model to commit at every step, preventing it from exploring or reflecting upon multiple plausible continuations. Furthermore, the compute allocation across tokens…

Enhancing Paragraph Generation with a Latent Language Diffusion Model

March 15, 2024[research area Methods and Algorithms](https://machinelearning.apple.com/highlights?domain=Methods%20and%20Algorithms)

In the fast-evolving world of natural language processing (NLP), there is a strong demand for generating coherent and controlled text, as referenced in the work [Toward Controlled Generation of Text.](https://arxiv.org/abs/1703.00955) Traditional autoregressive models such as GPT, which have long been the industry standard, possess inherent limitations that sometimes manifest as repetitive and low-quality outputs, as seen in the work [The Curious Case of Neural Text Degeneration.](https://arxiv.org/abs/1904.09751) This is primarily due to a phenomenon known as “exposure bias,” as seen in the work [Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks.](https://arxiv.org/abs/1506.03099) This imperfection arises due to a mismatch between how these models are trained and their actual use during inference, often leading to error accumulation during text generation.
