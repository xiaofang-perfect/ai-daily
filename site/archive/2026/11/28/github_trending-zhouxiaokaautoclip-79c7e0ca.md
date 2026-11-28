---
title: "zhouxiaoka/autoclip"
source: GitHub Trending
url: https://github.com/zhouxiaoka/autoclip
date: 2026-11-28
published_at: 2026-11-28T09:43:56.702884+00:00
tag: 工具开源
item_id: 79c7e0ca381db9fc
---
![AutoClip](https://github.com/zhouxiaoka/autoclip/raw/main/src-tauri/icons/128x128.png) 

**The open-source OpusClip alternative** — local-first AI clipping for **podcasts, interviews, and gaming streams** with smart reframing, captions, covers, titles, and built-in **MCP for AI agents**. Zero subscriptions, no paywall.

 
  

 
  

 
  

 
  



  
  



[**Website**](https://zhouxiaoka.github.io/autoclip_intro/)
   · 
  [**Download**](https://github.com/zhouxiaoka/autoclip/releases/latest)
   · 
  [**Live Replays (v1.6)**](https://zhouxiaoka.github.io/autoclip_intro/features/game-streams/)
   · 
  [**Showcase**](https://zhouxiaoka.github.io/autoclip_intro/cases/?lang=en)
   · 
  [**Quick Start**](https://github.com/zhouxiaoka/autoclip#quick-start)
   · 
  [**Docs**](https://github.com/zhouxiaoka/autoclip#documentation)
   · 
  **Issues**

**English** · [简体中文](https://github.com/zhouxiaoka/autoclip/blob/main/docs/i18n/README-ZH.md) · [繁體中文](https://github.com/zhouxiaoka/autoclip/blob/main/docs/i18n/README-ZH-TW.md) · [日本語](https://github.com/zhouxiaoka/autoclip/blob/main/docs/i18n/README-JA.md) · [한국어](https://github.com/zhouxiaoka/autoclip/blob/main/docs/i18n/README-KO.md) · [Español](https://github.com/zhouxiaoka/autoclip/blob/main/docs/i18n/README-ES.md) · [Português](https://github.com/zhouxiaoka/autoclip/blob/main/docs/i18n/README-PT.md) · [Русский](https://github.com/zhouxiaoka/autoclip/blob/main/docs/i18n/README-RU.md) · [Français](https://github.com/zhouxiaoka/autoclip/blob/main/docs/i18n/README-FR.md) · [Bahasa Indonesia](https://github.com/zhouxiaoka/autoclip/blob/main/docs/i18n/README-ID.md) · [Türkçe](https://github.com/zhouxiaoka/autoclip/blob/main/docs/i18n/README-TR.md) · [Tiếng Việt](https://github.com/zhouxiaoka/autoclip/blob/main/docs/i18n/README-VI.md) · [Deutsch](https://github.com/zhouxiaoka/autoclip/blob/main/docs/i18n/README-DE.md)

⭐ *Free, MIT-licensed, zero subscriptions — everything cuts and renders on your machine. Star the repo if you find it useful!*

| ![APIMart](https://github.com/zhouxiaoka/autoclip/raw/main/docs/sponsors/apimart.png) [**APIMart**](https://go.apimart.ai/tw-autoclip) <sub>Low-cost AI image & video API · GPT-Image-2 from $0.006/img</sub> | [**Sponsor / Partner with AutoClip**](mailto:christine_zhouye@163.com?subject=AutoClip%20Sponsor%20%2F%20Provider%20Partnership) <sub>Put your AI API or creator tool in front of AutoClip users worldwide (cloud dynamic provider listing supported, zero client release needed). [christine\_zhouye@163.com](mailto:christine_zhouye@163.com)</sub> | 

Drop in a link, local video, or **live stream replay** — AutoClip finds the best moments, tracks the speaker, burns in captions, generates covers, and exports ready-to-post clips for TikTok, Shorts, Reels, YouTube, Douyin, Xiaohongshu, and Bilibili.

**Local-first by design:** cutting and rendering run directly on your computer with no upload queues and no monthly fee. Bring your own API key or run 100% offline with **Ollama / LM Studio + Whisper / SenseVoice**.

![AutoClip v1.6 Live Stream Replays Walkthrough](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/v1.6/autoclip-v1.6-demo.gif)


*Home → 6 Live Replay sources → OBS WebSocket setup → Twitch import → Finished clip with captions & one-click publish.*

| Feature | Details | 
|---|---|
| **6 Live Replay Sources** | Dedicated **Live Replay** tab supporting **OBS Studio, Twitch, YouTube, Kick, Discord, and local recordings**. | 
| **OBS Auto-Capture** | Connect OBS WebSocket ( `4455`), trim losslessly (`-c copy`), and auto-queue clips right after you end stream. | 
| **Game Highlights** | Generalized highlight detection supporting **8s+** standalone plays with tighter vision/OCR budgets. | 
| **One-Click Repurpose** | Unified playable clip cards — switch target platforms in one click without losing previous exports. | 
| **13 Languages** | Full desktop UI, tray menus, and docs in 13 languages ( `+ zh-TW, de, id, tr, vi`) plus Arabic RTL captions. | 

## 📸 Inside the App (5 screenshots)

| ![Home screen with Link, File, and Live Replay tabs](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/v1.6/en-01-home.jpg) *Home screen — Link, File, and Live Replay* | ![Live Replay 6-source picker](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/v1.6/en-02-replays-obs.jpg) *Live Replay — 6 replay sources* | 
| ![Inline OBS Studio WebSocket connection settings](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/v1.6/en-03-replays-obs-settings.jpg) *Inline OBS Studio WebSocket settings* | ![Twitch replay import](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/v1.6/en-04-replays-twitch.jpg) *Twitch import & local recording picker* | 
| ![Finished clip with Twitch source attribution](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/v1.6/en-05-result-card.jpg) *Finished clip — source attribution, 9:16 crop, captions, and one-click Download / Publish / Redo* |  | 

Click any thumbnail or **▶ Play** to watch full clips rendered by AutoClip. Language labels indicate burned-in subtitle language.

| ![Bill Gates](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/demos/gates-ezra-01.jpg) **Bill Gates** Interview · Douyin · ZH [▶ Play 1:01](https://pub-3fb92949b9c2480b89feec5ec03f3540.r2.dev/cases/gates-ezra/01.mp4?v=2026-10-01g) · [Source](https://www.youtube.com/watch?v=A_156w0aYtU) | ![AI Experts Debate](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/demos/ai-labs-debate-01.jpg) **AI Experts Debate** Interview · Shorts · EN [▶ Play 1:25](https://pub-3fb92949b9c2480b89feec5ec03f3540.r2.dev/cases/ai-labs-debate/01.mp4?v=2026-10-01g) · [Source](https://www.youtube.com/watch?v=OhOmLqR5nN4) | ![Tony Robbins](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/demos/robbins-36months-01.jpg) **Tony Robbins** Podcast · Douyin · ZH [▶ Play 1:45](https://pub-3fb92949b9c2480b89feec5ec03f3540.r2.dev/cases/robbins-36months/01.mp4?v=2026-10-01g) · [Source](https://www.youtube.com/watch?v=DuRcrbP3kag) | ![Andrew Garfield × Amy Poehler](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/demos/garfield-poehler-01.jpg) **Garfield × Poehler** Podcast · Shorts · EN [▶ Play 1:01](https://pub-3fb92949b9c2480b89feec5ec03f3540.r2.dev/cases/garfield-poehler/01.mp4?v=2026-10-01g) · [Source](https://www.youtube.com/watch?v=OJV8AaWCxQQ) | 

| ![Tong Liya × Lu Yu](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/demos/luyu-tongliya-01.jpg) **佟丽娅 × 鲁豫** · 16:9 · Bilibili · ZH [▶ Play 1:41](https://pub-3fb92949b9c2480b89feec5ec03f3540.r2.dev/cases/luyu-tongliya/01.mp4?v=2026-10-01g) · [Source](https://www.bilibili.com/video/BV1qheu6kEFV/) | ![Sam Altman](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/demos/altman-uses-ai-01.jpg) **Sam Altman** · 16:9 · Bilibili · ZH [▶ Play 2:02](https://pub-3fb92949b9c2480b89feec5ec03f3540.r2.dev/cases/altman-uses-ai/01.mp4?v=2026-10-01g) · [Source](https://www.youtube.com/watch?v=jZh55CQwSh8) | 

## See 10 more clips

| ![Adam Neumann](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/demos/neumann-doac-01.jpg) **Adam Neumann** Podcast · TikTok · EN [▶ Play 0:59](https://pub-3fb92949b9c2480b89feec5ec03f3540.r2.dev/cases/neumann-doac/01.mp4?v=2026-10-01g) · [Source](https://www.youtube.com/watch?v=IQ4JVWdj4Q0) | ![Xiao Qi × Lu Yu](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/demos/luyu-xiaoqi-02.jpg) **小奇 × 鲁豫** Interview · Douyin · ZH [▶ Play 0:50](https://pub-3fb92949b9c2480b89feec5ec03f3540.r2.dev/cases/luyu-xiaoqi/02.mp4?v=2026-10-01g) · [Source](https://www.bilibili.com/video/BV1ighy6AEPz/) | ![Guo Keyu × Lu Yu](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/demos/luyu-guokeyu-01.jpg) **郭柯宇 × 鲁豫** Interview · Douyin · ZH [▶ Play 1:11](https://pub-3fb92949b9c2480b89feec5ec03f3540.r2.dev/cases/luyu-guokeyu/01.mp4?v=2026-10-01g) · [Source](https://www.bilibili.com/video/BV1LDYV6HEXR/) | ![Willem Dafoe](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/demos/dafoe-hot-ones-01.jpg) **Willem Dafoe** Podcast · TikTok · EN [▶ Play 1:07](https://pub-3fb92949b9c2480b89feec5ec03f3540.r2.dev/cases/dafoe-hot-ones/01.mp4?v=2026-10-01g) · [Source](https://www.youtube.com/watch?v=YqugY2zTIoI) | 
| ![TIM × Luo Yonghao](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/demos/tim-luoyonghao-01.jpg) **TIM × 罗永浩** Interview · Douyin · ZH [▶ Play 1:05](https://pub-3fb92949b9c2480b89feec5ec03f3540.r2.dev/cases/tim-luoyonghao/01.mp4?v=2026-10-01g) · [Source](https://www.bilibili.com/video/BV1B5xkzPEhx/) | ![Jensen Huang](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/demos/jensen-dwarkesh-01.jpg) **Jensen Huang** Interview · Xiaohongshu · ZH [▶ Play 1:17](https://pub-3fb92949b9c2480b89feec5ec03f3540.r2.dev/cases/jensen-dwarkesh/01.mp4?v=2026-10-01g) · [Source](https://www.youtube.com/watch?v=Hrbq66XqtCo) | ![Andrej Karpathy](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/demos/karpathy-dwarkesh-01.jpg) **Andrej Karpathy** Interview · Douyin · ZH [▶ Play 0:43](https://pub-3fb92949b9c2480b89feec5ec03f3540.r2.dev/cases/karpathy-dwarkesh/01.mp4?v=2026-10-01g) · [Source](https://www.youtube.com/watch?v=lXUZvyajciY) | ![A20 Pro](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/demos/apple-a20-01.jpg) **A20 Pro** Interview · Xiaohongshu · ZH [▶ Play 2:00](https://pub-3fb92949b9c2480b89feec5ec03f3540.r2.dev/cases/apple-a20/01.mp4?v=2026-10-01g) · [Source](https://www.bilibili.com/video/BV1e4Y96FEaJ/) | 
| ![Sylvester Stallone](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/demos/stallone-nyt-01.jpg) **Sylvester Stallone** Interview · Douyin · ZH [▶ Play 1:39](https://pub-3fb92949b9c2480b89feec5ec03f3540.r2.dev/cases/stallone-nyt/01.mp4?v=2026-10-01g) · [Source](https://www.youtube.com/watch?v=ccs-B_nTfZs) | ![MrBeast](https://github.com/zhouxiaoka/autoclip/raw/main/docs/images/demos/mrbeast-colin-samir-01.jpg) **MrBeast** Podcast · TikTok · EN [▶ Play 1:42](https://pub-3fb92949b9c2480b89feec5ec03f3540.r2.dev/cases/mrbeast-colin-samir/01.mp4?v=2026-10-01g) · [Source](https://www.youtube.com/watch?v=9IQ_ldV9z_A) |  |  | 

Browse 16+ clips, covers, and post copy in the **[Showcase →](https://zhouxiaoka.github.io/autoclip_intro/cases/?lang=en)**, or [share your own clips](https://github.com/zhouxiaoka/autoclip/discussions/new?category=show-and-tell). Source copyrights remain with their original creators.

| Use case | Recommended setup | Requirements | 
|---|---|---|
| **Desktop app (easiest)** | Download `.dmg` / `-setup.exe` from [Releases](https://github.com/zhouxiaoka/autoclip/releases/latest) | Apple Silicon macOS or Windows 10/11 x64 (Python & FFmpeg bundled) | 
| **AI agents / CLI / MCP** | `uvx autoclip-mcp` or `npx skills add zhouxiaoka/autoclip` | Python 3.10+ (3.11 recommended) & FFmpeg | 
| **Self-hosted / Linux / Intel Mac** | `docker compose up -d --build` | Docker & Compose v2 | 

1. Download the latest installer from **[GitHub Releases](https://github.com/zhouxiaoka/autoclip/releases/latest)** (`aarch64.dmg` for Apple Silicon macOS, `x64-setup.exe` for Windows). Portable Python and FFmpeg are bundled.
2. Open **Settings**, pick a cloud provider (or start Ollama / LM Studio), test the connection, and save — or click **Try the built-in example** with no API key.
3. Paste a video link, drop a file, or switch to **Live Replay** to connect OBS or import a stream recording. Pick your platforms and click **Generate**.

> Installers are built publicly on GitHub Actions (`Desktop Build`) with `build-provenance.json` SHA-256 verification. First launch on an unsigned build: on **macOS** run `xattr -dr com.apple.quarantine "/Applications/AutoClip Desktop.app"` (or *System Settings → Privacy & Security → Open Anyway*); on **Windows** click **More info → Run anyway** on SmartScreen. See **[Code Signing & Verification Policy](https://github.com/zhouxiaoka/autoclip/blob/main/CODE_SIGNING.md)** (notarization tracked in [#119](https://github.com/zhouxiaoka/autoclip/issues/119)).

Let AI coding agents clip videos directly from your terminal (`claude mcp add autoclip -- uvx autoclip-mcp`). Full MCP setup guides: **[English](https://github.com/zhouxiaoka/autoclip/blob/main/docs/MCP.en.md)** · [简体中文](https://github.com/zhouxiaoka/autoclip/blob/main/docs/CLI_AND_MCP.md) · [日本語](https://github.com/zhouxiaoka/autoclip/blob/main/docs/MCP.ja.md) · [한국어](https://github.com/zhouxiaoka/autoclip/blob/main/docs/MCP.ko.md) · [Español](https://github.com/zhouxiaoka/autoclip/blob/main/docs/MCP.es.md) · [Deutsch](https://github.com/zhouxiaoka/autoclip/blob/main/docs/MCP.de.md).

```
uvx autoclip-mcp
npx skills add zhouxiaoka/autoclip
autoclip --version
autoclip produce talk.mp4 --srt talk.srt --platform tiktok --portrait-style podcast --json
autoclip outputs PROJECT_ID --export-kits
```
## Offline wheel, source install & MCPB packaging

```
# Install from a downloaded CLI/MCP release ZIP wheel
python3 -m venv .venv && source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install --force-reinstall --no-deps autoclip_mcp-*-py3-none-any.whl
# Or install from source
python -m pip install --no-deps .
```
To build a local MCPB bundle without publishing, run `python scripts/pack_mcpb.py` (never run `smithery mcp publish` automatically).

```
git clone https://github.com/zhouxiaoka/autoclip.git
cd autoclip
cp env.example .env
mkdir -p data logs uploads
docker compose up -d --build
```
Open the web UI at `http://localhost:3000` (API docs at `http://localhost:8000/docs`). See [Docker Guide](https://github.com/zhouxiaoka/autoclip/blob/main/docs/DOCKER.en.md) for bind-mount permissions and custom origins.

Measured on an Apple Silicon Mac (LLM cost estimated with `qwen-plus`; excludes cloud ASR and AI image generation; check your provider bill for exact usage):

| Input | Source | Time & Output | Est. LLM Cost | 
|---|---|---|---|
| **With existing subtitles** | Jensen Huang · 1h 43m (EN → Xiaohongshu) | **7.5 min / 10 clips** | **¥0.09** | 
| **No subtitles (local Whisper)** | TIM × Luo Yonghao · 2h 52m (ZH → Douyin) | 29.5 min / 10 clips | ¥0.20 | 

| ![APIMart](https://github.com/zhouxiaoka/autoclip/raw/main/docs/sponsors/apimart.png) [**APIMart**](https://go.apimart.ai/tw-autoclip) | Thanks to **APIMart** for sponsoring AutoClip! **APIMart** is a low-cost API platform for AI image & video generation — GPT-Image-2 from **$0.006/image** (**160+** images per dollar). One async API covers both image and video: submit a task, get an ID, fetch results via polling or callback. Batch tens of thousands of images without timeouts and switch models without changing code. Pay-as-you-go with no monthly fee — [sign up here](https://go.apimart.ai/tw-autoclip). | 

*Affiliate link (separate from the sponsor above):* sign up on Alibaba Cloud, create an API key in the Bailian console, and enable Bailian cloud ASR under **Settings → Default models → Speech to subtitles**.

1. [Alibaba Cloud signup](https://www.aliyun.com/benefit?userCode=qmyj6jch) (affiliate link)
2. [Bailian console](https://bailian.console.aliyun.com/) — create your API key

## Is AutoClip free? Do I need an API key?

Yes — AutoClip is free and MIT-licensed. Cloud analysis, transcription, and AI covers use your own API keys at provider rates (local cover layout is free by default). Ollama and LM Studio require no cloud key. Direct publishing uses your own Bilibili or [Upload-Post](https://www.upload-post.com) account.

## Does my video get uploaded to the cloud?

Cutting and rendering run locally. Cloud analysis only sends transcript text; vision models only receive sampled frames; cloud ASR uploads audio. Running local LLMs + Whisper / SenseVoice keeps everything offline. Analytics and crash reports can be turned off in Settings. See [Privacy](https://github.com/zhouxiaoka/autoclip/blob/main/docs/PRIVACY.en.md).

## What kind of videos work best?

Podcasts, interviews, talks, courses, and gaming live stream replays (OBS / Twitch / YouTube / Kick / Discord). Sources with existing subtitles are fastest; otherwise use local Whisper / SenseVoice or cloud ASR. For gameplay or low-dialogue streams, enable a vision-capable model.

## Why weren't any clips generated?

Check the failed stage: subtitles/transcription, model connection, FFmpeg, disk space, or platform length limits (YouTube long-form requires ≥180s; use Shorts, TikTok, or Bilibili for shorter clips). If it still fails, open an issue with `autoclip --version`, OS, model, and redacted logs, or check [Known Issues (#96)](https://github.com/zhouxiaoka/autoclip/issues/96).

[Troubleshooting](https://github.com/zhouxiaoka/autoclip/blob/main/docs/FAQ.en.md) · [Known Issues](https://github.com/zhouxiaoka/autoclip/issues/96)

| Topic | Guide | 
|---|---|
| Install & first clips | [Installation Guide](https://github.com/zhouxiaoka/autoclip/blob/main/docs/USER_INSTALLATION_GUIDE.en.md) | 
| Self-hosting & agents | [Docker](https://github.com/zhouxiaoka/autoclip/blob/main/docs/DOCKER.en.md) · [MCP & AI Agents](https://github.com/zhouxiaoka/autoclip/blob/main/docs/MCP.en.md) ([ZH](https://github.com/zhouxiaoka/autoclip/blob/main/docs/CLI_AND_MCP.md) · [JA](https://github.com/zhouxiaoka/autoclip/blob/main/docs/MCP.ja.md) · [KO](https://github.com/zhouxiaoka/autoclip/blob/main/docs/MCP.ko.md) · [ES](https://github.com/zhouxiaoka/autoclip/blob/main/docs/MCP.es.md) · [DE](https://github.com/zhouxiaoka/autoclip/blob/main/docs/MCP.de.md)) · [Agent Skill](https://github.com/zhouxiaoka/autoclip/blob/main/skills/autoclip/SKILL.md) (ZH) · [OpenCode](https://github.com/zhouxiaoka/autoclip/blob/main/docs/OPENCODE.en.md) | 
| Models & troubleshooting | [Multi-LLM Setup](https://github.com/zhouxiaoka/autoclip/blob/main/docs/MULTI_LLM_PROVIDER_GUIDE.md) (ZH) · [FAQ](https://github.com/zhouxiaoka/autoclip/blob/main/docs/FAQ.en.md) | 
| Releases & privacy | [Changelog](https://github.com/zhouxiaoka/autoclip/blob/main/CHANGELOG.md) · [Code Signing](https://github.com/zhouxiaoka/autoclip/blob/main/CODE_SIGNING.md) · [Roadmap](https://github.com/zhouxiaoka/autoclip/blob/main/docs/ROADMAP.md) (ZH) · [Community Board](https://github.com/zhouxiaoka/autoclip/blob/main/docs/COMMUNITY_BOARD.md) (ZH) · [Privacy](https://github.com/zhouxiaoka/autoclip/blob/main/docs/PRIVACY.en.md) | 
| Research | [Pick the Moment, Not the Effect](https://github.com/zhouxiaoka/autoclip/blob/main/docs/research/2026-10-what-drives-views/article-en.md) · [中文](https://github.com/zhouxiaoka/autoclip/blob/main/docs/research/2026-10-what-drives-views/article-zh.md) | 
| Contributing & i18n | [Contributing](https://github.com/zhouxiaoka/autoclip/blob/main/CONTRIBUTING.md) (ZH) · [Translating AutoClip](https://github.com/zhouxiaoka/autoclip/blob/main/TRANSLATING.md) · [Translation Guide](https://github.com/zhouxiaoka/autoclip/blob/main/docs/i18n.md) (ZH) | 

PRs, bug reports, sample clips, and translations are welcome. If AutoClip saves you time, a ⭐ star helps!

- **Community:** [GitHub Discussions](https://github.com/zhouxiaoka/autoclip/discussions) · [First-Clip Q&A](https://github.com/zhouxiaoka/autoclip/discussions/128) · [Feature Ideas](https://github.com/zhouxiaoka/autoclip/discussions/129)
- **Bug reports:** use the [issue template](https://github.com/zhouxiaoka/autoclip/issues/new/choose) with OS, version, model, repro steps, and redacted logs
- **Partnerships:** [christine\_zhouye@163.com](mailto:christine_zhouye@163.com)

AutoClip is maintained solo — please expect async replies (no live or 1-on-1 setup support).

Built with FastAPI, React, Tauri, FFmpeg, yt-dlp, Whisper, and FunASR. [MIT License](https://github.com/zhouxiaoka/autoclip/blob/main/LICENSE).
