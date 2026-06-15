---
title: "Rio de Janeiro's 'homegrown' LLM appears to be a merge of an existing model"
source: Hacker News
url: https://github.com/nex-agi/Nex-N2/issues/4
date: 2026-06-15
published_at: 2026-06-14T15:37:31+00:00
tag: 行业动态
item_id: a53440a62179c013
---
`prefeitura-rio/Rio-3.5-Open-397B`[IplanRIO](https://iplanrio.rio.rj.gov.br/). It is not. Its weights are a **direct element-wise merge of our model, Nex, with the official **`Qwen3.5-397B-A17B` — about **0.6 Nex / 0.4 Qwen** — and we find **no evidence of any training of their own.** We can show this **two completely independent ways**:

- **With Rio's hard-coded "You are Rio" system prompt removed, its own deployed model identifies itself as "Nex, from Nex-AGI" 79% of the time — and as "Rio" 0% of the time.**It even recites our organization's bespoke backstory word-for-word.
- **Every weight tensor in Rio is, to thousands of standard deviations, the same 0.6/0.4 blend of Nex and Qwen**— across all 60 layers and every component of the network. Other finetunes cannot be explained as interpolations.

Below is the evidence. Judge for yourself.

`prefeitura-rio/Rio-3.5-Open-397B`is presented as an original 397B model trained by IplanRIO. It is not. Its weights are adirect element-wise merge of our model, Nex, with the official— about`Qwen3.5-397B-A17B`base0.6 Nex / 0.4 Qwen— and we findno evidence of any training of their own.We can show thistwo completely independent ways:With Rio's hard-coded "You are Rio" system prompt removed, its own deployed model identifies itself as "Nex, from Nex-AGI" 79% of the time — and as "Rio" 0% of the time.It even recites our organization's bespoke backstory word-for-word.Every weight tensor in Rio is, to thousands of standard deviations, the same 0.6/0.4 blend of Nex and Qwen— across all 60 layers and every component of the network. Other finetunes cannot be explained as interpolations.Below is the evidence. Judge for yourself.
