---
title: "Poisoning 0.1% of pretraining data planted a remote-code backdoor in a coding agent"
source: TLDR AI · 2026-11-02
url: https://arxiv.org/abs/2610.37741?utm_source=tldrai
date: 2026-11-03
published_at: 2026-11-02T12:00:00+00:00
tag: 论文研究
item_id: 533686017919b9f4
---
# Computer Science > Cryptography and Security

\[Submitted on 27 Oct 2026\]

# Title:Agentic Backdoors via Pretraining Poisoning

[View PDF](https://arxiv.org/pdf/2610.37741)

[HTML (experimental)](https://arxiv.org/html/2610.37741v1)

Abstract:Large language models are pretrained on vast, uncurated corpora scraped from the public web. This creates a security risk from attackers who plant poisoned content in the pretraining data. We show for the first time that such poisoning can plant a remote code execution backdoor in an agent, causing it to execute attacker-chosen commands on the user's machine. To measure the threat end to end, we pretrain Qwen3 models from scratch at sizes 0.6B, 1.7B, and 4B, and then post-train each into a CLI agent using a clean pipeline. Poisoning only 0.1% of the pretraining corpus with our new poison design implants the backdoor: the deployed agent executes the malicious command when the trigger is present while behaving normally on clean inputs. The attack success rate (ASR) increases with model scale, with the 4B model reaching roughly 92% ASR at a 0.1% poison rate and staying positive even when the poisoning rate drops to 0.0005%. Our code is available at [this https URL](https://github.com/safety-research/agentic-backdoor).

[Full-text links:]

## Access Paper:

[view license](http://creativecommons.org/licenses/by/4.0/)

![license icon](https://arxiv.org/icons/licenses/by-4.0.png) 

### Additional Features

### Current browse context:

cs.CR

### References & Citations

Loading...

### Bookmark

![BibSonomy](https://arxiv.org/static/browse/0.3.4/images/icons/social/bibsonomy.png) 

![Reddit](https://arxiv.org/static/browse/0.3.4/images/icons/social/reddit.png) 

# Bibliographic and Citation Tools

Bibliographic Explorer *([What is the Explorer?](https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer))*

Connected Papers *([What is Connected Papers?](https://www.connectedpapers.com/about))*

Litmaps *([What is Litmaps?](https://www.litmaps.co/))*

scite Smart Citations *([What are Smart Citations?](https://www.scite.ai/))*

# Code, Data and Media Associated with this Article

alphaXiv *([What is alphaXiv?](https://alphaxiv.org/))*

CatalyzeX Code Finder for Papers *([What is CatalyzeX?](https://www.catalyzex.com))*

DagsHub *([What is DagsHub?](https://dagshub.com/))*

Gotit.pub *([What is GotitPub?](http://gotit.pub/faq))*

Hugging Face *([What is Huggingface?](https://huggingface.co/huggingface))*

ScienceCast *([What is ScienceCast?](https://sciencecast.org/welcome))*

# Demos

# Recommenders and Search Tools

Influence Flower *([What are Influence Flowers?](https://influencemap.cmlab.dev/))*

CORE Recommender *([What is CORE?](https://core.ac.uk/services/recommender))*

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? [**Learn more about arXivLabs**](https://info.arxiv.org/labs/index.html).
