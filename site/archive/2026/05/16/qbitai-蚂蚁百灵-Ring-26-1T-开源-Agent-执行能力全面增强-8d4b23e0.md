---
title: "蚂蚁百灵 Ring-2.6-1T 开源 Agent 执行能力全面增强"
source: 量子位
url: https://www.qbitai.com/2026/05/417961.html
date: 2026-05-16
published_at: 2026-05-15T07:14:36+00:00
tag: 工具开源
item_id: 8d4b23e0878ba44e
---
# 蚂蚁百灵 Ring-2.6-1T 开源 Agent 执行能力全面增强

AIME 26 得分 95.83

5 月 15 日，蚂蚁百灵宣布其旗舰级思考模型 Ring-2.6-1T 正式开源，权重文件同步上线 Hugging Face、ModelScope 平台。此前，该模型上线 OpenRouter，并开放限时免费 API 体验。

![](https://i.qbitai.com/wp-content/uploads/2026/05/5f9d56ec18d9c25a8bff8333e285b215.jpg)


Ring-2.6-1T 的核心设计逻辑是“按需思考”，模型引入了可调节的 Reasoning Effort 机制，支持 high 与 xhigh 两种推理强度，开发者可以根据任务特性动态分配推理资源。其中，high 模式面向高频 Agent 工作流获得更高效率，适合多轮对话、工具协作与任务拆解；xhigh 模式则面向数学竞赛、科研分析等高难任务，释放能力上限。有开发者表示，这是“工程实用性”的进步。

根据权威评测，Ring-2.6-1T 的两档模式各有所长。high 模式下，PinchBench 得分 87.60，高于 GPT-5.4 xHigh和Gemini-3.1-Pro high，Tau2-Bench Telecom 达到 95.32，Agent 场景执行能力显著。xhigh 模式下，AIME 26 得分 95.83，接近多家头部模型水平；GPQA Diamond 达到 88.27，体现出稳健的科学知识理解与复杂推理能力。

在训练层面，Ring-2.6-1T 采用异步（Async）强化学习训练架构，将策略采样与参数更新解耦为独立流水线，解决了传统同步训练中 GPU 资源等待、训练吞吐不足的问题，并支持更长周期的持续训练。在此基础上，百灵将此前在 Ring-1T 中验证过的“棒冰算法”引入异步 RL 训练，解决训练不稳定问题。百灵表示，相关技术细节将在后续技术报告中公开。

近一个月内，百灵迭代发布并开源了多款模型，覆盖 Ling 语言模型和 Ring 推理模型。记者注意到，相较于追求更大的参数规模或更高的单点分数，百灵更强调“真实生产环境使用”，系列模型集体切入“Token Efficiency”，强调用更少的 token 完成高质量的任务输出。市场对此也有明确反馈，Ling-2.6-flash 的匿名测试版本“Elephant Alpha”上线 OpenRouter 后，连续多日位列 Trending 榜首，日均 tokens 调用量达到100B级别。

*版权所有，未经授权不得以任何形式转载及使用，违者必究。*


[容联云发布“数字员工”级 Al Agent 平台，重塑大模型联络中心](https://www.qbitai.com/2026/05/418140.html)*2026-05-15*[阿里发布Qoder 1.0，可全面接管代码生成、验证和交付流程](https://www.qbitai.com/2026/05/418027.html)*2026-05-15*[智能无处不在：OpenClaw预示的AI未来](https://www.qbitai.com/2026/05/417958.html)*2026-05-15*[淘天金码奖落幕：20 名超级工程师诞生，推动 AI Native 实践](https://www.qbitai.com/2026/05/417927.html)*2026-05-14*
