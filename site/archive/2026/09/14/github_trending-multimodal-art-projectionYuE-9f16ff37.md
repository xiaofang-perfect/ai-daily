---
title: "multimodal-art-projection/YuE"
source: GitHub Trending
url: https://github.com/multimodal-art-projection/YuE
date: 2026-09-14
published_at: 2026-09-14T07:30:11.498154+00:00
tag: 工具开源
item_id: 9f16ff3708e77254
---
Looking for the original YuE? Its code, documentation, and license are preserved on the **[YuE-v1 branch](https://github.com/multimodal-art-projection/YuE/tree/YuE-v1)**.


  
![YuE](https://github.com/multimodal-art-projection/YuE/raw/main/assets/logo.png)


  
  


**Compose in symbols. Create in sound.**

  [🎧 Demos](https://map-yue2.github.io/) ·
  [🤗 YuE2](https://huggingface.co/m-a-p/YuE2-3B) ·
  [🚀 Quick start](https://github.com#quick-start) ·
  [🤖 Agent skill](https://github.com#agent-skill) ·
  [📊 Benchmarks](https://github.com#benchmarks) ·
  [🤗 MERT2](https://huggingface.co/m-a-p/MERT-v2-FullSong) ·
  [🤗 SheetSage2](https://huggingface.co/m-a-p/SheetSage2) ·
  [🤗 WSB](https://huggingface.co/datasets/m-a-p/WildSongBench) ·
  [📦 Release](https://github.com/multimodal-art-projection/YuE/releases/tag/yue2-v0.1.6) ·
  

**YuE2 brings frontier song quality to music generation with an editable composition.** Give it lyrics and a style prompt: it writes a melody-and-chord plan, then realizes that plan as a complete song with vocals and accompaniment.

- **Frontier quality.** YuE2 is competitive with Suno v5/v6 on WildSongBench. YuE2 (best-of-8) achieves**6.9632 SongBench Avg** , the highest observed mean among all evaluated settings.
- **White-box music generation through symbolic planning.** Read, play, and change the composition before rendering it. Melody and chords become explicit controls that a person or an agent can inspect and edit.
- **Zero-shot covers and agentic editing.** Reimagine a transcribed song in a new style, or refine a song through a conversation about its score, arrangement, and lyrics—all with the same generation checkpoint.

![YuE2 song quality and text alignment on WildSongBench](https://github.com/multimodal-art-projection/YuE/raw/main/assets/frontier-teaser.png)


*192 WildSongBench prompts. Both YuE2 settings use symbolic planning. Bo8 = best-of-8. The axes are normalized comparison indices; bubble area represents AudioBox production quality. [Scores and evaluation protocol](https://github.com/multimodal-art-projection/YuE/blob/main/docs/benchmarks.md). [Vector PDF](https://github.com/multimodal-art-projection/YuE/blob/main/assets/frontier-teaser.pdf) · [SVG](https://github.com/multimodal-art-projection/YuE/blob/main/assets/frontier-teaser.svg).*

| Create | Cover | Edit with an agent | 
|---|---|---|
| Lyrics + style → score → full song | Source recording → melody score → a new interpretation | Musical feedback → score, style, or lyric revisions → a new recording | 
| [Listen and inspect the score](https://map-yue2.github.io/#abc-cot-gen) | [Hear zero-shot covers](https://map-yue2.github.io/#cover) | [Follow an editing conversation](https://map-yue2.github.io/#agentic-music-editing) | 

The agentic demo follows **The Last Train through 9 steps and 14 versions**, from Mandarin pop to English jazz with new harmony and a saxophone solo. Listen to each version and inspect its conversation, score, prompt, and lyrics.

![YuE2 architecture: style and lyrics become an editable score, semantic music tokens, acoustic latents, and audio](https://github.com/multimodal-art-projection/YuE/raw/main/assets/architecture.png)


One **AR–NAR Mixture-of-Transformers** backbone predicts the score and semantic tokens autoregressively, then generates acoustic latents with flow matching. A VAE decodes those latents into stereo audio. Creation, covering, and editing differ in where the score comes from: YuE2, a transcribed recording, or an edited composition.

The staged Python API exposes `plan()` → `generate_semantic()` → `synthesize()` → `decode()`. See the [generation guide](https://github.com/multimodal-art-projection/YuE/blob/main/docs/generation.md) for exact-plan reuse and decoder selection.

**Linux · Python 3.12 · NVIDIA GPU with BF16 support and 24 GB VRAM.** YuE2 produces 48 kHz stereo audio without quantization. Model files download from Hugging Face on first use.

```
git clone https://github.com/multimodal-art-projection/YuE.git
cd YuE
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install .
python examples/generate.py --output outputs/first-song
```
Open `outputs/first-song/audio.flac`. The output directory also retains the score, semantic tokens, acoustic latents, generation settings, and model identities.

The Python interface is equally short:

```
import json
from pathlib import Path
from yue2 import YuE2Pipeline
request = json.loads(Path("examples/song.json").read_text(encoding="utf-8"))
with YuE2Pipeline.from_pretrained("m-a-p/YuE2-3B", device="cuda") as pipe:
    song = pipe(**request)
    song.save_artifacts("outputs/my-song")
    print(song.truncated)
```
| Setting | Behavior | 
|---|---|
| `cot="full"` | Generate an editable melody-and-chord plan; the default for new songs | 
| `cot="melody"` | Use a melody plan with free accompaniment; recommended for covers | 
| `cot="off"` | Generate directly from lyrics and style | 
| `abc=...` | Supply your own score in `full` or`melody` mode | 

[Generation guide](https://github.com/multimodal-art-projection/YuE/blob/main/docs/generation.md) · [Original example inputs](https://github.com/multimodal-art-projection/YuE/blob/main/examples/README.md) · [v0.1.6 wheel archive](https://github.com/multimodal-art-projection/YuE/releases/download/yue2-v0.1.6/yue2_infer-0.1.6-py3-none-any.whl)

Transcribe a source recording with **[🤗 SheetSage2](https://huggingface.co/m-a-p/SheetSage2)**, review its melody ABC, and provide new lyrics or a target style. For covers, use **`cot="melody"` and a score without chord symbols** so the accompaniment can adapt to the new style.

```
from pathlib import Path
from yue2 import YuE2Pipeline
with YuE2Pipeline.from_pretrained("m-a-p/YuE2-3B", device="cuda") as pipe:
    cover = pipe(
        style="English, jazz-funk, warm lead vocal, Rhodes, bass and drums",
        lyrics=Path("cover-lyrics.txt").read_text(encoding="utf-8"),
        abc=Path("cover-score/score.abc").read_text(encoding="utf-8"),
        cot="melody",
        seed=42,
    )
    cover.save_artifacts("outputs/cover")
```
SheetSage2 runs in a separate environment and loads its MERT2 encoder automatically. The [cover guide](https://github.com/multimodal-art-projection/YuE/blob/main/docs/covers.md) gives the complete transcription and generation commands. An included [original melody example](https://github.com/multimodal-art-projection/YuE/blob/main/examples/melody.abc) also lets you try score-conditioned generation immediately.

Export a plan, revise the musical details, and render the edited score:

```
import json
from pathlib import Path
from yue2 import YuE2Pipeline
request = json.loads(Path("examples/song.json").read_text(encoding="utf-8"))
with YuE2Pipeline.from_pretrained("m-a-p/YuE2-3B", device="cuda") as pipe:
    plan = pipe.plan(**request)
    plan.save("outputs/plan")
```
Copy `outputs/plan/score.abc` to `edited.abc`, then ask an agent to change its harmony, melody, tempo, or form. Supply the edited file as a new score:

```
python examples/generate.py --request examples/song.json \
  --abc-file edited.abc --cot full --output outputs/edited
```
The editable score is the white-box interface: you can inspect the intended composition and intervene on it. Editing generates a new complete recording; it does not preserve the original waveform outside an edit. [Editing guide and a reproducible harmony example](https://github.com/multimodal-art-projection/YuE/blob/main/docs/editing.md).

The **[yue2-music skill](https://github.com/multimodal-art-projection/YuE/blob/main/skills/yue2-music/SKILL.md)** teaches an agent how to generate songs, transcribe and cover recordings, edit ABC scores, check musical invariants, and organize listening comparisons. It includes portable helpers and references to the released model interfaces.

Use **`skills/yue2-music/` from this repository** with an agent that supports `SKILL.md` packages. Install it using your agent's skill-directory or import mechanism; the Python runtime is installed separately with `pip install .`. The earlier [v0.1.6 skill ZIP](https://github.com/multimodal-art-projection/YuE/releases/download/yue2-v0.1.6/yue2-music.zip) remains available under its bundled license.

Try a concrete request:

Use the yue2-music skill to create an English piano-pop song. Keep the original audio and score. Make a second version with jazz harmony, preserve the vocal melody and lyric order, and give me both versions to compare.


**WildSongBench: 192 prompts, automatic evaluation, September 12, 2026.**

| System / setting | SongBench Avg ↑ | AudioBox PQ ↑ | MuLan ↑ | PER ↓ | 
|---|---|---|---|---|
| **YuE2 (best-of-8)** † | **6.9632** | 8.2714 | 0.5051 | 9.79% | 
| Mureka 9 | 6.9377 | 8.0226 | 0.4394 | 11.69% | 
| Suno v5 | 6.8721 | 8.1698 | **0.5428** | 8.10% | 
| **YuE2** † | 6.7316 | 8.2598 | 0.5068 | 8.44% | 
| Suno v5.5 | 6.7150 | 8.1955 | 0.5089 | 5.96% | 
| Suno v4.5 | 6.6995 | 8.2541 | 0.5022 | **5.80%** | 
| Suno v6 | 6.5562 | 8.1296 | 0.4916 | 7.58% | 
| Suno v6 Wild | 6.4195 | 8.1785 | 0.4999 | 7.45% | 
| LeVo 2 † | 6.3247 | **8.3966** | 0.3542 | 26.12% | 
| MiniMax Music 2.6 | 6.3222 | 8.1711 | 0.4251 | 24.55% | 
| MiniMax Music 3 † | 6.2830 | 8.2825 | 0.3928 | 6.27% | 
| HeartMuLa † | 6.2483 | 8.2933 | 0.3823 | 10.71% | 
| Muse † | 6.0349 | 8.0517 | 0.3937 | 33.42% | 
| ACE-Step 1.5 † | 6.0118 | 8.0518 | 0.4372 | 7.46% | 
| DiffRhythm 2 † | 5.2428 | 7.9782 | 0.3782 | 18.41% | 
| YuE 1 † | 4.9165 | 7.8683 | 0.2623 | 36.38% | 
| SongBloom † | 4.2350 | 8.1539 | 0.2697 | 19.19% | 

† Publicly available model weights. All 17 evaluated settings are shown, sorted by SongBench Avg; bold values mark the best result in each column.

Both YuE2 settings use symbolic planning and the benchmark decoder, **YuE2-Vae-legacy**. Standard YuE2 selects from two candidates; best-of-8 selects from eight. Rankings vary by metric; the small gap between the highest means does not establish statistical significance. [Full results and selection protocols](https://github.com/multimodal-art-projection/YuE/blob/main/docs/benchmarks.md).

**Zero-shot covers.** On 948 works, full-score YuE2 reaches **0.647 CLEWS mAP**, compared with **0.006 without a score**, while using the general generator without cover-specific fine-tuning. Source-identity preservation and target-style quality are measured separately; melody-only covers offer more freedom to change the arrangement. [Cover evaluation](https://github.com/multimodal-art-projection/YuE/blob/main/docs/benchmarks.md#zero-shot-cover-generation).

To reproduce the reported benchmark scores, follow the instructions on [🤗 WildSongBench (WSB)](https://huggingface.co/datasets/m-a-p/WildSongBench#reproduce-standard-yue2).

**State-of-the-art music understanding:** SOTA on **14 of 15 MARBLE metrics**, with **91.72% genre accuracy on GTZAN**.

[Demo and results](https://map-yue2.github.io/#mert2) · [🤗 MERT2-30s](https://huggingface.co/m-a-p/MERT-v2-30s) · [🤗 MERT2-FS](https://huggingface.co/m-a-p/MERT-v2-FullSong)

**State-of-the-art audio-to-score transcription:** SOTA on **10 of 13 benchmark metrics**, with **82.51% vocal melody pitch-class F1 on RWC-Pop**.

[Demo and results](https://map-yue2.github.io/#sheetsage2) · [🤗 Model and inference](https://huggingface.co/m-a-p/SheetSage2)

| Resource | Purpose | 
|---|---|
| [🤗 YuE2-3B](https://huggingface.co/m-a-p/YuE2-3B) | Song generation, symbolic planning, covering, and editing | 
| [🤗 YuE2-Vae](https://huggingface.co/m-a-p/YuE2-Vae) | Default generation and listening decoder | 
| [🤗 YuE2-Vae-legacy](https://huggingface.co/m-a-p/YuE2-Vae-legacy) | Decoder for the reported benchmark protocol | 
| [🤗 SheetSage2](https://huggingface.co/m-a-p/SheetSage2) | Audio-to-score transcription for covers and editing | 
| [🤗 MERT-v2-FullSong](https://huggingface.co/m-a-p/MERT-v2-FullSong) | Full-song music representations; SheetSage2's encoder | 
| [🤗 MERT-v2-30s](https://huggingface.co/m-a-p/MERT-v2-30s) | Music representations for short recordings | 
| [🤗 WildSongBench](https://huggingface.co/datasets/m-a-p/WildSongBench) | Evaluation prompts and benchmark resources | 

MERT2 feature extraction is optional for generation. YuE2's pipeline does not require a separate MERT2 model download. [Demos and interactive results](https://map-yue2.github.io/) · [Release downloads](https://github.com/multimodal-art-projection/YuE/releases/tag/yue2-v0.1.6).

YuE2's first-party code, agent skill, and documentation are licensed under **[Apache 2.0](https://github.com/multimodal-art-projection/YuE/blob/main/LICENSE)**. Copyright (c) 2026 the YuE2 authors.

Model weights are separately licensed under **[CC BY-NC 4.0](https://github.com/multimodal-art-projection/YuE/blob/main/MODEL_LICENSE)**. Third-party components retain their [original licenses](https://github.com/multimodal-art-projection/YuE/blob/main/THIRD_PARTY_NOTICES.md). The archived [YuE-v1 branch](https://github.com/multimodal-art-projection/YuE/tree/YuE-v1) retains its original license.

Apache 2.0 applies to the current repository source; the earlier `yue2-v0.1.6` download archives retain their bundled licenses.

The YuE2 technical report is coming soon. For now, please cite **[MERT](https://arxiv.org/abs/2306.00107)** and **[YuE](https://arxiv.org/abs/2503.08638)**:

```
@article{li2023mert,
  title = {{MERT}: Acoustic Music Understanding Model with Large-Scale Self-supervised Training},
  author = {Li, Yizhi and Yuan, Ruibin and Zhang, Ge and Ma, Yinghao and Chen, Xingran and Yin, Hanzhi and Xiao, Chenghao and Lin, Chenghua and Ragni, Anton and Benetos, Emmanouil and Gyenge, Norbert and Dannenberg, Roger and Liu, Ruibo and Chen, Wenhu and Xia, Gus and Shi, Yemin and Huang, Wenhao and Wang, Zili and Guo, Yike and Fu, Jie},
  journal = {arXiv preprint arXiv:2306.00107},
  year = {2023},
  eprint = {2306.00107},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2306.00107}
}
@article{yuan2025yue,
  title = {{YuE}: Scaling Open Foundation Models for Long-Form Music Generation},
  author = {Yuan, Ruibin and Lin, Hanfeng and Guo, Shuyue and Zhang, Ge and Pan, Jiahao and Zang, Yongyi and Liu, Haohe and Liang, Yiming and Ma, Wenye and Du, Xingjian and Du, Xinrun and Ye, Zhen and Zheng, Tianyu and Jiang, Zhengxuan and Ma, Yinghao and Liu, Minghao and Tian, Zeyue and Zhou, Ziya and Xue, Liumeng and Qu, Xingwei and Li, Yizhi and Wu, Shangda and Shen, Tianhao and Ma, Ziyang and Zhan, Jun and Wang, Chunhui and Wang, Yatian and Chi, Xiaowei and Zhang, Xinyue and Yang, Zhenzhu and Wang, Xiangzhou and Liu, Shansong and Mei, Lingrui and Li, Peng and Wang, Junjie and Yu, Jianwei and Pang, Guojian and Li, Xu and Wang, Zihao and Zhou, Xiaohuan and Yu, Lijun and Benetos, Emmanouil and Chen, Yong and Lin, Chenghua and Chen, Xie and Xia, Gus and Zhang, Zhaoxiang and Zhang, Chao and Chen, Wenhu and Zhou, Xinyu and Qiu, Xipeng and Dannenberg, Roger and Liu, Jiaheng and Yang, Jian and Huang, Wenhao and Xue, Wei and Tan, Xu and Guo, Yike},
  journal = {arXiv preprint arXiv:2503.08638},
  year = {2025},
  eprint = {2503.08638},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2503.08638}
}
```
For collaborations, licensing, and data partnerships, please contact [gezhang@umich.edu](mailto:gezhang@umich.edu).
