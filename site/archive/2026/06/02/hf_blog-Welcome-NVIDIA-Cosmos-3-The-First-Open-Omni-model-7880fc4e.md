---
title: "Welcome NVIDIA Cosmos 3: The First Open Omni-model for Physical AI Reasoning and Action"
source: HuggingFace Blog
url: https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai
date: 2026-06-02
published_at: 2026-06-01T04:44:55+00:00
tag: 工具开源
item_id: 7880fc4ecdc09e67
---
16B • Updated • 6.26k • 84

![](https://cdn-avatars.huggingface.co/v1/production/uploads/65df9200dc3292a8983e5017/Vs5FPVCH-VZBipV3qKTuy.png)

Whether you're building for robotics, autonomous vehicles, or smart spaces, Cosmos 3 gives you the foundation to simulate and understand the physical world.

Here's what's shipping with this release:

- Cosmos 3 Super and Cosmos 3 Nano on Hugging Face with model cards and licensing
- Cosmos 3 Diffusers integration for generation pipelines
- Post-training scripts for training Cosmos 3 on your own data (on GitHub)
- Open synthetic data generation (SDG) datasets for physical AI

**TABLE OF CONTENTS**

[What's new with Cosmos 3?](https://huggingface.co#section-1-whats-new-with-cosmos-3)[Cosmos 3 Capabilities](https://huggingface.co#section-2-cosmos-3-capabilities)[Using Cosmos 3 with Diffusers](https://huggingface.co#section-3-using-cosmos-3-with-diffusers)[Datasets for physical AI](https://huggingface.co#section-4-datasets-for-physical-ai)[Cosmos Framework](https://huggingface.co#section-5-cosmos-framework)[Resources](https://huggingface.co#section-6-resources)

The biggest change in Cosmos 3 compared to previous Cosmos releases is that it's an omni-model, built on a Mixture-of-Transformers (MoT) architecture. Previously, developers had to work with separate models for different capabilities like world generation (Cosmos Predict), controlled generation (Cosmos Transfer), scene understanding (Cosmos Reason) and policy generation (Cosmos Policy). Cosmos 3 enables all of this in a single model that can reason and generate different modalities in one unified forward pass.

This means you can now do all this from one model:

- Generate realistic and physically plausible video worlds from text, images, videos or action inputs
- Reason about physical properties like motion, causality, and spatial relationships
- Predict future video and action sequences based on the current state

**Why this matters for physical AI**

Cosmos 3 helps build physical AI systems capable of understanding the real world. Not just pixels and tokens, but motion, causality, physics, and action. If you're training a robot to fold laundry, building an autonomous driving simulation, or generating synthetic training data for warehouse safety scenarios, Cosmos 3 is the foundation model designed for exactly these use-cases.

![](https://cdn-uploads.huggingface.co/production/uploads/6799309995f2227228bc38f3/Wcx8G3cD6e3tib-Zj4Ryw.gif)


![](https://cdn-uploads.huggingface.co/production/uploads/6799309995f2227228bc38f3/FP6Mh3FqTyThuZ_RN4mt4.gif)


![](https://cdn-uploads.huggingface.co/production/uploads/6799309995f2227228bc38f3/WgIJWLbDhavkxYV8mBYjh.gif)


![](https://cdn-uploads.huggingface.co/production/uploads/6799309995f2227228bc38f3/g06bFosM9Br-cwgfmt7cl.png)


**Architecture**

Cosmos 3 is built on an MoT backbone that processes all modalities - text, image, video, audio, and action - within a single unified architecture. Each modality is first encoded by a dedicated encoder (a ViT for visual understanding, a VAE for visual/audio generation, and domain-aware vectors for actions), then projected into a shared representation space.

The input sequence is split into two subsequences: an autoregressive (AR) subsequence that handles reasoning and understanding via next-token prediction, and a diffusion (DM) subsequence that handles generation via iterative denoising. AR and DM tokens use separate parameter sets within each transformer layer but interact through joint attention - this is what lets a single model seamlessly switch between acting as a VLM, a video generator, a forward/inverse dynamics model, or a robot policy without any architectural changes.

**Model Versions**

This release of Cosmos 3 includes two model sizes, optimized for different deployment scenarios:

**Cosmos 3 Nano**- This is the 16B parameter model (8B reasoner and 8B generator), optimized for efficient inference. Cosmos 3 Nano is designed to run on workstation-grade compute like the RTX PRO 6000 GPU, and is available on Hugging Face at[nvidia/Cosmos3-Nano](http://huggingface.co/nvidia/Cosmos3-Nano).**Cosmos 3 Super**- This is the 64B parameter model (32B reasoner and 32B generator) designed for large-scale synthetic data generation (SDG) and research, and runs on NVIDIA Hopper and Blackwell GPUs. Cosmos 3 Super is available on Hugging Face at[nvidia/Cosmos3-Super](http://huggingface.co/nvidia/Cosmos3-Super).

Cosmos 3 supports multiple input and generation modalities through a single unified model:

Input Modality |
Output Modality |
Application |
|---|---|---|
| Text | Image | Video | Video | Video Model |
| Text | Video | Text | Vision Language Model (VLM) |
| Action | Image | Text | Video | Forward Dynamics Model |
| Text | Video | Action | Inverse Dynamics Model |
| Image | Text | Video & Action | Policy Model |

**Prompt Guide**

For video generation, we recommend using detailed prompts in the form of narrative paragraphs. For example:

The video begins with a view from inside a vehicle traveling on a multi-lane highway under a clear blue sky. The road is bordered by dense green trees on both sides, creating a tranquil environment. Several vehicles, including a prominent white semi-truck and various cars, are visible ahead, maintaining a steady pace. The highway features multiple lanes separated by concrete barriers, and the scene is bathed in bright sunlight, indicating a clear day. As the video progresses, a large amount of debris suddenly appears on the lane ahead. With little time to avoid it, the ego vehicle has to drive over the debris and continue moving forward. A noticeable jolt occurs as the ego vehicle passes over the scattered objects. A point-of-view shot from inside the vehicle, capturing the road ahead and the surrounding environment.


For action generation, prompts should be concise and provide spatial references. For example:

Put the pot to the left of the purple item. This video is captured from a first-person perspective looking at the scene.


Find the prompt upsampling template, and best practices for writing high-quality prompts in the prompting guide on GitHub.

Cosmos 3 is integrated with the Hugging Face Diffusers library, making it easy to use world generation pipelines with just a few lines of code. You can run Cosmos 3 through the familiar DiffusionPipeline via *Cosmos3OmniPipeline*. With this, the goal is enabling frictionless adoption of Cosmos 3 and integration with your existing pipelines.

Let's see a Text-to-Image example for single frame generation using the Cosmos 3 Nano model:

```
import torch
from diffusers import Cosmos3OmniPipeline
pipe = Cosmos3OmniPipeline.from_pretrained(
"nvidia/Cosmos3-Nano", torch_dtype=torch.bfloat16, device_map="cuda"
)
prompt = (
"A medium shot of a modern robotics research laboratory with white walls and a gray floor. "
"A robotic arm with a metallic finish is mounted on a clean white workbench, its gripper positioned "
"above a row of small colored objects. A laptop and neatly arranged tools sit beside the robot. "
"A large monitor on the wall behind displays a software interface. The scene is brightly lit by "
"overhead fluorescent lights."
)
result = pipe(prompt=prompt, num_frames=1, height=720, width=1280)
result.video[0].save("cosmos3_t2i.jpg", format="JPEG", quality=85)
```


Here's the image generated by the Cosmos 3 Nano model and given prompt:

![](https://cdn-uploads.huggingface.co/production/uploads/6799309995f2227228bc38f3/J7F5Kov02E21Tx1A21ZcB.jpeg)


The documentation also has examples on Text-to-Video, Image-to-Video and more. Find information and API usage in the [Cosmos 3 Diffusers documentation](https://huggingface.co/docs/diffusers/main/en/api/pipelines/cosmos3).

As part of the Cosmos 3 launch, NVIDIA is releasing a set of Synthetic Data Generation (SDG) datasets to help the physical AI community train and evaluate world foundation models. These datasets were generated by various NVIDIA teams and are available on Hugging Face.

Dataset |
Domain |
Description |
|---|---|---|
|

[Cosmos Framework](https://github.com/NVIDIA/Cosmos-Framework) is an end-to-end framework for training and serving WFMs like Cosmos 3. This is where you'll find inference and post-training scripts, and agent skills for development.

**Post-training Cosmos 3**

Cosmos 3 understands and generates world videos and actions for robotics, autonomous vehicles, and smart spaces out of the box, but some applications may require further post-training on specific datasets to get the best results. We encourage post-training Cosmos 3 for different robots, environments, and tasks - check out the post-training guide in the repo.

**Agent Skills**

The repo also comes with agent skills to make development fast and easy. These skills help validate requirements, and set up the environment with dependencies. You can also use them for learning about the repo structure and examples, drafting good prompts, or running the inference and post-training scripts.

Read the [Cosmos 3 technical blog](https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3) to learn about Cosmos 3 capabilities, performance, post-training, and deployment with NIM microservices.

[Cosmos 3 GitHub](https://github.com/nvidia/Cosmos)[Cosmos 3 NIM microservices](https://build.nvidia.com/models?q=cosmos)[Cosmos Cookbook](https://nvidia-cosmos.github.io/cosmos-cookbook/)[Cosmos Page](https://www.nvidia.com/en-us/ai/cosmos/)[Cosmos 3 Technical Paper](https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf)[Diffusers Cosmos Documentation](https://huggingface.co/docs/diffusers/main/en/api/pipelines/cosmos3)

Cosmos 3 is the result of amazing collaboration between many teams and people across NVIDIA, including -

Adeline Aubame, Aditya Mahajan, Aigul Dzhumamuratova, Akash Gokul, Akul Santhosh, Aleksandr Efitorov, Alex Sotelo, Alexander Schwarz, Alperen Degirmenci, Amol Fasale, Andrew Tham, Ankur Handa, Arihant Jain, Arslan Ali, Artur Zolkowski, Aryaman Gupta, Asawaree Bhide, Ashkan Mirzaei, Ashley Chow, Ashna Khetan, Atharva Joshi, Barnaby Simkin, Benedikt Falk, Brett Hamilton, Carlos Casanova, Chaeyeon Chung, Charles Zhou, Chen-Hsan Lin, Chen-Hsuan Lin, Chhavi Nijhawan, Chieh-Yun Chen, Chintan Shah, Chris Helvig, Chris Pruett, Cindy Zha, Cyrus Hogg, Dahjung Chung, Dan Blick, David Wehr, Dawid Majchrowski, DeLesley Hutchins, Delin Qu, Dennis Lynch, Diego Garzon, Dima Zhylko, Durra Mohsin, Egor Krivov, Ekram Mukbil, Eric Cameracci, Fangyin Wei, Fengzhe Zhou, Francesco Ferroni, Freya Li, George Kurian, Gwanghyun Kim, Haaland Hao Liang, Hai Loc Lu, Hans Yang, Hao Liang, Hao Wang, Hesam Rabeti, Hugo Hadfield, Hyejin Moon, Itai Zadok, Jayjun Lee, Jeana Choi, JF Lafleche, Jiangran Lyu, Jiaojiao Fan, Jiaxiang Tang, Jibin Varghese, Jim Fan, Jingyi Jin, Jinwei Gu, Jon Allen, Joshua Bapst, Joyjit Daw, Julia Kiczka, Julian Ouyang, Kaichun Mo, Kayley Ting, Ke Ding, Kedi Wu, Kevin Brady, Kirill Motkov, Kristen Rumley, Krzysztof Tomala, Liang Feng, Liangkai Zhang, Ling Li, Louis Marcoux, Maciej Bala, Madison Huang, Magdalena Dadela, Mahesh Patekar, Marco Di Lucca, Marilyn Reeb, Mark Carlson, Martin Antolini, Mateusz Sieniawski, Matt Cragun, Meredith Price, Michael Huang, Miguel Guerrero, Miguel Martin, Min Shi, Ming-Yu Liu, Mohammad Harrim, Morteza Ramezanali, Mukesh Beladiya, Nalin Dadhich, Naomi Eigbe, Nathan Hayes-Roth, Nicole Drumheller, Nikhilesh Joshi, Omar Laymoun, Paris Zhang, Paula Ramos, Pawel Morkisz, Peter Gambrill, Pooya Jannaty, Pooya Khaloo, Pranjali Joshi, Qi Wang, Qianli Ma, Qiao Wang, Qing Miao, Qizhi Chen, Rahul Heinrich Steiger, Raju Wagwani, Robert Denomme, Rodrigo Vieira Del Monte, Roy Anthony, Ruqing Xu, Ryan Bernard, Ryan Ji, Saeid Motiian, Sandip Bhaskar, Sandra Skaff, Santanu Dutta, Saurav Kumar, Sehwi Park, Sergiy Fefilatyev, Shangkun Sun, Shangru Li, Shilin Zhu, Shreyas Misra, Shun Zhang, Shuran Song, Simon Yuen, Simon Zhang, Slawek Kierat, Smita Ithape, Soha Pouya, Sophia Huang, Stefanie Manzinger, Steven Baughman, Suneel Indupuru, Sunil Srinivasa, Sunny Kim, Tavish Chen, Thabang Ngazimbi, Thomas Volk, Tianwei She, Tiffany Cai, Ting-Chun Wang, TJ Galda, Tolou Tavakkoli, Tomasz Kornuta, Trung Pham, Tsung-Yi Lin, Vanni Brighella, Varun Praveen, Wei-Cheng Tseng, Wenjie Luo, Wesley Li, Wojciech Kutak, Wojciech Rymer, Xiangyu Lu, Xiaodong Yang, Xiaotong Chen, Xin Kong, Xinquan Xu, Xiu Chia, Xuning Yang, Yan Chang, Yan Wang, Yanan Jian, Yao Xu, Yashraj Narang, Yeongho Seol, Yichu Yang, Yifan Ding, Yihuai Gao, Yilin Zhao, Yin Cui, Yogesh Balaji, Yu Wang, Yu-Wei Chao, Yue Tang, Yufan Huang, Yuke Zhu, Yuliya Zhautouskaya, Yurong You, Yuzhu Dong, Zaid Pervaiz Bhat, Zekun Hao, Zhaoshuo Li, Zhizheng Zhang.

16B • Updated • 6.26k • 84

65B • Updated • 2.11k • 69
