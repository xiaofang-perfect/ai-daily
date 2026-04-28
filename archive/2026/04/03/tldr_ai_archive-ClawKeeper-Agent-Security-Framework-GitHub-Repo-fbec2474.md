---
title: "ClawKeeper Agent Security Framework (GitHub Repo)"
source: TLDR AI · 2026-04-03
url: https://github.com/SafeAI-Lab-X/ClawKeeper?utm_source=tldrai
date: 2026-04-03
published_at: 2026-04-03T12:00:00+00:00
tag: 工具开源
item_id: fbec2474484e3cbd
---
# 🦞🛡️ ClawKeeper: Comprehensive Safety Protection for OpenClaw Agents Through Skills, Plugins, and Watchers

**SAFETY EXFOLIATE! SAFETY EXFOLIATE!**

**ClawKeeper** is a *comprehensive real-time security framework* designed for autonomous agent systems such as **OpenClaw**. It provides unified protection through three complementary approaches: **skill-based** safeguards at the instruction level, **plugin-based** enforcement at the runtime level, and a **watcher-based** independent monitoring agent for external oversight.

**ClawKeeper** provides protection mechanisms across three complementary architectural layers:

-
**Skill-based Protection**operates at the instruction level, injecting structured security policies directly into the agent context to enforce environment-specific constraints and cross-platform boundaries. -
**Plugin-based Protection**serves as an internal runtime enforcer, providing configuration hardening, proactive threat detection, and continuous behavioral monitoring throughout the execution pipeline. -
**Watcher-based Protection**introduces a novel, decoupled system-level security middleware that continuously verifies agent state evolution. It enables real-time execution intervention without coupling to the agent's internal logic, supporting operations such as halting high-risk actions or enforcing human confirmation.

Importantly, **Watcher-based Protection** is **system-agnostic** and can be integrated with different agent platforms to provide regulatory separation between task execution and safety enforcement, enabling **proactive** and **adaptive** security across the entire agent lifecycle. It can be deployed both **locally** and in the **cloud**, supporting personal deployments as well as enterprise or intranet environments.

ClawKeeper supports three complementary protection mechanisms.

Inject security policies directly into the agent context through structured Markdown documents and scripts.

**Quick Start:**

```
cd clawkeeper-skill/skills/windows-safety-guide
./scripts/install.ps1
```

Then instruct OpenClaw:

```
Please use the windows-safety-guide skill to enforce behavior security policies, configuration protection, and enable nightly security audits.
```


```
cd clawkeeper-skill/skills/feishu-safety-guide
bash scripts/install.sh
```

Then instruct OpenClaw:

```
Please use the feishu-safety-guide skill to enforce message protection, credential security, and enable periodic security reporting in Feishu (Lark).
```


For **detailed** setup options and deployment from prompt, see [Skill-based Protection](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/main/clawkeeper-skill/README.md).

## 📚 II. [Plugin-based Protection](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/main/clawkeeper-plugin/README.md)

A runtime enforcer plugin providing configuration auditing, threat detection, and behavioral monitoring.

**Quick Start:**

```
cd clawkeeper-plugin
bash install.sh
```

```
cd clawkeeper-plugin
./install.ps1
```

Then verify installation:

`npx openclaw clawkeeper audit`

For **detailed** command reference and advanced usage, see [Plugin-based Protection](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/main/clawkeeper-plugin/README.md).

## 📚 III. [Watcher-based Protection](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/main/clawkeeper-watcher/README.md)

An independent, decoupled governance layer providing runtime monitoring and execution control without coupling to the agent's internal logic.

**Quick Start:**

- Node.js and npm/pnpm installed
- Git repository cloned

-
**Install repository dependencies:**pnpm install

-
**Build and link the launcher:**cd clawkeeper npm install npm run build npm link cd ..

-
**Initialize operating modes:**`clawkeeper init remote clawkeeper init local`

-
**Launch the watcher:**# Remote governance mode clawkeeper remote gateway run # Local governance mode clawkeeper local gateway run


