---
title: "Mozilla says 271 vulnerabilities found by Mythos and 'almost no false positives'"
source: Hacker News
url: https://arstechnica.com/information-technology/2026/05/mozilla-says-271-vulnerabilities-found-by-mythos-have-almost-no-false-positives/
date: 2026-05-08
published_at: 2026-05-07T19:36:45+00:00
tag: 工具开源
item_id: d5105ddbb34ebfa0
---
The disbelief was palpable when Mozilla’s CTO last month declared that AI-assisted vulnerability detection meant “[zero-days are numbered](https://arstechnica.com/ai/2026/04/mozilla-anthropics-mythos-found-271-zero-day-vulnerabilities-in-firefox-150/)” and “defenders finally have a chance to win, decisively.” After all, it looked like part of an all-too-familiar pattern: Cherry-pick a handful of impressive AI-achieved results, leave out any of the fine print that might paint a more nuanced picture, and let the hype train roll on.

Mindful of the skepticism, Mozilla on Thursday provided a behind-the-scenes look into its use of Anthropic Mythos—an AI model for identifying software vulnerabilities—to ferret out 271 Firefox security flaws over two months. In a [post](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/), Mozilla engineers said the finally ready-for-prime-time breakthrough they achieved was primarily the result of two things: (1) improvement in the models themselves and (2) Mozilla’s development of a custom “[harness](https://arxiv.org/abs/2603.28052)” that supported Mythos as it analyzed Firefox source code.

## “Almost no false positives”

The engineers said their earlier brushes with AI-assisted vulnerability detection were fraught with “unwanted slop.” Typically, someone would prompt a model to analyze a block of code. The model would then produce plausible-reading bug reports, and often at unprecedented scales. Invariably, however, when human developers further investigated, they’d find a large percentage of the details had been hallucinated. The humans would then need to invest significant work handling the vulnerability reports the old-fashioned way.

Mozilla’s work with Mythos was different, Mozilla Distinguished Engineer Brian Grinstead said in an interview. The biggest differentiating factor was the use of an [agent harness](https://parallel.ai/articles/what-is-an-agent-harness), a piece of code that wraps around an LLM to guide it through a series of specific tasks. For such a harness to be useful, it requires significant resources to customize it to the project-specific semantics, tooling, and processes it will be used for.

Grinstead described the harness his team built as “the code that drives the LLM in order to accomplish a goal. It gives the model instructions (e.g., ‘find a bug in this file’), provides it tools (e.g., allowing it to read/write files and evaluate test cases), then runs it in a loop until completion.” The harness gave Mythos access to the same tools and pipeline that human Mozilla developers use, including the special Firefox build they use for testing.

It works when given a very clear, easily machine verified goal. They've basically taken what they've learned from machine speed training and applied it to finding memory bugs, where basically if the process crashed, you've succeeded. So what is described here at least is quite a narrow window of capability, when given a very clear success/failure model which can be automatically marked by another process, model , or algorithm.

The harness is what turns an AI model onto an AI system, and it is absolutely key to success.

It is a new arms race: How fast will the AI attack tools improve relative to the AI defense tools? If history is any lesson, the defenders will not be able to keep ahead of the attackers. I hope I am wrong, but history says I am correct.

Will AI change our future history? Only time will tell.

And great article -- appropriately skeptical but not negative.

There is real public good achieved here, and that's exactly the way for commercial companies to earn good will. Especially since covering 20+ years of historical code is largely a one-off (yes, there will be even more competent models; and yes, running them on FF and other major / foundational OSS projects is a win-win)

The alternative was just releasing it once ready and getting blamed for bad people using it.

There is no alternative of stopping work on AI, other AIs are getting there too, some with less safeguards, and some will probably be open-weights for which any safeguards can probably be disabled.

whyXYZ changed. The logic walk through is as important as the code itself, although you cansometimesget the logic by reading the code. It's just not always the case without a lot of practiced skill in complex code trees.For now, I think the reasonable stance here is to give Mozilla the benefit of the doubt and to point out that it's

not just Mythos one has to be worried about. People have tunnel vision. The forest itself is changing. The newer models are all closing in on useful contributions when properly directed to detecting problems in existing code bases. That's what arm chair experts and luddites are missing. It's a paradigm shift much like automated fuzzers and automatically generated testing harnesses gave us a few years ago (and generated similar backlash). Conservative programmers can bury their head in the sand all they want, but *LM-users are going to blow right past them in the near future much like fuzzer users blew people away sticking to meticulously piecing through code in a debugger, or a skilled debugger user adeptly outperforming someone that never moved past inserting print statements in code. 30 years ago no college CS course taught how to build test harnesses for software nor bothered considering input sanitation as anything beyond a UX exercise. Now, building testing harnesses and security considerations, including fuzzing tools, language agnostic and specific advanced debugging techniques, and input management techniques are part of any well crafted CS course. The question isn't if, it's when managing *LM tooling becomes equally required in CS degrees.
