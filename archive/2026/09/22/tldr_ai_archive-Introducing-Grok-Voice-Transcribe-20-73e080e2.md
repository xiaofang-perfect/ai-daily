---
title: "Introducing Grok Voice Transcribe 2.0"
source: TLDR AI · 2026-09-21
url: https://x.ai/news/grok-voice-transcribe-2?utm_source=tldrai
date: 2026-09-22
published_at: 2026-09-21T12:00:00+00:00
tag: 产品发布
item_id: 73e080e28a087c6f
---
Announcing SpaceXAI's newest speech-to-text model, with unparalleled accuracy and cost effectiveness.

Today we're releasing Grok Voice Transcribe 2.0, our latest speech-to-text model. Across our real-world evaluations, Grok Voice Transcribe 2.0 is one of the most accurate transcription models available today and twice as accurate as Grok Voice Transcribe 1.0, at the same price.

Grok Voice Transcribe 2.0 is built on the audio foundation model behind Grok Voice. Grok Voice already powers tens of thousands of customer-support calls a day, transcribes millions of hours of video narration, and runs voice agents in physical products, including the Grok assistant in Tesla vehicles. It is trained on a unique dataset of live, noisy, multilingual audio recorded across a diverse set of environments and refined with post-training.

The result is one of the most accurate transcription models for speech in real-world settings.

Most transcription models do well on clean, single-speaker audio. Real-world audio is harder: flaky phone lines, competing voices, local accents, and phone numbers or email addresses read aloud. We built Grok Voice Transcribe 2.0 for the hardest audio across conditions and environments.

On the public Artificial Analysis leaderboard, Grok Voice Transcribe 2.0 ranks first for accuracy among 32 streaming models.

Upper and to the right is better.

Source: [Artificial Analysis](https://artificialanalysis.ai/speech-to-text/streaming)

In addition to public benchmarks, we measure word error rate on four internal sets drawn from production traffic: telephony audio from customer-support calls, conversations with Grok, spoken credentials such as account codes and email addresses, and short multilingual voice commands. Grok Voice Transcribe 2.0 improves on Grok Voice Transcribe 1.0 across all four, and on telephony it leads every model we tested.

Customer support calls · English

Conversations with Grok · English

Phone numbers, emails, addresses · English

Voice-assistant utterances · 19 languages

Grok Voice Transcribe 2.0 transcribes dozens of languages, detects the language automatically, and follows mid-recording switches in a single pass. Multilingual accuracy is its largest improvement over Grok Voice Transcribe 1.0.

Word Error Rate (%). Lower is better.

Grok Voice Transcribe 2.0

Grok Voice Transcribe 1.0

ElevenLabs Scribe v2

Deepgram Nova-3

Short phrases such as in-car commands give the model little context to identify the language. On our short-phrase set, word error rate drops from 20.6% to 6.8%.

Grok Voice Transcribe 2.0 supports advanced configuration and controls. Existing Speech-to-Text API integrations get the accuracy improvement with no code changes:

- **Batch and streaming.** Transcribe recorded files and URLs, or transcribe an audio stream in real time.
- **Word-level timestamps.** Each word has precise start/end times and confidence scores.
- **Speaker diarization.** Label each speaker in the transcript, at no additional cost.
- **Multichannel transcription.** Transcribe up to 8 channels independently.
- **Key term biasing.** Pass up to 100 domain terms per request, such as product names or medical vocabulary.
- **Text formatting.** Numbers, dates, currencies, phone numbers, and email addresses are returned in written form.
- **Filler word removal.** Omit fillers such as "um" and "uh" from the transcript.
- **Smart turn detection.** Detect the end of a speaker's turn for voice agents.

[Atlassian Loom](https://www.loom.com/) is widely used for recording and sharing screen recordings. Atlassian found Grok Voice Transcribe 2.0 more accurate than their existing solution for transcribing Loom videos. Accurate transcripts open up new AI workflows: record an action plan in Loom, pipe the transcript into Cursor, and it makes the code updates directly.

“We've always believed the best way to move work forward is to capture context once and let it flow everywhere. With Grok powering Loom's speech-to-text and Cursor turning that into code, we're closing the loop from context to code: record what you mean, and the work gets done. It's a glimpse of where AI-assisted development is headed.”

Grok Voice Transcribe 2.0 pricing is identical to Grok Voice Transcribe 1.0. Batch transcription remains $0.10 per hour of audio and streaming $0.20 per hour, with diarization, timestamps, and key terms included.

USD per hour of audio

Grok Voice Transcribe 2.0 will soon be the default in the Speech-to-Text API, and Grok Voice Transcribe 1.0 will be deprecated in the coming weeks. To stay on it during the transition, pin `grok-voice-transcribe-1.0`.
