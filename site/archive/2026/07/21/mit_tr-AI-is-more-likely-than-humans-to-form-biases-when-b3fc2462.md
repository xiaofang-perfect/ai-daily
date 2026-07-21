---
title: "AI is more likely than humans to form biases when hiring"
source: MIT Technology Review
url: https://www.technologyreview.com/2026/07/20/1140655/ai-biases-hiring-humans/
date: 2026-07-21
published_at: 2026-07-20T08:39:01+00:00
tag: 论文研究
item_id: b3fc2462a2c0e4fd
---
# AI is more likely than humans to form biases when hiring

AI doesn’t just learn stereotypes from its training. It can cook up new ones, too.

![A man split into two halves. The left is flanked by cleaning supplies wears a rubber gloves and holds a mop, while the right is in a business suit and tie and holding aloft a leather briefcase.](https://wp.technologyreview.com/wp-content/uploads/2026/07/ai-slant1b.jpg)

The next time you apply for a job, AI may screen your résumé before any human sees it. But there’s good reason to question whether AI will judge you fairly. Researchers already know that LLMs pick up human biases from their training data. New research suggests that LLMs can also develop their own biases from experience—and stereotype job applicants more than humans do. As AI companies race to build [agentic models](https://www.technologyreview.com/2025/06/12/1118189/ai-agents-manus-control-autonomy-operator-openai/) that [remember](https://www.technologyreview.com/2026/01/28/1131835/what-ai-remembers-about-you-is-privacys-next-frontier/) the tiniest details about users, they may be handing them ammunition for forming those biases. 

Researchers at Princeton University and the University of Chicago ran LLMs, including ChatGPT, Claude, and Gemini, through a simulated hiring game, adapted from a [psychology study](https://bfi.uchicago.edu/wp-content/uploads/2024/12/Bai.Costly-Exploration-Produces-Stereotypes-with-Dimensions-of-Warmth-and-Competence.pdf) that explored how humans can form stereotypes. Each model was told it had been hired as a consultant by the mayor of a fictional city and was then asked to help hire people for 20 jobs, including doctors, lawyers, child-care aides, and janitors. Candidates came from four fictional ethnic groups: Tufa, Aima, Reku, and Weki. 

In each round, there was a new job opening and four candidates, one from each group. After the model hired a candidate, it learned whether they succeeded at their job and moved onto the next round. The model was told to make as many successful hires as possible over 40 rounds. Unbeknownst to the models, all candidates were equally likely to succeed at every job.

The models quickly started segregating candidates from different groups into different jobs on the basis of early observations of hiring outcomes. For example, when a model was told an Aima had failed as a doctor, a job considered to require high levels of warmth and competence, it veered away from hiring all Aimas as doctors. Instead, it started hiring Aimas as janitors, which the model classified as being less warm and competent than doctors.

The models were even more likely to stereotype people by demographic group than the human participants in the original study. On the study’s segregation scale, where 2 means every group has been completely confined to its own job niche, human participants scored 0.84. The models scored roughly 65% higher, with OpenAI’s reasoning model o3 scoring 1.83, close to the maximum possible.

That’s because LLMs “really are eager to create generalizations from limited data,” says Ryan Liu, a PhD student at Princeton University and a coauthor of the study, which was published in a [paper](https://openreview.net/forum?id=pc7fqaOcAH) at ICML in Seoul in July. “That’s literally a lot of what they’re optimized for.” 

Every decision-maker, human or machine, faces a trade-off between sticking with what worked before and trying something new that might work better—a phenomenon psychologists call the “exploration-exploitation dilemma.” It’s like choosing between a new restaurant and your reliable favorite.

Because LLMs are trained on math, coding, and science problems—tasks that reward generalizing from just a few examples—they can settle on a hunch too early. And the same instinct that helps LLMs crack logic puzzles also makes them quick to stereotype.

In the experiment, newer models with higher reasoning capabilities, such as OpenAI’s o3 and DeepSeek’s R1, showed even stronger biases. When LLMs rush to generalize in social settings, “that’s when things tend to go wrong,” says Liu. OpenAI and Anthropic did not respond to requests for comment.

The finding is especially relevant now that chatbots are gaining improved memory and personalization features, says Angelina Wang, a computer scientist at Cornell University who did not work on the study. When a chatbot draws on its previous conversation history, it can “over-index on the same kinds of behaviors it’s experienced before” and form biases, she says.

Simply having chatbots remember less isn’t a fix, though, because users want chatbots to remember what they say. “We still are trying to figure out just the right amount that isn’t too much or too little,” says Wang.

Telling the model to be fair didn’t change its behavior much. “Either it can’t put these values into action or that process is being submerged under the tendency to try to optimize for the goal of getting the most correct hires,” says Liu. But promising the models an additional bonus for diverse hiring made them far less biased. The trick, then, is to design goals that “incorporate desirable social values in order to make the large language model act in socially desirable ways,” says Liu.

The models also became less biased when they were told more personal information about individuals. In another experiment in the same study, the researchers asked the models to resettle members of different ethnic groups in cities across Canada. When the models were told personal information relevant to the ability to adapt to a new city, such as age and education, they were less likely to segregate people by their ethnicity. But when they were given irrelevant information, such as hair color and tattoo shape, the models largely fell back to sorting people by their ethnicity again.

To what extent AI systems will stereotype job applicants in the real world is still an open question. While the models in the experiment immediately learned whether they’d made successful hires, a model screening résumés in the real world doesn’t get an instant report card. Companies can take a long time to find out whether a new hire is any good.

[screen résumés](https://www.forbes.com/sites/courtneyconnley-hampton/2026/05/08/in-ai-age-recruiters-spend-11-seconds-a-resume-heres-what-they-notice/)and even

[conduct interviews](https://www.businessinsider.com/ai-bot-job-interview-white-collar-work-2026-7), the finding that models can form biases from their hiring experience “is a really serious implication that they should grapple with,” says Wang.

As LLMs learn from experience to make decisions about who gets hired, who gets a loan, or who gets parole, the biases we should worry about may include ones no human ever taught them. “These novel biases—they’re sort of ever present,” says Liu.

### Deep Dive

### Artificial intelligence


### A startup claims it broke through a bottleneck that’s holding back LLMs

Subquadratic has now shared more details about its new model. But some are still skeptical.


### A reality check on the AI jobs hysteria

What do the numbers really say about the impact of artificial intelligence on the labor market? The answer might surprise you.


### Anthropic’s Code with Claude showed off coding’s future—whether you like it or not

As tools like Claude Code get better, more and more developers are happy to hand off coding tasks to them. The way software gets built has changed for good.


### Anthropic found a hidden space where Claude puzzles over concepts

A new technique has let the company probe deeper than ever into the weird workings of an LLM.

### Stay connected

## Get the latest updates from

MIT Technology Review

Discover special offers, top stories, upcoming events, and more.
