---
title: "Building Cloud Environments for Coding Agents"
source: TLDR AI · 2026-07-31
url: https://cursor.com/blog/cloud-agent-environment?utm_source=tldrai
date: 2026-08-01
published_at: 2026-07-31T12:00:00+00:00
tag: 工具开源
item_id: 551f30c0552852e8
---
# 我们如何搭建云端智能体环境

[Mathew Hogan](https://cursor.com/cn/blog/author/mathew-hogan)&

[Arvind Saripalli](https://cursor.com/cn/blog/author/arvind-saripalli)2 分钟阅读

当我们决定[为云端智能体配备电脑](https://cursor.com/blog/agent-computer-use)，让它们能够测试自己所做的更改时，第一步是确保它们能在我们的代码库中熟练地进行测试。

让云端智能体能够使用我们的单体仓库，使我们意识到开发环境本身也是一种产品，只不过它的用户是智能体。你需要让云端环境与本地开发环境保持一致，让仓库足够清晰，使智能体无需了解团队内部的隐性知识也能运行和测试代码，并随着代码库的演进持续维护环境的健康状态。

构建这一环境改变了我们的工作方式。去年 12 月，合并到 Cursor 单体仓库的 PR 中，约十分之一由云端智能体编写。如今，这一比例已超过一半。

### 7-day rolling share of merged PRs from cloud agents

## 

要让云端智能体在我们的仓库中顺畅运行，第一步是让仓库能够在云端 VM 中顺畅运行。对于第一次搭建远程开发环境的工程师来说，这个阶段并不陌生。

大多数 Cursor 开发者在 Mac 上进行本地开发，而我们的云端 VM 运行 Linux。因此，我们需要让各种开发工具和设置脚本适配 Ubuntu VM。我们将关键开发依赖项添加到 Cursor 定义的 Dockerfile 中，该 Dockerfile 作为[云端智能体](https://cursor.com/docs/cloud-agent)的基础镜像。

![云端智能体在其环境中安全运行](https://cursor.com/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fcloud-agents-light-87YVZRZvWMWUkZ2ztCc6hIcohupUY9.png&w=1920&q=70)

![云端智能体在其环境中安全运行](https://cursor.com/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fcloud-agents-dark-ES43zfdrxU43nOLCVEUVDfXAbFSBWn.png&w=1920&q=70)

我们还与安全团队合作，为云端智能体产品添加了安全功能，让用户可以放心地将必需的密钥注入智能体环境。这些功能包括网络出口限制、受范围限制并经代理的 Git 远程访问、对提交和提交消息进行密钥扫描，以及对工具结果中的密钥进行脱敏处理；即使智能体尝试读取，也无法获得密钥值。

## 

即使我们已在 Ubuntu VM 上搭建好开发环境，智能体仍不擅长运行我们的代码。这并不意外，因为我们的开发体验十分混乱，需要学习和记忆大量构建命令、构建选项及实用脚本。

我们为系统中许多部分的构建和运行方式编写了技能，但帮助有限。技能可以记录正确的命令，但这些命令本身就很复杂，且暗藏许多陷阱。

为降低这种复杂性，我们构建了一个名为 anydev 的 CLI，智能体可用它启动所有服务。我们也将常用实用脚本统一通过 anydev 调用，并为 anydev 配备了多个 `--help` 菜单，说明各个子命令的用法。anydev 还包含一个监管进程，可监控并重启长时间运行的构建命令，完全免去了模型的这项职责。

anydev 让开发体验变得足够简单，使智能体能够可靠地运行代码。技能有助于说明其用法，但更大的改变是，智能体不再需要应付冷门的多步骤构建命令、避开隐藏陷阱，或盯着长时间运行的进程。

从这时起，拥有各自计算机的云端智能体开始比本地智能体展现出真正的价值。借助计算机使用能力、recordScreen 工具和可用的开发环境，智能体现在能够端到端测试其更改，并向用户证明其工作成果的正确性。

当有人修复缺陷报告或提交变更 PR 时，它们还可以在 Slack 或 PR 中分享由智能体录制的演示。对于许多任务，工程师如今可以放心地合并和部署云端智能体编写的代码，甚至无需在本地检出分支。

## 

智能体周围的环境始终在变化，因此要保持环境正常运行，就需要持续更新其运行方式以及可访问的资源。

为了在不健康的环境出现故障时进行诊断和恢复，我们构建了 [Cursor Cloud MCP](https://cursor.com/docs/cloud-agent/capabilities#cursor-cloud-mcp)。我们选择 MCP，是因为它提供了可动态发现的工具，且无需重新构建智能体循环即可更改其接口。云端智能体使用它检查自身环境中的设置失败、出口策略、已变更的密钥等。这使它们能够在问题出现时诊断并修复问题，更快恢复不健康的环境。

有了 Cursor Cloud MCP 后，我们设置了一项名为 Cloud Doctor 的[自动化功能](https://cursor.com/automate)。它会定期检查失败项，识别哪些错误信息可能是暂时性的、哪些值得关注，进行根本原因分析，并可在有较高把握时创建 PR 来修复问题。

## 

即使环境运行正常，智能体有时也会通过冗长或曲折的路径来确认所做的更改。它们可能使用错误的技能、在 VM 中遇到本可避免的问题，或遵循耗时超出应有程度的工作流。

我们同样会使用 Cursor Cloud MCP。Cloud Doctor 智能体会检查链路追踪，找出其他智能体在哪些环节出错、哪些技能或命令容易造成误导，以及哪些工作流长期偏慢。根据这些发现项，Cloud Doctor 会修复技能、简化路径，或调整环境，让下一个智能体更轻松地完成任务。

这一循环不断改善智能体本身的开发者体验。当环境健康且具备自愈能力时，智能体能稳定运行，开发者也会放心将更重要的工作交给云端智能体。

这让我们能够在内部扩大云端智能体的应用规模，如今它们已编写了我们交付代码中的大多数。

![Cloud Doctor 创建 PR 以修复不健康的环境](https://cursor.com/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fcloud-heal-light-yMlLRraMEnhKaeOHfHV1D2imkVt13g.png&w=1920&q=70)

![Cloud Doctor 创建 PR 以修复不健康的环境](https://cursor.com/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fcloud-heal-dark-PvfCh7vICeb0SxCVwLB0jLH4rtlcFt.png&w=1920&q=70)

## 

云端智能体能否高效工作，很大程度上取决于环境。要了解您的代码库是否已准备就绪，请先回答以下三个问题：

1. 智能体是否能访问开发者可用的相同工具和数据？
2. 智能体能否找到记录开发者实际工作方式的技能？
3. 智能体能否测试并确认核心工作流？

如果您需要协助准备环境，[请联系我们](https://cursor.com/contact-sales)。

或者，如需了解更多，请阅读 Faire 如何借助云端智能体[将每周 PR 吞吐量翻倍](https://cursor.com/blog/faire)。
