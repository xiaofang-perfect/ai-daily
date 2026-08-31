---
title: "Claude Session URL appended to commit messages and PR descriptions by default"
source: Hacker News
url: https://github.com/anthropics/claude-code/issues/66504
date: 2026-08-31
published_at: 2026-08-30T12:50:54+00:00
tag: 工具开源
item_id: 927a11e8973b1029
---
### Preflight Checklist

### Problem Statement

Every commit message and PR description created by Claude Code automatically includes a session URL at the bottom (e.g. [https://claude.ai/code/session](https://claude.ai/code/session)_...). There is no opt-in prompt, no warning, and no mention of it during onboarding. Users only discover it after it's already polluting their git history.

### Proposed Solution

Make the session URL attribution opt-in — don't include it unless the user explicitly enables it. A one-time prompt during onboarding ("Would you like to include a link back to this Claude session in commit messages?") would be the ideal UX.

### Alternative Solutions

- 
Keep it opt-out but make the setting discoverable — show it during first commit with a "Don't add this again" option
- 
Remove it entirely and rely only on the existing Co-Authored-By: Claude trailer for attribution

### Priority

Medium - Would be very helpful

### Feature Category

Other

### Use Case Example

A developer uses Claude Code to build a feature, commits the work, and opens a PR.

Their teammates and open source contributors see [https://claude.ai/code/session](https://claude.ai/code/session)_... at the bottom of every commit and PR description.

It looks unprofessional, clutters history, and the developer had no idea it was being added.

### Additional Context

- The attribution.commit: "" setting in .claude/settings.json can suppress it, but it's completely undiscovered
- A commit-msg git hook can also strip it, but it doesn't always fire reliably in remote/cloud environments
