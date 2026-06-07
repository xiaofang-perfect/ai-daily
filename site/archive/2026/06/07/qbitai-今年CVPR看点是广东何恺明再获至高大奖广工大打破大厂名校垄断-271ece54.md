---
title: "今年CVPR看点是广东：何恺明再获至高大奖，广工大打破大厂名校垄断"
source: 量子位
url: https://www.qbitai.com/2026/06/431186.html
date: 2026-06-07
published_at: 2026-06-06T07:00:06+00:00
tag: 行业动态
item_id: 271ece54ad5747f4
---
# 今年CVPR看点是广东：何恺明再获至高大奖，广工大打破大厂名校垄断

广东上大分！

### 听雨 发自 凹非寺

量子位 | 公众号 QbitAI

刚刚，CVPR 2026在丹佛颁出了今年的全部重磅奖项！

先给各位来个要点速览：

**最佳论文**：**D4RT**，一个能从单段视频里又快又准地重建动态4D场景的前馈模型，来自**Google DeepMind**（联合UCL、牛津）。这也意味着CVPR最佳论文连续两年颁向了几何重建（去年是VGGT）。**最佳论文荣誉提名（2篇）**：Meta的单图3D重建基座模型**SAM 3D**，以及英伟达的通用游戏智能体大模型**NitroGen**。**最佳学生论文**：清华×微软的**TRELLIS.2**——一个全华人阵容做出来的4B参数3D生成模型。**最佳学生论文提名**：**ChordEdit**，一支来自广工大、深大、北大等的**纯国内高校团队**，一作还是本科生。**时间检验奖（Longuet-Higgins Prize）**：双双颁给2016年的两位「祖师爷」——**ResNet和YOLO**。**PAMI人物奖**：年轻学者奖给了CMU的Deepak Pathak和MIT的Vincent Sitzmann；Thomas Huang纪念奖给了康奈尔的Noah Snavely。

今年论文奖的角逐相当惨烈：74篇入围、15篇杀进决赛圈，最终5篇拿到奖项。

规模上也是大年——CVPR 2026收到16092篇投稿、录用4071篇。论文数量再创新高，比去年增长23.71%。

