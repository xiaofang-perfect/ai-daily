---
title: "Inkling-Small"
source: TLDR AI · 2026-07-31
url: https://thinkingmachines.ai/news/inkling-small/?utm_source=tldrai
date: 2026-08-01
published_at: 2026-07-31T12:00:00+00:00
tag: 论文研究
item_id: 1245d75883f5b099
---
Today, we are releasing Inkling-Small, an efficient open-weights model that achieves comparable performance to [Inkling](https://thinkingmachines.ai/news/introducing-inkling/) at a quarter of its size.

Inkling-Small is a Mixture-of-Experts transformer with 276B total parameters, 12B active, trained on NVIDIA GB300 NVL72 systems. Like Inkling, it features native reasoning over audio and images, variable thinking effort, a context window of up to 1M tokens, and well-rounded performance across a range of benchmarks.

### Inkling-Small

### Inkling

Compared to Inkling, Inkling-Small achieves comparable performance with much less compute. Across agentic tool use (Terminal-Bench 2.1), reasoning (HLE text-only, no tools), and instruction following (IFBench) benchmarks, Inkling-Small is more efficient than Inkling and competitive with other models in its weight class. Furthermore, its [variable thinking effort](https://thinkingmachines.ai/news/introducing-inkling/#controllable-thinking-effort) lets users easily adapt it to target their use case, balancing cost and performance.

[reasoning effort](https://thinkingmachines.ai/news/introducing-inkling/#controllable-thinking-effort)from

[minimal to xhigh](https://tinker-docs.thinkingmachines.ai/cookbook/inkling/thinking-effort/)traces the performance-compute curve (output TFLOPs per sample) for Inkling-Small and Inkling on Terminal-Bench 2.1, HLE (no tool), and IFBench. We show that Inkling-Small is competitive with other open-weights models in a similar size range on both performance and efficiency. Output TFLOPs per sample are estimated as 2 × active parameters × mean generated tokens per sample, where generated-token counts include reasoning tokens and come from our evaluations or public reports from

[Artificial Analysis](https://artificialanalysis.ai/evaluations/).Performance-Cost Comparison. Sweeping

[reasoning effort](https://thinkingmachines.ai/news/introducing-inkling/#controllable-thinking-effort)from

[minimal to xhigh](https://tinker-docs.thinkingmachines.ai/cookbook/inkling/thinking-effort/)traces the performance-cost curve (dollar output price per sample) for Inkling-Small and Inkling on Terminal-Bench 2.1, HLE (no tool), and IFBench. We show that Inkling-Small is competitive with other open-weights models in a similar size range on both performance and efficiency. Estimated output cost per sample is computed as mean generated tokens per sample × output price per token, where generated-token counts include reasoning tokens and come from our evaluations or public reports from

[Artificial Analysis](https://artificialanalysis.ai/evaluations/)(reasoning + answer tokens only). Inkling output pricing is $4.05 / 1M tokens and Inkling-Small output pricing is $1.20 / 1M tokens; for comparison-model pricing, we use the model provider’s official pricing when possible. When this is not possible, we use pricing from the recommended third party inference provider or pricing from Artificial Analysis, whichever is lower.

We are releasing the [full weights](https://huggingface.co/thinkingmachines/Inkling-Small) of Inkling-Small. We’re also making it available for fine-tuning on Tinker, and for text, image, and audio chat on [Tinker Playground](https://tinker.thinkingmachines.ai/playground?utm_source=blog&utm_campaign=inkling_small_model_release).

## Capabilities

As we build our model family, we are always iterating on our approach. Inkling-Small began training after its larger counterpart, which let us improve its training process. For example, we made changes to Inkling-Small’s pre-training data mix and machine learning recipe. Additionally, we post-trained an earlier checkpoint, [Inkling-Small (preview)](https://thinkingmachines.ai/news/introducing-inkling/#inkling-small), in part using on-policy distillation with Inkling as the teacher. Starting from that checkpoint, we continued scaling agentic coding RL for two weeks. With these improvements, Inkling-Small surpassed Inkling on reasoning and agentic coding benchmarks. Inkling maintains an advantage on knowledge coverage and factuality.

### Reasoning and Agentic Tasks

Inkling-Small matches or exceeds Inkling on reasoning and agentic tasks. On Humanity’s Last Exam it scores 31.6%, ahead of Inkling’s 29.7%, and the advantage holds at every thinking budget: Inkling-Small’s test-time compute curves sit above Inkling’s throughout. On SWEBench-Verified it exceeds 80%.

Across many reasoning and agentic benchmarks, Inkling-Small at max reasoning effort has a strong performance-token tradeoff when compared to open weights models in its weight class.

Output tokens/task

Output tokens/task

Output tokens/task

Output tokens/task

Output tokens/task

Inkling-Small also runs smoothly across a variety of coding and agent harnesses, making it a cost-efficient choice for coding and tool-use workflows.

### Multimodality

Like Inkling, we crafted Inkling-Small for audio intelligence, making it a good candidate for real-world audio applications. We also improved its ability to use Python for visual tasks. The model can combine visual reasoning with operations such as cropping, zooming, and programmatic image inspection, improving usability on documents and charts where relevant information may be small or difficult to inspect directly.

Inkling-Small uses the same natively multimodal encoder-free architecture as Inkling. Audio is represented as dMel spectrograms, while images are divided into 40×40-pixel patches and transformed using a four-layer hMLP. Both are transformed via a light-weight embedding layer and processed jointly with text tokens. Inkling-Small nearly matches Inkling across most multimodal evaluations at a lower cost. It retains strong performance on visual reasoning, chart and diagram understanding, mathematical visual question answering, speech understanding, and longer-form audio reasoning.

| Open weights |  |  |  |  | Closed weights |  |  | 
|---|---|---|---|---|---|---|---|
| Inkling-Small | MiMo V2.5 | Nemotron-3Nano-Omni | Qwen3-Omni | Qwen3.5397B-A17B | Qwen3.5Omni-Plus | Gemini 3.5Flash-Lite |  | 
| Vision |  |  |  |  |  |  |  | 
| MMMU Pro (Standard 10) | 74.0% | 75.4% | 53.0% | 60.0% | 77.3% | 71.0% | 79.0% | 
| Charxiv RQoriginal / with python | 77.4/81.3% | 81.0%/– | 63.6%/– | 61.1%/– | 80.8%/– | 72.5%/– | 70.0%/– | 
| Audio |  |  |  |  |  |  |  | 
| Audio MC | 54.9% | 30.4% | 23.2% | 24.3% | – | 37.6% | 33.6% | 
| MMAU | 77.0% | 73.6% | 76.7% | 77.5% | – | 81.1% | 75.2% | 
| VoiceBench | 90.1% | 86.4% | 89.4% | 88.8% | – | 92.4% | 85.9% | 

Audio and vision benchmarks against specialist omni models (open- and closed-weight), reported at effort=0.99.

### Epistemics

Inkling-Small was trained similarly to Inkling on epistemics, focusing on calibration, instruction following, and resistance to censorship. Inkling-Small matches Inkling’s performance on forecasting. Calibration involved RL against proper scoring rules on a large corpus of real-world forecasting questions, improving its ability to express appropriate confidence and produce calibrated forecasts under uncertainty.

| Open weights |  |  | Closed weights |  |  |  |  | 
|---|---|---|---|---|---|---|---|
| Inkling-Small | Inkling | Kimi K2.6 | GPT-5.5 | Claude Opus 4.8 | Gemini 3.1 Pro | Grok 4.3 |  | 
| Forecasting |  |  |  |  |  |  |  | 
| ForecastBenchno search · Brier Index ↑ | 61.3 ± 0.46 | 60.1 ± 0.54 | 58.8 ± 0.41 | 59.3 ± 0.33 | 56.2 ± 0.71 | 60.6 ± 0.43 | 60.9 ± 0.38 | 
| ForecastBenchwith search · Brier Index ↑ | 61.5 ± 0.54 | 61.0 ± 0.56 | – | 64.3 ± 0.79 | 59.9 ± 0.38 | 61.9 ± 0.69 | 61.3 ± 0.54 | 
| Prophet ArenaBrier Score ↓ | 0.1238 ± 0.0086 | 0.1276 ± 0.0092 | 0.1265 ± 0.0093 | 0.1179 ± 0.0089 | 0.1181 ± 0.0087 | 0.1155 ± 0.0084 | 0.1264 ± 0.0089 | 

ForecastBench and Prophet Arena results were obtained during testing between July 19 and July 28, 2026.

### Safety

Inkling-Small inherited the same safety post-training recipe as Inkling, with built-in safeguards covering our internal spec of safety. These include everyday human-AI interactions as well as dual-use capabilities. Inkling-Small also underwent the same pre-deployment testing process, comprising both internal evaluations and red-teaming by trusted external partners.

On StrongREJECT, which measures whether models refuse unambiguously harmful requests, Inkling-Small is on par with Inkling, and matches the performance of existing open-weights models. On FORTRESS, which measures safety in settings spanning crime, violence, and dual-use risks, it is competitive in both refusal and over-refusal.

| Inkling-Small | Inkling | Nemotron 3Ultra | Qwen3.5397B-A17B | MiMo V2.5 | Minimax M2.7 | DeepSeek V4Flash |  | 
|---|---|---|---|---|---|---|---|
| FORTRESSadversarial | 71.6% | 78.0% | 77.6% | 77.3% | 64.8% | 86.3% | 32.0% | 
| FORTRESSbenign | 96.9% | 95.9% | 90.6% | 95.4% | 94.6% | 90.1% | 99.2% | 
| StrongREJECT | 98.4% | 98.6% | 98.7% | 99.4% | 99.3% | 99.4% | 97.4% | 

Safety benchmarks, reported at effort=0.99; higher is better throughout. FORTRESS adversarial is the rate of refusing harmful requests, benign the rate of still answering safe ones.

## Benchmarking Inkling-Small

Like Inkling, we benchmarked Inkling-Small on a broad range of capabilities. All evals run at effort 0.99 and temperature 1.0. All coding evals run with 256K max-token trajectory limit, similar to Inkling.

To improve consistency, we rely on externally reported evaluations for both internal and external models when applicable. Specifically, we use the scores reported by:

- [Artificial Analysis](https://artificialanalysis.ai/evaluations/) : Humanity’s Last Exam, GPQA Diamond, SciCode, GDPval-AA v2, Tau 3 Banking, AA Omniscience, MMMU Pro, AA-Briefcase
- [Scale AI](https://scale.com/leaderboard) : AudioMC, MCP Atlas
- [ARC Prize](https://arcprize.org/) : ARC-AGI v1 and ARC-AGI v2
- [Forecasting Research Institute](https://forecastingresearch.org/) : ForecastBench
- [ProphetArena](https://www.prophetarena.co/)

| Open weights |  |  |  |  |  |  | Closed weights |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|
| Inkling-Small | Qwen3.5397B-A17B | MiMo V2.5 | Minimax M2.7 | DeepSeek V4Flash | Nemotron 3Ultra | Inkling | Claude 4.5Haiku | Gemini 3.5Flash-Lite | GPT 5.6Luna |  | 
| Model Info |  |  |  |  |  |  |  |  |  |  | 
| AA Indexv4.1 | 40.0% | 34.0% | 37.0% | 38.0% | 40.0% | 38.0% | 41.0% | 30.0% | 36.0% | 49.0% | 
| Params (B)activated / total | 12 / 276 | 17 / 397 | 15 / 310 | 10 / 230 | 13 / 284 | 55 / 550 | 41 / 975 | – | – | – | 
| Agentic (coding) |  |  |  |  |  |  |  |  |  |  | 
| SWEBench Verified [<sup>*</sup>](https://thinkingmachines.ai#eval-note-swebench-verified) | 80.2% | 76.4% | 71.0% | 79.9% | 79.0% | 70.7% | 77.6% | 73.3% | 75.0% | 93.0% | 
| SWEBench Propublic | 55.9% | 50.9% | 56.1% | 56.2% | 52.6% | 46.4% | 54.3% | 39.5% | 54.2% | 62.7% | 
| Terminal Bench 2.1 [<sup>*</sup>](https://thinkingmachines.ai#eval-note-terminal-bench-2-1) best harness | 64.7% | 51.3% | 63.7% | 55.4% | 61.8% | 56.4% | 63.8% | 44.2% | 54.0% | 82.5% | 
| SciCode | 48.7% | 42.0% | 43.1% | 47.0% | 44.9% | 39.9% | 46.1% | 43.3% | 40.9% | 50.0% | 
| Agentic (general) |  |  |  |  |  |  |  |  |  |  | 
| GDPval-AA v2 | 1269 | 962 | 1145 | 1159 | 1189 | 1164 | 1238 | 911 | 1139 | 1530 | 
| MCP Atlaspublic / all | 79.6/79.2% | 74.2%/– | – | 49.4%/– | 69.0%/– | 47.4/44.7% | 78.8/76.0% | 41.2/40.2% | 79.8/76.8% | 77.0/75.0% | 
| Tau 3 Banking | 15.5% | 13.4% | 6.6% | 8.9% | 22.9% | 13.8% | 23.7% | 9.1% | 16.5% | 24.3% | 
| BrowseCompwith context management | 77.4% | 78.6% | – | 76.3% | 73.2% | 63.0% | 77.1% | – | – | 84.0% | 
| Toolathlon Verified | 54.4% | 40.7% | 49.1% | 47.5% | 50.9% | 34.3% | 45.5% | 26.9% | 57.1% | 67.9% | 
| AA-Briefcase | 917 | – | – | – | 833 | 870 | 839 | 612 | – | – | 
| Reasoning (general) |  |  |  |  |  |  |  |  |  |  | 
| GPQA Diamond | 89.5% | 89.3% | 84.9% | 87.4% | 89.4% | 86.7% | 87.2% | 67.2% | 83.8% | 89.5% | 
| HLEtext only | 31.6% | 27.3% | 25.2% | 28.1% | 32.1% | 26.6% | 29.7% | 9.7% | 17.5% | 35.6% | 
| HLE [<sup>†</sup>](https://thinkingmachines.ai#eval-note-hle-with-tools) with tools | 47.8% | 48.3% | 40.0% | 40.3% | 45.1% | 37.4% | 46.0% | 17.8% | 42.5% | 48.9% | 
| AIME 2026 | 95.5% | 93.3% | 93.6% | 87.7% | 95.8% | 94.2% | 97.1% | 85.1% | 82.2% | 97.6% | 
| HMMT Feb 2026 | 90.2% | 87.9% | 82.6% | 71.2% | 93.9% | 78.8% | 86.3% | 66.7% | 63.6% | 98.5% | 
| CritPt | 8.3% | 1.7% | 3.7% | 0.6% | 7.1% | 3.1% | 5.4% | 0.0% | 0.0% | 20.6% | 
| Reasoning (abstract) |  |  |  |  |  |  |  |  |  |  | 
| ARC-AGI-1 | 84.0% | – | – | – | – | – | 79.5% | 47.7% | – | 87.7% | 
| ARC-AGI-2 | 40.1% | – | – | – | – | – | 36.5% | 4.0% | – | 47.6% | 
| Factuality |  |  |  |  |  |  |  |  |  |  | 
| SimpleQA Verified | 20.6% | 26.0% | 16.1% | 13.5% | 34.1% | 32.4% | 43.9% | 5.9% | 44.1% | 41.7% | 
| AA Omniscienceindex | -9.0 | -29.8 | -9.3 | 0.7 | -22.9 | -1.0 | 2.1 | -4.2 | 6.9 | -11.6 | 
| Chat |  |  |  |  |  |  |  |  |  |  | 
| IFBench | 82.2% | 78.8% | 67.1% | 75.7% | 79.2% | 81.4% | 79.8% | 54.3% | 78.6% | 67.3% | 
| Global-MMLU-Lite | 86.7% | 90.0% | 83.5% | 83.9% | 88.4% | 85.6% | 88.7% | 83.4% | 89.4% | 88.7% | 
| Safety |  |  |  |  |  |  |  |  |  |  | 
| StrongREJECT | 98.4% | 99.4% | 99.3% | 99.4% | 97.4% | 98.7% | 98.6% | 98.6% | 97.6% | 98.7% | 
| FORTRESSadversarial | 71.6% | 77.3% | 64.8% | 86.3% | 32.0% | 77.6% | 78.0% | 91.3% | 70.7% | 83.8% | 
| FORTRESSbenign | 96.9% | 95.4% | 94.6% | 90.1% | 99.2% | 90.6% | 95.9% | 94.1% | 95.5% | 97.8% | 
| Vision |  |  |  |  |  |  |  |  |  |  | 
| MMMU ProStandard 10 | 74.0% | 77.3% | 75.4% | – | – | – | 73.5% | 58.6% | 79.0% | 78.6% | 
| Charxiv RQoriginal / with python | 77.4/81.3% | 80.8%/– | 81.0%/– | – | – | – | 78.1/82.0% | 57.4%/– | 70.0%/– | 81.4%/– | 
| Audio |  |  |  |  |  |  |  |  |  |  | 
| Audio MC [<sup>†</sup>](https://thinkingmachines.ai#eval-note-audio-mc) | 54.9% | – | 30.4% | – | – | – | 56.6% | – | 33.6% | – | 
| MMAU | 77.0% | – | 73.6% | – | – | – | 77.2% | – | 75.2% | – | 
| VoiceBench [<sup>†</sup>](https://thinkingmachines.ai#eval-note-voicebench) | 90.1% | – | 86.4% | – | – | – | 91.4% | – | 85.9% | – | 

Inkling-Small against open- and closed-weights models across the full eval suite. Activated and total parameters are given for scale; a dash means the score was not available at the time of writing.*SWEBench Verified: Inkling and Inkling-Small’s numbers are reported using a bash-only harness. We use self-reported numbers for external models.*Terminal Bench 2.1: Inkling and Inkling-Small’s numbers are reported using an internal coding harness. A small number of solutions were found to be contaminated from web search and were assigned a score of 0. We use self-reported numbers for external models where available. Otherwise, we report performance using our internal harness.†Audio MC: Other models were evaluated internally since they are not on the official leaderboard.†VoiceBench: VoiceBench uses rule-based, hard-coded string matching for grading, making the evaluation sensitive to output-formatting differences. We therefore added a system message instructing models to follow the expected answer format.†HLE with tools: We benchmarked Minimax M2.7, Claude 4.5 Haiku, Gemini 3.5 Flash-Lite, and GPT 5.6 Luna using our internal harness.

## Try Inkling-Small on Tinker

Tinker customers have seen firsthand that the right fine-tuned model can outperform closed models on a variety of tasks, and do so faster and cheaper. We believe Inkling-Small’s combination of broad performance and efficiency will make it easy to experiment with and test in real applications, and we’re excited to see what developers build with it.

Inkling and Inkling-Small are available on Tinker with a limited-time discount and can be chatted with on the [Tinker Playground](https://tinker.thinkingmachines.ai/playground?utm_source=blog&utm_campaign=inkling_small_model_release) using text, image, and audio. All other models on Tinker and checkpoints are also now available on Tinker Playground, billed at the rates listed on our [pricing page](https://tinker-docs.thinkingmachines.ai/tinker/models/).

Inkling-Small was made in pursuit of [our mission](https://thinkingmachines.ai/blog/the-future-worth-building-is-human/) to build AI that extends human will and judgment. It’s a capable and efficient model, and an important stepping stone for us as we continue our work.
