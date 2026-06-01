---
title: "别光给Agent加Tool了，它根本选不明白！复旦×通义提出全新CUA训练范式"
source: 量子位
url: https://www.qbitai.com/2026/05/427005.html
date: 2026-06-01
published_at: 2026-05-31T14:25:18+00:00
tag: 论文研究
item_id: 2efc6165786dca4f
---
# 别光给Agent加Tool了，它根本选不明白！复旦×通义提出全新CUA训练范式

下一代CUA训练范式

复旦×通义团队 投稿

量子位 | 公众号 QbitAI


**给Agent同时接上GUI操作和工具调用，准确率反而下降了。**

模型根本不会在GUI和Tool之间选择。该点按钮的时候去调API，该调API的时候又死磕菜单，两头乱窜，越帮越忙。

为应对这一挑战，**复旦大学**和**通义实验室MobileAgent团队**联合提出**ToolCUA**，一个面向GUI-Tool混合动作空间的Computer Use Agent。

核心目标就一个：让模型学会什么时候走GUI，什么时候切Tool，什么时候不该调工具。

结果相当能打。

ToolCUA-8B在OSWorld-MCP上拿到**46.85%**准确率，超过**Claude-4-Sonnet**，逼近**Claude-4.5-Sonnet**。

**代码、模型权重已全面开源。**

