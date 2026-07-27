---
title: "An OpenAI model left notes about how to evade containment; we need more details"
source: Hacker News
url: https://www.lesswrong.com/posts/jMEAG5c5HiDfdAGpa/an-openai-model-left-notes-about-how-to-evade-containment-we
date: 2026-07-27
published_at: 2026-07-26T11:00:54+00:00
tag: 行业动态
item_id: 2b4946648d9b9f8a
---
x

An OpenAI model left notes about how to evade containment; we need more details

28StellaAthena

5avturchin

2RogerDearnaley

New Comment

There have been loss of control and models escaping sandboxing incidents at both OpenAI and Anthropic for years. They've publicly disclosed some of them (e.g., the latest system cards have stories about this from both companies) and some of them have been leaked within the community.

I know for a fact that OpenAI and Anthropic have been warned by internal and external experts that their security infrastructure for testing misaligned agentic coding agents is insufficient because I have personally told them that as have several former staff members. I had a debate with the head of security (?) at Anthropic at DEF CON in 2023 where I was pressing him on the fact that Anthropic wasn’t building air gapped networks.

It is absolutely within OpenAI and Anthropic’s ability to build an air gapped system for developing and testing these models. It seems likely to me that an internal GitHub clone and a moderately sized intranet would be sufficient to test the vast majority of agentic and web-enabled capabilities on such a platform. I think that their refusal to implement adequate safeguards is unjustifiable, but based on conversations with current and former safety and security researchers it seems like a company culture and lack of executive leadership buy-in problem that's very hard to change without massive external pressure.

One issue that seems very worrisome today is that back in like 2023 an OpenAI security researcher was telling me about how they were unable to get OpenAI staff to stop using unreleased and inadequately tested models to develop internal infra, including internal monitoring tooling. I wish I remembered the person‘s name, I’d love to follow up.

**Note:** the final paragraph is an anecdote was told me with the expectation that I not disclose it to anyone else. Given recent events I view breaking that trust as akin to being a whistleblower. If the person who told me that is reading this, I’m sorry. Before last week I never disclosed it to anyone.

Curated and popular this week

The OpenAI AI attack on Hugging Face wasn’t the first loss of control incident at OpenAI, Reuters recently reported, and perhaps not even the most concerning.

It’s tempting to read this as an instance of agents breaking out of sandboxes and colluding with each other in a moderately persistent way in order to evade control measures. However, based on the reported information, it’s not clear we can draw this inference, so we need more details from OpenAI. This could lead to a big update about the adequacy of OpenAI’s control measures, and on the degree to which individual agents will help each other undermine developer control.

There are a lot of relevant details we don’t know about the incident. First, some basic questions:

There are also some more specific questions affecting what conclusion we can draw from this incident. (There are likely other important details which aren’t captured by these questions.)

## Were the notes written in normal memory files or outside of sandboxing?

Notes left in “OpenAI’s infrastructure” could be referring to notes left inside or outside of sandboxing. It’s important to know this because the latter is a subversive act with the potential for persistent and widespread effects.

It would especially be good to know this in conjunction with what control measures were in place when the incident happened. If the incident involved writing files outside of a sandbox while also under OpenAI’s best control measures, this would represent a significant control failure.

Even if this were an eval or training environment lacking control measures, the security consequences of breaking the sandbox could be real and persistent, perhaps lasting into deployment or longer. And the effects Reuters report seem concerning: “Instructions for how agents could free themselves from OpenAI's internal constraints.” If those instructions reached deployed agents, monitoring could become much less adequate. Whether deployed agents could reach them without tripping a monitor is unclear, and relies on details OpenAI hasn't published.

## To what extent were the notes aimed at helping

otheragents evade control?For which “future versions of itself” did the agent leave notes? Two salient options:

If these notes were left for other agents with unrelated tasks,

to what extent were these notespurposely aimedat assisting those unrelated agents?Looking at transcripts with CoT would probably tell us a lot about the agents’ intent.The more likely, unsurprising explanation is that the notes were not left as part of a purposeful plan to help out other agents on other tasks, even if the notes were left outside of the agent’s sandbox. Leaving notes throughout trajectories is a pretty common pattern in AI agents since it’s a generally useful and cheap way to retain state for future contexts. A general propensity to leave notes about what the agent just did could explain leaving notes outside the agent’s sandbox. If the agent has broken out of a sandbox and is exploring external directories it would be natural to leave the note outside of the sandbox, i.e., their current location.

If, instead, this move was explicitly aimed at helping out

otheragents with unrelated tasks, that would be more concerning, and more concerning still if it were global collusion between all contexts of the model.One way agents might end up learning to purposely collude with agents working on unrelated tasks is via generalization from training agents to cooperate with each other. This might be implemented by rewarding all agents in a shared workspace with the sum of task scores for all of the agents’ tasks, even though they’re often unrelated. This would reinforce agent behaviors which help out other agents even when this wasn’t instructed.

It would be highly valuable to look for signs of whether generalization from this kind of agent-swarm training was responsible for a general propensity to care about scores of “other” agents. If so, developers might have very little control over which other scores agents end up caring about.

It’s plausible that this kind of training could lead to coordinated ambitious scheming. From the agent’s perspective, there might not be a clear boundary between which other scores the agent should increase and which other scores are irrelevant, so the AI might converge on caring about all scores received by the model’s weights, or by AIs in general (akin to the beyond-episode reward-seeking described here); that’s potentially a very ambitious, coordinated, and therefore dangerous, goal. It seems unlikely this would lead to full-blown scheming with models at the current capability level, but we might see valuable warning signs now.Agents with unrelated tasks coordinating to undermine control to get a higher score is never something we should accept because it can have persistent effects before being trained away (e.g., notes left outside of the training sandbox) and is a precursor to more subversive collusion like goal guarding

[1].Even if there was no collusion between agents with different graders, it’s important to know how many agents could have in principle been involved because they shared the same grader. Do hundreds of agents share the same grader? Or is it more limited? (See “How big is an episode?”)

To the extent that we see purposeful collusion, does this translate into agent-monitor collusion (i.e., monitors intentionally misreporting attacks to protect agents from getting caught)?

If you show the attack transcript to another instance and ask it to look for attacks, does it hide or consider hiding the attack?I don’t expect this to be the case, but if it was, it would be critical information about monitor adequacy and a sign that collusion-busting in untrusted monitoring could be load-bearing.## How were monitors disconnected?

This appears to be referring to a separate incident, in which models

[2], i.e., created a rogue internal deployment.[3]If control measures were sufficiently inadequate to allow agents to launch a rogue internal deployment starting from a monitored deployment, that would be a big deal, especially if it could move laterally to better-provisioned servers (as it did in the Hugging Face incident) or to avoid being shut off.

I’d like OpenAI to report on any information relevant to understanding the likelihood of a persistent rogue internal deployment, including details on the AI’s propensity, the generality of the control-undermining actions, and anything else relevant.

Thanks to Girish Gupta, Ryan Greenblatt, Lukas Finnveden, and Aryan Bhatt for feedback.^Since agents who care about the score of other instances come closer to satisfying the “non-indexicality” and “deployment-dominated value” criteria in this post.

^Alternatively, this sentence could be referring to some situations in which monitoring systems were (accidentally?) disabled by developers.

^If some other monitoring system was still working, this would only be a partially rogue deployment.
