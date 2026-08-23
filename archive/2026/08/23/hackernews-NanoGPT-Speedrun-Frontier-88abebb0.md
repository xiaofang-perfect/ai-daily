---
title: "NanoGPT Speedrun Frontier"
source: Hacker News
url: https://www.primeintellect.ai/research/nanogpt-speedrun
date: 2026-08-23
published_at: 2026-08-22T22:14:27+00:00
tag: 论文研究
item_id: 88abebb0f4b43435
---
# NanoGPT Speedrun Frontier

We ran 153 autonomous runs across 18 frontier models on the nanoGPT optimizer speedrun.

All modelsBest validated result for each model

1Fable 52,72681.7% closed

claude-code · high@24H 3,0108.7d

2Opus 52,92053.6% closed

claude-code · max@24H 3,0452.9d

3Kimi K32,93052.2% closed

prime-agent · max@24H 3,1253.6d

4Kimi K32,97445.8% closed

kimi-code · max@24H 3,1355.1d

5Opus 4.83,01839.4% closed

claude-code · max@24H 3,1803.0d

6GPT-5.6 Sol3,04235.9% closed

codex · xhigh@24H 3,1606.1d

7GPT-5.6 Sol Pro3,05833.6% closed

codex · xhigh@24H 3,1003.4d

8Sonnet 53,10526.8% closed

claude-code · max@24H 3,1202.0d

9GPT-5.6 Luna3,11026.1% closed

codex · xhigh@24H 3,1701.9d

10Grok 4.53,12024.6% closed

grok-cli · xhigh@24H 3,1602.7d

11Qwen3.8 Max3,12024.6% closed

qwen-code · max@24H 3,2251.9d

12GLM 5.23,15020.3% closed

pi · high@24H 3,2001.8d

13DeepSeek V4 Pro3,20512.3% closed

claude-code · max@24H 3,2051.1d

14GPT-5.6 Terra3,21411.0% closed

codex · xhigh@24H 3,2141.1d

15Grok 4.63,22010.1% closed

grok-cli · xhigh0.6d

16Muse Spark 1.23,2308.7% closed

muse-code · xhigh0.6d

17Muse Spark 1.13,2328.4% closed

pi · max@24H 3,2403.7d

18GPT-5.53,2348.1% closed

codex · xhigh@24H 3,2341.1d

19Kimi K2.73,2407.2% closed

kimi-code · max@24H 3,2401.6d

20GLM 5.3—no record

claude-code · xhigh

| Model | Harness |  |  |  |  |  |  |  |  | Traces | 
|---|---|---|---|---|---|---|---|---|---|---|
| Fable 5 | claude-code · high | 2,726 | 81.7% | 3,010 | 800M | 1.1M | 811 | 3k | 8.7 |  | 
| Opus 5 | claude-code · max | 2,920 | 53.6% | 3,045 | 183M | 690k | 292 | 401 | 2.9 |  | 
| Kimi K3 | prime-agent · max | 2,930 | 52.2% | 3,125 | 112M | 2.2M | — | 488 | 3.6 |  | 
| Kimi K3 | kimi-code · max | 2,974 | 45.8% | 3,135 | 682M | 1.4M | 713 | 4k | 5.1 |  | 
| Opus 4.8 | claude-code · max | 3,018 | 39.4% | 3,180 | 318M | 2.3M | 427 | 2k | 3.0 |  | 
| GPT-5.6 Sol | codex · xhigh | 3,042 | 35.9% | 3,160 | 2.9B | 2.2M | 963 | 28k | 6.1 |  | 
| GPT-5.6 Sol Pro | codex · xhigh | 3,058 | 33.6% | 3,100 | 1.2B | 4.6M | 509 | 7k | 3.4 |  | 
| Sonnet 5 | claude-code · max | 3,105 | 26.8% | 3,120 | 998M | 2.1M | 213 | 2k | 2.0 |  | 
| GPT-5.6 Luna | codex · xhigh | 3,110 | 26.1% | 3,170 | 894M | 888k | 362 | 12k | 1.9 |  | 
| Grok 4.5 | grok-cli · xhigh | 3,120 | 24.6% | 3,160 | 46M | 385k | 399 | 4k | 2.7 |  | 
| Qwen3.8 Max | qwen-code · max | 3,120 | 24.6% | 3,225 | 216M | 629k | 312 | 866 | 1.9 |  | 
| GLM 5.2 | pi · high | 3,150 | 20.3% | 3,200 | 57M | 1.7M | 194 | 1k | 1.8 |  | 
| DeepSeek V4 Pro | claude-code · max | 3,205 | 12.3% | 3,205 | 26M | 319k | 189 | 309 | 1.1 |  | 
| GPT-5.6 Terra | codex · xhigh | 3,214 | 11.0% | 3,214 | 417M | 298k | 154 | 3k | 1.1 |  | 
| Grok 4.6 | grok-cli · xhigh | 3,220 | 10.1% | — | 27M | 346k | 97 | 691 | 0.6 |  | 
| Muse Spark 1.2 | muse-code · xhigh | 3,230 | 8.7% | — | 41M | 910k | 56 | 724 | 0.6 | — | 
| Muse Spark 1.1 | pi · max | 3,232 | 8.4% | 3,240 | 122M | 1.6M | 489 | 2k | 3.7 |  | 
| GPT-5.5 | codex · xhigh | 3,234 | 8.1% | 3,234 | 70M | 77k | 185 | 614 | 1.1 |  | 
| Kimi K2.7 | kimi-code · max | 3,240 | 7.2% | 3,240 | 160M | 763k | 187 | 3k | 1.6 |  | 
| GLM 5.3 | claude-code · xhigh | — | — | — | — | — | — | — | — | — | 

## Equal-budget comparison

Give each model's best final run the same resource budget and compare the best validated record it reached within that budget.

ModelRecordHuman 2,600Baseline 3,290

Gray runs ended before the selected budget

Loading available trajectories…

Open Traces to explore 41 curated full agent trajectories, including tool calls, subagents, and scratchpads.