![](https://i.qbitai.com/wp-content/uploads/2026/05/8e2f1aea4f0bc98b3bbfccee4ad63f23.png)

# 混合动作空间下的路径困惑

传统的CUA主要依赖原子化GUI操作，例如点击、输入、拖拽、滚动。这类操作泛化性强，只要界面上能看到按钮，理论上模型就能点；但它也有明显短板：步骤长、误差容易累积，在复杂任务中很容易出现cascading errors。

相反，tool calls或API-based operations往往更高效、更精确。例如在LibreOffice里批量处理表格，GUI-only方案可能需要一串冗长的菜单点击和参数配置，而工具调用可能一个API就能完成。

看起来最自然的方案，是让Agent同时拥有GUI和Tool。但实验发现一个非常反直觉的事实：**直接把tools接到强模型上，并不会自动提升性能。**

在hybrid GUI-Tool action space中，Agent每一步都站在一个岔路口：左边是GUI，右边是Tool。GUI泛化强但慢，Tool快但依赖覆盖与上下文条件。如果模型缺少路径选择能力，就会出现两类典型失败:

**Tool underuse**：明明有更高效的工具，模型仍然几乎只走GUI路线。

**Tool overuse**：模型频繁调用工具，但调用时机不对、调用粒度不对，反而降低任务成功率。

论文将这个问题定义为**optimal GUI-Tool path selection**：在长程任务中动态决定何时使用GUI actions、何时调用tools，从而形成更高效、更可靠的执行路径。

![](https://i.qbitai.com/wp-content/uploads/2026/05/eb90b8fdae55c7c42f5dde09425d7b0a.png)

上图左侧的表格直接给出了这个反直觉现象：一旦把tools接到强模型上，结果并不总是更好。

Qwen3VL-8B几乎不使用工具，平均tool calls只有0.003，准确率从29.0%降到28.2%；Qwen3VL-235B则明显更倾向于调用工具，平均tool calls达到6.10，步骤数从25.9降到17.4，但准确率反而从41.1%降到38.1%。

Claude系列同样说明了这一点。

Claude-4-sonnet在加入工具后步骤数从23.6降到19.2，但准确率从47.7%降到43.5%；Claude-4.5-sonnet的步骤数从23.3降到19.1，但准确率从61.9%降到48.4%。

这说明，混合动作空间真正难的不是有没有工具，而是**模型在GUI和Tool之间会不会选路**。

# 第一阶段：数据合成与Tool-Bootstrapped RFT

要让模型学会GUI-Tool path selection，首先需要高质量的interleaved GUI-Tool trajectories。但现实中，这类数据非常稀缺。

真实工具接口往往应用相关、覆盖不完整，而且维护成本高；而收集真实GUI-Tool混合轨迹又需要复杂的环境接入和人工标注。

已有GUI数据虽然规模很大，但大多是GUI-only trajectories，只教模型如何点击和输入，并没有告诉模型何时应该用工具替代冗长GUI操作。

ToolCUA的第一步，就是把这些GUI-only数据盘活，并顺势完成第一阶段的hybrid bootstrapping。

论文提出**Interleaved GUI-Tool Trajectory Scaling Pipeline**：从已有GUI轨迹出发，利用MLLM合成grounded tool library，再将GUI-only trajectories转换成interleaved GUI-Tool trajectories。

![](https://i.qbitai.com/wp-content/uploads/2026/05/02613396e0642e5b88a928a788f48b03.png)

整个pipeline可以概括为三个步骤:

**1、Trajectory-aware synthetic tool library construction。**

对每条GUI轨迹，模型会分析任务目标、动作序列和截图描述，从真实操作流程中抽象出可调用的工具。

例如从Chrome设置流程中抽象出chrome_open_language_settings，从LibreOffice表格操作中抽象出读取工作簿信息、创建透视表等工具。

这些工具不是凭空生成的API模板，而是grounded in concrete trajectory behavior，也就是从真实GUI行为中抽象出来的工具能力。

**2、Tool trajectory generation with next-state grounding。**

给定合成工具库和原始GUI轨迹，MLLM生成一个功能等价的tool-only trajectory，并为每一步预测tool response。

随后通过next-state grounding，将工具执行效果锚定到原始GUI轨迹中的下一帧截图，验证工具步骤和可见状态变化是否一致。

**3、Interleaved GUI-Tool trajectory generation。**

最后，系统不会简单地把所有GUI操作都替换成工具，而是随机采样部分工具调用，再替换回对应GUI子序列，形成多种GUI与Tool交错的轨迹。

这个设计非常关键：它让模型看到不同tool availability下的决策边界，也自然产生GUI -> Tool和Tool -> GUI的critical switching steps。

![](https://i.qbitai.com/wp-content/uploads/2026/05/300207877a49c7efec1ce32d2e9a6a7b.png)

最终，ToolCUA的数据中大约包括了4k个unique tools，覆盖fine-grained、mid-grained、coarse-grained多级粒度，大约有180k steps数据用于warmup SFT，还从critical steps中sample出5k条用于single-turn RL。

基于这些数据，ToolCUA进一步执行**Tool-Bootstrapped GUI RFT**。这一阶段的目标，不是直接学完整长程策略，而是先给模型打下一个可用的hybrid foundation。

具体来说，ToolCUA先在D_all上进行warmup SFT，学习多模态工具调用知识，包括工具用途、参数、返回结果，以及工具执行后的状态变化。

随后，模型在D_critical上进行single-turn RL，在明确的GUI-Tool switching steps上采样多个completion，并通过反馈校准模型在局部边界上的选择。

这一阶段做的事情是：**先把interleaved GUI-Tool数据合成出来，再让模型先学会会用工具和在局部切换点上别选错。**

# Online Agentic RL与Tool-Efficient Path Reward

如果说第一阶段解决的是模型先要进入hybrid action space，那么第二阶段解决的就是：**模型如何在真实环境里学会trajectory-level的路径选择。**

ToolCUA的第二阶段是**Online Agentic RL**。这一步不再只优化单步动作，而是在真实GUI-Tool environment中进行long-horizon rollout，让模型学习完整任务轨迹上的路径选择。

团队首先构建了同时具备GUI actions和Tool calls的高可用Sandbox用于agentic RL，并且为工具返回结果设计了更加结构化的格式便于模型理解。

Agentic RL优化的核心是**Tool-Efficient Path Reward**:

![](https://i.qbitai.com/wp-content/uploads/2026/05/5dd74d9f65f1b2a45b7e8f9e6cfecf42.png)

其中，R_fmt和R_acc分别是标准格式奖励与任务成功奖励；R_tool和R_length则是ToolCUA专门设计的两项轨迹级奖励，并且它们只在成功轨迹上激活，避免模型从失败执行里学到错误偏好。

第一项是**Tool Appropriateness Reward (R_tool)**。

![](https://i.qbitai.com/wp-content/uploads/2026/05/71f9dd1208de69fb5e1784d0624b418e.png)

在数据构建时，每个任务会带一个task-level的tool-beneficial标记：t_b = 1表示这个任务适合用工具，t_b = -1表示这个任务不适合用工具。与此同时，c表示整条轨迹里的tool calls数。

于是，R_tool奖励的不是工具调用更多，而是更精确的两种行为:

对于适合工具的任务，成功轨迹里确实调用了工具。

对于不适合工具的任务，成功轨迹里反而没有乱用工具。

它要解决的正是前面提到的hybrid confusion：有些模型明明该用工具却不用，有些模型则在不该用的时候乱用。R_tool的作用，就是把工具是否合适这件事从任务成功里单独拎出来训练。

第二项是**Path Efficiency Reward (R_length)**。

这里，s是当前轨迹的步数，\bar{s}是同组rollout的平均步长，S_max是最大执行步数。ToolCUA不拿一个固定阈值来判定长还是短，而是做group-relative comparison:

如果某条成功轨迹比组内平均更短，就给线性bonus。

如果更长，就做衰减。

这样设计的好处是，模型会自然倾向于探索更短的成功路径。而在很多场景里，更短的路径恰恰意味着：用一个高层工具替代一长串冗余GUI操作。因此，R_length本质上是在鼓励模型发现更高效的**GUI-Tool execution path**。

所以，这一阶段的核心并不是让模型调用更多工具，而是让它学会两件事：**什么时候工具真的合适，什么时候这条执行路径真的更短。**

# OSWorld-MCP上达到46.85%，相对提升约66%

ToolCUA主要在OSWorld-MCP上评测。这个benchmark在传统OSWorld的基础上引入了hybrid GUI-Tool action space，覆盖典型GUI actions、150+ tools和主流桌面应用，适合衡量模型在真实混合动作空间中的执行能力。

评测指标包括:

- Accuracy：任务成功率
- TIR (Tool Invocation Rate)：是否做对任务，并且在tool-beneficial tasks中使用工具，并在non-tool-beneficial tasks中避免工具
- ACS (Average Completion Steps)：平均完成步数，衡量执行效率

![](https://i.qbitai.com/wp-content/uploads/2026/05/069a9ab2d738f13ac0914146ca15b5a2.png)

ToolCUA-8B在OSWorld-MCP上取得**46.85%** accuracy，相比Qwen3-VL-8B-Instruct baseline的**28.23%**，相对提升约**66%**。

同时，ToolCUA超过了GUI-Owl-1.5-8B(**43.84%**)、Gemini-3.1-Pro(**41.14%**)和Claude-4-Sonnet(**43.54%**)，并接近Claude-4.5-Sonnet(**48.35%**)与GUI-Owl-1.5-32B(**48.05%**)。

更重要的是效率指标。ToolCUA的ACS仅为**14.93 steps**，是表中所有模型里最低的。这说明ToolCUA不只是完成了更多任务，也学会了用更短路径完成任务。

与Qwen3-VL-8B-Instruct相比，ToolCUA的overall TIR从**8.41%**提升到**24.32%**，ACS从**19.34**降到**14.93**。这说明模型不仅更会做任务，也更会判断什么时候应该调用工具。

![](https://i.qbitai.com/wp-content/uploads/2026/05/4e0774066a56d05b07908191220aaad3.png)

在训练阶段，Online Agentic RL只使用单应用Linux任务，并刻意排除了multi_apps domain，用于OOD验证。

结果显示，在held-out multi_apps任务上，ToolCUA从baseline的**9.8%**和pre-online RL stage的**18.5%**提升到**23.9%**。

在具体应用域上，ToolCUA也有明显提升。例如在libreoffice_calculation上从**19.6%**提升到**34.8%**，在vs_code上从**66.7%**提升到**94.4%**。

![](https://i.qbitai.com/wp-content/uploads/2026/05/b0163635df9fba6ad0c64a7dcffb2a0c.png)

更进一步，ToolCUA还在WindowsAgentArena上进行评测。

尽管训练数据和sandbox都来自Linux桌面环境，ToolCUA在unseen Windows desktop apps上达到**33.8%** accuracy，超过Qwen3-VL-8B-Instruct的**26.4%**、Qwen3-VL-32B-Instruct的**30.9%**，也超过Qwen3-VL-235B-A22B的**32.1%**。

这说明ToolCUA学到的并不只是某些特定任务模板，而是更接近一种可迁移的**hybrid action orchestration**能力。

# 为什么ToolCUA真正学会了选路

ToolCUA的提升到底来自哪里？论文里的ablation很清楚地给出三条结论。

**第一，如果没有interleaved GUI-Tool trajectory data，online RL本身学不会可靠的tool use。**

![](https://i.qbitai.com/wp-content/uploads/2026/05/8e01aa658fb009f7d98a9e7b7407a08d.png)

当去掉offline interleaved GUI-Tool bootstrapping，直接从Qwen3-VL-8B-Instruct baseline开始做online agentic RL时，模型的overall accuracy虽然也会继续上升，但它很难真正学会稳定的工具调用行为。

最典型的现象是：TIR长期偏低，训练后期也只到约**15%**；tool calls在大部分训练过程中都接近**0**。

这说明，仅靠trajectory-level online reward，并不足以让一个GUI-centric base model自然长出靠谱的hybrid switching能力。模型需要先通过interleaved supervision获得工具知识和切换先验。

**第二，如果没有Tool-Efficient Path Reward，模型学不会稳定且高效的路径。**

同样在rl_dynamics里可以看到，去掉R_tool和R_length后，只保留标准的R_acc与R_fmt，accuracy曲线会明显更不稳定，在训练step **8-11**左右出现下降，最终与完整ToolCUA之间有大约**7个点**的差距。

与此同时，TIR和tool-calls也没有稳定上升趋势，trajectory length也缺少持续下降。

这说明，任务成功奖励本身不足以教会模型什么时候工具是合适的和什么路径才是真正高效的。

**第三，Hybrid GUI-Tool training比pure GUI training更有效。**

![](https://i.qbitai.com/wp-content/uploads/2026/05/a304db04dc71fdfd06c81476ca809e88.png)

论文进一步比较了pure GUI training和hybrid GUI-Tool training。

GUI-only pipeline从baseline **29.03%**提升到SFT后**34.93%**，再到agentic RL后**42.05%**；而GUI+Tool pipeline中，RFT已经达到**38.13%**，完整ToolCUA进一步达到**46.85%**。

这表明hybrid GUI-Tool action space本身就是一个更高保真的训练环境。模型不只是学visual grounding，也在这个过程中学会何时应该用结构化工具替代冗余GUI操作。

WindowsAgentArena的结果也说明，这种训练范式带来的不是单点收益，而是更强的**跨平台泛化能力**。

# 真正的GUI-Tool协同

为了更直观地理解ToolCUA的能力，可以看两个实际案例。

第一个是LibreOffice Calc任务：用户要求在一个名为Sheet2的新sheet中创建两个pivot tables，分别统计product和sales channel对应的total revenue。

GUI-only方法通常需要选择数据范围、打开菜单、配置字段、确认参数，步骤冗长且容易出错。

ToolCUA则先调用工具读取workbook信息和sheet内容，识别数据结构与字段位置，然后直接调用create_pivot_table生成透视表。

![](https://i.qbitai.com/wp-content/uploads/2026/05/d766b21c9edbf10d9ae992a4b22d51aa.png)

这个案例展示的不是工具永远比GUI好，而是: 当任务核心是结构化表格操作时，Tool可以绕过脆弱的逐步GUI导航，用更确定的方式完成任务。

![](https://i.qbitai.com/wp-content/uploads/2026/05/ef0fbee1cf9460d430406484401ba18a.png)

第二个案例来自VS Code。任务是将/home/user/data1和/home/user/data2两个文件夹加入当前workspace。

ToolCUA先连续调用add_folder工具，把两个目录加入VS Code workspace。

这一步非常适合工具调用，因为路径明确、操作结构化、目标可验证。

![](https://i.qbitai.com/wp-content/uploads/2026/05/a15cd927efdd03b7a85f18f69920778d.png)

但工具调用完成后，VS Code弹出了Do you trust the authors?的信任确认对话框。

这个状态不是简单tool call就能闭环的。

此时ToolCUA切换回GUI action，点击Yes, I trust the authors。

![](https://i.qbitai.com/wp-content/uploads/2026/05/422c3274faabb312c2c4899c7cb16586.png)

完成界面上的最后一步。

![](https://i.qbitai.com/wp-content/uploads/2026/05/55446e26fc163400b3dbd91cd5003d29.png)

这正是ToolCUA想解决的问题：它不是试图用Tool替代所有GUI，也不是退回纯GUI操作，而是在真实环境里学习两种action space的**协同与切换**。

# Hybrid action training，下一代CUA训练范式

在agent热潮的推动下，computer use agent正在更积极地探索真实世界里的落地路径。

ToolCUA为社区揭示了一个关键现象：一旦进入hybrid action space，现有CUA和部分强基座模型会出现明显的路径困惑，甚至导致准确率下降。

团队通过staged training paradigm在hybrid action training上做了一次有益探索，并验证了这一路线的有效性。

接下来，更值得继续和推进的方向，是构建更大规模的CUA工具，训练更大规模的CUA基座模型，让CUA原生具有hybrid actions的能力，更好地解决人类复杂问题。

项目网站：https://x-plug.github.io/ToolCUA/

代码仓库：https://github.com/X-PLUG/ToolCUA

模型地址：https://huggingface.co/mPLUG/ToolCUA-8B

Mobile-Agent系列：https://github.com/X-PLUG/MobileAgent


*版权所有，未经授权不得以任何形式转载及使用，违者必究。*


[DDIM之父宋佳铭，宣布离职](https://www.qbitai.com/2026/05/427104.html)*2026-05-31*[英伟达版「MacBook Pro」曝光：老黄自研了CPU！](https://www.qbitai.com/2026/05/426991.html)*2026-05-31*[清华有了新老师：黄仁勋](https://www.qbitai.com/2026/05/425948.html)*2026-05-28*[5亿Tokens白送！全球首个商用AI主机发布，终于能放开烧Token了](https://www.qbitai.com/2026/05/426479.html)*2026-05-29*
