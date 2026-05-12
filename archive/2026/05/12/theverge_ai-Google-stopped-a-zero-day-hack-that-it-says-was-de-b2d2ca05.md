---
title: "Google stopped a zero-day hack that it says was developed with AI"
source: The Verge AI
url: https://www.theverge.com/tech/928007/google-ai-zero-day-exploit-stopped
date: 2026-05-12
published_at: 2026-05-11T12:09:42-04:00
tag: 行业动态
item_id: b2d2ca05d0bdf377
---
For the first time, Google says it has spotted and stopped a zero-day exploit developed with AI. According to a report from [Google Threat Intelligence Group](https://www.anrdoezrs.net/links/8836598/type/dlg/https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access) (GTIG), “prominent cyber crime threat actors” were planning to use the vulnerability for a “mass exploitation event” that would have allowed them to bypass two-factor authentication on an unnamed “open-source, web-based system administration tool.”

# Google stopped a zero-day hack that it says was developed with AI

Google researchers found evidence in the exploit’s code that it may have been created using AI, like a ‘hallucinated’ CVSS score.

Google researchers found evidence in the exploit’s code that it may have been created using AI, like a ‘hallucinated’ CVSS score.

![Photo illustration of a brain on a circuit board in red.](https://platform.theverge.com/wp-content/uploads/sites/2/chorus/uploads/chorus_asset/file/25330660/STK414_AI_CHATBOT_H.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400)

![Photo illustration of a brain on a circuit board in red.](https://platform.theverge.com/wp-content/uploads/sites/2/chorus/uploads/chorus_asset/file/25330660/STK414_AI_CHATBOT_H.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400)

Google’s researchers found hints in the Python script used for the exploit that indicated help from AI, like a “hallucinated CVSS score” and “structured, textbook” formatting consistent with LLM training data. The exploit takes advantage of “a high-level semantic logic flaw where the developer hardcoded a trust assumption” in the platform’s 2FA system. This follows weeks of hand-wringing over the capabilities of cybersecurity-focused AI models [like Anthropic’s Mythos](https://www.theverge.com/ai-artificial-intelligence/916500/mythos-v-firefox) and a [recently disclosed Linux vulnerability](https://www.theverge.com/tech/922243/linux-cve-2026-3141-copy-fail-exploit) that was discovered with AI assistance.

It’s the first time Google has found evidence that AI was involved in an attack like this, although Google’s researchers note that they “do not believe Gemini was used.” Google says it was able to “disrupt” this particular exploit, but also says hackers are increasingly using AI to find and take advantage of security vulnerabilities. The report also mentions AI as a target for attackers, saying “GTIG has observed adversaries increasingly target the integrated components that grant AI systems their utility, such as autonomous skills and third-party data connectors.”

Google’s report also details how hackers are using “persona-driven jailbreaking” to get AI to find security vulnerabilities for them, like an example prompt that instructs the AI to pretend it’s a security expert. Hackers are also feeding AI models whole repositories of vulnerability data and using OpenClaw in ways that suggest “an interest in refining AI-generated payloads within controlled settings to increase exploit reliability prior to deployment.”

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.
