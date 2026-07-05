---
title: "usestrix/strix"
source: GitHub Trending
url: https://github.com/usestrix/strix
date: 2026-07-05
published_at: 2026-07-05T06:03:11.655629+00:00
tag: 工具开源
item_id: 82aeb113e9e4cbb7
---
![Strix Banner](https://github.com/usestrix/.github/raw/main/imgs/cover.png) 

  

### The open-source AI pentesting tool. Autonomous AI hackers that find and fix your app’s vulnerabilities.






![Join Discord](https://github.com/usestrix/.github/raw/main/imgs/Discord.png)

![Follow on X](https://github.com/usestrix/.github/raw/main/imgs/X.png)


Tip

**New!** Strix integrates seamlessly with GitHub Actions and CI/CD pipelines. Automatically scan for vulnerabilities on every pull request and block insecure code before it reaches production - [Get started with no setup required](https://app.strix.ai).

Strix are autonomous AI penetration testing agents that act just like real hackers - they run your code dynamically, find vulnerabilities, and validate them through actual proofs-of-concept. Built for developers and security teams who need fast, accurate security testing without the overhead of manual pentesting or the false positives of static analysis tools.

**Key Capabilities:**

- **Full pentesting toolkit**- reconnaissance, exploitation, and validation out of the box
- **Multi-agent orchestration**- teams of AI pentesters that collaborate and scale
- **Real exploit validation**- working PoCs, not false positives like legacy vulnerability scanners
- **Developer‑first CLI**- actionable findings with remediation guidance
- **Auto‑fix & reporting**- generate patches and compliance-ready pentest reports

![Strix Demo](https://github.com/usestrix/strix/raw/main/.github/screenshot.png) 

  - **Application Security Testing**- Detect and validate critical vulnerabilities in your applications
- **Rapid Penetration Testing**- Get penetration tests done in hours, not weeks, with compliance reports
- **Bug Bounty Automation**- Automate bug bounty research and generate PoCs for faster reporting
- **CI/CD Integration**- Run tests in CI/CD to block vulnerabilities before reaching production

**Prerequisites:**

- Docker (running)
- An LLM API key from any [supported provider](https://docs.strix.ai/llm-providers/overview)(OpenAI, Anthropic, Google, etc.)

```
# Install Strix
curl -sSL https://strix.ai/install | bash
# Configure your AI provider
export STRIX_LLM="openai/gpt-5.4"
export LLM_API_KEY="your-api-key"
# Run your first security assessment
strix --target ./app-directory
```
Note

First run automatically pulls the sandbox Docker image. Results are saved to `strix_runs/<run-name>`

Try the Strix full-stack penetration testing platform at ** app.strix.ai** - sign up for free, connect your repos and domains, and launch a pentest in minutes.

- **Validated findings with PoCs**- every vulnerability includes a working proof-of-concept exploit and reproduction steps
- **One-click autofix**- AI-generated security patches as ready-to-merge pull requests
- **Continuous pentesting**- always-on vulnerability scanning that keeps pace with your deployments
- **DevSecOps integrations**- GitHub, GitLab, Bitbucket, Slack, Jira, Linear, and CI/CD pipelines
- **Continuous learning**- AI that builds on past findings, adapts to your codebase, and reduces false positives over time

Strix agents come equipped with a comprehensive offensive security toolkit - the same tools used by professional penetration testers and ethical hackers:

- **HTTP Interception Proxy**- Full request/response manipulation and analysis with Caido
- **Browser Exploitation**- Automated browser for testing XSS, CSRF, clickjacking, and auth bypass flows
- **Shell & Command Execution**- Interactive terminal for exploit development and post-exploitation
- **Custom Exploit Runtime**- Python sandbox for writing and validating proof-of-concept exploits
- **Reconnaissance & OSINT**- Automated attack surface mapping, subdomain enumeration, and fingerprinting
- **Static & Dynamic Code Analysis**- SAST + DAST capabilities for comprehensive application security testing
- **Vulnerability Knowledge Base**- Structured findings with CVSS scoring and OWASP classification

Strix identifies, validates, and exploits a wide range of security vulnerabilities across the OWASP Top 10 and beyond:

- **Broken Access Control**- IDOR, privilege escalation, auth bypass
- **Injection Attacks**- SQL injection, NoSQL injection, OS command injection, SSTI
- **Server-Side Vulnerabilities**- SSRF, XXE, insecure deserialization, RCE
- **Client-Side Attacks**- XSS (stored/reflected/DOM), prototype pollution, CSRF
- **Business Logic Flaws**- Race conditions, payment manipulation, workflow bypass
- **Authentication & Session**- JWT attacks, session fixation, credential stuffing vectors
- **Infrastructure & Cloud**- Misconfigurations, exposed services, cloud security issues
- **API Security**- Broken authentication, mass assignment, rate limiting bypass

Advanced multi-agent orchestration for comprehensive automated penetration testing:

- **Distributed Pentesting**- Specialized AI agents for recon, exploitation, and post-exploitation
- **Scalable Security Testing**- Parallel execution across multiple targets for fast, comprehensive coverage
- **Dynamic Coordination**- Agents share discoveries, chain vulnerabilities, and collaborate like a red team

```
# Scan a local codebase
strix --target ./app-directory
# Security review of a GitHub repository
strix --target https://github.com/org/repo
# Black-box web application assessment
strix --target https://your-app.com
```
```
# Grey-box authenticated testing
strix --target https://your-app.com --instruction "Perform authenticated testing using credentials: user:pass"
# Multi-target testing (source code + deployed app)
strix -t https://github.com/org/app -t https://your-app.com
# White-box source-aware scan (local repository)
strix --target ./app-directory --scan-mode standard
# Focused testing with custom instructions
strix --target api.your-app.com --instruction "Focus on business logic flaws and IDOR vulnerabilities"
# Provide detailed instructions through file (e.g., rules of engagement, scope, exclusions)
strix --target api.your-app.com --instruction-file ./instruction.md
# Force PR diff-scope against a specific base branch
strix -n --target ./ --scan-mode quick --scope-mode diff --diff-base origin/main
```
Run Strix programmatically without interactive UI using the `-n/--non-interactive` flag - perfect for servers and automated jobs. The CLI prints real-time vulnerability findings and the final report before exiting. Exits with non-zero code when vulnerabilities are found.

`strix -n --target https://your-app.com`Strix can be added to your pipeline to run a security test on pull requests with a lightweight GitHub Actions workflow:

```
name: strix-penetration-test
on:
  pull_request:
jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0
      - name: Install Strix
        run: curl -sSL https://strix.ai/install | bash
      - name: Run Strix
        env:
          STRIX_LLM: ${{ secrets.STRIX_LLM }}
          LLM_API_KEY: ${{ secrets.LLM_API_KEY }}
        run: strix -n -t ./ --scan-mode quick
```
Tip

In CI pull request runs, Strix automatically scopes quick reviews to changed files.
If diff-scope cannot resolve, ensure checkout uses full history (`fetch-depth: 0`) or pass
`--diff-base` explicitly.

```
export STRIX_LLM="openai/gpt-5.4"
export LLM_API_KEY="your-api-key"
# Optional
export LLM_API_BASE="your-api-base-url"  # if using a local model, e.g. Ollama, LMStudio
export PERPLEXITY_API_KEY="your-api-key"  # for search capabilities
export STRIX_REASONING_EFFORT="high"  # control thinking effort (default: high, quick scan: medium)
```
Note

Strix automatically saves your configuration to `~/.strix/cli-config.json`, so you don't have to re-enter it on every run.

**Recommended models for best results:**

- [OpenAI GPT-5.4](https://openai.com/api/)-- `openai/gpt-5.4`
- [Anthropic Claude Sonnet 4.6](https://claude.com/platform/api)-- `anthropic/claude-sonnet-4-6`
- [Google Gemini 3 Pro Preview](https://cloud.google.com/vertex-ai)-- `vertex_ai/gemini-3-pro-preview`

See the [LLM Providers documentation](https://docs.strix.ai/llm-providers/overview) for all supported providers including Vertex AI, Bedrock, Azure, and local models.

Get the same Strix experience with [enterprise-grade](https://strix.ai/demo) controls: SSO (SAML/OIDC), custom compliance-ready penetration testing reports (SOC 2, ISO 27001, PCI DSS), dedicated support & SLA, custom deployment options (VPC/self-hosted), BYOK model support, and tailored AI pentesting agents optimized for your environment. [Learn more](https://strix.ai/demo).

Full documentation is available at ** docs.strix.ai** - including detailed guides for usage, CI/CD integrations, skills, and advanced configuration.

We welcome contributions of code, docs, and new skills - check out our [Contributing Guide](https://docs.strix.ai/contributing) to get started or open a [pull request](https://github.com/usestrix/strix/pulls)/[issue](https://github.com/usestrix/strix/issues).

Have questions? Found a bug? Want to contribute? [Join our Discord!](https://discord.gg/strix-ai)

**Love Strix?** Give us a ⭐ on GitHub!

Strix builds on the incredible work of open-source projects like [LiteLLM](https://github.com/BerriAI/litellm), [Caido](https://github.com/caido/caido), [Nuclei](https://github.com/projectdiscovery/nuclei), [Playwright](https://github.com/microsoft/playwright), and [Textual](https://github.com/Textualize/textual). Huge thanks to their maintainers!

Warning

Only test apps you own or have permission to test. You are responsible for using Strix ethically and legally.
