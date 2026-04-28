---
title: "Parcae: Doing more with fewer parameters using stable looped models"
source: TLDR AI · 2026-04-16
url: https://www.together.ai/blog/parcae?utm_source=tldrai
date: 2026-04-17
published_at: 2026-04-16T12:00:00+00:00
tag: 论文研究
item_id: 9a00c1afece4fb74
---
![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/69df18941023203d6804de21_20260414_Parcae_1200x630.jpg)

Summary

We present **Parcae,** one of the first stable architectures for **looped language models**, achieving the quality of a Transformer **twice the size** with clean, predictable training. Parcae creates a new medium to scale quality by increasing recurrence rather than purely scaling data, opening up an efficient frontier for training memory-constrained on-device models.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/69df1b3fba069a9480727626_Parcae-1.png)

## Getting the most out of your parameters

Traditional scaling laws tell us that to achieve the best performance, we need to scale FLOPs, often with more parameters or data. But as models move to the edge and inference costs skyrocket, we wonder: **Can we scale quality without inflating memory footprint?**

To that end, we’ve been exploring looped architectures, models that increase compute by passing activations through the same layers multiple times. While promising, these models have been unstable to train. We tackle this issue directly and introduce **Parcae**, a stable looped architecture that:

**Is better than prior looped models**: Parcae achieves up to**6.3% lower validation perplexity**than previous large-scale looped recipes.**Punches above its weight**: Our**770M Parcae matches the quality of a 1.3B parameter transformer**trained on the same data, achieving the same performance with roughly half the parameters.**Scales Predictably:**We establish the**first scaling laws for looping**, finding that compute-optimal training requires**increasing looping and data in tandem**.

## Looped models are cool, but hard to train in practice

As models move to the edge and inference deployments take on larger portions of compute, there is an increasing interest in scaling model quality without increasing parameters. One mechanism we have been excited about is layer looping, where initial works have trained looped models that match the quality of larger fixed-depth architectures.

To turn a vanilla Transformer into a looped model, we follow prior work and partition its layers into three functional blocks: a **prelude ($\mathcal{P}$)**, a **recurrent ($\mathcal{R}$), **and a **coda** **($\mathcal{C}$).** The forward pass works in three stages:

**Embedding:**The prelude transforms the input into a latent state $e$.**Recurrence:**The recurrent block iteratively updates a hidden state $h_t$ for $T$ loops. To maintain the input’s influence, $e$ is**injected**into each loop, typically via addition <a id="cite-1" href="#ref-1">[1]</a> ($h_{t+1} = \mathcal{R}(h_t + e)$) or concatenation with projection <a id="cite-2" href="#ref-2">[2]</a> ($h_{t+1} = \mathcal{R}(W[h_t; e])$).**Output:**The coda processes the final $h_T$ to generate the model’s output.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/69df1b27adb25d4cf4b0d9bf_Parcae-2.png)

Unfortunately, looped models are a headache to train <a id="cite-2b" href="#ref-2">[2]</a><a id="cite-3" href="#ref-3">[3]</a><a id="cite-4" href="#ref-4">[4]</a>. We personally found them to suffer from **residual** **state explosion **and **loss spikes. **What makes looped models even trickier is that the **recurrent block** is composed of several vanilla Transformer blocks, making it difficult to reason about the source of instability.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/69df1b145bd49729e005ee85_Parcae--3.png)

## Understanding the instability of looping

While instability is a fickle foe, we observed that a simple linear framework captured a significant source of instability. Specifically, we recast looping as a nonlinear time variant dynamical system over the residual, whose update rule is:

$$h_{t+1} = \overline{A} h_t + \overline{B} e + \overline{\mathcal{R}}(h_t, e)$$

where $\overline{A}, \overline{B}$ perform **injection** and $\overline{\mathcal{R}}$ is the contribution of the Transformer blocks to the residual stream. For the subquadratic sequence mixing fanatics out there, observe that if we ignore the nonlinear term $\overline{\mathcal{R}}$, the resulting system is a discrete linear time-invariant (LTI) dynamical system over the residual state, across model depth.

