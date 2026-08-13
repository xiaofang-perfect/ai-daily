---
title: "The web's newest weapon against AI scrapers is a font"
source: Hacker News
url: https://arstechnica.com/ai/2026/08/new-font-turns-ordinary-webpages-into-nonsense-for-ai-scrapers/
date: 2026-08-13
published_at: 2026-08-13T01:30:31+00:00
tag: 工具开源
item_id: 1b112cccf698291e
---
AI companies’ penchant for [scraping through large swathes of the public web](https://arstechnica.com/ai/2025/03/devs-say-ai-crawlers-dominate-traffic-forcing-blocks-on-entire-countries/) in search of [valuable training data](https://arstechnica.com/information-technology/2024/01/openai-says-its-impossible-to-create-useful-ai-models-without-copyrighted-material/) has already led to [lawsuits](https://arstechnica.com/tech-policy/2025/10/reddit-sues-to-block-perplexity-from-scraping-google-search-results/) and [technical fixes](https://arstechnica.com/tag/ai-scraping/) aimed at stopping the practice. Now, a pair of designers are hoping to stymie these scrapers with a new font designed to offer people a perfectly readable webpage while serving scrapers a subtly edited, nonsensical version in the underlying HTML.

ShieldFont, as designers Isaque Seneda and Gabriel Abrucio [write in a recent white paper](https://shieldfont.org/white-paper/), was made to offer web publishers “a practical opt-out from unauthorized AI training and [to] disrupt what is collected when that choice is ignored.”

## When is a horse a potato?

The font is based around [ligatures](<https://en.wikipedia.org/wiki/Ligature_(writing)>), a long-standing feature of many fonts that is usually used to replace certain letter pairs with a more readable version when they’re smushed up next to each other. With ShieldFont, though, those ligatures are instead used to replace entire words with others in an attempt to destroy the text’s value to scrapers. This substitution only happens when the font engine draws the page on screen, meaning scrapers that simply download plaintext source code get an altered version that end users never see.

When it comes to fooling AI scrapers, though, not all ligature-based word replacements are created equal. Simply replacing common words with synonyms or antonyms would be too easy for a smart scraper to reverse. On the other end, replacing words with completely unrelated gibberish could lead to easier detection (and potentially circumvention) by a smart scraping filter.
