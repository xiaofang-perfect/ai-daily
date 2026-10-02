---
title: "何恺明团队新作：看猫片就能学会ARC挑战"
source: 量子位
url: https://www.qbitai.com/2026/10/499812.html
date: 2026-10-02
published_at: 2026-10-01T15:06:30+00:00
tag: 论文研究
item_id: fd82fac9b704f1ef
---
# 何恺明团队新作：看猫片就能学会ARC挑战

用ImageNet训练encoder

克雷西 发自 凹非寺

量子位 | 公众号QbitAI


教会AI做ARC抽象推理题的，竟然是猫猫？

![](https://i.qbitai.com/wp-content/uploads/2026/10/e32282d4e6facef6e97ad9ea54be37df.png)



何恺明团队最新论文提出了**NAT-ARC，一套纯视觉的ARC解题方案。**

它不靠LLM，用ImageNet上的猫狗花草做预训练，让模型学会「看」，再迁移到抽象格子推理上。

结果，NAT-ARC表现最好的单模型在ARC-1上跑出了63.4%的pass@2分数，集成后达到70.2%。

![](https://i.qbitai.com/wp-content/uploads/2026/10/46425b8a47a83342635a1d7f373f8a4e.png)



这是纯视觉方案首次**逼近专用LLM系统**的水平。

ARC，公认最难的AI视觉智力测验之一，给你几个彩色格子的输入输出示例，让你推断背后隐藏的变换规则，再应用到新格子上。

过去的主流解法清一色把格子翻译成文字或符号，交给LLM推理。

这篇论文偏不，甚至预训练阶段连ARC格子都没用上。

模型看真实世界学来的视觉能力，就水灵灵地迁移到了完全抽象的彩色格子推理上。

## ARC赛道，视觉方案崛起

ARC全称Abstraction and Reasoning Corpus，由Keras之父François Chollet在2019年提出。

ARC里每道题的格式很统一，一块最大30×30的二维格子，最多10种颜色，题目给2到5组输入输出示例，挑战者需要从示例中推断出隐藏的变换规则，再把这条规则应用到一个全新的输入格子上，预测它的输出。

![](https://i.qbitai.com/wp-content/uploads/2026/10/17ba46bfdf073b25cbf63098d6b38e3d.gif)



这些问题听起来像看图找规律的儿童智力题，但ARC对AI来说极难。

一方面，每道题的变化规则都不一样，没有固定模板可背。

还有就是数据量极少，两三个示例就要归纳出抽象规则，并且精确执行。

这种组合让ARC成了**测量AI抽象推理能力的标杆**。

目前ARC赛道上占据统治地位的几乎全是大语言模型方案，这些方案的共同思路都是把格子翻译成文本或符号序列，交给语言模型处理。

![](https://i.qbitai.com/wp-content/uploads/2026/10/2b8b7fe1202d9b3db4c33903d5753eda.png)



视觉路线后来才开始崛起。

一批研究者走了一条完全不同的路，他们不把格子翻译成文字，改成了用视觉模型直接处理格子图像。

其中最重要的一步来自同一个MIT团队提出的**VARC**，这个方法把ARC重新定义为条件图生图翻译任务，用19M参数的视觉模型跑到54%。

![](https://i.qbitai.com/wp-content/uploads/2026/10/7282724b077599258bf2323490f1bbd2.png)



LoopViT在这个框架上加入循环推理机制，18M参数达到65.8%。

Loop-OWM用视频预训练模型做few-shot，10.6M参数达到68.5%。

这些模型的参数量比LLM方案小了几个数量级，但效果已经开始追平。

![](https://i.qbitai.com/wp-content/uploads/2026/10/40f7ce3eb3bf9c265ef148c077e3be46.png)



但视觉路线依然有一个结构性短板。

LLM之所以能在ARC上越做越好，核心原因之一是它们通过海量语料预训练，积累下了通用能力，模型越大、预训练越充分，在下游任务上的scaling就越明显。

而多数视觉ARC方案的模型从随机初始化开始训练，没有吃到预训练的红利。

在此基础上，NAT-ARC的目标就是给视觉路线补上预训练这一步，试着打通它的scaling瓶颈。

## 看完猫猫，挑战ARC

NAT-ARC的核心思路，是**在VARC的视觉流程前面插入一步ImageNet MAE预训练**。

MAE，Masked Autoencoder，是何恺明在FAIR时期2022年提出的自监督视觉预训练方法。

其训练过程，是把一张图片遮住大部分区域，让模型从剩下的碎片里把原图复原出来。

通过这个任务，模型就可以理解物体的形状、结构和空间关系。

![](https://i.qbitai.com/wp-content/uploads/2026/10/9895664e70c9abed8cefa38d83265462.png)



NAT-ARC的做法是把MAE在ImageNet（包含约130万张猫狗花草等自然图像的数据集）上训出来的encoder权重直接拿来初始化视觉编码器，decoder则从随机初始化开始训练。

整个流程分三步。

- 第一步，用ImageNet上的MAE预训练encoder；
- 第二步，在ARC训练集上离线训练整个编解码器；
- 第三步，在测试时对每道题单独做LoRA微调。

微调阶段，每道题只有2到5组示范对，模型用这几组示范试图从中“学会”这道题的规则。

有个细节值得注意，NAT-ARC直接用了MAE的公开checkpoint，没有额外花一分钱预训练。

不过，这个checkpoint原本是为更大尺寸的ImageNet图片设计的，而ARC格子只有64×64像素，尺寸差异很大。

为了适配，NAT-ARC丢弃了原始的patch embedding和位置编码，只保留backbone权重，换成2D RoPE作为位置编码。

简单说，NAT-ARC只保留了MAE在ImageNet上学到的视觉特征提取能力，而把与ImageNet图像尺寸绑定的空间感知部分全部丢掉，用更灵活的方式重新学习。

![](https://i.qbitai.com/wp-content/uploads/2026/10/1a5033e921e217aeaca6733b40728682.png)



但为什么看猫狗照片学到的东西，能帮到抽象格子推理？

论文用注意力可视化给出了一条线索。

研究人员把三种初始化方式（无预训练、ImageNet MAE预训练和ARC风格格子MAE预训练）的模型放在同一道ARC题前，观察它们在还没开始训练ARC之前的注意力分布。

结果很明显，随机初始化的模型注意力均匀分散，毫无重点；而ImageNet预训练过的模型已经能区分前景和背景，注意力自动聚焦到格子中有意义的图案区域上。

这个模型从来没见过ARC格子，它在ImageNet上学到的「把物体从背景里认出来」的能力，在ARC格子上天然生效了。

![](https://i.qbitai.com/wp-content/uploads/2026/10/672a93326596014e93ea503843f11945.png)



研究人员进一步做了任务级拆解。

他们筛出了15道预训练后显著提升的ARC题目，手动标注后发现这些题集中在两类任务上。

其中6道属于match-and-copy，模型需要识别出匹配的对象、颜色或图案，再把对应的结构复制到输出中；

另外6道属于connected-component reasoning，模型需要识别、填充或重新着色空间上连通的区域。

这两类能力恰好对应自然图像里的视觉先验。

![](https://i.qbitai.com/wp-content/uploads/2026/10/45d9eba1259b49befca4d36e3219199e.png)



在ImageNet上看猫学到的「把猫从草地背景里分出来」，到了ARC里变成了「把这块连通的彩色区域从格子里认出来」。

视觉世界和抽象世界的底层逻辑，在物体分组、图案匹配、区域分割这些操作上，原来共享同一套表征。

## 从猫猫中来，到猫猫中去

NAT-ARC最终在ARC-1上的成绩如下。

表现最好的单模型采用huge尺度，参数量0.6B，pass@2成绩达到63.4±0.7%。

集成时，研究人员把三种不同预训练策略（无预训练、ImageNet MAE预训练、ARC风格格子MAE预训练）分别训出的模型池化在一起做多数投票，拿到70.2±0.6% pass@2，总参数量约2B。

作为参照，专门针对ARC微调的The ARChitects拿到71.6%，用的是8B的语言模型。

视觉路线用四分之一的参数量，打到了专用LLM系统的城下。

![](https://i.qbitai.com/wp-content/uploads/2026/10/26f27f41f017095f29dd6a7c58d69eb9.png)



数字之外，这篇论文最重要的一个发现，就是预训练打通了视觉路线的scaling瓶颈。

没有预训练时，模型越大效果反而越差；加上预训练后，scaling才开始代理正收益。

先看训练曲线。在离线训练阶段，用了ImageNet预训练的模型收敛速度明显更快，在base、large、huge三个尺度上都是如此，最终精度也更高。

![](https://i.qbitai.com/wp-content/uploads/2026/10/d1fbf265045e96f91c1071819faaf085.png)



但最有意思的发现藏在scaling曲线里。

没有预训练时，模型从base到large性能还能涨，但从large到huge反而掉点了。

模型变大，效果变差，这在深度学习里不是常见现象，说明ARC这个任务的数据量实在太少，模型容量增长带来的不是更强的泛化而是过拟合。

而加上ImageNet预训练后，scaling曲线变得健康了，base、large、huge三个尺度一路向上，模型越大效果越好。


论文里最酷的一个实验是一个可视化验证。

研究人员训了一个autoencoder，把ImageNet图像映射到一个60×60、10种颜色的离散格子表示上，相当于把一张猫片「翻译」成了ARC格子。

然后，他们用NAT-ARC对这个格子执行ARC变换，旋转180°、加一圈蓝色边框，再解码回像素。

结果，猫确实被转了，边框也确实加上了。这个从猫猫里训练出的模型，又在任务里回到了猫猫之中。


这个实验把「自然图像和ARC格子共享同一套表征空间」从统计数字变成了可视化证据。

在ARC格子上学会的变换规则，可以直接应用到自然图像的潜在表示上，反过来也一样。

抽象规则和视觉表征之间的连接，是这两个世界本来就有的。

## 作者简介

论文一作Xiaoman Delores Ding，MIT CSAIL成员，来自何恺明组。

她同时也是VARC的一作，这篇NAT-ARC相当于在自己上一篇工作的基础上继续往前推。

其余作者包括胡珂雅（Keya Hu），是何恺明首批女弟子之一，本科毕业于**上海交通大学**。

还有Katelyn Gan和Victor Yin，同样来自MIT，两人都是本科生，且均在CSAIL担任student researcher。

通讯作者何恺明不必多说，他是ResNet和MAE的作者，从这两个工作几乎可以串起近十年视觉AI的主线。

他从进入MIT后持续产出视觉基础工作，这篇论文用的正是他自己四年前提出的MAE作为预训练工具，等于用自己的旧武器打通了一条新路。

VARC已被CVPR 2026接收，NAT-ARC是它的直接后续。

这个团队连续两篇论文坚持纯视觉路线解ARC，在LLM大行其道的赛道上，它们正在用实验数据不断突破视觉路线的天花板。

论文地址：

https://eccv.ecva.net/virtual/2026/poster/5527

*版权所有，未经授权不得以任何形式转载及使用，违者必究。*


![](http://www.qbitai.com/wp-content/themes/liangziwei/imagesnew/head.jpg)

- [谷歌Gemini 4突然发布！RSI加持，GPT和Opus都让让](https://www.qbitai.com/2026/10/499663.html)*2026-10-01*
- [Qwen一号位定了！刘大一恒接棒](https://www.qbitai.com/2026/09/496384.html)*2026-09-23*
- [通用能力不打折，空间具身智能断层领先！ZDTaichu5.0-9B国产开源，跻身全球多模态第一梯队](https://www.qbitai.com/2026/09/490839.html)*2026-09-16*
- [今年外滩最特别Agent：能干活，能陪聊，还会朋友圈拉黑你](https://www.qbitai.com/2026/09/488447.html)*2026-09-13*
