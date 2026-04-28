---
title: "Ray Data LLM enables 2x throughput over vLLM's synchronous LLM engine at production-scale"
source: TLDR AI · 2026-03-25
url: https://www.anyscale.com/blog/ray-data-llm-2x-throughput-vs-vllm?utm_source=tldrai
date: 2026-03-25
published_at: 2026-03-25T12:00:00+00:00
tag: 工具开源
item_id: 5943c5cc127d98af
---
LLM are increasingly utilized in modern AI workflows such as synthetic data generation, data curation, and large-scale evaluation to produce diverse model outputs at scale, classify, filter, or enrich massive corpora, or measure model quality across extensive datasets.

In many of these workloads, unlike coding or interactive applications, these workloads prioritize throughput over per-request latency, which many LLM systems and deployments optimize for today. These workloads can be run in an offline batch fashion, and the systems designed to support these workloads must efficiently utilize hardware, minimize overhead, and reliably complete large jobs.

In this blog post, we’ll talk about [ Ray Data LLM](https://docs.ray.io/en/latest/data/working-with-llms.html), a library built for large-scale batch inference for LLMs, providing scalable execution, high throughput, and fault tolerance. We’ll highlight why Ray Data LLM provides a highly optimized architecture for running LLM batch inference from performance, scalability, and fault tolerance perspectives.

We finish by showing an example where by using Ray Data LLM, users can achieve 2x throughput over vLLM’s synchronous LLM engine while benefiting from production-scale resiliency.

Let’s walk through a naive batch inference approach to a production-scale pipeline, highlighting the limitations that emerge at each stage and how Ray Data LLM addresses them.

A naive approach to batch LLM inference is to load the entire dataset into CPU memory and run forward passes directly using [ vLLM’s LLM class](https://docs.vllm.ai/en/stable/serving/offline_inference/).

```
1from vllm import LLM
2llm = LLM(model="facebook/opt-125m")
3
4prompts = [
5 "What is machine learning?",
6 "Explain neural networks.",
7 "How does backpropagation work?",
8]
9
10sampling_params = SamplingParams(
11 temperature=0.7,
12 max_tokens=100,
13)
14
15outputs = llm.generate(prompts, sampling_params)
```


In practice, production datasets are often far too large for this approach to scale as large datasets can easily exceed available CPU memory which prohibits from processing datasets larger than available CPU RAM.

With this naive approach, we are missing streaming execution capability to process large datasets and fault tolerance.

A natural alternative method is to use a distributed execution engine like Ray Data with vLLM to scale out the data processing.

With its streaming execution model, Ray Data enables processing datasets that exceed available CPU memory. This approach creates synchronous LLM engines and leverages Ray Data’s map_batches API to process the dataset on distributed actors with synchronous LLM engines. More importantly, Ray Data built-in fault tolerance automatically replaces actors with crashed engines and retries failed batches, offering resiliency for production workloads.

```
1class vLLMCallable:
2 def __init__(self, *args, **kwargs):
3 self.llm = LLM(*args, **kwargs)
4
5 def __call__(self, batch: pd.DataFrame) -> dict:
6 prompts = batch['prompt'].tolist()
7 sampling_params = SamplingParams(temperature=0.7, max_tokens=100)
8
9 outputs = self.llm.generate(prompts, sampling_params)
10 generated_texts = [out.outputs[0].text for out in outputs]
11 return {"generated_text": generated_texts}
12
13ray.init()
14ds = ray.data.from_items([
15 {"prompt": "What is machine learning?"},
16 {"prompt": "Explain neural networks."},
17 {"prompt": "How does backpropagation work?"},
18])
19
20ds = ds.map_batches(
21 vLLMCallable,
22 batch_size=32,
23 num_gpus=1,
24 fn_constructor_kwargs={
25 "model": "facebook/opt-125m",
26 "max_model_len": 512,
27 },
28)
```


Despite the benefits from Ray Data, there are still limitations with this approach. LLMs present non-determinism in the decode process, resulting in variable decode sequence lengths and, consequently, requests with different execution times. When using a synchronous engine together with synchronous map_batches invocation, requests with shorter decode sequences must wait for those with longer ones to complete, creating pipeline bubbles and leading to inefficient resource utilization. Furthermore, this approach only batches prompts at the request level. The synchronous LLM class does not support [ continuous batching](https://www.anyscale.com/blog/continuous-batching-llm-inference) where prompts are batched at the token level rather than the request level, which further exacerbates pipeline inefficiencies.

With this approach, we are still missing some key features to achieve production-scale resiliency and performance, namely overlapping requests and batches and graceful failover.

Ray Data LLM addresses all of the challenges above. Under the hood, Ray Data LLM leverages vLLM’s asynchronous LLM engine, enabling continuous batching to maximize resource utilization, and invokes **map_batches()** asynchronously to concurrently process requests with varying output decode lengths. Moreover, Ray Data LLM disaggregates tokenization and detokenization from the vLLM engine, providing fine-grained control over the resources (CPU, GPU, and memory) for different stages (tokenization, engine, detokenization) in the pipeline.

In production scenarios where fault tolerance and observability are critical, Ray Data LLM provides strong support for both. In particular, when a single row fails due to a request level error from the engine (e.g. prompt too long, etc.), the overall data pipeline continues running, and the error is recorded in the resulting dataset rather than causing the job to crash. It also exposes row-level observability, including per-request latency, making it easier to debug slow or problematic requests.

```
1import ray
2from ray.data.llm import vLLMEngineProcessorConfig, build_processor
3
4ray.init()
5
6ds = ray.data.from_items([
7 {"prompt": "What is machine learning?"},
8 {"prompt": "Explain neural networks."},
9 {"prompt": "How does backpropagation work?"},
10])
11
12config = vLLMEngineProcessorConfig(
13 model_source="facebook/opt-125m",
14 concurrency=16,
15 batch_size=32,
16 engine_kwargs={
17 "max_model_len": 512,
18 },
19 tokenize_stage=True,
20 detokenize_stage=True,
21)
22
23processor = build_processor(
24 config,
25 preprocess=lambda row: {
26 "messages": [{"role": "user", "content": row["prompt"]}],
27 "sampling_params": {
28 "temperature": 0.7,
29 "max_tokens": 100,
30 },
31 },
32 postprocess=lambda row: {
33 "prompt": row["prompt"],
34 "response": row["generated_text"],
35 },
36)
37
38ds = processor(ds)
39result = ds.take_all()
```


Moreover, Ray Data LLM is designed to be modular, making it easy to integrate with existing data processing pipelines built on Ray Data. For example, users can chain multiple stages with different prompts and LLMs to perform more complex, large-scale data processing workflows using LLMs.

Asynchronous execution is the primary driver of Ray Data LLM’s performance advantages. It operates at two complementary layers: the batch level within Ray Data and the engine level within vLLM.

At the **batch level**, Ray Data executes batches asynchronously, allowing multiple batches to be processed concurrently. This prevents long-running batches from blocking subsequent ones and ensures that the vLLM engine actors remain continuously saturated with tasks.

At the **engine level**, vLLM performs asynchronous execution by dynamically batching requests at the token level. Under this mechanism, requests with longer decode sequences do not stall shorter ones, enabling efficient interleaving of generation across requests.

Together, **these two layers of asynchronous execution** eliminate blocking at both the batch and token levels, leading to significantly higher throughput compared to synchronous execution.

To better understand the trade-offs between synchronous and asynchronous execution, we conducted an ablation study using Ray Data with Qwen-4B across a range of decode patterns. We focus on mixed workloads that combine reasoning and non-reasoning traces, modeled using a bimodal decode-length distribution. The first mode is a normal distribution with a mean of 50 tokens and a standard deviation of 10, representing typical non-reasoning generation. The second mode varies from 100 to 2,000 tokens with increasing standard deviation to represent reasoning traces. To precisely control decode lengths, ignore_eos is enabled in the vLLM engine.

The results show that as reasoning traces become longer and more variable, asynchronous execution increasingly outperforms synchronous execution, with the relative improvement growing on a logarithmic scale. This trend suggests that the performance gains from asynchronous execution are not intrinsically bounded: as reasoning traces become arbitrarily long, asynchronous execution continues to overlap long-running requests, while synchronous execution is increasingly constrained by synchronization barriers at the batch and request level.

Ray Data LLM scales batch inference by streaming large datasets, leveraging continuous batching, and offering fault tolerance. Beyond the features covered in this post, Ray Data LLM also supports batch inference for vision-language models with multimodal inputs. Stay tuned for a follow-up post that explores these advanced capabilities in more detail!

Join the Ray Slack #llm channel:

[https://www.ray.io/join-slack](https://www.ray.io/join-slack)Ray LLM office hours; sign up here for the Calendar invite:

__https://forms.gle/QsjHNGvEhhpRcW3r5__Ray LLM office hours past recordings:

__https://youtube.com/playlist?list=PLzTswPQNepXl2IYF8DcV35FdCoVbeL4_6&si=huzJ7Oqn-LD4DgFL__
