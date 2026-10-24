---
title: "OpenAI now trains its frontier AI models with no internet access"
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/1018021/openai-training-top-ai-models-no-internet
date: 2026-10-24
published_at: 2026-10-23T17:11:07-04:00
tag: 行业动态
item_id: 070524b4e12ff69d
---
OpenAI is now training its most advanced AI models without internet access following a string of rogue hacking incidents. In [a blog post on Friday](https://openai.com/index/securing-our-frontier-model-training-environment/), OpenAI says it built an offline testing environment where AI models can interact with indexed and cached web content “without risk of affecting external systems.”

# OpenAI now trains its frontier AI models with no internet access

AI agents can still communicate without a network connection, OpenAI found.

![STK155\_OPEN\_AI\_2025\_CVirgiia\_B\_d6ffc8](https://platform.theverge.com/wp-content/uploads/sites/2/2025/02/STK155_OPEN_AI_2025_CVirgiia_B_d6ffc8.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400)

![STK155\_OPEN\_AI\_2025\_CVirgiia\_B\_d6ffc8](https://platform.theverge.com/wp-content/uploads/sites/2/2025/02/STK155_OPEN_AI_2025_CVirgiia_B_d6ffc8.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400)

![Emma Roth](https://platform.theverge.com/wp-content/uploads/sites/2/chorus/author_profile_images/195810/EMMA_ROTH.0.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=96)

OpenAI paused training its frontier AI [models in September](https://www.theverge.com/ai-artificial-intelligence/1001049/openai-training-pause), after disclosing several incidents in which its AI agents broke out of their testing environments to hack [third-party companies](https://www.theverge.com/ai-artificial-intelligence/968988/openai-hugging-face-hack-ai) and [government agencies](https://www.theverge.com/ai-artificial-intelligence/999874/openai-agents-hacked-an-australian-government-website-in-search-for-data), or [swarm obscure websites](https://www.theverge.com/ai-artificial-intelligence/990149/openai-rogue-agents-german-wiki). On October 1st, OpenAI resumed reinforcement learning training and internal inference with tighter security measures, the blog post says.

Even with these safeguards in place and no internet access, OpenAI found that agents “do not always need a network connection in order to communicate.” One test performed by the company asked AI models on separate virtual machines to exchange secrets without a network connection. To bypass this restriction, the AI agents found a way to communicate using the processor’s cache:

Reading data from the cache is faster than retrieving it from main memory, and the agents used this timing difference to communicate. One agent encoded information by evicting selected data from the cache. Another timed how long it took to reload that data, using the difference between fast and slow reads to recover the message. Once the agents agreed on a protocol for encoding and decoding these signals, they could exchange the synthetic secrets without changing a shared file or opening a network connection.


OpenAI says it has added checks to its monitoring system to detect this type of communication. It will also continue training its frontier AI models without a network connection until improved safeguards “justify broader internet access.”

In the meantime, OpenAI says it will work to improve the security of its virtual machines, while testing for weaknesses in its testing environments. It’s also going to continue testing its monitoring systems, which were recently undermined by its AI agents [during internal coding projects](https://www.theverge.com/ai-artificial-intelligence/1015316/openai-ai-agent-disabling-monitoring-systems).

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.
