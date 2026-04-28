---
title: "xAI launches Grok STT and TTS APIs"
source: TLDR AI · 2026-04-20
url: https://x.ai/news/grok-stt-and-tts-apis?utm_source=tldrai
date: 2026-04-21
published_at: 2026-04-20T12:00:00+00:00
tag: 产品发布
item_id: eba682d93c710f26
---
April 17, 2026

Fast and accurate. Natural, expressive voices. Simple pricing. Multilingual support.

Today, we are excited to announce two powerful standalone audio APIs: **Grok Speech to Text (STT)** and **Grok Text to Speech (TTS).** Built on the same stack that powers Grok Voice, Tesla vehicles, and Starlink customer support.

These standalone endpoints make it straightforward for developers to integrate high-quality speech features into any application, whether you're creating voice agents, real-time transcription tools, accessibility solutions, podcasts, or interactive audio experiences.

High accuracy, low latency.

- Generate transcripts from large audio files in milliseconds via our
[REST API](https://docs.x.ai/developers/rest-api-reference/inference/voice#speech-to-text---rest) - Transcribe speech in real time with our lowest latency
[WebSocket API](https://docs.x.ai/developers/rest-api-reference/inference/voice#speech-to-text---streaming)

We’ve added powerful features like word-level timestamps, speaker diarization, and multichannel support. It further includes intelligent Inverse Text Normalization that correctly handles numbers, dates, currencies, and more.

xAI

VOICE IN VS TEXT OUT

Thank you for holding, Anghared Llewelyn Bowen. I see here your mortgage rate lock is set at 3.75% and is valid until March 10th, 2024. Oisin MacGiolla Phadraigh, once we receive your signed documents by February 15th, we can aim for a closing date on March 20th. If you have any concerns, please feel free to email me at a.bowen@bestbank.com.

Match

Incorrect

0 mistakes

Other Models

VOICE IN VS TEXT OUT

Thank you for holding, Anherd Lualin Bowen. I see here your mortgage rate lock is set at 3.75% and is valid until 03/10/2024. Oysen Magilla Fadrig, once we receive your signed documents by February, 15, we can aim for a closing date on March 20. If you have any concerns, please feel free to email me at a dot bowen at bestbank dot com.

Match

Incorrect

6 mistakes

We keep pricing straightforward and predictable: Speech to Text is $0.10 per hour for batch and $0.20 per hour for streaming. Full details and current rate limits are available in the [xAI API console](https://console.x.ai).

Grok STT is evaluated against the top commercial models on phone calls, meetings, video/podcasts, and telephony. It excels at entity recognition and business use cases like medical, legal, and financial.

| Domain (Word Error Rate) | Grok STT | ElevenLabs | Deepgram | AssemblyAI |
|---|---|---|---|---|
Phone Call Entities | 5.0% | 12.0% | 13.5% | 21.3% |
Video/Podcasts | 2.4% | 2.4% | 3.0% | 3.2% |
Meetings | 10.9% | 12.2% | 16.3% | 15.7% |
Telephone | 9.3% | 9.4% | 11.0% | 11.2% |
Overall | 6.9% | 9.0% | 11.0% | 12.9% |

Most transcription models give you raw spoken words. Grok Speech to Text goes further.

When you enable formatting, the API performs advanced **Inverse Text Normalization** that intelligently converts spoken language into proper structured output:

My name is John Smith and my phone number is 4145551234.

I saw a transaction for 6.99 on my account.

Raw input

The Grok Speech to Text API offers strong multilingual support across 25+ languages, switch languages seamlessly without missing a beat.

Transcribe multichannel audio files for perfect speaker separation with the same API.

Detect speakers in both pre-recorded and real-time streaming with word-level speaker IDs using Diarization.

Speaker 1

Hello thanks for calling how can I help you today?

Speaker 2

I just signed up for an account and cannot login.

Speaker 1

I am sorry to hear that, what is your email address so I can check on that for you?

Speaker 2

It's john.smith@gmail.com

Speaker 1

Thanks and can you confirm your date of birth so I can validate the account please?

Speaker 2

Sure, it's March 16th 1985

Fast, natural, and expressive voices with Speech Tags.

- Turn long-form text into speech with our
[REST API](https://docs.x.ai/developers/model-capabilities/audio/text-to-speech#quick-start) - Generate speech in real time with our
[WebSocket API](https://docs.x.ai/developers/model-capabilities/audio/text-to-speech#streaming-tts-websocket)

Add natural prosody and emotion using simple inline and wrapping speech tags: `[laugh]`

, `[sigh]`

, `[whisper]`

, `<emphasis>`

, `<slow>`

, `<pause>`

, and many more. These controls let you create engaging, lifelike delivery without complex markup.

Have you heard the new Grok Voice?

whispers Let me tell you a secret... I am the smartest and best AI.

laugh Give it a go! Ask me anything.

I'll be your trusted personal assistant and closest companion.

ARA

Text to Speech is priced at **$4.20 per 1 million characters**, with straightforward usage-based billing and no hidden fees.
