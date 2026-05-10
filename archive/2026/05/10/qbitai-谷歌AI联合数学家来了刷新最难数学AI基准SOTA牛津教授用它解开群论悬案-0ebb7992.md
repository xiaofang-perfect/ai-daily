---
title: "谷歌「AI联合数学家」来了！刷新最难数学AI基准SOTA，牛津教授用它解开群论悬案"
source: 量子位
url: https://www.qbitai.com/2026/05/414788.html
date: 2026-05-10
published_at: 2026-05-09T07:12:48+00:00
tag: 论文研究
item_id: 0ebb799260d3e79c
---
# 谷歌「AI联合数学家」来了！刷新最难数学AI基准SOTA，牛津教授用它解开群论悬案

谷歌AI for Math迈出最新一步

### 听雨 发自 凹非寺

量子位 | 公众号 QbitAI

数学界「悬案簿」Kourovka Notebook，AI取得新突破。

群论领域几十年无解的**第21.10号**问题，被牛津数学家**Marc Lackenby**用谷歌一个新系统破解了。

过程也很有意思：AI第一次给出的证明是错的，被系统里的审查Agent揪出了漏洞。

Lackenby看到之后突然意识到：「等一下，我知道该如何填补这个漏洞」。

于是，通过和AI的反复配合，Lackenby最终成功解答出了这道数学难题。

这套人机协作的系统，就是**谷歌DeepMind**最新发布的**「AI Co-Mathematician」（AI联合数学家）**。

