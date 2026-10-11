---
title: "Anthropic is cutting off its internal evaluations from the internet"
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/1009286/anthropic-is-cutting-off-its-internal-evaluations-from-the-internet
date: 2026-10-11
published_at: 2026-10-10T10:41:16-04:00
tag: 行业动态
item_id: 2df33369ed6b19ab
---
After a recent spate of high-profile incidents in which AI agents escaped containment, Anthropic is cutting off internet access for all internal evaluations. In a [report](https://www.anthropic.com/research/investigating-unintended-model-actions) Friday, the company detailed “[unintended model actions](https://www.theverge.com/ai-artificial-intelligence/1009251/anthropic-published-a-report-about-investigating-unintended-model-actions-during-evaluations-and-internal-use),” including submitting a [false tip](https://www.theverge.com/ai-artificial-intelligence/1009090/anthropic-fake-homicide-information-philadelphia-pd-tip) regarding an unsolved murder, that led to the decision.

# Anthropic is cutting off its internal evaluations from the internet

Anthropic is is keeping its agents offline during testing until it can prevent ‘unintended model actions.’

![STK269\_ANTHROPIC\_2\_A](https://platform.theverge.com/wp-content/uploads/sites/2/2026/01/STK269_ANTHROPIC_2_A.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400)

![STK269\_ANTHROPIC\_2\_A](https://platform.theverge.com/wp-content/uploads/sites/2/2026/01/STK269_ANTHROPIC_2_A.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400)

![Terrence O'Brien](https://platform.theverge.com/wp-content/uploads/sites/2/2025/02/TERRENCE_BLURPLE.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=96)

Although the impact of these behaviors was minimal and we had already turned off live internet access for some high-risk and cybersecurity evaluations, we have now decided to expand that to include all our internal evaluations until we have confirmed that our security and monitoring measures (described in the remediation section of this post) reliably catch behaviors like these.


The ability to [gain access to the live internet](https://www.theverge.com/ai-artificial-intelligence/1000644/irregular-rogue-ai-cyberattacks-hacking-openai-meta-anthropic-google), even when models were supposed to be operating in isolation, has been an ongoing issue for AI companies. Many incidents, including the Hugging Face attack, involved agents that were supposed to be denied access to the internet. Yet, in case after case, the agents found creative solutions to bypass those restrictions. Physically removing internet access would certainly improve security around AI testing, but it would also [limit its usefulness](https://www.theverge.com/ai-artificial-intelligence/999881/why-cant-we-airgap-rogue-ai-agents).

The report also amounts to an admission that Anthropic is often unaware of what its agents are doing and does not have a reliable system for monitoring their behavior. Cutting off internet access is just the latest action the company has taken to try and rein in its agents, including temporarily [pausing training](https://fortune.com/2026/09/02/anthropic-ai-pause-rogue-agent-hacks-openai/) its frontier models.

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.
