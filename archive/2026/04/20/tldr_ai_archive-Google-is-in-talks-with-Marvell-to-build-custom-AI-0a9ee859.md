---
title: "Google is in talks with Marvell to build custom AI inference chips as it diversifies beyond Broadcom"
source: TLDR AI · 2026-04-20
url: https://thenextweb.com/news/google-marvell-ai-chips-inference-tpu-broadcom?utm_source=tldrai
date: 2026-04-20
published_at: 2026-04-20T12:00:00+00:00
tag: 行业动态
item_id: 0a9ee859030c549f
---
![Google is in talks with Marvell to build custom AI inference chips as it diversifies beyond Broadcom](https://cdn0.tnwcdn.com/wp-content/blogs.dir/1/files/2026/04/google-marvell-ai-chips-inference-tpu-broadcom.png)

*Summary: Google is in talks with Marvell Technology to develop two new AI chips – a memory processing unit and an inference-optimised TPU – adding a third design partner alongside Broadcom and MediaTek in its custom silicon supply chain. The discussions, which have not yet produced a signed contract, came days after Broadcom locked in a through-2031 TPU agreement and reflect Google’s shift toward inference as the dominant compute cost, as the custom ASIC market is projected to grow 45% in 2026 and reach $118 billion by 2033.*

Google is in talks with Marvell Technology to develop two new chips for running AI models, according to [The Information](https://www.theinformation.com/articles/google-talks-marvell-build-new-ai-chips-inference). One is a memory processing unit designed to work alongside Google’s existing Tensor Processing Units. The other is a new TPU built specifically for inference, the phase of AI where models serve users rather than learn from data. Marvell would act in a design-services role, similar to MediaTek’s involvement on Google’s latest Ironwood TPU. The discussions have not yet produced a signed contract.

The talks came days after Broadcom, Google’s primary custom chip partner, announced a long-term agreement to design and supply TPUs and networking components through 2031. The timing suggests Google is not replacing Broadcom but adding a third design partner to a supply chain that already includes Broadcom for high-performance chip variants, MediaTek for cost-optimised “*e*” variants at 20 to 30% lower cost, and TSMC for fabrication. The strategy is diversification, not substitution.

## Why inference matters now

Google’s seventh-generation TPU, Ironwood, debuted this month as what the company calls “*the first Google TPU for the age of inference.*” It delivers ten times the peak performance of the TPU v5p and scales to 9,216 liquid-cooled chips in a superpod spanning roughly 10 megawatts, producing 42.5 FP8 exaflops. Google plans to build millions of Ironwood units this year. The Marvell-designed chips would supplement rather than replace Ironwood, potentially targeting different workload profiles or cost points for the growing share of Google’s compute that goes to serving AI models rather than training them.

The shift from training to inference as the primary demand driver is reshaping the chip market. Training a frontier model is a one-time event that requires enormous compute for weeks or months. Inference runs continuously, serving every query from every user, and its costs scale with demand rather than capability. As AI products reach hundreds of millions of users, inference becomes the dominant expense, and purpose-built inference silicon becomes a competitive advantage that general-purpose GPUs cannot match on cost or efficiency.

## The backstory

The Google-Marvell relationship has a longer history than this week’s report suggests. The Information reported in 2023 that Google had been working since 2022 on a chip codenamed “*Granite Redux*” that would use Marvell instead of Broadcom, with Google expecting to save billions of dollars annually. At the time, Google’s spokesperson called Broadcom “an excellent partner” and said the company was “*productively engaged with Broadcom and multiple other suppliers for the long term.*”

What changed between 2023 and now is that Google appears to have abandoned the idea of dropping Broadcom entirely. The through-2031 agreement locked in that relationship. Instead, Google is building a multi-supplier architecture in which Broadcom, MediaTek, and potentially Marvell each handle different parts of the TPU programme, competing on specific segments rather than for the entire contract. The approach mirrors how automotive companies manage component suppliers: no single vendor gets enough leverage to dictate terms.

## What Marvell brings

Marvell’s data centre revenue reached a record $6.1 billion in its fiscal year ending February 2026, with total revenue of $8.2 billion, up 42% year over year. The company runs a custom silicon business with a $1.5 billion annual run rate across 18 cloud-provider design wins, building chips for Amazon (Trainium processors), Microsoft (Maia AI accelerator), and Meta (a new data processing unit), in addition to its existing work with Google on the Axion ARM CPU.

[Nvidia invested $2 billion in Marvell](https://thenextweb.com/news/nvidia-marvell-nvlink-fusion-ecosystem-lock-in) at the end of March, partnering through NVLink Fusion to integrate Marvell’s custom chips and networking with Nvidia’s interconnect fabric. The deal positions Marvell at the intersection of both the GPU and ASIC ecosystems. In December 2025, Marvell acquired Celestial AI for up to $5.5 billion, gaining photonic interconnect technology that CEO Matt Murphy said would deliver “*the industry’s most complete connectivity platform for AI and cloud customers.*” Murphy is targeting 20% market share in custom AI chips and expects roughly 30% year-over-year revenue growth in fiscal 2027.

Marvell’s stock has rallied approximately 50% year to date, with a 30% gain in April alone following the Nvidia partnership and the Google talks. Barclays analyst Tom O’Malley upgraded the stock to overweight and raised his price target from $105 to $150.

## Broadcom’s position

The Marvell talks do not appear to have weakened Broadcom’s position. Broadcom commands more than 70% market share in custom AI accelerators. Its AI revenue hit $8.4 billion in its most recent quarter, up 106% year over year, with guidance of $10.7 billion for the following quarter. The company is targeting $100 billion in AI chip revenue by 2027. Broadcom’s shares rose more than 6% on the day it announced the Google extension, and Mizuho analysts estimated the company would record $21 billion in AI revenue attributable to its Google and [Anthropic relationships](https://thenextweb.com/news/anthropic-custom-ai-chips-30-billion-revenue) in 2026, rising to $42 billion in 2027. Anthropic will access approximately 3.5 gigawatts of next-generation TPU-based compute starting in 2027.

The broader ASIC market is growing faster than the GPU market. TrendForce projects custom chip sales will increase 45% in 2026, compared with 16% growth in GPU shipments. Counterpoint Research projects Broadcom will hold roughly 60% of the custom AI accelerator market by 2027, with Marvell at approximately 25%. The market itself is expected to reach $118 billion by 2033.

## What this means for Google

Google’s chip strategy now involves four partners (Broadcom, MediaTek, Marvell, and TSMC), its own in-house design team, and a product line that spans training, inference, and general-purpose cloud compute. The complexity is deliberate. Every hyperscaler that depends on a single chip supplier, whether Nvidia or anyone else, faces pricing risk, supply risk, and the strategic vulnerability of building a business on someone else’s silicon.

The inference focus of the Marvell discussions reflects a shift in where the money goes. Training [Nvidia’s latest chips](https://thenextweb.com/news/nvidia-gtc-2026-opens-today) remain dominant in training workloads, but inference is where the volume is, and volume is where custom silicon’s cost advantages compound. Google serves billions of AI-augmented search queries, Gemini conversations, and Cloud AI API calls every day. Shaving even a small percentage off the cost per inference across that scale translates into billions of dollars annually, which is precisely what the 2023 “Granite Redux” discussions were about.

The talks with Marvell are not yet a deal, and chip development timelines mean any resulting product is likely years from production. But the direction is clear. Google is building a [chip supply chain](https://thenextweb.com/news/google-outpace-microsoft-ai-investment-deepmind-ceo-ted) designed to support the most demanding AI inference workloads in the world, and it intends to have more than one partner capable of building the silicon that runs them. For Marvell, a Google inference TPU contract would validate its position as the second-most important custom AI chip designer in the world. For Google, it would mean one more supplier in a market where no company can afford to depend on just one.

## Get the TNW newsletter

Get the most important tech news in your inbox each week.
