---
title: "$500 GPU outperforms Claude Sonnet on coding benchmarks"
source: Hacker News
url: https://github.com/itigges22/ATLAS
date: 2026-03-27
published_at: 2026-03-26T17:31:24+00:00
tag: 工具开源
item_id: 1e86688a58c69ed2
---
**Adaptive Test-time Learning and Autonomous Specialization**

ATLAS is a self-hosted coding assistant built on intelligent inference infrastructure. You point it at an open-weight model running locally, and it turns that model into something that competes with frontier systems, with no fine-tuning, no API calls, and no cloud in between.

Instead of training a larger model or routing to a hosted one, ATLAS wraps a frozen local model in a pipeline that plans before generating, verifies its own output against constraints it extracts from the problem, scores candidates with an energy-based lens, and repairs failures through self-generated test feedback. The weights never change. The intelligence lives in the scaffolding around them.

The result is a serious coding assistant that runs on a single consumer GPU for fractions of a cent per task. Nothing leaves your machine, no vendor can pull the model out from under you, and the entire stack is open source. One model, one GPU, no one else's infrastructure in the loop.

**2026-04-13**-["How to Run an AI Coding Assistant on a $500 GPU and Beat Claude Sonnet"](https://devtrends.ru/python/itigges22-atlas)- devtrends.ru**2026-04-05**-- interactive CLI, Docker Compose deployment, 95.8% reliability[V3.0.1 released](https://github.com/itigges22/ATLAS/blob/main/CHANGELOG.md)**2026-04-03**-["$500 GPU Beats Claude: Local AI Revolution for Web Devs"](https://ownet.it/blog/500-gpu-beats-claude-local-ai-revolution-for-web-devs)- ownet.it**2026-03-29**-["A $500 GPU Just Outscored Claude Sonnet on Coding Benchmarks"](https://aivy.com.au/news/atlas-500-gpu-outperforms-claude-sonnet-coding/)- Aivy**2026-03-28**-["Why a $500 GPU Can Beat Claude Sonnet on Coding Benchmarks"](https://medium.com/data-science-collective/why-a-500-gpu-can-beat-claude-sonnet-on-coding-benchmarks-6c8169ffe4fe)- Data Science Collective**2026-03-27**-["ATLAS: A $500 GPU Outperforms Claude Sonnet"](https://clauday.com/article/b92c5551-b490-4d76-ae3d-d8dedf10d88b)- Clauday**2026-03-27**-["ATLAS – lokal AI-koding på 5000kr GPU slår Claude på benchmark"](https://www.jansverre.net/atlas-lokal-ai-koding-pa-500-gpu-slar-claude-pa-benchmark/)- jansverre.net (Norwegian)**2026-03-26**-["Local LLM Coding: $500 GPU Beats Claude: Not the Story"](https://novaknown.com/2026/03/26/local-llm-coding/)- Sarah Fraser, novaknown.com**2026-03-26**-["ATLAS: How a $500 GPU Achieves 74.6% LiveCodeBench Performance Through Intelligent Infrastructure"](https://techplanet.today/post/atlas-how-a-500-gpu-achieves-746-livecodebench-performance-through-intelligent-infrastructure)- TechPlanet**2026-03-26**-[Hacker News front page](https://news.ycombinator.com/item?id=47533297)- 489 points, 285 comments**2026-03-05**-- 74.6% LiveCodeBench pass@1-v(k=3) on frozen Qwen3-14B[V3.0 released](https://github.com/itigges22/ATLAS/blob/main/docs/reports/V3_ABLATION_STUDY.md)**2026-02-18**-- benchmark infrastructure, HumanEval/MBPP/LiveCodeBench/GPQA/SciCode evaluation suite[V2.0 released](https://github.com/itigges22/ATLAS/blob/main/CHANGELOG.md)



- Go-based agent loop that orchestrates the entire system.[atlas-proxy](https://github.com/itigges22/ATLAS/blob/main/docs/ARCHITECTURE.md#3-atlas-proxy-outer-layer)

- a.
[Tool-call routing](https://github.com/itigges22/ATLAS/blob/main/docs/ARCHITECTURE.md#tools)- classifies file operations by complexity tier - b.
[Grammar enforcement](https://github.com/itigges22/ATLAS/blob/main/docs/ARCHITECTURE.md#grammar-enforcement)- GBNF schemas guarantee 100% valid JSON output - c.
[Safety limits](https://github.com/itigges22/ATLAS/blob/main/docs/ARCHITECTURE.md#safety-limits)- turn caps, token budgets, timeout enforcement

- multi-phase code generation that turns a single prompt into verified, high-quality output.[V3 Pipeline](https://github.com/itigges22/ATLAS/blob/main/docs/ARCHITECTURE.md#4-v3-pipeline-inner-layer)

- a.
[PlanSearch](https://github.com/itigges22/ATLAS/blob/main/docs/reports/V3_ABLATION_STUDY.md#phase-1-constraint-driven-generation-124pp)- constraint-driven structured planning - b.
[DivSampling](https://github.com/itigges22/ATLAS/blob/main/docs/reports/V3_ABLATION_STUDY.md#phase-1-constraint-driven-generation-124pp)- diverse candidate generation across temperature and strategy - c.
[Budget Forcing](https://github.com/itigges22/ATLAS/blob/main/docs/reports/V3_ABLATION_STUDY.md#phase-1-constraint-driven-generation-124pp)- controls thinking token allocation per phase - d.
[PR-CoT Repair](https://github.com/itigges22/ATLAS/blob/main/docs/reports/V3_ABLATION_STUDY.md#pr-cot-repair-36-rescues)- self-generated test cases for iterative fix cycles - e.
[Refinement Loops](https://github.com/itigges22/ATLAS/blob/main/docs/reports/V3_ABLATION_STUDY.md#refinement-loop-6-rescues)- repeated sandbox verification and correction - f.
[Derivation Chains](https://github.com/itigges22/ATLAS/blob/main/docs/reports/V3_ABLATION_STUDY.md#derivation-chains-0-rescues)- multi-step reasoning for complex problems

- energy-based scoring and retrieval without external oracles. ([Geometric Lens](https://github.com/itigges22/ATLAS/blob/main/docs/ARCHITECTURE.md#5-geometric-lens)[What is a "Geometric Lens"?](https://github.com/itigges22/ATLAS/blob/main/docs/ARCHITECTURE.md#why-geometric-lens))

- a.
[C(x) Cost Field](https://github.com/itigges22/ATLAS/blob/main/docs/ARCHITECTURE.md#scoring-models)- MLP that scores candidate quality from embeddings - b.
[G(x) Quality Prediction](https://github.com/itigges22/ATLAS/blob/main/docs/ARCHITECTURE.md#scoring-models)- XGBoost model for selection decisions - c.
[RAG / PageIndex V2](https://github.com/itigges22/ATLAS/blob/main/docs/ARCHITECTURE.md#rag--pageindex-v2)- AST-aware code retrieval and project indexing - d.
[Confidence Router](https://github.com/itigges22/ATLAS/blob/main/docs/ARCHITECTURE.md#confidence-router--pattern-cache)- Thompson Sampling routes compute where it matters

- isolated execution environment for build verification.[Sandbox](https://github.com/itigges22/ATLAS/blob/main/docs/ARCHITECTURE.md#6-sandbox)

- a. Multi-language execution - Python, Rust, Go, C, Shell, and more
- b. Compilation and linting - syntax verification before scoring
- c. Test running - executes generated and existing test suites

- local LLM inference on a single consumer GPU.[llama-server](https://github.com/itigges22/ATLAS/blob/main/docs/CONFIGURATION.md#6-llama-server)

- a. CUDA acceleration - quantized model inference (Q6_K / Q4_K_M)
- b. Grammar-constrained decoding - structured output at the token level
- c. Self-embeddings - embedding extraction without a separate model

- type[Interactive CLI](https://github.com/itigges22/ATLAS/blob/main/docs/CLI.md)`atlas`

in any project directory and start building.

- a.
[Tool-call agent loop](https://github.com/itigges22/ATLAS/blob/main/docs/CLI.md#streaming-output)- read, write, edit, delete, run commands - b.
[Streaming output](https://github.com/itigges22/ATLAS/blob/main/docs/CLI.md#how-streaming-works)- real-time response via SSE - c.
[Project-aware context](https://github.com/itigges22/ATLAS/blob/main/docs/CLI.md#proxy-file-access)- automatic file discovery and injection

Full documentation - setup guides, architecture, configuration, troubleshooting, benchmark reports, and the [research that informs each component](https://github.com/itigges22/ATLAS/blob/main/docs/SOURCES.md) - lives in the [docs/](https://github.com/itigges22/ATLAS/blob/main/docs) directory.

ATLAS requires a GPU with 16GB+ VRAM, Docker (with nvidia-container-toolkit) or Podman, and Python 3.9+. Currently tested on NVIDIA GPUs - ATLAS is not NVIDIA-specific, and ROCm support for AMD GPUs is on the roadmap. See ** SETUP.md** for full installation instructions covering Docker Compose, bare-metal, and K3s deployment. Once running, type

`atlas`

in any project directory and start building.**Tested on NVIDIA only**- ATLAS uses llama.cpp for inference, which supports multiple accelerator backends. ROCm support is a V3.1 priority.**9B model not formally benchmarked**- the CLI ships Qwen3.5-9B with the full V3 pipeline, but formal LiveCodeBench scores are from the 14B model. 9B benchmarks are V3.1 work. For the V3 (14B) benchmark results, methodology, and ablation analysis, see; raw benchmark traces are published on`docs/reports/V3_ABLATION_STUDY.md`

[HuggingFace](https://huggingface.co/datasets/itigges22/ATLAS).**Complex feature additions can fail**- adding features to existing projects succeeds ~67% of the time. The model sometimes over-explores instead of writing code.**Grammar-constrained inference speed**- ~51 tok/s on llama-server. Faster grammar integration is planned for V3.1.

**V3.0.1** - Current release. Interactive CLI, Docker Compose deployment, V3 pipeline integration.

**V3.1** - In progress.

- ROCm support - AMD GPU inference via llama.cpp ROCm backend.
- Formal 9B benchmarks - LiveCodeBench, GPQA Diamond, SciCode on Qwen3.5-9B.
- CLI reliability - expanded testing, targeting L6 ≥ 90%.
- Grammar speed - C-side sampler chain for faster constrained decoding.
- Structural code reasoning - tree-sitter + solver-backed call graph for reachability queries and scoped context injection, so the model stops burning agent turns exploring unfamiliar codebases on L6 tasks. Tracked as
[issue #39](https://github.com/itigges22/ATLAS/issues/39); inspired by[Dmitri Sotnikov's chiasmus](https://github.com/yogthos/chiasmus/tree/main).

**V3.2** - Exploratory.

[Reasoning with Sampling](https://arxiv.org/abs/2510.14901)- MCMC over logits during decoding to prune bad trajectories before completion, saving compute on PlanSearch candidates already going off the rails. Complements the Geometric Lens's post-hoc scoring; tracked as[issue #40](https://github.com/itigges22/ATLAS/issues/40).

ATLAS is built by a single college student in his free time on a single consumer GPU. If the project has been useful to you and you want to help keep it sustainable, please consider ** sponsoring on GitHub**.

Sponsorship directly funds:

**Compute & hardware**— more GPUs for faster benchmark iteration, access to architectures the maintainer can't afford (AMD ROCm, higher VRAM cards, cloud rentals for larger-model experiments).**Contributor bounties**— meaningful compensation for external contributors who put real time into substantive PRs, so ATLAS can grow faster than a single-person pace allows.**Research**— continued academic engagement around the architecture, from future workshop and conference submissions to paper writing and collaborations that validate and extend the approach.**Community**— continued support for the community and platforms ATLAS runs on, including documentation, user-facing channels, and educational content that help ATLAS reach more developers and better serve the ones already using it.

Every sponsor is credited in the release notes of the version they helped fund.

We're building ATLAS in the open and we're actively looking for contributors and core maintainers. Whether you're fixing a bug, adding accelerator support, or rethinking a whole subsystem - there's a place for you here. If you believe open models deserve better infrastructure, come build with us.

Found a bug or hit a wall? ** Open an issue** - you don't need to submit a fix. Bug reports and feedback help just as much as code.

See ** CONTRIBUTING.md** for guidelines.

Licensed under the [GNU Affero General Public License v3.0 (AGPL-3.0)](https://github.com/itigges22/ATLAS/blob/main/LICENSE).
