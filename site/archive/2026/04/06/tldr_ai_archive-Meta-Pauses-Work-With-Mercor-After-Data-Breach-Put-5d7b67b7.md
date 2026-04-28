---
title: "Meta Pauses Work With Mercor After Data Breach Puts AI Industry Secrets at Risk"
source: TLDR AI · 2026-04-06
url: https://www.wired.com/story/meta-pauses-work-with-mercor-after-data-breach-puts-ai-industry-secrets-at-risk/?utm_source=tldrai
date: 2026-04-06
published_at: 2026-04-06T12:00:00+00:00
tag: 行业动态
item_id: 5d7b67b7e445847f
---
Meta has paused all its work with the data contracting firm Mercor while it investigates a major security breach that impacted the startup, two sources confirmed to WIRED. The pause is indefinite, the sources said. Other [major AI labs](https://www.wired.com/tag/artificial-intelligence/) are also reevaluating their work with Mercor as they assess the scope of the incident, according to people familiar with the matter.

Mercor is one of a few firms that [OpenAI](https://www.wired.com/tag/openai), [Anthropic](https://www.wired.com/tag/anthropic/), and other AI labs rely on to generate training data for their models. The company hires massive networks of human contractors to generate bespoke, proprietary datasets for these labs, which are typically kept highly secret as they’re a core ingredient in the recipe to generate valuable AI models that power products like ChatGPT and [Claude Code](https://www.wired.com/story/claude-code-success-anthropic-business-model/). AI labs are sensitive about this data because it can reveal to competitors—including other AI labs in the US and China—key details about the ways they train AI models. It’s unclear at this time whether the data exposed in Mercor’s breach would meaningfully help a competitor.

While OpenAI has not stopped its current projects with Mercor, it is investigating the startup’s security incident to see how its proprietary training data may have been exposed, a spokesperson for the company confirmed to WIRED. The spokesperson says that the incident in no way affects OpenAI user data, however. Anthropic did not immediately respond to WIRED’s request for comment.

Mercor confirmed the attack in an email to staff on March 31. “There was a recent security incident that affected our systems along with thousands of other organizations worldwide,” the company wrote.

A Mercor employee echoed these points in a message to contractors on Thursday, WIRED has learned. Contractors who were staffed on Meta projects cannot log hours until—and if—the project resumes, meaning they could functionally be out of work, a source familiar claims. The company is working to find additional projects for those impacted, according to internal conversations viewed by WIRED.

Mercor contractors were not told exactly why their Meta projects were being paused. In a Slack channel related to the Chordus initiative—a Meta-specific project to teach AI models to use multiple internet sources to verify their responses to user queries—a project lead told staff that Mercor was “currently reassessing the project scope.”

An attacker known as TeamPCP appears to have recently compromised two versions of the AI API tool LiteLLM. The breach exposed companies and services that incorporate LiteLLM and installed the tainted updates. There could be thousands of victims, including other major AI companies, but the breach at Mercor illustrates the sensitivity of the compromised data.

Mercor and its competitors—such as Surge, Handshake, Turing, Labelbox, and Scale AI—have developed a reputation for being incredibly secretive about the services they offer to major AI labs. It’s rare to see the CEOs of these firms speaking publicly about the specific work they offer, and they internally use codenames to describe their projects.

Adding to the confusion around the hack, a group going by the well-known name [Lapsus$](https://www.wired.com/story/lapsus-hacking-group-extortion-nvidia-samsung/) claimed this week that it had breached Mercor. In a Telegram account and on a BreachForums clone, the actor offered to sell an array of alleged Mercor data, including a 200-plus GB database, nearly 1 TB of source code, and 3 TBs of video and other information. But researchers say that many cybercriminal groups now periodically take up the Lapsus$ name and that Mercor’s confirmation of the LiteLLM connection means that the attacker is likely TeamPCP or an actor connected to the group.

TeamPCP appears to have compromised the two LiteLLM updates as part of an even larger supply chain hacking spree in recent months that has been gaining momentum, catapulting TeamPCP to prominence. And while launching data extortion attacks and working with ransomware groups, such as the group known as Vect, TeamPCP has also strayed into political territory, spreading a data wiping worm known as “CanisterWorm” through vulnerable cloud instances with Farsi as their default language or clocks set to Iran’s time zone.

“TeamPCP is definitely financially motivated,” says Allan Liska, an analyst for the security firm Recorded Future who specializes in ransomware. “There might be some geopolitical stuff as well, but it’s hard to determine what’s real and what’s bluster, especially with a group this new.”

Looking at the dark-web posts of the alleged Mercor data, Liska adds, “There is absolutely nothing that connects this to the original Lapsus$.”
