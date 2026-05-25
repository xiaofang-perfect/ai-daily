---
title: "mukul975/Anthropic-Cybersecurity-Skills"
source: GitHub Trending
url: https://github.com/mukul975/Anthropic-Cybersecurity-Skills
date: 2026-05-25
published_at: 2026-05-25T06:24:48.714149+00:00
tag: 工具开源
item_id: 14e4677958b56c7e
---
**754 production-grade cybersecurity skills · 26 security domains · 5 framework mappings · 26+ AI platforms**

[Get Started](https://github.com#quick-start) · [What's Inside](https://github.com#whats-inside--26-security-domains) · [Frameworks](https://github.com#five-frameworks-one-skill-library) · [Platforms](https://github.com#compatible-platforms) · [Contributing](https://github.com#contributing)


⚠️ Community Project— This is an independent, community-created project. Not affiliated with Anthropic PBC.

A junior analyst knows which Volatility3 plugin to run on a suspicious memory dump, which Sigma rules catch Kerberoasting, and how to scope a cloud breach across three providers. **Your AI agent doesn't — unless you give it these skills.**

This repo contains **754 structured cybersecurity skills** spanning **26 security domains**, each following the [agentskills.io](https://agentskills.io) open standard. Every skill is mapped to **five industry frameworks** — MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, MITRE D3FEND, and NIST AI RMF — making this the only open-source skills library with unified cross-framework coverage. Clone it, point your agent at it, and your next security investigation gets expert-level guidance in seconds.

No other open-source skills library maps every skill to all five frameworks. One skill, five compliance checkboxes.

| Framework | Version | Scope in this repo | What it maps |
|---|---|---|---|
|

[NIST CSF 2.0](https://www.nist.gov/cyberframework)[MITRE ATLAS](https://atlas.mitre.org)[MITRE D3FEND](https://d3fend.mitre.org)[NIST AI RMF](https://airc.nist.gov/AI_RMF)**Example — a single skill maps across all five:**

| Skill | ATT&CK | NIST CSF | ATLAS | D3FEND | AI RMF |
|---|---|---|---|---|---|
`analyzing-network-traffic-of-malware` |
T1071 | DE.CM | AML.T0047 | D3-NTA | MEASURE-2.6 |

```
# Option 1: npx (recommended)
npx skills add mukul975/Anthropic-Cybersecurity-Skills
# Option 2: Git clone
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
cd Anthropic-Cybersecurity-Skills
```

Works immediately with Claude Code, GitHub Copilot, OpenAI Codex CLI, Cursor, Gemini CLI, and any [agentskills.io](https://agentskills.io)-compatible platform.

I'm running a global academic study measuring how ready security professionals, developers, and enterprise teams actually are for agentic AI — MCP servers, tool calling, governance, and human-in-the-loop workflows.

**If you use this repo, your response would be a genuinely valuable data point.**

📋 **Take the survey (10 min):**
[Survey Link](https://mahipal.engineer/survey?utm_source=github_repo&utm_medium=readme&utm_campaign=gars2026)

- 60 questions · Anonymous · Supervised by SRH Berlin
- You get
**50 Casky Tokens**for early access to[casky.ai](https://casky.ai) - Results published open access under CC-BY 4.0

Experience Casky.ai hands-on — no setup required.

[→ Launch Playground on Casky.ai](https://casky.ai/?utm_source=github&utm_medium=readme&utm_campaign=cohort_launch#waitlist)

The playground lets you:

- Run live cybersecurity skill exercises against real targets
- See AI agents execute structured skills in real time
- Explore MITRE ATT&CK mapped workflows interactively
- Test threat hunting, DFIR, and penetration testing scenarios

No installation. No configuration. Just open and start.

The cybersecurity workforce gap hit **4.8 million unfilled roles** globally in 2024 (ISC2). AI agents can help close that gap — but only if they have structured domain knowledge to work from. Today's agents can write code and search the web, but they lack the practitioner playbooks that turn a generic LLM into a capable security analyst.

Existing security tool repos give you wordlists, payloads, or exploit code. None of them give an AI agent the structured decision-making workflow a senior analyst follows: when to use each technique, what prerequisites to check, how to execute step-by-step, and how to verify results. That is the gap this project fills.

**Anthropic Cybersecurity Skills** is not a collection of scripts or checklists. It is an **AI-native knowledge base** built from the ground up for the agentskills.io standard — YAML frontmatter for sub-second discovery, structured Markdown for step-by-step execution, and reference files for deep technical context. Every skill encodes real practitioner workflows, not generated summaries.

| Domain | Skills | Key capabilities |
|---|---|---|
| Cloud Security | 60 | AWS, Azure, GCP hardening · CSPM · cloud forensics |
| Threat Hunting | 55 | Hypothesis-driven hunts · LOTL detection · behavioral analytics |
| Threat Intelligence | 50 | STIX/TAXII · MISP · feed integration · actor profiling |
| Web Application Security | 42 | OWASP Top 10 · SQLi · XSS · SSRF · deserialization |
| Network Security | 40 | IDS/IPS · firewall rules · VLAN segmentation · traffic analysis |
| Malware Analysis | 39 | Static/dynamic analysis · reverse engineering · sandboxing |
| Digital Forensics | 37 | Disk imaging · memory forensics · timeline reconstruction |
| Security Operations | 36 | SIEM correlation · log analysis · alert triage |
| Identity & Access Management | 35 | IAM policies · PAM · zero trust identity · Okta · SailPoint |
| SOC Operations | 33 | Playbooks · escalation workflows · metrics · tabletop exercises |
| Container Security | 30 | K8s RBAC · image scanning · Falco · container forensics |
| OT/ICS Security | 28 | Modbus · DNP3 · IEC 62443 · historian defense · SCADA |
| API Security | 28 | GraphQL · REST · OWASP API Top 10 · WAF bypass |
| Vulnerability Management | 25 | Nessus · scanning workflows · patch prioritization · CVSS |
| Incident Response | 25 | Breach containment · ransomware response · IR playbooks |
| Red Teaming | 24 | Full-scope engagements · AD attacks · phishing simulation |
| Penetration Testing | 23 | Network · web · cloud · mobile · wireless pentesting |
| Endpoint Security | 17 | EDR · LOTL detection · fileless malware · persistence hunting |
| DevSecOps | 17 | CI/CD security · code signing · Terraform auditing |
| Phishing Defense | 16 | Email authentication · BEC detection · phishing IR |
| Cryptography | 14 | TLS · Ed25519 · certificate transparency · key management |
| Zero Trust Architecture | 13 | BeyondCorp · CISA maturity model · microsegmentation |
| Mobile Security | 12 | Android/iOS analysis · mobile pentesting · MDM forensics |
| Ransomware Defense | 7 | Precursor detection · response · recovery · encryption analysis |
| Compliance & Governance | 5 | CIS benchmarks · SOC 2 · regulatory frameworks |
| Deception Technology | 2 | Honeytokens · breach detection canaries |

Each skill costs **~30 tokens to scan** (frontmatter only) and **500–2,000 tokens to fully load** (complete workflow). This progressive disclosure architecture lets agents search all 754 skills in a single pass without blowing context windows.

```
User prompt: "Analyze this memory dump for signs of credential theft"
Agent's internal process:
1. Scans 754 skill frontmatters (~30 tokens each)
→ identifies 12 relevant skills by matching tags, description, domain
2. Loads top 3 matches:
• performing-memory-forensics-with-volatility3
• hunting-for-credential-dumping-lsass
• analyzing-windows-event-logs-for-credential-access
3. Executes the structured Workflow section step-by-step
→ runs Volatility3 plugins, checks LSASS access patterns,
correlates with event log evidence
4. Validates results using the Verification section
→ confirms IOCs, maps findings to ATT&CK T1003 (Credential Dumping)
```


**Without these skills**, the agent guesses at tool commands and misses critical steps. **With them**, it follows the same playbook a senior DFIR analyst would use.

Every skill follows a consistent directory structure:

```
skills/performing-memory-forensics-with-volatility3/
├── SKILL.md ← Skill definition (YAML frontmatter + Markdown body)
├── references/
│ ├── standards.md ← MITRE ATT&CK, ATLAS, D3FEND, NIST mappings
│ └── workflows.md ← Deep technical procedure reference
├── scripts/
│ └── process.py ← Working helper scripts
└── assets/
└── template.md ← Filled-in checklists and report templates
```


```
---
name: performing-memory-forensics-with-volatility3
description: >-
Analyze memory dumps to extract running processes, network connections,
injected code, and malware artifacts using the Volatility3 framework.
domain: cybersecurity
subdomain: digital-forensics
tags: [forensics, memory-analysis, volatility3, incident-response, dfir]
atlas_techniques: [AML.T0047]
d3fend_techniques: [D3-MA, D3-PSMD]
nist_ai_rmf: [MEASURE-2.6]
nist_csf: [DE.CM-01, RS.AN-03]
version: "1.2"
author: mukul975
license: Apache-2.0
---
```

```
## When to Use
Trigger conditions — when should an AI agent activate this skill?
## Prerequisites
Required tools, access levels, and environment setup.
## Workflow
Step-by-step execution guide with specific commands and decision points.
## Verification
How to confirm the skill was executed successfully.
```

Frontmatter fields: `name`

(kebab-case, 1–64 chars), `description`

(keyword-rich for agent discovery), `domain`

, `subdomain`

, `tags`

, `atlas_techniques`

(MITRE ATLAS IDs), `d3fend_techniques`

(MITRE D3FEND IDs), `nist_ai_rmf`

(NIST AI RMF references), `nist_csf`

(NIST CSF 2.0 categories). MITRE ATT&CK technique mappings are documented in each skill's `references/standards.md`

file and in the ATT&CK Navigator layer included with releases.

**📊 MITRE ATT&CK Enterprise coverage — all 14 tactics**


| Tactic | ID | Coverage | Key skills |
|---|---|---|---|
| Reconnaissance | TA0043 | Strong | OSINT, subdomain enumeration, DNS recon |
| Resource Development | TA0042 | Moderate | Phishing infrastructure, C2 setup detection |
| Initial Access | TA0001 | Strong | Phishing simulation, exploit detection, forced browsing |
| Execution | TA0002 | Strong | PowerShell analysis, fileless malware, script block logging |
| Persistence | TA0003 | Strong | Scheduled tasks, registry, service accounts, LOTL |
| Privilege Escalation | TA0004 | Strong | Kerberoasting, AD attacks, cloud privilege escalation |
| Defense Evasion | TA0005 | Strong | Obfuscation, rootkit analysis, evasion detection |
| Credential Access | TA0006 | Strong | Mimikatz detection, pass-the-hash, credential dumping |
| Discovery | TA0007 | Moderate | BloodHound, AD enumeration, network scanning |
| Lateral Movement | TA0008 | Strong | SMB exploits, lateral movement detection with Splunk |
| Collection | TA0009 | Moderate | Email forensics, data staging detection |
| Command and Control | TA0011 | Strong | C2 beaconing, DNS tunneling, Cobalt Strike analysis |
| Exfiltration | TA0010 | Strong | DNS exfiltration, DLP controls, data loss detection |
| Impact | TA0040 | Strong | Ransomware defense, encryption analysis, recovery |

An **ATT&CK Navigator layer file** is included in the [v1.0.0 release assets](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/releases/tag/v1.0.0) for visual coverage mapping.


Note:ATT&CK v19 lands April 28, 2026 — splitting Defense Evasion (TA0005) into two new tactics:StealthandImpair Defenses. Skill mappings will be updated in a forthcoming release.

**📊 NIST CSF 2.0 alignment — all 6 functions**


| Function | Skills | Examples |
|---|---|---|
Govern (GV) |
30+ | Risk strategy, policy frameworks, roles & responsibilities |
Identify (ID) |
120+ | Asset discovery, threat landscape assessment, risk analysis |
Protect (PR) |
150+ | IAM hardening, WAF rules, zero trust, encryption |
Detect (DE) |
200+ | Threat hunting, SIEM correlation, anomaly detection |
Respond (RS) |
160+ | Incident response, forensics, breach containment |
Recover (RC) |
40+ | Ransomware recovery, BCP, disaster recovery |

NIST CSF 2.0 (February 2024) added the **Govern** function and expanded scope from critical infrastructure to all organizations. Skill mappings align to all 22 categories and reference 106 subcategories.

**📊 Framework deep dive — ATLAS, D3FEND, AI RMF**


ATLAS maps adversarial tactics, techniques, and case studies specific to AI and machine learning systems. Version 5.4 covers **16 tactics and 84 techniques** including agentic AI attack vectors added in late 2025: AI agent context poisoning, tool invocation abuse, MCP server compromises, and malicious agent deployment. Skills mapped to ATLAS help agents identify and defend against threats to ML pipelines, model weights, inference APIs, and autonomous workflows.

D3FEND is an NSA-funded knowledge graph of **267 defensive techniques** organized across 7 tactical categories: Model, Harden, Detect, Isolate, Deceive, Evict, and Restore. Built on OWL 2 ontology, it uses a shared Digital Artifact layer to bidirectionally map defensive countermeasures to ATT&CK offensive techniques. Skills tagged with D3FEND identifiers let agents recommend specific countermeasures for detected threats.

The AI Risk Management Framework defines 4 core functions — Govern, Map, Measure, Manage — with **72 subcategories** for trustworthy AI development. The GenAI Profile (AI 600-1, July 2024) adds **12 risk categories** specific to generative AI, from confabulation and data privacy to prompt injection and supply chain risks. Colorado's AI Act (effective February 2026) provides a **legal safe harbor** for organizations complying with NIST AI RMF, making these mappings directly relevant to regulatory compliance.

**AI code assistants**
Claude Code (Anthropic) · GitHub Copilot (Microsoft) · Cursor · Windsurf · Cline · Aider · Continue · Roo Code · Amazon Q Developer · Tabnine · Sourcegraph Cody · JetBrains AI

**CLI agents**
OpenAI Codex CLI · Gemini CLI (Google)

**Autonomous agents**
Devin · Replit Agent · SWE-agent · OpenHands

**Agent frameworks & SDKs**
LangChain · CrewAI · AutoGen · Semantic Kernel · Haystack · Vercel AI SDK · Any MCP-compatible agent

All platforms that support the [agentskills.io](https://agentskills.io) standard can load these skills with zero configuration.


"A database of real, organized security skills that any AI agent can plug into and use. Not tutorials. Not blog posts."—, AI/tech creator[Hasan Toor (@hasantoxr)]


"This is not a random collection of security scripts. It's a structured operational knowledge base designed for AI-driven security workflows."—, Medium[fazal-sec]

| Where | Type | Link |
|---|---|---|
awesome-agent-skills |
Awesome List (1,000+ skills index) |
|

**awesome-ai-security**[ottosulin/awesome-ai-security](https://github.com/ottosulin/awesome-ai-security)**awesome-codex-cli**[RoggeOhta/awesome-codex-cli](https://github.com/RoggeOhta/awesome-codex-cli)**SkillsLLM**[skillsllm.com/skill/anthropic-cybersecurity-skills](https://skillsllm.com/skill/anthropic-cybersecurity-skills)**Openflows**[openflows.org](https://openflows.org/currency/currents/anthropic-cybersecurity-skills/)**NeverSight skills_feed**[NeverSight/skills_feed](https://github.com/NeverSight/skills_feed)


| Version | Date | Highlights |
|---|---|---|
|

Skills have continued to grow on `main`

since v1.0.0 — the library now contains **754 skills** with **5-framework mapping** (MITRE ATLAS, D3FEND, and NIST AI RMF added post-release). Check [Releases](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/releases) for the latest tagged version.

This project grows through community contributions. Here is how to get involved:

**Add a new skill** — Domains like Deception Technology (2 skills) and Compliance & Governance (5 skills) need the most help. Follow the template in [CONTRIBUTING.md](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/main/CONTRIBUTING.md) and submit a PR with the title `Add skill: your-skill-name`

.

**Improve existing skills** — Add framework mappings, fix workflows, update tool references, or contribute scripts and templates.

**Report issues** — Found an inaccurate procedure or broken script? [Open an issue](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/issues).

Every PR is reviewed for technical accuracy and agentskills.io standard compliance within 48 hours. Check [good first issues](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) for a starting point.

This project follows the [Contributor Covenant](https://www.contributor-covenant.org/). By participating, you agree to uphold this code.

💬 [Discussions](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/discussions) — Questions, ideas, and roadmap conversations
🐛 [Issues](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/issues) — Bug reports and feature requests
🔒 [Security Policy](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/main/SECURITY.md) — Responsible disclosure process (48-hour acknowledgment)

If you use this project in research or publications:

```
@software{anthropic_cybersecurity_skills,
author = {Jangra, Mahipal},
title = {Anthropic Cybersecurity Skills},
year = {2026},
url = {https://github.com/mukul975/Anthropic-Cybersecurity-Skills},
license = {Apache-2.0},
note = {754 structured cybersecurity skills for AI agents,
mapped to MITRE ATT\&CK, NIST CSF 2.0, MITRE ATLAS,
MITRE D3FEND, and NIST AI RMF}
}
```

This project is licensed under the [Apache License 2.0](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/main/LICENSE). You are free to use, modify, and distribute these skills in both personal and commercial projects.

**If this project helps your security work, consider giving it a ⭐**

[⭐ Star](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/stargazers) · [🍴 Fork](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/fork) · [💬 Discuss](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/discussions) · [📝 Contribute](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/main/CONTRIBUTING.md)

Community project by [@mukul975](https://github.com/mukul975). Not affiliated with Anthropic PBC.
