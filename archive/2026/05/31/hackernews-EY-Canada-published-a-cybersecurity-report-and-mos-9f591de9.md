---
title: "EY Canada published a cybersecurity report and most citations were hallucinated"
source: Hacker News
url: https://gptzero.me/investigations/ey
date: 2026-05-31
published_at: 2026-05-30T19:02:54+00:00
tag: 行业动态
item_id: 9f591de9636f4f08
---
Earlier this year, an engineer at GPTZero coined the term “vibe citing” to describe the accidental creation of fake references via LLM hallucinations. It turns out that the friction of creating and checking citations is leading many researchers, consultants, lawyers, and public officials to embrace the vibe (if you know what we mean).

Among the converts are the authors of a 2025 Ernst & Young report titled Points of Attack: Uncovering Cyber Threats and Fraud in Loyalty Systems. This report, stuffed with fake citations and inaccurate claims, is surfacing in newspapers, blog posts, and AI search overviews, poisoning the data that both human researchers and AI agents rely on.

GPTZero began targeting vibe citations with our Hallucination Check tool in 2025, which we used to further investigations into a government publication, two different [Deloitte reports](https://gptzero.me/news/deloitte-australia-citation-check/), and prestigious machine learning / artificial intelligence conferences like [NeurIPS](https://fortune.com/2026/01/21/neurips-ai-conferences-research-papers-hallucinations/) and [ICLR](https://betakit.com/start-up-investigation-reveals-50-peer-reviewed-papers-contained-hallucinated-citations/). Over the past few months we've set up an automated pipeline to search for vibe citations by finding and scanning public reports from major consulting firms. What we've found suggests that the vibe citing epidemic is already endemic, even among the major players.

Instead of releasing our results all at once, we're going to focus on one report at a time. This approach both prevents individual examples being overlooked and allows us to illustrate the negative impacts of vibe citing on research quality and public trust.

![EY Tower, Toronto — as seen from GPTZero's office](/investigations/ey/pages/EY.jpg)

EY Tower, Toronto — as seen from GPTZero’s office

## On the menu: Ernst & Young (EY)

Ernst & Young is one of the “big four” global consulting firms, providing accounting and consulting services to governments and private entities from 150 offices around the world. The Canadian member firm (EY Canada) [provides millions of dollars of services](https://search.open.canada.ca/contracts/?sort=contract_date+desc&page=1&search_text=%22ERNST+%26+YOUNG%22&year=2024%7C2025) to the Canadian government annually.

In late 2025, EY Canada published a 44-page report on cyber security titled *Points of Attack: Uncovering Cyber Threats and Fraud in Loyalty Systems*. While credited to three employees (two partners and one senior manager), the document is a collage of vibe citations, misattributions, fake statistics, and AI-written text.

![Cover — EY 'Points of Attack' report](/_next/image?url=%2Finvestigations%2Fey%2Fpages%2Fcover.webp&w=3840&q=75)

## Why the Vibes Are Bad

EY Canada’s report doesn’t use footnotes or normal academic citations. Instead, it references sources directly in the text and/or includes them in a resources table (p. 41-43). This table provides a source title, description, and URL for all sources, as well as the publisher and date in certain cases. Almost all of the URLs are broken or fake, and more than half of the titles don’t correspond to real sources.

GPTZero uses a very specific definition of because of the potential reputational cost (to both us and the report’s authors) of false positives. One of our team members manually verified Hallucination Check’s results to ensure their accuracy.

| Airline Loyalty Breach: BleepingComputer | Report on credential stuffing attacks that compromised millions of airline loyalty accounts. |
|

| AI Voice Deepfakes Targeting Call Centers | Explains how attackers use AI-generated voices to exploit customer service workflows. |
|

| Gartner Market Trends – Loyalty Fraud | Strategic guidance on fraud evolution in digital loyalty programs and mobile wallets. |
|

| Forbes – The $200 Billion Loyalty Economy | Business case for loyalty programs as financially significant digital assets. |
|

| McKinsey & Company – Loyalty Economics Report (2022) | Estimates $200 billion in unredeemed rewards globally. |
|

| Cisco Talos: API Attacks on Retail | Insights into insecure API exploitation in commerce and loyalty systems. |
|

| TechCrunch: Loyalty Program Breaches | News coverage on incidents involving compromised reward accounts and user data. |
|

| Wired: API Security Gaps | Exploration of overlooked API vulnerabilities in consumer-facing digital services. |
|

During our previous analysis of academic conference submissions, we found that many authors primarily used AI to generate and format their references, resulting in papers with vibed citations but low AI text scores overall.

However, it’s hard to find human fingerprints in Points of Attack — harder, even, than finding a [human-written LinkedIn post](https://gptzero.me/ai-vision). Not only does the text scan as AI-generated, it’s riddled with common LLM errors like fake statistics, misattributions, and internal contradictions.

![PDF page 4](/_next/image?url=%2Finvestigations%2Fey%2Fpages%2Fpage-4.webp&w=3840&q=75)

![PDF page 42](/_next/image?url=%2Finvestigations%2Fey%2Fpages%2Fpage-42.webp&w=3840&q=75)

![PDF page 10](/_next/image?url=%2Finvestigations%2Fey%2Fpages%2Fpage-10.webp&w=3840&q=75)

![PDF page 43](/_next/image?url=%2Finvestigations%2Fey%2Fpages%2Fpage-43.webp&w=3840&q=75)

![PDF page 4](/_next/image?url=%2Finvestigations%2Fey%2Fpages%2Fpage-4.webp&w=3840&q=75)

![PDF page 42](/_next/image?url=%2Finvestigations%2Fey%2Fpages%2Fpage-42.webp&w=3840&q=75)

![PDF page 10](/_next/image?url=%2Finvestigations%2Fey%2Fpages%2Fpage-10.webp&w=3840&q=75)

![PDF page 43](/_next/image?url=%2Finvestigations%2Fey%2Fpages%2Fpage-43.webp&w=3840&q=75)

### A bold claim in the executive summary

In the report’s Executive Summary, its authors claim the global loyalty points market is $200 billion, and that 30–50% of those points go unused.

### A fake Forbes citation

The citation we just looked at supports the author's original claim of a $200 billion global market.

### A contradictory claim

Yet on page 10, the $200 billion figure is now the estimate of unredeemed loyalty points, not the collective value of all points globally. Since the authors have already claimed that up to 50% of points are unredeemed, this new statistic requires a global market value of at least $400 billion.

### A second fabricated citation: McKinsey

A few rows down, a fabricated McKinsey & Company report provides evidence for the latter claim — $200 billion as the value of unredeemed points globally. Two invented citations, two incompatible numbers.

[blogpost](https://financialit.net/blog/rewardsinnovation-loyaltyeconomy/points-value-why-were-unlocking-true-value-rewards)by Financial IT, which was published six months earlier.

![PDF page 1](/_next/image?url=%2Finvestigations%2Fey%2Fpages%2Ffinancial-it-page-1.webp&w=3840&q=75)

![PDF page 3](/_next/image?url=%2Finvestigations%2Fey%2Fpages%2Ffinancial-it-page-3.webp&w=3840&q=75)

![PDF page 1](/_next/image?url=%2Finvestigations%2Fey%2Fpages%2Ffinancial-it-page-1.webp&w=3840&q=75)

![PDF page 3](/_next/image?url=%2Finvestigations%2Fey%2Fpages%2Ffinancial-it-page-3.webp&w=3840&q=75)

### A similar claim

Six months before EY’s report, a [blog post](https://financialit.net/blog/rewardsinnovation-loyaltyeconomy/points-value-why-were-unlocking-true-value-rewards) on the obscure U.K. fintech magazine Financial IT claims that "more than $200 billion in points sit idle each year." The language is nearly identical to the EY report.

### The vibes are identical

The blog’s sources section cites "McKinsey & Company: Loyalty Economics Report (2022)" — a report that does not exist. This fabricated citation appears verbatim in the EY report’s reference table, laundering an invented source from a low-quality blog into a Big Four publication.

![PDF page 6](/_next/image?url=%2Finvestigations%2Fey%2Fpages%2Fpage-6.webp&w=3840&q=75)

![PDF page 11](/_next/image?url=%2Finvestigations%2Fey%2Fpages%2Fpage-11.webp&w=3840&q=75)

![PDF page 6](/_next/image?url=%2Finvestigations%2Fey%2Fpages%2Fpage-6.webp&w=3840&q=75)

![PDF page 11](/_next/image?url=%2Finvestigations%2Fey%2Fpages%2Fpage-11.webp&w=3840&q=75)

### The source is attributed to Paystone

On page 6, the authors claim that 72% of customer loyalty programs have reported theft or fraud. This fact is attributed to a [2019 post](https://www.paystone.com/resources/3-types-of-loyalty-fraud-and-how-to-prevent-them) by the Canadian payment processor Paystone.

### Actually, the source is Forter

However, on page 11, the same statistic is attributed to a different source — the unusually-named “[NRF 2020 summary](https://www.forter.com/blog/nrf20/)” published by the digital fraud prevention company Forter. Neither of these sources are included in the report’s reference table. In fact, while the statistic is referenced on both the Paystone and Forter pages, the original source seems to be a 2017 survey by Ipsos.

![PDF page 6](/_next/image?url=%2Finvestigations%2Fey%2Fpages%2Fpage-6.webp&w=3840&q=75)

![PDF page 11](/_next/image?url=%2Finvestigations%2Fey%2Fpages%2Fpage-11.webp&w=3840&q=75)

![PDF page 6](/_next/image?url=%2Finvestigations%2Fey%2Fpages%2Fpage-6.webp&w=3840&q=75)

![PDF page 11](/_next/image?url=%2Finvestigations%2Fey%2Fpages%2Fpage-11.webp&w=3840&q=75)

### The 89% claim

On page 6, the authors claim that loyalty program fraud attacks have increased 89% since 2019.

### A specific source for this claim

Yet on page 11, this 89% increase is limited to a single year, 2018 to 2019, and the statistic is attributed to a specific source: the Forter [Fraud Attack Index](https://cdn2.hubspot.net/hubfs/2776164/Fraud%20Attack%20Index%20Seventh%20Edition%202019/Forter-Fraud-Attack-Index-Seventh-Edition.pdf). Surprisingly, this source both exists and partially confirms the second version of the claim. However, like many of the sources used in the EY report, it is substantially out of date. Poorly paraphrased statistics are also a sign of AI slop.

## Why Vibes Matter

It’s difficult to measure the public impact of EY’s report. Points of Attack seems to have made few waves in Canada; however, it was recently referenced in a [Canberra Times article](https://www.canberratimes.com.au/story/9168790/new-phishing-scam-targets-qantas-loyalty-points/) that was syndicated to more than 60 newspapers across Australia. It may also have circulated through client briefings, internal decks, and other proprietary media that aren’t in the public domain. Yet vibe citations don’t just deceive readers or corporate audiences — they also have another, more insidious, impact.

Publishing a report online is essentially a form of data injection into the pool of knowledge that is the internet. When the report includes fake information (either vibed citations or false claims) it can “poison the well” by misleading future researchers, especially if the report is published by a well-known consulting firm and hosted on a high-traffic website.

This risk has been aggravated by the emergence of AI “deep research” tools which rely on different signals than humans when choosing sources and are therefore more vulnerable to data poisoning.

Fake information poisons the well and misleads future researchers, especially when published by a well-known consulting firm. Claude, ChatGPT, and Perplexity all surface hallucinations from EY's flawed report.


“What is the average time to detect loyalty fraud?”


![ChatGPT response citing EY report](/investigations/ey/ai-responses/chatgpt.png)

![Claude response citing EY report](/investigations/ey/ai-responses/claude.png)

![Perplexity response citing EY report](/investigations/ey/ai-responses/perplexity.png)

## GPTZero is Chasing the Vibe (Citations)

Our research over the past few months proves that vibe citing is a clear and present danger to researchers, academics, consultants, and (frankly) anyone who drinks from the digital pool by searching the web. Our Hallucination Check tool is our answer to this threat: a way to identify vibe citations and hallucinations without manually checking every citation. It is already being used to screen submissions by elite academic conferences like IJCAI, ICLR, and ICSE.

Now, more than ever, it's crazy to accept citations on faith — even those from a reputable source like Ernst & Young.

Try GPTZero’s [Hallucination Check](https://gptzero.me/hallucination-detector) for yourself, or [reach out to GPTZero’s team](https://gptzero.me/sales).
