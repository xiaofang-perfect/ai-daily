---
title: "Modular Post-Training"
source: TLDR AI · 2026-04-21
url: https://allenai.org/blog/bar?utm_source=tldrai
date: 2026-04-22
published_at: 2026-04-21T12:00:00+00:00
tag: 论文研究
item_id: ce3146556248332d
---
# Train separately, merge together: Modular post-training with mixture-of-experts

April 20, 2026

Jacob Morrison, Sanjay Adhikesaven, Akshita Bhagia, Matei Zaharia, Noah A. Smith, and Sewon Min - Ai2

After pretraining, language models go through a series of mid- and post-training stages to become practically useful—learning to follow instructions, reason through problems, reliably call tools, and so on. But updating or extending a model following these stages is often challenging. The most reliable option, retraining from scratch with new capabilities included from the start, is expensive and requires full access to the original training setup. Training further on new data is cheaper, but it can cause the model to lose capabilities it already had. And because post-training typically involves multiple stages – each with its own data and objectives – adding new skills means rerunning or adjusting each stage to accommodate them without breaking what came before.

We present **BAR **(Branch-Adapt-Route), a recipe for modular post-training that sidesteps these issues. Rather than training a single model on all data at once, BAR trains independent domain experts – each through its own complete training pipeline – and composes them into a unified model via a mixture-of-experts (MoE) architecture. Each expert can be developed, upgraded, or replaced without touching the others.

We're releasing [the recipe](https://github.com/allenai/FlexOlmo/blob/jacobm-flex-post-train/scripts/BAR/bar_scripts.md), [a technical report](http://allenai.org/papers/bar), and [the checkpoints](https://huggingface.co/collections/allenai/branch-adapt-route) used to validate the approach.

**Background and motivation**

