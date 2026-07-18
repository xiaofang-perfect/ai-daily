---
title: "NVIDIA Nemotron 3 Embed"
source: TLDR AI · 2026-07-17
url: https://huggingface.co/blog/nvidia/nemotron-3-embed-wins-rteb?utm_source=tldrai
date: 2026-07-18
published_at: 2026-07-17T12:00:00+00:00
tag: 工具开源
item_id: 833388bca16e7012
---
4B • Updated   •  982k  •  264  

#### mistralai/Ministral-3-3B-Instruct-2512

![](https://cdn-avatars.huggingface.co/v1/production/uploads/634c17653d11eaedd88b314d/9OgyfKstSZtbmsmuG8MbU.png) 

 Published
					July 16, 2026 

  Upvote 

 38

ybabakhin    

ronay-nv    

jiaruic    

viraman    

radekosmulski-nvidia    

jzakrzewski    

anmolg-nvidia    

oliverholworthy    

sahel-sh    

KhangPhamML    

hrong-nv    

steve-nvidia    

ssodha-nv    

ihulseman0220    

BoLiu    

Today, we are releasing [ NVIDIA Nemotron 3 Embed](https://huggingface.co/collections/nvidia/nemotron-3-embed), a collection of open and commercially available embedding models designed to improve retrieval quality while giving developers practical deployment options for production-scale RAG, agentic retrieval, code retrieval, and agent memory.

The collection includes three open models that achieve state-of-the-art retrieval across the accuracy-efficiency curve, led by an 8B model that tops the RTEB leaderboard and efficient 1B variants built for production-scale deployment:

| Model | Role | Best for | 
|---|---|---|
| [Nemotron-3-Embed-8B-BF16](https://huggingface.co/nvidia/Nemotron-3-Embed-8B-BF16) | Flagship Quality Anchor: The flagship embedding model, ranking #1 on RTEB. | Precision-critical retrieval and high-stakes enterprise RAG | 
| [Nemotron-3-Embed-1B-BF16](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16) | High-Efficiency Standard: A high-efficiency model for production retrieval where latency and cost matter. | Cost- and latency-sensitive production serving | 
| [Nemotron-3-Embed-1B-NVFP4](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-NVFP4) | Hardware-Accelerated Variant: A Blackwell-optimized variant for high-throughput retrieval with a smaller memory footprint. | Ultra-high-throughput and massive-scale infrastructure | 

*Table 1. Nemotron 3 Embed Model Usability and Deployment Matrix.*

![image5](https://cdn-uploads.huggingface.co/production/uploads/697fa5ae089a7f9330c5078f/I-QbjjUGW9tmE2mcDaW2f.png)


*Figure 1.  RTEB Multilingual Leaderboard screenshot (July 15, 2026) showing Nemotron-3-Embed-8B-BF16 ranked as #1.*

Beyond the RTEB result, Nemotron 3 Embed introduces a production-ready feature set for enterprise retrieval deployments:

- **Open Weights, Datasets, and Recipes:**Gives teams control to inspect, tune, fine-tune, and deploy retrieval models on their own infrastructure.
- **32k Context Window:**Supports retrieval over long documents, large code contexts, and multi-turn agent histories while reducing truncation.
- **Multilingual & Code Retrieval:**Supports retrieval across global enterprise data, technical documentation and multi-file code repositories.
- **NVIDIA NVFP4 Efficiency:**Provides a Blackwell-optimized 4-bit deployment path for high-throughput retrieval with a smaller memory footprint.
- **Fine-Tuning**- **and**- **Distillation**- **Recipes:**- [NVIDIA NeMo AutoModel](https://github.com/nvidia-nemo/automodel)recipes support domain adaptation and model compression for teams adapting retrieval models to their own data.
- **Day-0 Ecosystem Integration:**Available immediately on- [Hugging Face](https://huggingface.co/collections/nvidia/nemotron-3-embed), deployable as- [NVIDIA NIM](https://build.nvidia.com/nvidia/nemotron-3-embed-1b)microservice, supported by vLLM, and accessible through leading AI Cloud and inference partners.

We evaluate Nemotron 3 Embed across three dimensions: retrieval quality, downstream agentic efficiency, and deployment tradeoffs. The 8B model establishes the model collection’s quality ceiling, while the 1B BF16 and NVFP4 variants bring the same retrieval-focused design to lower-cost and higher-throughput deployment settings.

We first evaluated the models on [RTEB](https://huggingface.co/blog/rteb), where Nemotron-3-Embed-8B-BF16 ranks #1. We also tested these models across [ViDoRe V3](https://huggingface.co/blog/QuentinJG/introducing-vidore-v3) Text, and [MMTEB](https://arxiv.org/abs/2502.13595) Retrieval and [LongEmbed](https://github.com/dwzhu-pku/longembed) using average NDCG@10.

![retrieval_accuracy_vertical_longembed_with_gemma_no_gap_y0_y100_1dp](https://cdn-uploads.huggingface.co/production/uploads/697fa5ae089a7f9330c5078f/_4Rzuu2UMDD1DeHs-TOhP.png)


*Figure 2. Retrieval accuracy using average NDCG@10 across RTEB, ViDoRe V3 Text, MMTEB Retrieval and LongEmbed, comparing the Nemotron 3 Embed models with prior-generation Nemotron baselines.*

- **Nemotron-3-Embed-8B-BF16**ranks #1 on RTEB, scoring 78.5% on RTEB and 75.5% on MMTEB Retrieval.
- **Nemotron-3-Embed-1B-BF16**brings much of the 8B model’s retrieval quality into a smaller deployment footprint. It scores 72.4% on RTEB, reducing error rate by 27% over its 1B predecessor (llama-nemotron-embed-vl-1b-v2), and scores 71.0% on MMTEB Retrieval, reducing error rate by 28%.

To evaluate retrieval in an agentic setting, we use a [search agent](https://huggingface.co/blog/nvidia/nemo-retriever-agentic-retrieval) powered by [Nemotron 3 Ultra](https://github.com/NVIDIA-NeMo/Nemotron/tree/main/usage-cookbook/Nemotron-3-Ultra) and vary the embedding model used by the retrieval system. Better retrieval can return relevant evidence earlier, helping the agent avoid repeated searches, unnecessary reasoning turns, and extra context inspection. We compare average retrieval accuracy with estimated downstream agentic token cost per query across ViDoRe V3, [BRIGHT](https://brightbenchmark.github.io/), and [BrowseComp-Plus](https://huggingface.co/spaces/Tevatron/BrowseComp-Plus).

![image2](https://cdn-uploads.huggingface.co/production/uploads/697fa5ae089a7f9330c5078f/v45KGVKGsO_ZS8WW-KUgU.png)


*Figure 3. Average retrieval accuracy versus downstream agentic token cost per query across ViDoRe V3, BRIGHT, and BrowseComp-Plus.*

*Evaluation note: The search agent uses Nemotron 3 Ultra. Downstream token cost is estimated from Nemotron 3 Ultra input/output token counts using the GPT-5.5 pricing formula.*

Figure 3 shows that stronger retrieval reduces downstream agentic token cost. More accurate retrievers return relevant evidence earlier, which helps agents complete tasks with fewer repeated searches and fewer reasoning turns. In these evaluations, the Nemotron 3 Embed models improve the agentic retrieval frontier, with the 8B model delivering both the highest average retrieval accuracy and the lowest estimated downstream token cost across ViDoRe V3, BRIGHT, and BrowseComp-Plus.

For high-throughput deployments, teams often choose smaller embedding models to meet latency and cost targets. **Nemotron-3-Embed-1B-NVFP4** is designed to narrow the gap between serving efficiency and retrieval quality by using native NVFP4 acceleration on [NVIDIA Blackwell architectures](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/). The model quantizes the weights and activations of linear layers to NVFP4 for efficient inference, and uses Quantization-Aware Distillation (QAD) to help recover accuracy for long input sequences. 

![image3](https://cdn-uploads.huggingface.co/production/uploads/697fa5ae089a7f9330c5078f/R1QHlEFRytVBJcvt8lL9i.png)


*Figure 4. ViDoRe V3 retrieval accuracy versus serving efficiency, comparing Nemotron-3-Embed-1B-NVFP4 with selected smaller open embedding baselines, including Qwen3-Embedding-0.6B and EmbeddingGemma-300M.*

- **Serving Efficiency**: NVFP4 on Blackwell delivers up to 2x higher throughput than BF16 for high-throughput, low-latency retrieval serving.
- **Accuracy retention**: The NVFP4 variant retains 99%+ of BF16 retrieval accuracy while reducing memory footprint.

For production-scale retrieval systems, the serving stack also needs to preserve that efficiency under real request loads, across different input sequence lengths and hardware targets. To make Nemotron 3 Embed performant at enterprise scale today, we are also releasing an optimized NVIDIA NIM microservice for the 1B model. As shown in Figure 5, the Rust-based Nemotron 3 Embed NIM matches or outperforms the vLLM checkpoint on NVIDIA GB200 and RTX PRO 6000 GPUs across ISLs of 256 & 1024.

![image](https://cdn-uploads.huggingface.co/production/uploads/697fa5ae089a7f9330c5078f/ZFfiQHKsv2surfaCBUCkR.png)


*Figure 5.  Nemotron 3 Embed NIM serving performance compared with the vLLM checkpoint on NVIDIA GB200 and RTX PRO 6000 GPUs.*

**Nemotron-3-Embed-8B-BF16** adapts the [Ministral-3-8B-Instruct-2512](https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512) backbone by converting its causal decoder into a bidirectional encoder for full-sequence retrieval. The model is trained with contrastive pre-training on a blend of web-sourced and synthetic text pairs, then fine-tuned on curated multilingual retrieval datasets across domains such as legal, finance, medical, business, and education. This 8B model serves as the flagship embedding model, while earlier 8B teacher checkpoints from the same development line were used to distill the efficient 1B variants.

The 1B model is not a small retriever trained from scratch. We first applied the bidirectional adaptation recipe to the [Ministral-3-3B-Instruct-2512](https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512) backbone to establish a 3B retriever base, then compressed it through two-rounds of structured pruning and distillation.

First, the 3B parent model was compressed to a 2B intermediate footprint using [NVIDIA ModelOpt](https://github.com/NVIDIA/Model-Optimizer)’s mcore_minitron Neural Architecture Search engine. The NAS pipeline searched across hidden width, FFN size, attention heads, and depth under a strict parameter budget to identify an efficient architecture for retrieval workloads.

The resulting 2B intermediate model was then distilled from an 8B teacher checkpoint to recover ranking accuracy. We used a combined cosine distance loss and mean squared error loss on a multilingual, in-domain retrieval data blend to align the student’s embeddings with the teacher.

![image1](https://cdn-uploads.huggingface.co/production/uploads/697fa5ae089a7f9330c5078f/U6hbjPbLo70KwwtbAs2np.png)


*Figure 6. The pruning and distillation pipeline compresses the retriever from a 3B base to the final 1B production model.*

This same sequence, ModelOpt structured pruning followed by 8B teacher distillation, was repeated a second time to compress the 2B intermediate model down to the final 1.14B embedding model. Final training used a progressive two-stage context-scaling schedule:

- Stage 1: Focused on broad multilingual alignment at 1024-token context length to reconstruct the core retrieval behavior of the parent model.
- Stage 2: Expanded context length to 4096 tokens and added long-context synthetic and reasoning datasets, helping the 1B model retain discriminative recall across longer inputs.

The following table summarizes the core technical specifications and deployment targets for the Nemotron 3 Embed models:

| Model | Size | Emb Dim | Context Window | Pooling | Input Prefix | Target Hardware | 
|---|---|---|---|---|---|---|
| Nemotron-3-Embed-8B-BF16 | 8.0B | 4096 | 32k | Mean | query: / document: | General GPU Inference | 
| Nemotron-3-Embed-1B-BF16 | 1.14B | 2048 | 32k | Mean | query: / document: | Low-latency CPU/GPU | 
| Nemotron-3-Embed-1B-NVFP4 | 1.14B | 2048 | 32k | Mean | query: / document: | NVIDIA Blackwell/GB200 | 

*Table 2. Architectural specifications and core inference configurations for the Nemotron 3 Embed models.*

Enterprise ISVs, AI-native companies, and memory providers are already evaluating Nemotron 3 Embed across agentic retrieval, agent memory, code retrieval, and production inference workflows.

- *"Context is the key to agentic accuracy. Our Context Intelligence Graph uses embeddings and semantic similarity to deliver the most relevant enterprise context to agents like EnterpriseClaw, which we launched with NVIDIA in May. Early results from NVIDIA’s new Nemotron 3 Embed models are promising, particularly for question answering, where they show improvements over our current model. We’re excited about their potential to further improve the accuracy and reliability of our enterprise agents."*- Adi Kuruganti, Chief AI and Development Officer at Automation Anywhere
- *"Our initial evaluation of the NVIDIA Nemotron 3 Embed models shows strong retrieval performance for our agentic retrieval use cases. The availability of both 1B and 8B variants gives teams the flexibility to balance quality, latency, and deployment requirements across different environments. We're excited to continue evaluating the models and exploring how they can support high-performance retrieval for production AI applications."*- Mani Gill, Senior Vice President of Product Management at- [Boomi](https://boomi.com/blog/nvidia-nemotron-3-knowledge-hub)
- IBM has seen promising early results evaluating the new NVIDIA Nemotron Embed model in a proof-of-concept built on [watsonx.data](https://www.ibm.com/products/watsonx-data).
- *"We ran Nemotron-3-Embed-1B inside our own stack against various models and it came out on top. For instance, it scored 80.38% against Qwen-3-0.6B’s 78.71% on LongMemEval for Retrieval@10. The open weights and fine-tuning recipes are what interest us most, since they let us adapt the model to memory text and serve it ourselves."*- Rudraj Mehta, Product Manager at- [Mem0](https://mem0.ai/blog/how-mem0-uses-embeddings-and-why-we-are-evaluating-nvidia-nemotron-3-embed)
- Palantir is collaborating with NVIDIA to evaluate the deployment of Nemotron 3 Embed for end customers conducting edge retrieval workloads, building on the prior work making NVIDIA embedding models available in AIP's Model Catalog.
- ServiceNow is evaluating NVIDIA Nemotron Embed to retrieve through their documentation, with a continued interest in in-domain fine-tuning to improve their retrieval accuracy.
- [turbopuffer](http://turbopuffer.com/docs/embedding)is bringing Nemotron 3 Embed to its native embeddings service, enabling developers to use the models within its semantic search engine.
- *"Swapping in NVIDIA Nemotron 3 Embed model within our re-ranking stack delivered a significant leap in performance, letting us select query-relevant snippets from web pages with far greater accuracy than any model we'd used before."*- Rahul Mohan, Senior AI Engineer,- [You.com](http://you.com/home?utm_source=event-partner-nvidia&utm_medium=blog&utm_campaign=2026-07-homepage&utm_content=nemotron)
- [Zep](https://blog.getzep.com/evaluating-nemotron-3-embed-for-agent-memory)evaluated NVIDIA Nemotron 3 Embed 1B for agent memory and context retrieval. In early internal benchmarks against several models used by Zep, including some much larger than Nemotron 3 Embed 1B, the model ranked first across all memory retrieval tasks. Zep believes the availability of an FP4 checkpoint also makes the model very storage and latency competitive for their scale.
- Zoom is evaluating NVIDIA Nemotron 3 Embed for the retrieval layer behind the enterprise agentic search that powers Zoom's contextual layer, which helps agents retrieve relevant context across meetings and workplace knowledge sources, including docs, chat, tickets, and other internal systems.

NVIDIA Nemotron 3 Embed is released with open weights and open-source training recipes, giving organizations full control over how retrieval models are customized and deployed for production AI applications.

Developers can get started using the deployment option that best fits their workflow:

- **Hugging Face**
- **NVIDIA NIM**
- **AI Cloud and Inference Partners**- Deploy Nemotron 3 Embed through leading ecosystem partners -- [Baseten](http://baseten.co/blog/ai-retrieval-nvidia-nemotron-3-embed),- [Bitdeer AI](http://www.bitdeer.ai/en/blog/nvidia-nemotron-3-embed/),- [DeepInfra](http://deepinfra.com/blog/nvidia-nemotron-3-embed-release),- [Friendli AI](http://friendli.ai/blog/nvidia-nemotron-3-embed),- [OpenRouter.](https://openrouter.ai/nvidia/nemotron-3-embed-1b:free)

For workloads requiring domain adaptation or footprint reduction, we have also open-sourced  [NVIDIA NeMo AutoModel](https://github.com/nvidia-nemo/automodel) training recipes:

- **Fine-tuning recipe**
- **Distillation recipe**

For example, on the [NV Docs](https://huggingface.co/datasets/nvidia/Retrieval-Synthetic-NVDocs-v1) evaluation, fine-tuning Nemotron-3-Embed-1B-BF16 improved NDCG@10 from 56.7% to 63.3% (+11.6%) and Recall@5 from 56.1% to 62.8% (+11.9%).

Whether you are building enterprise search, production RAG, agent memory, code retrieval, or agentic AI systems, NVIDIA Nemotron 3 Embed provides flexible deployment options—from open-source models on Hugging Face to fully managed AI Cloud platforms and NVIDIA NIM microservices.

Explore the models, deploy them on your preferred platform, and let us know what you are building.

  4B • Updated   •  982k  •  264 

  9B • Updated   •  128k  •  186 

 Sentence Similarity •  1B • Updated   •  46.3k  •  60 

 Sentence Similarity •  0.8B • Updated   •  5.74k  •  44 

 Sentence Similarity •  8B • Updated   •  13k  •  47 

 Viewer • Updated  •  15.1k •  295  •  21 

🔍

 44

Fair and Disentangled Evaluation of Deep-Research Agents

More from this author

 17

 July 17, 2026  23

 July 8, 2026 Congratulations on the LMEB SOTA! 🎉

The results merged in [https://github.com/embeddings-benchmark/results/pull/617](https://github.com/embeddings-benchmark/results/pull/617) show outstanding LMEB performance:

Nemotron-3-Embed-8B-BF16: 64.4, a new overall SOTA.

Nemotron-3-Embed-1B-BF16: 61.5, a new SOTA at the ~1B scale.

The [LMEB leaderboard](https://mteb-leaderboard.hf.space/benchmark/LMEB) appears to be awaiting synchronization.

It's live now! Thank you for evaluating our models there!
