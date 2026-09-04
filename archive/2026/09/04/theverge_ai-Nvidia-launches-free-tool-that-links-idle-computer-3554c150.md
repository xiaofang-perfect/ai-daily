---
title: "Nvidia launches free tool that links idle computers into a personal AI data center"
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/989435/nvidia-pair-personal-ai-router-home-local-llm-compute-tool-rtx-macbook
date: 2026-09-04
published_at: 2026-09-03T12:00:00-04:00
tag: 工具开源
item_id: 3554c15062bdc43f
---
Nvidia is announcing its new [Personal AI Router](https://www.nvidia.com/en-us/ai-on-rtx/personal-ai-router/) (PAIR), a free tool that syncs up your home computers for tackling local AI inference tasks with tools like Ollama and LM Studio.

# Nvidia launches free tool that links idle computers into a personal AI data center

PAIR is designed to get your desktop and laptop working together on local AI tasks when not in use.

![Screenshot 2026-09-03 at 10.42.02 AM](https://platform.theverge.com/wp-content/uploads/sites/2/2026/09/Screenshot-2026-09-03-at-10.42.02-AM.png?quality=90&strip=all&crop=7.9200247985121%2C0%2C84.159950402976%2C100&w=2400)

![Screenshot 2026-09-03 at 10.42.02 AM](https://platform.theverge.com/wp-content/uploads/sites/2/2026/09/Screenshot-2026-09-03-at-10.42.02-AM.png?quality=90&strip=all&crop=7.9200247985121%2C0%2C84.159950402976%2C100&w=2400)

![Antonio G. Di Benedetto](https://platform.theverge.com/wp-content/uploads/sites/2/chorus/author_profile_images/195792/ANTONIO_DI_BENEDETTO.0.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=96)

Let’s get the obvious thing out of the way, despite what its name might imply: PAIR is not a hardware router. It’s [open-source software](https://github.com/NVIDIA/Personal-AI-Router) developed by Nvidia that discovers compatible PCs on a network, connects them, and prepares them for crunching numbers on agentic workflows. While the compatible devices are mostly Nvidia GeForce GPUs (PAIR works with RTX 20-series cards and newer, as well as RTX Pro GPUs and DGX Spark systems), Apple’s M4 chips or newer will also work.

The key thing here is that PAIR uses your in-home systems when they’re idle to avoid interfering with other tasks. And this disaggregated system of computers can work in parallel to chew through lots of processing requests — which should be helpful for an agentic workflow that breaks complex tasks into smaller jobs. This should prevent large bottlenecks on a single GPU, and Nvidia says PAIR can adapt as devices join or leave the network — including if a user does something like start playing a game on their desktop PC.

![<em>Nvidia PAIR’s graphical interface in action.</em>](https://platform.theverge.com/wp-content/uploads/sites/2/2026/09/Screenshot-2026-09-03-at-10.42.44-AM.png?quality=90&strip=all&w=2400)

![<em>Nvidia’s example of a prompt in Hermes being processed with PAIR.</em>](https://platform.theverge.com/wp-content/uploads/sites/2/2026/09/Screenshot-2026-09-03-at-10.43.56-AM.png?quality=90&strip=all&w=2400)

**1/2**

*Nvidia PAIR’s graphical interface in action.*

In a media briefing, Nvidia product manager Seth Schneider painted a picture of a household filled with powerful computers that could be doing much more with PAIR: a dad with both an Nvidia RTX Spark laptop and a DGX Spark desktop, a mom with an RTX 5090 laptop, a daughter with a gaming desktop, and a son with a MacBook Pro. In this incredibly *extreme* case, Schneider estimates this house has about 165 teraflops of underutilized compute. “It’s truly a treasure trove of free tokens just sitting in homes today,” he says, even when accounting for the electricity costs in the average American home.

Nvidia says PAIR is secured by pairing all devices through a six-digit code and then securing the channel via [mTLS](https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/#:~:text=Learn%20more-,How%20does%20mTLS%20work%3F,-Normally%20in%20TLS) (Mutual Transport Layer Security), to create an encrypted communication line that’s trusted in both directions between computers. The Nvidia PAIR beta is available today, with support for Windows, Linux, and macOS.

![The structure of Nvidia PAIR.](https://platform.theverge.com/wp-content/uploads/sites/2/2026/09/Screenshot-2026-09-03-at-10.43.22-AM.png?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400)

*The structure of Nvidia PAIR.*

PAIR does seem like a clever solution if you already have some beefy computers in your home and you want to run your own local AI. Upon my asking who PAIR is really for, and what kind of setups are *actually* realistic, Schneider said Nvidia envisions most PAIR users will have something like one MacBook or Windows laptop and one gaming PC.

In addition to PAIR, Nvidia is also announcing that three major AI agent apps — Perplexity Portable Computer, Hermes Agent, and OpenClaw — will offer simplified local setup with Nvidia GPUs on Windows. The new setup experiences are designed to allow users to get local agents up and running in just a few clicks, reducing the initial manual configuration necessary.

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.
