---
title: "NVIDIA Launches Cosmos 3, the Open Frontier Foundation Model for Physical AI"
source: TLDR AI · 2026-06-02
url: https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai?utm_source=tldrai
date: 2026-06-03
published_at: 2026-06-02T12:00:00+00:00
tag: 论文研究
item_id: 02394d1ef542cdcb
---
**News Summary:**

- NVIDIA Cosmos 3 is a new leaderboard-topping open physical AI foundation model, built on a breakthrough mixture-of-transformers architecture for physical AI reasoning, world simulation and action generation.
- Cosmos 3 is the world’s first fully open omnimodel with native vision reasoning and multimodal generation across text, image, video, ambient sound and action for state-of-the-art synthetic data generation and physical AI policy model development.
- NVIDIA launches the NVIDIA Cosmos Coalition with leading AI labs and robotics leaders — including Agile Robots, Black Forest Labs, Generalist, LTX, Runway and Skild AI — to advance the next generation of open world models.

**NVIDIA GTC Taipei**—NVIDIA today launched [ NVIDIA Cosmos™ 3](https://www.nvidia.com/en-us/ai/cosmos/), an open world foundation model for physical AI built on a breakthrough

[architecture that combines vision reasoning, world generation and action prediction in a single system.](https://www.nvidia.com/en-us/glossary/mixture-of-transformers/)

__mixture-of-transformers__Cosmos 3 is the world’s first fully open [ omnimodel](https://www.nvidia.com/en-us/glossary/omni-model/) that can natively understand and generate text, images, video, ambient sound and actions with leading physics accuracy, reducing physical AI training and evaluation cycles from months to days.

NVIDIA also launched the NVIDIA Cosmos Coalition, a global collaboration between [ world model](https://www.nvidia.com/en-us/glossary/world-models/) builders and AI developers — including

[, Black Forest Labs, Generalist, LTX, Runway and Skild AI — working together to advance next-generation world models.](https://www.agile-robots.com/en/news/detail/?tx_news_pi1%5Baction%5D=detail&tx_news_pi1%5Bcontroller%5D=News&tx_news_pi1%5Bnews_preview%5D=158&cHash=d40b462afdc783bd58a86c12e0bbb770)

__Agile Robots__“The big bang of physical AI is just around the corner thanks to breakthroughs in multimodal reasoning language, vision and world models,” said Jensen Huang, founder and CEO of NVIDIA. “The Cosmos 3 family of open, frontier omnimodels gives developers a generational leap in ability to build robots, autonomous vehicles and vision AI that perceive, reason, plan and act in the physical world.”

**A New Architecture for Physical AI**

Cosmos 3 tackles a fundamental challenge in physical AI: enabling robots, autonomous vehicles (AVs) or vision agents to generalize in the real world with limited training data and fragmented simulation stacks.

The model’s mixture-of-transformers architecture pairs a reasoning transformer with an expert generation transformer, enabling Cosmos 3 to understand object interactions, motion and spatial-temporal relationships before generating video and action trajectories.

Trained on one of the largest multimodal physical AI datasets — including billions of samples across text, image, video, sound and action trajectories — the model gives developers a powerful pretrained foundation for building physical AI systems with less data and lower training costs.

Developers can use Cosmos 3 as:

**A**that understands and reasons across modalities.__vision language model__**A world model or video foundation model**that simulates physical environments and predicts future world states for training and evaluation.**The backbone for**that help train robots to perform specific tasks.__world action models__

Cosmos 3 models deliver leading results on physical AI benchmarks. Among open models, it ranks first across [ Artificial Analysis](https://artificialanalysis.ai/leaderboards/models?weights=open&reasoning=reasoning&size=small%2Cmedium),

[,](https://physics-iq.github.io/)

__Physics-IQ__[and](https://huggingface.co/spaces/shi-labs/physical-ai-bench-leaderboard)

__PAI-Bench__[for world generation accuracy,](https://huggingface.co/spaces/DAGroup-PKU/RBench-Leaderboard)

__R-Bench__[and](https://research.nvidia.com/labs/srl/projects/robolab/)

__RoboLab__[for action policy, and the](https://robo-arena.github.io/leaderboard)

__RoboArena__[and](https://huggingface.co/spaces/clemson-computing/VANTAGE-Bench-Leaderboard)

__VANTAGE-Bench__[leaderboards for vision understanding.](https://eval.aicitychallenge.org/aicity2026/submission/leaderboard?trackId=3&type=general)

__TAR__The Cosmos 3 lineup gives developers options for different stages of physical AI development:

**Cosmos 3 Super**for post-training robotics and AV models that need the highest physics accuracy and generation quality.**Cosmos 3 Nano**for high-quality video and action reasoning in fractions of a second.**Cosmos 3 Edge**, coming soon, for real-time inference at the edge.

**Cosmos Coalition Accelerates Open World Model Development**

The Cosmos Coalition is a global collaboration between world model builders, AI developers and physical AI leaders to advance open world models across industries, enabling members to contribute models, research and evaluation techniques while using Cosmos 3 technologies, training tools and [ NVIDIA DGX™ Cloud](https://www.nvidia.com/en-us/data-center/dgx-cloud/) infrastructure for large-scale training.

Founding coalition members include Agile Robots, Black Forest Labs, Generalist, LTX, Runway and Skild AI. By building in the open and contributing across a shared ecosystem, the coalition aims to enable faster innovation, broader interoperability and more rapid advances in physical AI.

**Developers Build on Cosmos**

The Cosmos platform powers NVIDIA’s physical AI stack to accelerate training and evaluation workflows across industries. The platform now includes new datasets for robotics, physics, human motion, autonomous driving, warehouse safety and spatial reasoning, as well as new [ physical AI agent skills](https://nvidianews.nvidia.com/news/nvidia-releases-major-collection-of-open-source-agent-tools-and-skills-for-physical-ai) for neural scene reconstruction, defect-image generation and video augmentation.

Physical AI developers are building on the Cosmos platform across industries — Agile Robots, Doosan Robotics, LG Electronics, Samsung Electronics and Skild AI for robotics, Li Auto for AVs, and [Centific](https://www.centific.com/blog/centific-brings-last-mile-physical-ai-to-production-with-nvidia-cosmos-3), [Fogsphere](https://fogsphere.com/fogsphere-announces-cosmos-3-support/), [ Linker Vision](https://www.linkervision.com/post/linker-vision-unveils-application-driven-ai-grid-for-agentic-video-reasoning-at-scale),

[Milestone Systems](https://www.milestonesys.com/resources/content/articles/milestone-hafnia-nvidia-cosmos-3/)and

[Yuan](https://www.yuan.com.tw/news/preview-news?id=336&t=d74eb353274d4fd78e460600ae11a561)for

[to power industrial AI and smart spaces applications.](https://www.nvidia.com/en-us/use-cases/video-analytics-ai-agents/)

__vision AI agents__**Availability**

Cosmos 3 Super and Cosmos 3 Nano are available now, with Cosmos 3 Edge coming soon for real-time inference. Developers can try Cosmos 3 on [ build.nvidia.com](https://build.nvidia.com/models?q=cosmos), download open models from

[, customize models and generate synthetic data with Hugging Face Diffusers and resources on](https://huggingface.co/collections/nvidia/cosmos3)

__Hugging Face__[, and deploy the models as](https://github.com/nvidia/Cosmos)

__GitHub__[™ microservices.](https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/)

__NVIDIA NIM__Model builders and software providers can accelerate access, customization and deployment of Cosmos for key reasoning and synthetic data generation workloads using physical AI agent skills on GitHub through inference services and cloud infrastructure partners including [Baseten](https://www.baseten.co/blog/nvidia-cosmos-3-robots-finally-take-over), [CoreWeave](https://wandb.ai/wandb_fc/nvidia-cosmos/reports/Build-a-Robotics-Data-Flywheel-on-CoreWeave-using-NVIDIA-Cosmos-3--VmlldzoxNzA3MzA2Ng), Microsoft Azure, [Nebius](https://nebius.com/blog/posts/run-physical-ai-workflows-not-glue-code%20Classmethod:%20https://dev.classmethod.jp/articles/dgx-spark-cosmos3-omni-world-model-policy/), Deep Infra and Classmethod.

*Watch the *__keynote__* from Huang, learn more at *__NVIDIA GTC Taipei__* and explore these *__physical AI sessions__*.*
