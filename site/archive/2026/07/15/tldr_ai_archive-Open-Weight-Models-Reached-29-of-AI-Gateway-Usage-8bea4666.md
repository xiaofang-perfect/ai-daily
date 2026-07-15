---
title: "Open-Weight Models Reached 29% of AI Gateway Usage"
source: TLDR AI · 2026-07-14
url: https://vercel.com/blog/ai-gateway-production-index-july-2026?utm_source=tldrai
date: 2026-07-15
published_at: 2026-07-14T12:00:00+00:00
tag: 行业动态
item_id: 8bea46667c618920
---
*AI Gateway Production Index — July 2026 *

Every month, [AI Gateway](https://vercel.com/ai-gateway) routes tens of trillions of tokens between production applications and AI labs, giving us a view of what AI usage actually looks like in today’s enterprise. We publish that view here. See the Production Index reports published in [May](https://vercel.com/blog/ai-gateway-production-index) and [June](https://vercel.com/blog/ai-gateway-production-index-june-2026).

[Copy link to heading](https://vercel.com#july-2026-summary)July 2026 summary

The July index reports on AI Gateway data collected in June 2026.

- AI Gateway token volume grew - **29%**month over month and spend grew- **27%**. The price per token was flat after rising almost 20% in May.
- Open-weight models ran - **29%**of gateway tokens, up from 11% in April, on under- **4%**of spend. DeepSeek reached- **22.6%**of token volume, in third place and less than two points behind Google, and GLM 5.2 broke into the gateway's top models by volume two weeks after release.
- Anthropic took - **61%**of gateway spend on- **32%**of tokens, and captured- **72%**or more of spend in every high-stakes use case.
- Each modality has a different leader. OpenAI's GPT Image generated - **53%**of images, ahead of Google's Nano Banana at- **39%**. Chinese labs took- **two-thirds**of video spend, while xAI's Grok Imagine generated- **42%**of videos, the most of any model.
- Claude Fable 5 was released June 9 and reached - **22%**of Opus 4.8's request volume in four days. A US export-control directive suspended access for the rest of the month.

[Copy link to heading](https://vercel.com#ai-investment-kept-climbing,-and-the-average-token-price-went-flat)AI investment kept climbing, and the average token price went flat

In June, token volume and spend grew at nearly the same rate, 29% and 27%, while the price per token remained steady. The month before, spend had grown more than twice as fast as volume, driving the average token cost up by almost 20%.

The market spent more overall, but not more per token. Since April, open-weight models have climbed from a ninth of all token volume to nearly a third, at about a tenth of the average token price on the gateway. That alone should have pulled the price per token down. But as cheap volume rose in June, so too did closed-weight frontier prices, up about 12% per token. They offset each other, so the average price per token was flat.

This is evidence of the routing discipline June's report documented, now visible in the aggregate: high-volume work goes to low-cost models, high-risk work stays on the frontier. Investment in AI is still growing quickly, and companies are getting more strategic about balancing that spend across models.

![Usage and spend rose in June; the price per token, up almost 20% in May, held flat](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F3exL6W2TEhTlm4db4LiYyy%2Fccb1c712587f59557920e9fed27ba3ae%2FAI_Gateway_usage__spend__and_price_per_token.png&w=1920&q=75)

![Usage and spend rose in June; the price per token, up almost 20% in May, held flat](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F5XASjvhtz5kwH6BTY9V9LG%2F142008229776a5079a000f0130a47308%2FAI_Gateway_usage__spend__and_price_per_token_dark.png&w=1920&q=75)

[Copy link to heading](https://vercel.com#open-weight-ran-nearly-a-third-of-production-tokens)Open weight ran nearly a third of production tokens

Open-weight models ran 29% of gateway tokens in June on just under 4% of spend. That is nearly a third of the tokens for one twenty-fifth of the dollars.

Open-weight token share has almost tripled since April. Most of that volume comes from the continued growth of DeepSeek, now the third-largest source of tokens on the gateway at 22.6%, behind Anthropic and Google. Google's share of token volume slipped to 24% as its April surge unwound, leaving DeepSeek within two points of second place.

Roughly one in eight enterprise customers now runs an open-weight model in production. And on current trajectories, an open-weight lab will soon be the second-largest by volume on AI Gateway.

![DeepSeek reached 22.6% of gateway tokens in June, less than two points behind Google](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F3U95eP6ROuhM2c34M9jqoO%2F563ce3d0449d146eb0d10806fc3018ab%2Ftoken-volume-share-by-lab-web-light.png&w=1920&q=75)

![DeepSeek reached 22.6% of gateway tokens in June, less than two points behind Google](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F5U1hD0HQ7Sqt2Li13RlHWl%2F5401ae204da1e3d7cd8bdfc8a2fb7da4%2Ftoken-volume-share-by-lab-web-dark.png&w=1920&q=75)

The newest entrant shows the pattern accelerating. Z.ai released GLM 5.2, an MIT-licensed open-weight model aimed at long-horizon agentic work at approximately a fifth of Opus 4.8 pricing. From its June 16 API availability through month end, its daily token volume grew about 50x. It ranked #11 on AI Gateway by tokens in the final week, and as high as #7 on single days. It took 76% of its family's June tokens in barely two weeks. Gemini 3.1 Pro, the fastest in-family migration we had previously charted, took until its second month to reach a similar share.

![GLM 5.2's customer count grew far faster than its token usage in the two weeks after launch](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F5vL0oc9nrmoajVqGhuU880%2F7925e5309d12586218fbb5f820625f8d%2FGLM_5.2_adoption.png&w=1920&q=75)

![GLM 5.2's customer count grew far faster than its token usage in the two weeks after launch](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2FzAZbov1iVb2b0Sjhwb00l%2Fa27c2fe0460141e5f9e3920fefe07c1d%2FGLM_5.2_adoption_dark.png&w=1920&q=75)

[Copy link to heading](https://vercel.com#frontier-labs-kept-nearly-all-of-the-spend)Frontier labs kept nearly all of the spend

The top four frontier US labs took 95% of AI Gateway spend in June. Anthropic alone took 61% of spend on 32% of tokens, down from 65% in May, but in line with April. It also took 72% or more of spend in the most consequential use cases, where mistakes are costly: coding agents, back-office agents, and app generation.

OpenAI’s token share fell from 12.5% to 10.3% while its spend share rose from 13.3% to 16.1%, driving its cost per token up about 50% relative to the market in one month. In contrast to DeepSeek, customers sent OpenAI less volume but costlier work, a divergence that only shows up in production data.

![Anthropic took 61% of June spend; DeepSeek, prominent in the volume chart, is negligible here](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F4kgA7Fvto0w1bLwYJmccBm%2F523e126166cc29fb17525cabc3cc1091%2Fspend-share-by-lab-web-light.png&w=1920&q=75)

![Anthropic took 61% of June spend; DeepSeek, prominent in the volume chart, is negligible here](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F40UyAnldgQjWxTZC1KLmMn%2Fc18b70902d604f0044773d4b9f92f972%2Fspend-share-by-lab-web-dark.png&w=1920&q=75)

[Copy link to heading](https://vercel.com#each-modality-has-a-different-leader)Each modality has a different leader

Image generation is a two-lab race on AI Gateway. OpenAI's GPT Image family generated 53% of images and took 52% of image spend in June. Google's Nano Banana generated almost 39% of images and took 43% of spend. No other family cleared 5% of either.

![Two families generated 92% of the gateway's June images: OpenAI's GPT Image models at 53% and Google's Nano Banana models at 39%](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F1RQPGxk93EpeZclQaJ0Qjk%2F4122cd627deef193a4fdf769799410f1%2Fshare-of-images-generated-by-family-web-light__1_.png&w=1920&q=75)

![Two families generated 92% of the gateway's June images: OpenAI's GPT Image models at 53% and Google's Nano Banana models at 39%](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2FPc0S60l9QZDYCn9ykMPWx%2Fff9b8309648fc89560b6f40f1bc5ca43%2Fshare-of-images-generated-by-family-web-dark__1_.png&w=1920&q=75)

Video is the one modality where Chinese labs currently hold the premium tier. ByteDance's Seedance led spend at 49% with only a third of videos generated. xAI's Grok Imagine generated 42% of videos on 19% of spend, the same volume-discount position DeepSeek holds in text. The Chinese labs together, Seedance, Kling, and Alibaba's Wan, took roughly two-thirds of video dollars. The category is early, so we expect these shares to fluctuate.

![xAI's Grok Imagine generated the most videos on 19% of video spend; ByteDance's Seedance led spend on 34% of the volume](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F6L7qW2LzkYiPvDV9gmVsW3%2F7c3d6723ce8d42bbeaa2a1a233a4d4b0%2Fshare-of-videos-generated-by-family-web-light__2_.png&w=1920&q=75)

![xAI's Grok Imagine generated the most videos on 19% of video spend; ByteDance's Seedance led spend on 34% of the volume](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F1OMsB4BfjLlN7Xj3sJcZtq%2F6a95b10c1a1f90033891030ac80f2569%2Fshare-of-videos-generated-by-family-web-dark__1_.png&w=1920&q=75)

Anthropic leads text, OpenAI leads images, xAI leads video volume, and ByteDance leads video spend. Running the leading model in every modality requires routing across at least three labs.

[Copy link to heading](https://vercel.com#us-export-controls-suspended-claude-fable-5-only-days-after-launch)US export controls suspended Claude Fable 5 only days after launch

Anthropic released Claude Fable 5 on June 9, and it was adopted rapidly. In only four days, Fable usage rose to 22 requests for every 100 sent to Opus 4.8.

![Over its first four days, Fable 5 drew 22% of Opus 4.8's requests](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F5UapE44WFcGjXyKyfGp1HC%2Fd78e2db48da91f06d2b9f586704a365e%2Ffable-5-vs-opus-4-8-web-light__1_.png&w=1920&q=75)

![Over its first four days, Fable 5 drew 22% of Opus 4.8's requests](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F3Oqgy2oc1bj9yeArfDNZOk%2F81f2af8fe0ab285199b33b12f10e321c%2Ffable-5-vs-opus-4-8-web-dark__1_.png&w=1920&q=75)

On June 12, a US export-control directive took effect covering Fable 5, and Anthropic suspended access to comply. The model stayed offline for the rest of the month. Controls lifted on June 30 and access resumed July 1.

[Copy link to heading](https://vercel.com#also-in-june's-data)Also in June's data

- **Back-office agents are the most expensive workload per token on the gateway,**running 5% of total tokens on 14% of total spend.
- **B2B use cases drove 46% of June tokens but 60% of spend;**B2C the reverse, at 43% of tokens and 26% of spend.
- **Google's volume concentrates in consumer-shaped workloads.**It ran 57% of personal-assistant tokens and 54% of education tokens in June, but less than 2% of coding agent tokens.

[Copy link to heading](https://vercel.com#about-this-report)About this report

This analysis is based on anonymized, aggregate routing data from the Vercel AI Gateway through June 2026.

A few notes on measurement:

- *Spend*uses market-rate pricing (published list price) to provide a normalized view across teams that bring their own API keys.
- *Volume*counts tokens routed through AI Gateway.
- *B2C*,- *B2B*, and- *use-case*classifications are aggregate. No individual team or workload is identified.
- *Image*and- *video*figures count generated media (successful requests only), not tokens. Image and video models are not billed per token, so shares reflect images and videos produced.
- *Open-weight models*are measured two ways. Volume and spend shares (the lab-share charts) classify by provider, counting the four labs that serve their own models on the gateway (DeepSeek, MiniMax, Moonshot, Z.ai). This is conservative. The enterprise-adoption figure classifies by model, counting open-weight models regardless of which provider served them, such as Qwen, Gemma, GPT-OSS, and Kimi.
