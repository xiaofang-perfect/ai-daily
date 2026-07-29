---
title: "Releasing the model weights and technical report of Kimi K3"
source: TLDR AI · 2026-07-28
url: https://threadreaderapp.com/thread/2081760186235289764.html?utm_source=tldrai
date: 2026-07-29
published_at: 2026-07-28T12:00:00+00:00
tag: 工具开源
item_id: 41d7b318a2534ca4
---
**
              
              This Thread may be Removed Anytime!**
          

Twitter may remove this content at anytime! Save it as PDF for later use!

- Follow [@ThreadReaderApp](https://twitter.com/threadreaderapp)to mention us!
- From a Twitter thread mention us with a keyword "unroll"

`@threadreaderapp unroll`
          [Practice here](https://twitter.com/threadreaderapp/status/1054877865362112513) first or read more on our [help page](https://threadreaderapp.com/help)!

Feeling all the love for Kimi K3 already. Here are some of the amazing things people have been building with it. Enjoy K3.

          Built a fully functional macOS-style system with Kimi Agent Swarm.


          Animal Crossing with the cozy aesthetic, interactions, and gameplay loop.


      Introducing Kimi K3: Open Frontier Intelligence


🔹 2.8 Trillion Parameters, 1 Million Context, Native Multimodal

🔹 Kimi Delta Attention enables up to 6.3x faster decoding in million-token contexts

🔹 Attention Residuals deliver ~25% higher training efficiency at <2% additional cost

🔹 Built for long-horizon agentic coding and self-evolving workflows


Kimi K3 is now live on on[Kimi.com](http://Kimi.com), Kimi Work, Kimi Code, and the Kimi API.

Open Weights by July 27, 2026.


🔗 API:[platform.kimi.ai](http://platform.kimi.ai)

🔗 Tech blog:[kimi.com/blog/kimi-k3](http://kimi.com/blog/kimi-k3)![Image](/images/1px.png)


![Image](/images/1px.png)


          🔹 2.8 Trillion Parameters, 1 Million Context, Native Multimodal

🔹 Kimi Delta Attention enables up to 6.3x faster decoding in million-token contexts

🔹 Attention Residuals deliver ~25% higher training efficiency at <2% additional cost

🔹 Built for long-horizon agentic coding and self-evolving workflows

Kimi K3 is now live on on

Open Weights by July 27, 2026.

🔗 API:

🔗 Tech blog:

K3 is built on Kimi Delta Attention (KDA) and Attention Residuals (AttnRes), two architectural updates designed to improve how information flows across sequence length and model depth. 


We have also scaled up Mixture of Experts (MoE) sparsity, effectively activating 16 out of 896 experts when paired with a Stable LatentMoE framework.


Together with refined training and data recipes, these structural changes yield an approximate 2.5× improvement in overall scaling efficiency compared to K2, allowing the model to convert compute into intelligence more effectively.![Image](/images/1px.png)


          We have also scaled up Mixture of Experts (MoE) sparsity, effectively activating 16 out of 896 experts when paired with a Stable LatentMoE framework.

Together with refined training and data recipes, these structural changes yield an approximate 2.5× improvement in overall scaling efficiency compared to K2, allowing the model to convert compute into intelligence more effectively.

Internal knowledge work bench


Beyond public benchmarks, Kimi K3 Max also shows consistent gains on our internal benchmarks, which are built from recurring patterns and challenges in real-world user-agent workflows.


It scores 75.5 on Online Exp Bench, 73.5 on DECK-Bench, and 62.6 on Finance-Bench, outperforming Claude Opus 4.8 (max) and GPT-5.5 (xhigh) across all three.


These results reflect broad improvements in Kimi K3's agentic knowledge work capabilities, enabling more capable and reliable performance in real-world use cases.![Image](/images/1px.png)


      Beyond public benchmarks, Kimi K3 Max also shows consistent gains on our internal benchmarks, which are built from recurring patterns and challenges in real-world user-agent workflows.

It scores 75.5 on Online Exp Bench, 73.5 on DECK-Bench, and 62.6 on Finance-Bench, outperforming Claude Opus 4.8 (max) and GPT-5.5 (xhigh) across all three.

These results reflect broad improvements in Kimi K3's agentic knowledge work capabilities, enabling more capable and reliable performance in real-world use cases.

Meet Kimi Web Bridge - Kimi's browser extension.


Agent can now interact with websites like a human: search, scroll, click, type and complete tasks.


Supports Kimi Code CLI, Claude Code, Cursor, Codex, Hermes, and more.


Available now on and the Chrome Web Store.[kimi.com/features/webbr…](http://kimi.com/features/webbridge)

          Agent can now interact with websites like a human: search, scroll, click, type and complete tasks.

Supports Kimi Code CLI, Claude Code, Cursor, Codex, Hermes, and more.

Available now on and the Chrome Web Store.

Search across multiple platforms at scale and auto-fill results directly into your spreadsheet. 

          With K2.6's multimodal capability, your agent will open a website, navigate through it, and replicate it. 

      Meet Kimi K2.6 agent - Video hero section, WebGL shaders, real backends. From one prompt.


🔹 Video hero sections - cinematic aesthetic, auto-composited

🔹 WebGL shader animations - native GLSL / WGSL, liquid metal, caustics, raymarching

🔹 Motion design - GSAP + Framer Motion

🔹 Backend database: Kimi wires up auth + database + backend in one pass.

🔹 Website stack - React 19 + TypeScript + Vite + Tailwind + shadcn/ui

🔹 3D w/ physically-based lighting - Three.js + React Three Fiber

          🔹 Video hero sections - cinematic aesthetic, auto-composited

🔹 WebGL shader animations - native GLSL / WGSL, liquid metal, caustics, raymarching

🔹 Motion design - GSAP + Framer Motion

🔹 Backend database: Kimi wires up auth + database + backend in one pass.

🔹 Website stack - React 19 + TypeScript + Vite + Tailwind + shadcn/ui

🔹 3D w/ physically-based lighting - Three.js + React Three Fiber

Video hero sections, built right in.


K2.6 agent calls video generation APIs to create real cinematic footage for your hero, not stock placeholders. Composited into the page, synced to scroll, with shader overlays.

          K2.6 agent calls video generation APIs to create real cinematic footage for your hero, not stock placeholders. Composited into the page, synced to scroll, with shader overlays.

Speaks fluent WebGL shader.


Writes GLSL / WGSL directly - fragment shaders, vertex shaders, noise, SDF, raymarching. Prompt: "a liquid-metal hero with soft caustics."

      Writes GLSL / WGSL directly - fragment shaders, vertex shaders, noise, SDF, raymarching. Prompt: "a liquid-metal hero with soft caustics."

Introducing 𝑨𝒕𝒕𝒆𝒏𝒕𝒊𝒐𝒏 𝑹𝒆𝒔𝒊𝒅𝒖𝒂𝒍𝒔: Rethinking depth-wise aggregation.


Residual connections have long relied on fixed, uniform accumulation. Inspired by the duality of time and depth, we introduce Attention Residuals, replacing standard depth-wise recurrence with learned, input-dependent attention over preceding layers.


🔹 Enables networks to selectively retrieve past representations, naturally mitigating dilution and hidden-state growth.

🔹 Introduces Block AttnRes, partitioning layers into compressed blocks to make cross-layer attention practical at scale.

🔹 Serves as an efficient drop-in replacement, demonstrating a 1.25x compute advantage with negligible (<2%) inference latency overhead.

🔹 Validated on the Kimi Linear architecture (48B total, 3B activated parameters), delivering consistent downstream performance gains.


🔗Full report:

[github.com/MoonshotAI/Att…](https://github.com/MoonshotAI/Attention-Residuals/blob/master/Attention_Residuals.pdf)![Image](/images/1px.png)


          Residual connections have long relied on fixed, uniform accumulation. Inspired by the duality of time and depth, we introduce Attention Residuals, replacing standard depth-wise recurrence with learned, input-dependent attention over preceding layers.

🔹 Enables networks to selectively retrieve past representations, naturally mitigating dilution and hidden-state growth.

🔹 Introduces Block AttnRes, partitioning layers into compressed blocks to make cross-layer attention practical at scale.

🔹 Serves as an efficient drop-in replacement, demonstrating a 1.25x compute advantage with negligible (<2%) inference latency overhead.

🔹 Validated on the Kimi Linear architecture (48B total, 3B activated parameters), delivering consistent downstream performance gains.

🔗Full report:

Scaling law experiments reveal a consistent 1.25× compute advantage across varying model sizes. ![Image](/images/1px.png)


          Analysis of training dynamics demonstrates how AttnRes naturally mitigates hidden-state magnitude growth and yields a more uniform gradient distribution across depth. ![Image](/images/1px.png)


      Meet Kimi Agentic Slides!

Now with Nano Banana Pro 🍌


🎁 Thanksgiving Gift: 48H FREE & UNLIMITED ACCESS


🔸 Agentic search (Kimi K2)

🔸 Files → Slides (PDFs, images, docs+)

🔸 Fully editable + PPTX export

🔸 Designer-level visuals (infographics, illustrations)


Try now:[kimi.com/slides](https://www.kimi.com/slides)

          Now with Nano Banana Pro 🍌

🎁 Thanksgiving Gift: 48H FREE & UNLIMITED ACCESS

🔸 Agentic search (Kimi K2)

🔸 Files → Slides (PDFs, images, docs+)

🔸 Fully editable + PPTX export

🔸 Designer-level visuals (infographics, illustrations)

Try now:

Here's a quick guide. 👇 

          Research paper -> Presentation Ready Deck ![Image](/images/1px.png)
