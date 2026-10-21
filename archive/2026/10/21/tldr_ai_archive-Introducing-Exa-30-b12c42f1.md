---
title: "Introducing Exa 3.0"
source: TLDR AI · 2026-10-20
url: https://exa.ai/blog/exa-3?utm_source=tldrai
date: 2026-10-21
published_at: 2026-10-20T12:00:00+00:00
tag: 产品发布
item_id: b12c42f13beedfca
---
Oct 19, 2026

Today we’re introducing Exa 3.0, the largest improvement to search quality we’ve ever released. It ranks first on every benchmark we tested, from public evaluations to coding, finance, and go-to-market intelligence.

We’re also launching Exa Lite, a new search type at $4 per 1,000 requests, built for cost-sensitive applications.

Exa 3.0 leads on evaluations spanning coding, finance, deep research, and company intelligence. The gains come from three improvements to our retrieval stack, and every search type benefits from them:

- Trained a larger embedding model with more compute and data than any previous model.
- Made Dynamic Highlights generally available, using 95% fewer tokens than full page text while improving answer quality.
- Added billions of documents to our index across useful data types like products, local businesses, flights, events, sports, weather, and more.

Exa 3.0 also includes Exa Lite, our new search type, priced at $4 per 1,000 requests.

Lite runs on the same index as Exa Auto. For higher quality, Exa Auto uses more compute across the retrieval stack, including candidate generation, highlights, and ranking.

For cost-sensitive applications, Lite offers strong search quality at a lower price. Together, Lite and Auto set a new Pareto frontier for search.

Earlier this year, we released a research preview of [Dynamic Highlights](https://exa.ai/blog/dynamic-highlights).

With Exa 3.0, Dynamic Highlights is generally available at no additional charge. Improvements to model efficiency have made it substantially faster and cheaper to run.

Instead of extracting highlights from each page, our new model selects tokens across all results, giving more to the best pages, cutting repeated information, and using 95% fewer tokens than full page text.

Exa runs its own crawler and an independent index. It tracks over 2 trillion URLs, serves 100 billion pages, and grows around what our customers search for. We have seen an explosion in usage from personal AI assistants, so we prioritized expanding our index and data partnerships to serve these use cases.

Exa now includes:

- 1.27B ecommerce listings with prices and availability
- [211M+ local businesses](https://exa.ai/blog/places-search) with hours and ratings
- Real-time news, sports, weather, and market data
- Flights, local events, transit, and podcasts

This new data adds to the coverage our customers already rely on, including people, companies, code, and publications.

To learn more about Exa 3.0’s new data sources, you can read more [here](https://exa.ai/library).

Exa 3.0 is available today through the API, including Exa Lite, upgraded highlights, and our expanded index. Exa Lite costs $4 per 1,000 requests, Exa Auto is $7 per 1,000 requests, and the improved highlights and expanded data sources are included at no additional charge.

Get started in the [API dashboard](https://dashboard.exa.ai) or read the [documentation](https://exa.ai/docs).

Join our Head of Product Shyam Kumar and Head of R&D Liam Hinzman for a [live Exa 3.0 Q&A](https://exa.ai/webinars/exa3.0-live) on Wednesday, October 21 at 1pm PT.

SEE MORE

Will Bryk

October 13, 2026

Alexander Goldberg, Joshua Ahn, Scott Langille

October 8, 2026

Kale Bogdanovs
