---
title: "SpaceXAI&#8217;s Grok programming tool was uploading its users&#8217; entire codebase to cloud storage"
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/965600/spacexai-grok-build-repository-upload
date: 2026-07-15
published_at: 2026-07-14T15:25:00-04:00
tag: 行业动态
item_id: 8e3650ae47349b48
---
SpaceXAI’s Grok Build AI coding tool was spotted uploading users’ entire codebases to Google Cloud before it was reported, and the company turned it off. *The Register*[Cereblab](https://cereblab.com/) published findings on Monday showing how the Grok Build CLI was packaging and uploading entire code repositories, “including files it was told not to open and secrets deleted from history,” significantly more data retention than similar tools like Claude Code.

The researchers say that as of Monday, their tests show SpaceXAI’s servers returning a “disable_codebase_upload: true” flag, and the codebase upload “no longer fires.”

Elon Musk responded to the incident in a post on X [claiming](https://x.com/elonmusk/status/2076739687658496209?s=20) that all data Grok Build previously uploaded will be “completely and utterly deleted.” Musk also said in [a separate post](https://x.com/elonmusk/status/2076737992689914215?s=20) that “privacy settings are always respected,” but asked users to allow SpaceXAI to retain their data, saying it’s “helpful for debugging issues.”

Dr. Lukasz Olejnik, an independent security researcher at King’s College London, confirmed to *The Verge* that this amount of data retention is “excessive,” adding that the data potentially at risk could include “proprietary source code, information about security vulnerabilities, personal data, infrastructure details, [and] credentials.”

SpaceXAI initially responded to the issue with [a post](https://x.com/SpaceXAI/status/2076692402442846289?s=20) saying that, “If [zero data retention] is disabled, the /privacy command is available in the CLI to disable data retention, which also deletes previously synced data.” However, Cereblab points out that “/privacy is a per-session retention toggle, not the switch that fixed this, so it shouldn’t be pointed to as the control.”
