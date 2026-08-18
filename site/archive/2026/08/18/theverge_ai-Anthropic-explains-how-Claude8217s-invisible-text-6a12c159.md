---
title: "Anthropic explains how Claude&#8217;s invisible text watermarks will work"
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/980869/anthropic-claude-watermarks-synthid-text-system
date: 2026-08-18
published_at: 2026-08-17T06:57:13-04:00
tag: 产品发布
item_id: 6a12c159d1d8e5c8
---
Anthropic has clarified how it’s planning to apply invisible watermarks to Claude-generated text in order to comply with Europe’s AI transparency rules. On Friday, [Anthropic announced](https://www.anthropic.com/news/claude-text-watermark) that Claude’s text marking system is “a version of the SynthID-Text approach” — an open-source watermarking technology [developed by Google DeepMind](https://www.theverge.com/2024/10/23/24277873/google-artificial-intelligence-synthid-watermarking-open-source) that creates detectable patterns using wording probabilities.

# Anthropic explains how Claude’s invisible text watermarks will work

It’s using ‘a version’ of the open-source SynthID-Text system Google developed.

![STKB364_CLAUDE_2_C_96d15c](https://platform.theverge.com/wp-content/uploads/sites/2/2026/01/STKB364_CLAUDE_2_C_96d15c.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400)

![STKB364_CLAUDE_2_C_96d15c](https://platform.theverge.com/wp-content/uploads/sites/2/2026/01/STKB364_CLAUDE_2_C_96d15c.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400)

![Jess Weatherbed](https://platform.theverge.com/wp-content/uploads/sites/2/chorus/author_profile_images/195820/JESSICA_WEATHERBED.0.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=96)

This watermarking feature, [alongside C2PA support](https://www.theverge.com/ai-artificial-intelligence/977823/anthropic-claude-ai-watermarks-c2pa-text-images) for Claude-processed images, is being introduced to meet Anthropic’s obligations under the [European Union’s AI Act](https://www.theverge.com/ai-artificial-intelligence/974571/eu-ai-act-transparency-labels-rules-deepfakes), which requires synthetic audio, image, video, and text to include machine-readable marks that enable the content to be detected as artificially generated or manipulated. Anthropic says the text watermarks won’t make Claude more expensive for users, or “have any practical impact on the quality or content of Claude’s outputs.” Here’s Anthropic’s explanation for how it works:

Take the sentence “The weather today was cold and…”. The next word is very unlikely to be “sugary.” But it is quite likely to be “overcast” or “grey.” Under most circumstances, it doesn’t matter much to the reader which of these latter two words the model ultimately chooses—the meaning of the sentence is largely the same either way. In cases like this, the choice is settled by a random number.

Watermarking uses low-stakes choices like these—which occur many times over a piece of generated text—to leave a pattern in Claude’s responses. That pattern is undetectable to the reader, but is detectable to anyone who has a key that encodes it. When watermarking is used, choices are still made at random, but the source of the randomness is different. Instead of using an arbitrary random number generator to pick the next word, watermarking uses the key and a few words that come before to settle what word the model should pick.


As Anthropic notes, the EU’s AI transparency requirements also impact other major AI developers, so Claude won’t be the only model introducing text watermarks. Google’s Gemini chatbot has supported the [SynthID-Text solution since 2024](https://deepmind.google/blog/watermarking-ai-generated-text-and-video-with-synthid/), and while OpenAI hasn’t detailed any [text watermarking plans](https://help.openai.com/en/articles/8912793-provenance-signals-content-credentials-synthid-in-openai-generated-content) for ChatGPT in its [AI Act compliance roadmap](https://help.openai.com/en/articles/12141645-eu-ai-act-openai-resources-and-customer-guidance), it will also be subject to the law’s requirements.

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.