![](https://i.qbitai.com/wp-content/uploads/2026/06/3114ef2405991604803ef408fd418068.webp)

**△**图片来自CVPR2026官方X账号

![](https://i.qbitai.com/wp-content/uploads/2026/06/9f28167baec6500d4d5445c8d0f6a4f6.webp)

**△**图片来自CVPR2026官方X账号

作者、审稿人、领域主席数量也全部刷新历史纪录。

![](https://i.qbitai.com/wp-content/uploads/2026/06/5d7cb8aeba40fd1d41566bc8b2d3c857.webp)

**△**图片来自CVPR2026官方X账号

值得关注但也不意外的是：**这届的华人含量，也几乎拉满了**。

从最佳论文一作，到最佳学生论文的整支队伍，再到时间检验奖里的ResNet四人组，每一格荣誉里都站着华人面孔。

不过这种华人霸榜的局面，过去十年也几乎是主旋律见怪不怪了，AI研究离不开华人，就像……

但是！今年要说最令人耳目一新的，莫过于一众大厂名校里，大奖名单里有一个特殊存在——

拿下最佳学生论文提名的**ChordEdit**，出自**广东工业大学、惠州学院、深圳大学、北京大学**之手。一作以及团队里其他几位作者，都还是本科生。

纯学术团队，本科生阵容，一作还是没有大厂和名校资源的广东工业大学。

了不起啊了不起。

当然，CVPR赢麻了的何恺明大神，也是广东满分高考状元。

这届CVPR，美国丹佛举办，但**粤是广东圆了**。

**最佳论文D4RT：把动态4D重建做成「随用随查」**

今年CVPR的最佳论文是**D4RT**（《Effciently Reconstructing Dynamic Scenes One D4RT at a Time》）。

![](https://i.qbitai.com/wp-content/uploads/2026/06/476e71ae9caf59b8ad7bcf13a6ec8d99.webp)

**△**图片来自CVPR2026官方X账号

从一段普通视频里，重建出场景随时间变化的几何与运动——也就是所谓的**4D重建**（3D空间+时间），一直是计算机视觉里最难啃的骨头之一。

过去的方法要么把任务拆成一堆模块分头处理（又慢又复杂），要么干脆搞不定动态区域的点对应关系，常常是几个毛病一起犯。

D4RT则换了个思路：**把「逐帧把所有东西都解码一遍」的笨办法，改成「你问哪儿、我答哪儿」的按需查询**。

![](https://i.qbitai.com/wp-content/uploads/2026/06/8e68178fa055629c447f7c548f75bdee.webp)

具体来说，模型先用一个编码器，把整段视频压成一份全局场景表示；再挂一个轻量解码器，专门回答这么一个问题——

「视频里某个点，在某个时刻的三维位置是多少？」

深度图、点云、点轨迹、相机参数，全都从这同一套查询接口里吐出来，不用再为每个任务各养一个解码器。

效果上数字也很能打：在A100上，D4RT做位姿估计能跑到**200+ FPS**，**比去年的最佳论文VGGT快约9倍**，比MegaSaM快约100倍，精度还反超。

在一系列动态4D重建与追踪任务上刷新SOTA，并且支持对视频全部像素做稠密整体重建。

这里藏着一个有意思的「师承」彩蛋：**去年CVPR 2025最佳论文是出自牛津VGG实验室的VGGT**，今年D4RT直接把VGGT拎出来当主要对手按在地上摩擦。

而D4RT的作者名单里，正坐着VGG的灵魂人物**Andrew Zisserman**。

同一条几何重建脉络，连续两年拿下CVPR最高荣誉。

**其他荣誉：提名、时间检验奖、学生论文、人物奖**

**最佳论文荣誉提名（2篇）**

一篇是**SAM 3D**（《SAM 3D：3Dfy Anything in Images》），出自Meta超级智能实验室。

![](https://i.qbitai.com/wp-content/uploads/2026/06/50eff1118178ec784eea4743cefa60cd.webp)

**△**图片来自CVPR2026官方X账号

这篇论文把「SAM」系列从分割延伸到了**单图3D重建**。

给一张普通照片，它就能预测物体的几何、纹理和空间布局，尤其擅长应付现实照片里常见的遮挡和杂乱场景。

背后是一套「人机协同」标注流水线，以前所未有的规模拿到带视觉grounding的3D数据，靠合成预训练+真实对齐的多阶段训练，捅破了3D领域长期的「数据墙」。

在面向真实物体和场景的人类偏好测试里，它拿到了至少5:1的胜率。

另一篇是**NitroGen**（《NitroGen: An Open Foundation Model for Generalist Gaming Agents》）。

![](https://i.qbitai.com/wp-content/uploads/2026/06/dfb293d80aa851d237aee2179f75baf5.webp)

**△**图片来自CVPR2026官方X账号

来自英伟达、斯坦福大学、加州理工学院、芝加哥大学和德克萨斯大学奥斯汀分校。

NitroGen是一个通用游戏智能体的开源基座模型。它在**1000多款游戏、共4万小时游戏视频**上训练，核心做了三件事：

- 用自动化方式从公开游戏视频里反解出玩家动作、构建互联网规模的「视频-动作」数据集；
- 搭一个能衡量跨游戏泛化的多游戏评测环境；
- 再用大规模行为克隆训出统一的「视觉-动作」策略。

从3D动作游戏的战斗，到2D平台跳跃的精细操作，再到程序生成世界里的探索它都能拿下，迁移到没见过的新游戏时，任务成功率最高有52%的相对提升。

这支队伍正是当年用MineDojo拿下NeurIPS最佳论文的英伟达班底。

**时间检验奖（Longuet-Higgins Prize）**

这个奖专颁给「发表十年、扛住了时间考验」的CVPR论文，今年一口气给了2016年发表的两篇：

一篇是**ResNet**（《Deep Residual Learning for Image Recognition》）。

![](https://i.qbitai.com/wp-content/uploads/2026/06/4b839e0babe4b43f41c31684fb6d67fd.webp)

**△**图片来自CVPR2026官方X账号

ResNet用残差连接破解了深层网络「越深越难训」的死结，让上百层的网络真正可训。

十年来它几乎成了深度学习的默认地基，从视觉的CNN到NLP的Transformer再到大模型，处处都有残差连接的影子。

目前引用量**已超过32万**。

另一篇是**YOLO v1**的原始论文。

![](https://i.qbitai.com/wp-content/uploads/2026/06/3461378326c377c3babd5f28cd6f9d9e.webp)

**△**图片来自CVPR2026官方X账号

在它之前，检测主流是「先圈候选框、再逐个分类」的R-CNN路线。

YOLO把检测一把改写成端到端回归，整张图只看一次就直接输出「哪里有什么」。在Titan X上跑到45 FPS、Fast版本更是155 FPS，第一次让「实时检测」真正可用，直接催生了SSD、RetinaNet和后来整个YOLO家族。

目前引用量**接近8万**。

**最佳学生论文：TRELLIS.2**

获奖论文《Native and Compact Structured Latents for 3D Generation》，来自清华大学、微软研究院、中科大与Microsoft AI。

它有个更响亮的名字：**TRELLIS.2**。

![](https://i.qbitai.com/wp-content/uploads/2026/06/ee602cd98ad7a052160804c9a0416611.webp)

**△**图片来自CVPR2026官方X账号

它要解决的，是当前3D生成「画面越来越真、但表示方法拖后腿」的尴尬：复杂拓扑、精细外观总是抓不住。

团队的解法是一种叫**O-Voxel**的新型稀疏体素结构，把几何和外观（连PBR材质参数都算上）同时编进去，能稳稳建模开放面、非流形、全封闭等各种刁钻拓扑。

再配一个稀疏压缩VAE把它压成紧凑的潜在空间，最后训了个40亿参数的flow-matching大模型来做图生3D。

规模虽大，推理却很快，生成资产的几何和材质质量都明显甩开现有模型。

**最佳学生论文提名：ChordEdit**

《ChordEdit: One-Step Low-Energy Transport for Image Editing》，来自广东工业大学、惠州学院、深圳大学和北京大学，同时也是今年的Oral。

![](https://i.qbitai.com/wp-content/uploads/2026/06/f03d52515c49e32787a19cd54da6d97b.webp)

**△**图片来自CVPR2026官方X账号

它解决的是一步式（单步推理）文生图模型的痛点：这类模型生成飞快，但想拿来做文本引导的图像编辑，硬压成一步往往就崩——物体变形、该保留的地方也跟着乱。

团队把图像编辑重新表述成一个**最优传输**问题：在源文本和目标文本各自定义的分布之间做传输，再基于动态最优传输理论推出一套低能量控制策略，让编辑场更平滑、更稳，一大步就能走完。

最终效果是：这些「快但难编辑」的模型，第一次真正具备了实时编辑能力。

**PAMI人物奖**

**年轻学者奖**（Young Researcher Award），颁给博士毕业7年内、已形成代表性研究方向的青年学者。今年获奖的有两位。

一位是**Deepak Pathak**，CMU副教授，横跨CV、机器学习与机器人，研究机器人如何在真实世界里学习、感知与行动。

另一位是**Vincent Sitzmann**，MIT副教授，主攻神经场景表示、3D视觉、世界模型等，目标是让机器像人一样理解和模拟世界。

![](https://i.qbitai.com/wp-content/uploads/2026/06/1cfb7b2b8d0b61420cfd0652fa7f0463.webp)

**△**图片来自CVPR2026官方X账号

**Thomas S. Huang纪念奖**，表彰在研究、教学/指导与社区服务上堪称典范的学者。

今年授予康奈尔大学教授**Noah Snavely**（计算机视觉与图形学）。

![](https://i.qbitai.com/wp-content/uploads/2026/06/1d5a6f16a583d41889458ae142e7e3c9.webp)

值得一提的是，这个奖本身正是为纪念已故华裔计算机视觉先驱**黄煦涛（Thomas S. Huang）**而设。

**CVPR依旧华人闪耀**

这届CVPR，华人含量依然很高。

这种存在感，从投审两端的数据就能看出来：在作者来源地里，**中国以23233人断层第一**，几乎是第二名美国（7556）的三倍。

审稿人同样是中国（10687）人数更多。

![](https://i.qbitai.com/wp-content/uploads/2026/06/9332f0050c8b5b6280ca536ab2c5e6ff.webp)

**△**图片来自CVPR2026官方X账号

再看各路获奖论文，华人面孔也是层出不穷。

最佳论文D4RT的一作是DeepMind资深研究科学家**Chuhan Zhang**（张楚晗）。

![](https://i.qbitai.com/wp-content/uploads/2026/06/82d97914aba2e38ce174cfd75c099007.webp)

她此前在牛津大学几何研究组 （VGG）获得博士学位，导师正是Andrew Zisserman，研究方向覆盖视频理解、动态3D场景重建和生成模型的自动评估。

![](https://i.qbitai.com/wp-content/uploads/2026/06/c344fdde3ba085f1e8d1d7a28990032b.webp)

最佳论文的作者中，还包括牛津与DeepMind的多位华人研究者。

![](https://i.qbitai.com/wp-content/uploads/2026/06/20b0d8c550a503ceff320bdee65ebbea.webp)

**Junyu Xie**，同样来自牛津VGG，师从Andrew Zisserman和谢伟迪。D4RT正是他2025年夏在DeepMind实习期间完成的工作。

![](https://i.qbitai.com/wp-content/uploads/2026/06/dffa70c9ae38264c642872556d332885.webp)

还有**Shuyang Sun**和**Junlin Zhang**，均为Google DeeoMind研究员。

![](https://i.qbitai.com/wp-content/uploads/2026/06/104f973e2feb810b282690b268d31e0f.webp)

而**最佳学生论文TRELLIS.2**，整支队伍是**全华人阵容**。

![](https://i.qbitai.com/wp-content/uploads/2026/06/fce87fbab49425a0ff0793c5a081a5df.webp)

一作**Jianfeng Xiang**（向剑锋）是清华博士生，同时也是上一代爆款3D生成模型TRELLIS（v1）的一作。

![](https://i.qbitai.com/wp-content/uploads/2026/06/3812d57ffa0012ad39011aa3bc2b7834.webp)

**Xiaoxue Chen **（陈小雪），清华大学人工智能产业研究院（AIR）的博士研究生，研究方向为计算机视觉。

![](https://i.qbitai.com/wp-content/uploads/2026/06/84e26a1667820df12ddece4dc19df904.webp)

通讯作者**Jiaolong Yang**（杨蛟龙）来自微软亚研院，长期深耕3D视觉与生成。

![](https://i.qbitai.com/wp-content/uploads/2026/06/d52a19692d01394a1bde8687d9e0dced.webp)

**Sicheng Xu**（徐思成），同样来自微软亚研院，研究方向为物理人工智能和多模态。

![](https://i.qbitai.com/wp-content/uploads/2026/06/81a55ff9839a396395946f21c15b8a3b.webp)

**Ruicheng Wang**（王瑞程），中国科学技术大学计算机科学与技术学院的博士生，研究方向为空间智能。

![](https://i.qbitai.com/wp-content/uploads/2026/06/f3ed07de1740fa35b5569422576d596c.webp)

**Zelong Lv**，中国科学技术大学计算机科学学院博士生。

![](https://i.qbitai.com/wp-content/uploads/2026/06/e0c58a621b21935ea416c5c9915a096b.webp)

**Yu Deng**（邓誉），微软亚研院高级研究员，研究方向为3D视觉生成、空间理解和具身智能。

![](https://i.qbitai.com/wp-content/uploads/2026/06/b7f7be0f5522aacbdd044306237471ae.webp)

**Hao Zhao**（赵昊），清华大学智能产业研究院（AIR）助理教授，曾任Intel Labs China研究科学家。研究方向为机器人3D场景理解、具身智能、自动驾驶。

![](https://i.qbitai.com/wp-content/uploads/2026/06/273bb13a7a15d7442002d219be1b4955.webp)

**Nicholas Jing Yuan**（袁晶），微软全球合伙人、全球资深副总裁技术顾问；IEEE Fellow，引用17000+

此前曾任华为云人工智能副总裁、首席科学家兼语言与语音创新实验室主任。在微软期间，主导开发了微软小冰人工智能生成内容技术。

![](https://i.qbitai.com/wp-content/uploads/2026/06/49955579004772e02f288bc72de2a838.webp)

最佳学生论文提名**ChordEdit**，则是一支**纯国内高校班底**，甚至其中有不少本科生。

![](https://i.qbitai.com/wp-content/uploads/2026/06/f978a8f269cfb3e34025f285eaccf554.webp)

一作**Liangsi Lu**（卢梁司），广东工业大学信息与计算科学专业的本科生，研究方向为表征学习和视觉生成。

![](https://i.qbitai.com/wp-content/uploads/2026/06/a84ba92ebf5b7e293e7817be248f7252.webp)

通讯作者**Yang Shi**，广东工业大学计算机科学学院的本科生，研究方向为计算机视觉和数据挖掘。

![](https://i.qbitai.com/wp-content/uploads/2026/06/8f55501c2b38b9a1fe2dad862c618ecb.webp)

团队还有来自深圳大学、北京大学等的研究者，是今年华人荣誉里少见的「全本土」队伍。

**Xuhang Chen**，惠州学院计算机科学与工程学院讲师，同时在旭日信息科技担任研究员。2025年在澳门大学和中国科学院深圳先进技术研究院（SIAT）获得计算机科学博士学位。

![](https://i.qbitai.com/wp-content/uploads/2026/06/e70cb899c3f57a52ee4231b1e415ffae.webp)

此外还有**Minzhe Guo**（来自广东工业大学）、**Shichu Li**（来自深圳大学）、**Jingchao Wang**（来自北京大学）等作者。

接下来是时间检验奖ResNet的四位作者——**何恺明、张祥雨、任少卿、孙剑**。

这篇十年前从微软亚洲研究院走出的工作，如今几乎撑起了半个深度学习世界。

一作**何恺明**是其中最广为人知的那个。

ResNet之后，他又先后做出了Mask R-CNN、FPN、MAE等一系列奠基性工作，目前已从Meta AI转赴MIT任教，是当下计算机视觉领域引用量最高的研究者之一。

![](https://i.qbitai.com/wp-content/uploads/2026/06/2877bd0cd4f5e50580051200b4063507.webp)

也有网友在X上po出了与恺明的合照，感觉大佬好像瘦了呢（狗头

此外，Meta的超级智能实验室（MSL）和英伟达的两篇提名论文里，华人作者也非常多，放眼过去简直是「人从众」……

![](https://i.qbitai.com/wp-content/uploads/2026/06/1420b251a928c4a7e6439135b3b94de8.webp)

小道消息表示，Meta内部的非华人员工会感觉自己融入不进去公司，因为团队里华人太多了…嗯，从这个论文名单里也能一窥一二。

![](https://i.qbitai.com/wp-content/uploads/2026/06/becbc49ade0959a2707e343f5bdb0da7.webp)

感兴趣的朋友还可以继续深挖（小编已力竭.jpg）。

总之，让我们祝贺在CVPR 2026获得认可和嘉奖的所有朋友，也准备好接下来在如此火爆的AI时代被追逐的准备吧～

苟富贵，好好推动AI，造福全人类～

*版权所有，未经授权不得以任何形式转载及使用，违者必究。*


[刚刚，Anthropic提交了招股书！](https://www.qbitai.com/2026/06/428407.html)*2026-06-03*[马斯克是SpaceX面子，她才是里子](https://www.qbitai.com/2026/06/431371.html)*2026-06-06*[大模型发展三年半，AI圈终于等来了一场“不要大厂，只赌脑洞”的比赛](https://www.qbitai.com/2026/06/431287.html)*2026-06-06*[Hinton吹哨了：AI已经有意识！](https://www.qbitai.com/2026/06/431349.html)*2026-06-06*
