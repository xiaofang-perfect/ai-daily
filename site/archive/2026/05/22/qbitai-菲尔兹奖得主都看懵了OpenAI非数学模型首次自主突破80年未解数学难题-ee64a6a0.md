---
title: "菲尔兹奖得主都看懵了：OpenAI非数学模型首次自主突破80年未解数学难题"
source: 量子位
url: https://www.qbitai.com/2026/05/422032.html
date: 2026-05-22
published_at: 2026-05-21T09:36:23+00:00
tag: 论文研究
item_id: ee64a6a02daeaf19
---
# 菲尔兹奖得主都看懵了：OpenAI非数学模型首次自主突破80年未解数学难题

125页“令人恐惧”的推演

闻乐 发自 凹非寺

量子位 | 公众号 QbitAI


OpenAI又双叒搞数学了。

内部模型搞定了一道**埃尔德什**早年提出的**单位距离经典难题**，已经**80年**无实质进展。

解决这个问题的还不是数学专家模型，而是一个**通用模型**。

![](https://i.qbitai.com/wp-content/uploads/2026/05/7746de93748331d695fb57ad81aec72b.png)

该内部模型在埃尔德什经典问题上摸出了全新解题思路，连**菲尔兹奖得主高尔斯**（Timothy Gowers）都直言，这算是实打实头一回，AI自主啃下这种未解数学难题：

这是AI解决的第一个极其著名的、未解的数学问题的清晰案例，也是第一个由AI（自主）实现的数学突破。


![](https://i.qbitai.com/wp-content/uploads/2026/05/177c6056279d5ac24663c5c21ae9a668.png)

负责这款通用推理模型的**Noam Brown**也放话，要尽快发布！！

![](https://i.qbitai.com/wp-content/uploads/2026/05/118112598c39c7d4c1aa7c0219aca1ac.png)

# 打破人类80年固有认知

先说这个数学问题本身。它简单到你能在餐巾纸上画出来，但难到五代数学家都没搞定。

埃尔德什1946年提出的单位距离问题是说：

**平面上放n个点，最多能有多少对点之间的距离恰好为1？**

听着像小学数学对吧？但你试着摆一下——

三个点可以摆成等边三角形，每对距离都是1；

四个点呢？正方形不行，因为对角线不是1，所以就得你得动脑子了；

再推到n个点，问题就炸了。

![](https://i.qbitai.com/wp-content/uploads/2026/05/f4bc0fc3ec4a1c895325bd61ee498621.png)

过去近80年，数学家们达成了一个核心共识：最优方案大概就是**正方形网格**那样的排列。

用数学语言说，他们相信单位距离对数的增长速度大约是 O(n)，也就是说增长基本上是线性的。

写成公式就是 u(n) ≤ n^(1+o(1))，那个o(1) 趋近于0。

而这次OpenAI的内部通用模型没走几何路线，而是从代数数论绕进来，构造出了一族全新的点排列方式。

最后证明：**u(n) ≥ n^(1+δ)，其中δ>0**。

翻译过来就是增长速度不是线性的，是**超线性的**。

那个大家以为“趋近于0”的小尾巴，其实是正的。

80年的数学共识，被打破了。

![](https://i.qbitai.com/wp-content/uploads/2026/05/0bee72ef70d58fb5448ffb88a691926d.jpeg)

是AI给出的构造虽然证明了δ>0，但具体数值还不是最优。

人类数学家拿到这个构造之后，立刻在AI的基础上做了优化，把下界又往上推了一把。

虽然OpenAI没有发布AI未精简过的完整思路，但其精简后的内容足足有125页！

![](https://i.qbitai.com/wp-content/uploads/2026/05/194ba787eace294bd34b47107bafebdd.png)

网友还发现一个细节，该模型在第39页阐述了关键观点，并将构造过程描述为“令人恐惧的”。

于是不少数学爱好者表示：好想读到完整思路……

![](https://i.qbitai.com/wp-content/uploads/2026/05/3d912bc9f8db1157b4a7835964312f48.png)

而且据OpenAI自己说，这款模型还不是专门练数学的专用AI，就是正经通用大模型，纯靠自己逻辑推演完成突破……天赋拉满了。

# 这次不是狼来了

OpenAI在数学上翻过车，这个绕不开。

去年10月，OpenAI副总裁Kevin Weil发帖说GPT-5解了10个埃尔德什问题。

结果被维护erdosproblems网站的数学家Thomas Bloom当场拆穿：

这是误导，GPT-5只是搜到了Bloom个人不知道的已有论文，不是原创发现。

![](https://i.qbitai.com/wp-content/uploads/2026/05/d9cfa0c91b6140359d211ec1b99b0ee2.png)

DeepMind哈萨比斯也炮轰“令人尴尬”，最后Weil删帖收场。

七个月后，又是Thomas Bloom，面对OpenAI的新数学成果，说了句完全不同的话：

这是人工智能目前在数学领域取得的最亮眼成就。


![](https://i.qbitai.com/wp-content/uploads/2026/05/6c3e3cd151a3ee4edfcabe549b4e53c6.png)

年初First Proof项目里，OpenAI的一个内部数学模型解决了题集中的5道，当时Noam Brown就说那个内部模型即将发布；

![](https://i.qbitai.com/wp-content/uploads/2026/05/354d037dbb673e10f76793acd947c345.jpeg)

现在他又说一个通用模型会尽快发布……

我只想知道，OpenAI到底还藏着多少好东西（doge）。

参考链接：

[1]https://x.com/polynoamial/status/2057178198228586824?s=20

[2]https://x.com/voooooogel/status/2057198687307362642?s=20

*版权所有，未经授权不得以任何形式转载及使用，违者必究。*


[腾讯混元开源全新翻译模型Hy-MT2 ，上线小程序「腾讯Hy翻译」](https://www.qbitai.com/2026/05/422068.html)*2026-05-21*[虾马之后又火一个！OpenHuman用20分钟了解你的一切，存成卡帕西式知识库](https://www.qbitai.com/2026/05/418571.html)*2026-05-16*[Need is all you need：AI接手Coding后，程序员最值钱的能力只剩这一项?](https://www.qbitai.com/2026/05/418035.html)*2026-05-15*[别让模型烧Token了！GitHub 20k星神作：把全网变成命令行](https://www.qbitai.com/2026/05/418518.html)*2026-05-16*
