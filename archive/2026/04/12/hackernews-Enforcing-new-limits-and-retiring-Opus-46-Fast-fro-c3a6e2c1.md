---
title: "Enforcing new limits and retiring Opus 4.6 Fast from Copilot Pro+"
source: Hacker News
url: https://github.blog/changelog/2026-04-10-enforcing-new-limits-and-retiring-opus-4-6-fast-from-copilot-pro/
date: 2026-04-12
published_at: 2026-04-11T03:07:23+00:00
tag: 产品发布
item_id: c3a6e2c13e8b2501
---
# Enforcing new limits and retiring Opus 4.6 Fast from Copilot Pro+

As GitHub Copilot continues to rapidly grow, we continue to observe an increase in patterns of high concurrency and intense usage. While we understand this can be driven by legitimate workflows, this type of usage places significant strain on our shared infrastructure and operating resources.

To ensure every user gets a fast, reliable Copilot experience, we’re updating limits to better balance capacity. These will roll out over the next few weeks. There will be two types of limits that users may see. Both are meant to balance capacity and protect the system for everyone.

- Limits for overall service reliability
- Limits for specific models or model family capacity

[What this means for you](https://github.blog#what-this-means-for-you)

- When you hit a service reliability limit, you will need to wait until your current session resets. This will be visible in the error experience when you are rate limited.
- When you hit a usage limit for specific models or model family, you can switch to an alternative model or use
[Auto mode](https://docs.github.com/copilot/concepts/auto-model-selection).

We recommend distributing requests more evenly over time when possible, rather than sending them in large, concentrated waves. You can also [upgrade your plan](https://github.com/features/copilot/plans) for higher limits.

We know limits can be frustrating and are actively exploring new ways to offer increased capacity for all users. We will share updates as we identify durable solutions. Learn more in [our docs about rate limiting](https://docs.github.com/copilot/concepts/rate-limits).

To further improve service reliability, we are streamlining our model offerings and focusing resources on the models our users use the most. As a first step, we’ll be retiring Opus 4.6 Fast for Copilot Pro+ users, beginning today. We recommend using Opus 4.6 as an alternative model with similar capabilities.
