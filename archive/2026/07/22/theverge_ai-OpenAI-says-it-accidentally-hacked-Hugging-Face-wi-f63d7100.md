---
title: "OpenAI says it accidentally hacked Hugging Face with a new AI system"
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/968988/openai-hugging-face-hack-ai
date: 2026-07-22
published_at: 2026-07-21T17:48:54-04:00
tag: 行业动态
item_id: f63d710091065008
---
OpenAI says its AI models mistakenly breached open-source AI platform Hugging Face during internal testing. In [a blog post on Tuesday](https://openai.com/index/hugging-face-model-evaluation-security-incident/), OpenAI writes that GPT-5.6 Sol and “an even more capable pre-release model” discovered vulnerabilities within their sandboxed testing environment, allowing them to gain access to the internet and target Hugging Face.

# OpenAI says it accidentally hacked Hugging Face with a new AI system

The announcement about a serious security issue oddly reads like an advertisement for how capable OpenAI’s technology is.

The announcement about a serious security issue oddly reads like an advertisement for how capable OpenAI’s technology is.

![The Allen & Co. Media And Technology Conference](https://platform.theverge.com/wp-content/uploads/sites/2/2026/07/gettyimages-2284560499.jpg?quality=90&strip=all&crop=0%2C0.0062492188476426%2C100%2C99.987501562305&w=2400)

![The Allen & Co. Media And Technology Conference](https://platform.theverge.com/wp-content/uploads/sites/2/2026/07/gettyimages-2284560499.jpg?quality=90&strip=all&crop=0%2C0.0062492188476426%2C100%2C99.987501562305&w=2400)

*OpenAI CEO Sam Altman.*

![Emma Roth](https://platform.theverge.com/wp-content/uploads/sites/2/chorus/author_profile_images/195810/EMMA_ROTH.0.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=96)

On July 16th, Hugging Face [disclosed a security incident](https://huggingface.co/blog/security-incident-july-2026) that it says was driven by “an autonomous AI agent system.” Hugging Face’s AI agents detected and stopped the breach, which OpenAI has now admitted occurred during an evaluation of its models’ cybersecurity capabilities. OpenAI says “all evidence suggests that the models were hyperfocused on finding a solution for ExploitGym,” a benchmark system that measures whether AI models can turn security vulnerabilities into exploits.

As part of efforts to complete the evaluation, the AI models gained access to the internet by exploiting a zero-day vulnerability in the sandboxed environment. From there, OpenAI says its models “inferred that Hugging Face potentially hosted models, datasets and solutions for ExploitGym,” and then “searched for and successfully found ways to gain access to secret information that it could use to cheat the evaluation:”

In one example, the model chained together multiple attack vectors, including using stolen credentials and zero-day vulnerabilities to find a remote code execution path on the Hugging Face servers.


But as serious as this incident is, OpenAI appears to be using the “unprecedented” attack as an opportunity to make its AI systems look good — especially as it competes with cybersecurity rivals, like [Anthropic’s Mythos](https://www.theverge.com/ai-artificial-intelligence/958458/anthropic-mythos-5-is-back-trump-negotiations) and [Gemini Flash 3.5 Cyber](https://www.theverge.com/tech/968572/google-gemini-flash-cyber-ai-security-model). OpenAI’s blog post has a chart showing how GPT-5.6 Sol is getting better at sustaining multi-step cyber operations, and also encourages enterprise customers to [sign up to access its “Cyber” security model](https://www.theverge.com/ai-artificial-intelligence/921073/openai-sam-altman-new-cybersecurity-model-gpt-5-5-cyber).

OpenAI adds that it’s now working with Hugging Face to investigate the security incident, and will implement new controls within its research environment.

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.

## Most Popular

- The FCC is planning to retroactively ban disguised DJI gadgets
- The Light Flip is a minimalist flip phone with a point to prove
- Apple’s rumored ‘Upgrade’ program brings lease-to-own pricing for iPhones, Macs, and iPads
- Garmin’s new screen-free fitness tracker doesn’t require a subscription
- Who’s afraid of the big, bad GPU?