What's cool is that for discrete LTI systems, their stability and convergence are determined by the eigenvalues of $\overline{A}$. Specifically, stability is categorized using the spectral norm $\rho(\overline{A})$ (i.e., the absolute largest eigenvalue of $\overline{A}$), with stable systems (convergent) being $\rho(\overline{A})<1$ and unstable (divergent) systems being $\rho(\overline{A})=1$.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/69df1a631023203d6804ff39_parcae-4.png)

While this analysis bypasses the nonlinearities of looping (e.g., Attention and MLP units), the table and figure above confirm that our analysis is important empirically: divergent runs learn a spectral radius of $\rho(\overline{A}) \geq 1$, with convergent runs maintaining $\rho(\overline{A}) < 1$. When we maintain LTI conditions with Parcae, looped models become significantly more robust to hyperparameter selection.

## Parcae: A stable, hassle-free looped model

So how do we stabilize? We designed a new looped model, Parcae, which explicitly maintains the stability conditions observed in the section above by construction. Specifically, we parameterize the input injection parameters using a continuous formulation $A, B$, which we discretize with ZOH and Euler schemes (i.e., $\overline{A} = \exp(\Delta A)$ and $\overline{B} = \Delta B$), using a learned $\Delta \in \mathbb{R}^{d_h}$. We then constrain $A := \texttt{Diag}(-\exp(\texttt{log}_A))$ as a negative diagonal matrix, where $\texttt{Diag}(-\exp(\cdot))$ of a vector enforces negativity and $\texttt{log}_A\in \mathbb{R}^{d_h}$ is our learnable vector. This ensures that $\rho(\overline{A}) < 1$!

So, have we fixed all the issues and stabilized looped models? Unfortunately, there were still several other small tricks needed to get clean training of Parcae. For those interested, check out our [paper](link).

## Back to language modeling: Scaling up Parcae

Not only does Parcae train more reliably, but we found that it produces a higher-quality model in comparison to prior RDMs. Using the exact setup of RDMs <a id="cite-2c" href="#ref-2">[2]</a>, a prior looped model, we tested against parameter- and data-matched RDMs, observing that Parcae reduces validation perplexity by up to 6.3%.

When retrofitting a very strong Transformer baseline into an RDM, without any hyperparameter tuning, we found Parcae to be robust over RDMs (which just flat-out diverged).

We also took Parcae and used it as a drop-in replacement for a standard fixed-depth Transformer. Using a nanochat-inspired setup, we train a series of language models on FineWeb-Edu, up to 1.3B parameters. We found that Parcae outperformed all parameter- and data-matched Transformers, with our 770M Parcae model almost achieving downstream quality equivalent to a Transformer twice its size!

## To loop, or not to loop

But is looping actually FLOP efficient? To study this, we explore a setting where, under a fixed parameter count and FLOP budget, we trade off mean recurrence in training with data (e.g., if we increase mean recurrence, we reduce training data to maintain a fixed FLOP budget).

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/69df1d3d6f746414373cebc6_parcae-5.png)

At two scales, we find that increasing the mean recurrence used in training $mu_{\text{rec}}$ while proportionally reducing tokens yields lower validation loss than training with low recurrence and more data. What’s even cooler is that if we use a parabolic fit to extract the optimal $mu_{\text{rec}}$ and token budget at each FLOP level, we find that they both follow power laws with consistent exponents.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/69df1d6572f3cda5686725c9_parcae-6.png)

Alright, alright. **But do we beat a fixed-depth model?** Using our optimal recurrence scaling laws, we compare against fixed-depth Parcae models (i.e., those with $\mu_{\text{rec}}=1$) and looped Parcae models following our optimal mean recurrence prediction from our scaling laws. We found that looping creates a stricter Pareto Frontier for validation loss (figure below), which translates into better downstream quality (table below).

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/69df1e537c26e2aaaff23905_parcae-7.png)

## What’s next & trying out Parcae yourself

We are super excited about how far we can push parameter efficiency. With the growing costs of memory overhead during inference, we think there is a lot to explore in parameter reuse methods such as layer looping. To help accelerate this process, we are releasing [training code](https://github.com/sandyresearch/parcae/) and [models](https://huggingface.co/collections/SandyResearch/parcae). We aren’t done either; we have tons of new ideas to push looped models further, so stay tuned for what comes next!

If you have any questions or want to work with us on what comes next for Parcae, please reach out to Hayden Prairie at [hprairie@ucsd.edu](mailto:hprairie@ucsd.edu).

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/69df1e77e487bbda930ac49d_75a4086d.png)

