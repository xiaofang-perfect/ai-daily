---
title: "Quantization-Aware Healing: a compressed, 4-bit model that outperforms its full-precision original"
source: HuggingFace Blog
url: https://huggingface.co/blog/MultiverseComputingCAI/quantization-aware-healing
date: 2026-08-26
published_at: 2026-08-25T11:39:24+00:00
tag: 论文研究
item_id: c0b517cd6f190aa5
---
[Text Generation •  59B • Updated   •  3.94k  •  16](https://huggingface.co/MultiverseComputingCAI/Hypernova-60B-2605)  

#### MultiverseComputingCAI/Hypernova-60B-2605

![](https://cdn-avatars.huggingface.co/v1/production/uploads/6835694d56d5a69517655698/C3QUBARPGF4kbzJzZaT29.png) 

Published
					August 25, 2026 

  Upvote 

 14

AntonioTN    

Iker    

ali-hashemi    

bryskulov-mc    

Making a large language model smaller almost always comes with a cost. The now-standard recipe for efficient deployment is to compress the architecture first, cutting the parameter count by removing layers, heads, or neurons, and then quantize the remaining weights down to 4 bits to shrink memory and compute further. Both steps save a lot, but together they systematically degrade the capabilities people actually care about: reasoning, mathematical problem-solving, and code generation. Because of this, serious deployment pipelines add a recovery step, usually called healing, before the model goes into production. Recent open-weight releases such as [gpt-oss](https://huggingface.co/openai/gpt-oss-120b), NVIDIA's [Nemotron](https://huggingface.co/nvidia) family, and our own [Hypernova 60B](https://huggingface.co/MultiverseComputingCAI/Hypernova-60B-2605) all rely on some version of this compress-then-heal approach.
## 
	
		
	
	
		Why the usual healing methods fall short here
	

Most efficiency pipelines follow the same three steps: compress the architecture, quantize the compressed weights, then heal the damage. The difference between methods is entirely in that last step.

The dominant healing recipe is quantization-aware training (QAT). It inserts fake-quantization operators into the forward pass and keeps fine-tuning the model on a task loss, so the weights learn to tolerate the low-precision representation. In practice this means re-running an already expensive multi-stage post-training process, supervised fine-tuning, RLHF, agentic tuning, through a noisier, lower-precision forward pass. It is costly, and as our results show, it can also become unstable if training continues too long past its best point.

So the question of how to heal a model that has been both structurally compressed and quantized was, until now, genuinely open.

## 
	
		
	
	
		Our approach
	

QAH removes that ceiling with one change: it distills directly from the original, pre-compression model rather than from the recovered one. Teacher and student do not even share an architecture. The teacher is full-size and full-precision, the student is half the size and running in MXFP4. Because a teacher's output distribution is architecture-agnostic, nothing about the size or shape mismatch prevents the transfer. The student never sees hard labels, only the teacher's output distribution, matched through KL divergence on the logits.

This reframes what the quantization stage is doing. Under QAH it is no longer a lossy postprocessing step applied after healing is finished. It is a second, full pass of distillation against the original teacher, supervision that the bfloat16 checkpoint never received. The 4-bit student is not compensating for information lost to quantization; it is picking up information the earlier recovery stage did not have the time or data to transfer.

There is also a stability benefit that falls out of the loss itself. Because KL distillation ties the student to a fixed teacher distribution, once the student catches up there is no further pressure for it to drift. A cross-entropy task loss, by contrast, keeps pushing the student toward hard labels indefinitely. That difference turns out to matter for both accuracy and training stability, as the comparison below shows.

## 
	
		
	
	
		Results
	

We applied QAH to a GPT-OSS 120B model, compressed to 60B parameters and recovered in bfloat16, then re-quantized to MXFP4 under QAH. The natural comparison is against that same 60B model's bfloat16 checkpoint, the best full-precision version of this architecture that exists. The QAH model wins on 7 of the 9 benchmarks.

	

The two benchmarks where QAH trails, MMLU-Pro and SciCode, lose by less than a point and a half. Everywhere else the 4-bit model is ahead of its own 16-bit source, and the largest gains land on exactly the capabilities compression usually damages most: long-context reasoning (+7.4 on AA-LCR) and math (+5.6 on AIME 2025).

The comparison against the original 120B teacher is just as telling. Despite running at half the teacher's parameter count and roughly a quarter of its weight memory, the QAH model surpasses the full-size teacher on LiveCodeBench (66.5 vs. 66.0) and comes within 1.6 points on GPQA Diamond (67.4 vs. 69.0). The largest remaining gap against the teacher is on AA-LCR, an extreme long-context benchmark where the capacity lost to compression is intrinsically the hardest to recover.

### 
	
		
	
	
		QAH against QAT, head to head
	

To isolate the effect of the loss function from everything else, we also compared QAH directly against QAT under matched conditions, quantizing a GPT-OSS 9B model to MXFP4 and tracking average performance across MMLU-Pro, LiveCodeBench, and GPQA Diamond as training progresses.

Both methods reach a similar peak, 54.9 for QAH against 54.6 for QAT, so on best-case accuracy they are effectively tied. The difference is in how they get there and what happens afterwards. QAH reaches its peak in about 100 steps, roughly 7 times faster than QAT's 700, and then stays within about two points of that peak for the rest of training. QAT collapses sharply once past its peak, shedding nearly 19 points by step 1,200.

The practical consequence is a real deployment risk difference. A QAT checkpoint needs careful early stopping against a held-out signal to avoid shipping a model that has already started to degrade, whereas a sufficiently trained QAH checkpoint can be served safely because it simply does not drift. This is consistent with the mechanism: KL distillation against a frozen teacher gives the student no incentive to move once it matches the teacher, while a cross-entropy objective keeps pushing on hard labels and eventually erodes capabilities the model inherited from the original.

## 
	
		
	
	
		What this changes in practice
	

The accuracy story comes paired with the efficiency story that motivated compression in the first place. At 4-bit precision the QAH model uses roughly 4 times less weight memory than the bfloat16 student, and at half the parameter count of the 120B teacher it roughly halves compute per token, which is what lets it run on substantially smaller hardware. For model families that ship in bfloat16 rather than 4-bit, the combined parameter and precision reduction would be closer to 8 times less compute per token.

The takeaway is that a compressed, 4-bit model does not have to be a lower-accuracy version of its full-precision counterpart. With this healing recipe it can be smaller, cheaper to serve, and more accurate at the same time, and it reaches that point in a fraction of the training a QAT recipe would need. Quantization stops being a tax you pay for efficiency and becomes an extra opportunity to teach the model.

This work is part of Multiverse Computing's ongoing research into making large models smaller and cheaper to run without giving up the capabilities that make them useful. It sits alongside our companion work on efficient distillation, which supplies the long-context training machinery QAH depends on.


![QAH overview: after structural compression and quantization, capabilities drop sharply. QAH distills from the original pre-compression model as a frozen teacher, restoring performance without retracing the multi-stage post-training.](https://cdn-uploads.huggingface.co/production/uploads/668e37fd9c9aa124a3c867e8/_oc2ExO8yVJ9xIyRsHzGy.png)


| Benchmark | 120B teacher (MXFP4) | 60B BF16 (recovered) | 60B MXFP4 (QAH) | QAH vs BF16 | 
|---|---|---|---|---|
| AA-LCR (long-context reasoning) | 50.0 | 35.3 | 42.7 | +7.4 | 
| AIME 2025 (math) | 80.0 | 70.7 | 76.3 | +5.6 | 
| Aider (agentic coding) | 45.3 | 38.2 | 40.9 | +2.7 | 
| τ²-bench (tool use) | 68.4 | 59.4 | 61.7 | +2.3 | 
| GPQA Diamond (science) | 69.0 | 65.7 | 67.4 | +1.7 | 
| IFBench (instruction following) | 63.3 | 58.4 | 59.9 | +1.5 | 
| LiveCodeBench (coding) | 66.0 | 65.5 | 66.5 | +1.0 | 
| MMLU-Pro (knowledge) | 78.0 | 74.0 | 73.8 | −0.2 | 
| SciCode (science coding) | 37.5 | 35.6 | 34.2 | −1.4 | 

![Benchmark performance of the three checkpoints: the original GPT-OSS-120B teacher (MXFP4), the compressed and recovered 60B model in bfloat16, and the same 60B model re-quantized to MXFP4 with QAH, across nine benchmarks.](https://cdn-uploads.huggingface.co/production/uploads/668e37fd9c9aa124a3c867e8/fDOD3YXBoRPXFo2xDaiC0.png)


![Average performance of QAH and QAT as training progresses, quantizing GPT-OSS 9B to MXFP4. QAH peaks early and stays stable through 1,200 steps; QAT reaches a comparable peak much later, then collapses.](https://cdn-uploads.huggingface.co/production/uploads/668e37fd9c9aa124a3c867e8/r-bfWuDWpn0KnQ0Kqosai.png)


 Text Generation •  117B • Updated   •  5.12M  •  5.13k 

 Paper • 2608.20953 • Published  •  9 

More from this author

 38

 August 10, 2026 
Making a large language model smaller almost always comes with a cost. The now-standard recipe for efficient deployment is to compress the architecture first, cutting the parameter count by removing layers, heads, or neurons, and then quantize the remaining weights down to 4 bits to shrink memory and compute further. Both steps save a lot, but together they systematically degrade the capabilities people actually care about: reasoning, mathematical problem-solving, and code generation. Because of this, serious deployment pipelines add a recovery step, usually called healing, before the model goes into production. Recent open-weight releases such as [rbtv77](https://www.rbtv77plus.app/) gpt-oss, NVIDIA's Nemotron family, and our own Hypernova 60B all rely on some version of this compress-then-heal approach.


This is a really fascinating take on model compression 🤯🔥. The idea that a 4-bit model can actually outperform the full-precision version turns the usual assumption about quantization completely upside down.... Instead of simply accepting the accuracy loss that comes with compression, QAH seems to show how targeted recovery can bring back—and even improve—important capabilities like reasoning, math, and coding. 🧠⚡

What really caught my attention is the result with the compressed GPT-OSS 120B → 60B model.... Getting a smaller MXFP4 model to beat its own bfloat16 checkpoint on 7 of 9 benchmarks is pretty impressive. 📊🚀 It makes the whole compress-then-heal pipeline feel much more practical for real-world deployment, especially when memory usage and inference costs matter.

I also like the broader implication here.... Quantization doesn't necessarily have to mean sacrificing model quality if the recovery process is designed with the quantized model in mind. 💡🔧 A smaller model that costs less to operate while still delivering stronger benchmark performance could be a huge advantage for teams trying to deploy capable LLMs efficiently.

Definitely an interesting direction for efficient AI deployment.... Turning a heavily compressed 4-bit model into something that can outperform its larger full-precision counterpart is the kind of result that makes you rethink what "compression" actually means. 👏🔥 Really curious to see how far Quantization-Aware Healing can go across other architectures and workloads.... 🚀🧠
