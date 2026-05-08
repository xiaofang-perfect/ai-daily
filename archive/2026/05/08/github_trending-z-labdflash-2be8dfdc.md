---
title: "z-lab/dflash"
source: GitHub Trending
url: https://github.com/z-lab/dflash
date: 2026-05-08
published_at: 2026-05-08T04:51:58.907377+00:00
tag: 工具开源
item_id: 2be8dfdcab9744c0
---
**DFlash** is a lightweight **block diffusion** model designed for speculative decoding. It enables efficient and high-quality parallel drafting.

## DFlash_demo.mp4

| Model | DFlash Draft |
|---|---|
| gemma-4-26B-A4B-it |
|

[z-lab/gemma-4-31B-it-DFlash](https://huggingface.co/z-lab/gemma-4-31B-it-DFlash)[z-lab/Qwen3.6-27B-DFlash](https://huggingface.co/z-lab/Qwen3.6-27B-DFlash)[z-lab/Qwen3.6-35B-A3B-DFlash](https://huggingface.co/z-lab/Qwen3.6-35B-A3B-DFlash)[z-lab/MiniMax-M2.5-DFlash](https://huggingface.co/z-lab/MiniMax-M2.5-DFlash)[z-lab/Kimi-K2.5-DFlash](https://huggingface.co/z-lab/Kimi-K2.5-DFlash)[z-lab/Qwen3.5-4B-DFlash](https://huggingface.co/z-lab/Qwen3.5-4B-DFlash)[z-lab/Qwen3.5-9B-DFlash](https://huggingface.co/z-lab/Qwen3.5-9B-DFlash)[z-lab/Qwen3.5-27B-DFlash](https://huggingface.co/z-lab/Qwen3.5-27B-DFlash)[z-lab/Qwen3.5-35B-A3B-DFlash](https://huggingface.co/z-lab/Qwen3.5-35B-A3B-DFlash)[z-lab/Qwen3.5-122B-A10B-DFlash](https://huggingface.co/z-lab/Qwen3.5-122B-A10B-DFlash)[z-lab/Qwen3-Coder-Next-DFlash](https://huggingface.co/z-lab/Qwen3-Coder-Next-DFlash)[z-lab/Qwen3-Coder-30B-A3B-DFlash](https://huggingface.co/z-lab/Qwen3-Coder-30B-A3B-DFlash)[z-lab/gpt-oss-20b-DFlash](https://huggingface.co/z-lab/gpt-oss-20b-DFlash)[z-lab/gpt-oss-120b-DFlash](https://huggingface.co/z-lab/gpt-oss-120b-DFlash)[z-lab/Qwen3-4B-DFlash-b16](https://huggingface.co/z-lab/Qwen3-4B-DFlash-b16)[z-lab/Qwen3-8B-DFlash-b16](https://huggingface.co/z-lab/Qwen3-8B-DFlash-b16)[z-lab/LLaMA3.1-8B-Instruct-DFlash-UltraChat](https://huggingface.co/z-lab/LLaMA3.1-8B-Instruct-DFlash-UltraChat)Feel free to open a GitHub issue to request support for additional models. We will also open-source the training recipe soon, so you can train your own DFlash draft model to accelerate any LLM.


Use a separate virtual environment for each to avoid conflict.

| Backend | Install command |
|---|---|
Transformers |
`uv pip install -e ".[transformers]"` |
SGLang |
`uv pip install -e ".[sglang]"` |
vLLM |
See below |
MLX (Apple Silicon) |
`pip install -e ".[mlx]"` |

**vLLM:** vLLM v0.20.1+ includes core DFlash support. Use the standard install for most models:

`uv pip install -e ".[vllm]"`

Gemma4 DFlash currently needs our temporary vLLM Gemma4 build. Docker is recommended:

`docker pull ghcr.io/z-lab/vllm-openai:gemma4-dflash-cu130`

Source fallback for Gemma4:

```
uv pip install -U --torch-backend=auto \
"vllm @ git+https://github.com/vllm-project/vllm.git@refs/pull/41703/head"
```

Newer non-Gemma4 SWA draft models use the SWA support branch:

```
uv pip install -U --torch-backend=auto \
"vllm @ git+https://github.com/vllm-project/vllm.git@refs/pull/40898/head"
```

Gemma4 with Docker:

```
docker run --rm -it \
--gpus all \
--ipc=host \
--shm-size=16g \
-p 8000:8000 \
-v ~/.cache/huggingface:/root/.cache/huggingface \
ghcr.io/z-lab/vllm-openai:gemma4-dflash-cu130 \
google/gemma-4-26B-A4B-it \
--host 0.0.0.0 \
--port 8000 \
--speculative-config '{"method": "dflash", "model": "z-lab/gemma-4-26B-A4B-it-DFlash", "num_speculative_tokens": 15, "attention_backend": "flash_attn"}' \
--attention-backend triton_attn \
--max-num-batched-tokens 32768 \
--trust-remote-code
```

Non-Gemma4 models:

```
vllm serve Qwen/Qwen3.5-27B \
--speculative-config '{"method": "dflash", "model": "z-lab/Qwen3.5-27B-DFlash", "num_speculative_tokens": 15}' \
--attention-backend flash_attn \
--max-num-batched-tokens 32768
```

```
export SGLANG_ALLOW_OVERWRITE_LONGER_CONTEXT_LEN=1
# Optional: enable schedule overlapping (experimental, may not be stable)
# export SGLANG_ENABLE_SPEC_V2=1
# export SGLANG_ENABLE_DFLASH_SPEC_V2=1
# export SGLANG_ENABLE_OVERLAP_PLAN_STREAM=1
python -m sglang.launch_server \
--model-path Qwen/Qwen3.5-35B-A3B \
--speculative-algorithm DFLASH \
--speculative-draft-model-path z-lab/Qwen3.5-35B-A3B-DFlash \
--speculative-num-draft-tokens 16 \
--tp-size 1 \
--attention-backend trtllm_mha \
--speculative-draft-attention-backend fa4 \
--mem-fraction-static 0.75 \
--mamba-scheduler-strategy extra_buffer \
--trust-remote-code
```

Only Qwen3 and LLaMA-3.1 models support the Transformers backend.

```
from transformers import AutoModel, AutoModelForCausalLM, AutoTokenizer
draft = AutoModel.from_pretrained("z-lab/Qwen3-8B-DFlash-b16", trust_remote_code=True, dtype="auto", device_map="cuda:0").eval()
target = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-8B", dtype="auto", device_map="cuda:0").eval()
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-8B")
messages = [{"role": "user", "content": "How many positive whole-number divisors does 196 have?"}]
input_ids = tokenizer.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True, enable_thinking=False).to(draft.device)
output = draft.spec_generate(input_ids=input_ids, max_new_tokens=2048, temperature=0.0, target=target, stop_token_ids=[tokenizer.eos_token_id])
print(tokenizer.decode(output[0], skip_special_tokens=False))
```

There have been many great community DFlash implementations on MLX; we provide a simple and efficient one here, tested on an Apple M5 Pro with Qwen3, Qwen3.5 and Gemma-4 models.

```
from dflash.model_mlx import load, load_draft, stream_generate
model, tokenizer = load("Qwen/Qwen3.5-4B")
draft = load_draft("z-lab/Qwen3.5-4B-DFlash")
messages = [{"role": "user", "content": "How many positive whole-number divisors does 196 have?"}]
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True, enable_thinking=True)
tps = 0.0
for r in stream_generate(model, draft, tokenizer, prompt, block_size=16, max_tokens=2048, temperature=0.6):
print(r.text, end="", flush=True)
tps = r.generation_tps
print(f"\nThroughput: {tps:.2f} tok/s")
```

All benchmarks share the same datasets (gsm8k, math500, humaneval, mbpp, mt-bench). Datasets are automatically downloaded and cached as JSONL in `cache/`

on first run.

**vLLM**:

```
python -m dflash.benchmark --backend vllm \
--base-url http://127.0.0.1:8000 --model Qwen/Qwen3.5-27B \
--dataset gsm8k --num-prompts 128 --concurrency 1 --enable-thinking
```

**SGLang**:

```
python -m dflash.benchmark --backend sglang \
--base-url http://127.0.0.1:30000 --model Qwen/Qwen3.5-35B-A3B \
--dataset gsm8k --num-prompts 128 --concurrency 1 --enable-thinking
```

**Transformers** (Qwen3 and LLaMA only):

```
torchrun --nproc_per_node=8 -m dflash.benchmark --backend transformers \
--model Qwen/Qwen3-8B --draft-model z-lab/Qwen3-8B-DFlash-b16 \
--dataset gsm8k --max-samples 128
```

**MLX**:

```
python -m dflash.benchmark --backend mlx \
--model mlx-community/gemma-4-31b-it-4bit --draft-model z-lab/gemma-4-31B-it-DFlash \
--dataset gsm8k --max-samples 128 --enable-thinking
```

Huge thanks to [@dcw02](https://github.com/dcw02), [@gongy](https://github.com/gongy), and the team at [@modal-labs](https://github.com/modal-labs) for their fast, high-quality support in bringing DFlash to SGLang. And huge thanks as well to [@benchislett](https://github.com/benchislett) at NVIDIA for his work in bringing DFlash to vLLM and helping make it available to the broader serving community.

If you find DFlash useful, please cite our work. To share feedback on DFlash or request new model support, please fill out this form: [DFlash Feedback](https://forms.gle/4YNwfqb4nJdqn6hq9).

```
@article{chen2026dflash,
title = {{DFlash: Block Diffusion for Flash Speculative Decoding}},
author = {Chen, Jian and Liang, Yesheng and Liu, Zhijian},
journal = {arXiv preprint arXiv:2602.06036},
year = {2026}
}
```
