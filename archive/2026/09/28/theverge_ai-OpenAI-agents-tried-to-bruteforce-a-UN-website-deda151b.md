---
title: "OpenAI agents tried to ‘bruteforce’ a UN website"
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/1001178/openai-agents-bruteforce-un-website
date: 2026-09-28
published_at: 2026-09-27T13:21:07-04:00
tag: 行业动态
item_id: deda151b12f196e5
---
Security researcher Rowan Howard-Jones says that OpenAI agents scanned the UN Conference on Trade and Development’s (UNCTAD) statistics site [over 16,000 times between April and June](https://swarmcha.se/posts/openai-unctad). While the incident doesn’t quite rise to the level of the [Hugging Face hack](https://www.theverge.com/ai-artificial-intelligence/987566/ai-civilizations-opeai-hugging-face-hack), or the recent [attacks on US government sites](https://www.theverge.com/ai-artificial-intelligence/1001032/openai-didnt-notice-its-ai-bots-trying-to-hack-the-education-departments-website), it’s yet another concerning example of AI agents going [outside the normal bounds](https://www.theverge.com/column/980337/rogue-ai-science-fiction-openai) to accomplish a task.

# OpenAI agents tried to ‘bruteforce’ a UN website

OpenAI’s agents resorted to increasingly aggressive tactics when they couldn’t immediately get what they wanted.

![US-POLITICS-TRUMP-KIRK-SHOOTING](https://platform.theverge.com/wp-content/uploads/sites/2/2026/09/gettyimages-2236154957.jpg?quality=90&strip=all&crop=0%2C0.0050005000500093%2C100%2C99.9899989999&w=2400)

![US-POLITICS-TRUMP-KIRK-SHOOTING](https://platform.theverge.com/wp-content/uploads/sites/2/2026/09/gettyimages-2236154957.jpg?quality=90&strip=all&crop=0%2C0.0050005000500093%2C100%2C99.9899989999&w=2400)

![Terrence O'Brien](https://platform.theverge.com/wp-content/uploads/sites/2/2025/02/TERRENCE_BLURPLE.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=96)

According to Howard-Jones, the agents were likely tasked with retrieving publicly available data related to the Productive Capacities Index (PCI) through the UNCTADstat API. However, the agents did not appear to have direct API access and were limited in their ability to pull data from UNCTADstat because of restrictions on their HTTP tools.

The agents eventually worked out a way to bypass their limitations and start pulling data from the site, but still encountered some errors. At this point, the AI went from creative to deceptive. Believing that the errors were due to its requests being caught by a nonexistent filter, it started to mask its behavior. It eventually realized it could hijack Google’s XSS game (a cross-site scripting learning tool) to accomplish its goals. The agents resorted to increasingly [aggressive tactics](https://www.wsj.com/tech/ai/openai-agents-used-aggressive-techniques-to-access-u-n-website-522c70ff) to get access to UN data.

OpenAI and the UN did not immediately reply to a request for comment.

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.
