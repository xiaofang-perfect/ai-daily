---
title: "Meta's Muse Voice Transcribe"
source: TLDR AI · 2026-09-02
url: https://research.meta.ai/blog/introducing-muse-voice-transcribe?utm_source=tldrai
date: 2026-09-03
published_at: 2026-09-02T12:00:00+00:00
tag: 产品发布
item_id: 7cb708fb693ba4b6
---
# Introducing Muse Voice Transcribe

We’re excited to introduce Muse Voice Transcribe, the first real-time audio perception model developed by Meta Superintelligence Labs.

Muse Voice Transcribe marks a first milestone in bringing our real-time voice models to you. It delivers real-time streaming ASR, diarization with 20+ speakers, and endpointing. It is multilingual with seamless code-switching and improves accuracy with language, keyword, and context biasing.

We rank first on Artificial Analysis on streaming speech-to-text and on public diarization benchmarks. Model inclusion and rankings as of September 1, 2026.

![Bar chart of final-transcription streaming word error rate, with Muse Voice Transcribe lowest at 3.1 percent and seven other systems ranging from 3.4 to 4.0 percent.](https://research.meta.ai/_next/image?url=%2Farticles%2Fintroducing-muse-audio%2Fbenchmarks%2Fstreaming-final-transcription-wer-v1.png&w=3840&q=90&dpl=dpl_5rUkgVNQsZLqPX7kUV7cj5EjizMr)

![Bar chart of average diarization error rate across AMI-IHM, AMI-SDM, and VoxConverse, with Muse Voice Transcribe lowest at 17.5 percent and five other systems ranging from 21.1 to 28.6 percent.](https://research.meta.ai/_next/image?url=%2Farticles%2Fintroducing-muse-audio%2Fbenchmarks%2Fstreaming-diarization-der-v1.png&w=3840&q=90&dpl=dpl_5rUkgVNQsZLqPX7kUV7cj5EjizMr)

## Streaming ASR as the Foundation

Muse Voice Transcribe is an autoregressive multimodal model from the Muse Spark family.

Audio is processed in 80ms chunks (12.5 Hz), each of which is transformed into a single soft token. At each audio chunk, the model decides to either continue listening to the next audio chunk or emit a text token. When the model decides to continue listening, it predicts a `<|next_audio|>` special token and replaces `<|next_audio|>` with the actual audio chunk for the next input.

When the audio stream stops, we insert a special `<|empty_audio|>` token to inform the model there are no more audio chunks. The model emits all remaining text tokens without producing any `<|next_audio|>` tokens after seeing `<|empty_audio|>`.

Since the model has full control over when to listen, it decides on the amount of audio context before transcribing a word (we call this “delay”). There is a tradeoff between accuracy and delay. The longer the model waits to predict, the more accurate the transcript, but the higher the latency. Muse Voice Transcribe has “adaptive delay,” dynamically changing delay for each word based on difficulty. This is enabled with reinforcement learning (RL), where word error rate (WER) reward and a delay reward are combined multiplicatively.

With adaptive delay, Muse Voice Transcribe achieves the Pareto front on speed-accuracy trade-off measured by time to final transcription.

![Scatter plot comparing final-transcription word error rate with time to final transcription. Muse Voice Transcribe reaches about 3.0 percent error at 0.16 seconds, below the dotted previous Pareto frontier formed by Soniox, Cartesia, and ElevenLabs systems; the other current systems shown have higher error or latency.](https://research.meta.ai/_next/image?url=%2Farticles%2Fintroducing-muse-audio%2Fbenchmarks%2Fadaptive-delay-speed-accuracy-v4.png&w=3840&q=90&dpl=dpl_5rUkgVNQsZLqPX7kUV7cj5EjizMr)

## Building Diarization and Endpointing on Top of ASR

With streaming ASR as the foundation, we can easily support other audio perception tasks by introducing additional special tokens.

For diarization, we introduce a `<|start_of_turn|>` token to mark potential speaker switch and `<|speaker_{A-Z}|>` tag to differentiate the speaker. `<|start_of_turn|>` is predicted as soon as speaker switches and speaker tag prediction is delayed to the end of the chunk. The audio from the same speaker may also be segmented by `<|start_of_turn|>` but the speaker tag will be the same for all these segments.

Here is an example token sequence for diarization (we omit `<|next_audio|>` for simplicity):

`<|start_of_turn|>Hello, how are you doing?<|speaker_A|><|start_of_turn|> Did anything fun over the weekend?<|speaker_A|><|start_of_turn|> Hey I'm good!<|speaker_B|>`
For endpointing, we introduce a `<|speech_onset|>` token to mark beginning of the speech and `<|speech_endpoint|>` token to mark when the user finishes speaking.

Here is an example token sequence for endpointing (we omit `<|next_audio|>` for simplicity):

`<|speech_onset|>Hey Meta, what's the weather in Menlo Park?<|speech_endpoint|> [silence] <|speech_onset|>What should I wear today?<|speech_endpoint|>`
We train both tasks together with streaming ASR and add extra rewards on top of the ASR reward for diarization and endpointing respectively.

## Capabilities

### Language Coverage

Muse Voice Transcribe is trained with 70+ languages, of which 25 are extensively verified. In the initial release, we recommend trying these [25 validated languages](https://dev.meta.ai/docs/speech-to-text#language-biasing), with support for additional languages also available.

### Code-Switching

Code-switching is very common for bilingual speakers. Muse Voice Transcribe natively supports arbitrary code-switching, either within sentence or between sentence. In this audio clip, it also uses context biasing to further improve recognition accuracy.

### Long Context

Our model natively supports long audio input exceeding one hour and up to 20+ speakers, with no required post-processing.

- Speaker A
- Speaker B
- Speaker C
- Speaker D
- Speaker E
- Speaker F
- Speaker G
- Speaker H
- Speaker I
- Speaker J
- Speaker K

## Applications

With one click, voice dictation across Meta AI and Muse Code is now powered by Muse Voice Transcribe. It can be used with any application and work through tasks with Meta AI and any window on your screen — just hold 'Fn' to try.

Muse Voice Transcribe is available today via Meta Model API, [Meta AI for Mac](https://ai.meta.com/meta-ai/download/), and Muse Code.
