---
title: "Google will now let any AI agent run your smart home"
source: The Verge AI
url: https://www.theverge.com/tech/996310/google-home-mcp-integration-agentic-ai-smart-home-price-release-date
date: 2026-09-17
published_at: 2026-09-16T13:00:00-04:00
tag: 产品发布
item_id: 8b42908bbdca116a
---
Google is opening up its smart home to AI agents, letting tools like Claude and Open Claw access and control your connected devices and analyze your home’s data using the [standardized Model Context Protocol](https://www.theverge.com/ai-artificial-intelligence/841156/ai-companies-aaif-anthropic-mcp-model-context-protocol).

# Google will now let any AI agent run your smart home

Google Home adds MCP integration, allowing third-party AI agents to analyze your home data, control devices, and build custom dashboards.

![Gemini for Home](https://platform.theverge.com/wp-content/uploads/sites/2/2026/07/gemini-for-home.jpg?quality=90&strip=all&crop=7.8563995837669%2C0%2C84.287200832466%2C100&w=2400)

![Gemini for Home](https://platform.theverge.com/wp-content/uploads/sites/2/2026/07/gemini-for-home.jpg?quality=90&strip=all&crop=7.8563995837669%2C0%2C84.287200832466%2C100&w=2400)

*Google is inviting third-party agents, including Claude and Open Claw, into Google Home.*

![Jennifer Pattison Tuohy](https://platform.theverge.com/wp-content/uploads/sites/2/2025/01/Jenn_BLURPLE.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=96)

*Wirecutter*,

*Wired*,

*Dwell*,

*BBC*, and

*US News*.

[Google Home MCP](https://developers.home.google.com/mcp/home) is a new integration that lets third-party AI agents control and monitor your smart home and act on your behalf. It “allows any AI agents that support MCP, including Google Antigravity, Claude, Hermes or Open Claw, to securely work with all of the devices and event history in your Google Home ecosystem,” Taylor Lehman, group product manager at Google Home & Nest, said in a blog post.

According to Lehman, Home MCP integration will connect your AI agent of choice to real-world events, enabling a host of new capabilities. From things like cross-camera analysis — so you could ask your agent what your kid did when they got home from school — to using device state history to figure out how many loads of laundry you did last week or how long the lights were left on. It will also allow your agent to interact with you via voice, for example, by sending an audio message over your Google Home speaker when it has finished a task. You can also have your agent create a custom dashboard to control your Google Home.

![Google Home smart speakers will still be controlled by Gemini for Home, but with MCP enabled third-party AI agents will be able to send voice messages to you through them.](https://platform.theverge.com/wp-content/uploads/sites/2/2026/06/268614_Google_Home_Speaker_JTuohy_0015.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400)

*Google Home smart speakers will still be controlled by Gemini for Home, but with MCP enabled third-party AI agents will be able to send voice messages to you through them.*

This doesn’t replace Google’s [new Gemini for Home assistant](https://www.theverge.com/tech/788102/gemini-for-home-new-google-assistant-launch-date-price-features), which remains Google’s interface for interacting with Google Home through the Home app and Google Nest smart speakers, following the [demise of Google Assistant](https://www.theverge.com/tech/975516/google-assistant-android-phones-tablets-shutdown). Instead, MCP integration adds another layer of control, allowing third-party AI agents to interact directly with devices connected to Google Home through their own interfaces.

If this week wasn’t dominated by headlines about how AI will kill us all, I’d be really excited about this

At launch, availability is limited to [Google Home Premium Advanced users](https://www.anrdoezrs.net/links/8836598/type/dlg/https://store.google.com/product/google_home_premium) in the US ($20/month or $200/year), with access rolling out in the coming weeks. Setup requires [creating a Google Cloud project](https://developers.home.google.com/mcp/home) and configuring it to use the Home MCP.

Giving an AI agent access to real-world devices like smart locks, thermostats, and core infrastructure like HVAC systems and appliances raises obvious questions about security, privacy, and safety. Google says Home MCP enforces rate limits and safety protections; for example, it won’t allow an agent to unlock doors. However, depending on your agent, “connecting it to Home MCP can result in unexpected or even undesired behavior,” said Lehman, who recommends reviewing Google’s [developer policies](https://developers.home.google.com/policies) and [terms of service](https://developers.home.google.com/terms?hl=en).

[Home Assistant](https://www.theverge.com/24135207/home-assistant-announces-open-home-foundation), an open-source smart home platform, has implemented a similar MCP integration that shows what you can do when you give [an agent access to your smart home system](https://openclawai.io/blog/openclaw-home-automation-smart-home). I tested this last year to use [Claude to vibe-code my smart home](https://www.theverge.com/report/869318/claude-vibe-coding-home-assistant-smart-home), and it easily handled some of the more complex tasks that most interfaces — and users, for that matter — struggle with, including troubleshooting, creating automations, designing a dashboard, and setting up more advanced configurations, all using natural language.

The biggest change here isn’t that Google Home can now turn your lights on and off through your Claude app; it’s that Claude — or your agent of choice — has access to the underlying data and control layer of your home. It’s a step toward building [a whole home computer for your smart home](https://www.theverge.com/tech/993892/apples-next-computer-smart-home-hub-airport-router) that can understand what’s happening in it, reason across its history, and take action on your behalf. And if this last week wasn’t dominated by [headlines about how AI will kill us all](https://www.theverge.com/ai-artificial-intelligence/991927/anthropic-ai-kill-all-humans), I’d be really excited.

A system that can troubleshoot, suggest improvements, and identify patterns across your home is more useful than one that says “I’m sorry, I can’t do that”

Still, there are real advantages to giving an AI agent access to your smart home. It can reason across the data your home generates and act on it in ways traditional smart home systems generally can’t, moving the smart home from command and control toward something more contextual and proactive, closer to actual intelligence. A system that can troubleshoot a device, suggest improvements to automations, and track and identify patterns across your home is much more useful than one that just says “I’m sorry, I can’t do that.” With Home MCP integration, Google is bringing these capabilities into Google Home.

![Claude created this dashboard for me in Home Assistant using MCP. With Google Home MCP enabled, it should be able to do something similar for my Google Home.](https://platform.theverge.com/wp-content/uploads/sites/2/2026/09/Screenshot-2026-09-16-at-12.40.50-PM.png?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400)

*Claude created this dashboard for me in Home Assistant using MCP. With Google Home MCP enabled, it should be able to do something similar for my Google Home.*

While consumer-facing tools like Claude will be useful for smart home tinkerers, the bigger picture here is Google’s developer play. Over the last couple of years, Google has increasingly positioned itself as the smart home’s infrastructure layer. It launched [API access to its smart home](https://www.theverge.com/2024/5/15/24157154/google-home-api-matter-smart-home-chromecast-google-tv) in 2024 and more recently made Gemini for Home [a full-stack AI offering](https://developers.googleblog.com/empowering-service-providers-and-hardware-partners-with-gemini-for-home/). All of this points toward a more B2B2C strategy: Google can provide the AI and smart home infrastructure while [other companies build consumer-facing services and products](https://www.theverge.com/tech/935298/smart-home-cost-increase-ai-subscription-fatigue) on top.

With this week’s announcement, Google has also opened a path for developers to use its [agentic Antigravity coding tool](https://www.theverge.com/news/822833/google-antigravity-ide-coding-agent-gemini-3-pro) to build custom AI agents for the smart home that tap into Google Home device data and control layer. But even if developers use a different agent, as long as they’re using Google Home, it’s a win for Google. This way, Google becomes the smart home infrastructure layer, in much the same way AWS became infrastructure for internet and software businesses.

Whether smart home developers will buy into Google’s promises here is a big question. Based on the number of smart home platforms the company has launched and let die over the years — [Android @ Home](https://techcrunch.com/2012/06/24/what-happened-to-android-at-home/), [Weave](https://www.theverge.com/2016/1/5/10714466/google-brillo-weave-first-products-announced-ces-2016), [Project Brillo](https://www.theverge.com/2015/5/28/8677119/google-project-brillo-iot-google-io-2015), [Works with Nest](https://www.theverge.com/2019/5/16/18627719/google-works-with-nest-shutdown-clarification-statement-update), [Google Assistant](https://www.theverge.com/news/629904/google-assistant-gemini-moving-on) — developers will have to decide whether Google has finally settled on a smart home platform it intends to stick with.

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.
