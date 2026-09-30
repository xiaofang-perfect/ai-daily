---
title: "State of Agent Skills"
source: TLDR AI · 2026-09-29
url: https://vercel.com/blog/state-of-agent-skills?utm_source=tldrai
date: 2026-09-30
published_at: 2026-09-29T12:00:00+00:00
tag: 工具开源
item_id: 72953d1c780adf08
---
In seven months, the [skills.sh](https://www.skills.sh/) registry grew to one million agent skills and recorded nearly 280 million installs.

![In seven months, skills.sh reached more than one million skills and nearly 280 million installs.](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F7hxPZ4nBE0Mnsn1dkdGofj%2Fdc36258e2b82650482ec34d48c33a628%2Fskills-cumulative-installs-and-catalogue-web-light.png&w=1920&q=95)

![In seven months, skills.sh reached more than one million skills and nearly 280 million installs.](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F4ZL1hZ92nRJjKFxWyEVx4W%2Fc3808e92422a1ddb916564440a7237d0%2Fskills-cumulative-installs-and-catalogue-web-dark.png&w=1920&q=95)

A skill gives an AI agent reusable instructions for a particular job. Agents are capable but generic; they can do many jobs, but they don't know how a specific person, team, or company does them. A skill supplies that missing context and can be as simple as a file written in ordinary language.

Anthropic introduced [Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) in October 2025, and Vercel launched the [skills.sh](http://skills.sh) registry three months later.

Using aggregate data from the registry, this report follows a new market through its first million skills: what people teach agents, what gets installed, and where the value is heading.

## [Copy link to heading](https://vercel.com#skills-turn-expertise-into-software)Skills turn expertise into software

To write a skill, some of the judgment behind a job has to be made explicit, like the steps to follow, what good looks like, and how to evaluate the result. The agent and its tools already supply much of the underlying capability, so the skill only has to provide the judgment and instructions specific to a job.

This makes skills faster and easier to create than conventional software.

skills.sh reached one million skills in seven months. GitHub took 27 months to reach one million repositories. Apple's App Store took just over five years to get to one million apps. npm took more than nine years to reach one million packages.

![skills.sh reached one million skills seven months after launch, compared with 27 months for GitHub repositories, 63 for App Store apps, and 117 for npm packages.](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F2ZVzqIm2zX1BcLdWSUY7vo%2Fe1ac442a733ba6e9f42ba666a6b8ccee%2Fskills-time-to-one-million-web-light.png&w=1920&q=95)

![skills.sh reached one million skills seven months after launch, compared with 27 months for GitHub repositories, 63 for App Store apps, and 117 for npm packages.](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F4C5fWpVEoLOOwsJD5AdQoY%2Fe851bd20111512efec68926e77e63074%2Fskills-time-to-one-million-web-dark.png&w=1920&q=95)

Far more people can describe how work should be done than program a computer to do it. And once a skill is written, it can be distributed and installed without being rewritten for each agent. Skills pair a much larger pool of creators with software’s capacity for reuse, driving the explosive growth of the ecosystem.

## [Copy link to heading](https://vercel.com#what-people-are-teaching-agents)What people are teaching agents

We classified the registry's most-installed skills by the kind of work they help agents do. Together, these skills account for more than four-fifths of all installs. Published listings show supply: what authors have made available to agents. Installs show demand: what people want their agents to learn.

![Software engineering is the largest category by listings, but more than four in five installs go to other kinds of work.](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F712lycy79IeHLvzvmIiV5T%2Fb81ce8d1fd594a8a35566e9eb6e9812e%2Fskills-function-share-web-light.png&w=1920&q=95)

![Software engineering is the largest category by listings, but more than four in five installs go to other kinds of work.](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F7B3u6z5gqFw34DucMUMLIJ%2F129d7f2aab0fbf498a2500fea89d51d3%2Fskills-function-share-web-dark.png&w=1920&q=95)

Supply leans technical. More than half of listings teach software engineering, agent workflows, data, infrastructure, or security, with software engineering alone accounting for about a quarter.

Demand is more distributed. No category draws more than a fifth of installs. Software engineering remains the largest at 18%, followed by agent workflows at 15%, then business operations and writing at nearly 11% each.

To see how each category performs for its size, we also compared its installs per listing with the average.

![The index divides each category’s share of installs by its share of listings. The farther the result is from 1.0×, the wider the gap between the two.](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F4ZfG9I9ddkFwkpjHdOJMhQ%2F26eac9e9714bdf7e8e0e74554ab9a536%2Fskills-function-over-under-web-light.png&w=1920&q=95)

![The index divides each category’s share of installs by its share of listings. The farther the result is from 1.0×, the wider the gap between the two.](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2FEc0RTLEao4nThWkvkcW3b%2F64cfcbf8657e7795d3130afda8ecb434%2Fskills-function-over-under-web-dark.png&w=1920&q=95)

Business operations, writing and documents, and cloud and infrastructure get the most installs per listing. Demand for that work is split across fewer skills, so each one carries more of it. The average business operations skill draws 74% more installs than the average, writing and documents 50% more, cloud and infrastructure 42% more.

Software engineering, education and productivity, and research run the opposite way. The average software engineering skill draws about 30% fewer installs than average, education and productivity 39% fewer, research 55% fewer.

To write a skill, you need to understand a job. To install one, you need only want the job done. Most skills are technical because they began in developer tools. Installs cover a much broader range of work because agents are useful in every part of a company.

## [Copy link to heading](https://vercel.com#skills-that-improve-how-agents-work-are-among-the-most-installed)Skills that improve how agents work are among the most installed

Agent workflows and automation account for 14.8% of installs in the classified dataset, second only to software engineering. Among listings with at least 100,000 installs, agent workflows are the largest category.

![Among skills with at least 100,000 installs, improving how agents work is the most common category.](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F2ToVNKrrrDE6mJBqSu121r%2Fada587dbc7a45daeb84b5cc61880ea75%2Fskills-function-rank-by-install-tier-web-light.png&w=1920&q=95)

![Among skills with at least 100,000 installs, improving how agents work is the most common category.](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F37SiPOnvfswvFkScRBRAKN%2F5cdcc4321c58afc9a81804e7441066ae%2Fskills-function-rank-by-install-tier-web-dark.png&w=1920&q=95)

Agent workflow and automation skills teach agents how to plan, route work, use tools, and automate browsers, abilities that apply across many jobs. A contract-review skill applies to contracts, but a planning skill applies to any job the agent takes on, contracts included.

People are using agents to improve agents. And because agents also help write skills, the catalog grows by improving the very machinery used to build it.

## [Copy link to heading](https://vercel.com#a-few-skills-capture-most-installs)A few skills capture most installs

Install activity is highly concentrated. Nearly half of all skills were installed exactly once. At the other end, 375 skills, or 0.04% of the registry, account for 62% of installs, and the top 1.2% account for 94% of installs.

![The top 375 skills account for 62% of installs; the bottom 98.8% share less than 6%. Measured using a logarithmic scale.](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F6w0Y4IuwoNRSNYUQgf4ofF%2F57a4b36cfacf2f42dfcec936189d6deb%2Fskills-install-concentration-logx-web-light.png&w=1920&q=95)

![The top 375 skills account for 62% of installs; the bottom 98.8% share less than 6%. Measured using a logarithmic scale.](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2FAIO7klHQeQUiUB1lk5aSo%2F26463dda46b14791735e10e4fc9221da%2Fskills-install-concentration-logx-web-dark.png&w=1920&q=95)

For all that concentration, there's no single winner. Even the most-installed skill accounts for less than 1% of all installs.

Skills compete within jobs and accumulate across them. Once a team chooses an expense-report skill, it has little reason to install another expense-report skill. But it can use that skill alongside others for spreadsheets, research, and presentations. Each job crowns its own winner, and the winners together carry most of the installs.

## [Copy link to heading](https://vercel.com#seven-in-eight-installs-go-to-skills-that-work-across-industries)Seven in eight installs go to skills that work across industries

We also classified each skill by whether its work was shared across industries or specific to one. Tasks such as cleaning up a spreadsheet or deploying a website recur at banks and hospitals, law firms and restaurants. These cross-industry skills account for 66% of classified skills and 87.5% of installs. On average, they receive 3.6 times as many installs per listing as industry-specific skills.

![Only one in eight installs is tied to a specific industry.](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F4iUBstLD9XKJ2DCZIwSyAu%2Fe08d6bb537495e55b2e3dba709f2db96%2Fskills-installs-by-industry-web-light.png&w=1920&q=95)

![Only one in eight installs is tied to a specific industry.](https://vercel.com/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2FsdCAqTPkesYwCLyzuK7Mp%2F619bc35a1c9a34b02d699068ae4134aa%2Fskills-installs-by-industry-web-dark.png&w=1920&q=95)

The advantage is portability, whether a skill reaches across jobs, like agent workflows, or across industries. The skills installed most are the ones the most people can use.

## [Copy link to heading](https://vercel.com#the-next-generation-of-skills)The next generation of skills

The first million skills taught agents what everyone knows. The next million will teach your agents what only you know.

Public skills and better models are making general expertise available to every team, which will turn it into the baseline rather than any kind of advantage. More of the differentiating value will move to company-specific judgment. For example, when a customer gets a refund or what can ship without another review.

The measure of a skill will also shift from popularity to effectiveness. Today, the best signal of a skill's quality is its install count. As models improve, the bar rises, because a skill justifies itself only if the agent does the job better with it than without it. Skills will get tests and benchmarks that measure exactly that.

The first generation of skills turned expertise into software. The next generation will see the public catalog continue to grow as supply catches up to demand. And organizations will build on top of it, writing down the knowledge only they have and maintaining it the same way they now maintain code.

Explore the first million, or add to the next, at [skills.sh](http://skills.sh/).

### [Copy link to heading](https://vercel.com#about-this-report)About this report

This report uses aggregate [skills.sh](http://skills.sh/) data. A few notes on measurement:

- Catalog totals count unique registry listings.
- Install figures use aggregate registry counters. They do not represent unique people or necessarily independent choices.
- Function and industry findings describe a classified sample rather than the full catalog.
- Each analysis uses the latest complete data available. Figures may be revised as the underlying data and methodology improve.
