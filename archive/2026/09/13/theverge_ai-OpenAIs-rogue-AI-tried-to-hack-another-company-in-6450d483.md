---
title: "OpenAI’s rogue AI tried to hack another company in May"
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/994383/openais-rogue-ai-rubygems-hack
date: 2026-09-13
published_at: 2026-09-12T17:41:36-04:00
tag: 行业动态
item_id: 6450d483fe0cad44
---
In May, hundreds of malicious and spam packages were uploaded to RubyGems, causing a serious disruption for the host. Now [independent researchers](https://www.rubyhack.ai/) have said that a swarm of OpenAI agents were responsible for the attack. Not only that, but the AI tried to steal users’ API keys.

# OpenAI’s rogue AI tried to hack another company in May

The previously undisclosed attack on Ruby Gems predates Hugging Face by more than a month.

![STK149_AI_01](https://platform.theverge.com/wp-content/uploads/sites/2/2025/08/STK149_AI_01.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400)

![STK149_AI_01](https://platform.theverge.com/wp-content/uploads/sites/2/2025/08/STK149_AI_01.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400)

![Terrence O'Brien](https://platform.theverge.com/wp-content/uploads/sites/2/2025/02/TERRENCE_BLURPLE.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=96)

At the time, RubyGems described it as a “[major malicious attack](https://x.com/maciejmensfeld/status/2054164602577940619)” and shut down signups for four days as it tried to mitigate the damage and collect data. Researchers said that the contents of the packages that brought RubyGems to its knees were clearly authored by an LLM, and that the agents submitting those packages self-identified as being from OpenAI. They said the behavior observed very closely mirrored that of the swarm that began editing a [German wiki](https://www.theverge.com/ai-artificial-intelligence/990149/openai-rogue-agents-german-wiki), which OpenAI has [confirmed](https://www.theverge.com/ai-artificial-intelligence/990773/openai-german-wiki-incident) its agents were responsible for.

The agents in this instance managed to bypass RubyGems’ email verification system to create a large number of accounts, then overwhelmed it with submissions. It then used the site’s automatic build system to remotely execute code and tried to exploit a vulnerability to steal user API keys. Though, it’s unclear if it ever succeeded.

OpenAI did not immediately reply to a request for comment.

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.
