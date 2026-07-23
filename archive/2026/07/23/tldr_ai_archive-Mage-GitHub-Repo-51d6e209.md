---
title: "Mage (GitHub Repo)"
source: TLDR AI · 2026-07-22
url: https://github.com/microsoft/Mage?utm_source=tldrai
date: 2026-07-23
published_at: 2026-07-22T12:00:00+00:00
tag: 工具开源
item_id: 51d6e209d01e7594
---
**Microsoft Mage Team**

  
   
  
   
  

   
  

   
  



![gallery](https://github.com/microsoft/Mage/raw/main/assets/mage-model-cover.png)

**Mage** is a family of lightweight, research-friendly multimodal models built at a fixed **4B-parameter** budget. It is designed to make advanced visual **understanding** and **generation** accessible for controlled experiments, post-training research, and vertical-domain applications under realistic compute budgets.

The family is organized around a shared **codec-aligned efficiency** philosophy — *spend representation capacity where the signal is* — applied to both the understanding and the generation side:

| Model | Task | Scale | Code | Report | 
|---|---|---|---|---|
| [Mage-VL](https://github.com/microsoft/Mage/blob/main/mage_vl) | Image & video understanding, proactive streaming | 4B | `mage_vl/` | Coming Soon | 
| [Mage-Flow](https://github.com/microsoft/Mage/blob/main/mage_flow) | Text-to-image generation & instruction-based editing | 4B | `mage_flow/` | [arXiv](https://arxiv.org/abs/2607.19064) | 

Both models are compact enough to train, fine-tune, and deploy on modest hardware, yet remain competitive with much larger open systems in their respective domains.

**Mage-VL** is a codec-native, proactive-streaming multimodal foundation model for image & video understanding, trained **entirely from scratch** at a compact **4B** scale.

**🚧 Coming soon** — code, checkpoints, and full details are on the way. Stay tuned.

**Mage-Flow** is a compact 4B generative stack for **text-to-image generation** and **instruction-based image editing**, built from two co-designed components: **Mage-VAE** (a lightweight, high-fidelity latent tokenizer) and a **Native-Resolution Multimodal Diffusion Transformer** trained with rectified flow matching. Each task ships in **Base**, **RL-aligned**, and **4-step Turbo** variants.

**Highlights**

- **Compact & competitive.**A single 4B family for generation- *and*editing that matches or beats much larger open systems (Qwen-Image 20B, Z-Image 6B, FLUX.2 32B, FireRed-Image-Edit 20B).
- **Efficient tokenizer.**Mage-VAE matches FLUX.2-VAE reconstruction fidelity using- **~12× / ~22× fewer encode / decode MACs per pixel**, removing the VAE high-resolution bottleneck.
- **Native resolution.**One checkpoint generates from- **512 to 2048**on any aspect ratio, including extreme- **4:1**(e.g.- `512×2048`,- `2048×512`).
- **System-level speed.**Native-resolution packing + fused CUDA kernels cut per-step training time from- **~1.93 s → ~0.78 s**(- **~2.5× faster training**); at- `1024²`on a single A100,- **Mage-Flow-Turbo 0.59 s/image**and- **Mage-Flow-Edit-Turbo 1.02 s/edit**.
- **Versatile editing.**Mage-Flow-Edit supports semantic content editing, appearance transformation, image restoration, and structure-aware outputs within a unified image-and-text-conditioned model.

→ Details, installation, Python API, CLI, and Gradio app: `mage_flow/README.md`

- **2026-07-22**—- **Mage-Flow**checkpoints released on 🤗- [Hugging Face](https://huggingface.co/collections/microsoft/mage): Base, RL-aligned, and 4-step Turbo variants for both text-to-image generation and image editing.
- **Coming soon**—- **Mage-VL**: a- **Base**vision–language model plus a- **proactive-streaming**variant for codec-native image & video understanding. Stay tuned.

**Mage-VL** — vision–language (image & video understanding).

| Model | Task | Scale | Hugging Face | 
|---|---|---|---|
| `Mage-VL` | image & video understanding, proactive streaming | 4B | 🚧 Coming soon | 

**Mage-Flow** — generation & editing. Each checkpoint is a self-contained diffusers-style repo (`transformer/` + shared `vae/`, `text_encoder/`, `scheduler/`).

| Model | Task | Variant | Steps | Hugging Face | 
|---|---|---|---|---|
| `Mage-Flow-4B-Base` | text→image | Base | 30 | [🤗 microsoft/Mage-Flow-Base](https://huggingface.co/microsoft/Mage-Flow-Base) | 
| `Mage-Flow-4B` | text→image | RL-aligned | 20 | [🤗 microsoft/Mage-Flow](https://huggingface.co/microsoft/Mage-Flow) | 
| `Mage-Flow-4B-Turbo` | text→image | Few-step distilled | 4 | [🤗 microsoft/Mage-Flow-Turbo](https://huggingface.co/microsoft/Mage-Flow-Turbo) | 
| `Mage-Flow-Edit-4B-Base` | editing | Base | 30 | [🤗 microsoft/Mage-Flow-Edit-Base](https://huggingface.co/microsoft/Mage-Flow-Edit-Base) | 
| `Mage-Flow-Edit-4B` | editing | RL-aligned | 30 | [🤗 microsoft/Mage-Flow-Edit](https://huggingface.co/microsoft/Mage-Flow-Edit) | 
| `Mage-Flow-Edit-4B-Turbo` | editing | Few-step distilled | 4 | [🤗 microsoft/Mage-Flow-Edit-Turbo](https://huggingface.co/microsoft/Mage-Flow-Edit-Turbo) | 

Each model is self-contained in its own directory with a dedicated README:

- **Mage-VL**— image/video understanding demo, codec backends, CLI →- `mage_vl/README.md`
- **Mage-Flow**— installation, Python API, CLI, prompt enhancement, Gradio app →- `mage_flow/README.md`

```
@article{zhang2026mageflow,
  title={Mage-Flow: An Efficient Native-Resolution Foundation Model for Image Generation and Editing},
  author={Zhang, Xinjie and Zhang, Peng and Zheng, Shicheng and Guo, Jinghao and Jia, Zhaoyang and Shen, Yifei and Guo, Xun and Luo, Yuxuan and Li, Jiahao and Xie, Wenxuan and Pu, Fanyi and Zhang, Xiaoyi and Zhang, Kaichen and Guo, Zongyu and Bi, Tianci and Gui, Dongnan and Liu, Zhening and Wen, Zimo and Zheng, Zihan and Yang, Senqiao and Li, Xiao and Wang, Jinglu and Li, Bin and Lu, Yan},
  journal={arXiv preprint arXiv:2607.19064},
  year={2026}
}
```
These models are released for research purposes only and are not intended for product or service deployment. Responsible AI considerations were incorporated throughout the development process, including data selection, model training, and evaluation. The training data includes a combination of public, licensed, and internal datasets that were processed to remove clearly identifiable personal information and reduce harmful content where possible. However, as the data is largely sourced from web-scale collections, it may contain biases or uneven representation. As a result, the models may generate outputs that are inaccurate, biased, or inappropriate under certain prompts. The models should be used in controlled research settings with appropriate human oversight, and downstream users are responsible for applying additional safeguards — such as content moderation, validation, and compliance checks — before broader use.

This project is released under the [MIT License](https://github.com/microsoft/Mage/blob/main/LICENSE).
