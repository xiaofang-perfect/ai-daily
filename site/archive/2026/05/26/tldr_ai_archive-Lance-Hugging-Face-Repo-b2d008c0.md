---
title: "Lance (Hugging Face Repo)"
source: TLDR AI · 2026-05-25
url: https://huggingface.co/bytedance-research/Lance?utm_source=tldrai
date: 2026-05-26
published_at: 2026-05-25T12:00:00+00:00
tag: 论文研究
item_id: b2d008c0f86cd7cc
---
Paper • 2605.18678 • Published • 74

![Lance logo](/bytedance-research/Lance/resolve/main/assets/logo/lance-logo.webp)

# Lance: Unified Multimodal Modeling by Multi-Task Synergy

[Fengyi Fu](https://scholar.google.com.hk/citations?user=FXxoQlsAAAAJ&hl=zh-CN&oi=ao)*,
[Mengqi Huang](https://corleone-huang.github.io/)*,✉,
[Shaojin Wu](https://scholar.google.com.hk/citations?user=9ER6nVkAAAAJ&hl=zh-CN&oi=ao)*,
Yunsheng Jiang*,
Yufei Huo,
[Jianzhu Guo](https://guojianzhu.com/)✉,§

Hao Li,
Yinghang Song,
Fei Ding,
Qian He,
Zheren Fu,
Zhendong Mao,
Yongdong Zhang

*ByteDance*

* Equal contribution
✉ Corresponding authors
§ Project lead


English | [简体中文](https://huggingface.co/Lance/blob/main/README_zh.md)

##
[
](https://huggingface.co#🌟-highlights)
🌟 Highlights

Lance is a lightweight native unified multimodal model that supports **image and video understanding, generation, and editing** within a single framework.

**Efficient at 3B scale.**With only**3B active parameters**, Lance delivers strong performance across image generation, image editing, and video generation benchmarks.**Trained from scratch.**Lance is built with a staged multi-task recipe and trained entirely from scratch within a**128-A100-GPU**budget.

![Lance benchmark overview across image generation, image editing, video generation, and video understanding](/bytedance-research/Lance/resolve/main/assets/benchmarks/benchmark-overview.png)

##
[
](https://huggingface.co#🎨-demo)
🎨 Demo

###
[
](https://huggingface.co#text-to-video)
Text-to-Video

![]() |

![](/bytedance-research/Lance/resolve/main/assets/text-to-video/previews/text-to-video-demo-02.gif)

![](/bytedance-research/Lance/resolve/main/assets/text-to-video/previews/text-to-video-demo-02.gif)

![](/bytedance-research/Lance/resolve/main/assets/text-to-video/previews/text-to-video-demo-03.gif)

![](/bytedance-research/Lance/resolve/main/assets/text-to-video/previews/text-to-video-demo-03.gif)

![](/bytedance-research/Lance/resolve/main/assets/text-to-video/previews/text-to-video-demo-04.gif)

![](/bytedance-research/Lance/resolve/main/assets/text-to-video/previews/text-to-video-demo-04.gif)

![](/bytedance-research/Lance/resolve/main/assets/text-to-video/previews/text-to-video-demo-05.gif)

![](/bytedance-research/Lance/resolve/main/assets/text-to-video/previews/text-to-video-demo-05.gif)

![](/bytedance-research/Lance/resolve/main/assets/text-to-video/previews/text-to-video-demo-06.gif)

![](/bytedance-research/Lance/resolve/main/assets/text-to-video/previews/text-to-video-demo-06.gif)

![](/bytedance-research/Lance/resolve/main/assets/text-to-video/previews/text-to-video-demo-07.gif)

![](/bytedance-research/Lance/resolve/main/assets/text-to-video/previews/text-to-video-demo-07.gif)

![](/bytedance-research/Lance/resolve/main/assets/text-to-video/previews/text-to-video-demo-08.gif)

![](/bytedance-research/Lance/resolve/main/assets/text-to-video/previews/text-to-video-demo-08.gif)

###
[
](https://huggingface.co#video-editing)
Video Editing

![]() |

![](/bytedance-research/Lance/resolve/main/assets/video-editing/previews/video-editing-demo-02.gif)

![](/bytedance-research/Lance/resolve/main/assets/video-editing/previews/video-editing-demo-02.gif)

![](/bytedance-research/Lance/resolve/main/assets/video-editing/previews/video-editing-demo-03.gif)

![](/bytedance-research/Lance/resolve/main/assets/video-editing/previews/video-editing-demo-03.gif)

![](/bytedance-research/Lance/resolve/main/assets/video-editing/previews/video-editing-demo-04.gif)

![](/bytedance-research/Lance/resolve/main/assets/video-editing/previews/video-editing-demo-04.gif)

![](/bytedance-research/Lance/resolve/main/assets/video-editing/previews/video-editing-demo-05.gif)

![](/bytedance-research/Lance/resolve/main/assets/video-editing/previews/video-editing-demo-05.gif)

![](/bytedance-research/Lance/resolve/main/assets/video-editing/previews/video-editing-demo-06.gif)

![](/bytedance-research/Lance/resolve/main/assets/video-editing/previews/video-editing-demo-06.gif)

![](/bytedance-research/Lance/resolve/main/assets/video-editing/previews/video-editing-demo-07.gif)

![](/bytedance-research/Lance/resolve/main/assets/video-editing/previews/video-editing-demo-07.gif)

![](/bytedance-research/Lance/resolve/main/assets/video-editing/previews/video-editing-demo-08.gif)

![](/bytedance-research/Lance/resolve/main/assets/video-editing/previews/video-editing-demo-08.gif)

###
[
](https://huggingface.co#multi-turn-consistency-editing)
Multi-turn Consistency Editing

###
[
](https://huggingface.co#intelligent-video-generation)
Intelligent Video Generation

![]() |

![](/bytedance-research/Lance/resolve/main/assets/intelligent-video/previews/intelligent-video-demo-02.gif)

![](/bytedance-research/Lance/resolve/main/assets/intelligent-video/previews/intelligent-video-demo-02.gif)

![](/bytedance-research/Lance/resolve/main/assets/intelligent-video/previews/intelligent-video-demo-03.gif)

![](/bytedance-research/Lance/resolve/main/assets/intelligent-video/previews/intelligent-video-demo-03.gif)

![](/bytedance-research/Lance/resolve/main/assets/intelligent-video/previews/intelligent-video-demo-04.gif)

![](/bytedance-research/Lance/resolve/main/assets/intelligent-video/previews/intelligent-video-demo-04.gif)

###
[
](https://huggingface.co#video-understanding)
Video Understanding

###
[
](https://huggingface.co#text-to-image-generation)
Text-to-Image Generation

![Lance text-to-image generation examples](/bytedance-research/Lance/resolve/main/assets/text-to-image/text-to-image-overview.webp)

###
[
](https://huggingface.co#image-editing)
Image Editing

![Lance image editing examples](/bytedance-research/Lance/resolve/main/assets/image-editing/image-editing-overview.webp)

###
[
](https://huggingface.co#image-understanding)
Image Understanding

![]()
|
![]()
|
![]()
|
![]()
|
![]()
|
![]()
|

##
[
](https://huggingface.co#🚀-installation)
🚀 Installation

###
[
](https://huggingface.co#recommended-environment)
Recommended Environment

**Software:**Python 3.10+, CUDA 12.4+ (required)**Hardware:**A GPU with at least 40GB VRAM is required for inference

We have tested the following dependency combinations on NVIDIA A100:

- PyTorch 2.8.0 + cu126 + flash-attn 2.8.3
- PyTorch 2.5.1 + cu124 + flash-attn 2.6.3

The default installation commands use the PyTorch 2.8.0 + cu126 setup. For other GPU models, please choose and validate a PyTorch build and a matching `flash-attn`

version according to your driver, CUDA runtime, Python version, and GPU architecture.

###
[
](https://huggingface.co#installation-steps)
Installation Steps

First, clone the repository:

```
git clone https://github.com/bytedance/Lance.git
cd Lance
```


Then, set up the environment:

```
conda create -n Lance python=3.11 -y
conda activate Lance
pip install torch==2.8.0 torchvision==0.23.0 torchaudio==2.8.0 --index-url https://download.pytorch.org/whl/cu126
pip install -r requirements.txt
pip install flash-attn==2.8.3 --no-build-isolation
```



Note:If installing`flash-attn`

from source fails, you can install a prebuilt wheel instead. The wheelhouse below is from a third-party repository and is provided forreference only; please verify that any wheel you install matches your Python, PyTorch and CUDA versions.

```
``````
pip install --no-cache-dir --no-deps --force-reinstall \
"https://huggingface.co/strangertoolshf/flash_attention_2_wheelhouse/resolve/main/wheelhouse-flash_attn-2.8.3/linux_x86_64/torch2.8/cu12/abiTRUE/cp311/flash_attn-2.8.3+cu12torch2.8cxx11abiTRUE-cp311-cp311-linux_x86_64.whl"
```



Then, download the model weights from [Lance-3B on Hugging Face](https://huggingface.co/bytedance-research/Lance) and place them in the `downloads/`

directory:

```
from huggingface_hub import snapshot_download
save_dir = "./downloads/"
repo_id = "bytedance-research/Lance"
cache_dir = save_dir + "/cache"
snapshot_download(cache_dir=cache_dir,
local_dir=save_dir,
repo_id=repo_id,
local_dir_use_symlinks=False,
resume_download=True,
allow_patterns=["*.json", "*.safetensors", "*.bin", "*.py", "*.md", "*.txt","*.pth",],
)
```


##
[
](https://huggingface.co#📚-usage)
📚 Usage

###
[
](https://huggingface.co#inference)
Inference

We provide a unified command-line interface for all generation / editing / understanding tasks:

####
[
](https://huggingface.co#option-1-configure-and-run-the-unified-script)
Option 1: Configure and Run the Unified Script

```
bash inference_lance.sh
```


- Before running, please configure the inference parameters at the top of
`inference_lance.sh`

. **Supported tasks:**`t2i`

,`t2v`

,`image_edit`

,`video_edit`

,`x2t_image`

, and`x2t_video`

. You can modify`TASK_DEFAULT_CONFIGS`

in`inference_lance.py`

to customize the default data samples for each task.**Note:**For all tasks, we recommend following the`prompt`

format used in the provided examples when writing input prompts, as this typically leads to better generation quality.

####
[
](https://huggingface.co#option-2-configure-and-run-the-unified-script)
Option 2: Configure and Run the Unified Script

We provide task-specific one-click commands for different generation, editing, and understanding tasks.

#####
[
](https://huggingface.co#text-to-video-generation)
Text-to-Video Generation

```
bash inference_lance.sh \
--TASK_NAME t2v \
--MODEL_PATH downloads/Lance_3B_Video \
--RESOLUTION video_480p \
--NUM_FRAMES 121 \
--VIDEO_HEIGHT 480 \
--VIDEO_WIDTH 848 \
--SAVE_PATH_GEN results/t2v
```


#####
[
](https://huggingface.co#text-to-image-generation-1)
Text-to-Image Generation

```
bash inference_lance.sh \
--TASK_NAME t2i \
--MODEL_PATH downloads/Lance_3B \
--RESOLUTION image_768res \
--VIDEO_HEIGHT 768 \
--VIDEO_WIDTH 768 \
--SAVE_PATH_GEN results/t2i
```


#####
[
](https://huggingface.co#video-editing-1)
Video Editing

```
bash inference_lance.sh \
--TASK_NAME video_edit \
--MODEL_PATH downloads/Lance_3B_Video \
--RESOLUTION video_480p \
--SAVE_PATH_GEN results/video_edit
```


#####
[
](https://huggingface.co#image-editing-1)
Image Editing

```
bash inference_lance.sh \
--TASK_NAME image_edit \
--MODEL_PATH downloads/Lance_3B \
--RESOLUTION image_768res \
--SAVE_PATH_GEN results/image_edit
```


#####
[
](https://huggingface.co#video-understanding-1)
Video Understanding

```
bash inference_lance.sh \
--TASK_NAME x2t_video \
--MODEL_PATH downloads/Lance_3B_Video \
--RESOLUTION video_480p \
--NUM_FRAMES 50 \
--SAVE_PATH_GEN results/x2t_video
```


#####
[
](https://huggingface.co#image-understanding-1)
Image Understanding

```
bash inference_lance.sh \
--TASK_NAME x2t_image \
--MODEL_PATH downloads/Lance_3B \
--RESOLUTION image_768res \
--SAVE_PATH_GEN results/x2t_image
```


####
[
](https://huggingface.co#available-tasks)
Available Tasks

| Task Name | Description | Example JSON |
|---|---|---|
`t2v` |
Text-to-Video generation | `config/examples/t2v_example.json` |
`t2i` |
Text-to-Image generation | `config/examples/t2i_example.json` |
`image_edit` |
Image editing | `config/examples/image_edit_example.json` |
`video_edit` |
Video editing | `config/examples/video_edit_example.json` |
`x2t_image` |
Image understanding | `config/examples/x2t_image_example.json` |
`x2t_video` |
Video understanding | `config/examples/x2t_video_example.json` |

For understanding examples:

`config/examples/x2t_image_example.json`

: image understanding examples for visual question answering and image-based reasoning.`config/examples/x2t_video_example.json`

: video understanding examples for video question answering and video captioning.

####
[
](https://huggingface.co#parameters)
Parameters

You can configure the following hyperparameters at the top of the `inference_lance.sh`

script:

| Parameter | Default Value | Description |
|---|---|---|
`MODEL_PATH` |
`"downloads/lance_3b"` |
Path to the downloaded Lance model weights. |
`NUM_GPUS` |
`1` |
Number of GPUs to use for inference. |
`VALIDATION_NUM_TIMESTEPS` |
`30` |
Number of denoising steps (e.g., 30 or 50). |
`VALIDATION_TIMESTEP_SHIFT` |
`3.5` |
Timestep shift parameter for flow matching scheduling. |
`CFG_TEXT_SCALE` |
`4.0` |
Classifier-Free Guidance (CFG) scale for text conditioning. |
`VALIDATION_DATA_SEED` |
`42` |
Random seed for generation reproducibility. |
`NUM_FRAMES` |
`50` |
Number of frames for video generation (Max: 121). Unused for image tasks. |
`VIDEO_HEIGHT` / `VIDEO_WIDTH` |
`768` |
Spatial resolution. Unused for editing tasks (determined by input image/video). |
`RESOLUTION` |
`"video_480p"` |
Base resolution preset (`image_768res` or `video_480p` ). |

###
[
](https://huggingface.co#gradio)
Gradio

```
python lance_gradio_t2v_v2t.py --gpus 0 --server-port 7860
```


###
[
](https://huggingface.co#benchmarks)
Benchmarks

####
[
](https://huggingface.co#dpg-bench-evaluation)
DPG-Bench Evaluation

| Models | # Params. | Global | Entity | Attribute | Relation | Other | Overall |
|---|---|---|---|---|---|---|---|
Generation-only Models |
|||||||
| SDXL | 3.5B | 83.27 | 82.43 | 80.91 | 86.76 | 80.41 | 74.65 |
| DALL-E 3 | - | 90.97 | 89.61 | 88.39 | 90.58 | 89.83 | 83.50 |
| SD3-Medium | 2B | 87.90 | 91.01 | 88.83 | 80.70 | 88.68 | 84.08 |
| FLUX.1-dev | 12B | 74.35 | 90.00 | 88.96 | 90.87 | 88.33 | 83.84 |
| Qwen-Image | 20B | 91.32 | 91.56 | 92.02 | 94.31 | 92.73 | 88.32 |
Unified Models |
|||||||
| Janus-Pro-7B | 7B | 86.90 | 88.90 | 89.40 | 89.32 | 89.48 | 84.19 |
| OmniGen2 | 4B | 88.81 | 88.83 | 90.18 | 89.37 | 90.27 | 83.57 |
| Show-o2 | 7B | 89.00 | 91.78 | 89.96 | 91.81 | 91.64 | 86.14 |
BAGEL† | 7B | 88.94 | 90.37 | 91.29 | 90.82 | 88.67 | 85.07 |
| InternVL-U | 1.7B | 90.39 | 90.78 | 90.68 | 90.29 | 88.77 | 85.18 |
| TUNA | 7B | 90.42 | 91.68 | 90.94 | 91.87 | 90.73 | 86.76 |
| TUNA-2 | 7B | 89.50 | 91.40 | 92.07 | 91.91 | 88.81 | 86.54 |
🌟 Lance (Ours) | 3B | 83.89 | 91.07 | 89.36 | 93.38 | 80.80 | 84.67 |

† indicates methods that use LLM rewriters for prompt rewriting before generation.

####
[
](https://huggingface.co#geneval-evaluation)
GenEval Evaluation

| Models | # Params. | 1-Obj. | 2-Obj. | Count | Colors | Position | Attr. | Overall |
|---|---|---|---|---|---|---|---|---|
Generation-only Models |
||||||||
| SDXL | 3.5B | 0.98 | 0.74 | 0.39 | 0.85 | 0.15 | 0.23 | 0.55 |
| DALL-E 3 | - | 0.96 | 0.87 | 0.47 | 0.83 | 0.43 | 0.45 | 0.67 |
| SD3-Medium | 2B | 0.99 | 0.94 | 0.72 | 0.89 | 0.33 | 0.60 | 0.74 |
| FLUX.1-dev | 12B | 0.98 | 0.93 | 0.75 | 0.93 | 0.68 | 0.65 | 0.82 |
| Qwen-Image | 20B | 0.99 | 0.92 | 0.89 | 0.88 | 0.76 | 0.77 | 0.87 |
Unified Models |
||||||||
| Janus-Pro-7B | 7B | 0.99 | 0.89 | 0.59 | 0.90 | 0.79 | 0.66 | 0.80 |
| OmniGen2 | 4B | 1.00 | 0.95 | 0.64 | 0.88 | 0.55 | 0.76 | 0.80 |
| Show-o2 | 7B | 1.00 | 0.87 | 0.58 | 0.92 | 0.52 | 0.62 | 0.76 |
BAGEL† | 7B | 0.98 | 0.95 | 0.84 | 0.95 | 0.78 | 0.77 | 0.88 |
| Mogao | 7B | 1.00 | 0.97 | 0.83 | 0.93 | 0.84 | 0.80 | 0.89 |
| InternVL-U | 1.7B | 0.99 | 0.94 | 0.74 | 0.91 | 0.77 | 0.74 | 0.85 |
| TUNA | 7B | 1.00 | 0.97 | 0.81 | 0.91 | 0.88 | 0.83 | 0.90 |
| TUNA-2 | 7B | 0.99 | 0.96 | 0.80 | 0.91 | 0.84 | 0.76 | 0.87 |
🌟 Lance (Ours) | 3B | 1.00 | 0.94 | 0.84 | 0.97 | 0.87 | 0.81 | 0.90 |

† indicates methods that use LLM rewriters for prompt rewriting before generation.

####
[
](https://huggingface.co#gedit-bench-evaluation)
GEdit-Bench Evaluation

| Models | # Params. | BC | CA | MM | MC | PB | ST | SA | SR | SRp | TM | TT | Avg/G_O |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
Generation-only Models |
|||||||||||||
| Gemini 2.0 | - | - | - | - | - | - | - | - | - | - | - | - | 6.32 |
| GPT Image 1 | - | 6.96 | 6.85 | 7.10 | 5.41 | 6.74 | 7.44 | 7.51 | 8.73 | 8.55 | 8.45 | 8.69 | 7.49 |
| Qwen-Image-Edit | 20B | 8.23 | 8.30 | 7.33 | 8.05 | 7.49 | 6.74 | 8.57 | 8.09 | 8.29 | 8.48 | 8.50 | 8.01 |
Unified Models |
|||||||||||||
| Lumina-DiMOO | 8B | 3.43 | 4.27 | 3.08 | 2.77 | 4.74 | 5.19 | 4.44 | 3.80 | 4.38 | 2.68 | 4.20 | 3.91 |
| Ovis-U1 | 1.2B | 7.49 | 6.88 | 6.21 | 4.79 | 5.98 | 6.46 | 7.49 | 7.25 | 7.27 | 4.48 | 6.31 | 6.42 |
| BAGEL | 7B | 7.32 | 6.91 | 6.38 | 4.75 | 4.57 | 6.15 | 7.90 | 7.16 | 7.02 | 7.32 | 6.22 | 6.52 |
| InternVL-U | 1.7B | 7.08 | 7.05 | 6.38 | 7.02 | 6.03 | 6.27 | 7.13 | 6.55 | 6.33 | 6.59 | 6.85 | 6.66 |
| InternVL-U (w/ CoT) | 1.7B | 7.05 | 7.87 | 6.50 | 6.99 | 5.77 | 6.10 | 7.33 | 7.16 | 7.12 | 7.36 | 6.46 | 6.88 |
🌟 Lance (Ours) | 3B | 7.73 | 7.74 | 7.28 | 7.83 | 7.50 | 7.03 | 7.64 | 7.85 | 7.71 | 4.46 | 7.57 | 7.30 |

####
[
](https://huggingface.co#vbench-evaluation-video-generation)
VBench Evaluation (Video Generation)

| Type | Model | # Params. | Total Score ↑ |
|---|---|---|---|
Gen. Only |
ModelScope | 1.7B | 75.75 |
| LaVie | 3B | 77.08 | |
| Show-1 | 6B | 78.93 | |
| AnimateDiff-V2 | - | 80.27 | |
| VideoCrafter-2.0 | - | 80.44 | |
| CogVideoX | 5B | 81.61 | |
| Kling | - | 81.85 | |
| Open-Sora-2.0 | - | 81.71 | |
| Gen-3 | - | 82.32 | |
| Step-Video-T2V | 30B | 81.83 | |
| Hunyuan Video | - | 83.43 | |
| Wan2.1-T2V | 14B | 83.69 | |
Unified |
HaproOmni | 7B | 78.10 |
| Emu3 | 8B | 80.96 | |
| VILA-U | 7B | 74.01 | |
| Show-o2 | 2B | 81.34 | |
| TUNA | 1.5B | 84.06 |
|
🌟 Lance (Ours) | 3B | 85.11 |

####
[
](https://huggingface.co#running-benchmarks)
Running Benchmarks

Ready-to-run benchmark scripts are provided under `benchmarks/`

:

| Benchmark | Modality | Script |
|---|---|---|
| GenEVAL (image gen) | Image | `benchmarks/image_gen/GenEVAL/sample_GenEVAL.sh` |
| DPG (image gen) | Image | `benchmarks/image_gen/DPG/sample_DPG.sh` |
| GEdit (image edit) | Image | `benchmarks/image_gen/GEdit/sample_GEdit.sh` |
| VBench (video gen) | Video | `benchmarks/video_gen/Vbench/sample_vbench.sh` |

##
[
](https://huggingface.co#📄-license)
📄 License

Copyright 2025 Bytedance Ltd. and/or its affiliates.

##
[
](https://huggingface.co#🙏-acknowledgements)
🙏 Acknowledgements

We would like to thank the contributors of [BAGEL](https://github.com/ByteDance-Seed/bagel), [Qwen2.5-VL-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct), and [Wan2.2](https://github.com/Wan-Video/Wan2.2) for their open research and contributions.

##
[
](https://huggingface.co#💖-citation)
💖 Citation

If you find **Lance** useful for your project or research, welcome to 🌟 this repo and cite our work using the following BibTeX:

```
@misc{lance2026,
title = {Lance: Unified Multimodal Modeling by Multi-Task Synergy},
author = {Fengyi Fu and Mengqi Huang and Shaojin Wu and Yunsheng Jiang and Yufei Huo and Jianzhu Guo and Hao Li and Yinghang Song and Fei Ding and Qian He and Zheren Fu and Zhendong Mao and Yongdong Zhang},
year = {2026},
note = {Manuscript}
}
```


##
[
](https://huggingface.co#📞-contact)
📞 Contact

For questions, issues, or collaborations, please contact [Mengqi Huang](https://corleone-huang.github.io/) and [Jianzhu Guo](https://guojianzhu.com/).

- Downloads last month
- 1,679

[NEW](https://huggingface.co/docs/inference-providers)

[🙋 17 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/9942)

## Model tree for bytedance-research/Lance

Base model

[Qwen/Qwen2.5-VL-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct)

## Spaces using bytedance-research/Lance 5


bytedance-research/Lance

![](https://cdn-avatars.huggingface.co/v1/production/uploads/6535c9e88bde2fae19b6fb25/7a1zq0juEwFJVCIShnLI-.png)

[🚀 victor/lance-zerogpu-demo ](https://huggingface.co/spaces/victor/lance-zerogpu-demo)

[🐨 Nayefleb/Lance ](https://huggingface.co/spaces/Nayefleb/Lance)

[🎬 zontos/Lance ](https://huggingface.co/spaces/zontos/Lance)

[🎬 Daankular/Lance ](https://huggingface.co/spaces/Daankular/Lance)
