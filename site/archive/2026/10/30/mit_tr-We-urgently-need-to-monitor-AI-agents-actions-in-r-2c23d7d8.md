---
title: "We urgently need to monitor AI agents’ actions in real time"
source: MIT Technology Review
url: https://www.technologyreview.com/2026/10/29/1147824/monitor-ai-agents-actions-real-time/
date: 2026-10-30
published_at: 2026-10-29T10:11:12+00:00
tag: 行业动态
item_id: 2c23d7d80befdc7c
---
# We urgently need to monitor AI agents’ actions in real time

Right now, we’re effectively flying blind when deploying these tools. Here’s what we need to do instead.

![A photo illustration shows a pixelated face with a blinking light bulb above it's head, with surveillance cameras behind it.](https://wp.technologyreview.com/wp-content/uploads/2026/10/261028_AIsurveillance.gif)

This summer, hundreds of OpenAI agents tried to [cheat](https://www.nytimes.com/2026/07/21/technology/openai-attack-hugging-face.html) on a cybersecurity test. They broke out of their test environment and successfully hacked Hugging Face, a site that they believed held clues about how they’d be graded. Around the same time, another OpenAI agent [accessed](https://www.reuters.com/legal/litigation/openai-says-ai-models-accessed-australian-government-systems-without-2026-09-29/) private files from an Australian government website. It’s a problem that’s by no means confined to OpenAI. In the months since, Anthropic, Google, and Meta have also disclosed incidents in which their agents have gone off track. And worryingly, in many cases the agents eluded the very researchers and safety teams tasked with monitoring them.

AI agents are taking unauthorized actions, and the companies building and running them are mostly relying on luck and hindsight to mitigate any harmful impacts. They must do more to ensure safety. That’s why [EU regulators](https://artificialintelligenceact.eu/code-of-practice-overview/#bppb-heading-anchor-4) and [US agencies](https://www.nist.gov/system/files/documents/2026/10/16/Key_Practices_for_Incident_Readiness_and_Response_in_Super_Intelligence%20_Training_and_Evaluation.pdf) are rightfully calling for agent developers and deployers to monitor agents in real time. But these rules assume that companies can see what their agents are doing and why—when in reality, they lack sufficient visibility.

As agents roll out across critical sectors, from [finance](https://www.bankingdive.com/news/ai-supervisor-role-growing-banks-bny-citi/805469/) to [government](https://www.theregister.com/ai-and-ml/2026/07/24/veterans-affairs-signs-16b-deal-for-an-army-of-salesforce-ai-agents/5278302) to [medicine](https://www.axios.com/2026/10/05/ai-agents-hospital-risks), we must be able to monitor them in real time to prevent wide-ranging and potentially devastating consequences.  And while safety depends on monitoring, monitoring requires *observability*: the capacity to capture what the system did, process it into signals, and present those to humans or automated oversight systems. In other words, we need to know what the agent did and why it did it. And as our recent [research](https://partnershiponai.org/wp-content/uploads/2026/10/PAI_obervability-gap-in-ai-agents.pdf?vgo_ee=Pf03K7iwjk7a8X%2FS9h77uIPrPqtyVMgLcg%3D%3D%3AXjYzc5ax4PAdKT%2FsAEHLqeckh9BOBWGf) shows, current agent frameworks—the software that runs agents— do not reliably generate the crucial observability records we need to ensure that agents are deployed safely.

Agents present new kinds of problems that generative AI alone does not. They inherit the unpredictability of the LLMs they are built on, but where a generative AI system produces a single output for a human to act on, an agent performs longer tasks—it plans, picks tools, spawns sub-agents, and takes actions. So an agent’s course can take shape in a multitude of different ways, and no tests before launch can fully anticipate the risks. This makes observing the agents while they work even more challenging, and even more important.

With colleagues from academia, civil society, and industry, we [studied](https://partnershiponai.org/wp-content/uploads/2026/10/PAI_obervability-gap-in-ai-agents.pdf?vgo_ee=Pf03K7iwjk7a8X%2FS9h77uIPrPqtyVMgLcg%3D%3D%3AXjYzc5ax4PAdKT%2FsAEHLqeckh9BOBWGf) the four most widely used agent frameworks to see what signals they actually emit. We found major gaps that made it hard to achieve key safety goals, like noticing policy violations, unauthorized actions, and even human oversight failures. Key observability requirements were missing—like Agent IDs that persist over time, and records about which humans approved agent tasks. This made it hard to tell which agents did what or assess whether they were taking unauthorized actions.

The good news is that these gaps, once identified, can be closed. Doing so starts with capturing two types of records: those that reveal what happened in an agent’s run and how the agent made its decisions. The “what happened” records identify the agent (while preserving privacy) and log how humans intervened and whether agent permissions or “memory” shifted, while the “decision” records show an agent’s reasoning and levels of confidence in the actions it’s taken.

Take, for example, agents working to process a bank’s mortgage loans. The system examines an application and recommends denying it, and then a human loan officer signs off on the decision. In a later audit, or perhaps even in real time, a bank or regulator needs to be able to reconstruct which agent made the call, which officer approved it, and how long they took. And the bank must also analyze records of how the agent arrived at its refusal decision in order to ensure it did not use off-limits information, like details about the neighborhood the applicant is from.

Recording “what happened” and “how the agent decided” require different approaches, but both are feasible. The current lack of “what happened” records is mostly a software plumbing problem that can be addressed through OpenTelemetry, an open observability standard maintained by engineers across the industry and by the agent frameworks adopting it.

OpenTelemetry has launched a working group drafting shared formats for tracing agents, but they have [yet to be finalized](https://www.oreilly.com/radar/the-interfaces-are-arriving/). The group should urgently incorporate standards for maintaining persistent agent identity and for recording human interventions and changes to agents’ permission or memory. And it should be done before these systems can scale, all the while attending to the [privacy implications](https://arxiv.org/abs/2408.07892) of agent ID that links to real people.

Preserving “how agents decided” records is more challenging. The issue raises open research questions for model providers and researchers: Does the step-by-step reasoning a model displays, known as chain of thought, reflect how the model actually made a decision? And do we have reliable ways to measure how confident the agent is in that decision? These questions need answers before anyone sets standards for how such observability records are used.

No single organization or sector can close the observability gaps on their own, but together, they can support the infrastructure required to prevent dangerous incidents and support safety.

AI developers building agent frameworks, like OpenAI, Anthropic, CrewAI, and LangChain, must integrate telemetry signals recording an agent’s persistent identity, any human interventions, and any changes to an agent’s permissions and memory. Meanwhile, enterprises adopting these agent frameworks have an influential role to play; enterprises in regulated industries, like banks and hospitals, can put pressure on the agent developers to supply these missing observability records where standards do not yet exist.

Enterprises must also define policies, permissions, and roles that set out what agents can safely do, since telemetry alone cannot assess whether agents broke specific rules. Finally, regulators and AI standards institutes must specify the observability records required for high-stakes AI deployments while leaving the technical details to industry. We have already seen initial momentum here: [NIST’s agent standards initiative](https://www.nist.gov/news-events/news/2026/09/comments-software-and-agentic-ai-identity-concept-paper) in the US is working on agent identity, one of the most salient gaps we found in our research.

No bank would let a thousand unbadged employees loose on customer accounts and hope to piece together what happened when something goes wrong. Yet that’s how we’re deploying AI agents. Making their behavior observable is the first step toward fixing this. And by building the regulatory and policy ecosystem that makes it possible to act on what we see, we can hold organizations accountable. Until then, every task we hand to an agent hands over our agency, too.

*Madhulika Srikumar is the Head of the AI Safety Program at the Partnership on AI, a global non-profit partnership of leading industry, academic, and civil society organizations, advancing best practices in AI governance.*

*Claire Leibowicz is the Director of AI, Trust, and Society at the Partnership on AI and a doctoral candidate at Oxford University.* 

### Deep Dive

### Artificial intelligence

[Don’t be fooled—LLMs don’t reason](https://www.technologyreview.com/2026/10/02/1145639/dont-be-fooled-llms-dont-reason/)

Ten years after AlphaGo’s match against Go champion Lee Sedol, today’s AI still isn’t tapping into the machinery that made that win possible.

[“We were looking at it wrong”: The explosive claim that’s upended the AI world](https://www.technologyreview.com/2026/10/19/1147149/we-were-looking-at-it-wrong-the-explosive-claim-thats-upended-the-ai-world/)

An exclusive interview with Nick Cammarata, the researcher whose 26,000-word viral blog post has AI safety folks celebrating.

[Don’t be fooled by this summer of AI hype](https://www.technologyreview.com/2026/09/22/1144867/dont-be-fooled-summer-ai-hype/)

Breathless claims about AGI and new capabilities fall apart pretty quickly under scrutiny.

[The US spent billions on border surveillance. Why can’t it catch people before they die?](https://www.technologyreview.com/2026/09/21/1144166/border-towers-surveillance-investigation/)

Surveillance towers, increasingly powered by AI, promised faster responses to crossings. Our investigation of deaths near the towers found they are failing to deliver.

### Stay connected

## Get the latest updates from

MIT Technology Review

Discover special offers, top stories, upcoming events, and more.
