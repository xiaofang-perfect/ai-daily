---
title: "rohitg00/ai-engineering-from-scratch"
source: GitHub Trending
url: https://github.com/rohitg00/ai-engineering-from-scratch
date: 2026-05-25
published_at: 2026-05-25T06:24:48.713156+00:00
tag: 工具开源
item_id: 9213973d80eae777
---
```
░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒
```



84% of students already use AI tools. Only 18% feel prepared to use them professionally.This curriculum closes that gap.435 lessons. 20 phases. ~320 hours. Python, TypeScript, Rust, Julia. Every lesson ships a reusable artifact: a prompt, a skill, an agent, an MCP server. Free, open source, MIT.

You don't just learn AI. You build it. End-to-end. By hand.


Most AI material teaches in scattered pieces. A paper here, a fine-tuning post there, a flashy agent demo somewhere else. The pieces rarely line up. You ship a chatbot but can't explain its loss curve. You hook a function to an agent but can't say what attention does inside the model that's calling it.

This curriculum is the spine. 20 phases, 435 lessons, four languages: Python, TypeScript, Rust, Julia. Linear algebra at one end, autonomous swarms at the other. Every algorithm gets built from raw math first. Backprop. Tokenizer. Attention. Agent loop. By the time PyTorch shows up, you already know what it's doing under the hood.

Each lesson runs the same loop: read the problem, derive the math, write the code, run the test, keep the artifact. No five-minute videos, no copy-paste deploys, no hand-holding. Free, open source, and built to run on your own laptop.

```
░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒
```


Twenty phases stack on top of each other. Math is the floor. Agents and production are the roof. Skip ahead if you already know the lower layers, but don't skip and then wonder why something at the top is breaking.

```
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#fafaf5','primaryTextColor':'#1a1a1a','primaryBorderColor':'#3553ff','lineColor':'#3553ff','fontFamily':'JetBrains Mono','fontSize':'12px'}}}%%
flowchart TB
P0["Phase 0 — Setup & Tooling"] --> P1["Phase 1 — Math Foundations"]
P1 --> P2["Phase 2 — ML Fundamentals"]
P2 --> P3["Phase 3 — Deep Learning Core"]
P3 --> P4["Phase 4 — Vision"]
P3 --> P5["Phase 5 — NLP"]
P3 --> P6["Phase 6 — Speech & Audio"]
P3 --> P9["Phase 9 — RL"]
P5 --> P7["Phase 7 — Transformers"]
P7 --> P8["Phase 8 — GenAI"]
P7 --> P10["Phase 10 — LLMs from Scratch"]
P10 --> P11["Phase 11 — LLM Engineering"]
P10 --> P12["Phase 12 — Multimodal"]
P11 --> P13["Phase 13 — Tools & Protocols"]
P13 --> P14["Phase 14 — Agent Engineering"]
P14 --> P15["Phase 15 — Autonomous Systems"]
P15 --> P16["Phase 16 — Multi-Agent & Swarms"]
P14 --> P17["Phase 17 — Infrastructure & Production"]
P15 --> P18["Phase 18 — Ethics & Alignment"]
P16 --> P19["Phase 19 — Capstone Projects"]
P17 --> P19
P18 --> P19
```

```
░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒
```


Each lesson lives in its own folder, with the same structure across the entire curriculum:

```
phases/<NN>-<phase-name>/<NN>-<lesson-name>/
├── code/ runnable implementations (Python, TypeScript, Rust, Julia)
├── docs/
│ └── en.md lesson narrative
└── outputs/ prompts, skills, agents, or MCP servers this lesson produces
```


Every lesson follows six beats. The *Build It / Use It* split is the spine — you implement the
algorithm from scratch first, then run the same thing through the production library. You
understand what the framework is doing because you wrote the smaller version yourself.

