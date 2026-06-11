---
title: "Cohere Launched an Agentic Coding Model"
source: TLDR AI · 2026-06-10
url: https://cohere.com/blog/north-mini-code?utm_source=tldrai
date: 2026-06-11
published_at: 2026-06-10T12:00:00+00:00
tag: 工具开源
item_id: 2e17dc0942acbec4
---
Today we're launching North Mini Code open-source. A mixture-of-experts (MoE) model, North Mini Code is Cohere's first agentic coding model, and the inaugural member of our next generation of powerful models.

At 30B total parameters with just 3B active, North Mini Code delivers strong software development performance without demanding extensive hardware to match. Efficient by design, it's built to run where you need it.

Freely available under an [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0?_gl=1*gri8sk*_gcl_au*MjU0OTU5MzQwLjE3Nzk4MDczMTc.) license, North Mini Code advances Cohere’s mission to make sovereign AI a practical reality, giving developers direct access to agentic coding capabilities. We're building in the open, because the future of AI should be shaped by the people running, testing, and improving it.

Download the weights on [Hugging Face](https://huggingface.co/CohereLabs/North-Mini-Code-1.0), or deploy in a dedicated, managed inference environment on [Model Vault](https://dashboard.cohere.com/welcome/login). Alternatively, try it for free in your harness of choice on [OpenCode](https://opencode.ai/) or with a [Cohere API key](https://dashboard.cohere.com/). Share what you build and tag @ Cohere on [X](https://x.com/cohere) or [Discord](https://discord.com/invite/co-mmunity), or engage with us on [Reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tylzy2/coheres_unreleased_coding_model_early_access_for/). 

##### Snapshot

| Model | North-Mini-Code-1.0 | 
|---|---|
| License | Apache 2.0 | 
| Model size | 30B total; 3B active | 
| Context length | 256K total context; 64K max generation | 
| Optimized for | Code generation, agentic software engineering, and terminal tasks | 
| Availability | Hugging Face (Weights), Cohere API, Cohere Model Vault, OpenRouter | 
| Hardware (minimum) | 1× H100 @ FP8 | 

##### Agentic coding capabilities

North Mini Code achieves competitive scores across benchmarks against models of this size class, demonstrating strong performance in real-world software engineering tasks.

![Benchmarks comparing North Mini Code to leading open-source models of small sizes.](https://cdn.sanity.io/images/rjtqmwfu/web3-prod/06e7b98d2b53bf7ca8b7dfa53d758991a031c2e5-3140x2400.png?auto=format&fit=max&q=90&w=1570)

North Mini Code’s benchmark scores [translate to a 33.4 on the Artificial Analysis Coding Index](https://artificialanalysis.ai/models/north-mini-code), a competitive position among similarly sized models.

##### The speed advantage for developer tasks

North Mini Code is designed for speed and efficiency, with a strong focus on minimizing total cost of ownership as we continue to refine and scale the model.

In our testing, North Mini Code achieved up to 2.8x higher output throughput than Devstral Small 2 under identical concurrency levels and hardware configurations. In practical terms, that translates to nearly three times the work rate, enabling faster iteration while reducing computational overhead.

North Mini Code also demonstrated a 30% advantage in inter-token latency, a metric that reflects the consistency and pacing of token generation. Time-to-first-token (TTFT) performance was more closely matched between the two models, with Devstral Small 2 maintaining a slight edge across the tested conditions.

![](https://cdn.sanity.io/images/rjtqmwfu/web3-prod/fd68dfc478f63ca564dd882daadc4004d57d6732-3140x1792.png?auto=format&fit=max&q=90&w=1570)

##### Sovereign open models for developers

North Mini Code is our first open-source model for developers. As coding agents transform software engineering, developers need control and flexibility over their agentic coding infrastructure.

North Mini Code represents a step forward in small agentic coding models that can accomplish tasks that matter to developers. Specifically, it is built for agentic workflows, including understanding and orchestrating sub-agents, mapping systems architecture, and running code reviews. Deploy on-prem or locally, on your own terms.

Community feedback will directly shape our roadmap as we expand the ecosystem toward more open and sovereign developer models. Try North Mini Code when you need freedom from vendor constraints, and help us build what's next.

##### What’s next?

North Mini Code launches as the first—but certainly not the last—of Cohere's new generation of powerful models, designed for a more sovereign open-source ecosystem.

We're committed to increasing our capabilities, with community input informing what comes next.

##### Getting started

Help us build a complete sovereign AI ecosystem for software development by trying North Mini Code. North Mini Code is available for free on [Hugging Face](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)  and [Model Vault](https://dashboard.cohere.com/welcome/login?_gl=1*uxjn5q*_gcl_au*MjA0ODIxMjk3My4xNzgwOTUxMzc0*_ga*NzE2NDY3MTkyLjE3ODA5NTEzNzQ.*_ga_CRGS116RZS*czE3ODA5NTEzNzMkbzEkZzAkdDE3ODA5NTEzNzQkajU5JGwwJGgw)—our fully managed inference platform. We've specifically trained it for compatibility with [OpenCode](https://opencode.ai/), but it works with most coding agents.

Share what you build and tag @ Cohere on [X](https://x.com/cohere) or [Discord](https://discord.com/invite/co-mmunity), or engage with us on [Reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tylzy2/coheres_unreleased_coding_model_early_access_for/) to help shape the future of sovereign models.

Visit our [documentation](https://docs.cohere.com/docs/north-mini-code-1.0) for detailed model specs, deployment guides, and cookbooks to get started.

1 We used publicly reported scores for competitor models either from original reports or Artificial Analysis Intelligence Index where available. Additionally, Gemma 4’s scores for agentic coding tasks were reported by [Qwen team](https://qwen.ai/blog?id=qwen3.6-35b-a3b). For the benchmark results that any public report is missing denoted by (*) in Image 1, we run internally with recommended model configuration.

2 We evaluated North Mini Code using “SWE-agent” harness for SWE-Bench Verified and SWE-Bench Pro, and a simple ReAct harness employing a single terminal-use tool for Terminal Bench v2. For Terminal Bench Hard, we used Terminus-2 harness for both North Mini Code and the other models that are evaluated internally.
