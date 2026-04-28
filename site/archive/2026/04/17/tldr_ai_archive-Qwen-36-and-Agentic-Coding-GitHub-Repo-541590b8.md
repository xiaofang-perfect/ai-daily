---
title: "Qwen 3.6 and Agentic Coding (GitHub Repo)"
source: TLDR AI · 2026-04-17
url: https://github.com/QwenLM/Qwen3.6?utm_source=tldrai
date: 2026-04-17
published_at: 2026-04-17T12:00:00+00:00
tag: 工具开源
item_id: 541590b8b648652f
---
![](https://camo.githubusercontent.com/62c3afa85f0ae23aabf23f58e5311f7232e7a792f71e7ab53014c216cc2284cf/68747470733a2f2f7169616e77656e2d7265732e6f73732d616363656c65726174652e616c6979756e63732e636f6d2f5177656e332e362f6c6f676f2e706e67)


[💜 Qwen Studio](https://chat.qwen.ai/) |

[🤗 Hugging Face](https://huggingface.co/Qwen)|

[🤖 ModelScope](https://modelscope.cn/organization/qwen)| 📑 Paper | 📖 Documentation |

[💬 WeChat (微信)](https://github.com/QwenLM/Qwen/blob/main/assets/wechat.png)|

[ Discord](https://discord.gg/CV4E9rpNSD)

Welcome to the GitHub repository of Qwen3.6 (& Qwen3.5). Here, you can find official information about Qwen3.6 (User Guide, coming soon), post your questions ([Issues](https://github.com/QwenLM/Qwen3.6/issues)), and share your ideas with the community ([Discussions](https://github.com/QwenLM/Qwen3.6/discussions)).

Qwen3.6 is the latest addition to the Qwen model family. Building upon the fundamental breakthroughs of Qwen3.5, this release prioritizes stability and real-world utility. It offers developers a more intuitive, responsive, and genuinely productive coding experience, shaped by direct community feedback. This update delivers substantial upgrades, particularly in:

**Agentic Coding:**The model now handles front-end workflows and repository-level reasoning with greater fluency and precision.**Thinking Preservation:**A new feature retains thinking context across conversation history, streamlining iterative development and reducing overhead.

Over recent months, we have intensified our focus on developing foundation models that deliver exceptional utility and performance. Qwen3.5 represents a significant leap forward, integrating breakthroughs in multimodal learning, architectural efficiency, reinforcement learning scale, and global accessibility to empower developers and enterprises with unprecedented capability and efficiency.

Qwen3.5 features the following enhancement:

-
**Unified Vision-Language Foundation**: Early fusion training on trillions of multimodal tokens achieves cross-generational parity with Qwen3 and outperforms Qwen3-VL models across reasoning, coding, agents, and visual understanding benchmarks. -
**Efficient Hybrid Architecture**: Gated Delta Networks combined with sparse Mixture-of-Experts deliver high-throughput inference with minimal latency and cost overhead. -
**Scalable RL Generalization**: Reinforcement learning scaled across million-agent environments with progressively complex task distributions for robust real-world adaptability. -
**Global Linguistic Coverage**: Expanded support to 201 languages and dialects, enabling inclusive, worldwide deployment with nuanced cultural and regional understanding. -
**Next-Generation Training Infrastructure**: Near-100% multimodal training efficiency compared to text-only training and asynchronous RL frameworks supporting massive-scale agent scaffolds and environment orchestration.

- 2026-04-22: Qwen3.6-27B is now availabe on
[Hugging Face Hub](https://huggingface.co/collections/Qwen/qwen36)and[ModelScope](https://modelscope.cn/collections/Qwen/Qwen36). Read more on our[release blog](https://qwen.ai/blog?id=qwen3.6-27b)! - 2026-04-16: Qwen3.6-35B-A3B is now availabe on
[Hugging Face Hub](https://huggingface.co/collections/Qwen/qwen36)and[ModelScope](https://modelscope.cn/collections/Qwen/Qwen36). Read more on our[release blog](https://qwen.ai/blog?id=qwen3.6-35b-a3b)! - 2026-03-02: Qwen3.5-9B, Qwen3.5-4B, Qwen3.5-2B, and Qwen3.5-0.8B are now available on
[Hugging Face Hub](https://huggingface.co/collections/Qwen/qwen35)and[ModelScope](https://modelscope.cn/collections/Qwen/Qwen35)! - 2026-02-24: Qwen3.5-122B-A10B, Qwen3.5-35B-A3B, and Qwen3.5-27B are released. Check out the model cards on
[Hugging Face Hub](https://huggingface.co/collections/Qwen/qwen35)or[ModelScope](https://modelscope.cn/collections/Qwen/Qwen35)for more information! - 2026-02-16: We release Qwen3.5. The first release includes a 397B-A17B MoE model. Read more on our
[release blog](https://qwen.ai/blog?id=qwen3.5). More sizes are coming & Happy Chinese New Year! - 2025-09-11: We release Qwen3-Next-80B-A3B, an ultra-sparse mixture-of-experts model with hybrid attention architecture, designed for extreme efficiency. Read more on our
[blog](https://qwen.ai/blog?id=qwen3-next).

The official model weights are released on:

[🤗Hugging Face Hub](https://huggingface.co/Qwen): Most LLM frameworks and applications support downloading model files from Hugging Face Hub automatically by specifying the model ID, e.g.,`Qwen/Qwen3.6-35B-A3B`

and`Qwen/Qwen3.5-397B-A17B`

. You can also download model files manually using`huggingface download`

or`git clone`

. Please follow the instructions on the model page.[🤖ModelScope](https://www.modelscope.cn/organization/Qwen): For users unable to access Hugging Face Hub, we strongly recommend using ModelScope. For supported frameworks, you can download from ModelScope by setting environment variables, such as`SGLANG_USE_MODELSCOPE=true`

or`VLLM_USE_MODELSCOPE=true`

. You can also download model files manually using`modelscope download`

or`git clone`

. Please follow the instructions on the model page.

**Qwen3.6 Open Models**

For detailed results, please check out the [Qwen3.6-35B-A3B blog](https://qwen.ai/blog?id=qwen3.6-35b-a3b) and the [Qwen3.6-27B blog](https://qwen.ai/blog?id=qwen3.6-27b).

**Qwen3.5 Open Models**

For detailed results, please check out the [Qwen3.5 blog](https://qwen.ai/blog?id=qwen3.5).

To learn more about Qwen3.6, feel free to read our documentation (coming soon).

You can try Qwen3.6 on our official sites and enjoy the native experience with extra features, such as deep research, web dev, and adaptive tool use.

For users who simply would like to try Qwen3.6, [Qwen Studio](https://chat.qwen.ai) (formerly known as Qwen Chat) is just a touch away.
Qwen Studio provides Web UI and desktop and mobile applications, with a familiar, easy-to-use user interface.
Qwen Studio is also a playground for our ideas, showcasing how Qwen3.6 can be integrated into your workflow and applications.

The official Qwen API is provided by [Alibaba Cloud Model Studio](https://modelstudio.alibabacloud.com/).

Alibaba Cloud Model Studio provides first-class support for Qwen3.6, which is compatible with various API specifications, including OpenAI and Anthropic, making it simple for you to try Qwen3.6 in your own applications.

[Qwen Code](https://github.com/QwenLM/qwen-code) is an open-source AI agent for the terminal, optimized for Qwen models. It helps you understand large codebases, automate tedious work, and ship faster.

For more information, please refer to [Qwen Code](https://qwenlm.github.io/qwen-code-docs/).

For agent development, take a look at [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent). Qwen Agent is an open-source AI agent framework that helps you build powerful LLM applications based on the instruction following, tool usage, planning, and memory capabilities of Qwen.

Check out [Qwen Agent](https://qwenlm.github.io/Qwen-Agent/en/) to find out more!

[ transformers](https://huggingface.co/transformers) acts as the model-definition framework in the current open-weight LLM landscape.
It also includes functionalities for LLM inference and training. The addition of serving capabilities in

`transformers`

makes it much easier to integrate new models in your development.To launch a server, simply use the `transformers serve`

command:

`transformers serve --port 8000 --continuous-batching`

OpenAI-compatible APIs can be accessed at `http://localhost:8000/v1`

and the server downloads models from Hugging Face Hub automatically.

With the server running, you can also interact with Qwen3.6 directly from the command line:

`transformers chat Qwen/Qwen3.6-35B-A3B`

[ llama.cpp](https://github.com/ggml-org/llama.cpp) enables LLM inference with minimal setup and state-of-the-art performance on a wide range of hardware.
llama.cpp supports Qwen3.6 (text & vision).
Look for models ending with GGUF on Hugging Face Hub.

If you are running on Apple Silicon, both [ mlx-lm](https://github.com/ml-explore/mlx-lm) (text-only) and

[(vision + text) support Qwen3.6. Look for models ending with](https://github.com/Blaizzy/mlx-vlm)

`mlx-vlm`

**MLX**on the Hugging Face Hub.

Qwen3.6 is supported by multiple inference frameworks.
Here we demonstrate the usage of `SGLang`

and `vLLM`


[SGLang](https://github.com/sgl-project/sglang) is a fast serving framework for large language models and vision language models.
SGLang could be used to launch a server with OpenAI-compatible API service.

`python -m sglang.launch_server --model-path Qwen/Qwen3.6-35B-A3B --port 8000 --tp-size 4 --context-length 262144 --reasoning-parser qwen3`

An OpenAI-compatible API will be available at `http://localhost:30000/v1`

.

[vLLM](https://github.com/vllm-project/vllm) is a high-throughput and memory-efficient inference and serving engine for LLMs.
vLLM could be used to launch a server with OpenAI-compatible API service.

`vllm serve Qwen/Qwen3.6-35B-A3B --port 8000 --tensor-parallel-size 4 --max-model-len 262144 --reasoning-parser qwen3`

An OpenAI-compatible API will be available at `http://localhost:8000/v1`

.

We advise you to use training frameworks, including [UnSloth](https://github.com/unslothai/unsloth), [Swift](https://github.com/modelscope/swift), [Llama-Factory](https://github.com/hiyouga/LLaMA-Factory), etc., to finetune your models with SFT, DPO, GRPO, etc.

All our open-weight models are licensed under Apache 2.0. You can find the license files in the respective Hugging Face repositories.

If you find our work helpful, feel free to give us a cite.

```
@misc{qwen3.6-27b,
title = {{Qwen3.6-27B}: Flagship-Level Coding in a {27B} Dense Model},
author = {{Qwen Team}},
year = {2026},
month = {April},
url = {https://qwen.ai/blog?id=qwen3.6-27b}
}
@misc{qwen3.6-35b-a3b,
title = {{Qwen3.6-35B-A3B}: Agentic Coding Power, Now Open to All},
author = {{Qwen Team}},
year = {2026},
month = {April},
url = {https://qwen.ai/blog?id=qwen3.6-35b-a3b}
}
@misc{qwen3.5,
title = {{Qwen3.5}: Towards Native Multimodal Agents},
author = {{Qwen Team}},
year = {2026},
month = {February},
url = {https://qwen.ai/blog?id=qwen3.5}
}
```

If you are interested to leave a message to either our research team or product team, join our [Discord](https://discord.gg/z3GAxXZ9Ce) or [WeChat groups](https://github.com/QwenLM/Qwen3/blob/main/assets/wechat.png)!
