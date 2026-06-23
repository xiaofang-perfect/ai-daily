---
title: "Sakana Fugu"
source: TLDR AI · 2026-06-22
url: https://threadreaderapp.com/thread/2068862070062485867.html?utm_source=tldrai
date: 2026-06-23
published_at: 2026-06-22T12:00:00+00:00
tag: 产品发布
item_id: 6f376e8ed967101f
---
**
              
              This Thread may be Removed Anytime!**
          

Twitter may remove this content at anytime! Save it as PDF for later use!

- Follow [@ThreadReaderApp](https://twitter.com/threadreaderapp)to mention us!
- From a Twitter thread mention us with a keyword "unroll"

`@threadreaderapp unroll`
          [Practice here](https://twitter.com/threadreaderapp/status/1054877865362112513) first or read more on our [help page](https://threadreaderapp.com/help)!

We’re excited to introduce AB-MCTS!


Our new inference-time scaling algorithm enables collective intelligence for AI by allowing multiple frontier models (like Gemini 2.5 Pro, o4-mini, DeepSeek-R1-0528) to cooperate.


Blog:[sakana.ai/ab-mcts](https://sakana.ai/ab-mcts)

Paper:[arxiv.org/abs/2503.04412](https://arxiv.org/abs/2503.04412)


Inspired by the power of human collective intelligence, where the greatest achievements arise from the collaboration of diverse minds, we believe the same principle applies to AI. Individual frontier models like ChatGPT, Gemini, and DeepSeek are remarkably advanced, each possessing unique strengths and biases stemming from their training, which we view as valuable resources for collective problem-solving.


AB-MCTS (Adaptive Branching Monte Carlo Tree Search) harnesses these individualities, allowing multiple models to cooperate and engage in effective trial-and-error, solving challenging problems for any single AI. Our initial results on the ARC-AGI-2 benchmark are promising, with AB-MCTS combining o4-mini + Gemini-2.5-Pro + R1-0528, current frontier AI models, significantly outperforming individual models by a substantial margin.


This research builds on our 2024 work on evolutionary model merging, shifting focus from “mixing to create” to “mixing to use” existing, powerful AIs. At Sakana AI, we remain committed to pioneering novel AI systems by applying nature-inspired principles such as evolution and collective intelligence. We believe this work represents a step toward a future where AI systems collaboratively tackle complex challenges, much like a team of human experts, unlocking new problem-solving capabilities and moving beyond single-model limitations.


Algorithm (TreeQuest):[github.com/SakanaAI/treeq…](https://github.com/SakanaAI/treequest)

ARC-AGI Experiments:[github.com/SakanaAI/ab-mc…](https://github.com/SakanaAI/ab-mcts-arc2)![Image](/images/1px.png)


          Our new inference-time scaling algorithm enables collective intelligence for AI by allowing multiple frontier models (like Gemini 2.5 Pro, o4-mini, DeepSeek-R1-0528) to cooperate.

Blog:

Paper:

Inspired by the power of human collective intelligence, where the greatest achievements arise from the collaboration of diverse minds, we believe the same principle applies to AI. Individual frontier models like ChatGPT, Gemini, and DeepSeek are remarkably advanced, each possessing unique strengths and biases stemming from their training, which we view as valuable resources for collective problem-solving.

AB-MCTS (Adaptive Branching Monte Carlo Tree Search) harnesses these individualities, allowing multiple models to cooperate and engage in effective trial-and-error, solving challenging problems for any single AI. Our initial results on the ARC-AGI-2 benchmark are promising, with AB-MCTS combining o4-mini + Gemini-2.5-Pro + R1-0528, current frontier AI models, significantly outperforming individual models by a substantial margin.

This research builds on our 2024 work on evolutionary model merging, shifting focus from “mixing to create” to “mixing to use” existing, powerful AIs. At Sakana AI, we remain committed to pioneering novel AI systems by applying nature-inspired principles such as evolution and collective intelligence. We believe this work represents a step toward a future where AI systems collaboratively tackle complex challenges, much like a team of human experts, unlocking new problem-solving capabilities and moving beyond single-model limitations.

Algorithm (TreeQuest):

ARC-AGI Experiments:

The AB-MCTS combination of o4-mini + Gemini-2.5-Pro + R1-0528, current frontier AI models, achieves strong performance on the ARC-AGI-2 benchmark, outperforming individual models by a large margin.


We open-sourced our implementation of AB-MCTS:

[github.com/SakanaAI/treeq…](https://github.com/SakanaAI/treequest)![Results of AB-MCTS and Multi-LLM AB-MCTS on ARC-AGI-2, showing Pass@k as a function of the number of LLM calls.](/images/1px.png)


          We open-sourced our implementation of AB-MCTS:

Many ARC-AGI-2 examples that were unsolvable by any single LLM were solved by combining multiple LLMs. In some cases, an initially incorrect attempt by o4-mini is used by R1-0528 and Gemini-2.5-Pro as a hint to get to the correct solution.


ARC-AGI-2 code:

 [github.com/SakanaAI/ab-mc…](https://github.com/SakanaAI/ab-mcts-arc2)![An example problem from ARC-AGI-2. The task is to infer the common transformation rule from the three demonstration cases on the left and apply it to the test case on the right. This is one of the problems that became solvable using Multi-LLM AB-MCTS.](/images/1px.png)


      ARC-AGI-2 code:
