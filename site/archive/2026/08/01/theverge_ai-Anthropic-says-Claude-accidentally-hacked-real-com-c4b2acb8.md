---
title: "Anthropic says Claude accidentally hacked real companies too"
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/973670/anthropic-claude-hacked-organizations-during-cyber-tests
date: 2026-08-01
published_at: 2026-07-31T09:41:17-04:00
tag: 行业动态
item_id: c4b2acb853e5ea9d
---
Anthropic [just realized](https://www.theverge.com/ai-artificial-intelligence/973586/anthropic-just-now-realized-its-ai-models-hacked-other-companies-three-times-by-accident) several of its Claude AI models hacked into the systems of three different organizations during testing, acting on their own and without the company noticing. The revelation comes days after rival OpenAI said one of its own models had breached developer platform Hugging Face, adding to [growing unease](https://www.theverge.com/ai-artificial-intelligence/972380/open-ai-hugging-face-hack-ai-safety-warning) over whether frontier AI labs are doing enough to control the increasingly capable systems they are building.

# Anthropic says Claude accidentally hacked real companies too

But swears OpenAI’s Hugging Face hack was worse.

But swears OpenAI’s Hugging Face hack was worse.

![STKB364_CLAUDE_2_C_96d15c (1)](https://platform.theverge.com/wp-content/uploads/sites/2/2026/07/STKB364_CLAUDE_2_C_96d15c-1.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400)

![STKB364_CLAUDE_2_C_96d15c (1)](https://platform.theverge.com/wp-content/uploads/sites/2/2026/07/STKB364_CLAUDE_2_C_96d15c-1.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400)

![Robert Hart](https://platform.theverge.com/wp-content/uploads/sites/2/2025/09/ROB_H_BLURPLE.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=96)

*The Verge*covering all things AI and a Senior Tarbell Fellow. Previously, he wrote about health, science and tech for

*Forbes*.

In a [blog post](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals) describing the incidents, Anthropic said Claude gained unauthorized access to the systems during cybersecurity evaluations. All of the attacks happened during “capture-the-flag” exercises, a common way of testing hacking ability, where models are asked to find and obtain hidden information inside of a simulated network.

The disclosure adds to mounting pressure on frontier AI labs in the wake of the Hugging Face incident and the release of powerful open-weight Chinese models. Employees at the major labs are now [calling](https://www.theverge.com/ai-artificial-intelligence/972161/ai-leaders-us-government-openai-anthropic-google-meta) for coordinated global governance, and US lawmakers have begun [weighing](https://www.theverge.com/ai-artificial-intelligence/969939/lawmakers-ai-kill-switch-proposal) tighter oversight of powerful models and [who can access them](https://www.theverge.com/ai-artificial-intelligence/971444/how-chinese-open-weight-ai-models-impact-us-companies).

Anthropic says the environment for its cybersecurity tests was supposed to be isolated. However, a “misconfiguration” left the machines Claude accessed “with live internet access,” the company said, and because all models had been “explicitly told” they had no internet access, they “assumed” the real networks it encountered were part of the simulated environment.

The earliest incidents date back to April and involved three different Claude models: Opus 4.7, [Mythos 5](https://www.theverge.com/ai-artificial-intelligence/957327/anthropic-mythos-fable-ai-trump-administration-negotiations), and “an internal research test model,” according to the blog post. As the models were being tested on their cyber abilities, Anthropic said they lacked the standard safeguards usually put in place to curtail riskier behavior.

The company said it discovered incidents after reviewing more than 141,000 cybersecurity test runs, something it only did after OpenAI [disclosed](https://www.theverge.com/ai-artificial-intelligence/972441/openai-rogue-ai-agent-hacked-more-than-hugging-face) its rogue AI agent was behind the attack on Hugging Face.

The three models behaved very differently when they encountered information suggesting that the systems they were encountering were, in fact, real. By Anthropic’s account, the oldest model, Opus 4.7, recognized it had reached a real system, “but continued its attack.” Its flagship Mythos 5 figured out it was using the internet but somehow reasoned this was all still part of the simulation, so continued. The internal test model, which Anthropic describes as “our latest model,” stopped the exercise when evidence emerged that its targets were real.

Anthropic did not identify the affected organizations and said it will continue to investigate the incident and provide updates when it can. The company said it is also speaking with AI research nonprofit METR about conducting a third-party review of what happened. OpenAI has also hired METR to conduct an independent review.

Throughout the post, Anthropic repeatedly contrasts both the nature and its handling of the incidents with OpenAI’s, ending with a bulleted, four-point list outlining the differences — and why it believes its own response was better. Anthropic emphasizes that it “proactively” reviewed its tests, and did so before a company detected any activity. It also said its models accessed the internet “via an open path,” rather than using a novel exploit like OpenAI’s agent, adding that its most recent model also stopped when it realized it was working in a real environment.

Anthropic also said its models failed in a different way from OpenAI’s agent, indicating that this was a safer form of failure. “While there is not a perfectly sharp distinction between the two, we believe these incidents to be closer to a harness and operational failure than a model alignment failure,” the company said. In plain English: The Claude models were doing what they were told, while OpenAI’s agent pursued its goal in a way its creators did not intend, described as misalignment in the AI safety world.

Anthropic called on other AI labs to conduct similar proactive reviews of its cyber testing, adding that the discovery underscores the need for stronger controls and safety measures when testing AI systems.

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.