```
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#fafaf5','primaryTextColor':'#1a1a1a','primaryBorderColor':'#3553ff','lineColor':'#3553ff','fontFamily':'JetBrains Mono','fontSize':'13px'}}}%%
flowchart LR
M["MOTTO<br/><sub>one-line core idea</sub>"] --> Pr["PROBLEM<br/><sub>concrete pain</sub>"]
Pr --> C["CONCEPT<br/><sub>diagrams & intuition</sub>"]
C --> B["BUILD IT<br/><sub>raw math, no frameworks</sub>"]
B --> U["USE IT<br/><sub>same thing in PyTorch / sklearn</sub>"]
U --> S["SHIP IT<br/><sub>prompt · skill · agent · MCP</sub>"]
```

Three ways in. Pick one.

**Option A — read.** Open any completed lesson on
[aiengineeringfromscratch.com](https://aiengineeringfromscratch.com) or expand a phase under
[Contents](https://github.com#contents). No setup, no cloning.

**Option B — clone and run.**

```
git clone https://github.com/rohitg00/ai-engineering-from-scratch.git
cd ai-engineering-from-scratch
python phases/01-math-foundations/01-linear-algebra-intuition/code/vectors.py
```

**Option C — find your level (recommended).** Skip ahead intelligently. Inside Claude, Cursor, Codex, OpenClaw, Hermes, or any agent with the curriculum skills installed:

`/find-your-level`

Ten questions. Maps your knowledge to a starting phase, builds a personalized path with hour estimates. After each phase:

```
/check-understanding 3 # quiz yourself on phase 3
ls phases/03-deep-learning-core/05-loss-functions/outputs/
# ├── prompt-loss-function-selector.md
# └── prompt-loss-debugger.md
```

- You can write code (any language; Python helps).
- You want to understand how AI
**actually works**, not just call APIs.

| Skill | What it does |
|---|---|
`/find-your-level` |

`/check-understanding <phase>`

```
░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒
```


Other curricula end with *"congratulations, you learned X."* Each lesson here ends with a
**reusable tool** you can install or paste into your daily workflow.

Install the lot with

`python3 scripts/install_skills.py`

. Real tools, not homework. By the end of the curriculum, you have a portfolio of 435 artifacts you actually understand because you built them.

Phase 14, lesson 1: the agent loop. ~120 lines of pure Python, no dependencies.

|
```
def run(query, tools):
history = [user(query)]
for step in range(MAX_STEPS):
msg = llm(history)
if msg.tool_calls:
for call in msg.tool_calls:
result = tools[call.name](**call.args)
history.append(tool_result(call.id, result))
continue
return msg.content
raise StepLimitExceeded
``` |
```
---
name: agent-loop
description: ReAct-style loop for any tool list
phase: 14
lesson: 01
---
Implement a minimal agent loop that...
```
```
You are an agent debugger. Given the trace
of an agent run, identify the step where
the agent went wrong and explain why...
``` |

```
░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒
```


Twenty phases. Click any phase to expand its lesson list.

Get your environment ready for everything that follows.


| # | Lesson | Type | Lang |
|---|---|---|---|
| 01 |
|

[Git & Collaboration](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/02-git-and-collaboration)[GPU Setup & Cloud](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/03-gpu-setup-and-cloud)[APIs & Keys](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/04-apis-and-keys)[Jupyter Notebooks](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/05-jupyter-notebooks)[Python Environments](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/06-python-environments)[Docker for AI](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/07-docker-for-ai)[Editor Setup](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/08-editor-setup)[Data Management](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/09-data-management)[Terminal & Shell](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/10-terminal-and-shell)[Linux for AI](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/11-linux-for-ai)[Debugging & Profiling](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/12-debugging-and-profiling)**Phase 1 — Math Foundations** `22 lessons`

*The intuition behind every AI algorithm, through code.*

**Phase 2 — ML Fundamentals** `18 lessons`

*Classical ML — still the backbone of most production AI.*

| # | Lesson | Type | Lang |
|---|---|---|---|
| 01 |
|

[Linear Regression from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/02-linear-regression)[Logistic Regression & Classification](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/03-logistic-regression)[Decision Trees & Random Forests](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/04-decision-trees)[Support Vector Machines](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/05-support-vector-machines)[KNN & Distance Metrics](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/06-knn-and-distances)[Unsupervised Learning: K-Means, DBSCAN](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/07-unsupervised-learning)[Feature Engineering & Selection](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/08-feature-engineering)[Model Evaluation: Metrics, Cross-Validation](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/09-model-evaluation)[Bias, Variance & the Learning Curve](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/10-bias-variance)[Ensemble Methods: Boosting, Bagging, Stacking](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/11-ensemble-methods)[Hyperparameter Tuning](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/12-hyperparameter-tuning)[ML Pipelines & Experiment Tracking](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/13-ml-pipelines)[Naive Bayes](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/14-naive-bayes)[Time Series Fundamentals](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/15-time-series)[Anomaly Detection](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/16-anomaly-detection)[Handling Imbalanced Data](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/17-imbalanced-data)[Feature Selection](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/02-ml-fundamentals/18-feature-selection)**Phase 3 — Deep Learning Core** `13 lessons`

*Neural networks from first principles. No frameworks until you build one.*

| # | Lesson | Type | Lang |
|---|---|---|---|
| 01 |
|

[Multi-Layer Networks & Forward Pass](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/02-multi-layer-networks)[Backpropagation from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/03-backpropagation)[Activation Functions: ReLU, Sigmoid, GELU & Why](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/04-activation-functions)[Loss Functions: MSE, Cross-Entropy, Contrastive](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/05-loss-functions)[Optimizers: SGD, Momentum, Adam, AdamW](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/06-optimizers)[Regularization: Dropout, Weight Decay, BatchNorm](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/07-regularization)[Weight Initialization & Training Stability](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/08-weight-initialization)[Learning Rate Schedules & Warmup](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/09-learning-rate-schedules)[Build Your Own Mini Framework](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/10-mini-framework)[Introduction to PyTorch](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/11-intro-to-pytorch)[Introduction to JAX](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/12-intro-to-jax)[Debugging Neural Networks](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/03-deep-learning-core/13-debugging-neural-networks)**Phase 4 — Computer Vision** `28 lessons`

*From pixels to understanding — image, video, 3D, VLMs, and world models.*

**Phase 5 — NLP: Foundations to Advanced** `29 lessons`

*Language is the interface to intelligence.*

**Phase 6 — Speech & Audio** `17 lessons`

*Hear, understand, speak.*

| # | Lesson | Type | Lang |
|---|---|---|---|
| 01 |
|

[Spectrograms, Mel Scale & Audio Features](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/06-speech-and-audio/02-spectrograms-mel-features)[Audio Classification](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/06-speech-and-audio/03-audio-classification)[Speech Recognition (ASR)](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/06-speech-and-audio/04-speech-recognition-asr)[Whisper: Architecture & Fine-Tuning](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/06-speech-and-audio/05-whisper-architecture-finetuning)[Speaker Recognition & Verification](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/06-speech-and-audio/06-speaker-recognition-verification)[Text-to-Speech (TTS)](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/06-speech-and-audio/07-text-to-speech)[Voice Cloning & Voice Conversion](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/06-speech-and-audio/08-voice-cloning-conversion)[Music Generation](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/06-speech-and-audio/09-music-generation)[Audio-Language Models](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/06-speech-and-audio/10-audio-language-models)[Real-Time Audio Processing](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/06-speech-and-audio/11-real-time-audio-processing)[Build a Voice Assistant Pipeline](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/06-speech-and-audio/12-voice-assistant-pipeline)[Neural Audio Codecs — EnCodec, SNAC, Mimi, DAC](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/06-speech-and-audio/13-neural-audio-codecs)[Voice Activity Detection & Turn-Taking](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/06-speech-and-audio/14-voice-activity-detection-turn-taking)[Streaming Speech-to-Speech — Moshi, Hibiki](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/06-speech-and-audio/15-streaming-speech-to-speech-moshi-hibiki)[Voice Anti-Spoofing & Audio Watermarking](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/06-speech-and-audio/16-anti-spoofing-audio-watermarking)[Audio Evaluation — WER, MOS, MMAU, Leaderboards](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/06-speech-and-audio/17-audio-evaluation-metrics)**Phase 7 — Transformers Deep Dive** `14 lessons`

*The architecture that changed everything.*

| # | Lesson | Type | Lang |
|---|---|---|---|
| 01 |
|

[Self-Attention from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/02-self-attention-from-scratch)[Multi-Head Attention](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/03-multi-head-attention)[Positional Encoding: Sinusoidal, RoPE, ALiBi](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/04-positional-encoding)[The Full Transformer: Encoder + Decoder](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/05-full-transformer)[BERT — Masked Language Modeling](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/06-bert-masked-language-modeling)[GPT — Causal Language Modeling](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/07-gpt-causal-language-modeling)[T5, BART — Encoder-Decoder Models](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/08-t5-bart-encoder-decoder)[Vision Transformers (ViT)](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/09-vision-transformers)[Audio Transformers — Whisper Architecture](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/10-audio-transformers-whisper)[Mixture of Experts (MoE)](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/11-mixture-of-experts)[KV Cache, Flash Attention & Inference Optimization](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/12-kv-cache-flash-attention)[Scaling Laws](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/13-scaling-laws)[Build a Transformer from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/07-transformers-deep-dive/14-build-a-transformer-capstone)**Phase 8 — Generative AI** `14 lessons`

*Create images, video, audio, 3D, and more.*

| # | Lesson | Type | Lang |
|---|---|---|---|
| 01 |
|

[Autoencoders & VAE](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/08-generative-ai/02-autoencoders-vae)[GANs: Generator vs Discriminator](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/08-generative-ai/03-gans-generator-discriminator)[Conditional GANs & Pix2Pix](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/08-generative-ai/04-conditional-gans-pix2pix)[StyleGAN](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/08-generative-ai/05-stylegan)[Diffusion Models — DDPM from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/08-generative-ai/06-diffusion-ddpm-from-scratch)[Latent Diffusion & Stable Diffusion](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/08-generative-ai/07-latent-diffusion-stable-diffusion)[ControlNet, LoRA & Conditioning](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/08-generative-ai/08-controlnet-lora-conditioning)[Inpainting, Outpainting & Editing](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/08-generative-ai/09-inpainting-outpainting-editing)[Video Generation](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/08-generative-ai/10-video-generation)[Audio Generation](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/08-generative-ai/11-audio-generation)[3D Generation](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/08-generative-ai/12-3d-generation)[Flow Matching & Rectified Flows](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/08-generative-ai/13-flow-matching-rectified-flows)[Evaluation: FID, CLIP Score](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/08-generative-ai/14-evaluation-fid-clip-score)**Phase 9 — Reinforcement Learning** `12 lessons`

*The foundation of RLHF and game-playing AI.*

| # | Lesson | Type | Lang |
|---|---|---|---|
| 01 |
|

[Dynamic Programming](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/02-dynamic-programming)[Monte Carlo Methods](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/03-monte-carlo-methods)[Q-Learning, SARSA](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/04-q-learning-sarsa)[Deep Q-Networks (DQN)](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/05-dqn)[Policy Gradients — REINFORCE](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/06-policy-gradients-reinforce)[Actor-Critic — A2C, A3C](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/07-actor-critic-a2c-a3c)[PPO](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/08-ppo)[Reward Modeling & RLHF](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/09-reward-modeling-rlhf)[Multi-Agent RL](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/10-multi-agent-rl)[Sim-to-Real Transfer](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/11-sim-to-real-transfer)[RL for Games](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/09-reinforcement-learning/12-rl-for-games)**Phase 10 — LLMs from Scratch** `22 lessons`

*Build, train, and understand large language models.*

**Phase 11 — LLM Engineering** `17 lessons`

*Put LLMs to work in production.*

| # | Lesson | Type | Lang |
|---|---|---|---|
| 01 |
|

[Few-Shot, CoT, Tree-of-Thought](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/02-few-shot-cot)[Structured Outputs](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/03-structured-outputs)[Embeddings & Vector Representations](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/04-embeddings)[Context Engineering](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/05-context-engineering)[RAG: Retrieval-Augmented Generation](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/06-rag)[Advanced RAG: Chunking, Reranking](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/07-advanced-rag)[Fine-Tuning with LoRA & QLoRA](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/08-fine-tuning-lora)[Function Calling & Tool Use](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/09-function-calling)[Evaluation & Testing](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/10-evaluation)[Caching, Rate Limiting & Cost](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/11-caching-cost)[Guardrails & Safety](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/12-guardrails)[Building a Production LLM App](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/13-production-app)[Model Context Protocol (MCP)](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/14-model-context-protocol)[Prompt Caching & Context Caching](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/15-prompt-caching)[LangGraph: State Machines for Agents](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/16-langgraph-state-machines)[Agent Framework Tradeoffs](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/17-agent-framework-tradeoffs)**Phase 12 — Multimodal AI** `25 lessons`

*See, hear, read, and reason across modalities — from ViT patches to computer-use agents.*

**Phase 13 — Tools & Protocols** `23 lessons`

*The interfaces between AI and the real world.*

| # | Lesson | Type | Lang |
|---|---|---|---|
| 01 |
|

[Function Calling Deep Dive](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/02-function-calling-deep-dive)[Parallel and Streaming Tool Calls](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/03-parallel-and-streaming-tool-calls)[Structured Output](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/04-structured-output)[Tool Schema Design](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/05-tool-schema-design)[MCP Fundamentals](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/06-mcp-fundamentals)[Building an MCP Server](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/07-building-an-mcp-server)[Building an MCP Client](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/08-building-an-mcp-client)[MCP Transports](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/09-mcp-transports)[MCP Resources and Prompts](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/10-mcp-resources-and-prompts)[MCP Sampling](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/11-mcp-sampling)[MCP Roots and Elicitation](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/12-mcp-roots-and-elicitation)[MCP Async Tasks](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/13-mcp-async-tasks)[MCP Apps](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/14-mcp-apps)[MCP Security I — Tool Poisoning](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/15-mcp-security-tool-poisoning)[MCP Security II — OAuth 2.1](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/16-mcp-security-oauth-2-1)[MCP Gateways and Registries](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/17-mcp-gateways-and-registries)[MCP Auth in Production — DCR + JWKS on iii](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/18-mcp-auth-production)[A2A Protocol](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/19-a2a-protocol)[OpenTelemetry GenAI](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/20-opentelemetry-genai)[LLM Routing Layer](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/21-llm-routing-layer)[Skills and Agent SDKs](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/22-skills-and-agent-sdks)[Capstone — Tool Ecosystem](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/23-capstone-tool-ecosystem)**Phase 14 — Agent Engineering** `42 lessons`

*Build agents from first principles — loop, memory, planning, frameworks, benchmarks, production, workbench.*

Each Phase 14 workbench lesson (31-42) ships a `mission.md`

briefing the agent before it opens the full lesson docs.

**Phase 15 — Autonomous Systems** `22 lessons`

*Long-horizon agents, self-improvement, and the 2026 safety stack.*

**Phase 16 — Multi-Agent & Swarms** `25 lessons`

*Coordination, emergence, and collective intelligence.*

**Phase 17 — Infrastructure & Production** `28 lessons`

*Ship AI to the real world.*

| # | Lesson | Type | Lang |
|---|---|---|---|
| 01 | Managed LLM Platforms — Bedrock, Azure OpenAI, Vertex AI | Learn | Python |
| 02 | Inference Platform Economics — Fireworks, Together, Baseten, Modal | Learn | Python |
| 03 | GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler | Learn | Python |
| 04 | vLLM Serving Internals — PagedAttention, Continuous Batching, Chunked Prefill | Learn | Python |
| 05 | EAGLE-3 Speculative Decoding in Production | Learn | Python |
| 06 | SGLang and RadixAttention for Prefix-Heavy Workloads | Learn | Python |
| 07 | TensorRT-LLM on Blackwell with FP8 and NVFP4 | Learn | Python |
| 08 | Inference Metrics — TTFT, TPOT, ITL, Goodput, P99 | Learn | Python |
| 09 | Production Quantization — AWQ, GPTQ, GGUF, FP8, NVFP4 | Learn | Python |
| 10 | Cold Start Mitigation for Serverless LLMs | Learn | Python |
| 11 | Multi-Region LLM Serving and KV Cache Locality | Learn | Python |
| 12 | Edge Inference — ANE, Hexagon, WebGPU, Jetson | Learn | Python |
| 13 | LLM Observability Stack Selection | Learn | Python |
| 14 | Prompt Caching and Semantic Caching Economics | Learn | Python |
| 15 | Batch APIs — the 50% Discount as Industry Standard | Learn | Python |
| 16 | Model Routing as a Cost-Reduction Primitive | Learn | Python |
| 17 | Disaggregated Prefill/Decode — NVIDIA Dynamo and llm-d | Learn | Python |
| 18 | vLLM Production Stack with LMCache KV Offloading | Learn | Python |
| 19 | AI Gateways — LiteLLM, Portkey, Kong, Bifrost | Learn | Python |
| 20 | Shadow, Canary, and Progressive Deployment | Learn | Python |
| 21 | A/B Testing LLM Features — GrowthBook and Statsig | Learn | Python |
| 22 | Load Testing LLM APIs — k6, LLMPerf, GenAI-Perf | Build | Python |
| 23 | SRE for AI — Multi-Agent Incident Response | Learn | Python |
| 24 | Chaos Engineering for LLM Production | Learn | Python |
| 25 | Security — Secrets, PII Scrubbing, Audit Logs | Learn | Python |
| 26 | Compliance — SOC 2, HIPAA, GDPR, EU AI Act, ISO 42001 | Learn | Python |
| 27 | FinOps for LLMs — Unit Economics and Multi-Tenant Attribution | Learn | Python |
| 28 | Self-Hosted Serving Selection — llama.cpp, Ollama, TGI, vLLM, SGLang | Learn | Python |

**Phase 18 — Ethics, Safety & Alignment** `30 lessons`

*Build AI that helps humanity. Not optional.*

**Phase 19 — Capstone Projects** `17 projects`

*2026 end-to-end shippable products, 20-40 hours each.*

| # | Project | Combines | Lang |
|---|---|---|---|
| 01 |
|

[RAG over Codebase (Cross-Repo Semantic Search)](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/02-rag-over-codebase)[Real-Time Voice Assistant (ASR → LLM → TTS)](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/03-realtime-voice-assistant)[Multimodal Document QA (Vision-First)](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/04-multimodal-document-qa)[Autonomous Research Agent (AI-Scientist Class)](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/05-autonomous-research-agent)[DevOps Troubleshooting Agent for Kubernetes](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/06-devops-troubleshooting-agent)[End-to-End Fine-Tuning Pipeline](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/07-end-to-end-fine-tuning-pipeline)[Production RAG Chatbot (Regulated Vertical)](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/08-production-rag-chatbot)[Code Migration Agent (Repo-Level Upgrade)](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/09-code-migration-agent)[Multi-Agent Software Engineering Team](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/10-multi-agent-software-team)[LLM Observability & Eval Dashboard](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/11-llm-observability-dashboard)[Video Understanding Pipeline (Scene → QA)](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/12-video-understanding-pipeline)[MCP Server with Registry and Governance](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/13-mcp-server-with-registry)[Speculative-Decoding Inference Server](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/14-speculative-decoding-server)[Constitutional Safety Harness + Red-Team Range](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/15-constitutional-safety-harness)[GitHub Issue-to-PR Autonomous Agent](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/16-github-issue-to-pr-agent)[Personal AI Tutor (Adaptive, Multimodal)](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/17-personal-ai-tutor)```
░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒
```


Every lesson produces a reusable artifact. By the end you have:

```
outputs/
├── prompts/ prompt templates for every AI task
└── skills/ SKILL.md files for AI coding agents
```


Install them with `python3 scripts/install_skills.py`

. Plug them into Claude, Cursor,
Codex, OpenClaw, Hermes, or any MCP-compatible agent. Real tools, not homework.

The repo ships 378 skills and 99 prompts under `phases/**/outputs/`

.
`scripts/install_skills.py`

walks every artifact, parses YAML frontmatter, and
copies the matching files into a target directory in the layout your agent
expects.

```
python3 scripts/install_skills.py ~/.claude/skills # every skill, nested layout
python3 scripts/install_skills.py ./out --type all # skills + prompts + agents
python3 scripts/install_skills.py ./out --phase 14 # one phase only
python3 scripts/install_skills.py ./out --tag rag # filter by tag
python3 scripts/install_skills.py ./out --layout flat # flat files
python3 scripts/install_skills.py ./out --dry-run # preview without writing
python3 scripts/install_skills.py ./out --force # overwrite existing files
```

By default the script refuses to overwrite an existing destination and exits
with code 1 after listing every colliding path. Use `--dry-run`

to preview
collisions or `--force`

to overwrite. Every non-dry-run run writes a
`manifest.json`

in the target with the full inventory grouped by type and
phase. Pick the layout your agent reads:

`--layout` |
Path written |
|---|---|
`skills` |
`<target>/<name>/SKILL.md` (Claude / Cursor convention) |
`by-phase` |
`<target>/phase-NN/<name>.md` |
`flat` |
`<target>/<name>.md` |

The Phase 14 capstone ships a reusable Agent Workbench pack (AGENTS.md, schemas, init / verify / handoff scripts). Scaffold it into any repo with:

```
python3 scripts/scaffold_workbench.py path/to/your-repo # full pack + seeds
python3 scripts/scaffold_workbench.py path/to/your-repo --minimal # skip docs/
python3 scripts/scaffold_workbench.py path/to/your-repo --dry-run # preview only
python3 scripts/scaffold_workbench.py path/to/your-repo --force # overwrite
```

You get the seven workbench surfaces wired up, a starter `task_board.json`

,
and a fresh `agent_state.json`

at `schema_version: 1`

. From there: edit the
task, edit `AGENTS.md`

, run `scripts/init_agent.py`

, hand the contract to
your agent. The pack source lives at
`phases/14-agent-engineering/42-agent-workbench-capstone/outputs/agent-workbench-pack/`

.

`scripts/build_catalog.py`

walks every phase, every lesson, every artifact on
disk and writes `catalog.json`

at the repo root. One file, every course truth.

```
python3 scripts/build_catalog.py # writes <repo>/catalog.json
python3 scripts/build_catalog.py --stdout # to stdout, do not touch repo
python3 scripts/build_catalog.py --out path/to/file.json
```

The catalog is filesystem-derived, not README-derived, so counts always match what is actually on disk. Use it for site builds, downstream tooling, or to verify the README counts have not drifted. Schema is documented at the top of the script.

A GitHub Action (`.github/workflows/curriculum.yml`

) rebuilds `catalog.json`

on every PR and fails the build if the committed file is stale. After editing
any lesson, run `python3 scripts/build_catalog.py`

and commit the result, or
CI will reject the PR. The same workflow runs `audit_lessons.py`

in
warn-only mode (so existing drift does not block contributors).

`scripts/lesson_run.py`

byte-compiles every `.py`

file under each lesson's
`code/`

directory. Default mode is syntax-check only — no execution, no API
keys, no heavy ML deps required. Catches the regressions contributors
introduce most often (bad indentation, broken f-strings, stray edits).

```
python3 scripts/lesson_run.py # syntax-check the whole curriculum
python3 scripts/lesson_run.py --phase 14 # one phase only
python3 scripts/lesson_run.py --json # JSON report on stdout
python3 scripts/lesson_run.py --strict # exit 1 if any lesson fails
python3 scripts/lesson_run.py --execute # actually run, 10s timeout per lesson
```

`--execute`

runs each lesson's `code/main.py`

(or the first `.py`

file) with a
10-second timeout. Lessons whose entry file starts with a `# requires: pkg1, pkg2`

comment listing non-stdlib deps are skipped with reason `needs <deps>`

.
The script is opt-in and not wired into CI.

Stdlib only, Python 3.10+. Set `LINK_CHECK_SKIP=domain1,domain2`

to override
the default skip-list (`twitter.com`

, `x.com`

, `linkedin.com`

,
`instagram.com`

, `medium.com`

— domains that aggressively block automated
HEAD/GET).

| Background | Start at | Estimated time |
|---|---|---|
| New to programming and AI | Phase 0 — Setup | ~306 hours |
| Know Python, new to ML | Phase 1 — Math Foundations | ~270 hours |
| Know ML, new to deep learning | Phase 3 — Deep Learning Core | ~200 hours |
| Know deep learning, want LLMs and agents | Phase 10 — LLMs from Scratch | ~100 hours |
| Senior engineer, only want agent engineering | Phase 14 — Agent Engineering | ~60 hours |

```
░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒
```


FIG_003 · ATHE INDUSTRY SIGNAL |
FIG_003 · BFOUNDATIONAL PAPERS COVERED |
|---|---|
|
*Attention Is All You Need*— Vaswani et al., 2017 →[Phase 7](https://github.com#phase-7)*Language Models are Few-Shot Learners*(GPT-3) →[Phase 10](https://github.com#phase-10)*Denoising Diffusion Probabilistic Models*→[Phase 8](https://github.com#phase-8)*InstructGPT / RLHF*→[Phase 10](https://github.com#phase-10)*Direct Preference Optimization*→[Phase 10](https://github.com#phase-10)*Chain-of-Thought Prompting*→[Phase 11](https://github.com#phase-11)*ReAct: Reasoning + Acting in LLMs*→[Phase 14](https://github.com#phase-14)*Model Context Protocol*— Anthropic →[Phase 13](https://github.com#phase-13)
|

```
░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒
```


| Goal | Read |
|---|---|
| Contribute a lesson or fix |
|

[FORKING.md](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/FORKING.md)[LESSON_TEMPLATE.md](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/LESSON_TEMPLATE.md)[ROADMAP.md](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/ROADMAP.md)[glossary/terms.md](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/glossary/terms.md)[CODE_OF_CONDUCT.md](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/CODE_OF_CONDUCT.md)Before submitting a lesson, run the invariant check:

```
python3 scripts/audit_lessons.py # full curriculum
python3 scripts/audit_lessons.py --phase 14 # single phase
python3 scripts/audit_lessons.py --json # CI-friendly output
```

Exit code is non-zero when any rule fails. Rules (L001–L010) validate directory
shape, `docs/en.md`

presence + H1, `code/`

non-emptiness, `quiz.json`

schema
(rejects the legacy `q/choices/answer`

keys that caused issue #102), and
relative links inside lesson docs.

```
░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒
```


Free, MIT-licensed, 435 lessons. The curriculum is maintained on sponsorship alone. Cash only.

**Reach (verified 2026-05-14):** 55,593 monthly visitors · 90,709 page views · 7.5K stars ·
Twitter/X is the #1 acquisition channel.

| Tier | $/mo | What you get |
|---|---|---|
| Backer | $25 | Name in BACKERS.md |
| Bronze | $250 | Text-only row in README sponsor block + launch-day tweet |
| Silver | $750 | Small logo in README + listed as one supported provider in API lessons |
| Gold | $2,000 | Medium logo in README + sponsor page + quarterly X / LinkedIn co-feature |
| Platinum | $5,000 | Hero logo above the fold + one dedicated integration lesson, max 1 partner |

Full rate card, hard rules, pricing anchors, and reach data: [SPONSORS.md](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/SPONSORS.md).
Sign up via [GitHub Sponsors](https://github.com/sponsors/rohitg00).

```
░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒
```




If this manual helped you, star the repo. It keeps the project alive.

MIT. Use it however you want — fork it, teach it, sell it, ship it. Attribution appreciated, not required.

Maintained by [Rohit Ghumare](https://github.com/rohitg00) and the community.
