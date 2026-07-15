---
title: "Smart Cellular Bricks: Towards Collective Intelligence for the Physical World"
source: TLDR AI · 2026-07-14
url: https://sakana.ai/smart-cellular-bricks/?utm_source=tldrai
date: 2026-07-15
published_at: 2026-07-14T12:00:00+00:00
tag: 论文研究
item_id: e83a574c9e1ff383
---
[Smart Cellular Bricks: Towards Collective Intelligence for the Physical World](https://sakana.ai/smart-cellular-bricks/)

  *Collections of hundreds of physical 3D cellular bricks, simple modular hardware units that run identical local Neural Cellular Automata without any global knowledge, collaboratively infer their overall shape class.*

At Sakana AI, a recurring theme in our research is collective intelligence: the observation that sophisticated, robust behavior can arise from many simple parts following local rules, with no central controller, as it does in a colony, a tissue, or a brain. Until now, we have explored this idea in simulated systems, such as getting several frontier models to [reason together and build on one another’s attempts](https://sakana.ai/ab-mcts/), coordinating them so that [many models act as one](https://sakana.ai/fugu/), or having agents with partial, overlapping views [negotiate along their shared boundaries](https://pub.sakana.ai/sheaf-admm/) to converge on a globally consistent solution.

Today, we are happy to share that a paper extending this line of work into physical hardware has been accepted for publication in *Nature Communications*. The system is a collection of simple cubic bricks, each running the same small neural network and communicating only with the bricks it is physically connected to. No brick is told its position or which shape it is part of, yet from these purely local exchanges the collective converges on the correct global shape and can locate where modules are missing or damaged.

For us, this is a first step toward taking our work on collective intelligence beyond software and into the physical world. We wanted to ask whether the same decentralized principles hold up when communication is noisy and modules fail. They largely do. Hundreds of bricks classify a range of 3D shapes, still recognize shapes with variations they were not trained on, and keep converging correctly even when a fraction of their modules go silent. Using the same framework, the collective can also flag structural damage and guide a step-by-step recovery.

The work is a collaboration between researchers at **IT University of Copenhagen**, **Sakana AI**, and **Autodesk**.

Read the full paper in *Nature Communications*: [https://www.doi.org/10.1038/s41467-026-75166-7](https://www.doi.org/10.1038/s41467-026-75166-7)

Explore the code on GitHub: [https://github.com/rmorenoga/cube3D](https://github.com/rmorenoga/cube3D)

## Introduction

Many biological systems exhibit a remarkable capacity to determine their own anatomical structure. Through local communication and self-organization, groups of cells can assess whether they have correctly formed a target shape, such as an organ, and can actively remodel body parts following injury. A salamander can regenerate a damaged tail that transforms into a functional leg, and simple organisms like Hydra and Planaria can fully restore their morphology regardless of which part is lost. This ability to classify general anatomical features, rather than match a fixed target shape, is what enables variability among individuals while enhancing the robustness of the process. The overall function and design of an organ may be consistent across a species, even as its specific shape, size, or scale differs from one individual to the next.

Artificial systems composed of many physically distributed modules that can autonomously infer their structural class, without centralized control, would represent a significant step toward more adaptable, intelligent artificial collectives. Such systems could enable powerful applications in smart materials and reconfigurable robotics, where global knowledge must emerge from local sensing and communication. Motivated by the scalability and resilience of biological collective intelligence, we introduce a fully decentralized system in which hundreds of physically embodied “cellular” bricks collectively classify their global shape and detect local damage, with no central controller and no module ever knowing its own position.

![](https://sakana.ai/assets/smart-cellular-bricks/shape-classification.png) 

*Neural cellular automata for shape classification. (A) A cellular brick module. (B) Bricks assembled into four different shapes. (C) Each cell takes in local information from its connecting neighbors and its own hidden channels; information is aggregated locally, enabling the object to recognize its particular shape over multiple iterations. (D) The local update rules are encoded with a neural cellular automaton, a deep neural network.*

The collective intelligence algorithm we developed builds on the framework of differentiable [Neural Cellular Automata (NCA)](https://distill.pub/2020/growing-ca/) and [self-classifying collective systems](https://distill.pub/2020/selforg/mnist/), extended to operate in 3D and implemented on physical modular hardware. NCAs generalize traditional cellular automata, in which the local update rules are typically hand-crafted, by instead learning these rules. Unlike traditional CAs that operate with discrete cell states, NCAs use continuous-valued cell states, enabling end-to-end differentiability and compatibility with gradient descent. On a high level, each cell in our system is tasked with determining which type of shape it is a part of, based solely on communication with its local neighbors and its own memory state. The update rules are parameterized by a deep neural network built from 3D convolutional layers, whose outputs are added to the state of each cell. Here, the collective is tasked to distinguish between objects resembling planes, chairs, cars, tables, houses, guitars, and boats, trained with a cross-entropy loss to predict the class label through gradient-based optimization.

Rather than matching against a single, predefined configuration, our system generalizes across entire classes of shapes, such as different planes or different tables. This shift from precise self-recognition to high-level shape classification enables greater flexibility and tolerance to variation. The system can also detect structural inconsistencies caused by missing or faulty modules, using only local interactions and without requiring any actuation or centralized sensing.

## Results

Each cellular brick is a small printed-circuit-board cube with electrical connectors on all six faces, a microcontroller, an LED to display its current class guess, and the electronics to power itself. Bricks stack together into arbitrary objects and communicate purely locally over a custom digital serial protocol, iterating until the collective converges on a single shape label.

We ran large-scale experiments with more than 500 bricks in simulation and almost 200 physical bricks. In simulation the approach reaches 98.97% accuracy. Transferring the simulation-trained NCA directly onto hardware, we built four distinct shapes ranging from 26 bricks (a guitar) to 197 (a round table); the bricks reached correct consensus on a plane, a guitar, a boat, and a table, with 100% success rate across all four. In hardware, the collective converges in fewer than 60 update cycles, about three minutes of real time.

## Robustness to faulty cells and shape variation

Biological systems are remarkably robust to damage, noise, and faulty components, thanks to their local, distributed decision-making. To test whether our system inherits this property, we disabled subsets of bricks in hardware, preventing them from sending or receiving messages, and measured the effect on recognition. Most shapes maintained high accuracy at 5% failure rates, and some, like the plane and boat, degraded only minimally even at 15%. The exception is shapes with narrow structural bottlenecks: in the guitar, a single failure along the neck can sever the two halves of the object and disrupt classification.

![](https://sakana.ai/assets/smart-cellular-bricks/robustness.png) 

*For the guitar and plane assembled in hardware, we disabled particular cells (marked in red) to test robustness. By design, the plane is far more robust than the guitar, where a single failure along the neck can break the classification process.*

The system also generalizes beyond the specific examples it saw during training. We designed test shapes with novel variations within known classes: a table modified to have five shortened legs at random positions, a boat with its central bridge shifted off-center, and scaled-down versions of the plane and table. The altered five-legged table was still correctly classified as a table, and the shifted boat bridge did not impair recognition, suggesting the NCA captures abstract structural features rather than overfitting to specific instances. It is not infallible, however: the scaled-down table was misclassified as a chair, likely because the reduced module count compresses the structural cues the network relies on.

## Emerged communication strategies

We also looked at how the collective actually solves the task. Inspired by morphogens (the diffusible molecules that form gradients across developing tissues and give cells positional information), we examined the activation patterns of the NCA’s hidden channels. Early in the process, the system often establishes left-right and radial patternings that resemble the developmental axes of embryos.

*The hidden channels learn morphogen-like activation patterns, such as left-right and radial gradients, enabling decentralized shape recognition and differentiation.*

This also explains how the collective tells tables from chairs. Many cells in a chair are initially classified as a plane, just as in tables. Unlike tables, though, an anterior-posterior patterning is established (akin to the biological head-to-tail axis), and over time this signal propagates from the backrest outward, guiding the cells to a consensus that they form a chair. The default reading for both is “table,” and morphogen-like signals originating in the backrest gradually induce a coherent reclassification.

## Damage detection and recovery

An exciting extension is to let each cell not only recognize which larger shape it belongs to, but also detect whether one of its neighboring cells has been damaged. To achieve this, the cells were trained jointly for shape classification and local damage detection, predicting either no damage or damage in one of six spatial directions. Training used synthetically damaged shapes with spherical and cubic lesions. Despite the added task, the system retained 98.9% shape-classification accuracy while detecting damage with an average accuracy of 94.8%.

Can we exploit this to recover from damage, rather than merely predict it? Biological organisms like planarians and axolotls regrow complex body parts through distributed, decentralized cycles of sensing and regeneration, with no central controller. Mirroring this, we started from a small cluster of cells and repeatedly added new cells in the direction indicated by the existing ones, until no more damage was detected. Without ever being trained starting from only a few cells, the model recovered almost all shapes across all object classes with high accuracy. Models with larger hidden states performed significantly better, likely because they can carry more information across the growth process.

*Starting from a small seed cluster, cells repeatedly add new modules in the direction their neighbors indicate, regrowing a chair, a table, and a plane until no further damage is detected.*

## Simulation scaling to larger and more complex morphologies

Hardware experiments are naturally limited by the number of available robotic bricks and the practical constraints of physical deployment. We therefore evaluated scaling behavior in simulation, where the approach already works well beyond the morphologies demonstrated in hardware, extending from 15x15x15 to 32x32x32 and 64x64x64 grids. Moreover, the higher-resolution experiments involve substantially richer geometries than those used in hardware, including shapes with hollowness, internal cavities, and assemblies of more than 18,000 cubes. These experiments reveal encouraging scaling behavior: as spatial resolution and structural complexity increase, maintaining high performance requires greater model capacity, but the relationship is predictable and favorable.

*Regeneration of objects (grid up to 64³): a fish, the Sakana AI logo, and a heart. Cells locally predict the direction of missing neighbors (colors) and regrow by consensus of these predictions.*

## Conclusion

These experiments show that learned, fully-decentralized control lets large assemblies of simple, identical modules reach a coherent understanding of their global shape and pinpoint structural faults, using nothing more than short-range communication and on-board computation. In hardware trials with almost 200 bricks, the collective converged on the correct class in fewer than 60 update cycles, about three minutes of real time, and the very same infrastructure and identical per-cube code extends to localizing missing modules and even guiding their regrowth. To our knowledge, this is the first physical realization of large-scale, bio-inspired self-recognition in three dimensions, and a concrete step toward the long-standing goal of modular, self-reconfigurable systems.

For us at Sakana AI, it is also a first step in a broader direction: taking the principles of collective intelligence we have studied in software and letting them emerge, decentralized and robust, in the physical world.

## Looking ahead

We are excited about where this leads. In the future, we imagine smart materials that let structures sense and report damage on their own, enabling safer and more resilient architecture, or LEGO-like systems that recognize their own configuration and adapt in real time. Getting there will require active self-repair through actuation, such as magnetically docked milli-scale blocks, along with miniaturized electronics and refined connectors for denser, more organic geometries, and closed-loop growth in which bricks autonomously recruit others from a shared pool.

More broadly, embedding distributed intelligence into the building blocks themselves points toward environments that are robust, adaptive, and regenerative, blurring the boundary between construction and computation. We can imagine many other directions too, from denser cellular collectives to mobile, reconfigurable physical systems.

To learn more, read the full paper in * Nature Communications* and explore the 

[code on GitHub](https://github.com/rmorenoga/cube3D).

## Sakana AI

We are looking for people to help shape the future of AI together with Sakana AI. Please see our [careers page](https://sakana.ai/careers/) for more information.

# 集合知を物理世界へ：自らの形状を認識し修復する「Smart Cellular Bricks」

*局所的なニューラル・セルラー・オートマトンを動かすだけの単純なモジュール型ハードウェアである何百個もの3次元のブロックが、協調して全体の形状を推論する。*

Sakana AIでは、一貫して「集合知（collective intelligence）」を主な研究テーマとしてきました。生物の群れや生体組織、あるいは脳のように、中央の制御装置なしに局所的なルールに従う多数の単純な要素から、複雑かつ高度な振る舞いがどのようにして生まれるのか。これまでSakana AIでは、集合知の発想を主にAIシステムに適用し、複数のフロンティアモデルに協力して推論させる[木探索アルゴリズム](https://sakana.ai/ab-mcts/)、単一のインターフェースで[複数のモデルを束ねるオーケストレーターモデル](https://sakana.ai/fugu/)、部分的で重なり合う視野を持つエージェント同士が[境界を通じてすり合わせ全体として整合した解に収束させる手法](https://pub.sakana.ai/sheaf-admm/)などを開発してきました。

今回のNature Communications 誌に掲載された「Smart Cellular Bricks」は、集合知の原理を物理的なハードウェアへと発展させた研究です。「Smart Cellular Bricks」は単純な立方体状のブリックの集合であり、各ブリックは同一の小さなニューラルネットワークを動かし、物理的に接続された隣のブリックとだけ通信します。それぞれのブリックは自分の位置や全体の形状については知らされていないにもかかわらず、集団として正しい形状を認識し、さらにモジュールの損傷箇所の特定も可能になります。

私たちにとってこれは、集合知の研究をソフトウェアの外、すなわち物理的な世界へと踏み出す最初の一歩です。通信にノイズが乗り、モジュールが故障することもある環境で、同じ分散的な原理が通用するのかを確かめる試みでもあります。何百個ものブリックがさまざまな3D形状を分類し、学習時には見たことのないバリエーションの形状も認識し、一部のモジュールが動作を止めても正しく収束し続けることを示しました。同じ枠組みを使えば、集団は構造的な損傷を検知し、段階的な修復も可能になります。

本研究は、コペンハーゲンIT大学、Sakana AI、Autodeskの研究者の共同で行われました。

Nature Communications 論文：[https://www.doi.org/10.1038/s41467-026-75166-7](https://www.doi.org/10.1038/s41467-026-75166-7)

コード（GitHub）：[https://github.com/rmorenoga/cube3D](https://github.com/rmorenoga/cube3D)

## はじめに

多くの生物システムは、自らの解剖学的な構造を自分で見きわめるという、驚くべき能力を備えています。細胞の集団は、局所的な通信と自己組織化を通じて、たとえば器官のような目標の形が正しくできているかを確かめ、傷を負ったあとには体の一部を能動的に作り変えることができます。サンショウウオは、損傷した尾を機能的な脚へと変えて再生しますし、ヒドラやプラナリアのような単純な生物は、どの部分を失っても元の形態を完全に取り戻せます。ここでみられるのは、決まった形にぴったり合わせるのではなく、大まかな解剖学的特徴を「分類」する能力です。器官の機能や全体の設計がおおむね共通していれば、形・大きさ・スケールは個体ごとに異なっても全体の形がわかるようになっています。

たくさんの部品が、中央の制御に頼らず、自分たちがどんな構造なのかを分散的・自律的に見きわめる。そうした人工システムができれば、より適応的で知的な人工の集団に向けた大きな一歩になります。こうしたシステムは、スマートマテリアルや再構成可能なロボティクスといった分野で、高い有用性を持ちます。生物の集合知が持つスケーラビリティと回復力に着想を得て、私たちは分散型の「Smart Cellular Bricks」を提案しました。このシステムでは、何百個もの物理的な「cellular brick」が、中央の制御装置を持たず、どのモジュールも自分の位置を知らないまま、集団として全体の形状を分類し、局所的な損傷を検知します。

![](https://sakana.ai/assets/smart-cellular-bricks/shape-classification.png) 

*形状分類のためのニューラル・セルラー・オートマトン。(A) cellular brickのモジュール。(B) ブリックを組み上げて作った4種類の形状。(C) 各セルは、接続された隣接セルと自身の隠れチャネルから局所的な情報を取り込む。情報は局所的に集約され、複数回の反復を通じて対象物が自らの形状を認識できるようになる。(D) 局所的な更新ルールは、ディープニューラルネットワークであるニューラル・セルラー・オートマトンによって符号化される。*

私たちが開発した集合知アルゴリズムは、微分可能な[ニューラル・セルラー・オートマトン（Neural Cellular Automata: NCA）](https://distill.pub/2020/growing-ca/)と[自己分類する集団システム](https://distill.pub/2020/selforg/mnist/)の先行研究を土台に、これを3Dで動くように拡張し、物理的なモジュール型ハードウェアの上で動かせるようにしました。従来のセルラー・オートマトンは、局所的な更新ルールを人手で設計するのが一般的ですが、NCAはこのルールそのものを「学習」で獲得します。また、離散的なセル状態を扱う従来のセルラー・オートマトンとは違い、NCAは連続値のセル状態を用いるため、全体をエンドツーエンドで微分でき、勾配降下法とも相性がよくなります。大まかに言えば、各セルは、隣り合うセルとの通信と自分の記憶状態だけを手がかりに、自分がどの種類の形状の一部なのかを判断します。更新ルールは3次元の畳み込み層から成るディープニューラルネットワークで表現され、その出力が各セルの状態に加算されていきます。本研究では、飛行機・椅子・自動車・テーブル・家・ギター・ボートの形態を区別する設定とし、交差エントロピー損失を使った勾配ベースの最適化によって、正しいクラスラベルを予測できるよう学習させました。

このシステムは、あらかじめ定められた形態だけでなく、たとえばさまざまな形の飛行機やテーブルといった、形状のクラス全体に汎化します。このように、厳密な形態認識からより抽象的な形状分類へと移行することで、柔軟性が増し、形のばらつきにも強くなります。さらにこのシステムは、局所的な相互作用だけを用い、いかなるアクチュエーションや中央集権的なセンシングも必要とせずに、欠損や故障したモジュールによって生じる構造的な不整合を検知することもできます。

## 結果

各cellular brickは、小さなプリント基板でできた立方体であり、6面すべてに電気コネクタを備え、マイクロコントローラ、現在のクラス推定を表示するLED、そして自らに給電する電子回路を搭載しています。ブリックを組み合わせ任意の物体を組み上げることができ、独自のデジタルシリアルプロトコルで純粋に局所的に通信しながら、集団が一つの形状ラベルの認識に収束するまで推論を続けます。

私たちは、シミュレーション上で500個以上のブリック、実機では200個近いブリックを使った実験を行いました。シミュレーションでは、この手法は98.97%の精度に達します。シミュレーションで学習したNCAをそのまま実機に移し、26個（ギター）から197個（円形のテーブル）まで、規模の異なる4種類の形状を組み上げました。ブリックは飛行機・ギター・ボート・テーブルのいずれについても正しい合意に到達し、4種類すべてで成功率100%を達成しました。実機では、集団は60回未満の更新サイクル、実時間にしておよそ3分で収束します。

## 故障セルと形状のばらつきに対する頑健性

生物システムは、局所的で分散的な意思決定のおかげで、損傷やノイズ、部品の故障に対して驚くほど頑健です。私たちのシステムもこの性質を受け継いでいるのかを確かめるため、実機で一部のブリックを無効化してメッセージの送受信をできなくし、認識にどう影響するかを測定しました。ほとんどの形状は5%の故障率に対して高い精度を保ち、一部の例（飛行機やボートなど）では15%が故障してもほとんど性能が落ちませんでした。例外は、細い構造的なボトルネックを持つ形状であり、たとえばギターの場合、ネックの部分で一つ故障が起きるだけで物体が二つに分断され、分類が破綻してしまうことがあります。

![](https://sakana.ai/assets/smart-cellular-bricks/robustness.png) 

*ギターと飛行機で、特定のセル（赤で表示）を無効化し、頑健性を検証した。飛行機はギターよりもはるかに頑健だった。ギターでは、細い箇所が少し壊れるだけで分類が不可能になる。*

このシステムは、学習した具体的な形態を超えて汎化するのでしょうか。既知のクラスの中に新しいバリエーションを持たせたテスト形状、たとえば、脚をランダムな位置に5本、短く付け替えたテーブル、中央のブリッジ部分を中心からずらしたボート、そして飛行機とテーブルを縮小したバージョンを用意したところ、5本脚に変形したテーブルはそれでも正しく「テーブル」と分類され、ブリッジをずらしたボートも認識できました。NCAが個々の事例に過剰適合するのではなく、抽象的な構造的特徴を捉えている証拠と言えます。ただし、縮小版のテーブルは「椅子」と誤って分類されるなどエラーもみられました。モジュール数が減ったことで、構造の手がかりが失われてしまったためだと考えられます。

## コミュニケーション戦略の創発

この集団は、自分の形を推定するという課題を、どのように解いているのでしょうか。私たちは、生物の発生のプロセスで重要な役割を果たすモルフォゲン（発生中の組織全体に濃度勾配を形成し、細胞に位置情報を与える拡散性の分子）に着想を得ました。NCAの隠れチャネルがどう活性化するのかを観察したところ、プロセスの初期には、システムはしばしば「胚の発生軸」を思わせる左右方向や放射状のパターンを形成しました。

*隠れチャネルは、左右方向や放射状の勾配といった、モルフォゲンに似た活性化パターンを学習し、分散的な形状認識と分化を可能にする。*

これが、集団がテーブルと椅子を見分ける仕組みだと考えられます。椅子を構成する多くのセルは、テーブルの場合と同じように、最初は「テーブル」と分類されます。ただしテーブルと違うのは、（生物の頭尾軸に相当する）前後方向のパターンが立ち上がる点です。時間が経つにつれてこの信号が背もたれから外側へと伝わり、セルたちを「自分たちは椅子だ」という合意へと導きます。どちらの場合もデフォルトの解釈は「テーブル」であり、背もたれを起点とするモルフォゲンのような信号が、少しずつ再分類を誘発するのです。

## 損傷の検知と修復

この手法の重要な拡張の一つは、各セルに、自分がどの形状に属するかを認識させるだけでなく、隣接するセルが損傷しているかどうかも検知させる応用です。これを実現するため、セルを形状分類と局所的な損傷検知の両方について同時に学習させ、「損傷なし」または6つの空間方向のいずれかの「損傷」を予測するようにしました。学習には、球状および立方体状の欠損を人工的に加えた損傷形状を用いました。このように課題を一つ増やしても、システムは98.9%の形状分類精度を維持しつつ、平均94.8%の精度で損傷を検知しました。

これを単なる損傷予測だけでなく、損傷からの「修復」に活かせないでしょうか。プラナリアやアホロートル（ウーパールーパー）といった生物は、中央制御に頼らず、センシングと再生を繰り返す分散的なサイクルによって、複雑な体の部位を作り直します。これになぞらえ、私たちは小さなセルの塊から出発し、既存のセルの指示に沿って新しいセルを損傷が検知されなくなるまで付け加えました。数個のセルから始める訓練は一度もしていないにもかかわらず、モデルはすべての物体クラスでほぼすべての形状を高い精度で復元しました。隠れ状態を多く持つモデルほど成績が良く、これは形の成長過程でより多くの情報を運べるためだと考えられます。

*小さな種となる塊から出発し、セルは隣接セルが示す方向に新しいモジュールを繰り返し追加していき、損傷がこれ以上検知されなくなるまで、椅子・テーブル・飛行機を再成長させる。*

## シミュレーションで、より大きく複雑な形態へ

ハードウェア実験は、利用できるロボットブリックの数や、物理的に配置する際の現実的な制約によって、どうしても規模が限られます。そこで私たちは、シミュレーション上でスケーリングの挙動を評価しました。シミュレーションでは、この手法はハードウェアで実証した形態をはるかに超えてうまく機能し、15×15×15から32×32×32、さらには64×64×64のグリッドへと拡張できます。しかも、高解像度の実験では、ハードウェアで用いたものよりもはるかに豊かな幾何形状を扱います。たとえば、中空の構造や内部の空洞、さらには18,000個を超える立方体から成る集合体などです。これらの実験からは、有望なスケーリングの傾向が見えてきます。空間解像度と構造的な複雑さが増すにつれて、高い性能を保つにはより大きなモデル容量が必要になりますが、そこには予測可能な関係性がみられました。

*最大64³グリッドで物体を再生させる様子（魚・Sakana AIロゴ・心臓）。各セルは欠けた隣接セルの方向を局所的に予測し（色がついた部分）、予測についての合意が得られた部分が再成長する。*

## おわりに

これらの実験は、単純な形の同一形態モジュールの集合が、近距離の通信と各要素が完全に分散型の計算を行うだけで、自分たちの全体形状を理解し、構造的な欠陥まで正確に突き止められるということを明らかにしました。200個近いブリックを用いた実機試験では、集団は60回未満の更新サイクル、実時間にしておよそ3分で正しいクラスに収束しました。しかも、まったく同じハードウェアと立方体ごとに共通のコードが、欠損モジュールの位置特定から、その再成長の誘導にまでそのまま拡張できました。私たちの知る限り、これは大規模かつ生物に着想を得た3次元での自己認識を物理的に実現した初めての例であり、モジュール型で自己再構成可能なシステムという長年の目標に向けた、具体的な一歩だと考えています。

Sakana AIにとっては、これまでソフトウェアの中で研究してきた集合知の原理を、分散的で頑健なかたちのまま、物理世界で実現するための第一歩でもあります。

## 今後の展望

こうした研究はこの先どこへ向かうのでしょうか。たとえば、構造物が自分で損傷を感じ取って報告してくれるスマートマテリアルがあれば、より安全で回復力のある建築が可能になるかもしれません。あるいは、自分の構成を認識してリアルタイムに適応する、レゴのようなシステムができるかもしれません。そのためには、磁力で結合するミリスケールのブロックなど、能動的な自己修復のためのアクチュエーターを組み込んだハードウェアや、より高密度で有機的な形状を実現するための電子回路の小型化やコネクタの改良、さらに、ブリックのプールから自律的に仲間を呼び寄せる閉ループ型の成長の仕組みも必要になります。

さらに広い視点からは、分散的な知能を構成要素そのものに組み込む本研究のアプローチは、ロバストかつ適応的かつ再生的（regenerative）な環境への接近を意味します。そこでは、「構築」と「計算」の境界が曖昧になっていくかもしれません。もっとずっと高密度なセルの集団や、移動可能で再構成可能な物理システムまで、発展の可能性は多くあります。

さらに詳しくは、* Nature Communications* の論文やGitHubで公開している

[コード](https://github.com/rmorenoga/cube3D)をご覧ください。

## Sakana AI

AIの未来を、Sakana AIと一緒に切り拓いてくださる方を募集しています。当社の[募集要項](https://sakana.ai/careers/)をご覧ください。

![](https://sakana.ai/assets/careers/applied_research_eng_high_res4.jpg)
