---
title: "Multimodal 3D World Model (GitHub Repo)"
source: TLDR AI · 2026-04-20
url: https://github.com/Tencent-Hunyuan/HY-World-2.0?utm_source=tldrai
date: 2026-04-21
published_at: 2026-04-20T12:00:00+00:00
tag: 工具开源
item_id: fc2812196519b735
---
*"What Is Now Proved Was Once Only Imagined"*

## hyworld2_en.mp4

**[April 16, 2026]**: 🚀 Release HY-World 2.0 technical report & partial codes!**[April 16, 2026]**: 🤗 Open-source WorldMirror 2.0 inference code and model weights!**[Coming Soon]**: Release Full HY-World 2.0 (World Generation) inference code.**[Coming Soon]**: Release(HY-Pano 2.0) model weights & code.**[Coming Soon]**: Release（WorldNav） code.**[Coming Soon]**: Release(WorldStereo 2.0) model weights & inference code.

[📖 Introduction](https://github.com#-introduction)[✨ Highlights](https://github.com#-highlights)[🧩 Architecture](https://github.com#-architecture)[📝 Open-Source Plan](https://github.com#-open-source-plan)[🎁 Model Zoo](https://github.com#-model-zoo)[🤗 Get Started](https://github.com#-get-started)[🔮 Performance](https://github.com#-performance)[🎬 More Examples](https://github.com#-more-examples)[📚 Citation](https://github.com#-citation)

**HY-World 2.0** is a multi-modal world model framework for **world generation** and **world reconstruction**. It accepts diverse input modalities — text, single-view images, multi-view images, and videos — and produces 3D world representations (meshes / Gaussian Splattings). It offers two core capabilities:

**World Generation**(text / single image → 3D world): syntheses high-fidelity, navigable 3D scenes through a four-stage method —— a)with HY-Pano 2.0, b)with WorldNav, c)with WorldStereo 2.0, and d)with WorldMirror 2.0 & 3DGS learning.**World Reconstruction**(multi-view images / video → 3D): Powered by WorldMirror 2.0, a unified feed-forward model that simultaneously predicts depth, surface normals, camera parameters, 3D point clouds, and 3DGS attributes in a single forward pass.

HY-World 2.0 is an **open-source state-of-the-art** world model. We will release all model weights, code, and technical details to facilitate reproducibility and advance research in this field.

Existing world models, such as Genie 3, Cosmos, and HY-World 1.5 (WorldPlay+WorldCompass), generate pixel-level videos — essentially "watching a movie" that vanishes once playback ends. **HY-World 2.0 takes a fundamentally different approach**: it directly produces editable, persistent 3D assets (meshes / 3DGS) that can be imported into game engines like Blender/Unity/Unreal Engine/Isaac Sim — more like "building a playable game" than recording a clip. This paradigm shift natively resolves many long-standing pain points of video world models:

| Video World Models | 3D World Model (HY-World 2.0) | |
|---|---|---|
Output |
Pixel videos (non-editable) | Real 3D assets — meshes / 3DGS (fully editable) |
Playable Duration |
Limited (typically 1 min) | Unlimited — assets persist permanently |
3D Consistency |
No (flickering, artifacts across views) | Native — inherently consistent in 3D |
Real-Time Rendering |
Requires per-frame inference; high latency | Consumer GPUs can render in real time |
Controllability |
Weak (imprecise character control, no real physics) | Precise — zero-error control, real physics collision, accurate lighting |
Inference Cost |
Accumulates with every interaction | One-time generation; rendering cost ≈ 0 |
Engine Compatibility |
✗ Video files only | ✓ Directly importable into Blender / UE / Isaac Engine |

![]() |

![](/Tencent-Hunyuan/HY-World-2.0/raw/main/assets/screenshot_2.gif)

![](/Tencent-Hunyuan/HY-World-2.0/raw/main/assets/screenshot_2.gif)

![](/Tencent-Hunyuan/HY-World-2.0/raw/main/assets/screenshot_7.gif)

![](/Tencent-Hunyuan/HY-World-2.0/raw/main/assets/screenshot_7.gif)

![](/Tencent-Hunyuan/HY-World-2.0/raw/main/assets/screenshot_8.gif)

