---
title: "Google’s AlphaGenome 2 zooms in on the cellular roots of disease"
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/1031524/google-deepmind-alphagenome-2-genetic-ai-model
date: 2026-11-12
published_at: 2026-11-11T10:00:00-05:00
tag: 论文研究
item_id: d7b620cf325a0d82
---
Researchers at Google DeepMind have unveiled a new AI model designed to unravel how changes in our DNA affect different cells, giving scientists a more detailed view of a notoriously difficult problem that could hold important clues to the causes of disease — and point the way to new treatments.

# Google’s AlphaGenome 2 zooms in on the cellular roots of disease

DeepMind’s new DNA model better predicts how mutations affect different cells, potentially opening paths to treatment.

![alphagenome-atlas-cover\_\_background](https://platform.theverge.com/wp-content/uploads/sites/2/2026/09/alphagenome-atlas-cover__background.jpg?quality=90&strip=all&crop=7.8125%2C0%2C84.375%2C100&w=2400)

![alphagenome-atlas-cover\_\_background](https://platform.theverge.com/wp-content/uploads/sites/2/2026/09/alphagenome-atlas-cover__background.jpg?quality=90&strip=all&crop=7.8125%2C0%2C84.375%2C100&w=2400)

*A graphic representing Google’s AlphaGenome Atlas.*

![Robert Hart](https://platform.theverge.com/wp-content/uploads/sites/2/2025/09/ROB_H_BLURPLE.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=96)

*The Verge*covering all things AI and a Senior Tarbell Fellow. Previously, he wrote about health, science and tech for

*Forbes*.

AlphaGenome 2 is the successor to DeepMind’s genome-predicting AI model AlphaGenome, which was [released last year](https://deepmind.google/blog/alphagenome-ai-for-better-understanding-the-genome/). While nearly every cell in the human body carries the same DNA, different types of cells — from heart muscle cells and skin cells to immune cells fighting an infection — switch different genes on and off, and those patterns can change depending on what a cell is doing. As a result, the same genetic variant can have very different effects depending on the type and state of the cell.

The new model is designed to capture those differences, predicting the effects of genetic variants on individual cell types and states. Google said in a [blog post](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/) published Wednesday that it offers a much finer-grained view than broader models like AlphaGenome, potentially revealing disease-relevant effects in specific cells that might otherwise go unnoticed.

AlphaGenome 2 was trained on more than 100 million individual cell profiles across 68 tissues to give it that more detailed view. DeepMind says the model effectively turns static cell atlases — [huge data repositories that map and catalog](https://www.bbc.co.uk/news/articles/c23829l8kzro) individual cells in detail — “into a predictive engine for human genetics.” According to the company, AlphaGenome 2 identifies nearly twice as many variants that can change gene expression in cells than its previous state-of-the-art model.

Notably, the researchers found that AlphaGenome 2 could also make predictions about new types of cells and biological states without needing to be retrained. It could also identify gaps in experimental data, potentially helping scientists decide what to investigate next in the lab.

For Adam Gayoso, a research scientist at Google DeepMind involved in the project, the big breakthrough is “tying human genetics to cell biology.” AlphaGenome 2 gives researchers a way to drill down on genetic variants identified in large populations, to see what effects they may be having on a cellular level, and potentially connect those effects to disease, he told *The Verge*.

Google DeepMind’s genomics lead Žiga Avsec told *The Verge* that this specificity is important if you have a goal like figuring out how to treat a particular disease. “When you develop drugs, you’re targeting specific proteins and specific cell types,” he explained, which makes having this kind of granularity vital.

Building a model like AlphaGenome 2 has only recently become possible thanks to new technologies that can capture individual cells and their states at high resolution and create the vast datasets needed to train it, Avsec said. DeepMind is now working to improve its genetics models by generating more data, including for cell states that aren’t represented well today. Avsec said future versions could also potentially be trained on data “across multiple species,” giving the models a broader view of biology. Longer term, he said models like AlphaGenome 2 could feed into efforts to create “[virtual cells](https://www.nature.com/articles/d41586-026-01731-1),” digital simulations designed to mimic biological systems.

Although Avsec said he views AlphaGenome 2 as a successor to AlphaGenome, it isn’t replacing it any time soon. He said its more detailed predictions come at a computational cost and are “more expensive” to produce than those of its predecessor, he said. Those demands would have made it impractical to use AlphaGenome 2 to produce the genome-wide [Atlas](https://www.theverge.com/ai-artificial-intelligence/991180/google-launches-alpha-genome-atlas) covering “every possible DNA letter change in the human genome” that DeepMind released in September.

Google says it is making AlphaGenome 2 available for non-commercial research via the AlphaGenome API from today, with a limited “private preview” for commercial research.

The model is the latest in a growing array of efforts by Google and rival AI labs to use the technology to tackle major problems in science and medicine. Pushmeet Kohli, who heads DeepMind’s AI for science research, has [hinted](https://x.com/pushmeet/status/2119373171321196892?a=XN98ecEJmbYrhiVYeEQ&s=20) that more impressive scientific results are on the way, and the organization is expected to open an automated materials science lab in the UK soon. Anthropic, meanwhile, has been [experimenting](https://www.theverge.com/ai-artificial-intelligence/961311/anthropic-claude-science-ai-drug-development) with drug [design](https://www.theverge.com/ai-artificial-intelligence/1016443/anthropic-claude-citrini-vibecoding-scorpion-antivenom) and given Claude a [wet lab](https://www.theverge.com/ai-artificial-intelligence/999470/anthropic-biolab-claude-crispr), while OpenAI has been [mowing down](https://www.theverge.com/ai-artificial-intelligence/1004933/ai-math-openai-breakthrough-solution) an [impressive](https://www.theverge.com/ai-artificial-intelligence/1001477/openai-math-advisory-group) [amount](https://www.theverge.com/ai-artificial-intelligence/1005004/openai-math-release-github) of [longstanding](https://www.theverge.com/ai-artificial-intelligence/1019921/openai-breakthrough-math-computer-science-physics) [problems](https://www.theverge.com/ai-artificial-intelligence/977273/the-ai-takeover-of-mathematics-has-begun) in [mathematics](https://www.theverge.com/ai-artificial-intelligence/1008726/openai-mathematics-solutions-chaos) and [related fields](https://www.theverge.com/ai-artificial-intelligence/994255/openai-millennium-prize-problem-tristan-buckmaster-competition).

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.
