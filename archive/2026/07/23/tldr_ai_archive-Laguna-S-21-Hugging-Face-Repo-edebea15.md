---
title: "Laguna S 2.1 (Hugging Face Repo)"
source: TLDR AI · 2026-07-22
url: https://huggingface.co/poolside/Laguna-S-2.1?utm_source=tldrai
date: 2026-07-23
published_at: 2026-07-22T12:00:00+00:00
tag: 工具开源
item_id: edebea15281541db
---
Collection  Our most capable model to date, designed for long-horizon work.  • 12 items • Updated  •  23

#   ![](https://cdn-avatars.huggingface.co/v1/production/uploads/699484cbe85a4b61cbc5ee0f/GpYWuz-CovEFgbPOW21dZ.png) 

   [poolside](https://huggingface.co/poolside)  /            

 ![](https://cdn-avatars.huggingface.co/v1/production/uploads/699484cbe85a4b61cbc5ee0f/GpYWuz-CovEFgbPOW21dZ.png) 

  [poolside](https://huggingface.co/poolside)

[  Text Generation  ](https://huggingface.co/models?pipeline_tag=text-generation)

[  Transformers  ](https://huggingface.co/models?library=transformers)

[  Safetensors  ](https://huggingface.co/models?library=safetensors)

[  laguna  ](https://huggingface.co/models?other=laguna)

[  laguna-s-2.1  ](https://huggingface.co/models?other=laguna-s-2.1)

[  vllm  ](https://huggingface.co/models?other=vllm)

[  conversational  ](https://huggingface.co/models?other=conversational)

[  custom_code  ](https://huggingface.co/models?other=custom_code)

[  Eval Results  ](https://huggingface.co/models?other=eval-results)

### Instructions to use poolside/Laguna-S-2.1 with libraries, inference providers, notebooks, and local apps. Follow these links to get started.

- Libraries
- [Transformers](https://huggingface.co/poolside/Laguna-S-2.1?library=transformers)- How to use poolside/Laguna-S-2.1 with Transformers: - `# Use a pipeline as a high-level helper from transformers import pipeline pipe = pipeline("text-generation", model="poolside/Laguna-S-2.1", trust_remote_code=True) messages = [ {"role": "user", "content": "Who are you?"}, ] pipe(messages)`- `# Load model directly from transformers import AutoTokenizer, AutoModelForCausalLM tokenizer = AutoTokenizer.from_pretrained("poolside/Laguna-S-2.1", trust_remote_code=True) model = AutoModelForCausalLM.from_pretrained("poolside/Laguna-S-2.1", trust_remote_code=True, device_map="auto") messages = [ {"role": "user", "content": "Who are you?"}, ] inputs = tokenizer.apply_chat_template( messages, add_generation_prompt=True, tokenize=True, return_dict=True, return_tensors="pt", ).to(model.device) outputs = model.generate(**inputs, max_new_tokens=40) print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:]))`
- Notebooks
- [Google Colab](https://huggingface.co/poolside/Laguna-S-2.1/colab)
- [Kaggle](https://huggingface.co/poolside/Laguna-S-2.1/kaggle)
- Local Apps [Settings](https://huggingface.co/settings/local-apps)
- [vLLM](https://huggingface.co/poolside/Laguna-S-2.1?local-app=vllm)- How to use poolside/Laguna-S-2.1 with vLLM: - ##### Install from pip and serve model- `# Install vLLM from pip: pip install vllm # Start the vLLM server: vllm serve "poolside/Laguna-S-2.1" # Call the server using curl (OpenAI-compatible API): curl -X POST "http://localhost:8000/v1/chat/completions" \ -H "Content-Type: application/json" \ --data '{ "model": "poolside/Laguna-S-2.1", "messages": [ { "role": "user", "content": "What is the capital of France?" } ] }'`- ##### Use Docker- docker model run hf.co/poolside/Laguna-S-2.1 
- [SGLang](https://huggingface.co/poolside/Laguna-S-2.1?local-app=sglang)- How to use poolside/Laguna-S-2.1 with SGLang: - ##### Install from pip and serve model- `# Install SGLang from pip: pip install sglang # Start the SGLang server: python3 -m sglang.launch_server \ --model-path "poolside/Laguna-S-2.1" \ --host 0.0.0.0 \ --port 30000 # Call the server using curl (OpenAI-compatible API): curl -X POST "http://localhost:30000/v1/chat/completions" \ -H "Content-Type: application/json" \ --data '{ "model": "poolside/Laguna-S-2.1", "messages": [ { "role": "user", "content": "What is the capital of France?" } ] }'`- ##### Use Docker images- `docker run --gpus all \ --shm-size 32g \ -p 30000:30000 \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HF_TOKEN=<secret>" \ --ipc=host \ lmsysorg/sglang:latest \ python3 -m sglang.launch_server \ --model-path "poolside/Laguna-S-2.1" \ --host 0.0.0.0 \ --port 30000 # Call the server using curl (OpenAI-compatible API): curl -X POST "http://localhost:30000/v1/chat/completions" \ -H "Content-Type: application/json" \ --data '{ "model": "poolside/Laguna-S-2.1", "messages": [ { "role": "user", "content": "What is the capital of France?" } ] }'`
- [Docker Model Runner](https://huggingface.co/poolside/Laguna-S-2.1?local-app=docker-model-runner)- How to use poolside/Laguna-S-2.1 with Docker Model Runner: - docker model run hf.co/poolside/Laguna-S-2.1 

  


  [ Use on OpenRouter](https://openrouter.ai/poolside/laguna-s-2.1) ·
  

[·](https://vercel.com/ai-gateway/models/laguna-s-2.1)

**Use on Vercel AI Gateway**

**Release blog post**# 
	[
		
	](https://huggingface.co#laguna-s-21)
	
		Laguna S 2.1
	

Laguna S 2.1 is a 118B total parameter Mixture-of-Experts model with 8B activated
parameters per token, designed for agentic coding and long-horizon work. It sits
between [Laguna XS 2.1](https://huggingface.co/poolside/Laguna-XS-2.1) (33B-A3B) and
Laguna M.1 (225B-A23B) in the Laguna series and shares the family recipe: a
token-choice router with softplus gating over 256 routed experts plus one shared
expert, grouped-query attention, and interleaved full/sliding-window attention.

## 
	[
		
	](https://huggingface.co#highlights)
	
		Highlights
	

- **Mixed SWA and global attention layout**: 48 layers in a 1:3 global-to-SWA ratio (12 global attention layers, 36 sliding-window layers, window 512), with softplus attention gating and per-layer-type rotary scales
- **1M context**: 1,048,576-token context window
- **Native reasoning support**: interleaved thinking between tool calls, with per-request control via- `enable_thinking`
- **Speculative decoding**: a trained- [DFlash draft model](https://huggingface.co/poolside/Laguna-S-2.1-DFlash)is available for lower-latency serving
- **Quantized variants**:- [FP8](https://huggingface.co/poolside/Laguna-S-2.1-FP8),- [NVFP4](https://huggingface.co/poolside/Laguna-S-2.1-NVFP4),- [INT4](https://huggingface.co/poolside/Laguna-S-2.1-INT4)and- [GGUF](https://huggingface.co/poolside/Laguna-S-2.1-GGUF)
- **OpenMDW-1.1 license**: Use and modify the model and associated materials freely for commercial and non-commercial purposes (- [learn more about OpenMDW](https://openmdw.ai/))

## 
	[
		
	](https://huggingface.co#model-overview)
	
		Model overview
	

- Number of parameters: 118B total, ~8B activated per token
- Layers: 48 (12 global attention, 36 sliding-window attention)
- Experts: 256 routed (top-10) plus 1 shared expert
- Attention: grouped-query, 8 KV heads, head dim 128; per-head softplus output gating
- Sliding window: 512 tokens
- Context window: 1,048,576 tokens
- Vocabulary: 100,352 tokens (Laguna family tokenizer)
- Modality: text-to-text
- Reasoning: interleaved thinking with preserved thinking

## 
	[
		
	](https://huggingface.co#benchmark-results)
	
		Benchmark results
	

  


| Model | Size | Terminal-Bench 2.1 | SWE-bench Multilingual | SWE-Bench Pro (Public Dataset) | DeepSWE | SWE Atlas (Codebase QnA) | Toolathlon Verified | 
|---|---|---|---|---|---|---|---|
| Laguna S 2.1 | 118B-A8B | 70.2% | 78.5% | 59.4% | 40.4% | 46.2% | 49.7% | 
| Tencent Hy3 | 295B-A21B | 71.7% | 75.8% | 57.9% | - | - | - | 
| Inkling | 975B-A41B | 63.8% | - | 54.3% | - | - | 45.5%* | 
| Nemotron 3 Ultra | 550B-A55B | 56.4% | 67.7% | - | - | - | 34.3%* | 
| DeepSeek-V4-Pro Max | 1.6T-A49B | 64.0%* | 76.2% | 55.4% | 9.0%* | 27.2%* | 55.9%* | 
| Kimi K3 | 2800B-A50B | 88.3% | - | - | 69% | - | - | 
| Qwen 3.7 Max | - | 74.5%* | 78.3% | 60.6% | - | - | - | 
| Muse Spark 1.1 | - | 80% | - | 61.5% | 53.3% | 42.2%* | 75.6% | 
| Claude Fable 5 | - | 88% | - | 80.3% | 70% | - | - | 

Benchmarks as of 21 July 2026. Laguna S 2.1 in **bold**; a dash (-) marks a benchmark a model was not evaluated on. Scores marked * are as reported by third parties: Terminal-Bench 2.1 and DeepSWE via Artificial Analysis, SWE Atlas via Scale AI's official leaderboard, and Toolathlon Verified via its official leaderboard. Full evaluation trajectories: [trajectories.poolside.ai](https://trajectories.poolside.ai).

## 
	[
		
	](https://huggingface.co#usage)
	
		Usage
	

Laguna S 2.1 uses the same `laguna` architecture as Laguna XS 2.1, so the same
engine integrations apply (vLLM, SGLang, Transformers, TRT-LLM, llama.cpp). At 118B
parameters the BF16 checkpoint needs multiple GPUs (roughly 236GB of weights);
quantized variants reduce this substantially.

### 
	[
		
	](https://huggingface.co#vllm)
	
		vLLM
	

```
vllm serve \
    --model poolside/Laguna-S-2.1 \
    --tensor-parallel-size 4 \
    --tool-call-parser poolside_v1 \
    --reasoning-parser poolside_v1 \
    --enable-auto-tool-choice \
    --served-model-name laguna \
    --default-chat-template-kwargs '{"enable_thinking": true}'
```

Optional: speculative decoding with DFlash.Pair with the[Laguna S 2.1 DFlash draft model](https://huggingface.co/poolside/Laguna-S-2.1-DFlash)by adding`--speculative-config '{"model":"poolside/Laguna-S-2.1-DFlash","num_speculative_tokens":7,"method":"dflash"}'`.

### 
	[
		
	](https://huggingface.co#sglang)
	
		SGLang
	

```
python -m sglang.launch_server \
  --model-path poolside/Laguna-S-2.1 \
  --tp-size 4 \
  --reasoning-parser poolside_v1 \
  --tool-call-parser poolside_v1 \
  --trust-remote-code
```
### 
	[
		
	](https://huggingface.co#trt-llm)
	
		TRT-LLM
	

```
trtllm-serve poolside/Laguna-S-2.1 --trust-remote-code \
    --tool_parser poolside_v1 --reasoning_parser laguna
```
Note the flag names differ from vLLM's (`--tool_parser`, and the reasoning parser
is `laguna`, not `poolside_v1`).

### 
	[
		
	](https://huggingface.co#llamacpp)
	
		llama.cpp
	

GGUF conversions are available at
[poolside/Laguna-S-2.1-GGUF](https://huggingface.co/poolside/Laguna-S-2.1-GGUF).
Serve with poolside's llama.cpp fork, branch
[ laguna](https://github.com/poolsideai/llama.cpp/tree/laguna), which carries
full Laguna support including DFlash speculative decoding. (Base Laguna support
is also in upstream review:

[ggml-org/llama.cpp#25165](https://github.com/ggml-org/llama.cpp/pull/25165).)

```
git clone --branch laguna https://github.com/poolsideai/llama.cpp
cd llama.cpp && cmake -B build && cmake --build build -j
./build/bin/llama-server -m laguna-s-2.1-Q4_K_M.gguf --jinja --port 8000
# with DFlash speculative decoding:
./build/bin/llama-server -m laguna-s-2.1-Q4_K_M.gguf \
  -md laguna-s-2.1-DFlash-BF16.gguf \
  --spec-type draft-dflash --spec-draft-n-max 7 -fa on --jinja --port 8000
```
## 
	[
		
	](https://huggingface.co#controlling-reasoning)
	
		Controlling reasoning
	

Laguna S 2.1 has native reasoning support and works best with *preserved thinking*:
keep `reasoning_content` from prior assistant messages in the message history.
The model will generally reason before calling tools and between tool calls, and
may stop reasoning in follow-up steps if prior thinking blocks are dropped.

Thinking is controlled per request via the chat template:

```
extra_body={"chat_template_kwargs": {"enable_thinking": False}}
```
or at the server level with
`--default-chat-template-kwargs '{"enable_thinking": true}'`. For agentic coding
use cases we recommend enabling thinking and preserving reasoning in the message
history.

## 
	[
		
	](https://huggingface.co#license)
	
		License
	

This model is licensed under the [OpenMDW-1.1 License](https://huggingface.co/poolside/Laguna-S-2.1/blob/main/LICENSE.md).

## 
	[
		
	](https://huggingface.co#intended-and-responsible-use)
	
		Intended and Responsible Use
	

Laguna S 2.1 is designed for software engineering and agentic coding use cases, and you are responsible for confirming that it is appropriate for your intended application. Laguna S 2.1 is subject to the [OpenMDW-1.1 License](https://huggingface.co/poolside/Laguna-S-2.1/blob/main/LICENSE.md), and should be used consistently with Poolside's [Acceptable Use Policy](https://poolside.ai/legal/acceptable-use-policy). We advise against circumventing Laguna S 2.1 safety guardrails without implementing substantially equivalent mitigations appropriate for your use case.

Please report security vulnerabilities or safety concerns to [security@poolside.ai](mailto:security@poolside.ai).

- Downloads last month
- 3,056

##  Model tree for poolside/Laguna-S-2.1 

    ## Spaces using poolside/Laguna-S-2.1 4

[ poolside/Laguna-S-2.1   ](https://huggingface.co/spaces/poolside/Laguna-S-2.1)

![](https://cdn-avatars.huggingface.co/v1/production/uploads/699484cbe85a4b61cbc5ee0f/GpYWuz-CovEFgbPOW21dZ.png) 

 [🌖 akhaliq/Laguna-S-2.1  ](https://huggingface.co/spaces/akhaliq/Laguna-S-2.1)

[📈 DeepImagix/self-trained2  ](https://huggingface.co/spaces/DeepImagix/self-trained2)

[🤖 bep40/ml-intern  ](https://huggingface.co/spaces/bep40/ml-intern)

## Collection including poolside/Laguna-S-2.1

##  Evaluation results 

 - [datacurve/deep-swe](https://huggingface.co/datasets/datacurve/deep-swe)· Deep Swe- [View evaluation results](https://huggingface.co/poolside/Laguna-S-2.1/blob/main/.eval_results/deepswe.yaml)- [leaderboard](https://huggingface.co/datasets/datacurve/deep-swe?eval_result=poolside/Laguna-S-2.1&leaderboard_task_id=deep_swe)
- [ScaleAI/SWE-bench_Pro](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)· SWE Bench Pro- [View evaluation results](https://huggingface.co/poolside/Laguna-S-2.1/blob/main/.eval_results/swe-bench_pro.yaml)- [leaderboard](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro?eval_result=poolside/Laguna-S-2.1&leaderboard_task_id=SWE_Bench_Pro)
- [SWE-bench/SWE-bench_Multilingual](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multilingual)· Swe Bench Resolved- [View evaluation results](https://huggingface.co/poolside/Laguna-S-2.1/blob/main/.eval_results/swe-bench_multilingual.yaml)
