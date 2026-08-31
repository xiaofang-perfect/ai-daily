---
title: "Continuous Diffusion Language Models (CDLM's)"
source: Hacker News
url: https://sander.ai/2026/08/24/continuous-dlms.html
date: 2026-08-31
published_at: 2026-08-30T20:46:53+00:00
tag: 论文研究
item_id: f5cd89abcf595384
---
A flurry of recent activity in the space of **continuous diffusion models for language**, after a few years of relative dormancy, suggests that this approach is making something of a comeback. Fully discrete diffusion methods had largely supplanted earlier attempts to make continuous diffusion work for language, but the tide is starting to turn. In this post, I want to take a closer look at what’s going on, and why it is happening now.

The recent influx of new research in this space inspired me to write up some of my thoughts. I have written about [diffusion language models](https://sander.ai/2023/01/09/diffusion-language.html) before, so this mainly serves as an update to cover everything that’s happened since then. This will be a fairly subjective account – other perspectives and dissenting opinions are very welcome in the comments and elsewhere! I’ll discuss some technical aspects of continuous diffusion for language later on, but first, some historical context.

## 

![](https://sander.ai/images/chain.jpg)

Modern language models are, by and large, **autoregressive**: they generate sequences one token at a time. This is a natural decomposition of a difficult generation task into smaller, easier sequential steps. All steps are instances of the same underlying task (predict a token given preceding tokens), which enables parameter sharing across the sequence dimension. In spite of this inherently sequential generative process, the Transformer architecture<sup>[1](https://sander.ai#fn:transformer)</sup> admits efficient parallel training across all sequence positions using teacher forcing<sup>[2](https://sander.ai#fn:teacherforcing)</sup>. This has turned out to be an extremely scalable recipe<sup>[3](https://sander.ai#fn:gpt2)</sup>, which has brought us large language models (LLMs).

However, autoregression is not the only way to construct an iterative generative process for sequences. Inspired by early successes in the audiovisual domain, researchers sought to apply **diffusion** to language generation instead. Rather than generating a sequence one element at a time, the generative process of diffusion models is defined by reversing a corruption process, which gradually destroys information. The canonical way to do this is to add Gaussian noise little by little, until it completely overpowers the signal.

### 2021: early discrete diffusion models

After early successes in image generation in 2019<sup>[4](https://sander.ai#fn:score)</sup> and 2020[5](https://sander.ai#fn:improvedscore)<sup>[6](https://sander.ai#fn:ddpm)</sup>, the first attempts to apply this idea to language arrived in 2021, and involved **replacing a continuous corruption process with a discrete one** to enable modelling of categorical data: multinomial diffusion<sup>[7](https://sander.ai#fn:multinomial)</sup>, D3PM<sup>[8](https://sander.ai#fn:d3pm)</sup> and SUNDAE<sup>[9](https://sander.ai#fn:sundae)</sup>.

Back then, the dominance of autoregression was not as well-established as it is today: GPT-3<sup>[10](https://sander.ai#fn:gpt3)</sup> had turned some heads, but the ‘ChatGPT moment’ wouldn’t come until late 2022. At the time, discrete diffusion seemed to address some real theoretical flaws in the autoregressive paradigm, like exposure bias due to [teacher forcing](https://en.wikipedia.org/wiki/Teacher_forcing) and the relative difficulty of applying it to infilling and constrained generation tasks. Note that there had been some exploration of non-autoregressive and any-order autoregressive approaches in the preceding years[11](https://sander.ai#fn:maskpredict)<sup>[12](https://sander.ai#fn:xlnet)</sup> (especially for machine translation[13](https://sander.ai#fn:nat)<sup>[14](https://sander.ai#fn:iternat)</sup>), but not yet from a diffusion perspective.

### 2022: continuous diffusion for discrete data

In 2022, several attempts to **apply continuous diffusion to language modelling** appeared, starting with Diffusion-LM<sup>[15](https://sander.ai#fn:diffusionlm)</sup>. This approach addresses the incompatibility between categorical data and corruption with Gaussian noise in a different way: simply represent the discrete categories with continuous embedding vectors, which are perfectly amenable to Gaussian noise corruption. That way, the Gaussian diffusion mechanism, which works so well for images, can be applied without any changes.

Diffusion-LM touted the advantages of this alternative generative paradigm for controllable text generation in particular. In the last few months of 2022, quite a few other papers using variations of this approach were published, including DiffuSeq<sup>[16](https://sander.ai#fn:diffuseq)</sup>, SSD-LM<sup>[17](https://sander.ai#fn:ssdlm)</sup>, Difformer<sup>[18](https://sander.ai#fn:difformer)</sup>, SeqDiffuSeq<sup>[19](https://sander.ai#fn:seqdiffuseq)</sup>, GENIE<sup>[20](https://sander.ai#fn:genie)</sup>, LD4LG<sup>[21](https://sander.ai#fn:ld4lg)</sup> and also two papers that I worked on: self-conditioned embedding diffusion (SED)<sup>[22](https://sander.ai#fn:sed)</sup> and continuous diffusion for categorical data (CDCD)<sup>[23](https://sander.ai#fn:cdcd)</sup>.

At the time, the allure of these continuous methods was that they could benefit from all the insights, tools and machinery that were being discovered and developed for continuous diffusion, as it completely took over audiovisual generation. For example, applying some of the sampling and distillation techniques developed for continuous diffusion models to discrete diffusion was often much less straightforward, or even downright impossible.

### Late 2023: the continuous extinction

Then, something interesting happened: **after 2023, virtually all new research in this space used discrete diffusion**, and continuous diffusion for language went extinct. A diagram from a 2025 survey paper<sup>[24](https://sander.ai#fn:survey)</sup> about diffusion language models clearly shows this:

New survey on diffusion language models: [https://t.co/SHicf69gxV](https://t.co/SHicf69gxV) (via [@NicolasPerezNi1](https://twitter.com/NicolasPerezNi1?ref_src=twsrc%5Etfw)). Covers pre/post-training, inference and multimodality, with very nice illustrations.

I can't help but feel a bit wistful about the apparent extinction of the continuous approach after 2023🥲 [pic.twitter.com/RYvLHuLHWH](https://t.co/RYvLHuLHWH)

[August 19, 2025](https://twitter.com/sedielem/status/1957906664410984848?ref_src=twsrc%5Etfw)

Continuous methods are marked in yellow, discrete methods in green. The transition from 2023 to 2024 is quite stark! It is difficult to say for certain why this happened, but I can think of a few potential factors: one is the ChatGPT moment, which gradually shifted the focus of language diffusion research from theoretical advantages and elegance to raw performance. Now, the goal was to try and **match powerful autoregressive models at scale**, or even outcompete them in specific settings. It seems that people felt closing the performance gap would be easier to achieve with fully discrete methods, perhaps because they are conceptually more closely related to autoregression.

Another factor could be that the **science of scaling language diffusion models** had started to be explored, and initial observations for continuous methods weren’t looking promising. In May 2023, Gulrajani & Hashimoto<sup>[25](https://sander.ai#fn:plaid)</sup> quantified the training efficiency gap for a likelihood-based continuous diffusion language model (Plaid-1B): **64x less efficient**. (Note that the diagram above marks Plaid as discrete, but it is a continuous method.)

At a time when the LLM community was still very much focused on the pareto frontier of training compute versus perplexity (Chinchilla-optimality<sup>[26](https://sander.ai#fn:chinchilla)</sup>), any modelling approach whose training efficiency was almost two orders of magnitude worse than an autoregressive baseline was difficult to take seriously. The first LLaMA<sup>[27](https://sander.ai#fn:llama)</sup> model, which challenged this training efficiency focus and argued for taking the inference budget into account, had only just been released a few months earlier (February 2023), so I believe it is plausible that the community had not yet internalised this shift.

Needless to say, this is all highly speculative. Perhaps it was just a coincidence, and discrete methods ended up having more momentum around that time purely by chance. If you have any thoughts about what could have caused the late-2023 continuous extinction event, I’d be keen to hear them in the comments!

Personally, I had stopped working on diffusion language models by that point (I got too busy building image and video generation models: [Imagen](https://deepmind.google/models/imagen/) and [Veo](https://deepmind.google/models/veo/), and later on, [Nano Banana](https://deepmind.google/models/gemini-image/) and [Omni](https://deepmind.google/models/gemini-omni/)), so I was just observing this evolution from the sidelines. I found it somewhat suprising, because I believed continuous diffusion has a few key advantages, like an ability to represent uncertainty at the individual token level, and a rich toolbox of sampling algorithms and tricks to draw on. Giving those up seemed like it could be a mistake, but the research community as a whole clearly figured that this was the way to go.

## 

![](https://sander.ai/images/discrete.jpg)

We will talk about what’s been happening in the diffusion language modelling space more recently in [the next section](https://sander.ai#comeback), but first, I think it is useful to discuss how continuous diffusion can actually be applied to discrete data in a bit more detail. This context will be helpful to understand what might be driving recent events.

The first thing to consider is the nature of the discrete data we are trying to model. Usually when people say ‘discrete’, they actually mean *categorical*, i.e. the output space (at the token level) is an unstructured set, and there is no relationship (ordinal or otherwise) between the different values that each discrete variable can assume. Digital images represented as pixel grids are *also* discrete, technically speaking, but because the discrete values assumed by the pixel colour channels represent an underlying continuous physical signal (light intensity), we tend to simply ignore that, and treat them as continuous anyway.

Assuming we are working with categorical data, there are a few necessary ingredients to make continuous diffusion work well: an **embedding strategy**, a **loss function**, and a sensible **noise schedule**. In addition, there is a trick that pops up in almost every paper on this topic, which turns out to have a huge impact on performance: **self-conditioning**. We’ll take a closer look at each of these in turn. For brevity, I will use the acronym **CDLM** to refer to continuous diffusion language models going forward, and **DDLM** to refer to their discrete counterparts.

### 

Modern neural networks typically have real-valued parameters and activations. Therefore, the first thing that usually happens in any neural network that processes discrete data, is *embedding* the discrete inputs in a continuous representation space. From that point on, the network exclusively manipulates real-valued representations. These embeddings are usually just treated as additional parameters, which can be optimised jointly with the rest of the model. It’s worth pointing out that this is also the case for DDLMs and autoregressive models – the internals of the neural networks powering these models are still continuous.

To apply continuous diffusion to discrete data, we can simply ‘lift’ the corruption process from the discrete input space into a continuous embedding space. In other words, compared to discrete diffusion, it’s just a question of changing the order of operations. Rather than applying discrete corruption followed by continuous embedding during training, we first embed the inputs and then apply continuous corruption instead.

![Schematic diagram of (a) an autoregressive model, (b) a discrete diffusion model (masked diffusion) and (c) a continuous diffusion model. Green blocks indicate continuous embeddings of the discrete tokens. Blue blocks represent the layers of the model. For a and b, the embedding stage is typically considered also part of the model. Corruption for b happens at the token level, before embedding. For c, corruption is applied by adding noise to the continuous embeddings.](https://sander.ai/images/cdlm_embeddings.png)

The shape and structure of the embedding space profoundly impacts the nature of the continuous corruption process that happens within it. Various embedding strategies have been explored:

- 
    **Explicit** (e.g. SSD-LM<sup>[17](https://sander.ai#fn:ssdlm)</sup> ): arguably the simplest approach is to use something like a[one-hot representation](https://en.wikipedia.org/wiki/One-hot) , where every element in a vocabulary of size $V$ is associated with a $V$-dimensional vector that has $V-1$ zeros and a single one. Since a vocabulary is a set, assigning representations to the elements requires arbitrarily picking a specific ordering. This kind of embedding space can be cumbersome to work with for modern language models, because $V$ tends to be pretty large nowadays. A potential workaround is to use compact binary patterns instead, as in Analog Bits<sup>[28](https://sander.ai#fn:analogbits)</sup> .
- 
    **Pre-trained** (e.g. SED<sup>[22](https://sander.ai#fn:sed)</sup> ): we can use a representation learning strategy to learn embeddings, and then repurpose them for use in a diffusion language model. For example, they could be borrowed from an autoregressive language model, or taken from a bidirectional language model like BERT<sup>[29](https://sander.ai#fn:bert)</sup> . They can also be made*contextual* , i.e. the embedding for a given token can depend not only on the token itself, but also on adjacent tokens, resulting in a richer embedding space<sup>[21](https://sander.ai#fn:ld4lg)</sup> .
- 
    **Jointly learned** (e.g. CDCD<sup>[23](https://sander.ai#fn:cdcd)</sup> ): we can try to fit the embeddings together with the denoiser model in a single learning procedure, potentially letting them co-adapt.

The latter might seem like the most natural thing to do, because joint learning of the embeddings is what works for DDLMs and autoregressive LLMs. An end-to-end single-stage learning approach is also widely considered the most attractive nowadays, both from a conceptual and from a practical standpoint. But the elevated role of the embedding space in CDLMs (relative to DDLMs) means that this comes with some challenges: naive formulations are prone to embeddings collapsing or growing uncontrollably. For example, denoising error can be minimised pathologically by making all embeddings the same, so this suggests that some sort of trade-off between multiple constraints or terms in the loss function might be necessary.

There has been a fair bit of discussion in the literature about the importance of the **geometry** of the embedding space. It is often assumed or suggested that embedding spaces with meaningful semantic structure lend themselves better to continuous diffusion language modelling. Concretely, this means that the embeddings should be organised in such a way that a given amount of corruption creates commensurate confusion between tokens from a semantic perspective; e.g. if a small amount of noise is added to the embedding for ‘cat’, it might become indistinguishable from the embedding for ‘dog’ with the same amount of noise added, but it will still look very different from the embedding for, say, ‘umbrella’, at the same noise level.

It is still unclear to me how important this actually is, if what we care about is raw language modelling performance. This is not a factor that is usually considered in the context of DDLMs or autoregressive LLMs. It has been suggested in the literature that some strategies and learning objectives for CDLMs have a *dispersive* effect<sup>[30](https://sander.ai#fn:replaid)</sup> (i.e. pushing embeddings for semantically related tokens apart, rather than together), and that this might be a bad thing, which certainly seems plausible.

Related to this is the question of whether continuous embeddings should represent individual tokens, tokens in context (i.e. contextual embeddings), or something more hierarchical, like sequences of multiple tokens, or even entire sentences or paragraphs. While the focus in this blog post is on token-based approaches, I’ll briefly discuss these higher-level alternatives (often framed as ‘latent diffusion for language’) [later on](https://sander.ai#next).

As the goal of CDLMs is ultimately to generate a discrete token sequence, an **unembedding strategy** is also needed. Neural networks for classification tasks use a softmax nonlinearity to make predictions in a categorical space, and interpret the network outputs as *probabilities* (which are themselves continuous). This approach can also be used for denoisers: even if we are denoising continuous vectors, we can use the knowledge that they each represent one of a finite number of discrete vocabulary elements to constrain the predictions (in CDCD<sup>[23](https://sander.ai#fn:cdcd)</sup>, we took advantage of this observation and called it ‘score interpolation’, framing it as an alternative to ‘score matching’). In most works however, predictions are made directly in the continuous embedding space, without such constraints, and a final discretisation step is performed at the end of sampling. This is often done simply by clamping the embeddings to the nearest vocabulary element, but the procedure can also be more involved.

### 

There is some interesting variety in the loss functions used for training CDLMs. I won’t enumerate all the options, but I do want to point out some trends. Usually, the choice of loss function is closely tied to the unembedding strategy. If the denoiser makes predictions directly in the continuous embedding space, the usual **mean squared error** (MSE) loss tends to be used, just like in continuous diffusion models for audiovisual data.

If the denoiser outputs probabilities across vocabulary elements, it can be trained using the **categorical cross-entropy** loss instead, which makes things look more similar to the autoregressive setting. Note that this approach only works with per-token embeddings and is not compatible with contextual or higher-level embeddings: predicting probabilities for every possible output is feasible at the per-token level if the vocabulary size is not too large, but not beyond that.

Another approach is to start from the maximum likelihood principle<sup>[25](https://sander.ai#fn:plaid)</sup>, and come up with an objective that **bounds the likelihood** from below (in the same way that variational autoencoders[31](https://sander.ai#fn:vaekingma)<sup>[32](https://sander.ai#fn:vaerezende)</sup> are trained). Some CDLM variants that jointly learn the embeddings and the denoiser include additional loss terms to regularise or constrain them<sup>[15](https://sander.ai#fn:diffusionlm)</sup>, but sometimes these constraints are handled through parameterisation instead (e.g. forcing the embeddings to be normalised vectors<sup>[23](https://sander.ai#fn:cdcd)</sup>).

Several works have explored various ways to constrain the continuous diffusion process to the $V$-simplex: the space of valid categorical probability distributions across $V$ categories[33](https://sander.ai#fn:simplex)[34](https://sander.ai#fn:ddsm)[35](https://sander.ai#fn:floto)<sup>[36](https://sander.ai#fn:dirichletfm)</sup>. In this setup, intermediate noisy vectors are themselves constrained to be valid probability distributions across all vocabulary elements, which also requires alternative loss functions. While it seems like a good idea in theory, in practice, this usually adds significant complexity and it doesn’t seem to be very scalable to large vocabulary sizes. Most successful applications of this idea have actually been in biology, where interesting discrete sequence modelling problems with much smaller vocabularies exist (e.g. $V=4$ for DNA, $V\approx22$ for amino acids).

### 

The corruption process of a diffusion model is governed by the noise schedule, which determines the rate at which the noise level increases over the course of the process. I wrote a lot more about noise schedules for continuous diffusion models [in an earlier blog post](https://sander.ai/2024/06/14/noise-schedules.html).

Ideally, the schedule is chosen so that information is destroyed gradually, allowing the generative process to be broken up into smaller subtasks that each resolve small amounts of uncertainty. A poorly chosen noise schedule results in large segments of the corruption process where nothing happens (i.e. almost no information is lost, and therefore the denoiser has nothing to learn), and some segments where a lot of information is destroyed all at once, making for a very difficult denoising task.

For CDLMs, getting the noise schedule right is especially important, as a naive strategy will almost certainly result in a very uneven corruption process. This is a direct consequence of the fact that embeddings are usually high-dimensional vectors, which represent discrete underlying categories. In that setting, **meaningful corruption happens across a relatively small range of noise levels**. Most noise levels either destroy almost no information about token identity (too low), or destroy almost all information (too high). It is important to avoid spending denoiser modelling capacity on those noise levels, as it will not be able to learn anything useful there.

A common strategy has been to explicitly adapt the noise schedule to the geometry of the embedding space, either offline or through **online adaptation of the noise schedule during training**. This creates a feedback loop, where the model predictions are used to determine which noise levels are of interest, and subsequently the distribution of noise levels sampled to corrupt training examples is adapted to focus training on precisely those noise levels.

The original inspiration for such online adaptation mechanisms was the variational diffusion models (VDM) paper<sup>[37](https://sander.ai#fn:vdm)</sup>, which used this idea to minimise the variance of the training objective, in order to accelerate convergence. In the context of CDLMs, this approach was adapted to obtain a balanced corruption process with a focus on noise levels where the level of corruption is just right to enable learning of meaningful structure. This can be achieved by learning a schedule $\sigma(t)$ that linearises the entropy of the denoiser predictions[23](https://sander.ai#fn:cdcd)<sup>[38](https://sander.ai#fn:infonoise)</sup> (in terms of $t$), or the decoding error rate<sup>[39](https://sander.ai#fn:fmlm)</sup>. With $t$ sampled uniformly, entropy linearisation ensures that each diffusion sampling step resolves the same number of bits of information.

![Figure from the CDCD paper showing the effect of adapting the noise schedule during training. The relative weight of the different noise levels (middle plot) becomes highly non-uniform, and the focus is on those noise levels where the entropy changes the fastest. In terms of the learnt schedule (referred to here as 'uniform time'), the entropy increases approximately linearly. If sampling steps are spaced evenly in uniform time, the amount of entropy they resolve is roughly constant.](https://sander.ai/images/time_warping.png)

### 

Diffusion sampling is *stateless*, in the sense that the next update step in the sampling procedure only depends on the current canvas. One could consider the canvas itself to constitute a form of state, but crucially, it is always fully observed. There is no additional hidden context that the model can manipulate during sampling, which is why the sampling procedure can be (and often is) framed in terms of differential equations<sup>[40](https://sander.ai#fn:sde)</sup>.

This led some people to wonder if perhaps denoisers used for diffusion sampling are doing redundant work: at every sampling step, they compute the optimal denoising direction from observing the current noisy canvas, without access to their own previous predictions from earlier steps. But if the steps are small enough, the optimal denoising direction might actually be quite similar to the previous prediction, so this seems like it could be wasteful.

**Self-conditioning**<sup>[28](https://sander.ai#fn:analogbits)</sup> was introduced to address this: simply **pass the denoiser’s previous prediction to the next step** as an extra input. This allows the denoiser to learn how to modify a rough estimate, rather than having to make predictions from scratch. To train such a denoiser, the additional ‘previous prediction’ input is sometimes left blank, and sometimes provided during training by using the denoiser itself to make a prediction from scratch (hence ‘self’-conditioning). This clever mechanism ensures that the denoiser still works when no previous prediction is available, but also knows what to do with it when it is provided.

![Illustration of self-conditioning from the Analog Bits paper, which introduced it.](https://sander.ai/images/selfcond.png)

[Analog Bits](https://arxiv.org/abs/2208.04202)paper, which introduced it.

For CDLMs, it was discovered pretty quickly that self-conditioning tends to provide a huge boost in performance, and so almost all works in this space make use of it. This is in spite of the fact that it breaks the statelessness assumption built into various diffusion machinery, most notably sampling algorithms based on differential equations (ODEs and SDEs). It is fair to assume that it probably biases the modelled distribution in hard-to-understand ways, but everyone uses it anyway, because it makes such a huge difference to sample quality that it would be an act of self-sabotage not to.

Exactly why this works so well for language diffusion in particular is still unclear – especially because attempts to apply the idea for audiovisual generative modelling have been far less fruitful (Recurrent Interface Networks<sup>[41](https://sander.ai#fn:rin)</sup> are a notable exception). The underlying discrete structure of the output space seems to play a role in this. A recent paper by Yoo et al.<sup>[42](https://sander.ai#fn:fpf)</sup> reanalyses diffusion with self-conditioning as an efficient approximation of a fixed-point model embedded within a diffusion model, almost like a nested for-loop. This perspective provides an explanation as to why the statefulness of denoisers with self-conditioning does not appear to be a problem in practice: it is merely a side effect of approximating the nested for-loop with a single flat loop.

### 

To wrap up this section, I want to illustrate how these ingredients can come together in a few different ways, using some early works in the CDLM space that I contributed to. All of these date back to late 2022, because I stopped working on language after that.

[Simplex diffusion](https://arxiv.org/abs/2210.14784)<sup>[33](https://sander.ai#fn:simplex)</sup> uses a non-Gaussian corruption process: the so-called Cox-Ingersoll-Ross (CIR) process<sup>[43](https://sander.ai#fn:cir)</sup>. This operates on strictly positive real values, and it was originally used to model interest rates. It comes with a built-in assumption that these interest rates cannot be negative, so as you can imagine, it lost a bit of traction for that purpose after 2008! That property does make it very well-suited to model (unnormalised) probabilities, though. We used the score-based SDE formalism (📉) with this alternative process, which (somewhat surprisingly) yields tractable, if slightly exotic formulas for all the quantities of interest. For example, the transition density is a non-central chi-squared distribution, instead of the usual Gaussian. This was a theoretical exploration during the project that later became CDCD (see below). We ended up not pursuing it further, because it seemed to scale poorly to larger vocabulary sizes.

[Self-conditioned embedding diffusion](https://arxiv.org/abs/2211.04236)<sup>[22](https://sander.ai#fn:sed)</sup> (SED) is built around pre-trained embeddings (📍) obtained using a BERT model, which is slightly modified to have a low-rank bottleneck, as diffusion on lower-dimensional embeddings was found to perform better. Note that even though they come from a BERT model, the embeddings themselves are per-token, not contextual. The loss function is a combination of the usual denoising MSE and a cross-entropy-based unembedding loss (📉), the noise schedule is a cosine schedule (📻 fairly standard for the time), and self-conditioning is an important ingredient (🔄 it’s in the name!).

[Continuous diffusion for categorical data](https://arxiv.org/abs/2211.15089)<sup>[23](https://sander.ai#fn:cdcd)</sup> (CDCD) is built on the principle that language diffusion would be more likely to see wider adoption if it looks as familiar as possible to existing LLM practitioners. The paper frames it as a version of BERT, but with Gaussian noise instead of masking noise. It uses standard Gaussian diffusion, but with a cross-entropy loss function (📉 *score interpolation*), and with embeddings learnt on the fly, jointly with the denoiser (📍). As this makes the embeddings prone to uncontrollable growth, a normalisation layer is used to force them to have unit norm. It also relies heavily on self-conditioning to achieve good performance (🔄). Another key performance factor is the *adaptive* noise schedule based on an entropy linearisation heuristic (📻 *time warping*), which ensures that both training and sampling spend more time and capacity on the noise levels that matter most.

To my own delight, many of the CDCD ingredients have become fairly mainstream in modern CDLM works (several of which I’ll discuss in the next section). Adaptive schedules feature frequently, and they often use some sort of linearisation heuristic. The score interpolation strategy that originally enabled cross-entropy-based training of continuous denoisers has been rederived in a more modern setting (i.e. flow matching<sup>[44](https://sander.ai#fn:flowmatching)</sup> and flow maps<sup>[45](https://sander.ai#fn:fmm)</sup>), and given a stronger theoretical underpinning. Self-conditioning is now ubiquitous.

## 

![](https://sander.ai/images/embers.jpg)

With all of that in mind, let’s pick up where we left off at the end of [the first section](https://sander.ai#history), and take a look at what’s been going on with CDLMs more recently.

After 2023, this space was very quiet for a long time as people focused on discrete diffusion. Two strategies for discrete corruption are commonly used: **masked discrete diffusion** corrupts tokens by gradually replacing all of them with mask tokens, until the sequence is fully masked. **uniform-state discrete diffusion** corrupts tokens by replacing them with random tokens instead, until the sequence is fully randomised. The former approach has a single deterministic *absorbing* end state (fully masked), whereas the end state of the latter is that all possible token sequences are equally likely (uniform  categorical distribution).

In the second half of 2025, people started trying to bring back some continuous flavour in the form of **hybrid methods**, combining discrete and continuous approaches in various ways to try and get the best of both worlds. This was followed in 2026 by a full-on resurgence of continuous methods.

### 

Sahoo et al.<sup>[46](https://sander.ai#fn:duo)</sup> started off this trend by observing a close connection between Gaussian continuous diffusion and uniform-state discrete diffusion. They found that mapping continuous noisy intermediate states to discrete states using the $\arg \max$ operator also implicitly turns the Gaussian corruption process into a uniform-state corruption process. They called this relationship the **diffusion duality**, and used it to apply consistency distillation<sup>[47](https://sander.ai#fn:cm)</sup> to discrete diffusion models, as well as for training loss variance reduction.

CADD<sup>[48](https://sander.ai#fn:cadd)</sup>, CCDD<sup>[49](https://sander.ai#fn:ccdd)</sup> and CANDI<sup>[50](https://sander.ai#fn:candi)</sup> all suggest different ways to **combine discrete and continuous corruption** into a single process. CADD uses continuous intermediate representations to augment masked diffusion, in order to ensure that information is lost in a more gradual fashion. CCDD uses joint diffusion over discrete and continuous representations simultaneously, to tap into the increased expressivity of continuous diffusion, while avoiding the challenge of decoding continuous embeddings back into discrete tokens.

CANDI instead tries to address a scaling issue with continuous diffusion for discrete data, which they call *temporal dissonance*: for high-dimensional vocabularies, the discrete identity of individual tokens decays quickly as the corruption process progresses, but their relative rank among all posibilities decreases much more slowly. By the time there is anything interesting to learn about the semantic structure of the continuous embedding space, all token identities have already been corrupted, and the model will have a really difficult time learning about the conditional relationships between tokens as a result. They identify this as a key problem holding back continuous methods, and propose to address it by using discrete masking and applying Gaussian corruption only to the masked positions, thereby decoupling these two kinds of corruption.

These works all appeared within a few months of each other, making it almost seem like a coordinated effort to rehabilitate continuous diffusion for discrete data, while still sticking closely to the dominant discrete paradigm. Not long after this, the purely continuous approach also saw a revival, as we will discuss next.

### 

2025 had also seen the development and rapid adoption of *flow maps*[45](https://sander.ai#fn:fmm)<sup>[51](https://sander.ai#fn:selfdist)</sup>, the subject matter of [my previous blog post](https://sander.ai/2026/05/06/flow-maps.html). A flow map is essentially the integral of a diffusion model. In a diffusion model, a denoiser is learnt, which can be used to move through input space from noise to data by repeatedly taking small steps in the predicted denoising direction. Flow maps try to do this in one go instead, or at least, in as few steps as possible. To achieve this, a network is trained to directly approximate the output of the diffusion sampling procedure. (I’m deliberately cutting some corners here for brevity’s sake, but that is the gist of it.)

Although [step distillation of diffusion models](https://sander.ai/2024/02/28/paradox.html) had already been a fruitful research topic long before that, the development of such a powerful framework seemed to inspire several groups of researchers to revisit continuous methods for language modelling, in hopes of bringing the benefits of the framework to this class of models as well. Early 2026 saw the appearance of three closely related works in rapid succession: Categorical Flow Maps<sup>[52](https://sander.ai#fn:cfm)</sup>, Flow Map Language Models<sup>[39](https://sander.ai#fn:fmlm)</sup> and Discrete Flow Maps<sup>[53](https://sander.ai#fn:dfm)</sup>. All three **extend flow maps to the discrete categorical setting** using explicit one-hot embeddings (📍) and cross-entropy-based loss functions (📉), bringing their application to language modelling within reach.

In the spring of 2026, this was followed by something of a Cambrian explosion in the space of CDLMs. A series of papers appeared that revisited and extended various recipes:

- 
    LangFlow <sup>[54](https://sander.ai#fn:langflow)</sup> , Spherical flows<sup>[55](https://sander.ai#fn:sf)</sup> and Hyperspherical flows<sup>[56](https://sander.ai#fn:hsf)</sup> build on CDCD<sup>[23](https://sander.ai#fn:cdcd)</sup> , making use of jointly learned normalised embeddings (📍), the cross-entropy loss (📉) and adaptive noise schedules (📻). The latter two works constrain the corruption process to the sphere (we tried a naive variant of this in CDCD and called it ‘renormalisation’, but that didn’t work very well).
- 
    Latent diffusion language models (LDLM) <sup>[57](https://sander.ai#fn:ldlm)</sup> and Embedded language flows (ELF)<sup>[58](https://sander.ai#fn:elf)</sup> follow the design of Diffusion-LM<sup>[15](https://sander.ai#fn:diffusionlm)</sup> and SED<sup>[22](https://sander.ai#fn:sed)</sup> , applying the standard continuous diffusion recipe in an appropriately chosen embedding space. A major difference is that they make use of contextual embeddings, rather than per-token ones (📍 following LD4LG<sup>[21](https://sander.ai#fn:ld4lg)</sup> ). They are jointly learnt with the denoiser for LDLM, whereas ELF (primarily) uses pre-trained and frozen embeddings.
- 
    Continuous bitstream diffusion (CoBit) <sup>[59](https://sander.ai#fn:cobit)</sup> uses explicit embeddings in the form of bit sequences (📍), applying and extending the Analog Bits<sup>[28](https://sander.ai#fn:analogbits)</sup> approach to language.
- 
    RePlaid <sup>[30](https://sander.ai#fn:replaid)</sup> revisits Plaid<sup>[25](https://sander.ai#fn:plaid)</sup> and modernises its likelihood-based approach (📉) by drawing from recent DDLMs.

Compared to their predecessors, these works feature a modernised framing, improved implementations, new theoretical insights, updated evaluation methodologies and increased scale. Several of them argue that the **previous consensus about discrete diffusion having the edge is incorrect**. RePlaid and LangFlow even make the opposite claim in their respective paper titles: *‘Continuous Diffusion Scales Competitively with Discrete Diffusion for Language’, ‘Continuous Diffusion Rivals Discrete in Language Modeling’*.

### 

The revival of CDLMs is very much ongoing, so it is probably a bit too early for a historical perspective that tries to fully explain the back-and-forth between discrete and continuous methods over the past five years. Nevertheless, I want to point out a few trends that have likely influenced it.

First of all, **continuous methods have gotten simpler and easier to use** over the years: earlier perspectives required understanding score matching<sup>[4](https://sander.ai#fn:score)</sup>, deep latent variable models<sup>[6](https://sander.ai#fn:ddpm)</sup> or differential equations<sup>[40](https://sander.ai#fn:sde)</sup>; modern explanations rely mostly on basic concepts like linear interpolation between data and noise<sup>[44](https://sander.ai#fn:flowmatching)</sup>. This has lowered the barrier of entry for practitioners in adjacent fields to also explore these methods.

Interest in alternative modelling paradigms for language beyond autoregression has also increased overall, thanks to the success of DDLMs and the quest to explore novel substrates for reasoning. The potential pay-off of finding the next big thing has only increased as large language models have become big business: **making language models faster and more flexible has become highly economically valuable**.

Attempts to decrease the number of steps required to sample from DDLMs tend to hit a wall: **simultaneously sampled tokens are assumed to be conditionally independent** given previously sampled tokens. In the limit of single-step sampling, this means all tokens are necessarily sampled independently, and the models are then fundamentally unable to capture any correlations between them. This makes step distillation challenging, and overcoming that problem might require introducing significant additional complexity.

Continuous methods side-step this issue completely: trajectory-based step distillation methods (like flow map methods) enable even single-step models to capture all correlations, at least in theory – in practice, the limited capacity of the models still makes this challenging to do in just one step. Nevertheless, I think it is fair to say that few-step sampling comes much more naturally to the continuous setting. This **distillability advantage** is probably the main reason why CDLMs are back with a vengeance today.

Step distillation doesn’t just enable faster sampling: it also unlocks possibilities for reward-based steering and fine-tuning that were challenging to achieve with diffusion-based language models before (see [this section](https://sander.ai/2026/05/06/flow-maps.html#applications) in my previous blog post). Given the major role that post-training plays in the success of modern LLMs, this is also an important consideration.

Whether so-called **flow map language models** will displace the current status quo wholesale remains to be seen, but I fully expect them to continue to gain traction, and efforts to scale them up are underway<sup>[60](https://sander.ai#fn:scalingcfms)</sup>. I strongly recommend reading Floor Eijkelboom’s [deep dive on flow-based language generation](https://flow-based-llms.github.io/) for a more technical treatment of this topic. Jiaming Song also has [a nice write-up](https://tsong.me/blog/inference-time-scaling/) on the role of diffusion and flow maps in language modelling.

It is interesting to ponder how the dominant position of continuous diffusion models for audiovisual generation is motivated by almost entirely different reasons. I have previously written extensively about the [spectral perspective on diffusion](https://sander.ai/2024/09/02/spectral-autoregression.html), and the [link between noise levels and feature scales](https://sander.ai/2024/06/14/noise-schedules.html#noise-levels) in the visual domain. I believe the fact that we can manipulate the diffusion loss to emphasise perceptually relevant content is a key reason for their success, but that clearly does not apply to language modelling at all.

One commonly heard argument in favour of CDLMs is that they make multimodal integration easier: we can use continuous diffusion across all modalities and combine them into a single model. While that is true, I think it misses the point a little bit. The challenge of building multimodal generative models is not so much about bridging multiple modelling paradigms, which is actually not that difficult (see e.g. Diffusion Forcing<sup>[61](https://sander.ai#fn:diffusionforcing)</sup>, Transfusion<sup>[62](https://sander.ai#fn:transfusion)</sup>). A more pertinent challenge is the **semantic gap** that exists between language representations and representations of perceptual signals used in diffusion models (i.e. [latents](https://sander.ai/2025/04/15/latents.html) or patches of pixels): language tokens are semantically abstract, audiovisual tokens are not. I will probably have more to say about that in a future blog post. For now, all I have is a spicy tweet 🌶️:

In a multimodal context, even the discrete/continuous divide is a distraction.

The real challenge is bridging the semantic gap between inherently high-level language tokens, and the very low-level representations we tend to use for perceptual signals.

(I couldn't resist😆) [https://t.co/0or588gBV5](https://t.co/0or588gBV5)

[June 1, 2026](https://x.com/sedielem/status/2061375507824882038?ref_src=twsrc%5Etfw)

### 

Is this the end of the line for discrete diffusion, then? That seems rather unlikely. Dimitri von Rütte made the case that [diffusion language models are the future](https://dimitri.ml/posts/why-diffusion-language-models-are-the-future/) a while back (uniform-state discrete models in particular). More recently, Volodymyr Kuleshov and colleagues shared [a post describing the building blocks](https://kuleshov-group.github.io/blog/blog/2026/how-to-build-a-diffusion-language-model/) of DDLMs, and Junbo Zhao wrote [a blog post](https://jzhao2024.github.io/notes/2026/08/08/diffusion-language-models.html) about their move into the mainstream. A lot of people seem to be bullish enough about the approach to blog about it!

The recent release of [DiffusionGemma](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/)<sup>[63](https://sander.ai#fn:diffusiongemma)</sup>, an open-weights uniform-state DDLM developed by my colleagues at Google DeepMind, as well as NVIDIA’s [Nemotron Diffusion](https://research.nvidia.com/publication/2026-05_nemotron-labs-diffusion-tri-mode-language-model-unifying-autoregressive)<sup>[64](https://sander.ai#fn:nemotron)</sup>, also significantly increased awareness that autoregression is not the only game in town.

Step distillation of DDLMs is not a complete impossibility either: methods such as [discrete moment matching distillation](https://ehoogeboom.github.io/post/discrete_mmd_diffusion_language_models/) (D-MMD)<sup>[65](https://sander.ai#fn:dmmd)</sup> and inverse-distilled diffusion language models (IDLM)<sup>[66](https://sander.ai#fn:idlm)</sup> show that some approaches can be ported over from the continuous to the discrete setting.

It is worth noting that displacing autoregression entirely is not the only way for diffusion language models to be successful. They can coexist, sometimes even within the same system. A common strategy to accelerate sampling from autoregressive language models is speculative decoding, where a faster draft model is used to predict multiple tokens at a time, which can then be verified in parallel by the autoregressive model. **Discrete diffusion is increasingly being used for drafting** in this context (e.g. DFlash<sup>[67](https://sander.ai#fn:dflash)</sup>).

A different perspective on the same idea is that autoregressive verification can be used to mitigate the impact of independence assumptions in few-step discrete diffusion sampling<sup>[68](https://sander.ai#fn:fefdllm)</sup>. DMax<sup>[69](https://sander.ai#fn:dmax)</sup> uses a combination of continuous relaxations and post-training to reduce the impact of these independence assumptions instead.

In the meantime, some recent works have continued to explore hybrid continuous-discrete approaches. Sticky Jump Diffusions<sup>[70](https://sander.ai#fn:sticky)</sup> are an attempt to create a unified view of hybrid methods, building on the SDE formalism, with both discrete masked diffusion and continuous diffusion as special cases. Posterior Refinement<sup>[71](https://sander.ai#fn:posterior)</sup> wraps continuous diffusion within masked diffusion. This creates a nested sampling loop, where the inner loop can be distilled down to very few steps using [flow map methods](https://sander.ai/2026/05/06/flow-maps.html). This results in a form of masked diffusion where each step can also capture correlations between simultaneously unmasked tokens (unlike standard masked diffusion, which assumes their conditional independence).

### 

The current trend of diffusion language models moving into the mainstream shows no signs of slowing down. Whether discrete or continuous methods will come to dominate is hard to predict – perhaps they will coexist, alongside autoregression. As the LLM community moved on from the Chinchilla perspective (focusing exclusively on training efficiency), alternative modelling paradigms have gradually received more attention, which diffusion language models are undoubtedly benefiting from. In the longer term, another aspect of diffusion models may gain importance: their increased data efficiency relative to autoregression<sup>[72](https://sander.ai#fn:dataconstrained)</sup>.

In the meantime, I believe it is crucial for the research community to work to address a common weakness of diffusion language modelling papers: the **evaluation methodology**. Because of their flexible sampling procedure, diffusion models are particularly amenable to tuning the trade-off between quality and diversity at sampling time. If this trade-off is not carefully quantified and accounted for, this can lead to certain models appearing to be significantly better than others, even if they merely represent different points along this trade-off. Because the evaluation methodology is not currently standardised, different papers use different approaches and results can be unintentionally misleading.

Moreover, because many formulations do not readily admit the estimation of likelihoods or perplexities under the models themselves, surrogate autoregressive models are often used to measure these instead (referred to as *generative perplexity*, GenPPL), which biases the evaluation towards the capabilities and weaknesses of the surrogates used.

Patrick Pynadath and colleagues suggest quantifying the trade-off by looking at *generative frontiers* (i.e. plotting perplexity vs. entropy) in [a recent blog post](https://patrickpynadath1.github.io/blog/eval_methodology/). Sam Acquaviva also has [a blog post](https://samacquaviva.com/projects/flow-evals/) identifying several diffusion language model evaluation issues and potential fixes. Franca and Tong<sup>[73](https://sander.ai#fn:genppl)</sup> demonstrate just how easy it is to game GenPPL as a metric, and argue that it should not be used even when entropies are matched. Metrics such as MAUVE<sup>[74](https://sander.ai#fn:mauve)</sup> were proposed to try and address the challenge of evaluating open-ended text generation, but ultimately still rely on pre-trained autoregressive models.

A research direction that continues to capture people’s imagination is **latent diffusion for language**: learning a higher-level and potentially more coarse-grained continuous representation for language that is easy to model with vanilla continuous diffusion. The main challenge here continues to be learning the latent space itself, not so much the diffusion part. As previously discussed in [my blog post on latent diffusion](https://sander.ai/2025/04/15/latents.html#modalities), language is a very different beast compared to perceptual signals, and representation learning techniques that work well for the latter might completely fail for the former.

Aside from LD4LG<sup>[21](https://sander.ai#fn:ld4lg)</sup> and LDLM<sup>[57](https://sander.ai#fn:ldlm)</sup> (previously mentioned), there has been a steady stream of work on learning higher-level language representations at the token, phrase, sentence or paragraph level, including Time Control<sup>[75](https://sander.ai#fn:timecontrol)</sup>, PLANNER<sup>[76](https://sander.ai#fn:planner)</sup>, Large Concept Models<sup>[77](https://sander.ai#fn:lcm)</sup>, Segment-level Diffusion<sup>[78](https://sander.ai#fn:sld)</sup>, LaDiR<sup>[79](https://sander.ai#fn:ladir)</sup>, Latent Thought Flows<sup>[80](https://sander.ai#fn:ltf)</sup> and AURORA-LM<sup>[81](https://sander.ai#fn:auroralm)</sup>. Mapping out this space would lead us too far, but this line of work cannot go unmentioned when talking about CDLMs, even if it is not the focus of this post.

## 

![](https://sander.ai/images/eclipse_sunset.jpg)

I wanted to write a quick note about the recent resurgence of CDLMs, given my earlier work in the space, my fondness for the idea, and my disappointment when DDLMs seemed to take over completely after 2023. Inevitably, it turned into an essay and a historical account of language diffusion research over the past five years – I just can’t seem to help myself 🤷. Some key takeaways to wrap up:

- As of this year, CDLMs are back on the menu, I believe primarily because of their **distillability advantage** . Step distillation enables faster sampling, but also creates new possibilities for post-training and steering during sampling.
- The level of interest in CDLMs relative to DDLMs has ebbed and flowed over the years, but currently it’s **high tide** ! Recent incarnations echo their predecessors, but extend and improve them in various ways (including but not limited to scaling up).
- There are a variety of approaches, and so far, **no clear convergence** on a particular recipe. This makes the space all the more exciting from a research perspective.
- For a while, there was an **implicit consensus** in the community that**DDLMs work better** than CDLMs at scale, but that seems to be waning. As with many things in machine learning, how strongly we collectively believe in an idea and how hard we try to make it work could significantly impact the outcome!
- To ensure that this direction of research continues to be taken seriously, sorting out the **evaluation methodology** will be crucial, as this is currently a weak point of many contributions in the space.

I also want to highlight a few upcoming **diffusion language modelling workshops**:

- [Non-Autoregressive Language Models for Fast & Flexible Text Generation](https://pengzhangzhi.github.io/NonAR-LM/) at COLM 2026 in San Francisco, USA
- [Diffusion Language Models: Foundations, Efficiency, and Reasoning](https://7amin.github.io/diffulm-neurips2026/) at NeurIPS 2026 in Sydney, Australia
- [Beyond Next‑Token Prediction — Diffusion & Flow Models for Next‑Generation Decoding](https://bento-neurips.github.io/) at NeurIPS 2026 in Sydney, Australia

The submission deadline for the NeurIPS workshops is in a few days! Thanks for reading, and as usual, please feel free to share your thoughts in the comments, on [Twitter](https://x.com/sedielem), or via email.

**Disclosure regarding the use of AI in producing this blog post**: I want to write in my own voice, and I want to respect everyone who takes the time to read what I write. Therefore, you will not find any passages or sentences in this post that are fully AI-generated. (Even the em dashes are all mine!) That said, I do occasionally consult AI when considering a particular turn of phrase, or to help me find the best wording (like a souped-up version of thesaurus.com). I primarily use it to help me understand papers and the relationship between them, and sometimes to create images and diagrams. AI was extensively used in the making of this blog post, but the prose is entirely ‘artisanal intelligence’. That is the level of AI involvement I am currently comfortable with.

*If you would like to cite this post in an academic context, you can use this BibTeX snippet:*

```
@misc{dieleman2026continuousdlms,
  author = {Dieleman, Sander},
  title = {Continuous diffusion language models},
  url = {https://sander.ai/2026/08/24/continuous-dlms.html},
  year = {2026}
}
```
## 

Many thanks to James Thornton, Oliver Wang, Sheel Shah, Jinwoo Kim, Justin Deschenaux, Patrick Pynadath, Oscar Davis, Luca Ambrogioni and Zhengyang Geng for sharing their thoughts and insights on this and many other topics. I’d also like to thank the organisers, other speakers and participants of the wonderful [EEML 2026 summer school](https://www.eeml.eu/) in Cetinje, Montenegro, and the ICML 2026 diffusion circle crew. As usual, thanks to my colleagues at Google DeepMind and the wider research community.

## 

1. 
      Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser and Polosukhin, “ [Attention is All you Need](http://papers.nips.cc/paper/7181-attention-is-all-you-need) ”, Advances in neural information processing systems 30 (NeurIPS), 2017.[↩](https://sander.ai#fnref:transformer)
2. 
      Williams, Zipser, “ [A learning algorithm for continually running fully recurrent neural networks](http://leech.cybernoid.gr/files/text/publications/A%20Learning%20Algorithm%20for%20Continually%20Running%20Fully%20Recurrent%20Neural%20Networks%20-%2010.1.1.52.9724.pdf) ”, Neural Computation, 1989.[↩](https://sander.ai#fnref:teacherforcing)
3. 
      Radford, Wu, Child, Luan, Amodei, Sutskever, “ [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) ”, OpenAI blog, 2019.[↩](https://sander.ai#fnref:gpt2)
4. 
      Song, Ermon, “ [Generative Modeling by Estimating Gradients of the Data Distribution](https://arxiv.org/abs/1907.05600) ”, Neural Information Processing Systems, 2019.[↩](https://sander.ai#fnref:score)[↩<sup>2</sup>](https://sander.ai#fnref:score:1)
5. 
      Song, Ermon, “ [Improved Techniques for Training Score-Based Generative Models](https://arxiv.org/abs/2006.09011) ”, Neural Information Processing Systems, 2020.[↩](https://sander.ai#fnref:improvedscore)
6. 
      Ho, Jain, Abbeel, “ [Denoising Diffusion Probabilistic Models](https://proceedings.neurips.cc/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html) ”, 2020.[↩](https://sander.ai#fnref:ddpm)[↩<sup>2</sup>](https://sander.ai#fnref:ddpm:1)
7. 
      Hoogeboom, Nielsen, Jaini, Forré, Welling, “ [Argmax Flows and Multinomial Diffusion: Learning Categorical Distributions](https://arxiv.org/abs/2102.05379) ”, Neural Information Processing Systems, 2021.[↩](https://sander.ai#fnref:multinomial)
8. 
      Austin, Johnson, Ho, Tarlow, van den Berg, “ [Structured Denoising Diffusion Models in Discrete State-Spaces](https://arxiv.org/abs/2107.03006) ”, Neural Information Processing Systems, 2021.[↩](https://sander.ai#fnref:d3pm)
9. 
      Savinov, Chung, Binkowski, Elsen, van den Oord, “ [Step-unrolled Denoising Autoencoders for Text Generation](https://arxiv.org/abs/2112.06749) ”, International Conference on Learning Representations, 2022.[↩](https://sander.ai#fnref:sundae)
10. 
      Brown, Mann, Ryder, Subbiah, Kaplan, Dhariwal, Neelakantan, Shyam, Sastry, Askell, Agarwal, Herbert-Voss, Krueger, Henighan, Child, Ramesh, Ziegler, Wu, Winter, Hesse, Chen, Sigler, Litwin, Gray, Chess, Clark, Berner, McCandlish, Radford, Sutskever, Amodei, “ [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) ”, Neural Information Processing Systems, 2020.[↩](https://sander.ai#fnref:gpt3)
11. 
      Ghazvininejad, Levy, Liu, Zettlemoyer, “ [Mask-Predict: Parallel Decoding of Conditional Masked Language Models](https://arxiv.org/abs/1904.09324) ”, Empirical Methods in Natural Language Processing, 2019.[↩](https://sander.ai#fnref:maskpredict)
12. 
      Yang, Dai, Yang, Carbonell, Salakhutdinov, Le, “ [XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://arxiv.org/abs/1906.08237) ”, Neural Information Processing Systems, 2019.[↩](https://sander.ai#fnref:xlnet)
13. 
      Gu, Bradbury, Xiong, Li, Socher, “ [Non-Autoregressive Neural Machine Translation](https://arxiv.org/abs/1711.02281) ”, International Conference on Learning Representations, 2018.[↩](https://sander.ai#fnref:nat)
14. 
      Lee, Mansimov, Cho, “ [Deterministic Non-Autoregressive Neural Sequence Modeling by Iterative Refinement](https://arxiv.org/abs/1802.06901) ”, Empirical Methods in Natural Language Processing, 2018.[↩](https://sander.ai#fnref:iternat)
15. 
      Li, Thickstun, Gulrajani, Liang, Hashimoto, “ [Diffusion-LM Improves Controllable Text Generation](https://arxiv.org/abs/2205.14217) ”, Neural Information Processing Systems, 2022.[↩](https://sander.ai#fnref:diffusionlm)[↩<sup>2</sup>](https://sander.ai#fnref:diffusionlm:1)[↩<sup>3</sup>](https://sander.ai#fnref:diffusionlm:2)
16. 
      Gong, Li, Feng, Wu, Kong, “ [DiffuSeq: Sequence to Sequence Text Generation with Diffusion Models](https://arxiv.org/abs/2210.08933) ”, International Conference on Learning Representations, 2023.[↩](https://sander.ai#fnref:diffuseq)
17. 
      Han, Kumar, Tsvetkov, “ [SSD-LM: Semi-autoregressive Simplex-based Diffusion Language Model for Text Generation and Modular Control](https://arxiv.org/abs/2210.17432) ”, Association for Computational Linguistics, 2023.[↩](https://sander.ai#fnref:ssdlm)[↩<sup>2</sup>](https://sander.ai#fnref:ssdlm:1)
18. 
      Gao, Guo, Tan, Zhu, Zhang, Bian, Xu, “ [Difformer: Empowering Diffusion Model on Embedding Space for Text Generation](https://arxiv.org/abs/2212.09412) ”, arXiv, 2022.[↩](https://sander.ai#fnref:difformer)
19. 
      Yuan, Yuan, Tan, Huang, Huang, “ [SeqDiffuSeq: Text Diffusion with Encoder-Decoder Transformers](https://arxiv.org/abs/2212.10325) ”, Association for Computational Linguistics, 2024.[↩](https://sander.ai#fnref:seqdiffuseq)
20. 
      Lin, Gong, Shen, Wu, Fan, Lin, Duan, Chen, “ [Text Generation with Diffusion Language Models: A Pre-training Approach with Continuous Paragraph Denoise](https://arxiv.org/abs/2212.11685) ”, International Conference on Machine Learning, 2023.[↩](https://sander.ai#fnref:genie)
21. 
      Lovelace, Kishore, Wan, Shekhtman, Weinberger, “ [Latent Diffusion for Language Generation](https://arxiv.org/abs/2212.09462) ”, Neural Information Processing Systems, 2023.[↩](https://sander.ai#fnref:ld4lg)[↩<sup>2</sup>](https://sander.ai#fnref:ld4lg:1)[↩<sup>3</sup>](https://sander.ai#fnref:ld4lg:2)[↩<sup>4</sup>](https://sander.ai#fnref:ld4lg:3)
22. 
      Strudel, Tallec, Altché, Du, Ganin, Mensch, Grathwohl, Savinov, Dieleman, Sifre, Leblond, “ [Self-conditioned Embedding Diffusion for Text Generation](https://arxiv.org/abs/2211.04236) ”, arXiv, 2022.[↩](https://sander.ai#fnref:sed)[↩<sup>2</sup>](https://sander.ai#fnref:sed:1)[↩<sup>3</sup>](https://sander.ai#fnref:sed:2)[↩<sup>4</sup>](https://sander.ai#fnref:sed:3)
23. 
      Dieleman, Sartran, Roshannai, Savinov, Ganin, Richemond, Doucet, Strudel, Dyer, Durkan, Hawthorne, Leblond, Grathwohl, Adler, “ [Continuous diffusion for categorical data](https://arxiv.org/abs/2211.15089) ”, arXiv, 2022.[↩](https://sander.ai#fnref:cdcd)[↩<sup>2</sup>](https://sander.ai#fnref:cdcd:1)[↩<sup>3</sup>](https://sander.ai#fnref:cdcd:2)[↩<sup>4</sup>](https://sander.ai#fnref:cdcd:3)[↩<sup>5</sup>](https://sander.ai#fnref:cdcd:4)[↩<sup>6</sup>](https://sander.ai#fnref:cdcd:5)[↩<sup>7</sup>](https://sander.ai#fnref:cdcd:6)
24. 
      Li, Chen, Guo, Shen, “ [A Survey on Diffusion Language Models](https://arxiv.org/abs/2508.10875) ”, arXiv, 2025.[↩](https://sander.ai#fnref:survey)
25. 
      Gulrajani, Hashimoto, “ [Likelihood-Based Diffusion Language Models](https://arxiv.org/abs/2305.18619) ”, Neural Information Processing Systems, 2023.[↩](https://sander.ai#fnref:plaid)[↩<sup>2</sup>](https://sander.ai#fnref:plaid:1)[↩<sup>3</sup>](https://sander.ai#fnref:plaid:2)
26. 
      Hoffmann, Borgeaud, Mensch, Buchatskaya, Cai, Rutherford, de Las Casas, Hendricks, Welbl, Clark, Hennigan, Noland, Millican, van den Driessche, Damoc, Guy, Osindero, Simonyan, Elsen, Rae, Vinyals, Sifre, “ [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) ”, Neural Information Processing Systems, 2022.[↩](https://sander.ai#fnref:chinchilla)
27. 
      Touvron, Lavril, Izacard, Martinet, Lauchaux, Lacroix, Rozière, Goyal, Hambro, Azhar, Rodriguez, Joulin, Grave, Lample, “ [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971) ”, arXiv, 2023.[↩](https://sander.ai#fnref:llama)
28. 
      Chen, Zhang, Hinton, “ [Analog Bits: Generating Discrete Data using Diffusion Models with Self-Conditioning](https://arxiv.org/abs/2208.04202) ”, International Conference on Learning Representations, 2023.[↩](https://sander.ai#fnref:analogbits)[↩<sup>2</sup>](https://sander.ai#fnref:analogbits:1)[↩<sup>3</sup>](https://sander.ai#fnref:analogbits:2)
29. 
      Devlin, Chang, Lee, Toutanova, “ [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) ”, North American Chapter of the Association for Computational Linguistics, 2019.[↩](https://sander.ai#fnref:bert)
30. 
      Yang, Guo, Zhang, Sahoo, Chen, Vahdat, Mardani, Thickstun, “ [Continuous Diffusion Scales Competitively with Discrete Diffusion for Language](https://arxiv.org/abs/2605.18530) ”, arXiv, 2026.[↩](https://sander.ai#fnref:replaid)[↩<sup>2</sup>](https://sander.ai#fnref:replaid:1)
31. 
      Kingma and Welling, “ [Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114) ”, International Conference on Learning Representations, 2014.[↩](https://sander.ai#fnref:vaekingma)
32. 
      Rezende, Mohamed and Wierstra, “ [Stochastic Backpropagation and Approximate Inference in Deep Generative Models](https://arxiv.org/abs/1401.4082) ”, International Conference on Machine Learning, 2014.[↩](https://sander.ai#fnref:vaerezende)
33. 
      Richemond, Dieleman, Doucet, “ [Categorical SDEs with Simplex Diffusion](https://arxiv.org/abs/2210.14784) ”, ICML workshop on Sampling and Optimization in Discrete Space, 2023.[↩](https://sander.ai#fnref:simplex)[↩<sup>2</sup>](https://sander.ai#fnref:simplex:1)
34. 
      Avdeyev, Shi, Tan, Dudnyk, Zhou, “ [Dirichlet Diffusion Score Model for Biological Sequence Generation](https://arxiv.org/abs/2305.10699) ”, International Conference on Machine Learning, 2023.[↩](https://sander.ai#fnref:ddsm)
35. 
      Floto, Jonsson, Nica, Sanner, Zhu, “ [Diffusion on the Probability Simplex](https://arxiv.org/abs/2309.02530) ”, International Conference on Machine Learning, 2023.[↩](https://sander.ai#fnref:floto)
36. 
      Stark, Jing, Wang, Corso, Berger, Barzilay, Jaakkola, “ [Dirichlet Flow Matching with Applications to DNA Sequence Design](https://arxiv.org/abs/2402.05841) ”, International Conference on Machine Learning, 2024.[↩](https://sander.ai#fnref:dirichletfm)
37. 
      Kingma, Salimans, Poole, Ho, “ [Variational Diffusion Models](https://arxiv.org/abs/2107.00630) ”, Neural Information Processing Systems, 2021.[↩](https://sander.ai#fnref:vdm)
38. 
      Raya, Nguyen, Batzolis, Takida, Stancevic, Murata, Lai, Mitsufuji, Ambrogioni, “ [Noise Scheduling as Information-Guided Allocation in Diffusion Training](https://arxiv.org/abs/2602.18647) ”, ICML workshop on Structured Probabilistic Inference & Generative Modelling, 2026.[↩](https://sander.ai#fnref:infonoise)
39. 
      Lee, Yoo, Agarwal, Shah, Huang, Raghunathan, Hong, Boffi, Kim, “ [Flow Map Language Models: One-step Language Modeling via Continuous Denoising](https://arxiv.org/abs/2602.16813) ”, arXiv, 2026.[↩](https://sander.ai#fnref:fmlm)[↩<sup>2</sup>](https://sander.ai#fnref:fmlm:1)
40. 
      Song, Sohl-Dickstein, Kingma, Kumar, Ermon and Poole, “ [Score-Based Generative Modeling through Stochastic Differential Equations](https://arxiv.org/abs/2011.13456) ”, International Conference on Learning Representations, 2021.[↩](https://sander.ai#fnref:sde)[↩<sup>2</sup>](https://sander.ai#fnref:sde:1)
41. 
      Jabri, Fleet, Chen, “ [Scalable Adaptive Compute for Iterative Generation](https://arxiv.org/abs/2212.11972) ”, International Conference on Machine Learning, 2023.[↩](https://sander.ai#fnref:rin)
42. 
      Yoo, Kim, Eijkelboom, Lee, Boffi, Hong, Kim, “ [Self-conditioned Flow Map Language Models via Fixed-point Flows](https://arxiv.org/abs/2607.00714) ”, arXiv, 2026.[↩](https://sander.ai#fnref:fpf)
43. 
      Cox, Ingersoll, Ross, “ [A theory of the term structure of interest rates](https://www.jstor.org/stable/1911242) ”, Econometrica, 1985.[↩](https://sander.ai#fnref:cir)
44. 
      Lipman, Chen, Ben-Hamu, Nickel, Le, “ [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747) ”, International Conference on Learning Representations, 2023.[↩](https://sander.ai#fnref:flowmatching)[↩<sup>2</sup>](https://sander.ai#fnref:flowmatching:1)
45. 
      Boffi, Albergo, Vanden-Eijnden, “ [Flow map matching with stochastic interpolants: A mathematical framework for consistency models](https://arxiv.org/abs/2406.07507) ”, Transactions on Machine Learning Research, 2025.[↩](https://sander.ai#fnref:fmm)[↩<sup>2</sup>](https://sander.ai#fnref:fmm:1)
46. 
      Sahoo, Deschenaux, Gokaslan, Wang, Chiu, Kuleshov, “ [The Diffusion Duality](https://arxiv.org/abs/2506.10892) ”, International Conference on Machine Learning, 2025.[↩](https://sander.ai#fnref:duo)
47. 
      Song, Dhariwal, Chen, Sutskever, “ [Consistency Models](https://arxiv.org/abs/2303.01469) ”, International Conference on Machine Learning, 2023.[↩](https://sander.ai#fnref:cm)
48. 
      Zheng, Gong, Zhang, Chen, Gu, Zhou, Jaitly, Zhang, “ [Continuously Augmented Discrete Diffusion model for Categorical Generative Modeling](https://arxiv.org/abs/2510.01329) ”, International Conference on Learning Representations, 2026.[↩](https://sander.ai#fnref:cadd)
49. 
      Zhou, Yang, Hu, Wang, Zhang, Zhang, Mackey, Jaakkola, Bates, Zhang, “ [Coevolutionary Continuous Discrete Diffusion: Make Your Diffusion Language Model a Latent Reasoner](https://arxiv.org/abs/2510.03206) ”, International Conference on Machine Learning, 2026.[↩](https://sander.ai#fnref:ccdd)
50. 
      Pynadath, Shi, Zhang, “ [CANDI: Hybrid Discrete-Continuous Diffusion Models](https://arxiv.org/abs/2510.22510) ”, International Conference on Machine Learning, 2026.[↩](https://sander.ai#fnref:candi)
51. 
      Boffi, Albergo, Vanden-Eijnden, “ [How to build a consistency model: Learning flow maps via self-distillation](https://arxiv.org/abs/2505.18825) ”, Neural Information Processing Systems, 2025.[↩](https://sander.ai#fnref:selfdist)
52. 
      Roos, Davis, Eijkelboom, Bronstein, Welling, Ceylan, Ambrogioni, van de Meent, “ [Categorical Flow Maps](https://arxiv.org/abs/2602.12233) ”, arXiv, 2026.[↩](https://sander.ai#fnref:cfm)
53. 
      Potaptchik, Yim, Saravanan, Holderrieth, Vanden-Eijnden, Albergo, “ [Discrete Flow Maps](https://arxiv.org/abs/2604.09784) ”, arXiv, 2026.[↩](https://sander.ai#fnref:dfm)
54. 
      Chen, Liang, Sui, Guo, Cheng, You, Liu, “ [LangFlow: Continuous Diffusion Rivals Discrete in Language Modeling](https://arxiv.org/abs/2604.11748) ”, arXiv, 2026.[↩](https://sander.ai#fnref:langflow)
55. 
      Chemseddine, Kornhardt, Steidl, “ [Spherical Flows for Sampling Categorical Data](https://arxiv.org/abs/2605.05629) ”, arXiv, 2026.[↩](https://sander.ai#fnref:sf)
56. 
      Deschenaux, Gulcehre, “ [Language Modelling with Hyperspherical Flows](https://arxiv.org/abs/2605.11125) ”, arXiv, 2026.[↩](https://sander.ai#fnref:hsf)
57. 
      Meschaninov, Shabalin, Chimbulatov, Gushchin, Koziev, Korotin, Vetrov, “ [How to Train Your Latent Diffusion Language Model Jointly With the Latent Space](https://arxiv.org/abs/2605.07933) ”, arXiv, 2026.[↩](https://sander.ai#fnref:ldlm)[↩<sup>2</sup>](https://sander.ai#fnref:ldlm:1)
58. 
      Hu, Qiu, Lu, Zhao, Li, Kim, Andreas, He, “ [ELF: Embedded Language Flows](https://arxiv.org/abs/2605.10938) ”, arXiv, 2026.[↩](https://sander.ai#fnref:elf)
59. 
      Batzolis, Girolami, Ambrogioni, “ [CoBit: Language Modeling with Bitstream Diffusion](https://arxiv.org/abs/2605.07013) ”, arXiv, 2026.[↩](https://sander.ai#fnref:cobit)
60. 
      Davis, Filippova, Ablin, Turrisi, Shidani, Cuturi, Béthune, “ [Scaling Categorical Flow Maps](https://arxiv.org/abs/2605.07820) ”, arXiv, 2026.[↩](https://sander.ai#fnref:scalingcfms)
61. 
      Chen, Monso, Du, Simchowitz, Tedrake, Sitzmann, “ [Diffusion Forcing: Next-token Prediction Meets Full-Sequence Diffusion](https://arxiv.org/abs/2407.01392) ”, Neural Information Processing Systems, 2024.[↩](https://sander.ai#fnref:diffusionforcing)
62. 
      Zhou, Yu, Babu, Tirumala, Yasunaga, Shamis, Kahn, Ma, Zettlemoyer, Levy, “ [Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model](https://arxiv.org/abs/2408.11039) ”, International Conference on Learning Representations, 2025.[↩](https://sander.ai#fnref:transfusion)
63. 
      DiffusionGemma team, “ [DiffusionGemma Technical Report](https://arxiv.org/abs/2608.00146) ”, arXiv, 2026.[↩](https://sander.ai#fnref:diffusiongemma)
64. 
      Fu, Whalen, Garg, Wu, Khadkevich, Oswald, Xie, Egert, Sreenivas, Diao, Yu, Yu, Chen, Norouzi, Liu, Lan, Zhu, Wang, Jiang, Mardani, Maghoumi, Han, Jukić, Tajbakhsh, Kautz, Molchanov, “ [Nemotron-Labs-Diffusion: A Tri-Mode Language Model Unifying Autoregressive, Diffusion, and Self-Speculation Decoding](https://arxiv.org/abs/2607.05722) ”, arXiv, 2026.[↩](https://sander.ai#fnref:nemotron)
65. 
      Hoogeboom, Ruhe, Heek, Mensink, Salimans, “ [Beyond Single Tokens: Distilling Discrete Diffusion Models via Discrete MMD](https://arxiv.org/abs/2603.20155) ”, arXiv, 2026.[↩](https://sander.ai#fnref:dmmd)
66. 
      Li, Gushchin, Abulkhanov, Moulines, Osedelets, Panov, Korotin, “ [IDLM: Inverse-distilled Diffusion Language Models](https://arxiv.org/abs/2602.19066) ”, International Conference on Machine Learning, 2026.[↩](https://sander.ai#fnref:idlm)
67. 
      Chen, Liang, Liu, “ [DFlash: Block Diffusion for Flash Speculative Decoding](https://arxiv.org/abs/2602.06036) ”, International Conference on Machine Learning, 2026.[↩](https://sander.ai#fnref:dflash)
68. 
      Fang, Li, Yuan, Yu, “ [Factorization-Error-Free Discrete Diffusion Language Model via Speculative Decoding](https://arxiv.org/abs/2605.14305) ”, arXiv, 2026.[↩](https://sander.ai#fnref:fefdllm)
69. 
      Chen, Fang, Ma, Yu, Wang, “ [DMax: Aggressive Parallel Decoding for dLLMs](https://arxiv.org/abs/2604.08302) ”, arXiv, 2026.[↩](https://sander.ai#fnref:dmax)
70. 
      Jutras-Dubé, Pynadath, Lu, Gao, Zhang, “ [Sticky Jump Diffusions: A Unifying View of Masked, Continuous, and Hybrid Diffusion](https://arxiv.org/abs/2607.10951) ”, arXiv, 2026.[↩](https://sander.ai#fnref:sticky)
71. 
      Agarwal, Shah, Lee, Yoo, Huang, Hong, Raghunathan, Kim, Boffi, “ [Posterior Refinement: Fast Language Generation via Any-Order Flow Maps](https://arxiv.org/abs/2606.24773) ”, arXiv, 2026.[↩](https://sander.ai#fnref:posterior)
72. 
      Prabhudesai, Wu, Zadeh, Fragkiadaki, Pathak, “ [Diffusion Beats Autoregressive in Data-Constrained Settings](https://arxiv.org/abs/2507.15857) ”, Neural Information Processing Systems, 2025.[↩](https://sander.ai#fnref:dataconstrained)
73. 
      Franca, Tong, “ [Hacking Generative Perplexity: Why Unconditional Text Evaluation Needs Distributional Metrics](https://arxiv.org/abs/2606.08417) ”, arXiv, 2026.[↩](https://sander.ai#fnref:genppl)
74. 
      Pillutla, Swayamdipta, Zellers, Thickstun, Welleck, Choi, Harchaoui, “ [MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers](https://arxiv.org/abs/2102.01454) ”, Neural Information Processing Systems, 2021.[↩](https://sander.ai#fnref:mauve)
75. 
      Wang, Durmus, Goodman, Hashimoto, “ [Language modeling via stochastic processes](https://arxiv.org/abs/2203.11370) ”, International Conference on Learning Representations, 2022.[↩](https://sander.ai#fnref:timecontrol)
76. 
      Zhang, Gu, Wu, Zhai, Susskind, Jaitly, “ [PLANNER: Generating Diversified Paragraph via Latent Language Diffusion Model](https://arxiv.org/abs/2306.02531) ”, Neural Information Processing Systems, 2023.[↩](https://sander.ai#fnref:planner)
77. 
      Barrault, Duquenne, Elbayad, Kozhevnikov, Alastruey, Andrews, Coria, Couairon, Costa-jussà, Dale, Elsahar, Heffernan, Janeiro, Tran, Ropers, Sánchez, San Roman, Mourachko, Saleem, Schwenk, “ [Large Concept Models: Language Modeling in a Sentence Representation Space](https://arxiv.org/abs/2412.08821) ”, arXiv, 2024.[↩](https://sander.ai#fnref:lcm)
78. 
      Zhu, Karadzhov, Whitehouse, Vlachos, “ [Segment-Level Diffusion: A Framework for Controllable Long-Form Generation with Diffusion Language Models](https://arxiv.org/abs/2412.11333) ”, Association for Computational Linguistics, 2025.[↩](https://sander.ai#fnref:sld)
79. 
      Kang, Zhang, Kuang, Majamaki, Jaitly, Ma, Qin, “ [LaDiR: Latent Diffusion Enhances LLMs for Text Reasoning](https://arxiv.org/abs/2510.04573) ”, International Conference on Learning Representations, 2026.[↩](https://sander.ai#fnref:ladir)
80. 
      Prabhudesai, Geng, “ [Latent Thought Flows with Text Compression](https://latent-thought-flows.vercel.app/) ”, blog, 2026.[↩](https://sander.ai#fnref:ltf)
81. 
      Liang, Liao, Cao, Wei, Li, Tan, Zhang, Cui, Yang, Guo, Yang, Yang, Shan, Liu, Si, “ [AURORA-LM: Autoencoding Unified Representation for Continuous-Latent Diffusion Language Modeling](https://arxiv.org/abs/2608.02602) ”, arXiv, 2026.[↩](https://sander.ai#fnref:auroralm)
