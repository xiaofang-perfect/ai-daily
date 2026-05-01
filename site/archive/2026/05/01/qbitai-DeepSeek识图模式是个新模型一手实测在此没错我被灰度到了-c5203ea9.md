---
title: "DeepSeek识图模式是个新模型？！一手实测在此（没错我被灰度到了）"
source: 量子位
url: https://www.qbitai.com/2026/04/411797.html
date: 2026-05-01
published_at: 2026-04-30T06:52:23+00:00
tag: 论文研究
item_id: c5203ea9ee27ebe9
---
# DeepSeek识图模式是个新模型？！一手实测在此（没错我被灰度到了）

非思考模式快到飞起

鱼羊 发自 凹非寺

量子位 | 公众号 QbitAI


今天，你被DeepSeek识图模式灰度到了吗？

![](https://i.qbitai.com/wp-content/uploads/2026/04/c7675b60f85d4117790cb490cb84d8fb.webp)


大家对DeepSeek的多模态属实期待了太久太久，如今惊喜紧随V4的发布而来，没等DeepSeek官方释出更多信息，民间已经从各个方向开始挖掘“识图”背后的种种蛛丝马迹。

还真有不少发现。

比如，DeepSeek识图模式背后，看上去是一个独立于V4 flash/pro的新模型。

![](https://i.qbitai.com/wp-content/uploads/2026/04/549a6e91d3de902cfb438a2fe181a865.webp)


又比如，DeepSeek在V4技术报告里的“未来展望”，实际上可能都做的差不多了……

![](https://i.qbitai.com/wp-content/uploads/2026/04/d26f3882319a5bb41ff1d7b8ad9da90e.webp)


今天眼睛一睁，俺也喜提灰度，这就来展示一下实测成果。

# 实测DeepSeek识图模式

在识图模式下，可以选择是否开启深度思考。

![](https://i.qbitai.com/wp-content/uploads/2026/04/873bbcea2b30ae2fdefdf45e8796ce01.webp)


**非思考模式下，这个DeepSeek视觉模型的速度非常快**，~~比闪电五连鞭还要快。~~

点击发送键，几乎无需等待，答案就哗啦一下冒了出来。

![](https://i.qbitai.com/wp-content/uploads/2026/04/7e93fa6cc33f1442aa85f647e53fe958.gif)


那么思考和非思考模式下，DeepSeek识图模式的推理能力会有什么样的差别？

# 推理能力

先上一道**空间推理题**：要想使右侧图形在不旋转的情况下拼合成左侧的正方体造型，还需在问号处添加的图形是哪个？

![](https://i.qbitai.com/wp-content/uploads/2026/04/899c17464c539e036432e347b9b16fea.webp)


非思考模式秒给答案，然后……秒错。

![](https://i.qbitai.com/wp-content/uploads/2026/04/86287f359499c7e7e6fb45ab2f604c7b.webp)


开启深度思考后，DeepSeek成功闯关，给出了正确答案D。

![](https://i.qbitai.com/wp-content/uploads/2026/04/89ae45f203f4d4e1c54d5ae82a3a4e17.webp)


但可以看到，它思考这个问题整整用了**4分多钟**。

这个思考过程的冗长程度，我们可以直观地感受一下——

在思考的中段，其实DeepSeek已经找到了正确答案：

![](https://i.qbitai.com/wp-content/uploads/2026/04/a368e25196cc7007492541759d8edc63.webp)


但马上就是一个“等等”，然后……又绕了一大堆。

![](https://i.qbitai.com/wp-content/uploads/2026/04/ba844d7de4d3c7b301a48f981c95762c.gif)


这个问题有人也在DeepSeek研究员陈小康的推文下反馈了。

![](https://i.qbitai.com/wp-content/uploads/2026/04/b5fe36bae6fb088eef08cd167677f9f8.webp)


再试试**图片找不同**：找出两张图片中所有的不同点。

![](https://i.qbitai.com/wp-content/uploads/2026/04/f2a6ac8f4d0eb29f3c2ff739380897aa.jpeg)


非思考模式下，DeepSeek很快找到了7处不同。

![](https://i.qbitai.com/wp-content/uploads/2026/04/cff7bd9a172ef4e140e680b1da348938.webp)


可以很明显地看出，其中幻觉不少，比如第5点托盘里的钥匙不知道是怎么来的，第7点苹果和香蕉之间也没有白色的空盘子。

思考模式这次则只用了16秒的时间，找出了12处不同。

![](https://i.qbitai.com/wp-content/uploads/2026/04/db7c6385c3d004ab9d982c4685db5ec9.webp)


但……不知道是不是图片本身的原因，幻觉更多了。

# 实用功能

推理部分还有进步空间，那么在实用功能方面，DeepSeek的识图模式是否靠谱呢？

试试**OCR**。

把DeepSeek V4技术报告的摘要丢进DeepSeek识图模式，不开深度思考的情况下，它依然是闪电出结果，还贴心地给开源链接给超链了。

![](https://i.qbitai.com/wp-content/uploads/2026/04/cf85ad39677887aa7fb7864313bf3292.webp)


纯文本看上去问题不大，再看看表格DeepSeek能不能hold住。

![](https://i.qbitai.com/wp-content/uploads/2026/04/af3983dd8d6ce5597baf43ee61f02072.webp)


没什么问题，格式上也能用markdown码得整整齐齐。

而更受欢迎的一种新玩法是，**把网页图片发给DeepSeek，它直接能给你复原出HTML来**（非思考模式就能实现）。

![](https://i.qbitai.com/wp-content/uploads/2026/04/3de3cc0013d4f723b11ad08c8d3323d2.webp)


其中的按钮都是可用的，比如给出API文档的链接，它能自动配置好实现跳转。

![](https://i.qbitai.com/wp-content/uploads/2026/04/d0183e7d3c547b171e33da9cc78e8dd2.gif)


DeepSeek还能顺利通过“隐藏图片”测试。

![](https://i.qbitai.com/wp-content/uploads/2026/04/dc8ae36148d5e4884cfa92c26096ea5f.webp)


但在色盲测试中，偶见翻车。

![](https://i.qbitai.com/wp-content/uploads/2026/04/cef1b116f46e554bda092b361be5d2e7.webp)


根据识图模式自己的回答，它的知识和DeepSeek V4 flash/pro一样，截止到2025年5月。

![](https://i.qbitai.com/wp-content/uploads/2026/04/2168f3d230fffe4a560308947428a25b.webp)


而从它的世界知识中，有博主发现了端倪：视觉模型知道Ta，而V4 flash/pro则并不了解Ta。

是不是说，**识图模式中的视觉模型，是独立训练的？**

![](https://i.qbitai.com/wp-content/uploads/2026/04/1bf65b1548ac097873be5a168dcaedfd.webp)


验证了一下，flash不联网的时候确实没有关于这位主包的知识。但识图模式则找到了2026年4月的信息。

![](https://i.qbitai.com/wp-content/uploads/2026/04/8325669ba93fd068275a57ba3bb3e5ea.webp)


![](https://i.qbitai.com/wp-content/uploads/2026/04/1ef79fe581e91da352b5e2a51a2f1678.jpeg)


# 做的比说的更快

目前，DeepSeek的识图模式还在灰度测试当中，陈小康透露灰度范围正在逐步扩大。

![](https://i.qbitai.com/wp-content/uploads/2026/04/7cfe2cdfcff1cc5aa542d0d15b686ce9.webp)


实测下来坦白说，DeepSeek Vision还有不少可以精进之处。

但话说回来，谁又能想到DeepSeek的多模态，来的这么快呢？

当DeepSeek在V4的技术报告中写下，“我们也正在努力将多模态能力整合到我们的模型中”，大家都以为这还只是个优先级没那么高的目标，不少朋友都在惋惜的同时，也认同“资源有限的情况下优先做好纯文本是对的”。

而现在看来，DeepSeek做到的或许比外界想象的更多、更快。

那么论文中提到的“在MoE和稀疏注意力架构之外，将积极探索模型稀疏性的其他新维度”，是不是也……

![](https://i.qbitai.com/wp-content/uploads/2026/04/33c93359991d91f6b3440c25890ae405.gif)


参考链接：

[1]

https://x.com/teortaxesTex/status/2049422327914332307?s=20

[2]

https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf

*版权所有，未经授权不得以任何形式转载及使用，违者必究。*


[DeepSeek不惜代价保住它！V4关键特性被挖出来了](https://www.qbitai.com/2026/04/409896.html)*2026-04-28*[DeepSeek V4终于发布！打破最强闭源垄断，明确携手华为芯片](https://www.qbitai.com/2026/04/406359.html)*2026-04-24*[黄仁勋率先开源量子AI大模型](https://www.qbitai.com/2026/04/401351.html)*2026-04-15*[别养龙虾了，硅谷Agent新潮流是「爱马仕」](https://www.qbitai.com/2026/04/400522.html)*2026-04-13*
