---
title: "Multi-Agent Kernel Optimization"
source: TLDR AI · 2026-04-15
url: https://cursor.com/blog/multi-agent-kernels?utm_source=tldrai
date: 2026-04-15
published_at: 2026-04-15T12:00:00+00:00
tag: 论文研究
item_id: 7b45d3cec5473c0a
---
# 多智能体系统将 GPU kernel 提速 38%

我们的多智能体系统仅用 3 周时间便自主优化了 235 个面向 NVIDIA Blackwell 200 GPU 的 CUDA kernel，较基线实现了 38% 的几何平均提速。

在过去几个月里，我们一直在开发一个能够自主构建、维护和部署复杂软件的多智能体系统。作为这项工作的一部分，我们已在多个领域对该系统进行了测试，包括让它[从零构建一个浏览器](https://cursor.com/blog/scaling-agents)，以及在 [First Proof 基准](https://x.com/mntruell/status/2028903020847841336?s=20)上解决研究级的数学问题。

最近，我们开始与 NVIDIA 合作，应对一项新的挑战：将多智能体框架用于优化 CUDA kernel。这类技术问题难度很高，而且有着重要的现实意义：CUDA kernel 是支撑 AI 模型在 NVIDIA GPU 上进行训练和推理的核心软件。kernel 越快，就意味着 GPU 利用率越高、能耗越低、延迟越低、每 token 成本越低——从而让服务提供商能够同时为更多用户提供更大、能力更强的模型。

我们的多智能体框架围绕 235 个问题自主运行了三周。系统从零开始构建并优化 Blackwell GPU kernel，一直深入到底层汇编级别，实现了 38% 的几何平均提速。

这种级别的性能提升，通常只有经验极其丰富的 kernel 工程师经过数月甚至数年的工作才能实现。而这个多智能体系统只用了几周就做到了，并解决了一长尾的 kernel 问题——这些问题用现有方法原本并不适合处理。

将 kernel 优化作为检验智能体系统能力的测试

评估长时间运行的多智能体系统，最佳方式之一就是给它们开放式的优化问题，在这类问题中，连我们自己也不知道正确答案。Kernel 优化问题正符合这一标准：它们有可量化的目标，系统可以围绕这些目标持续迭代优化，而不是只去逼近一个已知的简单 diff。

如今，工程师优化 kernel 时，通常会先把模型拆解成单独的数学运算，再分别对每一项进行调优。这样虽然让问题更易处理，但也会遗留一部分性能，因为这种零散的逐项优化会错过对整个系统同时优化所能带来的潜在收益。到目前为止，GPU 性能一直受限于我们无法跳出这些人工简化，去探索完整的解空间。

通过这项实验，我们想看看，多智能体系统能否跳出这些限制，在更广阔的解空间中探索，从而生成更快的 kernel。

用于问题生成和基准测试的 SOL-ExecBench

NVIDIA 使用 SOL-ExecBench，从 Deepseek、Qwen、Gemma、Kimi 和 Stable Diffusion 等 124 多个生产级开源模型中生成了 235 个优化问题。与合成数据或玩具 kernel 不同，每个问题都对应训练或推理工作负载中的真实约束，涵盖多种模型架构：LLM、diffusion、vision、audio、video 以及多模态混合架构。

![SOL-ExecBench 在 LLM、diffusion、vision、audio、video 和多模态架构中生成了 235 个优化问题](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2FNVIDIA%2520Multi-agent%2Fkernel-optimization-segmented-light.png&w=1920&q=70)

![SOL-ExecBench 在 LLM、diffusion、vision、audio、video 和多模态架构中生成了 235 个优化问题](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2FNVIDIA%2520Multi-agent%2Fkernel-optimization-segmented-dark.png&w=1920&q=70)

我们还使用 SOL-ExecBench，在 27 块 NVIDIA Blackwell 200 GPU 上对多智能体 kernel 方案进行了基准测试。SOL-ExecBench 是一种高效的评估工具，可将 kernel 性能与现有软件基线以及理论硬件性能上限进行比较。如果智能体采用缓存等作弊手段，表现出超出 B200 所能支持范围的性能，流程就会判定该结果无效。

我们如何开展这项实验

这个多智能体系统通过部署一个规划器智能体，根据性能指标在各个自主 worker 之间分配并重新平衡工作，在一次运行中就解决了所有 235 个 GPU kernel 优化问题。

整个协调协议都写在一个 Markdown 文件中，其中规定了输出格式、规则和测试。多智能体系统在运行过程中自主学会了调用基准测试流水线，从而形成一个循环，使系统在无需任何开发者干预的情况下持续测试、调试并优化 kernel。

![多智能体系统的自主调试、测试和优化循环](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2FNVIDIA%2520Multi-agent%2Fdebug-test-loop-light.png&w=1920&q=70)

![多智能体系统的自主调试、测试和优化循环](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2FNVIDIA%2520Multi-agent%2Fdebug-test-loop-dark.png&w=1920&q=70)

为了更准确地评估多智能体系统的功能，我们要求它在两次彼此独立的运行中，分别用两种语言写出解决方案；这两种语言位于 GPU 抽象层级的两端：

**带内联 PTX 的 CUDA C**，让智能体能够直接访问寄存器和 ISA 级指令，用于测试系统是否能在最底层进行硬件推理。**CuTe DSL**，提供可组合的高层抽象，但在公开训练数据中几乎不存在，用于测试系统是否能够仅凭提供的文档学习全新的 API。

提速 38%，其中 19% 的优化提速超过 2 倍

我们通过两种方式报告多智能体系统的性能：

**几何平均提速**：与作为基线、由单个智能体优化的 PyTorch 代码相比的几何平均提速。**SOL 分数**：表示某个解决方案在对数刻度下相对于理论硬件极限的表现。0.5 表示优化后的 PyTorch 基线，1.0 则表示性能极限。

![SOL 分数刻度：0.5 表示优化后的 PyTorch 基线，1.0 表示理论硬件极限](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2FNVIDIA%2520Multi-agent%2Fsol-score-light.png&w=1920&q=70)

![SOL 分数刻度：0.5 表示优化后的 PyTorch 基线，1.0 表示理论硬件极限](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2FNVIDIA%2520Multi-agent%2Fsol-score-dark.png&w=1920&q=70)

我们的多智能体系统在 235 个问题中，有 149 个的表现优于基线 (63%) ，几何平均比值为 1.38x (几何平均提速 38%) 。

![多智能体系统在 235 个 kernel 优化问题上实现了 1.38x 的几何平均提速](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2FNVIDIA%2520Multi-agent%2Fspeedup-chart-light.png%3Fv%3D2&w=1920&q=70)

![多智能体系统在 235 个 kernel 优化问题上实现了 1.38x 的几何平均提速](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2FNVIDIA%2520Multi-agent%2Fspeedup-chart-dark.png%3Fv%3D2&w=1920&q=70)

在 235 个问题中，有 45 个 (19%) 的优化结果相较于基线超过了 2x。您可以在这个[公开 repo](https://github.com/anysphere/kernel-optimization-results)中查看我们系统开发的最终解决方案。

![各问题提速分布，其中 19% 超过了 2x 的提升](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2FNVIDIA%2520Multi-agent%2Fproblem-level-speedup-chart-light.png&w=1920&q=70)

![各问题提速分布，其中 19% 超过了 2x 的提升](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2FNVIDIA%2520Multi-agent%2Fproblem-level-speedup-chart-dark.png&w=1920&q=70)

针对不同问题的优化策略各不相同

为了展示系统在不同类型问题上的适应性，我们重点介绍了三个案例，说明系统如何自然形成了各具特色的优化策略。

采用分页预填充的 BF16 分组查询注意力

采用分页预填充的分组查询注意力，是现代 LLM 推理栈中提示处理阶段的常见操作。优化良好的实现可以在相同的 GPU VRAM 下支持更长的上下文、更高的并发度以及更好的吞吐量。

该智能体使用 CUDA C++ 优化了一个从面向 Llama 3.1 8B 的 SGLang 推理流程中提取出来的注意力问题。在迭代这个 kernel 的过程中，智能体成功利用了特定的硬件指令来进行内存加载和数学计算，通过长期生效 kernel 改进了调度，并针对输入大小做了深度优化。

我们将多智能体系统的自定义 kernel 与 FlashInfer 库中人工优化的基线进行了比较。我们发现，该系统产出的方案已接近硬件极限，SOL 分数达到 0.9722，相比基线取得了 84% 的几何平均提速。

我们还替换了 SGLang 中现有的 kernel，并观察到在 Llama 3.1 8B 上首个 token 时间 (TTFT) 提速了 3%。考虑到这个注意力问题根据服务配置的不同会占预填充过程的 2–5%，我们认为这是一次不容忽视的端到端提速。

![BF16 分组查询注意力优化轨迹，SOL 分数达到 0.9722，几何平均提速达到 84%](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2FNVIDIA%2520Multi-agent%2Fevolution-trajectory-BF16-light.png&w=1920&q=70)

![BF16 分组查询注意力优化轨迹，SOL 分数达到 0.9722，几何平均提速达到 84%](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2FNVIDIA%2520Multi-agent%2Fevolution-trajectory-BF16-dark.png&w=1920&q=70)

带门控的 NVFP4 MoE 线性层

这个问题体现了 Qwen3 这类 Mixture-of-Experts 模型中一种常见的双 kernel 模式，不过这里的输入张量和中间乘法输出都被量化为 NVFP4 (4 位浮点) 。

智能体正确识别出量化部分是主要瓶颈，并据此将缩放计算与舍入操作融合在一起。它没有在量化过程中先缩放再舍入，而是使用预先计算好的阈值分桶，直接将 FP32 值映射为 FP4 编码；之所以可行，是因为 NVFP4 只有 16 个可能的取值。接着，它将这些优化应用到了更大规模的测试用例中。

智能体最终超越了优化后的 PyTorch 基线，实现了 39% 的几何平均提速，并获得 0.58 的 SOL 分数。

![NVFP4 MoE Linear 优化轨迹，实现 39% 的几何平均提速，并获得 0.58 的 SOL 分数](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2FNVIDIA%2520Multi-agent%2Fevolution-trajectory-nvfp4-light.png%3Fv%3D2&w=1920&q=70)

![NVFP4 MoE Linear 优化轨迹，实现 39% 的几何平均提速，并获得 0.58 的 SOL 分数](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2FNVIDIA%2520Multi-agent%2Fevolution-trajectory-nvfp4-dark.png%3Fv%3D2&w=1920&q=70)

BF16 矩阵乘法

矩阵乘法向来是最难优化的问题之一，因为它需要对各种硬件单元及其调度方式有非常深入的理解。要写出性能拉满的矩阵乘法 kernel (GEMM) ，通常需要用到内联 PTX (类似汇编语言) 、流水线，以及 kernel 内的暂存 (staging) 。因此，能够编写高性能 GEMM 的人，历来基本都局限于经验极其丰富的 kernel 专家。

Cursor 多智能体系统从零生成了一个专用的 CUDA C++ GEMM kernel，其性能惊人地逼近了 NVIDIA cuBLAS 库中经过人工精细调优的基线版本 (达到 86%) 。系统之所以能做到这一点，是因为它自主学会了使用 Blackwell 特有指令，针对硬件优化了内存读写，并进一步针对精确的矩阵形状做了深度优化。

而在 small-M 测试用例中——这类用例对 LLM 推理的 decode 阶段尤为重要——该多智能体系统生成的 kernel 性能最多比库实现高出 9%。这一结果表明，即便是在最棘手的 kernel 问题上，多智能体系统也有望很快超越领域专家。

![BF16 矩阵乘法结果：达到人工优化 cuBLAS 性能的 86%，并在 small-M 场景下最多超出 9%](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2FNVIDIA%2520Multi-agent%2Fhuman-optimized-kernel-percentage-light.png&w=1920&q=70)

![BF16 矩阵乘法结果：达到人工优化 cuBLAS 性能的 86%，并在 small-M 场景下最多超出 9%](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2FNVIDIA%2520Multi-agent%2Fhuman-optimized-kernel-percentage-dark.png&w=1920&q=70)

用于构建软件的多智能体系统

尽管多智能体框架 相比基线几何平均提速 38%，但 SOL 分数的中位数仍只有 0.56，说明仍有很大的优化空间。我们相信，只要有更多算力，多智能体方案还能得到大幅提升，因为当时我们需要在仅 27 块 GPU 上运行数百个问题和智能体。这限制了我们充分发挥多智能体系统潜力的能力。有了更多 GPU，系统就能探索更深入、更新颖的解法。

软件领域中最具挑战性的任务往往是开放式的，没有明确解法。单智能体系统在这类场景下往往难以胜任，因为模型最擅长的是边界清晰、范围较窄且在训练中已经见过的任务。我们认为，kernel 优化实验进一步印证了，多智能体架构将很快成为构建软件的默认方式，因为它们能够解决那些远远超出训练数据分布的新问题。

我们在这里研究的这些技术，很快就会为 Cursor 的核心产品提供参考。如果您有兴趣攻克多智能体协同中的难题，Cursor 团队非常期待您通过 [hiring@cursor.com](mailto:hiring@cursor.com) 与我们联系。
