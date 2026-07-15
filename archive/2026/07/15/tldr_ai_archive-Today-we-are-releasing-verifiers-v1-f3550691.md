---
title: "Today, we are releasing verifiers v1"
source: TLDR AI · 2026-07-14
url: https://threadreaderapp.com/thread/2076447247693402301.html?utm_source=tldrai
date: 2026-07-15
published_at: 2026-07-14T12:00:00+00:00
tag: 工具开源
item_id: f355069162feeb1d
---
**
              
              This Thread may be Removed Anytime!**
          

Twitter may remove this content at anytime! Save it as PDF for later use!

- Follow [@ThreadReaderApp](https://twitter.com/threadreaderapp)to mention us!
- From a Twitter thread mention us with a keyword "unroll"

`@threadreaderapp unroll`
          [Practice here](https://twitter.com/threadreaderapp/status/1054877865362112513) first or read more on our [help page](https://threadreaderapp.com/help)!

The next wave of AI will not be won by better prompts. It will be won by systems that learn from experience.


Today, Prime Intellect Lab is out of beta, open for you to start training your own models.


The era of self-improving agents is here.

          Today, Prime Intellect Lab is out of beta, open for you to start training your own models.

The era of self-improving agents is here.

Previously, improving a model meant waiting on the frontier labs.


Lab brings the model improvement engine right to you:


Build. Evaluate. Train. Deploy.![Image](/images/1px.png)


          Lab brings the model improvement engine right to you:

Build. Evaluate. Train. Deploy.

Lab is launching with self-serve support for models from Nvidia, OpenAI, Meta, Qwen, with more coming soon.


Models range from 1B to 400B parameters covering both dense and MoE architectures, reasoning and non-reasoning modes, and text and image modalities.![Image](/images/1px.png)


      Models range from 1B to 400B parameters covering both dense and MoE architectures, reasoning and non-reasoning modes, and text and image modalities.

Over the past months, Cohort I of our RL Residency has been shipping.


Highlights

- continual learning

- automating AI research (from GPU programming to RL itself)

- embodied environments

- multi-agent systems

- materials science discovery

          Highlights

- continual learning

- automating AI research (from GPU programming to RL itself)

- embodied environments

- multi-agent systems

- materials science discovery

CARLA-Env – @myainotez


An open-source embodied RL environment based on the CARLA simulator. It provides high-fidelity physics, sensors, and configurable urban scenarios for training and evaluating decision-making agents.


Blog:[blog.sinatras.dev/Carla-EnvEnvir…](https://blog.sinatras.dev/Carla-EnvEnvironment): [app.primeintellect.ai/dashboard/envi…](https://app.primeintellect.ai/dashboard/environments/sinatras/carla-env)

[x.com/myainotez/stat…](https://x.com/myainotez/status/2021296337233309986)

          An open-source embodied RL environment based on the CARLA simulator. It provides high-fidelity physics, sensors, and configurable urban scenarios for training and evaluating decision-making agents.

Blog:

PMPP-Eval – @myainotez


A dataset and RL environment based on the book “Programming Massively Parallel Processors,” focused on CUDA and GPU programming skills. Includes verifiable coding exercises and a frontier eval based on it.


Blog:[blog.sinatras.dev/PMPP-Eval+Jour…](https://blog.sinatras.dev/PMPP-Eval+Journey)


Environment:[app.primeintellect.ai/dashboard/envi…](https://app.primeintellect.ai/dashboard/environments/sinatras/pmpp)


[x.com/myainotez/stat…](https://x.com/myainotez/status/1979381611398316507)

      A dataset and RL environment based on the book “Programming Massively Parallel Processors,” focused on CUDA and GPU programming skills. Includes verifiable coding exercises and a frontier eval based on it.

Blog:

Environment:

Introducing Lab: A full-stack platform for training your own agentic models


Build, evaluate and train on your own environments at scale without managing the underlying infrastructure.


Giving everyone their own frontier AI lab.

          Build, evaluate and train on your own environments at scale without managing the underlying infrastructure.

Giving everyone their own frontier AI lab.

We are not inspired by a future where a few labs control the intelligence layer


So we built a platform to give everyone access to the tools of the frontier lab


If you are an AI company, you can now be your own AI lab


If you are an AI engineer, you can now be an AI researcher

          So we built a platform to give everyone access to the tools of the frontier lab

If you are an AI company, you can now be your own AI lab

If you are an AI engineer, you can now be an AI researcher

Lab unifies everything you need for post-training research into one platform


+ Environments Hub

+ Hosted Evaluations

+ Hosted Training

+ Deployments & Inference


Without needing to worry about the costs of massive GPU clusters or the headaches of low-level algorithm details![Image](/images/1px.png)


      + Environments Hub

+ Hosted Evaluations

+ Hosted Training

+ Deployments & Inference

Without needing to worry about the costs of massive GPU clusters or the headaches of low-level algorithm details

We're excited to introduce @arcee_ai's Trinity Large model.


An open 400B parameter Mixture of Experts model, delivering frontier-level performance with only 13B active parameters.


Trained in collaboration between Arcee, Datology and Prime Intellect.

          An open 400B parameter Mixture of Experts model, delivering frontier-level performance with only 13B active parameters.

Trained in collaboration between Arcee, Datology and Prime Intellect.

Trinity Architecture


Key design choices:

- Interleaved local + global attention (3:1 pattern)

- Grouped-query + gated attention

- New load-balancing method (SMEBU)

- Depth scaled sandwich norm and QK norm


With extreme sparsity, built for long context and fast inference.![Image](/images/1px.png)


          Key design choices:

- Interleaved local + global attention (3:1 pattern)

- Grouped-query + gated attention

- New load-balancing method (SMEBU)

- Depth scaled sandwich norm and QK norm

With extreme sparsity, built for long context and fast inference.

Infrastructure


- Large-scale synthetic data generation on ~2k H100s

- Training Trinity Large on 2k B300 GPUs


Training stack:

- Modified torchtitan

- Muon optimizer

- HSDP with FSDP group size 128

- Expert parallelism

- Context parallelism for context extension

- Improvements to recover quickly from hardware failures

      - Large-scale synthetic data generation on ~2k H100s

- Training Trinity Large on 2k B300 GPUs

Training stack:

- Modified torchtitan

- Muon optimizer

- HSDP with FSDP group size 128

- Expert parallelism

- Context parallelism for context extension

- Improvements to recover quickly from hardware failures

We believe the next breakthrough in long-horizon agents is training models to manage their own context.


Introducing our new research direction on Recursive Language Models.


We are sharing our initial experiments showing the promise of RLMs.


[primeintellect.ai/blog/rlm](https://www.primeintellect.ai/blog/rlm)

          Introducing our new research direction on Recursive Language Models.

We are sharing our initial experiments showing the promise of RLMs.

First introduced by @a1zhang in Oct 2025, the RLM has access to its inputs through a variable in a persistent Python REPL.


The model can inspect & transform that variable with code, and pipe parts of it into sub-LLMs with tools without ever loading the potentially huge input data into its context.![Image](/images/1px.png)


          The model can inspect & transform that variable with code, and pipe parts of it into sub-LLMs with tools without ever loading the potentially huge input data into its context.

RLMs are a simple, flexible form of context folding that doesn't depend on lossy summarization.


Instead, the model proactively delegates context to:


- Python scripts (search, filter, transform)

- Sub-LLMs (fresh instances) for parallel work

- Iterative answer edits until it's actually correct

      Instead, the model proactively delegates context to:

- Python scripts (search, filter, transform)

- Sub-LLMs (fresh instances) for parallel work

- Iterative answer edits until it's actually correct

Introducing INTELLECT-3: Scaling RL to a 100B+ MoE model on our end-to-end stack


Achieving state-of-the-art performance for its size across math, code and reasoning


Built using the same tools we put in your hands, from environments & evals, RL frameworks, sandboxes & more

          Achieving state-of-the-art performance for its size across math, code and reasoning

Built using the same tools we put in your hands, from environments & evals, RL frameworks, sandboxes & more

INTELLECT-3 is a 106B parameter Mixture-of-Experts model trained with both SFT and RL on top of the GLM 4.5 Air Base model.


Both stages, including multiple ablations, were carried out on a 512-GPU H200 cluster over the course of two months.![Image](/images/1px.png)


          Both stages, including multiple ablations, were carried out on a 512-GPU H200 cluster over the course of two months.

Our Training Stack


+ PRIME-RL: Our scalable, asynchronous RL trainer

+ Verifiers: Our unified library used for hundreds of envs and evals on the Environments Hub

+ Sandboxes: Custom container infra optimized for agentic RL

+ Compute: Orchestration & observability for 512 H200s

      + PRIME-RL: Our scalable, asynchronous RL trainer

+ Verifiers: Our unified library used for hundreds of envs and evals on the Environments Hub

+ Sandboxes: Custom container infra optimized for agentic RL

+ Compute: Orchestration & observability for 512 H200s
