---
title: "DeepReinforce releases Ornith-1.0 open-source coding models"
source: TLDR AI · 2026-06-26
url: https://www.testingcatalog.com/deepreinforce-releases-ornith-1-0-open-source-coding-models/?utm_source=tldrai
date: 2026-06-27
published_at: 2026-06-26T12:00:00+00:00
tag: 工具开源
item_id: ab1f04883f539fe2
---
![Google Preferred Source](https://www.testingcatalog.com/assets/images/google_preferred_source_badge_light_en.png?v=d81cbce2e9) 

        DeepReinforce has open-sourced Ornith-1.0, a self-improving family of models built for agentic coding. The release spans the full range, from a compact 9B Dense version meant for edge deployment up to a 397B MoE model aimed at frontier-scale work, with 31B Dense and 35B MoE options in between. Each variant is trained on top of pretrained Gemma 4 and Qwen 3.5 foundations.

![Ornith-1.0](https://storage.ghost.io/c/2a/1b/2a1b1782-8506-4d7d-bf53-ad3fb52e2a0f/content/images/2026/06/HLqjo1CbMAAoc8u.jpeg)

What sets Ornith-1.0 apart from most reinforcement learning setups is how it handles the scaffold. Rather than depending on human-designed harnesses to steer solution generation, the model learns to produce both the solution rollouts and the task-specific scaffolds that guide them. Each RL step runs in two stages. Conditioned on a task and the scaffold last used for it, the model proposes a refined scaffold, then generates a solution conditioned on that scaffold. Reward from the rollout flows back to both stages, so the model is trained to author the orchestration as well as the answer. Repeated across training, scaffolds get mutated and selected toward those that produce higher-reward trajectories, and per-task strategies surface on their own without hand-engineered harness design.

Letting a model write its own scaffold opens a path to reward hacking, where a scaffold satisfies the verifier without doing the task. DeepReinforce describes a three-layer defense:

- A fixed outer trust boundary that keeps the environment and test isolation beyond the model's reach.
- A deterministic monitor that flags attempts to read withheld paths or alter verification scripts.
- A frozen LLM judge that vetoes the verifier when gaming happens inside the allowed tool surface.

![Ornith-1.0](https://storage.ghost.io/c/2a/1b/2a1b1782-8506-4d7d-bf53-ad3fb52e2a0f/content/images/2026/06/image-8.png)

On performance, DeepReinforce positions Ornith-1.0 as state of the art among open-source models of comparable size. The company reports the 397B flagship reaching 77.5 on Terminal-Bench 2.1 and 82.4 on SWE-Bench Verified, figures it says match Claude Opus 4.7 and top open peers such as MiniMax M3 and DeepSeek-V4-Pro. The 35B model is reported to clear similarly sized Qwen and Gemma builds, while the 9B version is said to hit 43.1 on Terminal-Bench 2.1 and 69.4 on SWE-Bench Verified and match far larger models like Gemma 4-31B, which puts capable coding within reach of resource-limited hardware.

Check the models out on HuggingFace!

[Learn more](https://huggingface.co/deepreinforce-ai?ref=testingcatalog.com)

DeepReinforce is the AI lab behind the release, a team that publishes reinforcement learning research in the open, including prior work such as CUDA-L1, and that shipped the IterX optimization loop for code agents. Ornith-1.0 carries that direction further by folding scaffold construction into the training process itself. The weights and a technical report are released on Hugging Face for teams that want to run or study the models directly.
