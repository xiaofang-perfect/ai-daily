---
title: "挑战扩散自回归统治！字节提出视觉生成第三种路线，让模型像人类一样边画边改"
source: 量子位
url: https://www.qbitai.com/2026/05/416978.html
date: 2026-05-14
published_at: 2026-05-13T14:04:35+00:00
tag: 论文研究
item_id: fd5f660a2f0a659f
---
# 挑战扩散自回归统治！字节提出视觉生成第三种路线，让模型像人类一样边画边改

相同参数量超越扩散自回归

鹭羽 发自 凹非寺

量子位 | 公众号 QbitAI


ber！这个五一假期，我也是真够忙的：

自拍、电影、追剧、街头采访、听音乐会，还抽空回老家结了次婚……

![](https://i.qbitai.com/wp-content/uploads/2026/05/49ecf13bbcc8a5295e0acacf243304ce.png)


视频链接：https://mp.weixin.qq.com/s/TAYMBnKLbiG_gtkJpC8Ekw

![](https://i.qbitai.com/wp-content/uploads/2026/05/08825d20de17c728f2c5686bd8c7fdcd.png)


视频链接：https://mp.weixin.qq.com/s/TAYMBnKLbiG_gtkJpC8Ekw

![](https://i.qbitai.com/wp-content/uploads/2026/05/8efbe4860ca15ef719f567bf2a978a0f.png)


视频链接：https://mp.weixin.qq.com/s/TAYMBnKLbiG_gtkJpC8Ekw

（咳咳）不卖关子了，其实以上这些，通通都是AI生成。

但u1s1，就这逼真的眼神和动作，也太对味了！

它们都出自**字节商业化技术团队**研发的新一代视觉生成模型，更妙的是——

它的底层架构，不是主流的扩散模型，也并非近来大火的自回归模型，而是**全新的第三条路**。

![](https://i.qbitai.com/wp-content/uploads/2026/05/9f1f98892c510727510c2e58e33d1351.webp)



这篇研究论文，提出了另一种AI视觉生成构想：

让AI像人类一样画画，不仅可以边画边改，还能复杂多画、简单少画。也就是**生成精炼网络GRN**（Generative Refinement Networks）。

简单来说，如果把AI视觉生成比作在白纸上作画，那么现有的扩散和自回归模型各有各的优缺点。

先说扩散模型，作为目前最常用的视觉生成架构，还是有两把刷子的，其所生成的视频几乎能够以假乱真。

但实则它的绘画过程还像个笨拙的学生，无论是画简单的一颗苹果，还是复杂的巴洛克壁画，都必须老老实实一笔一笔画，所以即使是复杂度天差地别的画作，也要花费相同的时间步数。

自回归模型这边，虽然天生具备画面复杂度感知，但由于需要先将颜色离散化，画作始终缺乏高频细节。

它还粗心大意没有橡皮，前面一笔画错了，不仅不改，还会“自由发挥”越画越离谱。

GRN则从根本上解决了这些问题，知错就改，可以在画的过程中就不断修改细化，直到满意为止。

![](https://i.qbitai.com/wp-content/uploads/2026/05/0c1046f98aa55d890c8033ccf505e155.webp)



比如下面这些风格多样的头像，都是生成精炼网络所画。

![](https://i.qbitai.com/wp-content/uploads/2026/05/2a741a4f82b05e86195c2c335bc66cd3.webp)



再比如这些，all by GRN。

![](https://i.qbitai.com/wp-content/uploads/2026/05/fa0fb1dc0f73b79c70e29c6890c0e6b8.webp)



类别生图、文生图、文生视频、图生视频，GRN样样手拿把掐。

毕竟懂的都懂，**“允许犯错、及时纠正”**，这套一以贯之的思路真的很字节范儿～（doge）

## 实测架构性能

说一千道一万，咱再来仔细实测看看。

目前GRN T2I模型直接在HuggingFace就能体验（

https://huggingface.co/spaces/hanjian/GRN）。

可以自行调整参数，比如提示词相关性、创意发散程度等。

![](https://i.qbitai.com/wp-content/uploads/2026/05/b8e42d7b1fde19083f16741fd1c3b7d1.webp)



先来生成一张80年代家庭照片。

一张80年代生日派对上拍摄的全家福。一个小男孩吹灭奶油蛋糕上的蜡烛，家人围绕在他身边鼓掌。


![](https://i.qbitai.com/wp-content/uploads/2026/05/2790714e14256172f6574e32f7952014.webp)



很有CCD老照片那味儿了～

再上难度，让GRN尝试生成一张漫画：

Two men dressed in dark suits, red ties, and black hats. They are both wearing sunglasses and holding revolvers, pointing them directly at the viewer. The men have stern expressions on their faces. Their attire and demeanor suggest a sense of authority and menace…


两名男子身着深色西装、系红色领带、头戴黑色礼帽。二人均佩戴墨镜，手持左轮手枪，枪口直指观者。两人神情冷峻，着装与气场透着威严感与威慑感…

![](https://i.qbitai.com/wp-content/uploads/2026/05/9bc09a66910e55ef361b1b533d3cbf60.webp)



一眼望去，配色大胆、风格鲜明，角色与构图也搭配和谐。

文生视频这边，作者**开源**了2B模型，同时提供了一个Discord网站Demo，大家登录Discord之后，点击下面这个链接就可以体验：

http://opensource.bytedance.com/discord/invite。

在左侧导航栏，可以找到GRN-T2V 2B模型，然后在聊天框输入/generate_video [提示词]即可。

![](https://i.qbitai.com/wp-content/uploads/2026/05/7052547a660339e36c6b7ae92f9b35c1.webp)



先来一个单人简单场景的测试：

A man in an orange shirt and glasses stands before a red brick wall, holding and presenting a dark gray cylindrical object.


一名身穿橙色上衣、戴着眼镜的男子站在红砖墙前，手持并展示一个深灰色的圆柱形物体。

![](https://i.qbitai.com/wp-content/uploads/2026/05/2527c667ac7903f95980abc8f70dd42c.png)


视频链接：https://mp.weixin.qq.com/s/TAYMBnKLbiG_gtkJpC8Ekw

人物皮肤、面部细节和动作流畅度都不像是只有2B参数的模型～

再看看一个多人舞蹈、镜头快速推进的例子，也没有出现画面畸形的情况。

A K-pop group performs on stage with vibrant lighting and dynamic choreography, singing a song about preferring night meetings, as shown in a live broadcast.


一场直播画面中，一支韩国流行偶像团体在绚丽的舞台灯光下登台表演，舞步灵动富有张力，演唱着一首偏爱夜间相约主题的歌曲。

![](https://i.qbitai.com/wp-content/uploads/2026/05/a274ed8d2841b416702f8c82812005fe.png)


视频链接：https://mp.weixin.qq.com/s/TAYMBnKLbiG_gtkJpC8Ekw

另外，各种复杂的人物动作和镜头调度，也都能一步到位，还原得相当丝滑。

![](https://i.qbitai.com/wp-content/uploads/2026/05/5d026603748d96067e5f3c5f5feaaf9d.png)


视频链接：https://mp.weixin.qq.com/s/TAYMBnKLbiG_gtkJpC8Ekw

妥妥成片级表现，直接给到夯！

这就引出了新的问题——

为什么团队要执意跳出舒适区，探索一套全新的生成范式呢？

## AI视觉生成的第三条路

这就源自团队对现有主流技术路线的洞察——

**扩散模型：虽然生成质量高，但不够智能。它对所有样本，无论复杂与否，都分配相同的迭代步数，缺乏自适应能力。****自回归模型：通过似然估计，天然具有复杂度感知能力。但一方面，受限于离散token化，存在严重的信息损失。另一方面，存在误差累计和误差传播的问题，早期错误无法修正，于是越错越离谱。**

而GRN则是对二者的扬长补短，同时兼顾全局精调和内容复杂度感知。

其核心架构包括三个部分：

**1、层次二叉树量化**（HBQ）

首先针对自回归模型的离散损失，HBQ采用近乎无损的离散编码，能够避免在压缩过程中丢失信息，同时实现图像与视频的统一建模。

![](https://i.qbitai.com/wp-content/uploads/2026/05/23086e54d58e1c0e43a2c1d42d9d93f6.webp)



具体来说，它将VAE编码后的连续特征映射到[-1, +1]区间，然后通过二叉树结构进行多轮二进制量化。

这样重建误差就会随着量化轮数增加逐渐被分配到更精细的量化区间，量化误差随着轮数指数级衰减，理论上可以实现完全无损的量化。

最终将获得M个二进制标签，分别代表从粗到细的信息层次。

其中，GRN包含两种预测目标，GRN_ind是将通道维度的M位二进制合并成一个整数标签进行预测，更适合简单量化轮数少的情况；GRN_bit则是直接逐位预测二进制值，更适合量化轮次高、模型大、任务复杂的情况，比如视频生成。

另外，二者均采用多token并行预测，以提升生成速度。

**2、全局精炼网络**（GRN）

至于解决误差积累问题，GRN引入了全局精调过程，模拟人类绘画过程，从随机token图开始，逐轮开始修改迭代。

![](https://i.qbitai.com/wp-content/uploads/2026/05/757fbdb88c6b0143fc9cb849dbe2af16.webp)



首先每一步的生成状态都由两部分组成：

- 当前已经生成的内容，也就是已画好的部分([F] token)；
- 随机token，模拟空白画布 ([R] token])；

然后Transformer就会基于当前状态，预测一个更优的token图。

这个过程中，GRN需要自己从当前输入判断哪些是画好的[F] token，哪些是随机的[R] token，然后对所有token都输出一个refine后的结果。

当然，如果GRN判断是画好的[F] token，倾向于复制输出。对于[R] token，需要根据全局上下文的token推断应该画上什么。

![](https://i.qbitai.com/wp-content/uploads/2026/05/截屏2026-05-13-21.38.58.png)


另外，就算某些token被多次选中，随着模型看到的信息越来越多，这些token也不会一成不变，而是会被模型更优的预测结果代替，研究人员把这种机制叫做**“token精调”**。

通过这个全局refine的更新机制，确定的token不断增多，不确定的token反复改写，就像一个画家一样，真正做到了边画边改，生成效果也越来越好，彻底解决了自回归模型错误累计、错误传播的老大难问题！

**3、复杂度感知采样**

为了避免扩散模型一刀切的计算分配方式，GRN采用熵来衡量画面复杂度。

计算每一步预测的平均熵，熵低意味着样本简单，可以分配较少的推理步数，熵高则意味着样本复杂，需要分配更多的精炼步数。

应用复杂度感知采样后，在对步数最敏感、参数量最小的130M模型上，推理步数能够从总共50步变成了20~40步，平均24步，而gFID仅仅从3.56略微上升到3.79（gFID数值越小越好），真正做到了简单少画、复杂多画！

并且，简单的样本20步就能搞定，复杂的样本GRN也只分配了40步。

基于此，实验结果显示，GRN在多项基准测试中均刷新了**SOTA**记录。

首先在ImageNet 256×256的图像重建上，HBQ达到了0.56 rFID，远超SD-VAE (0.87)、RAE (0.62)、VAR（0.85)、Open-MAGVIT2（1.17)。

在视频重建时，8轮HBQ效果与连续VAE基线标准**相当**，说明HBQ无需增加隐层通道数，就能在更高的压缩率下逼近连续编码质量。

而将隐层通道从16提升至64，PSNR就会从30.40跃升至33.97，性能媲美当前最优的Wan 2.1，但比特数减少了4倍。

![](https://i.qbitai.com/wp-content/uploads/2026/05/679c9fe30145ab27d0cb07c88b51b1de.webp)



在类别-图像生成（C2I）任务中，GRN‑G（2B）的FID值为1.81，IS值为299.0，超越了DiT‑XL/2、SiT‑XL/2、VAR‑d30、LlamaGen‑XXL、JiT-G主流生成模型。

另外，相比于MaskGIT（227M），GRN‑B（130M）参数量仅为前者的一半，但性能实现反超，FID从6.18降至3.56。

这也就意味着，GRN的**全局精调**不仅彻底解决了AR误差积累问题，生成质量同时还超越主流扩散模型。

![](https://i.qbitai.com/wp-content/uploads/2026/05/cbe0c3e21b582c357c16c5ffacfa87e6.webp)



在文生图（T2I）任务中，GRN_bit 2B在GenEval上得分0.76，超过同为2B参数的SD3 Medium、Infinity，因为2B的参数量限制，落后于其他6B～20B等大模型，不过研究人员表示，GRN这种类似语言模型的离散token建模，有很好的scaling特性，他们会在未来推出更大的模型。

![](https://i.qbitai.com/wp-content/uploads/2026/05/a686639ce5c811360679a917d24d974b.webp)



在文生视频（T2V）任务中，2B参数的GRN最高可支持**480p**、**2~10秒**高保真视频生成，在VBench测试中，超越5B的CogVideoX、14B的Wan 2.1等模型，以及**所有同规模的AR和扩散模型**。

![](https://i.qbitai.com/wp-content/uploads/2026/05/d7cd3aaa2e3088deae66d8ab95f5cc90.webp)



另外，消融实验也证明了全局精调、复杂度感知模块在GRN中的关键作用。

总的来说，在同等参数量下，GRN已经实现了比**扩散模型与传统自回归模型更聪明的生成**。

它证明，在扩散和自回归这两条既定路径之外，视觉生成还有新的可能。GRN同时解决了量化损失、误差累计、复杂度感知生成的三个问题，在AR和Diffusion中间架起了一座桥梁。

如果再脑洞大开一下，现在的**dLLM**或许也可以借鉴GRN的思路。

dLLM也是一次性生成，一旦早期token出错，后面就只能将错就错，如果像GRN一样，引入全局精调，也许模型在生成文本后，还有机会推翻之前写的内容。

这也不失为一个好的破局之道。

此外，GRN证明了纯血离散token是能够做好图像和视频生成的。从长远来看，能够更好地统一图像、视频、文本token，显著提升模型的多模态理解与生成能力。

相比自回归模型，GRN重建上限更高，对抗误差累计能力更强；相比扩散模型，GRN能更聪明地分配计算步数。GRN用优雅的设计解决了一直以来困扰自回归和扩散模型的难题。

论文链接：

https://arxiv.org/abs/2604.13030

代码链接：

https://github.com/MGenAI/GRN

HuggingFace链接：

https://huggingface.co/spaces/hanjian/GRN

项目主页：

https://mgenai.github.io/GRN/

*版权所有，未经授权不得以任何形式转载及使用，违者必究。*


[原来Ilya还有70亿美元OpenAI股权](https://www.qbitai.com/2026/05/416597.html)*2026-05-12*[智谱公布“降智”的秘密：Scaling不可避免的痛](https://www.qbitai.com/2026/05/412585.html)*2026-05-01*[陶哲轩在线安利Claude Code：审稿意见全给它，15分钟欧了](https://www.qbitai.com/2026/05/413265.html)*2026-05-06*[0博士组合拿下ICLR时间检验奖！两个GPT天才本科生+二本逆袭LeCun弟子，十年论文终封神](https://www.qbitai.com/2026/04/406892.html)*2026-04-25*