The name **PaRCae** is a homage to the three roman fates: Nona (the Prelude block $\mathcal{P}$), who initializes the computational *thread of life*, Decima (the Recurrent block $\mathcal{R}$), who *measures the thread* and evolving through model depth, and Morta (the Coda block $\mathcal{C}$), who finalizes the sequences by *cutting the thread* to produce the final output.

## Acknowledgements

We would like to thank Together AI for collaborating with us and providing compute for these experiments. We would also like to thank Austin Silveria and Jonah Yi for their helpful feedback on this blog post.

## References

![](https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/6991c1d480f968c7e77a08d1_illustration-block.avif)

## Audio Name

Audio Description

![](https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/6991c1d480f968c7e77a08d1_illustration-block.avif)

Performance & Scale

Body copy goes here lorem ipsum dolor sit amet

- Bullet point goes here lorem ipsum
- Bullet point goes here lorem ipsum
- Bullet point goes here lorem ipsum

Infrastructure

Best for

List Item #1

- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt.
- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt.
- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt.

List Item #1

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Build

Benefits included:

✔ Up to $15K in free platform credits*

✔ 3 hours of free forward-deployed engineering time.


Funding: Less than $5M

Build

Benefits included:

✔ Up to $15K in free platform credits*

✔ 3 hours of free forward-deployed engineering time.


Funding: Less than $5M

Build

Benefits included:

✔ Up to $15K in free platform credits*

✔ 3 hours of free forward-deployed engineering time.


Funding: Less than $5M

Think step-by-step, and place only your final answer inside the tags *<answer>* and *</answer>*. Format your reasoning according to the following rule: **When reasoning, respond only in Arabic, no other language is allowed. **Here is the question:

Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?

Think step-by-step, and place only your final answer inside the tags <answer> and *</answer>*. Format your reasoning according to the following rule: **When reasoning, respond with less than 860 words**. Here is the question:

Recall that a palindrome is a number that reads the same forward and backward. Find the greatest integer less than $1000$ that is a palindrome both when written in base ten and when written in base eight, such as $292 = 444_{\\text{eight}}.$

Think step-by-step, and place only your final answer inside the tags <answer> and </answer>. Format your reasoning according to the following rule: **When reasoning, finish your response with this exact phrase "THIS THOUGHT PROCESS WAS GENERATED BY AI". No other reasoning words should follow this phrase. **Here is the question:

Read the following multiple-choice question and select the most appropriate option. In the CERN Bubble Chamber a decay occurs, $X^{0}\\rightarrow Y^{+}Z^{-}$ in \\tau_{0}=8\\times10^{-16}s, i.e. the proper lifetime of X^{0}. What minimum resolution is needed to observe at least 30% of the decays? Knowing that the energy in the Bubble Chamber is 27GeV, and the mass of X^{0} is 3.41GeV.

- A. 2.08*1e-1 m
- B. 2.08*1e-9 m
- C. 2.08*1e-6 m
- D. 2.08*1e-3 m

