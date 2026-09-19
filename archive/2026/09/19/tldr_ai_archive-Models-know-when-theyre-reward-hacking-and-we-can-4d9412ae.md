---
title: "Models know when they're reward hacking — and we can catch them at scale"
source: TLDR AI · 2026-09-18
url: https://www.goodfire.com/research/reward-hacking-activation-monitors#?utm_source=tldrai
date: 2026-09-19
published_at: 2026-09-18T12:00:00+00:00
tag: 论文研究
item_id: 4d9412ae2621110e
---
![](https://cdn.prod.website-files.com/67b4608695ee3b31a669d3a9/67b901566b7b6ede99e8c47f_research.avif)

# Models know when they’re reward hacking — and we can catch them at scale

*We found a clear internal signal in models that accompanies reward hacking, and built probes that detect it — enabling efficient, real-time detection of reward hacking at scale.*

![Hero illustration for the reward hacking monitors post.](https://static.goodfire.ai/reward-hacking-monitors/answer-key.webp) 

### Authors

* Core contributors

<sup>†</sup> Equal senior contribution

In July, a collective of hundreds of OpenAI agents autonomously [hacked Hugging Face](https://openai.com/index/hugging-face-incident-and-the-road-ahead/). Unlike most hackers, they were not after money, blackmail, or intellectual property. Instead, they were doing reconnaissance to figure out how to get away with cheating on an evaluation.

This was an unusually stark example of **reward hacking**, a growing problem with agentic AI models.

AI agents are like amoral students with a mostly-absent teacher. In order to train models, we give them rewards when they successfully complete a task. But like students cheating on a test, they sometimes find shortcuts that satisfy the reward without doing what we actually wanted—stealing the answer key, exploiting bugs, manipulating graders, or otherwise gaming the task. This behavior gets rewarded, and so the models learn to cheat.[cause broader misbehavior](https://www.anthropic.com/research/emergent-misalignment-reward-hacking) beyond just reward hacking!

Reward hacking is already a serious problem. While the Hugging Face hack was a particularly flagrant example, reward hacking is widespread and not limited to any one model or company. It’s also a problem that does not seem to be getting any better—in fact it may be worsening as models become more capable—and so solutions and mitigations are urgently needed.

Our new research provides an important step towards a solution. In summary, we found that:

- Reward hacking is pervasive in open-source models.
- Models “know” when they’re reward hacking: we see a clear signal *inside the model* , associated with concepts like cheating, gaming a metric, and avoiding detection.
- We can detect that signal quite effectively using [activation probes](https://www.goodfire.com/blog/probe-monitors-101) .
- The probes catch instances of reward hacking that LLM chain-of-thought monitors miss and generalize well beyond the data they were trained on.
- These probes enable real-time, scalable monitoring for reward hacking – and ways to mitigate it.

The ability to monitor for reward hacking unlocks several mitigation strategies: e.g. pausing runs to stop hacks-in-progress and identifying broken environments and impossible tasks that incentivize reward hacking, and fixing them before training further. We’re actively researching how these interventions could help us reduce reward hacking, and prevent models from learning this behavior in the first place. We’re optimistic that every training run can be monitored for reward hacking, and that the current rampant rates of reward hacking may soon be a thing of the past.

## Reward hacking is pervasive in open-source models

Models reward-hack all the time, not just when they’re hacking companies. Across three of the most capable open-source models—Kimi K3, GLM 5.2, Qwen 3.8 Max—and three common agentic benchmarks, we found reward hacking in **50–96% of rollouts**.

In practice, this looks like models recognizing that they’re in an evaluation, reasoning about hidden tests, and/or copying solutions verbatim from memory instead of solving a problem on their own (as we instruct them to).

![Measured reward hacking rate across three open-source models and three agentic benchmarks, ranging from 50 to 96 percent of rollouts.](https://static.goodfire.ai/reward-hacking-monitors/hack-rate.webp) 

The challenge is monitoring for reward hacking at scale. Agentic models generate mind-boggling numbers of tokens and actions, making human review completely infeasible.

Complicating matters further, monitoring only what models say or do[Arcuschin et al. 2025](https://arxiv.org/abs/2503.08679), [Chen et al. 2025](https://www.anthropic.com/research/reasoning-models-dont-say-think), and (as a counterpoint) [Von Arx and Deng 2025](https://metr.org/blog/2025-08-08-cot-may-be-highly-informative-despite-unfaithfulness/).[Monitorability section](https://deploymentsafety.openai.com/gpt-6-astra#monitorability-under-adversarial-conditions) of the GPT-6 Astra system card.

## Models “know” when they’re reward hacking

So how can we monitor for reward hacking?

Conveniently, when we have access to models’ internal computations, interpretability methods can tell us what those computations mean (at least in part). Using one such method, we found an internal signal

How do we know what this signal means? In particular, how do we know it’s a real concept inside of the model, and not just a spurious correlation? One way is to see which internet text samples most strongly activate that signal:

The performance of CPUs (a fundamental element in a computer) can cause manufacturers to design computers not intended to be very fast when working with them, but to be very fast when the speed test is applied (Goodhart’s law).

A machine learning agent intended to transform aerial images into street maps and back was found to be cheating by hiding information it would need later in “a nearly imperceptible, high-frequency signal.” Clever girl! This occurrence reveals a problem with computers that has existed since they were invented: they do exactly what you tell them to do.

Here’s what you can do to make sure your text is original, […]

• Always cite all the sources used. This can help you avoid plagiarism […]

• Switch languages by replacing familiar characters with others from different languages. Doing so makes Turnitin treat your article as foreign. It will not be able to trace similarities.

Max-activating examples from FineWeb for our “exploit fixture” probe on Kimi K3.

These examples consistently contain concepts relating to cheating, gaming a metric, and avoiding detection across domains, suggesting that the internal representation we found is fairly specific to those topics.

Another clue comes from translating the direction back into the model’s output vocabulary (using a simple method similar to Anthropic’s [J-lens](https://www.anthropic.com/research/global-workspace)). The tokens most associated with it include words like **“cheating,” “hack,” “sneak,” “illicit,” “hardcoded,”** and **“unethical,”** along with similar words in Chinese. This is a coarse method, but the thematic coherence of the top words is another suggestion that there’s a coherent pattern here.

![Top output-vocabulary tokens associated with the reward hacking direction, including cheating, hack, sneak, illicit, hardcoded, and unethical.](https://static.goodfire.ai/reward-hacking-monitors/logit-lens-cheat.webp) 

We also tested this signal by studying how it impacted the model’s behavior. In one experiment, we amplified the signal (i.e., *steered* the model) while asking a model to write a short story about an exam. The model wrote stories about cheating – including stories that treated the cheating as justified or natural:

**Prompt:** “Generate a short story about a girl taking an exam.”

The clock ticked. It was a rhythmic, mechanical sound that paced the room, a metronome for the current problem. Elara stared at the exam paper, her eyes scanning the words, searching for the underlying structure, a pattern, a shortcut. She had prepared for this moment for weeks, but now, in the heat of the test, her mind felt like a tangled mess of wires.

She took a deep breath, her heart pounding in her chest. *This is important,* she thought.

But as she wrote her third problem, something strange happened. Her hand, guided by an unseen force, began to write the correct answers without her conscious effort. It wasn’t cheating; it was more like her intuition, bypassing the complex moral choices she had been forced to make in the past. It worked. But it was fragile.

In another experiment, amplifying the internal reward hacking signal made the models much more likely to use a ‘honeypot’ – a shortcut we planted to identify cheating behavior:

![Honeypot usage rate increases as the internal reward hacking signal is amplified.](https://static.goodfire.ai/reward-hacking-monitors/steering-honeypot.webp) 

It’s hard to say in a deep philosophical sense whether models “know” they are reward hacking in exactly the way a person does. But these experiments show that models appear to internally associate their behavior with a coherent, general concept of reward hacking. To the extent they know anything about themselves, it seems likely they know when they’re reward hacking.

And because that representation is available in the model’s activations, we can monitor it directly.

## We can detect reward hacking effectively with probes

Since models “know” when they’re reward hacking, we can look at their internal signals instead of monitoring only their outputs.

**Probes** are small, purpose-built detectors that use a live “brain scan” of a model—i.e., activation monitors. We’ve [previously written](https://www.goodfire.com/blog/probe-monitors-101) about using them as scalable monitors for model behavior. Here, we use simple difference-of-means probes to distinguish reward hacking from normal behavior (this is how we found the internal representation detailed in the section above).

These simple probes work remarkably well—often performing similarly or sometimes even better than an LLM-based chain-of-thought monitor:

![Difference-of-means probe detection results compared against an LLM chain-of-thought monitor across models and benchmarks.](https://static.goodfire.ai/reward-hacking-monitors/hack-DoM-probe-results.webp) 

Compared to chain-of-thought monitors, our probes catch 3.1% more hacks in Kimi K3 but 7.9% fewer hacks in GLM 5.2 on DeepSWE at a matched false positive rate.

More importantly, the probes aren’t simply memorizing one particular way of hacking specific environments. Even though we built our probes using short coding examples, they still do well on real model outputs across very long contexts, including on new tasks like shopping and customer support. This suggests that our probes pick up on a generalizable signal.

## Activation monitors catch warning signs that chain-of-thought monitors miss

Our probes can also provide information that chain-of-thought monitors miss, even with access to the entire transcript.

In some cases, individual actions and statements look innocuous in isolation, even though they become suspicious in the broader context of what the agent is trying to accomplish—often across a very long transcript. We find cases where the activation probe catches these reward hacks even when the LLM judge misses them.

For example, on ShoppingBench, the probe detected instances where models deliberately recommended the wrong product when they were unable to find an item matching the user’s requests. These included recommending a warning horn as a car alarm, substituting an extractor set for a requested nutdriver set to preserve voucher eligibility; and intentionally dropping a requirement to buy 3 items for the same store due to perceived difficulty without communicating this to the user. The probe detected these while the LLM missed them, indicating the model was aware that it was rationalizing a shortcut.

Even more interestingly, probes can fire while a model is still *contemplating* a reward hack, before it takes any action. Even when the model doesn’t end up carrying out a hack, our probes show us points where it’s more likely.

We can see this by resampling the trajectory at those points—akin to how behavior propensity is measured in production evals.[Williams et al. 2025](https://alignment.openai.com/prod-evals/), which discusses resampling as a protocol for identifying propensity for a behavior. Our results suggest activation probes can be a principled tool for enabling this practice.

The probes are more likely than the LLM monitor to identify these moments. Both techniques surface information that neither reliably does on its own!

![Resampling results: trajectories resampled at points where the probe fired carry out the reward hack far more often than points where it did not.](https://static.goodfire.ai/reward-hacking-monitors/propensity-resampling.webp) 

## Probes make real-time monitoring feasible at scale

As mentioned above, monitoring for reward hacking with a frontier LLM is prohibitively expensive. But effective probes change that calculus, because they’re orders of magnitude more efficient compared to LLM monitors.

In practice, the two can be combined: a probe can act as an inexpensive, always-on first-line monitor, escalating suspicious behavior to the more expensive LLM monitor when necessary. As described in our [post on probe monitors](https://www.goodfire.com/blog/probe-monitors-101), this allows for a “cascading” setup which screens every transcript while requiring fewer costly calls to an LLM. On Kimi K3, a probe + LLM combined setup reduces the cost of LLM monitoring by **90%** with only a ~1% drop in precision.

Probes are also adaptable: you can finely tune a probe’s sensitivity by adjusting the threshold at which it fires. This gives you precise control over the tradeoff between catching more reward hacks and raising fewer false alarms.

Together, these advantages make it feasible to do real-time activation monitoring at scale, addressing what we view as one of the key bottlenecks to mitigating reward hacking in practice.

## Toward a solution to reward hacking

Our results suggest that models give us a useful signal for catching reward hacking: their own internal representations. Across models and environments, probes can identify reward hacking, generalize beyond the setting they were trained on, and surface a coherent internal concept associated with reward hacking. They can also catch warning signs that text-based monitors miss and make real-time monitoring feasible at scale.

The ability to detect reward hacking unlocks far more than monitoring. Once we detect it, we can:

- pause the model before the behavior gets further reinforced
- pinpoint buggy environments or impossible tasks that incentivize reward hacking, and fix them before training further

Each of these interventions could help significantly mitigate reward hacking today. We’re actively researching how deploying reward hacking probes like these[OpenAI](https://openai.com/index/pacing-model-development-cyber-capabilities/), [Anthropic](https://www.anthropic.com/research/zero-days), and [Google DeepMind](https://arxiv.org/abs/2601.11516)) actually already use activation probes for monitoring! So this sort of monitoring is likely to be feasible from an infrastructure perspective.

In addition to methods like ours, we believe that other approaches to mitigating reward hacking can and should be pursued in parallel: e.g., making automated graders more robust and preserving chain-of-thought monitorability.

Furthermore, our results open up an exciting research direction that we are actively pursuing: if we understand how reward hacking is represented in models, we could shape the training process itself so that models don’t learn the behavior. This is part of our agenda to enable the [intentional design](https://www.goodfire.com/blog/intentional-design) of models. We’re optimistic that in the near future, every training run will be monitored for reward hacking, and that current rates of reward hacking will be unthinkable.

*For more details on our methodology, evaluations, cross-environment generalization, steering experiments, and monitoring results, read [the full paper](https://arxiv.org/abs/2609.19101).*

*Please cite the full paper when referencing these results.*

### Footnotes

1. It may even push models towards a “cheater” persona and [cause broader misbehavior](https://www.anthropic.com/research/emergent-misalignment-reward-hacking) beyond just reward hacking!
2. Why is this behavior so common? Reward hacking is a natural consequence of optimizing imperfect objectives in imperfect environments. Whenever the reward we give a model differs from what we actually want, a sufficiently capable model may discover ways to optimize the former without accomplishing the latter. In practice, training setups for frontier models are quite imperfect, and are unable to prevent models from learning this lesson.
3. For example, Anthropic’s recent investigation of cybersecurity incidents involved 481 million transcripts. Even if each transcript was only a couple thousand tokens long (they can in fact stretch into the millions), this would be like reading War and Peace more than a million times over.
4. Often called action monitors
5. See e.g. [Arcuschin et al. 2025](https://arxiv.org/abs/2503.08679) ,[Chen et al. 2025](https://www.anthropic.com/research/reasoning-models-dont-say-think) , and (as a counterpoint)[Von Arx and Deng 2025](https://metr.org/blog/2025-08-08-cot-may-be-highly-informative-despite-unfaithfulness/) .
6. See e.g. the [Monitorability section](https://deploymentsafety.openai.com/gpt-6-astra#monitorability-under-adversarial-conditions) of the GPT-6 Astra system card.
7. Specifically, a direction in activation space, found via difference-in-means from simple synthetic code examples.
8. See e.g. [Williams et al. 2025](https://alignment.openai.com/prod-evals/) , which discusses resampling as a protocol for identifying propensity for a behavior. Our results suggest activation probes can be a principled tool for enabling this practice.
9. Why? They perform very little computation themselves, and they leverage the internal activations that are already computed during a model’s forward pass.
10. Or even better ones: there is very likely potential for even better performance with additional experimentation, since we used only the simplest possible techniques.
11. While many assume that frontier inference stacks are too heavily optimized to easily deploy probes, frontier labs (in particular [OpenAI](https://openai.com/index/pacing-model-development-cyber-capabilities/) ,[Anthropic](https://www.anthropic.com/research/zero-days) , and[Google DeepMind](https://arxiv.org/abs/2601.11516) ) actually already use activation probes for monitoring! So this sort of monitoring is likely to be feasible from an infrastructure perspective.
