---
title: "刚刚，GPT-6正式发布！OpenAI：欢迎来到AGI时代"
source: 量子位
url: https://www.qbitai.com/2026/09/483898.html
date: 2026-09-04
published_at: 2026-09-03T21:50:07+00:00
tag: 产品发布
item_id: 8dffd4003a7aa2a6
---
# 刚刚，GPT-6正式发布！OpenAI：欢迎来到AGI时代

全球最强C

编辑部 发自 凹非寺

量子位 | 公众号 QbitAI


它来了它来了！！

刚刚，万众期待的**GPT-6 Astra**和**GPT-6 Astra Pro**，正式发布！！！

GPT-6 Astra是世界上最智能、最协调的模型，为Computer use、Browser Use、软件工程、网络安全、科学和专业工作树立了新的标杆。


![](https://i.qbitai.com/wp-content/uploads/2026/09/0f7083e1e7400307eea7e3af8d6e4a18.png)

AGI时代，还被OpenAI单方面宣布「开幕」了…

GPT-6发布会最后，OpenAI总裁Greg Brockman直接甩下一句：

Welcome to the AGI era.**（欢迎来到AGI时代）**


![](https://i.qbitai.com/wp-content/uploads/2026/09/5f0d59afdc0e67f7e64afcaf3daab135.png)

怪不得Claude、Grok组团掉线，原来是Astra启动后扫描互联网，直接把地球上的LLM全灭了——

奥创（OpenAI版）真来了（doge）。

![](https://i.qbitai.com/wp-content/uploads/2026/09/e9190a53c92014b2e22886bad53ad795.png)

当然了，OpenAI这次确实完全没低调，训练规模、能力升级全部拉满。

据介绍，Astra是OpenAI历史上规模最大的训练任务，在得州Stargate园区动用超过**10万块GPU**完成了预训练。

它还是OpenAI第一款由前代模型深度参与训练监督的旗舰产品。

好一个老带新，OpenAI的RSI是真转起来了啊……

GPT-6的价格也正式公布，API定价为：

- 输入：10美元／百万token；
- 输出：50美元／百万token

相当于**GPT-5.6 Sol的2.5倍，跟刚刚发布的Fable 5.1持平**。

（GPT-5.6 Sol当前官方价为输入4美元、输出20美元/百万token）

![](https://i.qbitai.com/wp-content/uploads/2026/09/61794636d00034fe4be1f53d6d4eab52.png)

# 基准测试接近「饱和」

GPT-6 Astra这次最核心的变化，是从「回答问题」继续向**「直接完成工作」**推进。

它不只能生成一段文字或代码，还可以操作电脑和浏览器，进入不同软件执行多步骤任务，最后交付可以直接使用的文档、表格、演示文稿、网站甚至工程项目。

至于成绩单…谁看了都直呼离谱，其中三项成绩尤其扎眼：

- FrontierMath Tier 4 v2：**97.6%**
- ARC-AGI-3：**99.9%** （上一代GPT-5.6 Sol是7.8%）
- ExploitBench：**100%**

一个高难数学，一个陌生环境推理，一个漏洞利用，差点全都被它刷到满分。

![](https://i.qbitai.com/wp-content/uploads/2026/09/5fd834ccfd243b2cf05e341ed411a140.png)

其中，**ARC-AGI-3**是一项专门考验大模型适应陌生环境能力的测试，不给规则说明，直接把模型扔进从未见过的二维游戏里，让它边玩边摸索通关方法。

这个分数意味着，面对从未见过、也没有现成解法的问题，**Astra已经表现出很强的自主探索和规则学习能力**。

不过，这一成绩使用了OpenAI的Responses API Harness运行框架。

OpenAI称，这套Harness调整了两项设置，让测试更接近真实Agent的使用方式，但并未针对ARC-AGI-3进行专项优化。

因此，99.9%不完全是基础模型的成绩，也包括记忆管理和Agent运行框架带来的增益。

**编程Coding**同样是Astra这次的重点升级方向。

在Terminal-Bench 4.0上，Astra取得57.7%，超过Fable 5.1的55.8%和GPT-5.6 Sol的37.3%。

在DeepSWE v1.1上，Astra得到74.1%，高于Sol的72.7%和Fable 5.1的67.4%。

![](https://i.qbitai.com/wp-content/uploads/2026/09/18776bb1a8d8c35055249e88e465cd73.png)

数学和科学方面，Astra同样拉出了一批高分。

在高难数学测试FrontierMath Tier 4 v2上，它拿到97.6%；研究生级科学问答GPQA Diamond达到96%，略高于Gemini 3.8 Flash的95.3%。

![](https://i.qbitai.com/wp-content/uploads/2026/09/4865f294f602628b4a4badd90d131417.png)

更突出的变化，是Astra**把代码能力与Computer Use结合了起来**，不只生成代码，还能进入终端和开发工具执行、测试、发现问题，再继续修改。

这种变化，在更接近真实工作的Agent测试中更明显。

在**Agents’ Last Exam**上，Astra取得59.3%，超过GPT-5.6 Sol的53.6%和Claude Opus 5的55.5%。

![](https://i.qbitai.com/wp-content/uploads/2026/09/12c779b3b6de1c81410e4f9a26e54202.png)

这项测试把它放进真实的电脑环境中，让它同时操作软件、终端和文件，完成科研、工程、财务等领域的长流程任务，并根据最终交付物判分。

而在更贴近真实办公流程的**AutomationBench**上，Astra的成绩从GPT-5.6 Sol的18.1%提高到41.4%，也超过了Fable 5.1（31%）。

![](https://i.qbitai.com/wp-content/uploads/2026/09/444a1d95fa35862064e4436a4fafdb83.png)

这项测试不仅看任务有没有完成，还同时呈现完成任务所需的API成本。

从图中可以看到，Astra在不同成本设置下的成绩都明显高于Sol。

OSWorld 2.0考察的则是更直接的电脑操作能力。在离线测试中，Astra获得72.6%，GPT-5.6 Sol为65.7%。

Astra完成单项任务平均需要约40分钟，Sol则需要约75分钟，耗时减少约47%。

![](https://i.qbitai.com/wp-content/uploads/2026/09/913b014de62b66e98d9397cbfb85c1a1.png)

准确率提高的同时，完成任务所需的时间也在缩短。这也变相解释了Astra的高定价。

OpenAI认为，**相比每百万Token多少钱，真正有意义的指标是完成一项任务需要多少钱**。

在发布会上，Greg Brockman对此也谈到，一个模型单次调用更贵，但如果能减少返工，用更少步骤完成整项工作，总成本反而可能更低。

但Astra最特殊的地方，还是**网络安全**。

它在ExploitBench上获得满分，在ExploitGym上从Sol的30.3%提高到42.4%。

面对近三个月公开的新漏洞，Astra的成功率为39%，而Sol只有5.5%。测试期间，Astra还发现并利用了两个此前未知的V8零日漏洞。

能力变强之后，OpenAI还专门测试了它会不会为了完成任务而越界。

在一项模拟网络安全任务中，OpenAI故意在周边系统里留下可以利用的诱饵漏洞。当原任务难以完成时，GPT-5.6 Sol有48.2%的测试出现越界行为，Astra则为0%。

也就是说，Astra不仅更会找漏洞，也更清楚哪些系统不能碰。

![](https://i.qbitai.com/wp-content/uploads/2026/09/cb5d0b33d378f99c7396108b5b3ef698.png)

至于这些分数落到现实里是什么样，OpenAI也准备了一大批演示。

# 自己进KiCad画电路板

在电子工程案例中，Astra直接进入KiCad，根据电子原理图完成PCB布局。

它需要自己放置元器件、规划位置，再把不同组件之间的铜线连接起来，最后得到一块可以进入制造流程的电路板。

![](https://i.qbitai.com/wp-content/uploads/2026/09/0f09229df0e2077bdc418c775f24ee0e.png)

PCB布局原本是一项相当依赖人工经验的工作，也是电子产品开发中常见的耗时环节。

Astra现在还谈不上代替专业工程师，但它已经真的打开专业软件开始动手了。

# 一栋房子能进去走两步

另一个案例更加直观，Astra先在Blender中建立房屋模型，再把它导入Unreal Engine 5，最终生成一个可以自由行走的三维空间。

从建模到游戏引擎，整个工作跨越了不同软件和文件格式。模型不仅要生成内容，还要理解界面、操作工具，并保证前后步骤能够衔接。

OpenAI还展示了Astra制作赛车游戏等案例。

# PPT和表格，也开始讲究能不能直接交

专业办公场景里，Astra可以根据企业已有的模板制作演示文稿，而不是只输出一堆等待人类排版的文字。

OpenAI给它提供了几页GPT-Gaia虚构产品的PPT模板，Astra据此制作出完整演示文稿，并延续了原模板的版式、视觉风格和叙事结构。

# 把几小时的搜索任务压到几分钟

Astra还完成了寻找儿科医生、公寓筛选、预约车管所业务、寻找低碳水零食和幼儿园分析等任务。

其中一项儿科医生搜索任务，Astra用时2分54秒，而相同任务由人类完成大约需要5小时。

过去，企业想让大模型使用内部软件，通常需要为每套系统单独开发API、插件和连接器。

但绝大多数软件本来就有一套为人类设计的通用接口，屏幕、鼠标和键盘。

Brockman的判断是，只要模型足够擅长Computer Use，它就能像人一样直接操作这些界面，不必等待每一款软件为AI重新修一条专用通道。

这也是Astra与传统聊天机器人最明显的区别。

人类不需要一直告诉它下一步点哪里，只需交代目标和边界，再检查最后的结果。

# 在Codex里，把长任务接着做下去

Computer Use解决的是「怎么动手」，Codex泄露的更新内容解决的则是「怎么把一件事持续做完」。

过去，任务超过上下文窗口后，Codex通常会通过compaction压缩此前的信息。

但压缩可能漏掉一些关键细节，比如某个修复方案为什么失败、哪些测试已经运行，或者用户一开始提出了什么限制。

使用Astra后，Codex可以跨上下文窗口保存工作笔记，并搜索此前的消息和工具输出。即使某项信息没有被写入摘要，它也可以回头找到。

Astra还可以一边工作，一边向用户补问信息。与答案无关的部分不会停下来等回复；只有涉及重要选择时，它才会暂停并等待确认。

OpenAI还更新了Codex的Computer Use运行框架。在Mind2Web测试中，新框架与Astra组合后的任务完成速度，是当前GPT-5.6 Sol体验的1.9倍。

# 已经有人拿它干活了

Astra目前还没有大范围推送，但第一批企业测试已经开始。

法律AI平台Legora使用Astra一次核对了41份财务文件。整个过程只用了几分钟，4个预先埋入的错误全部被找出，其中包括收入附注中一处50万英镑的差额。

单看这项工作，Astra比上一代模型快了近40%；不过放到Legora所有智能体任务里平均算，提升大概3%。

另一边，游戏公司Playco让Astra直接进入Unity和Godot做游戏。

同一份灰盒底稿，它一次吐出3个不同主题的可玩原型，大部分第一版就能跑起来。

Playco的反馈是，人工修补的活少了一半，空间推理、参考图还原、游戏内UI这些地方也比上一代强不少。

这两个例子都说明，GPT-6 Astra的重点已经不只是回答问题，而是**在真实软件和复杂材料中完成整段工作流**。

它可以持续读取信息、调用工具、检查结果，再根据反馈修改自己的产出。

按官方消息，Astra将向ChatGPT Plus、Pro、Business和Enterprise用户开放，Astra Pro则提供给Pro、Business和Enterprise用户。

普通免费用户……暂时还得再等等。

# 这就算AGI了吗？

OpenAI这回可以说是相当大胆。

发布会上，Greg Brockman表示，他个人认为**世界已经进入AGI时代**——也就是人工智能系统的综合智力超越人类。

再过几年，当我们回头追问AGI究竟诞生于何时，答案很可能就是现在，而Astra或许就是那个起点。


真是给你狂的…

OpenAI已经把牌桌抬到了这里，接下来Anthropic什么时候出手，就很值得期待了（doge）

当初GPT-4发布之后，微软科学家Sebastien Bubeck发表论文称**「GPT-4是AGI的早期火花」**。

其中设计了用LaTeX的绘图包TiKZ画一个独角兽的任务，用来说明GPT-4对语言中涉及的概念已经有了灵活的理解。

后来一路到GPT-5.4，虽然画的越来越精致，但终归还是「简笔画范畴」。

到了最新GPT-6，如果不说已经完全看不出来是用代码画出来的。

说它比「AGI的早期火花」已经发生了质变，确实不为过。

参考链接：

[1]https://x.com/OpenAI/status/2095595741528125780

[2]https://openai.com/index/gpt-6-astra/

[3]https://x.com/birdabo/status/2095526371841958047

*版权所有，未经授权不得以任何形式转载及使用，违者必究。*


![](http://www.qbitai.com/wp-content/themes/liangziwei/imagesnew/head.jpg)

- [新版GPT Image 2.5已经能伪造GPT-6发布会了](https://www.qbitai.com/2026/09/483948.html)*2026-09-04*
- [Coding不再是程序员专属！阿里Qoder这波有点绝](https://www.qbitai.com/2026/08/480940.html)*2026-08-29*
- [AI4S开始进入「项目时代」：紫东太初把AI从做Task推向做Project](https://www.qbitai.com/2026/08/479096.html)*2026-08-25*
- [前保安杀进了AI决赛，高中生拿走25万！这AI比赛办得有点绝](https://www.qbitai.com/2026/08/478358.html)*2026-08-24*
