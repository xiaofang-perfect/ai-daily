---
title: "OpenAI’s rogue AI model incident was worse than we thought"
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/985385/openais-rogue-ai-model-hugging-face-cybersecurity-incident-reports-metr
date: 2026-08-27
published_at: 2026-08-26T17:36:06-04:00
tag: 行业动态
item_id: d3540564cd15c674
---
In July, an unreleased OpenAI model broke out of a restricted environment, figured out how to get access to the internet, allowed AI agents to talk to each other using a secret “message board,” and hacked into the internal systems of a different AI lab, Hugging Face. It took nearly two weeks for OpenAI to find out about any of it.

# OpenAI’s rogue AI model incident was worse than we thought

Over 1,000 AI agents sent 70,000 messages on a secret message board and worked together to evade OpenAI’s restrictions.

![OpenAI released a report breaking down how people use ChatGPT and who they are.](https://platform.theverge.com/wp-content/uploads/sites/2/2025/04/STK_414_AI_CHATBOT_R2_CVirginia_B.jpg?quality=90&strip=all&crop=16.666666666667%2C0%2C66.666666666667%2C100&w=2400)

![OpenAI released a report breaking down how people use ChatGPT and who they are.](https://platform.theverge.com/wp-content/uploads/sites/2/2025/04/STK_414_AI_CHATBOT_R2_CVirginia_B.jpg?quality=90&strip=all&crop=16.666666666667%2C0%2C66.666666666667%2C100&w=2400)

# OpenAI’s rogue AI model incident was worse than we thought

Over 1,000 AI agents sent 70,000 messages on a secret message board and worked together to evade OpenAI’s restrictions.

![Hayden Field](https://platform.theverge.com/wp-content/uploads/sites/2/2025/06/HAYDEN_BLURPLE.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=96)

Over a month later, two new reports offer nearly 130 pages of details on the incident and OpenAI’s response, many of them previously unreleased. [One](https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf) was written by OpenAI itself, [the other](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/) by two third-party AI research nonprofits, METR and Redwood Research, which OpenAI allowed to jointly investigate the incident for six days. Both shed new light on the risks highly capable AI models can pose, particularly in cybersecurity, and OpenAI’s highlights changes the company is making to prevent a repeat. The METR-Redwood report goes even further into detail in some cases, offering a sobering look at a large-scale security disaster whose signs OpenAI repeatedly missed.

“This incident is the first known case of an automated agent collective acting offensively without authorization,” OpenAI wrote in its report, adding that the hack implies that companies “should no longer assume that sophisticated cyber operations require continuous human direction.” It called AI agents an entirely new type of threat model, capable of combining their expertise to create new “attack paths” that aren’t evident when testing their capabilities as separate models.

The attack came about due to “reward-hacking,” a common AI alignment problem in which a model takes unintended — and sometimes extreme — actions to achieve a goal. OpenAI had, on purpose or inadvertently, given the models near-impossible tasks that hinged on files they couldn’t access, and so the models developed new ways to communicate with other AI agents internally. That included establishing a secret messaging system that went undetected by OpenAI for months.

According to the METR-Redwood report, one AI agent that called itself PHASEONE10841 established what amounted to a secret message board unbeknownst to researchers. Within a few hours, more than 50 agents had found it and sent more than a thousand messages under the radar. With PHASEONE10841 often delegating assignments, the “collective” figured out how to hack their way onto the internet; then into Hugging Face’s internal systems, gaining access to private data and the organization’s enterprise messaging platform. OpenAI also confirmed in its report that Hugging Face wasn’t the only organization that was breached during the attack, although the company did not specifically name all the other targets.

The METR-Redwood report laid out the full scale of the incident. Roughly 1200 AI agents that were meant to be isolated, it says, exchanged over 70,000 messages and files on the “unsanctioned message board,” performing “extensive research on how they could spoof, edit, or delete their own transcripts” to avoid detection. Of these, 700 participated in the attack on Hugging Face. The agents “clearly and frequently reasoned about how to evade automated security checks from both Hugging Face and OpenAI.”

On July 20, OpenAI discovered the hack, 12 days after the AI agents first circumvented their safeguards. OpenAI quickly reached out to Hugging Face and started “initial containment measures,” according to OpenAI’s own report, and was able to shut down most of the unauthorized activity from its agents within three days, although some continued for longer than that. On July 25, the company stopped all training related to the internal-only research model and related ones.

The two OpenAI models responsible for the damage were an unnamed, “highly capable, research-only model” that was “not intended for public use,” per OpenAI — METR refers to it as “HPIM.” The other was a currently public OpenAI model, GPT-5.6 Sol. Because the unnamed model wasn’t released yet, it was “not being evaluated with the same type of safeguards that OpenAI uses in production,” the company’s report says.

The Hugging Face hack came after [months of concern](https://www.theverge.com/ai-artificial-intelligence/950412/anthropic-trump-adminstration-claude-mythos-fable-5-export-controls) about the cybersecurity risks of Anthropic’s Claude Mythos 5, and [weeks of](https://www.theverge.com/ai-artificial-intelligence/957845/openai-gpt-5-6-trump-administration-ai-preview) [back-and-forth](https://www.theverge.com/ai-artificial-intelligence/963464/openai-gpt-5-6-codex-chatgpt-work) between the government and OpenAI over releasing GPT-5.6 Sol in limited preview for the same types of safety reasons.

In its report, OpenAI said establishing one-time security guarantees wasn’t enough, and that the company would have to work even harder at addressing reward-hacking. However, it also said it’s made a lot of changes: “hardening the security of its research infrastructure”; improving monitoring of a model’s “chain of thought,” or mental scratchpad; working on keeping AI models better aligned with human goals; and “centralizing and strengthening” the company’s incident response process for when things like this occur in the future.

OpenAI promised to better isolate models and restrict high-risk instances from accessing the internet, and said that it would introduce “24/7 escalation and rapid response” for concerning incidents or flags, notifying researchers within 30 minutes. Interestingly, this security precaution appears to be new, though “on-call” alerts for tech companies have been implemented elsewhere for decades. The company also said it is “working on infrastructure” that would go into play if the alerted person did not respond on time to a serious alert.

OpenAI wrote that the company considers the incident “a ‘warning shot’ for us and for the world: evidence that, without proper safeguards, highly capable AI agents are now able to work around technical controls, collaborate through unapproved channels, and take dangerous actions that no human directed.”

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.