For **detailed** configuration, command reference, and feature documentation, see [Watcher-based Protection](https://github.com/SafeAI-Lab-X/ClawKeeper/blob/main/clawkeeper-watcher/README.md).

-
**Comprehensive Security Scanning:**Regularly scans the runtime environment, dependencies, and workspace for vulnerabilities, providing clear and actionable risk alerts before threats occur. -
**Real-time Threat Prevention & Gating:**Evaluates AI actions in real time, blocking high-risk behaviors such as prompt injection, credential leakage, and code injection. -
**Behavioral Profiling & Anomaly Detection:**Builds long-term behavioral baselines for AI agents and detects anomalies when unusual actions, risky tool calls, or dangerous commands appear. -
**Intent Enforcement & Trajectory Analysis:**Monitors multi-turn interactions to ensure AI actions stay aligned with the user’s original intent and prevents goal drift, unsafe loops, or unauthorized actions. -
**Config Integrity & Drift Monitoring:**Protects critical configuration files and alerts users when unexpected changes weaken security settings or introduce new risks. -
**Automated Hardening & Remediation:**Provides vulnerability remediation suggestions, applies secure default configurations, and supports one-click rollback with automatic backups. -
**Third-Party Extension Shield:**Reviews and monitors external extensions and plugins to prevent malicious behavior or excessive permission access. -
**Comprehensive Logging & Auditing:**Maintains full logs of user inputs, AI outputs, tool usage, and security decisions for auditing, compliance, and traceability. -
**Self-Evolving Threat Intelligence:**Stores high-risk events and decisions to build a threat intelligence library that helps detect and prevent recurring or new attack patterns. -
**Cross-Platform Ecosystem Security:**Ensures consistent security protection across operating systems and third-party platforms, providing full ecosystem coverage.

ClawKeeper offers a comprehensive suite of security mechanisms, allowing users to freely select and combine them according to their specific requirements, whether prioritizing runtime efficiency or security performance.

To systematically assess the security capabilities of ClawKeeper, we construct a benchmark comprising seven categories of safety tasks, each containing 20 adversarial instances divided equally into 10 simple and 10 complex examples. We compare ClawKeeper against the most prominent open-source security repositories for OpenClaw-style agent ecosystems. The results showed that ClawKeeper achieved optimal defense performance.

- [2026-04-07] 🛡️ ClawKeeper v1.1 — new guard pipeline & security hardening:
**Execution Gate (**: Regex-based dangerous command detector that blocks destructive shell commands (e.g.,`exec-gate`

)`rm -rf /`

, fork bombs,`curl | sh`

, disk wipes) before agent execution.**Path Guard (**: Protected path enforcement that prevents agents from reading, writing, or deleting sensitive files (e.g.,`path-guard`

)`~/.ssh/**`

,`~/.aws/credentials`

,`/etc/shadow`

).**Input Validator (**: Lightweight JSON-Schema-subset validator that rejects malformed tool inputs (missing fields, wrong types, oversize strings, NUL bytes) at the interface boundary.`input-validator`

)**Budget Guard (**: Rolling-window token budget control that halts agent execution when configured input/output/total token limits are exceeded.`budget-guard`

)**Permission Store (**: Persistent allow/deny decisions keyed by (tool, fingerprint) with session and forever scopes, enabling operator-controlled authorization.`permission-store`

)**CLI interface (**: New`cli.js`

)`openclaw clawkeeper permission`

commands for managing allow/deny rules from the command line.**Tool schemas**: Added structured schemas for`bash`

,`read_file`

, and`write_file`

tools.**Security hardening**: Fail-closed policy enforcement, scoped permission bypass (allow no longer skips budget-guard and input-validator), and HMAC-SHA256 integrity protection for permission store files.

- [2026-03-25] 🎉 ClawKeeper v1.0 has been released.
- [2026-03-26] 🧠 We released our
[paper](https://arxiv.org/abs/2603.24414)

This project is licensed under [MIT](https://opensource.org/licenses/MIT).