![](/Tencent-Hunyuan/HY-World-2.0/raw/main/assets/screenshot_8.gif)

*All above are real 3D assets (not generated videos) and entirely created by HY-World 2.0 -- captured from live real-time interaction.*

-
**Real 3D Worlds, Not Just Videos**Unlike video-only world models (e.g., Genie 3, HY World 1.5), HY-World 2.0 generates

**real 3D assets**— 3DGS, meshes, and point clouds — that are freely explorable, editable, and directly importable into**Unity / Unreal Engine / Isaac**. From a single text prompt or image, create navigable 3D worlds with diverse styles: realistic, cartoon, game, and more.

-
**Instant 3D Reconstruction from Photos & Videos**Powered by

**WorldMirror 2.0**, a unified feed-forward model that predicts dense point clouds, depth maps, surface normals, camera parameters, and 3DGS from multi-view images or casual videos in a single forward pass. Supports flexible-resolution inference (50K–500K pixels) with SOTA accuracy. Capture a video, get a digital twin.

-
**Interactive Character Exploration**Go beyond viewing —

**play inside your generated worlds**. HY-World 2.0 supports first-person navigation and third-person character mode, enabling users to freely explore AI-generated streets, buildings, and landscapes with physics-based collision. Go to[our product page](https://3d.hunyuan.tencent.com/sceneTo3D)for free try ().

-
**Refer to our tech report for more details**A systematic pipeline of HY-World 2.0 —

*Panorama Generation*(HY-Pano-2.0) →*Trajectory Planning*(WorldNav) →*World Expansion*(WorldStereo 2.0) →*World Composition*(WorldMirror 2.0 + Splattings Learning) — that automatically transforms text or a single image into a high-fidelity, navigable 3D world (3DGS/mesh outputs).

- ✅ Technical Report
- ✅ WorldMirror 2.0 Code & Model Checkpoints
- ⬜ Full Inference Code for World Generation (WorldNav + World Composition)
- ⬜ Panorama Generation (HY-Pano 2.0) Model & Code —
[HunyuanWorld 1.0](https://github.com/Tencent-Hunyuan/HunyuanWorld-1.0)available as interim alternative - ⬜ World Expansion (WorldStereo 2.0) Model & Code —
[WorldStereo](https://github.com/FuchengSu/WorldStereo)available as interim alternative

| Model | Description | Params | Date | Hugging Face |
|---|---|---|---|---|
| WorldMirror-2 [new] | Multi-view / video → 3D reconstruction | ~1.2B | 2026 |
|

[Download](https://huggingface.co/tencent/HunyuanWorld-Mirror/tree/main)| Model | Description | Params | Date | Hugging Face |
|---|---|---|---|---|
| HY-Pano-2 [new] | Text / image → 360° panorama | — | Coming Soon | — |

| Model | Description | Params | Date | Hugging Face |
|---|---|---|---|---|
| WorldStereo-2 [new] | Panorama → 3DGS world | — | Coming Soon | — |

| Algorithm | Description | Params | Date |
|---|---|---|---|
| WorldNav [new] | Panorama → Camera Traj. | — | Coming Soon |

We recommend referring to our previous works, [WorldStereo](https://github.com/FuchengSu/WorldStereo) and [WorldMirror](https://github.com/Tencent-Hunyuan/HunyuanWorld-Mirror), for background knowledge on 3D world generation and reconstruction.

We recommend CUDA 12.4 for installation.

```
# 1. Clone the repository
git clone https://github.com/Tencent-Hunyuan/HY-World-2.0
cd HY-World-2.0
# 2. Create conda environment
conda create -n hyworld2 python=3.10
conda activate hyworld2
# 3. Install PyTorch (CUDA 12.4)
pip install torch==2.4.0 torchvision==0.19.0 --index-url https://download.pytorch.org/whl/cu124
# 4. Install dependencies
pip install -r requirements.txt
# 5. Install FlashAttention
# (Recommended) Install FlashAttention-3
git clone https://github.com/Dao-AILab/flash-attention.git
cd flash-attention/hopper
python setup.py install
cd ../../
rm -rf flash-attention
# For simpler installation, you can also use FlashAttention-2
pip install flash-attn --no-build-isolation
```

*Coming soon.*

*Coming soon.*

**We recommend referring to our previous work, WorldStereo, for the open-source preview version of WorldStereo-2.**

WorldMirror 2.0 supports the following usage modes:

We provide a `diffusers`

-like Python API for WorldMirror 2.0. Model weights are automatically downloaded from Hugging Face on first run.

```
from hyworld2.worldrecon.pipeline import WorldMirrorPipeline
pipeline = WorldMirrorPipeline.from_pretrained('tencent/HY-World-2.0')
result = pipeline('path/to/images')
```

**With Prior Injection (Camera & Depth):**

```
result = pipeline(
'path/to/images',
prior_cam_path='path/to/prior_camera.json',
prior_depth_path='path/to/prior_depth/',
)
```

For the detailed structure of camera/depth priors and how to prepare them, see

[Prior Preparation Guide].

**CLI:**

```
# Single GPU
python -m hyworld2.worldrecon.pipeline --input_path path/to/images
# Multi-GPU
torchrun --nproc_per_node=2 -m hyworld2.worldrecon.pipeline \
--input_path path/to/images \
--use_fsdp --enable_bf16
```


Important:In multi-GPU mode, the number of input images must be>= the number of GPUs. For example, with`--nproc_per_node=8`

, provide at least 8 images.

We provide an interactive [Gradio](https://www.gradio.app/) web demo for WorldMirror 2.0. Upload images or videos and visualize 3DGS, point clouds, depth maps, normal maps, and camera parameters in your browser.

```
# Single GPU
python -m hyworld2.worldrecon.gradio_app
# Multi-GPU
torchrun --nproc_per_node=2 -m hyworld2.worldrecon.gradio_app \
--use_fsdp --enable_bf16
```

For the full list of Gradio app arguments (port, share, local checkpoints, etc.), see [DOCUMENTATION.md](https://github.com/Tencent-Hunyuan/HY-World-2.0/blob/main/DOCUMENTATION.md#gradio-app).

For full benchmark results, please refer to the [technical report](https://3d-models.hunyuan.tencent.com/world/).

| Methods | Camera Metrics | Visual Quality | |||||
|---|---|---|---|---|---|---|---|
| RotErr ↓ | TransErr ↓ | ATE ↓ | Q-Align ↑ | CLIP-IQA+ ↑ | Laion-Aes ↑ | CLIP-I ↑ | |
| SEVA | 1.690 | 1.578 | 2.879 | 3.232 | 0.479 | 4.623 | 77.16 |
| Gen3C | 0.944 | 1.580 | 2.789 | 3.353 | 0.489 | 4.863 | 82.33 |
| WorldStereo | 0.762 | 1.245 | 2.141 | 4.149 | 0.547 | 5.257 | 89.05 |
WorldStereo 2.0 | 0.492 | 0.968 | 1.768 | 4.205 | 0.544 | 5.266 | 89.43 |

| Methods | Tanks-and-Temples | MipNeRF360 | ||||||
|---|---|---|---|---|---|---|---|---|
| Precision ↑ | Recall ↑ | F1-Score ↑ | AUC ↑ | Precision ↑ | Recall ↑ | F1-Score ↑ | AUC ↑ | |
| SEVA | 33.59 | 35.34 | 36.73 | 51.03 | 22.38 | 55.63 | 28.75 | 46.81 |
| Gen3C | 46.73 | 25.51 | 31.24 | 42.44 | 23.28 | 75.37 |
35.26 | 52.10 |
| Lyra | 50.38 |
28.67 | 32.54 | 43.05 | 30.02 | 58.60 | 36.05 | 49.89 |
| FlashWorld | 26.58 | 20.72 | 22.29 | 30.45 | 35.97 | 53.77 | 42.60 | 53.86 |
| WorldStereo 2.0 | 43.62 | 41.02 | 41.43 | 58.19 | 43.19 |
65.32 | 51.27 |
65.79 |
| WorldStereo 2.0 (DMD) | 40.41 | 44.41 |
43.16 |
60.09 |
42.34 | 64.83 | 50.52 | 65.64 |

**Point Map Reconstruction on 7-Scenes, NRGBD, and DTU.** We report the mean Accuracy and Completeness of WorldMirror under different input configurations. **Bold** results are best. "L / M / H" denote low / medium / high inference resolution. "+ all priors" denotes injection of camera extrinsics, camera intrinsics, and depth priors.

| Method | 7-Scenes (scene) |
NRGBD (scene) |
DTU (object) |
|||
|---|---|---|---|---|---|---|
| Acc. ↓ | Comp. ↓ | Acc. ↓ | Comp. ↓ | Acc. ↓ | Comp. ↓ | |
WorldMirror 1.0 | ||||||
| L | 0.043 | 0.055 | 0.046 | 0.049 | 1.476 | 1.768 |
| L + all priors | 0.021 | 0.026 | 0.022 | 0.020 | 1.347 | 1.392 |
| M | 0.043 | 0.049 | 0.041 | 0.045 | 1.017 | 1.780 |
| M + all priors | 0.018 | 0.023 | 0.016 | 0.014 | 0.735 | 0.935 |
| H | 0.079 | 0.087 | 0.077 | 0.093 | 2.271 | 2.113 |
| H + all priors | 0.042 | 0.041 | 0.078 | 0.082 | 1.773 | 1.478 |
WorldMirror 2.0 | ||||||
| L | 0.041 | 0.052 | 0.047 | 0.058 | 1.352 | 2.009 |
| L + all priors | 0.019 | 0.024 | 0.017 | 0.015 | 1.100 | 1.201 |
| M | 0.033 | 0.046 | 0.039 | 0.047 | 1.005 | 1.892 |
| M + all priors | 0.013 | 0.017 | 0.013 | 0.013 | 0.690 | 0.876 |
| H | 0.037 | 0.040 | 0.046 | 0.053 | 0.845 | 1.904 |
H + all priors | 0.012 | 0.016 | 0.015 | 0.016 | 0.554 | 0.771 |

**Comparison with Pow3R and MapAnything under Different Prior Conditions.** Results are averaged on 7-Scenes, NRGBD, and DTU datasets. Pow3R (pro) refers to the original Pow3R with Procrustes alignment.

![]() |

![](/Tencent-Hunyuan/HY-World-2.0/raw/main/assets/screenshot_4.gif)

![](/Tencent-Hunyuan/HY-World-2.0/raw/main/assets/screenshot_4.gif)

![](/Tencent-Hunyuan/HY-World-2.0/raw/main/assets/screenshot_5.gif)

![](/Tencent-Hunyuan/HY-World-2.0/raw/main/assets/screenshot_5.gif)

![](/Tencent-Hunyuan/HY-World-2.0/raw/main/assets/screenshot_6.gif)

![](/Tencent-Hunyuan/HY-World-2.0/raw/main/assets/screenshot_6.gif)

![](/Tencent-Hunyuan/HY-World-2.0/raw/main/assets/screenshot_9.gif)

![](/Tencent-Hunyuan/HY-World-2.0/raw/main/assets/screenshot_9.gif)

![](/Tencent-Hunyuan/HY-World-2.0/raw/main/assets/screenshot_10.gif)

![](/Tencent-Hunyuan/HY-World-2.0/raw/main/assets/screenshot_10.gif)

For detailed usage guides, parameter references, output format specifications, and prior injection instructions, see ** DOCUMENTATION.md**.

If you find HunyuanWorld 2.0 useful for your research, please cite:

```
@article{hyworld22026,
title={HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds},
author={Team HY-World},
journal={arXiv preprint},
year={2026}
}
@article{hunyuanworld2025tencent,
title={HunyuanWorld 1.0: Generating Immersive, Explorable, and Interactive 3D Worlds from Words or Pixels},
author={Team HunyuanWorld},
year={2025},
journal={arXiv preprint}
}
```

Please send emails to [tengfeiwang12@gmail.com](mailto:tengfeiwang12@gmail.com) for questions or feedback.

We would like to thank [HunyuanWorld 1.0](https://github.com/Tencent-Hunyuan/HunyuanWorld-1.0), [WorldMirror](https://github.com/Tencent-Hunyuan/HunyuanWorld-Mirror), [WorldPlay](https://github.com/Tencent-Hunyuan/HY-WorldPlay), [WorldStereo](https://github.com/FuchengSu/WorldStereo), [HunyuanImage](https://github.com/Tencent-Hunyuan/HunyuanImage-3.0) for their great work.
