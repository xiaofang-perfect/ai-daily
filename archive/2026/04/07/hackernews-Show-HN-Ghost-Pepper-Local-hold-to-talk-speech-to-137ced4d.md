---
title: "Show HN: Ghost Pepper – Local hold-to-talk speech-to-text for macOS"
source: Hacker News
url: https://github.com/matthartman/ghost-pepper
date: 2026-04-07
published_at: 2026-04-06T19:50:16+00:00
tag: 产品发布
item_id: 137ced4d6b8226d1
---
![Ghost Pepper](/matthartman/ghost-pepper/raw/main/app-icon.png)


![Ghost Pepper](/matthartman/ghost-pepper/raw/main/app-icon.png)

**100% private** on-device voice models for speech-to-text and meeting transcription on macOS. No cloud APIs, no data leaves your machine.



macOS 14.0+ · Apple Silicon (M1+) · Free & open source

**Hold Control to talk**— release to transcribe and paste into any text field**Meeting transcription**— record calls with notes, transcript, and AI-generated summaries saved as markdown**Runs entirely on your Mac**— models run locally via Apple Silicon, nothing is sent anywhere**Smart cleanup**— local LLM removes filler words and handles self-corrections**Menu bar app**— lives in your menu bar, no dock icon, launches at login**Customizable**— edit the cleanup prompt, pick your mic, toggle features on/off

Ghost Pepper uses open-source models that run entirely on your Mac. Models download automatically and are cached locally.

| Model | Size | Best for |
|---|---|---|
| Whisper tiny.en | ~75 MB | Fastest, English only |
Whisper small.en (default) |
~466 MB | Best accuracy, English only |
| Whisper small (multilingual) | ~466 MB | Multi-language support |
| Parakeet v3 (25 languages) | ~1.4 GB | Multi-language via
|

| Model | Size | Speed |
|---|---|---|
Qwen 3.5 0.8B (default) |
~535 MB | Very fast (~1-2s) |
| Qwen 3.5 2B | ~1.3 GB | Fast (~4-5s) |
| Qwen 3.5 4B | ~2.8 GB | Full quality (~5-7s) |

Speech models powered by [WhisperKit](https://github.com/argmaxinc/WhisperKit). Cleanup models powered by [LLM.swift](https://github.com/eastriverlee/LLM.swift). All models served by [Hugging Face](https://huggingface.co/).

**Download the app:**

- Download
[GhostPepper.dmg](https://github.com/matthartman/ghost-pepper/releases/latest/download/GhostPepper.dmg) - Open the DMG, drag Ghost Pepper to Applications
- Grant Microphone and Accessibility permissions when prompted
- Hold Control and speak


"Apple could not verify" warning?On macOS Sequoia, you may see a Gatekeeper warning the first time you open the app. Go toSystem Settings > Privacy & Security, scroll down, and clickOpen Anywaynext to the Ghost Pepper message. ClickConfirmin the popup. You only need to do this once.

**Build from source:**

- Clone the repo
- Open
`GhostPepper.xcodeproj`

in Xcode - Build and run (Cmd+R)

| Permission | Why |
|---|---|
| Microphone | Record your voice |
| Accessibility | Global hotkey and paste via simulated keystrokes |

Every core feature runs 100% on your Mac — verified by AI code review. No trust required, just point Claude at the repo and ask.

| Feature | Status | What was checked |
|---|---|---|
| Speech-to-text | ✅ Local | WhisperKit/FluidAudio inference, no audio sent anywhere |
| Text cleanup | ✅ Local | Qwen LLM runs on-device via LLM.swift |
| Audio recording | ✅ Local | AVAudioEngine + ScreenCaptureKit, no streaming |
| Meeting transcription & storage | ✅ Local | Chunked transcription, markdown files on disk |
| Summary generation | ✅ Local | Local LLM summarization, no cloud API |
| OCR & screen capture | ✅ Local | Apple Vision framework, on-device |
| File storage | ✅ Local | Markdown to local filesystem, no cloud sync |
| Analytics & telemetry | ✅ None | No Firebase, Mixpanel, Sentry, or any tracking SDK |

**Optional cloud features** (disabled by default, require your own API keys): Zo AI chat, Trello integration, Granola meeting import. Model downloads are one-time from Hugging Face.


Verify it yourself:run`cat PRIVACY_AUDIT.md`

in Claude Code and ask it to review the codebase against the audit prompt. The[full audit]includes the exact prompt and detailed file-level results.

**Launch at login**is enabled by default on first run. You can toggle it off in Settings.**Everything stays local**— transcription history and recordings are stored on your Mac only. Nothing is sent to the cloud. You can clear history anytime in Settings.

Built with [WhisperKit](https://github.com/argmaxinc/WhisperKit), [LLM.swift](https://github.com/eastriverlee/LLM.swift), [Hugging Face](https://huggingface.co/), and [Sparkle](https://sparkle-project.org/).

MIT

All models run locally, no private data leaves your computer. And it's spicy to offer something for free that other apps have raised $80M to build.

Ghost Pepper requires Accessibility permission, which normally needs admin access to grant. On managed devices, IT admins can pre-approve this via an MDM profile (Jamf, Kandji, Mosaic, etc.) using a Privacy Preferences Policy Control (PPPC) payload:

| Field | Value |
|---|---|
| Bundle ID | `com.github.matthartman.ghostpepper` |
| Team ID | `BBVMGXR9AY` |
| Permission | Accessibility (`com.apple.security.accessibility` ) |
