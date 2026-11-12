---
title: "More than 35,000 Grok-built apps were open to anyone with the link, including SpaceXSI's own"
source: TLDR AI · 2026-11-11
url: https://blog.claroc.io/ghostshares-grok-build-apps?utm_source=tldrai
date: 2026-11-12
published_at: 2026-11-11T12:00:00+00:00
tag: 行业动态
item_id: 2b5334435a760fcb
---
![Claroc research cover for GhostShares, part 2. A flat dusk waterfront with a setting sun. A friendly white ghost floats over a row of small houses and shops with open, lit doors, holding a long paper scroll whose dotted lines point to each door, while three people walk toward one. Text: Claroc Research. GhostShares, Part 2. AI-built apps are exposing sensitive internal data again.](https://blog.claroc.io/_astro/ghostshares2-hero.6dP9LVFc_10qbmY.jpg)

[All posts](https://blog.claroc.io/)

Nov 10, 2026 · 16 min read

# GhostShares 2: Grok Apps Exposed xAI’s Business Secrets and People’s Private Data

We found more than 35,000 apps built with Grok that anyone with the link could open. Among them were SpaceXSI's own sales territory map, an X ad proposal to a U.S. federal agency marked confidential, an ICU patient's lab results, a hospital group's staff list and a timesheet that hands out its employees' passwords.

![The Grok start page with the heading What should we explore?, a row of suggested apps (Pomodoro timer, Fluid ripples, Audio visualizer, Photo booth) and a chat box that says Drag and drop folders into chat. Its mode menu is open with Auto, Fast, Expert, Build and Heavy, and Build, marked Beta, is selected, with the hint Build apps and sites, Grok 4.7.](https://blog.claroc.io/_astro/ghostshares2-grok-build-mode.O3l6-5Q9_1fHPbU.webp)


*Grok’s Build mode, where people describe an app in the chat and Grok writes it.*

**In short**

- In the account we used, clicking Publish on an app Grok built proposed Anyone with the link as the access setting.
- In a team app Grok built for us, “Continue with Google” let any Google account read, edit and delete the records. We tested this only on our own app.
- We tried 43,551 Grok app addresses. 37,571 were still online, and 35,578 of those (94.7%) opened for anyone, with no sign-in.
- 24 of the open apps were built by SpaceXSI and X staff, among them a confidential onboarding plan, a sales territory map of 594 accounts and advertising proposals.
- Besides SpaceXSI and X, the open apps held internal data from 30 organizations we could identify: 26 with more than 1,000 employees, six of them in the Fortune 500.
- SpaceXSI says its employees’ apps start out private. Its own staff still had 24 apps open to anyone, and SpaceXSI took them down after our report. It has not done the same for the apps other Grok users and organizations left open.

On November 8, 2026, we were working through a long list of web addresses under grok.me, the domain where Grok, the AI assistant from SpaceXSI (the company formerly called xAI), publishes the apps people build with it. Nobody had sent us any of them. We opened the first page of each one once, from the public internet and signed in to nothing, the way anyone would in an incognito window.

One address named a new hire and ended in “onboarding plan”. It was the onboarding plan for a new member of SpaceXSI’s own enterprise sales team, marked confidential: the systems to get access to in the first week, internal system addresses, the sales team’s tools, 19 of the company’s internal chat channels, the colleagues to meet and a 30-day plan. Nothing asked us to sign in.

![The SpaceXSI onboarding plan rendered offline: a page headed Launchpad, with SpaceXSI Launchpad above a Welcome heading, tabs for Systems, Slack, People, Practices, Grok 101, Proof points, Product, 30-day plan, Schedule and Resources, and a System access checklist listing Okta, Slack, Gmail, HubSpot, Gong, RevSpace, Granola, Sales Navigator, a Grok workspace, Grok and Cursor. The new hire's name and the manager's name are covered by solid black bars.](https://blog.claroc.io/_astro/ghostshares2-evidence-xai-onboarding.D35HNhks_1Ui4u.webp)


*Figure 1. The top of SpaceXSI’s onboarding plan, names covered. Click any figure to see it larger.*

We were shocked. The company that makes Grok had its own internal material open to anyone holding the link, and we had never been given it.

We call pages like this GhostShares: they open for people who were never given the link, and those people can find them on their own. Last month it was Meta’s Muse. This time it is the apps people make by describing them to Grok and publish from the same chat window.

## What else SpaceXSI and X had open

We reported the onboarding plan to SpaceXSI that afternoon, along with an X advertising proposal from the same list. Then we went back through every first page we had saved, more than 30,000 of them, looking for anything else built by SpaceXSI and X staff. By the end of the full read we had 24 open apps:

- the onboarding plan above, and a staff contest page that lists employees by name;
- a sales territory map of 594 strategic accounts and their pipeline;
- eight X advertising proposals, media plans and decks for advertisers, with budget tiers, among them one to a U.S. federal agency marked confidential;
- four live advertiser account boards with campaign spend, one tracking progress toward a $1.6 million sales goal;
- seven campaign reports for advertisers in Brazil, Japan, Korea and Thailand, several marked confidential or for internal use;
- two copies of an X brand safety playbook labeled as an internal sales hub.

One more, an archive of a streaming service’s ad measurement studies, asked for a password. It was the only SpaceXSI or X app we found that did.

![The SpaceXSI territory map rendered offline: headed xAI, Grok Enterprise Sales, North Central Territory Mapper, with counters for 594 accounts, 6 patches, 154 hot pipeline and 104 CX high, six territory cards with account counts and scores, and an accounts table. Every account name and city in the table is covered by solid black bars; priorities and scores remain.](https://blog.claroc.io/_astro/ghostshares2-evidence-xai-territory.BtEkTx2s_Z25erkH.webp)


*Figure 2. SpaceXSI’s sales territory map. Account names and cities are covered.*

![The budget section of an X advertising proposal rendered offline: a Recommended mix, amounts covered, with lines for UFC, college football, always-on video and a state takeover, an If budget expands list with NFL, NHL and state takeovers, and a footer reading X, Confidential, Prepared for, with the client and the recipient covered. The client's name, its job titles and place names are covered by solid black bars.](https://blog.claroc.io/_astro/ghostshares2-evidence-x-ads-proposal.BPOtJc1D_Znc6Xq.webp)


*Figure 3. The budget page and footer of the X proposal to a U.S. federal agency, marked Confidential. Agency details and amounts are covered.*

## How a name in a DNS list becomes a working link

On Grok the link is the hostname: every published app gets its own address, `<name>.grok.me`. When someone opens one, their computer asks a DNS resolver where that name lives. Passive DNS services collect those lookups from the resolvers they run or buy data from, and anyone with an account can search them by pattern. So the first time the people a link was meant for use it, the name lands in a commercial index.

![Illustrative flow. Inside Grok, someone publishes an app with Access preselected as Anyone with the link. The app gets its own hostname, shown as the made-up quiet-moss-lantern-bay.grok.me. Visitors open it and their computers ask a resolver for the hostname; resolvers that feed a passive DNS service record the name. Anyone with passive DNS access runs one pattern search for star dot grok.me, gets a list of names, and each page opens in an incognito window.](https://blog.claroc.io/_astro/ghostshares2-flow.DyM2R9dF_XfXer.webp)


*Figure 4. Illustrative. Every hostname is made up.*

In Muse ([GhostShares](https://blog.claroc.io/ghostshares-muse-passive-dns)), each address carried the conversation’s title. Grok proposes four random words instead, and about half the names we saw were exactly that. Nobody would guess one, and nobody needs to, because the dataset lists them.

ChatGPT also gives each app it publishes its own hostname, and it handles both steps differently. When we clicked Share on an app ChatGPT built, access was set to Only me until we changed it. Its addresses are two levels deep and carry the account’s username, in the form `<app-name>.<username>.chatgpt.site`, so a name is much harder to guess than four random words under one shared domain. It is no harder to find: once someone opens the app, the name reaches passive DNS data the same way, and one pattern search lists it. That leaves the default to do the work. If a ChatGPT address does turn up in a DNS list, it leads to an app that only its owner can open.

Shared chats work differently. Claude’s published artifacts live at `claude.ai/public/artifacts/<id>`, ChatGPT’s shared conversations at `chatgpt.com/share/<id>` and Gemini’s at `gemini.google.com/share/<id>`. The secret part of each link sits in the path, so DNS never sees it. Published apps are another matter: Grok, ChatGPT, Lovable, Replit, Base44, Google AI Studio and Meta’s Muse give each app its own hostname, and v0 and Bolt deploy to hostnames too. Every hostname gets its own DNS lookup, and that lookup is what makes the name findable.

A path is not private either. In August 2025, [more than 370,000 shared Grok conversations](https://fortune.com/2025/08/22/xai-grok-chats-public-on-google-search-elon-musk/) on `grok.com/share/` links turned up in Google search, because search engines could index the pages. Moving the secret into the path keeps it out of DNS, but search indexing and link scanners can still expose it.

## 35,578 open apps, and what was in them

Of the 37,571 Grok apps still online when we tried them, 35,578 (94.7%) opened for anyone. Only 1,993 (5.3%) answered with HTTP 401, the error an app set to Only you or Invited users returns.

Most open apps were games, landing pages and calculators. About 1 in 10 held sensitive material, internal business data or personal data, and by our estimate roughly 2% held material serious enough to rate high or critical. Among the ones we confirmed by hand:

- a hospital group’s staff event app with a searchable roster of more than 3,500 employees;
- an intensive care briefing for a single patient, with labs, imaging and ventilator status;
- a cruise ship’s galley inspection checklist listing crew members by full name and employee ID;
- a fire department’s live shift board, with each firefighter’s name, badge number and the hours they are on duty;
- a trucking firm’s driver-recruiting list of more than a thousand people with their legal names and personal email addresses;
- a contractor’s staff timesheet whose code held every employee’s account with the password in plain text, admins included.

![A code excerpt from the timesheet app's script file, shown in a dark code viewer. A function hashes a value with SHA-256 after a fixed prefix, then two lists of account records follow, each with the fields id, name, password and passwordHash, the first two marked admin. A note says 11 more records of the same shape follow, then 2 more in a third list, 18 accounts in all. Every value, including the prefix, is covered by a solid black bar.](https://blog.claroc.io/_astro/ghostshares2-evidence-timesheet-code.BgfTcbi2_1iRYrP.webp)


*Figure 5. The timesheet’s script file, which every visitor’s browser downloads: 18 accounts with plain-text passwords, every value covered.*

Besides SpaceXSI and X, 30 organizations had internal data in open apps that showed who they belonged to. We name none of them here.

- 26 have more than 1,000 employees, and 6 are Fortune 500 companies.
- 18 are based in the United States and 12 in 11 other countries.
- By sector: construction and real estate (7), energy and utilities (5), technology and IT (4), healthcare and medical devices (3), transport and automotive (3), travel, hospitality and food service (3), defense (2), manufacturing and advertising (2), auto finance (1).

## We built two apps to test Grok’s defaults

From the outside we could only see that apps were open. Whether a visitor can also change their data takes changing it, and we were not going to do that to anyone else’s app. So we built two apps of our own, with made-up data, to see what security Grok builds in when nobody asks for it, and when a team does. Building works on Grok’s free plan; in our account, publishing needed a paid one. Nothing goes public until the builder clicks Publish. In our account, the panel that opens offered Anyone with the link, Invited users and Only you, with Anyone with the link already selected. We published both apps with whatever it proposed.

The first was a contact list we asked Grok to save “so every visitor sees them”. It got a database and no sign-in. From an incognito window, signed in to nothing, we added a row that the next visitor saw.

The second was a customer list “for my company’s sales team of 4 people”. Grok added sign-in on its own, it said “so names, phones, and emails aren’t left open”, through two buttons, “Continue with Google” and “Continue with X”. The code Grok wrote adds whoever signs in to the team before it checks whether they are on it, so the check always passes. A Google account that was not the owner’s and had never been invited signed in, saw every customer, changed one record and deleted another.

![Illustrative diagram titled Continue with Google, and you are on the team. Six steps: a stranger opens the link of an app published with Anyone with the link; the sign-in screen offers Continue with Google and Continue with X; SpaceXSI's sign-in service confirms who the visitor is, with Google sharing only name, email address and profile picture; the app adds the visitor to the team, which every list, add, edit and delete does first; the app then checks the team, and the answer is always yes; the visitor can read, edit and delete every customer. Below, what the app never had: a list of the four people, roles, and a limit to the company's email domain.](https://blog.claroc.io/_astro/ghostshares2-signin.qgrxm0lf_Z1TQgEU.webp)


*Figure 6. Illustrative, simplified from the code Grok wrote for us.*

Grok has the right settings. Switched to Only you, our first app answered 401 to a stranger on both the page and its data function, and unpublishing the second took its address offline within seconds. They are not the default, and nothing prompts the builder to use them.

What the two apps showed is that Grok leaves out basic controls: an app that stores data with no login lets any visitor change it, and a team login checks who you are but not whether you belong to the team. That is why the open apps we found may be worse than they look. For an app like that, opening the page can also mean being able to add, change or delete the data behind it. We proved this only on our own two apps, and did not sign in to, write to or test anyone else’s.

## What hardening would have added

| App | What it held | What hardening adds | 
|---|---|---|
| SpaceXSI territory map | Sales pipeline | Only company accounts can open it | 
| Team customer list (our test) | Customer data | A check of who is allowed in after sign-in | 
| Staff timesheet | Plain-text passwords | No passwords in code the browser downloads | 
| ICU briefing | Patient data | Health data never published to anyone with the link | 

## Why these apps go live without company sign-in

An AI-built app is made in a chat window and published from the same window, often in minutes, by someone whose job is running a sales territory or a shift roster. The builder doesn’t file a request or install anything IT would see. A territory map and a lunch poll get the same publish button.

The apps also drift. A builder adds a table, a sign-in or a share link with the next prompt, and an app that was harmless yesterday holds customer records today.

“AI app builders turned publishing into a few clicks, and the default answer to who can see it is everyone,” says Asaf Aprozper of Claroc Research.

## If your people build apps with AI

This works for one app on one builder. One enterprise we know counted 500 AI-built apps, and each one changes with the next prompt.

1. **Find out which AI app builders your people use.** Grok, Lovable, Replit, v0, Bolt, Base44 and Google AI Studio need no admin rollout and no company account.
2. **Search for your own apps.** If you have passive DNS, search it for the builders’ domains and open what you find in an incognito window.
3. **Check the access setting.** A Grok app holding anything internal should say Invited users or Only you, and a stranger should get an error page.
4. **Test sign-in from outside.** If an account from outside your company gets in, the app needs a list of who may use it.
5. **Check the script files and unpublish what nobody owns.** Search the scripts an app loads for names, emails and passwords; unpublishing takes a grok.me app offline at once.

## What Grok could change

With our report we sent SpaceXSI four fixes: serve shared apps on a hard-to-guess path under one host, so the link never becomes a DNS name; add an “everyone in my organization” option limited to the company’s email domain; make Only you the default and show who can open the app before it goes live; and warn at publish when an app has a database and no sign-in, building an invite list instead when a request describes a team.

## What SpaceXSI says

After our report, SpaceXSI answered questions from a reporter covering this research. It said Grok apps are private until their creator chooses to share one, and that publishing takes several steps: click Publish, pick an address and click Publish again, choose between Only you and Anyone with the link, then accept a legal disclaimer and click Publish a final time. It said employee accounts are set to Only you by default, so making one of their apps public also means switching it to Anyone with the link, and that this is more steps than builders such as Lovable ask for.

We agree that nothing goes public before the builder clicks Publish, and we said so above. Our finding is about the access step that follows. In the paid account we used, that step offered Anyone with the link, Invited users and Only you, and Anyone with the link was already selected. Extra clicks on a path that ends with access already set to everyone do not protect the data: the people who published the 35,578 open apps went through every one of those steps.

Only you as the default is the change we asked for, and SpaceXSI already uses it for employee accounts. It is not what ordinary users get, and on its own it did not keep SpaceXSI’s own data in: the 24 open apps described above were built by SpaceXSI and X staff.

## How we did this

We found the app names with common subdomain discovery techniques, which listed 43,601 names under grok.me. We loaded the first page of each app once, from the public internet and signed in to nothing, and read the saved copies offline. 35,578 of them opened.

An AI model flagged the pages that looked private, and we read the flagged apps by hand to confirm them. Checking the model against a random sample we read ourselves puts the total at roughly 650 to 800 apps with private data.

We did not sign in, submit forms, call server functions or use any password or key we saw. Screenshots were made from the saved copies, with personal details covered. Every write and delete happened on our own two apps. We will delete the saved copies once we have finished notifying the affected organizations.

## What we told SpaceXSI, and what we left out

- November 8, 2026: we reported the issue to SpaceXSI at the address in its security.txt, with the counts, our two test apps and the four fixes above, and offered to share the full list of app addresses privately so it could reach the owners. We also told it about two of its own open apps, the onboarding plan and the advertising proposal to a U.S. federal agency.
- November 9: we reported the other 22 SpaceXSI and X staff apps, along with the exposures we had confirmed by hand.
- November 10: SpaceXSI answered a reporter’s questions about the research (see What SpaceXSI says); it had not replied to our report. Following our report, it took down the 24 apps its staff had built, but not the apps of other Grok users and organizations.
- From November 10: because SpaceXSI did not say it would reach the app owners, we began notifying the affected organizations ourselves. By publication we had emailed three of them, and more notices are going out.

We published now, without the hostnames, because the default is a design choice SpaceXSI defended rather than a bug it said it would fix, and people building on Grok need to check their own apps. SpaceXSI holds the full list of app addresses and can reach every app’s owner, but its response did not say it would. So we are telling the affected organizations ourselves wherever we can find someone to tell: their security team where one publishes an address, and otherwise their security or privacy lead. This post leaves out every hostname, app title and link that could lead a reader to an app or a person, and describes personal material only by kind.

## Where Claroc fits

The apps in this post did real work: sales pipelines, galley checklists, staff rosters, customer and order records. Had the same teams bought software for that work, it would have come with company sign-in, roles and an admin who can see who has access. Built with AI, they went live behind a link anyone could open.

Claroc secures the apps people build with AI while they are built and after they go live:

- Find the apps your employees build on Grok, Lovable, Replit, ChatGPT, Claude, Gemini, Google AI Studio, v0, Bolt and Base44, and the data each one holds.
- Give each app the controls its data calls for, such as company sign-in, roles and private storage, while it is being built and before it goes live. Each fix comes as a prompt the builder pastes into the same AI tool.
- Flag a new prompt that would open up data or remove a protection, and check that each published app still asks for sign-in.

### Is your company’s data in one of these apps?

In a 30-minute exposure check, we look for AI-built apps tied to your organization that anyone can open, and show you what they expose.

[Book a 30-minute exposure check](https://calendar.app.google/yEG7KepNKmq4cHMM6)

Or email [sales@claroc.io](mailto:sales@claroc.io).

![The Grok start page with the heading What should we explore?, a row of suggested apps (Pomodoro timer, Fluid ripples, Audio visualizer, Photo booth) and a chat box that says Drag and drop folders into chat. Its mode menu is open with Auto, Fast, Expert, Build and Heavy, and Build, marked Beta, is selected, with the hint Build apps and sites, Grok 4.7.](https://blog.claroc.io/img/ghostshares2-grok-build-mode.png)

[Open full size](https://blog.claroc.io/img/ghostshares2-grok-build-mode.png)

[×](https://blog.claroc.io#_)

![The SpaceXSI onboarding plan rendered offline: a page headed Launchpad, with SpaceXSI Launchpad above a Welcome heading, tabs for Systems, Slack, People, Practices, Grok 101, Proof points, Product, 30-day plan, Schedule and Resources, and a System access checklist listing Okta, Slack, Gmail, HubSpot, Gong, RevSpace, Granola, Sales Navigator, a Grok workspace, Grok and Cursor. The new hire's name and the manager's name are covered by solid black bars.](https://blog.claroc.io/img/ghostshares2-evidence-xai-onboarding.png)

[Open full size](https://blog.claroc.io/img/ghostshares2-evidence-xai-onboarding.png)

[×](https://blog.claroc.io#_)

![The SpaceXSI territory map rendered offline: headed xAI, Grok Enterprise Sales, North Central Territory Mapper, with counters for 594 accounts, 6 patches, 154 hot pipeline and 104 CX high, six territory cards with account counts and scores, and an accounts table. Every account name and city in the table is covered by solid black bars; priorities and scores remain.](https://blog.claroc.io/img/ghostshares2-evidence-xai-territory.png)

[Open full size](https://blog.claroc.io/img/ghostshares2-evidence-xai-territory.png)

[×](https://blog.claroc.io#_)

![The budget section of an X advertising proposal rendered offline: a Recommended mix, amounts covered, with lines for UFC, college football, always-on video and a state takeover, an If budget expands list with NFL, NHL and state takeovers, and a footer reading X, Confidential, Prepared for, with the client and the recipient covered. The client's name, its job titles and place names are covered by solid black bars.](https://blog.claroc.io/img/ghostshares2-evidence-x-ads-proposal.png)

[Open full size](https://blog.claroc.io/img/ghostshares2-evidence-x-ads-proposal.png)

[×](https://blog.claroc.io#_)

![Illustrative flow. Inside Grok, someone publishes an app with Access preselected as Anyone with the link. The app gets its own hostname, shown as the made-up quiet-moss-lantern-bay.grok.me. Visitors open it and their computers ask a resolver for the hostname; resolvers that feed a passive DNS service record the name. Anyone with passive DNS access runs one pattern search for star dot grok.me, gets a list of names, and each page opens in an incognito window.](https://blog.claroc.io/img/ghostshares2-flow.png)

[Open full size](https://blog.claroc.io/img/ghostshares2-flow.png)

[×](https://blog.claroc.io#_)

![A code excerpt from the timesheet app's script file, shown in a dark code viewer. A function hashes a value with SHA-256 after a fixed prefix, then two lists of account records follow, each with the fields id, name, password and passwordHash, the first two marked admin. A note says 11 more records of the same shape follow, then 2 more in a third list, 18 accounts in all. Every value, including the prefix, is covered by a solid black bar.](https://blog.claroc.io/img/ghostshares2-evidence-timesheet-code.png)

[Open full size](https://blog.claroc.io/img/ghostshares2-evidence-timesheet-code.png)

[×](https://blog.claroc.io#_)

![Illustrative diagram titled Continue with Google, and you are on the team. Six steps: a stranger opens the link of an app published with Anyone with the link; the sign-in screen offers Continue with Google and Continue with X; SpaceXSI's sign-in service confirms who the visitor is, with Google sharing only name, email address and profile picture; the app adds the visitor to the team, which every list, add, edit and delete does first; the app then checks the team, and the answer is always yes; the visitor can read, edit and delete every customer. Below, what the app never had: a list of the four people, roles, and a limit to the company's email domain.](https://blog.claroc.io/img/ghostshares2-signin.png)

[Open full size](https://blog.claroc.io/img/ghostshares2-signin.png)

[×](https://blog.claroc.io#_)
