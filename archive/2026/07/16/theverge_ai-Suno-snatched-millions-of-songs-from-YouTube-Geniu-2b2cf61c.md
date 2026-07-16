---
title: "Suno snatched millions of songs from YouTube, Genius, and Deezer"
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/966072/suno-ai-music-training-scraping-youtube-hack
date: 2026-07-16
published_at: 2026-07-15T13:48:01-04:00
tag: 行业动态
item_id: 2b2cf61c3d5ae6ec
---
Suno data obtained in a hacking incident has exposed that the AI music generator was trained by scraping millions of songs and lyrics from online audio platforms, including YouTube Music, Deezer, and Genius, *404 Media**actually* been taking from online platforms.

That’s relevant because Suno has been the subject of several lawsuits that allege it used [copyrighted materials](/ai-artificial-intelligence/906896/sunos-copyright-ai-music-covers) to train its AI models. In [a notable case](/2024/6/24/24184710/riaa-ai-lawsuit-suno-udio-copyright-umg-sony-warner) filed by the Recording Industry Association of America (RIAA), [Suno openly admitted](/2024/8/2/24211842/ai-music-riaa-copyright-lawsuit-suno-udio-fair-use) that it does so, arguing that training on copyrighted materials and publicly available music files from the open internet is legally permitted under fair use doctrine. Whether or not a court agrees with that, an amendment filed by the RIAA last year also alleges that Suno unlawfully circumvented YouTube’s copyright protections by intentionally [“stream ripping” tracks](/news/782448/riaa-suno-ai-lawsuit-update-stream-ripping-youtube) from the platform.

Materials shared with *404 Media* by the hacker, referred to as “ellie.191,” reportedly back up those allegations. The data includes Suno source code from 2023 and 2024, alongside scraping instructions to pull audio files from YouTube Music, Deezer, Genius, Pond5, Jamendo, Freesound, and the International Music Score Library Project (IMSLP). Other leaked code reportedly suggests that Suno used a third-party company called Bright Data to scrape music from YouTube, and seemingly searched for a cappella versions of songs on the platform to source vocal-only audio.

A file for YouTube Music notes that Suno had consumed 2,013,545 YouTube Music clips at the point it was last updated. According to another file, datasets compiled by Suno included hundreds of thousands of hours of YouTube Music, thousands of hours of Deezer, Genius, IMSLP, Jamendo, and Pond5, and hundreds of hours of Freesound and MuseScore lyrics. Suno also sought to download roughly one million hours of podcasts via an online tool called PodcastIndex, according to additional code.

“As we have stated in public filings and [disclosures](https://help.suno.com/en/articles/9709569?ref=404media.co), Suno’s AI models have been trained on publicly available music files and related metadata accessible on third-party websites on the open Internet,” an unnamed Suno spokesperson said in a statement to *404 Media*.

Suno customer information was also accessed by the hacker, which included email addresses, phone numbers, and Stripe payment details. Some of the customers contacted by *404 Media* confirmed that they had signed up for the service, and said that Suno never notified them about a security breach.

In a statement to *404 Media*, a Suno spokesperson said the company became aware of a security incident in November 2025, and that the situation was quickly contained.

“At the time, we immediately conducted an investigation and verified that the incident primarily involved outdated source code that is no longer in use at Suno and that no sensitive personal information was compromised. Importantly, Suno does not have access to customers’ full credit card numbers in Stripe,” the Suno spokesperson said. “Based on the limited nature of the customer information believed to be involved, we determined that individual notifications were not warranted under applicable privacy laws.”
