---
title: "New ways to balance cost and reliability in the Gemini API"
source: TLDR AI · 2026-04-03
url: https://blog.google/innovation-and-ai/technology/developers-tools/introducing-flex-and-priority-inference/?utm_source=tldrai
date: 2026-04-04
published_at: 2026-04-03T12:00:00+00:00
tag: 产品发布
item_id: bb64ec81bfd1593a
---
# New ways to balance cost and reliability in the Gemini API

Today, we are adding two new service tiers to the Gemini API: [Flex and Priority](https://ai.google.dev/gemini-api/docs/optimization#inference-tiers). These new options give you granular control over cost and reliability through a single, unified interface.

As AI evolves from simple chat into complex, autonomous agents, developers typically have to manage two distinct types of logic:

**Background tasks**: High-volume workflows like data enrichment or "thinking" processes that don't need instant responses.**Interactive tasks**: User-facing features like chatbots and copilots where high reliability is needed.

Until now, supporting both meant splitting your architecture between standard synchronous serving and the asynchronous Batch API. Flex and Priority help to bridge this gap. You can now route background jobs to Flex and interactive jobs to Priority, both using standard synchronous endpoints. This eliminates the complexity of async job management while giving you the economic and performance benefits of specialized tiers.

[Flex Inference](https://ai.google.dev/gemini-api/docs/flex-inference): scale innovation for 50% less

Flex Inference is our new cost-optimized tier, designed for latency-tolerant workloads without the overhead of batch processing.

**50% price savings:**Pay half the price of the Standard API by downgrading criticality of your request (making them less reliable, and adding latency).**Synchronous simplicity:**Unlike the Batch API, Flex is a synchronous interface. You use the same familiar endpoints without managing input/output files or polling for job completion.**Ideal use cases:**Background CRM updates, large-scale research simulations, and agentic workflows where the model "browses" or "thinks" in the background.

Get started fast by simply configuring the `service_tier`

parameter in your request:

Flex tier will be available for all paid tiers and is available for GenerateContent and Interactions API requests.

[Priority Inference](https://ai.google.dev/gemini-api/docs/priority-inference): Highest reliability for critical apps

The new Priority Inference tier offers our highest level of assurance at a premium price point. This helps to ensure your most important traffic is not preempted, even during peak platform usage.

**Highest criticality:**Priority requests get highest criticality leading to higher reliability, even during peak load.**Graceful downgrade:**If your traffic exceeds your Priority limits, overflow requests are automatically served at the Standard tier instead of failing. This keeps your application online and helps to ensure business continuity.**Transparent response:**The API response indicates which tier served your request, giving you full visibility into your performance and billing.**Ideal use cases:**Real-time customer support bots, live content moderation pipelines, and time-sensitive requests.

To use Priority Inference, simply set the `service_tier`

parameter accordingly:

Priority inference will be available to users with Tier 2 / 3 paid projects across the `GenerateContent` API and [Interactions API](https://ai.google.dev/gemini-api/docs/interactions) endpoints.

Visit the [Gemini API documentation](https://ai.google.dev/gemini-api/docs/pricing) to see the full pricing breakdown and start optimizing your production tiers today. To see it in action, check out the [cookbook](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Inference_tiers.ipynb) for runnable code examples.
