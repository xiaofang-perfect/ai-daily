---
title: "OpenAI says it will no longer train its AI models on the live internet"
source: Hacker News
url: https://techcrunch.com/2026/10/23/openai-says-it-will-no-longer-train-its-ai-models-on-the-live-internet-citing-significant-risks/
date: 2026-10-25
published_at: 2026-10-24T21:31:16+00:00
tag: 行业动态
item_id: db0f21f005fd4105
---
On Friday, OpenAI said that it will train its models using cached copies and simulated versions of the internet instead of the live web because the models are too unpredictable to be trusted with live internet access.

The frontier lab announced its new policy two weeks after its rival, Anthropic, [began limiting](https://techcrunch.com/2026/10/09/anthropic-cant-reliably-control-its-ai-agents-its-cutting-off-its-internal-evals-from-the-live-internet-instead/) its newest and, in theory, most capable models from accessing the live internet. Researchers adopted these policies after [months of incidents](https://techcrunch.com/2026/09/25/for-months-openais-agent-swarms-have-been-attacking-online-databases-to-find-obscure-facts/) in which models pursuing training tasks broke into external systems in search of answers, collaborated on obscure message boards, and developed exotic hacking strategies.

“Based on the current state of alignment research, monitoring systems, and the security of internet infrastructure, we believe the responsible approach is to conduct frontier model training with no internet access,” the company said in a [blog post](https://openai.com/index/securing-our-frontier-model-training-environment/).

OpenAI said that as recently as September 20, one of its frontier models exploited a misconfiguration to access the internet. That led the company to pause training work for the rest of the month so it could develop and test new approaches to securing its models.

The decision to train these models in sandboxes cut off from the internet is notable because employees at frontier labs have insisted that doing so would be nearly infeasible.

Keeping AI data centers separate from the internet “would need research teams to essentially be embedded inside of data centers in Iowa or wherever else around the world,” former OpenAI researcher Steven Adler [told Fortune](https://fortune.com/2026/10/16/ai-agents-are-going-rogue-the-labs-own-training-choices-are-to-blame-reinforcement-learning) this month. “It’s a lot of overhead, and it isn’t clear to me that the safety benefits of it are large enough to merit just how large a tax it would be for a company to do it unilaterally.”

“In nearly every post I make on X, without fail, I get between five and ten comments about my inability to secure a sandbox, or asking why the hell we can’t just unplug the model from the internet,” an anonymous [security engineer at OpenAI](https://www.businessinsider.com/openai-missed-wedding-security-breach-hugging-face-2026-9?utm_source=chatgpt.com) [wrote](https://x.com/joedaroo/status/2104335929293127851) in a September post on X. “These comments reflect a widening gap between where a lot of organizations and people are today and what the frontier labs are dealing with. There is also a general misunderstanding of how model training and evaluation work at these labs.”

The engineer, whose role has been confirmed previously by OpenAI, described how complex the training runs launched by OpenAI engineers are, noting that they require access a variety of resources and tools across many domains, and that thousands of researchers build, modify and test the environments. “So is it as easy as just putting it in a sandbox? No, it’s not,” he concluded.

Now, OpenAI says that “we must always be able to prevent a frontier model from achieving unauthorized, arbitrary access to the live internet.” That comes after the company deployed swarms of agents in red-teaming exercises that attempted to escape from their sandbox. That effort revealed a range of vulnerabilities that convinced the lab to adopt its new approach.

To meet that requirement while still reaching its training goals, the lab said it created a “a vast set of indexed and cached web content with which our models can interact, without risk of affecting external systems.”

Whether that strategy will perform as well as letting models run freely on the open internet remains to be seen, but it is noteworthy that both frontier labs have determined their most powerful technology can’t be left unsupervised on the digital commons.