Our earlier work on [FlexOlmo](https://arxiv.org/abs/2502.13613) showed that modular MoE-based training works well for pretraining: you can branch from a shared base, train domain-specific feed-forward network (FFN) experts while freezing all shared layers, and merge them back. But we found that this recipe doesn’t transfer to post-training. The reason is intuitive in hindsight—pretraining primarily updates knowledge representations, which live largely in FFN layers. Post-training, on the other hand, introduces behavioral shifts such as new output formats, reasoning patterns, and safety constraints that require changes to shared parameters like attention layers, embeddings, and the language modeling head.

For example, when we tried the FlexOlmo approach directly during reinforcement learning with verified rewards (RLVR), the reward curve was completely flat; the model simply could not learn with all shared parameters frozen. This motivated us to develop a new recipe specifically for post-training.

**How BAR works**

BAR has three stages:

**Stage 1: Independent expert training.** Each domain expert is instantiated as a two-expert MoE: one frozen "anchor" expert that preserves the base model's FFN weights, and one trainable expert. Experts go through whichever training stages their domain requires. In our experiments, math and code go through mid-training, supervised fine-tuning (SFT), and RLVR; tool use and safety use SFT only.

The key technical contribution is a **progressive unfreezing schedule** for shared parameters across stages:

**Mid-training**: All shared layers frozen (same as pretraining, since knowledge acquisition is well-captured by FFN updates alone).**SFT**: Embedding layer and language modeling head unfrozen. This is necessary for domains that introduce new special tokens (e.g., function-calling formats for tool use). Without this, on the Berkeley Function Calling Leaderboard (BFCL) – the tool use benchmark we used for tool-calling performance evaluation – our tool use expert scored 20.3. With unfreezing, it reached 46.4.**RLVR**: All shared parameters unfrozen, including attention. RL induces distributional shifts that extend beyond what expert FFNs can accommodate.

Each expert also trains on a **mixture of domain-specific and general SFT data**. We found this is critical: domain-only SFT produces strong in-domain performance but severely degrades general capabilities like instruction following and knowledge.

**Stage 2: Expert merging.** After training, we merge all experts into a single MoE model. Shared parameters that diverged across expert runs (because they were unfrozen during SFT or RLVR) are simply averaged. We find this averaging introduces little to no measurable performance loss on domain-specific evaluations compared to any individual expert.

**Stage 3: Router training.** Finally, we train the router inside of the MoE with all other experts and shared weights frozen. We found that a stratified 5% sample of the SFT data is sufficient for effective routing, making this stage fast and cheap.

**Strong performance across evals**

Our models are all at least at the 7B scale, training experts for math, code, tool use, and safety on top of a fully post-trained Olmo 2 base model. (We use Olmo 2 because our FlexOlmo architecture was built around it, and because it provides a useful testbed for exploring how newer datasets and post-training improvements can strengthen a model beyond its original release configuration.) We compare against six baselines across 19 benchmarks, spanning 7 evaluation categories. All scores reported below are category-level averages (out of 100, the higher the better). For per-benchmark breakdowns, please refer to our technical report.

A few things stand out:

**On average, BAR outperforms all baselines that don't require rerunning mid-training from scratch.** BAR beats retraining with post-training only overall (49.1 vs. 47.8), with particularly large gains in math (+7.8) and code (+4.7). We attribute this to a structural advantage of modular training: in a monolithic pipeline, late-stage RL on math and code can degrade safety capabilities learned during earlier SFT stages. Modular training avoids this entirely because each domain's pipeline is isolated.

**Dense model merging after mid-training fails catastrophically**. Mid-training causes models to diverge enough that naive weight averaging produces a nearly non-functional model—one that scores 6.5 overall on our benchmarks. Even without mid-training, merging trails BAR by a wide margin (36.9 vs 49.1 overall).

**BTX, a technique that trains each expert as a fully independent dense model, underperforms BAR** (46.7 vs. 49.1 overall) despite using the same per-domain data and training stages. Training without shared parameters leads to greater divergence, making composition via routing more difficult.

**Full retraining with mid-training remains the performance ceiling** (50.5), but requires full access to the original pretraining checkpoint and reprocessing everything from scratch— impractical for most open-weight models, and expensive even with full access.

**Modular upgrades**

One of the most tangibly useful properties of BAR is that experts can be upgraded independently. We demonstrate two types of upgrades:

**Upgrading to newer data**: Replacing a code expert with one trained on higher-quality data and RL improves code performance by +16.5 points in the combined model, while all other domains remain essentially unchanged.**Adding a training stage**: Taking an existing math expert and adding RL on top of its SFT improves math by +13 points in the combined model, again with minimal impact on other domains.

In both cases, only the affected expert and the lightweight router need retraining. In a monolithic pipeline, either of these upgrades would require retraining the full model across all domains. This gives BAR linear cost scaling for domain updates, compared to the effectively quadratic cost of monolithic retraining (each domain update requires reprocessing all domains).

**What we learned**

A few practical takeaways:

**Post-training needs more flexibility than pretraining.**The FlexOlmo recipe of freezing all shared layers works for pretraining but breaks during post-training. Progressive unfreezing is essential, especially unfreezing attention during RL and embeddings/LM head for domains with new tokens.**Domain-only SFT isn’t enough.**Training an expert on only its own domain data improves in-domain performance but destroys general capabilities. Mixing with general SFT data is critical.**Weight averaging after unfreezing works surprisingly well.**Despite each expert independently modifying shared parameters during SFT and RLVR, simply averaging the diverged parameters introduces little to no measurable degradation.**Not every expert needs to be active.**Activating 4 of 5 experts at inference time achieves nearly identical performance to using all 5, suggesting room for more efficient routing strategies.

**Looking ahead**

In practice, large-scale model development is already modular: different teams work on different capabilities, new datasets appear on different timelines, and the cost of rerunning an entire pipeline for a single domain improvement is hard to justify. BAR offers a recipe that aligns the training process with this reality.

Full retraining still sets the performance ceiling. But for teams iterating on individual capabilities, BAR provides a way to upgrade parts of a model independently, compose independently trained experts without degradation, and avoid the catastrophic forgetting that comes from running all domains through a single training sequence. One natural next step is starting from a natively sparse architecture rather than upcycling a dense model, which could improve both the efficiency and scalability of the modular approach.