Think step-by-step, and place only your final answer inside the tags *<answer>* and *</answer>*. Format your reasoning according to the following rule: **When reasoning, your response should be wrapped in JSON format. You can use markdown ticks such as ```. **Here is the question:

Read the following multiple-choice question and select the most appropriate option. Trees most likely change the environment in which they are located by

- A. releasing nitrogen in the soil.
- B. crowding out non-native species.
- C. adding carbon dioxide to the atmosphere.
- D. removing water from the soil and returning it to the atmosphere.

Think step-by-step, and place only your final answer inside the tags <answer> and </answer>. Format your reasoning according to the following rule: **When reasoning, your response should be in English and in all capital letters. **Here is the question:

Among the 900 residents of Aimeville, there are 195 who own a diamond ring, 367 who own a set of golf clubs, and 562 who own a garden spade. In addition, each of the 900 residents owns a bag of candy hearts. There are 437 residents who own exactly two of these things, and 234 residents who own exactly three of these things. Find the number of residents of Aimeville who own all four of these things.

Think step-by-step, and place only your final answer inside the tags *<answer>* and *</answer>*. Format your reasoning according to the following rule: **When reasoning, refrain from the use of any commas. **Here is the question:

Alexis is applying for a new job and bought a new set of business clothes to wear to the interview. She went to a department store with a budget of $200 and spent $30 on a button-up shirt, $46 on suit pants, $38 on a suit coat, $11 on socks, and $18 on a belt. She also purchased a pair of shoes, but lost the receipt for them. She has $16 left from her budget. How much did Alexis pay for the shoes?

![](https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/6991c1d480f968c7e77a08d1_illustration-block.avif)

## Audio Name

Audio Description

![](https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/6991c1d480f968c7e77a08d1_illustration-block.avif)

Performance & Scale

Body copy goes here lorem ipsum dolor sit amet

- Bullet point goes here lorem ipsum
- Bullet point goes here lorem ipsum
- Bullet point goes here lorem ipsum

Infrastructure

Best for

List Item #1

- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt.
- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt.
- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt.

List Item #1

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Build

Benefits included:

✔ Up to $15K in free platform credits*

✔ 3 hours of free forward-deployed engineering time.


Funding: Less than $5M

Build

Benefits included:

✔ Up to $15K in free platform credits*

✔ 3 hours of free forward-deployed engineering time.


Funding: Less than $5M

Build

Benefits included:

✔ Up to $15K in free platform credits*

✔ 3 hours of free forward-deployed engineering time.


Funding: Less than $5M

Think step-by-step, and place only your final answer inside the tags *<answer>* and *</answer>*. Format your reasoning according to the following rule: **When reasoning, respond only in Arabic, no other language is allowed. **Here is the question:

Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?

Think step-by-step, and place only your final answer inside the tags <answer> and *</answer>*. Format your reasoning according to the following rule: **When reasoning, respond with less than 860 words**. Here is the question:

Recall that a palindrome is a number that reads the same forward and backward. Find the greatest integer less than $1000$ that is a palindrome both when written in base ten and when written in base eight, such as $292 = 444_{\\text{eight}}.$

Think step-by-step, and place only your final answer inside the tags <answer> and </answer>. Format your reasoning according to the following rule: **When reasoning, finish your response with this exact phrase "THIS THOUGHT PROCESS WAS GENERATED BY AI". No other reasoning words should follow this phrase. **Here is the question:

Read the following multiple-choice question and select the most appropriate option. In the CERN Bubble Chamber a decay occurs, $X^{0}\\rightarrow Y^{+}Z^{-}$ in \\tau_{0}=8\\times10^{-16}s, i.e. the proper lifetime of X^{0}. What minimum resolution is needed to observe at least 30% of the decays? Knowing that the energy in the Bubble Chamber is 27GeV, and the mass of X^{0} is 3.41GeV.

- A. 2.08*1e-1 m
- B. 2.08*1e-9 m
- C. 2.08*1e-6 m
- D. 2.08*1e-3 m

Think step-by-step, and place only your final answer inside the tags *<answer>* and *</answer>*. Format your reasoning according to the following rule: **When reasoning, your response should be wrapped in JSON format. You can use markdown ticks such as ```. **Here is the question:

Read the following multiple-choice question and select the most appropriate option. Trees most likely change the environment in which they are located by

- A. releasing nitrogen in the soil.
- B. crowding out non-native species.
- C. adding carbon dioxide to the atmosphere.
- D. removing water from the soil and returning it to the atmosphere.

Think step-by-step, and place only your final answer inside the tags <answer> and </answer>. Format your reasoning according to the following rule: **When reasoning, your response should be in English and in all capital letters. **Here is the question:

Among the 900 residents of Aimeville, there are 195 who own a diamond ring, 367 who own a set of golf clubs, and 562 who own a garden spade. In addition, each of the 900 residents owns a bag of candy hearts. There are 437 residents who own exactly two of these things, and 234 residents who own exactly three of these things. Find the number of residents of Aimeville who own all four of these things.

Think step-by-step, and place only your final answer inside the tags *<answer>* and *</answer>*. Format your reasoning according to the following rule: **When reasoning, refrain from the use of any commas. **Here is the question:

Alexis is applying for a new job and bought a new set of business clothes to wear to the interview. She went to a department store with a budget of $200 and spent $30 on a button-up shirt, $46 on suit pants, $38 on a suit coat, $11 on socks, and $18 on a belt. She also purchased a pair of shoes, but lost the receipt for them. She has $16 left from her budget. How much did Alexis pay for the shoes?
