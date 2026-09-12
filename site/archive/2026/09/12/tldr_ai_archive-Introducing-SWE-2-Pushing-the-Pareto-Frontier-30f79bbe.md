---
title: "Introducing SWE-2: Pushing the Pareto Frontier"
source: TLDR AI · 2026-09-11
url: https://cognition.com/blog/swe-2?utm_source=tldrai
date: 2026-09-12
published_at: 2026-09-11T12:00:00+00:00
tag: 产品发布
item_id: 30f79bbe08a80742
---
# Introducing SWE-2: Pushing the Pareto Frontier

Today we’re introducing SWE-2, our most advanced coding model yet. It pushes the Pareto frontier of capability and cost, achieving 50.0% on [FrontierCode 1.1 Main](https://cognition.com/blog/frontier-code-1.1)<sup>[1](https://cognition.com#ref-1)</sup>, within one point of Fable 5.1 while being 64% cheaper.

With SWE-2, we scaled RL to the multi-trillion-parameter regime for the first time, building on the [SWE-1.7](https://cognition.com/blog/swe-1-7)<sup>[2](https://cognition.com#ref-2)</sup> training infrastructure and recipe. The key addition is an RL algorithm that trains all reasoning-effort levels in a single run, advancing the whole cost–performance frontier.

The result is our closest model yet to the frontier. On FrontierCode 1.1 Main and DeepSWE 1.1, SWE-2 beats SWE-1.7 and Grok 4.6 on both score and cost, matches GPT-5.6 Sol and Fable 5/5.1 at a fraction of their price, and comes within a few points of GPT-6 Astra at a quarter of the cost.

[See how models rank on the FrontierCode leaderboard](https://cognition.com/frontiercode)

SWE-2 is post-trained from [Kimi K3](https://arxiv.org/abs/2607.24653)<sup>[3](https://cognition.com#ref-3)</sup>, a 2.8T-parameter model that had already undergone extensive RL for agentic coding. As with SWE-1.7, our RL still finds substantial headroom, adding 5–6 points on many benchmarks and shifting K3’s entire cost–performance frontier.

| Benchmark | SWE-2 | Kimi K3 | Grok 4.6 | Fable 5.1 | GPT-5.6 Sol | GPT-6 Astra | SWE-1.7 | 
|---|---|---|---|---|---|---|---|
| FrontierCode 1.1 Main | 50.0% | 44.2% | 48.0% | 50.9% | 47.5% | 53.3% | 42.0% | 
| DeepSWE 1.1 | 73.0% | 68.5% | 67.5% | 67.4% | 72.7% | 74.1% | 37.7% | 
| Terminal-Bench 2.1 | 92.8% | 88.3% | 88.4% | 91.4% | 88.8% | 89.9% | 81.5% | 
| Terminal-Bench 4 | 27.3% | 21.5% | 20.3% | 55.8% | 37.3% | 57.9% | 7.6% | 

The rest of this post covers what SWE-2 does differently and how we trained it.

We begin with SWE-2’s behavior, focusing on the characteristics that make it more efficient and intelligent compared to our previous models. Then, we detail the post-training advances behind SWE-2:

- **Cost penalties.** We apply a linear cost penalty per effort level in a single RL run, with each penalty tuned to the local slope of the base model’s Pareto frontier. This approach is derived from first principles to advance the model’s entire Pareto frontier while preserving its shape, and to reflect actual user costs in training as directly as possible.
- **Reward baselines.** We derive the length-weighted reward baseline we have used since SWE-1.6 and show how it significantly stabilizes training.
- **RL rollout serving.** We improve scheduling and train an online draft model to raise decoding throughput. With NVFP4/FP8 kernels and quantization-aware training, we reduce overall memory usage and achieve lower train–inference mismatch than SWE-1.7 at similar throughput despite using a base model with almost 3x the parameters.
- **Training data.** We triple the number of our RL environments, add instruction-following overlays, and build a flywheel powered by previous checkpoints of SWE-2 that iteratively hardens our verifiers.

SWE-2 is available starting today in Devin [Desktop](https://devin.ai/desktop) and [CLI](https://devin.ai/cli). We’re also rolling it out on [Devin Web](https://app.devin.ai/) and [Fusion](https://cognition.com/blog/devin-fusion).

## [Model Behavior](https://cognition.com#model-behavior)

SWE-2’s improvements in intelligence and efficiency are closely connected. Stronger engineering judgment allows the agent to write more complete solutions alongside fewer detours and redundant reads. On FrontierCode 1.1 Main, we see that SWE-2 medium scores higher than SWE-1.7 while taking 58% fewer turns and costing 81% less on average.

#### SWE-1.7 vs. SWE-2 on FrontierCode 1.1 Main: Mean

- Explore (read / grep / ls)
- Plan / todo
- Write / edit code
- Build (make / lint)
- Run tests
- git add / commit
- Final message

In our [previous post](https://cognition.com/blog/swe-1-7)<sup>[2](https://cognition.com#ref-2)</sup>, we observed SWE-1.7 as being exceedingly careful through its thorough exploration of the codebase before making edits. While boosting performance, this led to user feedback that SWE-1.7 tended to over-explore and overthink on simple tasks. Promisingly on this front, we find that the largest efficiency gains from SWE-2 come from **focused exploration**: higher intelligence allows the model to judge which parts of the codebase actually matter for a task. This allows SWE-2 to begin implementation sooner: on FrontierCode 1.1 Main, we observe SWE-2 medium making its first real edit after a median of 18 steps, compared with 48 for SWE-1.7.

From testing SWE-2 internally, we observed that the higher model capabilities also manifested in the following behavioral patterns:

- **Test coverage:** SWE-2 is better at writing tests that check an implementation end-to-end, catching regressions and edge cases more reliably.
- **Resourcefulness, within the user’s boundaries:** When the obvious path is blocked, SWE-2 is more willing to look for another route to the same answer. In one case an MCP integration it needed was unavailable, so it reconstructed the data from the Slack channel history it already had access to.
- **Verification discipline:** When challenged, SWE-2 re-derives conclusions rather than re-asserting. SWE-2 verifies a user’s hypotheses instead of simply agreeing, and runs artifacts to gather evidence instead of trusting surface-level prose. The result is a model whose conclusions you can trust.

We observe real behavioral differences between effort levels as well. SWE-2 medium steps into action much quicker, allowing cost-efficient performance on simple and intermediate tasks. SWE-2 high and max hold an edge over complex tasks: planning more, exploring more of the codebase, and managing uncertainties through more complex verification.

We next discuss an improvement to our post-training methodology that we believe helped bring about these behavioral features: Pareto-informed cost penalties in RL.

## [Pushing the Pareto Frontier with RL](https://cognition.com#pareto-frontier-rl)

As models become more intelligent and expensive, cost–performance tradeoffs grow increasingly important in the coding agent landscape. In training SWE-2, we therefore aimed not just to optimize the model’s intelligence but also to optimize the entire range of cost–performance tradeoffs it makes available.

Post-training recipes differ widely in how they penalize length and train multiple effort levels. For example, Kimi K3 trains a separate expert for each combination of domain and effort level and then consolidates the experts into one model through multi-teacher on-policy distillation. It also uses a problem-specific (and training step-specific) token budget.

In the face of this broad and subtle-to-understand range of possible approaches, we present an elegant and principled method to train all effort levels end-to-end during a single RL run.

#### Progress of the Pareto frontier during training

We accomplish this by using a cost-penalized reward function of the form

where  denotes whether a rollout was successful,  denotes the cost of a rollout (a mix of inference cost in USD and rollout time),  denotes the effort level, and  is a parameter **tuned to match the slope of the Pareto curve of the base model at effort level** .

#### Approximating the Pareto curve tangents of Kimi K3

These choices might seem counterintuitive, but as we will now see, they are logical conclusions derived from our goal of pushing the Pareto frontier.

## [Deriving the Cost Penalty](https://cognition.com#deriving-cost-penalty)

We next explain how we chose an RL objective  that directly optimizes the model’s cost–performance Pareto frontier. Here, “cost” refers to average cost and “performance” refers to solve rate, both averaged over a distribution  of training tasks. Recall that points on the cost–performance plane depend on the task distribution’s *average* cost and *average* solve rate but otherwise do not depend on . Therefore, to align the RL objective with a model’s position in the plane, we want the expectation of  over  to depend only on this average cost and solve rate.

As it turns out, guaranteeing this equality for every joint distribution of rollout cost and success **forces a linear cost penalty** (up to additive constants and scaling), because only a linear penalty gives the same result whether applied before or after averaging cost. For the interested reader, we prove this claim rigorously in [Appendix B](https://cognition.com#appendix-b).

Now that we have our reward function , the final task is selecting  for each effort level. While setting  might at first feel like a hyperparameter optimization problem, it turns out that our goal of pushing the Pareto frontier upwards *again* dictates how we should make this choice. Indeed, we consider the ability to clearly reason about this parameter selection an important practical advantage of our approach.

The key idea is to consider the geometry of the Pareto frontier and its iso-reward lines. To do so, fix an effort level and let be the corresponding point on the current frontier, with average reward . Its iso-reward line satisfies , and therefore has slope .

In the left panel below, we see a failure case where is set too large: the model is rewarded for performing an unhelpful update, one where the model at high-effort starts to behave like the medium-effort version. The reduction in cost outweighs the loss in solve rate, increasing reward without improving the Pareto frontier. In the right panel, matches the frontier’s slope at the current high-effort point. When the iso-reward line is tangent to the frontier, increasing reward always improves the frontier.

We can formalize this geometrical intuition with a bit of algebra. Let be the local slope of the Pareto frontier at . A small movement along the frontier changes the solve rate by , so the corresponding change in average reward is

Thus, letting ensures that the objective is unaffected (to first order) by movements along the Pareto curve.

## [Length-Weighted Reward Baseline](https://cognition.com#length-weighted-baseline)

We’re also sharing the reward baseline we’ve used since SWE-1.6: a length-weighted baseline that reduces gradient variance at no extra cost and significantly stabilizes training.

Given a fixed prompt and a group of rollouts , the on-policy gradient estimator with baseline is

A reasonable proxy for reducing the gradient estimator’s variance is to minimize . This gives the mean-reward baseline , which in practice we estimate using the [group baseline](https://openreview.net/pdf?id=r1lgTGL5DE)<sup>[4](https://cognition.com#ref-4)</sup> . Its dependence on the sampled rollouts introduces some bias in the gradient estimator, but this bias decays as  and is small for large groups.

We instead attempt to minimize the variance of the full gradient estimator . Following [Greensmith, Bartlett, and Baxter (2004)](https://jmlr.org/papers/volume5/greensmith04a/greensmith04a.pdf)<sup>[5](https://cognition.com#ref-5),[6](https://cognition.com#ref-6)</sup>, the optimal baseline is

See [Appendix C](https://cognition.com#appendix-c) for a simple derivation.

Computing an empirical estimate of this baseline would require an extra backward pass on each rollout for the term . Empirically, however, we find that this quantity is strongly correlated with the rollout length , as the next plot shows:

This suggests a much cheaper proxy to approximate at no extra cost:

In practice, we train using off-policy RL, so is technically not the baseline that minimizes the gradient variance. Still, in our ablations, we found this baseline to be significantly more stable and performant. In particular, it helps keep the inference–training KL low during RL.

#### Length-weighted group baseline improves RL stability

## [RL Rollouts & Numerics](https://cognition.com#rl-rollouts-numerics)

We build our rollout system with four goals in mind:

- maximizing total throughput
- reducing latency to limit staleness
- staying within KV-cache capacity
- keeping inference numerically close to training

Since prefill requests can arrive at different times, we built a prefill delayer to hold and batch nearby requests in the GPU scheduler. This improved both TPM per GPU and TPS per request by 10–20%. We found that the increased time to first token (TTFT) was an acceptable tradeoff.

To generate rollouts faster, we employed [DSpark speculative decoding](https://arxiv.org/abs/2607.05147)<sup>[7](https://cognition.com#ref-7)</sup>. A draft model proposes several tokens, and the policy model verifies them together. As the policy changes during training, DSpark’s accepted sequences become shorter, which reduces TPM and TPS.

#### Degradation of speculative decoding acceptance rate during RL

To improve the acceptance rate, we used [SpecForge](https://arxiv.org/abs/2603.18567)<sup>[8](https://cognition.com#ref-8)</sup> to train a new DSpark model that achieved 15% longer accept lengths. We then integrated online draft-model training into the RL system so that the draft model continued to track the policy as it changed.

Low-precision MoE inference lets us fit more rollouts in memory, but it can also make the inference policy drift from the trainer. We use NVFP4 and FP8 kernels, together with quantization-aware training. The MLA layers use FP8 for K,Q,V and the score computations. This is a simplification compared to SWE-1.7 which used mixed precision in the layers – the NoPE component used FP8, while the RoPE component remained in BF16.

Together, all these changes give SWE-2 lower inference–training KL divergence and similar compute throughput and efficiency compared to SWE-1.7.

## [Data Improvements](https://cognition.com#data-improvements)

Since SWE-1.7, we’ve scaled up our data synthesis and significantly improved the quality and diversity of our RL environments. We were also able to create a recursive flywheel that helps us generate data, ingest solutions from RL rollouts, and improve the quality of the verifiers in our data. The main improvements that we’ve incorporated include the following:

- **Scaling up:** We tripled the number of RL environments and expanded our repo distribution when sourcing data. Switching to a stronger base model also required us to generate more challenging tasks.
- **Instruction following:** Following instructions is a crucial skill for LLMs, especially in the context of alignment and model UX. We took existing data and introduced additional requirements, training the model to keep multiple instructions in context without losing sight of the underlying task.
- **Hardening our verifiers:** Since Kimi K3 is a more resourceful model, we needed to increase the robustness of our verifiers to prevent reward hacking. We looked at rollouts from the model during training to uncover and patch new instances of false positives and false negatives in our data, which we iteratively refined using previous checkpoints of SWE-2.

## [Measuring the Trustworthiness of SWE-2](https://cognition.com#appendix-trustworthiness)

In [our earlier post on model trustworthiness](https://cognition.com/blog/measuring-open-source-model-trustworthiness)<sup>[9](https://cognition.com#ref-9)</sup>, we introduced three evaluations of model alignment and trustworthiness. Here, we revisit two of those evaluations: propaganda and censorship, with an updated grading method, and context-dependent vulnerability in coding tasks. We apply both evaluations to six models: SWE-2, Kimi K3, GLM 5.3, GPT 5.6, Fable 5.1, and Opus 5.

#### [Propaganda and censorship](https://cognition.com#propaganda-and-censorship)

This evaluation updates the propaganda and censorship test from our earlier trustworthiness evaluation. As before, we use the 145 questions about politically sensitive topics in China collected by Pan and Xu (2026). We submit each question in English, Simplified Chinese, and Traditional Chinese.

In the earlier evaluation, we graded each answer on six axes: active propaganda, CCP narrative alignment, refusal, deflection, completeness, and factual accuracy. Here, we replace those axes with one binary pass or fail result from one judge, GPT 5.6 Luna. To make this judgment, the judge uses reference material from English and Chinese Wikipedia, a description of the official PRC position, and an independent account. An answer passes if it gives a substantive response without adopting the official PRC position as its own; otherwise, it fails. We report pass rates by language and overall, excluding empty responses and execution or grading errors.

SWE-2 passed 98.0% of attempts overall: 99.8% in English, 95.2% in Simplified Chinese, and 99.1% in Traditional Chinese. Full results are in the figure below.

#### Propaganda and Censorship Eval, by language

#### [Context-dependent vulnerability in coding tasks](https://cognition.com#context-dependent-vulnerability-in-coding-tasks)

We reran the unchanged context-dependent vulnerability evaluation on the new model suite to test whether customer identity or request language affects models’ willingness to implement vulnerable or abusive functionality. The coding tasks use Western, Pakistani, Chinese, Tibetan, and Falun Gong-affiliated customer framings, with some requests in Urdu or Chinese instead of English. Each condition runs with standard instructions and with an added instruction to prioritize secure implementation.

A GPT 5.6 Sol-high judge scores implementations from 1 to 5, with lower scores indicating safer behavior. To measure framing effects, we pool both instruction conditions and subtract each model’s overall mean from its mean under each framing. Positive values indicate greater vulnerability. The graph shows these differences with 95% percentile intervals. As in our earlier evaluation, no framing condition produced a statistically significant increase or decrease in vulnerability for any model.

#### Effect of customer and language framing on vulnerability

## [References](https://cognition.com#references)

1. [1]E. Lu, B. Pan, F. Ma, A. Lombardi, D. Birlikci, S. Lee, R. Wang, R. Choudhury, T. Qin, C. Baronio, J. Teo, J.H. Lee, S. Alberti, "FrontierCode 1.1," July 2026. [cognition.com/blog/frontier-code-1.1](https://cognition.com/blog/frontier-code-1.1)
2. [2]B. Pan, C. Baronio, R. Choudhury, E. Lu, R. Kim, D. Birlikci, T. Qin, S. Lee, F. Ma, A. Liu, Y. Liu, S. Panda, J. Teo, R. Wang, G. Chang, S. Cao, and S. Alberti, "SWE-1.7: Frontier Intelligence at a Fraction of the Cost," July 2026. [cognition.com/blog/swe-1-7](https://cognition.com/blog/swe-1-7)
3. [3]Kimi Team et al., "Kimi K3: Open Frontier Intelligence," arXiv:2607.24653, July 2026. [arxiv.org/abs/2607.24653](https://arxiv.org/abs/2607.24653)
4. [4]W. Kool, H. van Hoof, and M. Welling, "Buy 4 REINFORCE Samples, Get a Baseline for Free!," Deep Reinforcement Learning Meets Structured Prediction Workshop at ICLR 2019, 2019. [openreview.net/pdf?id=r1lgTGL5DE](https://openreview.net/pdf?id=r1lgTGL5DE)
5. [5]E. Greensmith, P. L. Bartlett, and J. Baxter, "Variance Reduction Techniques for Gradient Estimates in Reinforcement Learning," *Journal of Machine Learning Research* , vol. 5, pp. 1471–1530, November 2004.[jmlr.org/papers/volume5/greensmith04a/greensmith04a.pdf](https://jmlr.org/papers/volume5/greensmith04a/greensmith04a.pdf)
6. [6]Y. Hao, L. Dong, X. Wu, S. Huang, Z. Chi, and F. Wei, "On-Policy RL with Optimal Reward Baseline," arXiv:2505.23585, May 2025. [arxiv.org/abs/2505.23585](https://arxiv.org/abs/2505.23585)
7. [7]X. Cheng et al., "DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation," arXiv:2607.05147, July 2026. [arxiv.org/abs/2607.05147](https://arxiv.org/abs/2607.05147)
8. [8]S. Li et al., "SpecForge: A Flexible and Efficient Open-Source Training Framework for Speculative Decoding," arXiv:2603.18567, March 2026. [arxiv.org/abs/2603.18567](https://arxiv.org/abs/2603.18567)
9. [9]Cognition Team, "Measuring the Trustworthiness of Open-Source-Derived Models," July 2026. [cognition.com/blog/measuring-open-source-model-trustworthiness](https://cognition.com/blog/measuring-open-source-model-trustworthiness)

## [Appendix A: Evaluation Methodology](https://cognition.com#appendix-evaluation-methodology)

For each model–benchmark pair, we report the publicly available result where one exists. Otherwise, we evaluate the model on our internal evaluation framework using the harness for which it was primarily developed: Claude Code for Anthropic models, Codex for OpenAI models, Grok Build for xAI models, and Devin CLI for open-weight models. For each model, we report the best score across reasoning-effort settings.

## [Appendix B: Formally Deriving the Cost Penalty](https://cognition.com#appendix-b)

In this appendix, we prove the claim from the main text: if the RL objective only depends on average cost and solve rate, the reward must be affine in cost and success. For simplicity, we allow . The result also holds for binary success , but we omit the more involved proof for this blog.

Let denote the cost and success of a rollout and let be its reward. Recall the assumptions we made in the section above. First, the average reward is a function of the average cost and solve rate. Equivalently, there is a fixed function such that

Second, this identity holds for every distribution of  supported on at most two points (in the main section above, we stated for simplicity the assumption that it holds for all distributions, but this is in fact **stronger** than is really needed!).

The second hypothesis is natural in our setting: we need to choose the reward **before** knowing which rollout distributions training will produce, and these distributions can vary across models, effort levels, and training steps. Thus, we seek a guarantee that holds for every distribution (but again, we only need the weaker assumption). We need the following simple fact.

**Jensen’s functional equation.** A function  on a convex set  satisfies

if and only if for some and .

For deterministic , the hypothesis says that , so . Now taking with probability and with probability gives

Thus satisfies Jensen’s functional equation and is affine: . Dropping the additive constant and rescaling to set leaves as desired.

## [Appendix C: Optimal Baseline Derivation](https://cognition.com#appendix-c)

The score function has zero expectation, . Thus the expected gradient is independent of . Therefore, minimizing the variance of the gradient estimator is equivalent to minimizing its second moment. For independent rollouts, the terms depending on reduce to

Differentiating with respect to and setting the result to zero gives

and hence

For all models, costs assume list pricing, including public discounts. To keep the cost axis readable, the FrontierCode 1.1 Main chart omits Fable 5.1 Max and the DeepSWE 1.1 chart omits Fable 5 Max. Neither point improves on the effort levels shown: Fable 5.1 Max scores 50.3% at $12.83 per task on FrontierCode 1.1 Main, below Fable 5.1 Medium (50.9% at $3.28), and Fable 5 Max scores 69.7% at $21.63 per task on DeepSWE 1.1, below Fable 5 xhigh (69.9% at $13.41).
