---
title: "Anthropic's compute spending is increasing by 4x per year, outpacing OpenAI's 3x"
source: TLDR AI · 2026-11-19
url: https://epoch.ai/data-insights/anthropic-openai-compute-spend-growth?utm_source=tldrai
date: 2026-11-20
published_at: 2026-11-19T12:00:00+00:00
tag: 行业动态
item_id: 7df815f3e56c0d28
---
Epoch's work is free to use, distribute, and reproduce provided the source and authors are credited under the Creative Commons BY license.

## Learn more about this graph

We compile reports and disclosures about Anthropic and OpenAI’s spending on compute over time, and convert these figures into spending run rates to estimate how quickly each company has ramped up their compute spending over the past several years.

### Data

For Anthropic, we use compute spending figures from the company’s Form [S-1](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm), filed in advance of its IPO.
The S-1 disclosed “compute and infrastructure” spending for the [seven calendar quarters](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm#i199fd6a8a0664d5da497db9a78cf0452_103:~:text=Quarterly%20Consolidated%20Statements%20of%20Operations) from 2025 through Q3 2026, as well as [annual totals in 2023 and 2024](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm#i199fd6a8a0664d5da497db9a78cf0452_97:~:text=Compute%20and%20infrastructure%20expenses%20for%20the%20year%20ended%20December%2031%2C%202024%20increased).
It also disclosed spending commitments of $447.5 billion, “substantially all” related to compute and infrastructure, from September 2026 through the end of 2030, or around $100 billion per year.
We primarily rely on the amended [S-1](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm) filed on November 2; [the original](https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm) is also available.

For OpenAI, we source compute spend from media reports.
The figures are compiled in our [AI companies](https://epoch.ai/data/ai-companies?view=graph&tab=compute) data explorer, along with earlier reports about Anthropic.
However, as of this writing, the explorer only visualizes annual totals through 2025, and does not include quarterly spending disclosures from Anthropic’s S-1.
Additionally, OpenAI President Greg Brockman [testified](https://www.reuters.com/technology/openai-projects-50-billion-spending-computing-power-this-year-brockman-says-2026-05-05/) in May 2026 that the company expects to spend $50 billion on compute this year, but we do not have any non-forecasted figures for OpenAI in 2026.

Because these spending figures are a mix of quarterly and annual data, they need to be converted to annualized run rates for direct comparison. This requires some estimation and interpolation, which is explained below.

We do not adjust for inflation.

### Analysis

Code for the data analysis can be found [in this notebook](https://colab.research.google.com/drive/1yK22-eZE9VpmD5RhegbvactOpGTfaLXY#scrollTo=6cbd85eb).

All of Anthropic and OpenAI’s compute spend figures are period-based totals for a given year or quarter. To compare a mix of annual and quarterly data, we convert them into estimated annualized spending rates. For quarterly numbers, this means multiplying the spending amount by four. We also need to attribute the spending rates for each period to an exact date. We assign each spending estimate a date by assuming that spending grew at a steady exponential rate between reporting periods. The dates are one to three days after the midpoint of the quarter, or two to four weeks after the midpoint of the year.

We then fit growth rates to these points via a log-linear regression. We derive 90% confidence intervals analytically using standard errors. Uncertainty in the assigned dates introduces an additional source of uncertainty, but modeling it had little effect on the resulting confidence intervals.

Both Anthropic and OpenAI rely primarily on compute capacity from cloud partners such as Amazon, CoreWeave, Google, Microsoft, Oracle, and SpaceX.
It would be misleading to compare upfront compute spending (e.g. capital expenditures) with ongoing operating expenses on cloud compute, but neither company incurs a significant amount of upfront compute spending.
Per its S-1, Anthropic will increasingly use TPUs that it leases directly (“Anthropic Direct”), but these lease payments will still be amortized (discussed further in [previous commentary](https://epoch.ai/gradient-updates/will-financing-bottleneck-ai-compute)).

Most of Anthropic’s compute is used internally for R&D and other purposes, not to serve external customers.
Anthropic’s [S-1](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm#i199fd6a8a0664d5da497db9a78cf0452_331:~:text=The%20following%20table%20presents%20the%20Company%E2%80%99s%20operating%20expenses%20grouped%20by%20function) discloses its customer inference spending as “cost of revenue,” which is “substantially all” compute:

- In 2025, Anthropic’s cost of revenue was $2.773 billion, or 38% of its $7.326 billion in total compute spending.
- In the first 9 months of 2026, this share decreased to just 26%, or $4.812 billion in cost of revenue against $18.8 billion in compute spend.

“Cost of revenue” is a slight underestimate of external inference spending because Anthropic classifies compute used by free-tier customers as sales and marketing expenses rather than cost of revenue. Anthropic’s sales and marketing expenses in the first nine months of 2026 were $5.5 billion, and most of the year-on-year growth in these expenses—$4.8 billion out of a total $5.2 billion increase—came from revenue-sharing fees paid to cloud partners, not compute costs. This means that total free-tier compute spend is minor, at most in the hundreds of millions.

By comparison, media reports [indicate](https://epoch.ai/data/ai-companies?view=graph&tab=compute) that around 50% of OpenAI’s compute spending was allocated to customer inference in 2025, up from roughly one-third in 2024.

We do not have full data on each developer’s spending with its cloud partners, but Anthropic made up [34.5%](https://www.bloomberg.com/news/articles/2026-10-29/spacex-s-largest-revenue-source-is-a-finite-deal-with-anthropic) of SpaceX’s total revenue in Q3 2026, or around $5 billion, half of Anthropic’s compute spend that quarter.

In terms of future growth, Anthropic has also already contractually committed to $447.5 billion in future compute spending through 2030 per its S-1.
This would be roughly another doubling from the current rate, so it is not clear that Anthropic’s future compute spending will grow at anywhere near the 4x annual growth of the past three years, though the company notes that it may spend even more on compute before 2030 than this current committed total.
Meanwhile, OpenAI plans to spend around [$750 billion](https://finance.yahoo.com/technology/ai/articles/openai-raises-planned-ai-infrastructure-134830365.html) on compute over the same period.

### Assumptions and limitations

- OpenAI’s compute spending figures come from media reporting, not from disclosed financial statements, so there is more uncertainty in the underlying accuracy and interpretation of the numbers.
- Dollar spending cannot be straightforwardly converted into other metrics of compute capacity, such as floating point operations per second or watts of power.
This relationship can vary according to the composition of a developer’s chip fleet, as well as the terms of cloud compute deals and pricing trends in the AI compute rental market over time.
Our analysis of AI compute capacity [used by frontier AI developers](https://epoch.ai/data/ai-chip-users?view=graph&tab=main) involves some modeling from cloud compute spending (among other inputs); for more information, see the AI chip users [methodology](https://epoch.ai/data/ai-chip-users-documentation/methodology#anthropic).
- While it is safe to assume that a large majority of these companies’ compute spending is for capacity directly supporting AI research and the training and inference of AI models, we do not know exactly how this spending breaks down between AI accelerator capacity, dedicated CPU capacity related to training or inference, or general cloud compute capacity for other parts of the technology stack.

## Download this data

## Explore this data

![AI companies](https://epoch.ai/assets/images/datahub/thumbnails/small/ai-companies.png)

AI company data, with data on revenue, funding, staff, and compute for many of the key players in frontier AI.