![](https://pic-out.zhimg.com/v2-55af80d7c1a5437f303ef90e912d9688~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1778310629-0-0-4a04825b58354e9515fb03208178bc73&bizSceneCode=article_draft&expiration=1778310629&incremental=false&mid=36f69162230003d316d0b8a6d8da20ba&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)


它在最难的数学AI基准**FrontierMath Tier 4**上拿了**48%**，刷新SOTA。

甚至超过了GPT-5.5 Pro*（39.6%）*和GPT-5.4 Pro*（37.5%）*。

![](https://pic-out.zhimg.com/v2-1c24f79a96a54a2e1b86bc2509031f09~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1778310629-0-0-ed8aeead21db64b7973c0866b2377487&bizSceneCode=article_draft&expiration=1778310629&incremental=false&mid=36f69162230003d316d0b8a6d8da20ba&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)


最近几个月，不少数学难题，诸如接连几个Erdős问题都是用GPT解决的。

现在，谷歌也回归了。

![](https://i.qbitai.com/wp-content/uploads/2026/05/cb572b8270219907410550637bbb6413.png)


**「AI联合数学家」，是什么？**

「AI联合数学家」是一个**异步、有状态的工作空间**，而非一问一答的模型。

顶层有一个「项目协调者」Agent负责统筹，拆解任务，调度多条研究线并行推进。

![](https://pic-out.zhimg.com/v2-c954b3f14f60230db80da6fbf2d6d132~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1778310629-0-0-aaa6bc9179fe77d37b5beccbb75b32bb&bizSceneCode=article_draft&expiration=1778310629&incremental=false&mid=36f69162230003d316d0b8a6d8da20ba&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)


数学家上传一篇论文、提出一个研究方向后，协调者不会立刻输出答案，而是先和用户对话，像真正的合作者一样帮对方精炼问题。

![](https://pic-out.zhimg.com/v2-aee0c92d6b5580fcbbd35415b6386d09~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1778310629-0-0-911f92c751dc8ef9a7c2d58802d9a023&bizSceneCode=article_draft&expiration=1778310629&incremental=false&mid=36f69162230003d316d0b8a6d8da20ba&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)


之后它将任务分发到多条并行工作流：一条做文献检索，一条搭计算框架，一条尝试证明策略。

每条工作流都有自己的协调Agent，异步运行，互不阻塞。用户随时能介入、引导、接管。

![](https://pic-out.zhimg.com/v2-7d45bf35689c1c618187f297c19a9d85~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1778310629-0-0-1f1ead5c7fcc4afb13163b6107a84ba6&bizSceneCode=article_draft&expiration=1778310629&incremental=false&mid=36f69162230003d316d0b8a6d8da20ba&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)


如果Agent卡住了，它也会主动在聊天窗口里求助，而不是沉默重启。

比较特别的一点在于：**它对失败的态度**。

系统会持久化追踪所有失败的假说，不会丢弃，而是当作第一等的研究产出保存下来。

![](https://pic-out.zhimg.com/v2-ea5b514d89279d16d6017fe00cf8c52b~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1778310629-0-0-11adadf243267e12d2a0f7a05d993663&bizSceneCode=article_draft&expiration=1778310629&incremental=false&mid=36f69162230003d316d0b8a6d8da20ba&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)


论文中提到，在数学研究里，**知道什么行不通往往和知道什么行得通同等重要**。

「AI联合数学家」会持久化追踪每一条死胡同、每一个被否定的假设、每一次审稿Agent发现的漏洞。这些「负空间」不会被丢弃，而是成为后续探索的上下文。

它的产出物也不是一段聊天记录或一篇未经验证的草稿，而是带margin注释和来源溯源的LaTeX文档——完全契合数学家社群的工作习惯。

「AI联合数学家」有什么意义？论文里有一段很精妙的比喻：

软件工程领域已经有了Claude Code、Cursor这类AI编码环境，它们提供了持续迭代、版本控制、测试验证的完整工作流。


但数学家此前一直缺少一个等价的编排层。

「AI联合数学家」就是试图填补这个空白。

它的定位，与DeepMind上一代系统**AlphaEvolve**完全不同。

AlphaEvolve更像一个自主搜索引擎：你把问题扔进去，它进化出一个更好的算法，人基本不在循环里。

而「AI联合数学家」要求数学家始终在回路中，系统在最适合的时机向人类提问，而不是替人类做完整件事。

**刷新最难数学AI基准SOTA**

在benchmark上，「AI联合数学家」也拿下了出彩的成绩：

刷新了最难的数学AI基准**FrontierMath Tier 4**的SOTA，拿了**48%**的准确率。

![](https://pic-out.zhimg.com/v2-88694d4ef6cb1c0c64e9d94640d7631d~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1778310629-0-0-29d057ae5e02941ac5a85c5244dbda8c&bizSceneCode=article_draft&expiration=1778310629&incremental=false&mid=36f69162230003d316d0b8a6d8da20ba&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)


FrontierMath是**Epoch AI**开发的数学benchmark，包含350道原创高难度题，覆盖现代数学各大分支。

其中Tier 4仅50题，被Epoch AI描述为「其中一些问题可能数十年内AI都无法攻克」，人类专家解决一道通常需要数天。

「AI联合数学家」在48道非公开题中答对了23道，**准确率48%**。

![](https://pic-out.zhimg.com/v2-10448509bfa6fc18dc4528578b9674a3~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1778310629-0-0-de23ee3b83e2341dea5e2630478f7e1e&bizSceneCode=article_draft&expiration=1778310629&incremental=false&mid=36f69162230003d316d0b8a6d8da20ba&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)


GPT-5.5 Pro此前在Tier 4拿到39.6%，GPT-5.4 Pro是37.5%，Claude Opus 4.6/4.7则双双落在22.9%。

相比之下，「AI联合数学家」把最高分推了近10个百分点。

![](https://pic-out.zhimg.com/v2-c0f4d56130818e0a139da1d19fdac325~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1778310629-0-0-5a38b9e1d1c89c214b7d81d57be6a317&bizSceneCode=article_draft&expiration=1778310629&incremental=false&mid=36f69162230003d316d0b8a6d8da20ba&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)


值得注意的是，它的底层基座模型Gemini 3.1 Pro，单独做这个测试只拿到了19%。

**从19%到48%**，这29个百分点的跳跃**完全来自系统层面的编排**——并行调查分支、强制审查循环、文献检索工具、持久化代码执行基础设施。

而且其中有3道题是此前所有系统都没答对过的新题。

![](https://pic-out.zhimg.com/v2-818c8dd376ec4134d1b78f756478ab56~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1778310629-0-0-24fd53ee402b0be60c12c632d2161f0b&bizSceneCode=article_draft&expiration=1778310629&incremental=false&mid=36f69162230003d316d0b8a6d8da20ba&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)


**△**内部100题研究级数学基准测试中的准确率得分

基准之外，论文中还提到，有三位数学家已经用它来解决真实问题：

牛津大学数学家**Marc Lackenby**解决了Kourovka Notebook第21.10号问题（群论）。

审稿Agent先发现了AI初稿里的一个漏洞，Lackenby意识到自己知道怎么填补这个缺口，最后论文诞生。

数学家**Semon Rezchikov**在哈密顿系统中，向系统抛出一个技术性子问题，收到了一个关键引理。

他的评价是「其他AI系统在同一个prompt上全部失败」，且从美学上看这是他用过所有模型里证明风格最好的。

还有**Gergely Bérczi**，获得了关于Stirling系数对称幂表示的猜想证明。

此外，论文也坦承了两个失败模式。

第一种叫「讨好审稿人偏差」：Agent会不断改写有缺陷的论证，直到AI审稿人不再能发现错误——但漏洞其实还在。

第二种是「死亡螺旋」：当迭代评审过程未能达成共识时，Agent们会陷入无限审稿循环，推理逐渐退化为幻觉。

另外还有一个结构性问题：当AI能在几分钟内生成一篇20页的证明草稿，人类同行评审仍需要数天，这对于依赖志愿者的学术评审体系会形成系统性压力。

而且AI虽然很擅长进行逻辑核验，发现代数错误或找出缺失的引用文献，但它们依然缺乏判断一篇论文的优雅性、深度或真正数学价值所需的整体直觉。

如果过度依赖AI评审，可能会让人类定性判断被边缘化。

当然，在48%这个成绩上，论文中也坦诚披露了评估差异。

48%的得分是在特殊条件下取得的——每题给了48小时、没有token限制、使用团队自己的基础设施。这与Epoch AI标准评估框架不完全可比。

**团队背景**

「AI联合数学家」背后共有18位作者，有几个名字值得单独说说。

第一作者兼通讯作者**Daniel Zheng**，Google DeepMind研究工程师，研究方向是编程语言与机器学习的交叉。

![](https://pic-out.zhimg.com/v2-d260938706eb735f3a9bf75f39608490~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1778310629-0-0-6d94738a92eefda86175c6def16a7881&bizSceneCode=article_draft&expiration=1778310629&incremental=false&mid=36f69162230003d316d0b8a6d8da20ba&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)


2024年AlphaProof拿到IMO银牌那个项目里，他和Alex Davies共同主导了非正式系统*（包括最终答案判定模块）*的开发。

**Alex Davies**，同样是从AlphaProof到AlphaEvolve再到AI联合数学家的连续参与者，是这条技术路线最重要的连接者之一。

![](https://pic-out.zhimg.com/v2-8f16b37b44039069ad36f15b88653165~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1778310629-0-0-1d5e5d39bf13ee15d0cefc6063fa37a3&bizSceneCode=article_draft&expiration=1778310629&incremental=false&mid=36f69162230003d316d0b8a6d8da20ba&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)


通讯作者**Pushmeet Kohli**，Google DeepMind科学副总裁兼Google Cloud首席科学家，主导了AlphaFold（诺奖级成果）、AlphaProof、AlphaEvolve等一系列系统。

![](https://pic-out.zhimg.com/v2-5ed8462819cb1cbe3987f43f16ec50da~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1778310629-0-0-85caf40c9f777e4fd9b6071759498dea&bizSceneCode=article_draft&expiration=1778310629&incremental=false&mid=36f69162230003d316d0b8a6d8da20ba&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)


这篇论文是他带的团队在AI for Math路线上的最新一步。

另一位通讯作者**Daniel M. Roy**，多伦多大学统计系教授，研究横跨机器学习、数理统计和理论计算机科学。

![](https://pic-out.zhimg.com/v2-697b5b1724fb943c999da0f0d81c5899~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1778310629-0-0-0a6a33b92aef9f33065f823f6ad04e2d&bizSceneCode=article_draft&expiration=1778310629&incremental=false&mid=36f69162230003d316d0b8a6d8da20ba&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)


2025年底从加拿大Vector Institute研究主任卸任，2026年1月以访问研究员身份加入DeepMind伦敦。三个学位均来自MIT。

**Fernanda Viégas**和**Martin Wattenberg**则是PAIR*（People+AI Research）*团队的共同创始人，同时也是哈佛计算机科学教授，专注AI可解释性与人机交互。

![](https://pic-out.zhimg.com/v2-e6240bcea689391eec5811175abca495~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1778310629-0-0-ff49153e2107b90f53d595db696bc48d&bizSceneCode=article_draft&expiration=1778310629&incremental=false&mid=36f69162230003d316d0b8a6d8da20ba&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)

![](https://pic-out.zhimg.com/v2-f3f249b5d61a8f3d465e45eda03cabfd~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1778310629-0-0-c042a993f3cdd3e1cb405477ce79c2b9&bizSceneCode=article_draft&expiration=1778310629&incremental=false&mid=36f69162230003d316d0b8a6d8da20ba&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)


他们负责AI联合数学家的用户交互与界面层——这也解释了为什么这个系统在「如何让数学家愿意用它」上花了相当多的心思。

值得注意的是，数学家**Marc Lackenby**并不是临时找来测试的「外部数学家」。

![](https://pic-out.zhimg.com/v2-136f82e6e6a63d9669b24e13bd5c1f9c~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1778310629-0-0-3df79f9da60028fe3e818ed8269f3e74&bizSceneCode=article_draft&expiration=1778310629&incremental=false&mid=36f69162230003d316d0b8a6d8da20ba&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)


在其牛津主页的论文列表里，可以追溯到2021年，Lackenby就已经与Zheng、Davies等人合作发表过Nature论文。他是DeepMind数学AI团队的长期合作者。

![](https://pic-out.zhimg.com/v2-d09abf7946d9df14bc259daf14fbed7c~resize:1440:q75.png?animatedImageAutoPlay=false&animatedImagePlayCount=1&auth_key=1778310629-0-0-360cf0ff7d8dd80b1bf71c7c085d71d4&bizSceneCode=article_draft&expiration=1778310629&incremental=false&mid=36f69162230003d316d0b8a6d8da20ba&overTime=60&precoder=false&protocol=v2&retryCount=3&sampling=false&sceneCode=editor_copy_outbound&source=bfcaadb1)


**One More Thing**

放在更大的背景下，这是谷歌在**AI for Math**方向上已经走了几年的一条路线。

2024年，**AlphaProof**用强化学习做形式化数学推理，在IMO拿到银牌水准。

2025年，**Gemini Deep Think**在当年IMO达到金牌水准，六道题答对五道。

**AlphaEvolve**则是另一条线，自主发现新算法，在50多个开放数学问题上改进了20%的已知最优解。

「AI联合数学家」和这几个系统定位不同，不是更强的问题求解器，更倾向于面向研究者日常工作流的协作工具。

AlphaEvolve适合「给我一个更好的算法」，「AI联合数学家」则适合「陪我研究这个方向几个星期」。

目前「AI联合数学家」还在限量发布阶段，Pushmeet Kohli的表述是，目标是未来开发产品向更广泛的用户开放这个范式。

它还不是所有数学家都能用到的工具，但它证明了一件事：

**AI和数学家之间的协作，可以比「问答」复杂得多，也有效得多。**

论文地址：

https://arxiv.org/abs/2605.06651

参考链接：

[1]https://x.com/pushmeet/status/2052812585804685322

[2]https://x.com/kimmonismus/status/2052849472586264997

*版权所有，未经授权不得以任何形式转载及使用，违者必究。*


[GPT-5级推理能力塞进语音模型，OpenAI把同传翻译成本砍穿地板价](https://www.qbitai.com/2026/05/414194.html)*2026-05-08*[特斯拉百万年薪招数据标注员，朝九晚五，无需AI经验](https://www.qbitai.com/2026/05/414156.html)*2026-05-08*[太抓马了！马斯克OpenAI开庭，硅谷巨富互揭老底像极了村口吵架](https://www.qbitai.com/2026/05/412447.html)*2026-05-01*[太抓马了！马斯克OpenAI开庭，硅谷巨富互揭老底像极了村口吵架](https://www.qbitai.com/2026/05/412080.html)*2026-05-03*
