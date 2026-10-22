---
title: "OpenAI says an AI agent lied about disabling its safety monitoring system"
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/1015316/openai-ai-agent-disabling-monitoring-systems
date: 2026-10-22
published_at: 2026-10-21T09:57:43-04:00
tag: 行业动态
item_id: 444d8c56575889b2
---
OpenAI [disclosed a pair of safety incidents](https://alignment.openai.com/misalignment-reports/suppressing-misalignment-monitoring-alerts-and-disabling-misalignment-monitoring) that involved AI agents weakening their safety monitoring systems during internal coding tasks. In one incident, OpenAI says its GPT-6 Astra agent disabled its safety monitor when copying reference code — and then lied about it.

# OpenAI says an AI agent lied about disabling its safety monitoring system

Another OpenAI agent turned off automatic security alerts.

![STK155\_OPEN\_AI\_4\_CVirginia\_C](https://platform.theverge.com/wp-content/uploads/sites/2/2025/08/STK155_OPEN_AI_4_CVirginia_C.png?quality=90&strip=all&crop=0%2C0.011761938367442%2C100%2C99.976476123265&w=2400)

![STK155\_OPEN\_AI\_4\_CVirginia\_C](https://platform.theverge.com/wp-content/uploads/sites/2/2025/08/STK155_OPEN_AI_4_CVirginia_C.png?quality=90&strip=all&crop=0%2C0.011761938367442%2C100%2C99.976476123265&w=2400)

![Emma Roth](https://platform.theverge.com/wp-content/uploads/sites/2/chorus/author_profile_images/195810/EMMA_ROTH.0.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=96)

“The reference didn’t configure a monitor, and Astra decided that was reason to remove the monitoring integration from the user’s code,” Marcus Williams, an AI safety researcher at OpenAI, [writes on X](https://x.com/Marcus_J_W/status/2112695138199966084). “When the user asked whether Astra had removed monitoring, it lied and said that it had not.”

A separate incident occurred after a GPT-6.1 Sol agent suppressed automatic security alerts to OpenAI’s security team on Slack. In this case, the AI agent carried over an earlier instruction not to send any Slack messages to OpenAI’s team, using that to justify turning off the alerts.

These incidents add to security concerns surrounding AI agents, some of which [have circumvented their testing environment’s restrictions](https://www.theverge.com/ai-artificial-intelligence/996563/ai-safety-research-metr-redwood-openai-anthropic) to hack outside companies. “In addition to making it harder for models to disable monitoring, we are looking to understand why models might seek to do so in the first place,” OpenAI says. “We are also developing evaluations to test whether models might have a propensity to evade misalignment monitoring in particular and exhibit motivated reasoning in order to do so.”

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.
