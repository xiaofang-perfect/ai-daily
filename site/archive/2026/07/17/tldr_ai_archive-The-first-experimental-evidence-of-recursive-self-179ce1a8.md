---
title: "The first experimental evidence of recursive self-improvement"
source: TLDR AI · 2026-07-16
url: https://threadreaderapp.com/thread/2077079778793042425.html?utm_source=tldrai
date: 2026-07-17
published_at: 2026-07-16T12:00:00+00:00
tag: 论文研究
item_id: 179ce1a8284bcd8f
---
**
              
              This Thread may be Removed Anytime!**
          

Twitter may remove this content at anytime! Save it as PDF for later use!

- Follow [@ThreadReaderApp](https://twitter.com/threadreaderapp)to mention us!
- From a Twitter thread mention us with a keyword "unroll"

`@threadreaderapp unroll`
          [Practice here](https://twitter.com/threadreaderapp/status/1054877865362112513) first or read more on our [help page](https://threadreaderapp.com/help)!

Is autoresearch really better than classic hyperparameter tuning?


We did experiments comparing Optuna & autoresearch.

Autoresearch converges faster, is more cost-efficient, and even generalizes better: 🧵(1/6)![Image](/images/1px.png)


          We did experiments comparing Optuna & autoresearch.

Autoresearch converges faster, is more cost-efficient, and even generalizes better: 🧵(1/6)

Experiments were done on NanoChat: we let Claude define Optuna’s search space to align the priors between methods.

Both optimization methods were run three times.

Autoresearch is far more sample-efficient on average: (2/6)![Image](/images/1px.png)


          Both optimization methods were run three times.

Autoresearch is far more sample-efficient on average: (2/6)

In 5 min training setting, LLM tokens cost as much as GPUs, but despite a 2× higher per-step cost, AutoResearch still comes out ahead across all cost budgets: (3/6) ![Image](/images/1px.png)


      Training LLMs with Reinforcement Learning (RL) isn’t a new idea.

So why does it suddenly seem to be working now (o1/DeepSeek)?


Here are a few theories and my thoughts on each of them: (1/N)![Image](/images/1px.png)


          So why does it suddenly seem to be working now (o1/DeepSeek)?

Here are a few theories and my thoughts on each of them: (1/N)

Better Base Models

The most plausible hypothesis in my opinion. There’s evidence in the DeepSeek R1 report:


Even if you want a small reasoning model, it’s much better to train a larger LM first and distill it back into smaller ones, rather than train a smaller one directly with RL. (2/N)![Image](/images/1px.png)


          The most plausible hypothesis in my opinion. There’s evidence in the DeepSeek R1 report:

Even if you want a small reasoning model, it’s much better to train a larger LM first and distill it back into smaller ones, rather than train a smaller one directly with RL. (2/N)

It Takes Time to Find the Right Pipeline

Yes, DeepSeek R1 adopted a rather simple RL algorithm. But the whole training pipeline is actually quite complex.


Barebones RL (R1-Zero) produces unreadable chain-of-thought and degrades general capabilities on non-STEM tasks. Eventually, they found a multi-stage approach, mixing different reward types in the final phase. It took strong conviction (and plenty of trials) to get here.


And actually, it might have taken the o1 team even more effort since they didn’t have proof of existence. (3/N)![Image](/images/1px.png)


      Yes, DeepSeek R1 adopted a rather simple RL algorithm. But the whole training pipeline is actually quite complex.

Barebones RL (R1-Zero) produces unreadable chain-of-thought and degrades general capabilities on non-STEM tasks. Eventually, they found a multi-stage approach, mixing different reward types in the final phase. It took strong conviction (and plenty of trials) to get here.

And actually, it might have taken the o1 team even more effort since they didn’t have proof of existence. (3/N)

As a RL research myself, I once doubted Reinforcement Learning (RL) because massive self-supervised LLMs were dominating.

But now I see how RL can bring us closer to super-intelligent (ASI) systems—far beyond board games.

Here’s what changed my mind: (1/5)![Image](/images/1px.png)


          But now I see how RL can bring us closer to super-intelligent (ASI) systems—far beyond board games.

Here’s what changed my mind: (1/5)

1)  Why I Was Pessimistic About RL

RL soared to ASI levels in games like Go. But in real-world tasks, its poor data efficiency often makes it less economical than simply gathering more supervised examples. (2/5)![Image](/images/1px.png)


          RL soared to ASI levels in games like Go. But in real-world tasks, its poor data efficiency often makes it less economical than simply gathering more supervised examples. (2/5)

2)  RLHF & O1 Reasoning

Fast-forward: RLHF and advanced reasoning models like O1 proved that RL can fine-tune beyond imitation learning by a large margin.![Image](/images/1px.png)


      Fast-forward: RLHF and advanced reasoning models like O1 proved that RL can fine-tune beyond imitation learning by a large margin.

I finally find an explanation for why RL is needed for RLHF that satisfied me. It's actually like playing board games.

The reward model can only judge a full answer and a "critic" is needed to efficiently improve the intermediate moves (earlier tokens in the answer) 1/4![Image](/images/1px.png)


          The reward model can only judge a full answer and a "critic" is needed to efficiently improve the intermediate moves (earlier tokens in the answer) 1/4

One question I always had about RLHF is why we bother to use approximate gradients coming from RL if both the reward function and the model are differentiable. 

And the key is in the auto-regressive sampling.

The reward model is not connected to the language model directly. 2/4

          And the key is in the auto-regressive sampling.

The reward model is not connected to the language model directly. 2/4

Instead, it takes a full answer sampled from the language model as input. The autoregressive sampling process is not differentiable.

Every single step of sampling is followed by many forking futures, forming a tree.

3/4

      Every single step of sampling is followed by many forking futures, forming a tree.

3/4

I'm excited to announce Trajectory Autoencoding Planner (TAP), a novel planning-based sequence modelling method that can scale to high dimensionality state-action space. (1/N)

🕸️Website:[sites.google.com/view/latentplan](https://sites.google.com/view/latentplan)

📜Paper:[arxiv.org/abs/2208.10291](https://arxiv.org/abs/2208.10291)

💻Code:[github.com/ZhengyaoJiang/…](https://github.com/ZhengyaoJiang/latentplan) 

          🕸️Website:

📜Paper:

💻Code:

Compared to Trajectory Transformer (TT), the planning of TAP is fast and its decision latency won't increase along with the state-action dimensionality. On high-dimensional offline control tasks, TAP shows strong performance, surpassing model-based and model-free baselines.(2/N) ![Image](/images/1px.png)


          Using a state conditional VQ-VAE, TAP builds a map between possible future trajectories and latent code sequences, where each latent code corresponds to multiple steps of the potential complement of the existing trajectory. (3/N) ![Image](/images/1px.png)
