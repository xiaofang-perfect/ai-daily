---
title: "The biggest names in AI are backing a new way to opt out of scraping"
source: The Verge AI
url: https://www.theverge.com/tech/1023763/openai-google-microsoft-ai-scraping-standard-opt-out
date: 2026-10-31
published_at: 2026-10-30T16:26:10-04:00
tag: 行业动态
item_id: a031c786265b63cb
---
OpenAI, Google, Microsoft, and Anthropic say they will adopt a new standard that publishers can use to opt out of being scraped by AI, as [reported earlier by *Search Engine Roundtable*](https://www.seroundtable.com/google-ai-training-control-42430.html). With this control, publishers can apply their AI training preferences across multiple AI companies, instead of setting them individually.

# The biggest names in AI are backing a new way to opt out of scraping

The new control will allow publishers to apply their AI training preferences across multiple crawlers.

![Photo illustration of a brain on a circuit board in red.](https://platform.theverge.com/wp-content/uploads/sites/2/chorus/uploads/chorus_asset/file/25330660/STK414_AI_CHATBOT_H.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400)

![Photo illustration of a brain on a circuit board in red.](https://platform.theverge.com/wp-content/uploads/sites/2/chorus/uploads/chorus_asset/file/25330660/STK414_AI_CHATBOT_H.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400)

![Emma Roth](https://platform.theverge.com/wp-content/uploads/sites/2/chorus/author_profile_images/195810/EMMA_ROTH.0.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=96)

The [shared “policy token” signal](https://datatracker.ietf.org/doc/draft-kelley-aipref-training-preference-signal/) is proposed by Kevin Kelley, a technical lead for standards at Anthropic, as part of the Internet Engineering Task Force (IETF). It will live within a website’s [robots.txt file](https://www.theverge.com/24067997/robots-txt-ai-text-file-web-crawlers-spiders), which has long signaled which web crawlers can and can’t scrape a site — whether for search indexing, archiving, or AI training. Currently, sites have to signal their AI training preferences separately to each AI company.

The announcement comes as publishers grapple with the continuing influx of AI crawlers scraping their sites and feeding their content into AI models. Some companies and organizations have attempted to combat unauthorized scraping, with the [Really Simple Licensing (RSL) standard](https://www.theverge.com/news/841222/rsl-licensing-ai-spec-launch) giving publishers the ability to charge crawlers that visit their sites, and [Cloudflare blocking AI crawlers by default](https://www.theverge.com/news/695501/cloudflare-block-ai-crawlers-default).

[OpenAI](https://openai.com/index/helping-websites-express-ai-training-preferences/), [Google](https://developers.google.com/search/blog/2026/10/ai-training-control), [Microsoft](https://blogs.bing.com/search/2026/10/your-content-your-choice-clearer-preferences-for-training-and-grounding/), and [Anthropic](https://mailarchive.ietf.org/arch/msg/ai-control/mddjatOxSR0h6GmLRBWlc839c7w/]) say they will restrict their AI crawlers from accessing a site if they encounter the shared token. Meta communications head Andy Stone [also signaled support](https://x.com/andymstone/status/2116257949773607300?a=Q9vDWTsvBBcq3_OBloc&s=20) for the new setting, but doesn’t say whether the company will honor it. “We believe creating a common signal that conveys such preferences to multiple providers at once is an important step,” Stone says. “And we look forward to working with other AI companies on the standards and their implementation across the industry.”

Microsoft says it [will offer granular controls](https://blogs.bing.com/search/2026/10/your-content-your-choice-clearer-preferences-for-training-and-grounding/) that will give publishers the ability to opt out of AI training or [AI grounding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/overview), the process of pointing an AI model to a verified source of information to reduce hallucinations. Microsoft notes that websites will still appear in Bing’s search results regardless of their preferences. Google previously implemented similar controls that allow sites to control whether their [content appears in AI search features](https://support.google.com/webmasters/answer/16908024?hl=en&sjid=6465996090185817348-NA) or is used for AI training, without impacting visibility in search.

While Anthropic has already adopted the signal, Google and Microsoft plan to support it next year. OpenAI says it will implement it in the “coming months.”

**Update, October 30th:** Added a comment from Meta.

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.
