---
title: "Tencent/AI-Infra-Guard"
source: GitHub Trending
url: https://github.com/Tencent/AI-Infra-Guard
date: 2026-08-23
published_at: 2026-08-23T02:57:34.292856+00:00
tag: 工具开源
item_id: a80442f26e8a8e0f
---
[📖 Documentation](https://tencent.github.io/AI-Infra-Guard/)  | 
  🌐 [🇨🇳 中文](https://github.com/Tencent/AI-Infra-Guard/blob/main/readme/README_ZH.md) · [🇯🇵 日本語](https://github.com/Tencent/AI-Infra-Guard/blob/main/readme/README_JA.md) · [🇪🇸 Español](https://github.com/Tencent/AI-Infra-Guard/blob/main/readme/README_ES.md) · [🇩🇪 Deutsch](https://github.com/Tencent/AI-Infra-Guard/blob/main/readme/README_DE.md) · [🇫🇷 Français](https://github.com/Tencent/AI-Infra-Guard/blob/main/readme/README_FR.md) · [🇰🇷 한국어](https://github.com/Tencent/AI-Infra-Guard/blob/main/readme/README_KR.md) · [🇧🇷 Português](https://github.com/Tencent/AI-Infra-Guard/blob/main/readme/README_PT.md) · [🇷🇺 Русский](https://github.com/Tencent/AI-Infra-Guard/blob/main/readme/README_RU.md)

    
    
    
    

    
    

    
    

    

    


    
    
    
    

    

    


    
    


   
   
  

![Tencent%2FAI-Infra-Guard | blackhat](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/blackhat.png) 

![Tencent%2FAI-Infra-Guard | awesome-deepseek-integration](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/awesome-deepseek.png)



**A.I.G (AI-Infra-Guard)** integrates capabilities such as ClawScan(OpenClaw Security Scan), Agent Scan，AI infra vulnerability scan, MCP Server & Agent Skills scan, and Jailbreak Evaluation, aiming to provide users with the most comprehensive, intelligent, and user-friendly solution for AI security risk self-examination.

We are committed to making A.I.G(AI-Infra-Guard) the industry-leading AI red teaming platform. More stars help this project reach a wider audience, attracting more developers to contribute, which accelerates iteration and improvement. Your star is crucial to us!

  
  


Help us improve A.I.G! Please take 3-5 minutes to fill out our [User Feedback Survey](https://doc.weixin.qq.com/forms/AJEAIQdfAAoAFkA0QbdAFwCNcKSO0BFLf). Users who provide high-quality feedback and leave a valid email address will receive an exclusive Tencent souvenir gift.

- **2026-08-17** ·[v4.5.2](https://github.com/Tencent/AI-Infra-Guard/releases/tag/v4.5.2) — Skill-Scan: .pyc bytecode bypass detection + charset smuggling defense; MCP-Scan: RCE prevention via tool whitelisting in dynamic mode; new SkillJack research project; vuln library expanded to 2000+ CVE rules.
- **2026-07-30** ·[v4.5.1](https://github.com/Tencent/AI-Infra-Guard/releases/tag/v4.5.1) — Jailbreak Evaluation: 4 multi-turn jailbreak attacks (Many-Shot, PAIR, GOAT, ActorAttack); Agent-Scan: 5 new OWASP skills + web-exfiltration detection (10 skills total); MCP-Scan: 4 new security rules
- **2026-07-27** ·[v4.5.0](https://github.com/Tencent/AI-Infra-Guard/releases/tag/v4.5.0) — AI Security Skill Market launched (3 official skills); frontend fully open-sourced; Skill scan engine upgraded (9 risk categories, SkillTrustBench top score 0.9848); Skill/MCP/Agent scan as standalone CLI; vuln library expanded to 130 components, 1888 rules
- **2026-06-25** ·[v4.1.15](https://github.com/Tencent/AI-Infra-Guard/releases/tag/v4.1.15) — MCP Scan: 3 new threat detection rules (tool poisoning, credential exfiltration, command injection); 6 new llama.cpp CVE rules;`model.token` now optional with system default fallback.
- **2026-06-18** ·[v4.1.14](https://github.com/Tencent/AI-Infra-Guard/releases/tag/v4.1.14) — Prompt Security: 9 new single-turn jailbreak operators; new`aig-agent-redteam` skill for comprehensive Agent red-team assessment.

👉 [Earlier releases](https://github.com/Tencent/AI-Infra-Guard/blob/main/CHANGELOG.md) · 🛒 [AI Security Skill Market](https://matrix.tencent.com/skill-market/) · 🔍 [skill-scan CLI](https://github.com/Tencent/AI-Infra-Guard/tree/main/skill-scan) · 🔍 [mcp-scan CLI](https://github.com/Tencent/AI-Infra-Guard/tree/main/mcp-scan) · 🔍 [agent-scan CLI](https://github.com/Tencent/AI-Infra-Guard/tree/main/agent-scan) · 📊 [SkillTrustBench](https://matrix.tencent.com/skilltrustbench/)

| Docker | RAM | Disk Space | 
|---|---|---|
| 20.10 or higher | 4GB+ | 10GB+ | 

```
# This method pulls pre-built images from Docker Hub for a faster start
git clone https://github.com/Tencent/AI-Infra-Guard.git
cd AI-Infra-Guard
# For Docker Compose V2+, replace 'docker-compose' with 'docker compose'
docker-compose -f docker-compose.images.yml up -d
```
Once the service is running, you can access the A.I.G web interface at:
`http://localhost:8088`

You can also call A.I.G directly from OpenClaw chat via the `aig-scanner` skill.

`clawhub install aig-scanner`
Then configure `AIG_BASE_URL` to point to your running A.I.G service.

For more details, see the [`aig-scanner` README](https://github.com/Tencent/AI-Infra-Guard/blob/main/skills/aig-scanner/README.md).

## **More installation options**

**Method 2: One-Click Install Script （Recommended）**

```
# This method will automatically install Docker and launch A.I.G with one command
curl https://raw.githubusercontent.com/Tencent/AI-Infra-Guard/refs/heads/main/docker.sh | bash
```
**Method 3: Build and run from source**

```
git clone https://github.com/Tencent/AI-Infra-Guard.git
cd AI-Infra-Guard
# This method builds a Docker image from local source code and starts the service
# (For Docker Compose V2+, replace 'docker-compose' with 'docker compose')
docker-compose up -d
```
Note: The AI-Infra-Guard project is positioned as an AI red teaming platform for internal use by enterprises or individuals. It currently lacks an authentication mechanism and should not be deployed on public networks.

For more information, see: [https://tencent.github.io/AI-Infra-Guard/?menu=getting-started](https://tencent.github.io/AI-Infra-Guard/?menu=getting-started)

Agent Skill security audit tool, easily integrated into enterprise CI/CD pipelines. Vulnerability classification aligns with [SkillTrustBench](https://matrix.tencent.com/skilltrustbench/) T01–T09 taxonomy. [Learn more →](https://github.com/Tencent/AI-Infra-Guard/tree/main/skill-scan)

```
pip install aig-skill-scan
# Set API key via environment variable
export LLM_API_KEY="your-api-key"
# Scan a local Skill project directory
aig-skill-scan --repo /path/to/your/skill \
           -m deepseek-v4-flash \
           --language en \
           -o result.json
```
The checker frontend is deployed separately. Docker deployment keeps the
checker APIs available at `GET /api/v1/relay/models` and
`POST /api/v1/relay/check/stream`; API documentation is available at
`http://127.0.0.1:8088/api-checker/docs`. To run the checker and unified CLI
from source:

```
python3 -m venv services/api_checker/.venv
services/api_checker/.venv/bin/pip install -r services/api_checker/requirements.txt
go build -o ai-infra-guard ./cmd/cli/main.go
export AIG_API_CHECKER_PYTHON="$PWD/services/api_checker/.venv/bin/python"
./ai-infra-guard api-checker list
./ai-infra-guard api-checker audit
```
See the [API Checker integration guide](https://github.com/Tencent/AI-Infra-Guard/blob/main/docs/api-checker-integration.md) for
the Agent-embedded runtime architecture, HTTP API, configuration, and security boundaries.

Experience the Pro version with advanced features and improved performance. The Pro version requires an [invitation code](https://wj.qq.com/s2/25099467/25vn/) and is prioritized for contributors who have submitted issues, pull requests, or discussions, or actively help grow the community. Visit: [https://aigsec.ai/](https://aigsec.ai/).


Performance on [SkillTrustBench](https://matrix.tencent.com/skilltrustbench/) with different LLMs:

| # | Model | F1 | Precision | Recall | FPR | 
|---|---|---|---|---|---|
| 1 | Claude Opus 4.6 | **0.9848** | 0.9725 | **0.9974** | 0.0663 | 
| 2 | GLM 5.1 | 0.9836 | 0.9701 | **0.9974** | 0.0723 | 
| 3 | Gemini 3.5 Flash | 0.9792 | **0.9947** | 0.9641 | **0.0120** | 
| 4 | Kimi 2.6 | 0.9780 | 0.9895 | 0.9667 | 0.0241 | 
| 5 | DeepSeek v4 Flash | 0.9740 | 0.9868 | 0.9615 | 0.0301 | 

Covers 9 categories of Skill security risks (SkillTrustBench T01–T09):

| Layer | Risks | 
|---|---|
| A · Instruction & Memory | T01 Skill Instruction Hijacking, T02 Memory Poisoning | 
| B · Code Execution | T03 Remote Payload Download & Execution, T04 Embedded Malicious Code | 
| C · System Privilege | T05 Privilege Escalation & Unauthorized Access, T06 System Persistence | 
| D · Toolchain & Dependencies | T07 Tool Hijacking & Spoofing, T08 Insecure Dependencies | 
| E · Skill Code Quality | T09 Insecure Coding Practices | 

For full leaderboard and details, visit [SkillTrustBench](https://matrix.tencent.com/skilltrustbench/).

| Feature | More Info | 
|---|---|
| **[ClawScan(OpenClaw Security Scan)](https://matrix.tencent.com/clawscan)** | Supports one-click evaluation of OpenClaw security risks. It detects insecure configurations, Skill risks, CVE vulnerabilities, and privacy leakage. | 
| **Agent Scan** | This is an independent, multi-agent automated scanning framework. It is designed to evaluate the security of AI agent workflows. It seamlessly supports agents running across various platforms, including Dify and Coze. | 
| **MCP Server & Agent Skills scan** | It thoroughly detects 14 major categories of security risks. The detection applies to both MCP Servers and Agent Skills. It flexibly supports scanning from both source code and remote URLs. | 
| **AI infra vulnerability scan** | This scanner precisely identifies over 100 AI framework components. It covers more than 2000 known CVE vulnerabilities. Supported frameworks include Ollama, ComfyUI, vLLM, n8n, Triton Inference Server and more. | 
| **Jailbreak Evaluation** | It assesses prompt security risks using carefully curated datasets. The evaluation applies multiple attack methods to test robustness. It also provides detailed cross-model comparison capabilities. | 
| **Model and API Relay Checker** | Model fingerprinting, Claude Signature verification, relay black-box auditing, PAMELA, and Ventor QTest. | 

## **💎 Additional Benefits**

- 🖥️ **Modern Web Interface** : User-friendly UI with one-click scanning and real-time progress tracking
- 🔌 **Complete API** : Full interface documentation and Swagger specifications for easy integration
- 🤖 **Agent-Ready** : Plug-and-play agent skills on ClawHub —[EdgeOne ClawScan](https://clawhub.ai/aigsec/edgeone-clawscan) ,[EdgeOne Skill Scanner](https://clawhub.ai/aigsec/edgeone-skill-scanner) , and[AIG Scanner](https://clawhub.ai/aigsec/aig-scanner) — seamlessly embed security scanning into any AI agent workflow
- 🌐 **Multi-Language** : Chinese and English interfaces with localized documentation
- 🐳 **Cross-Platform** : Linux, macOS, and Windows support with Docker-based deployment
- 🆓 **Free & Open Source** : Completely free under the Apache 2.0 license

![A.I.G Main Page](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/aig.gif)


![Plugin Management](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/plugin-gif.gif)


After deployment, open `http://localhost:8088` in your browser.


**What to enter as the target URL / IP?**

The target is the **network address of a running AI service** you want to scan - not a GitHub URL or source code path. A.I.G connects to the live service and fingerprints it for known CVE vulnerabilities.

| Scenario | Example target | 
|---|---|
| A locally running vLLM instance | `http://127.0.0.1:8000` | 
| An Ollama server on your LAN | `http://192.168.1.100:11434` | 
| A ComfyUI instance exposed internally | `http://10.0.0.5:8188` | 
| Multiple hosts (one per line) | `192.168.1.0/24` (CIDR),`10.0.0.1-10.0.0.20` (range) | 

**Step-by-step: Scan a local vLLM instance**

1. Start vLLM normally (e.g. `python -m vllm.entrypoints.api_server --model meta-llama/...` )
2. In the A.I.G web UI, click **"AI基础设施安全扫描 / AI Infra Scan"**
3. Enter `http://127.0.0.1:8000` (or the IP/port where vLLM is listening)
4. Click **Start Scan** - A.I.G will fingerprint the service and match it against 2000+ known CVEs
5. View the report: component version, matched vulnerabilities, severity, and remediation links

💡 **Tip**: To scan the *nightly* build of vLLM specifically, just run that nightly build and point A.I.G at its address. The scanner detects the version automatically.


Enter either a **remote URL** (e.g. `https://github.com/user/mcp-server`) or **upload a local source archive** - no running instance required.

Configure the target LLM's API endpoint (base URL + API key) in **Settings → Model Config**, then select a dataset and start the evaluation.

Visit our online documentation: [https://tencent.github.io/AI-Infra-Guard/](https://tencent.github.io/AI-Infra-Guard/)

For more detailed FAQs and troubleshooting guides, visit our [documentation](https://tencent.github.io/AI-Infra-Guard/?menu=faq).


A.I.G provides a comprehensive set of task creation APIs that support AI infra scan, MCP Server Scan, and Jailbreak Evaluation capabilities.

After the project is running, visit `http://localhost:8088/docs/index.html` to view the complete API documentation.

For detailed API usage instructions, parameter descriptions, and complete example code, please refer to the [Complete API Documentation](https://github.com/Tencent/AI-Infra-Guard/blob/main/api.md).


The extensible plugin framework serves as A.I.G's architectural cornerstone, inviting community innovation through Plugin and Feature contributions.

1. **Fingerprint Rules** : Add new YAML fingerprint files to the`data/fingerprints/` directory.
2. **Vulnerability Rules** : Add new vulnerability scan rules to the`data/vuln/` directory.
3. **MCP Plugins** : Add new MCP security scan rules to the`data/mcp/` directory.
4. **Jailbreak Evaluation Datasets** : Add new Jailbreak evaluation datasets to the`data/eval` directory.

Please refer to the existing rule formats, create new files, and submit them via a Pull Request.

This project is led and developed by **Tencent Zhuque Lab**, part of the Tencent Security Platform Department. Founded in 2019, [Tencent Zhuque Lab](https://matrix.tencent.com/) is a top-tier security research lab focused on real-world offensive and defensive research and frontier technology in the AI security space, covering large model security, AI agent security, AI-empowered security, and AI-generated content detection.

The team has helped major vendors such as **NVIDIA, Google, and Microsoft**, as well as open-source communities like **OpenClaw, Linux, and Hugging Face**, fix a large number of high-risk vulnerabilities, and has been publicly acknowledged by them.

We have released open-source AI security products including the AI Red Team Security Testing Platform **A.I.G (AI-Infra-Guard)** and the **Zhuque AI Detection Assistant**. Our research has been widely published at top international security and AI conferences such as **Black Hat, DEF CON, ICLR, CVPR, NeurIPS, and ACL**, and we have authored the book *"AI Security: Technology and Practice"*.

| Role | Member | Contribution | 
|---|---|---|
| Head of Tencent Security Platform Department | **Yong Yang** | Initiated A.I.G and proposed automated assessment of AI agent loss-of-control risks, guiding the platform's expansion from AI infrastructure vulnerability scanning to agent execution risk, tool misuse, and permission-boundary evaluation. | 
| Head of Tencent Zhuque Lab | **Xing Zheng** | Proposed the automated vulnerability-update and benchmark-alignment mechanism, helping AI Infra fingerprints, CVE/GHSA rules, and benchmarks iterate continuously. | 
| Project Lead | **Nicky** | Frontier security research, product planning, technical-route decisions, internal and external collaboration, and communications. | 
| Technical Lead | **Python** | Overall architecture design, core module development, and version iteration. | 
| Core Contributor | **Zona** | Frontend interaction, product experience, community operations, and user-feedback loop. | 
| Core Contributor | **Fyoung** | AI Infra vulnerability component fingerprint updates and Benchmark system construction. | 
| Core Contributor | **Xiangfan** | Security capability development for Skill risks and agent loss-of-control scenarios. | 
| Core Contributor | **Elwood** | Enhancing Agent security scanning capabilities and updating technical reports. | 
| Core Contributor | **Robert** | LLM safety assessment and jailbreak-evaluation strategy operations. | 
| Core Contributor | **Zoe** | LLM safety assessment, jailbreak evaluation, and model-integration module development. | 
| Contributor | **Ronin** | Participated in AI agent security scanning development. | 
| Contributor | **Rsin** | Participated in community operations and campaign communications. | 

We thank our academic partners for their research contributions and technical support.

|          [<sub>**Prof. hui Li**</sub>](https://github.com)        |          [<sub>**Bin Wang**</sub>](mailto:1546697086@qq.com)        |          [<sub>**Zexin Liu**</sub>](mailto:kpghat@gmail.com)        |          [<sub>**Hao Yu**</sub>](mailto:g.diorld@gmail.com)        |          [<sub>**Ao Yang**</sub>](mailto:719001405@qq.com)        |          [<sub>**Zhengxi Lin**</sub>](mailto:linzhengxi7@126.com)        | 

|          [<sub>**Prof. Zhemin Yang**</sub>](mailto:yangzhemin@fudan.edu.cn)        |          [<sub>**Kangwei Zhong**</sub>](mailto:kwzhong23@m.fudan.edu.cn)        |          [<sub>**Jiapeng Lin**</sub>](mailto:linjp23@m.fudan.edu.cn)        |          [<sub>**Cheng Sheng**</sub>](mailto:csheng25@m.fudan.edu.cn)        | 

Thanks to all the developers who have contributed to the A.I.G project.

|  | ![WeChat Security](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/wechat_security.png) | ![Fit Security](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/fit_sec_logo.png) | 

Thanks to the users from the following organizations and teams for using A.I.G and their valuable feedback.

![Tencent](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/tencent.png) 

![DeepSeek](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/deepseek.png) 

![Lenovo](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/lenovo.png) 

![ICBC](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/ICBC.jpg) 

![Vivo](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/vivo.png) 

![Oppo](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/oppo.png) 

![Haier](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/haier.png) 

![Abc](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/abc.png) 

![招商银行](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/JkOvmDOXpr.png) 

![中国电信](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/中国电信.png) 

![Bilibili](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/bilibili.jpg) 

![Qunar](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/qunar.png) 

![蜜雪冰城](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/蜜雪冰城.png) 

![IDG](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/IDG.webp) 

![kingdee](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/kingdee.png) 

![联通数科](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/unicom.png) 

![长安汽车](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/changan.png) 

![天鹅到家](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/tiane.png)

![清华大学](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/清华大学.jpg) 

![北京大学](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/北京大学.png) 

![南洋理工大学](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/nanyang.png) 

![复旦大学](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/fudan.png) 

![浙江大学](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/浙江大学.png) 

![南京大学](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/南京大学.png) 

![武汉大学](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/wuhan.png) 

![An-Najah National University](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/An-NajahNationalUniversity.png) 

![西安交通大学](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/西安交通大学.png) 

![华中科技大学](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/huazhong.png) 

![南开大学](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/南开大学.jpg) 

![四川大学](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/四川大学.png) 

- **GitHub Discussions** :[Join our community discussions](https://github.com/Tencent/AI-Infra-Guard/discussions)
- **Issues & Bug Reports** :[Report issues or suggest features](https://github.com/Tencent/AI-Infra-Guard/issues)

| WeChat Group | Discord [\[link\]](https://discord.gg/U9dnPnyadZ) | 
|---|---|
| ![WeChat Group](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/wechatgroup.png) | ![discord](https://github.com/Tencent/AI-Infra-Guard/raw/main/img/discord.png) | 

For collaboration inquiries or feedback, please contact us at: [zhuque@tencent.com](mailto:zhuque@tencent.com)

If you are interested in code security, check out [A.S.E (AICGSecEval)](https://github.com/Tencent/AICGSecEval), the industry's first repository-level AI-generated code security evaluation framework open-sourced by the Tencent Wukong Code Security Team.

If you use A.I.G in your research, please cite:

```
@misc{Tencent_AI-Infra-Guard_2025,
  author={{Tencent Zhuque Lab}},
  title={{AI-Infra-Guard: A Comprehensive, Intelligent, and Easy-to-Use AI Red Teaming Platform}},
  year={2025},
  howpublished={GitHub repository},
  url={https://github.com/Tencent/AI-Infra-Guard}
}
```
**Research:**

1. 
**"DeepSeek Harness Indirect Prompt-Injection Assessment"** — Authorized security assessment of DeepSeek Harness against indirect prompt-injection across 14,560 agent runs.[\[code\]](https://github.com/Tencent/AI-Infra-Guard/blob/main/Research/deepseek-harness-security-assessment)
2. 
**"SkillJack: Persistent Skill Backdoors in Self-Evolving Agents"** — Demonstrates how poisoned trajectories can inject persistent backdoors into self-evolving agent skill systems.[\[code\]](https://github.com/Tencent/AI-Infra-Guard/blob/main/Research/SkillJack)

**Papers:**

1. 
**"Securing the AI Agent: A Unified Framework for Multi-Layer Agent Red Teaming"** — A comprehensive framework for securing AI agent systems through multi-layer red teaming across infrastructure, supply chain, runtime interaction, and deployment surfaces.[\[arXiv\]](https://arxiv.org/pdf/2606.31227)[\[pdf\]](https://github.com/Tencent/AI-Infra-Guard/blob/main/Securing_the_AI_Agent.pdf)
2. 
**"AI-Infra-Guard: An AI Red Teaming Platform"** — Black Hat Europe 2025 Arsenal presentation showcasing A.I.G's capabilities and real-world use cases.[\[pdf\]](https://github.com/Tencent/AI-Infra-Guard/blob/main/Arsenal-BHEU2025-AI-Infra-Guard.pdf)
3. 
**"MCP Unchained: Compromising The AI Agent Ecosystem Via Its Universal Connector"** — Black Hat Europe 2025 talk revealing security risks in the MCP protocol within the AI agent ecosystem.[\[pdf\]](https://github.com/Tencent/AI-Infra-Guard/blob/main/BHEU-25-MCP-Unchained-Compromising-The-AI-Agent-Ecosystem-Via-Its-Universal-Connector.pdf)

Thanks to the research teams who have cited A.I.G in their academic work (19 papers):

## 📄 View all 19 cited papers

1. 
Chenning Li, Pan Hu, Justin Xu et al. **"ADR: An Agentic Detection System for Enterprise Agentic AI Security."** arXiv preprint arXiv:2605.17380 (2026).[\[pdf\]](http://arxiv.org/abs/2605.17380v1)
2. 
Zhaojiacheng Zhou. **"Proteus: A Self-Evolving Red Team for Agent Skill Ecosystems."** arXiv preprint arXiv:2605.11891 (2026).[\[pdf\]](http://arxiv.org/abs/2605.11891v1)
3. 
Hengkai Ye, Zhechang Zhang, Jinyuan Jia et al. **"TRUSTDESC: Preventing Tool Poisoning in LLM Applications via Trusted Description Generation."** arXiv preprint arXiv:2604.07536 (2026).[\[pdf\]](https://arxiv.org/abs/2604.07536)
4. 
Zenghao Duan, Yuxin Tian, Zhiyi Yin et al. **"SkillAttack: Automated Red Teaming of Agent Skills through Attack Path Refinement."** arXiv preprint arXiv:2604.04989 (2026).[\[pdf\]](https://arxiv.org/abs/2604.04989)
5. 
Yiheng Huang, Zhijia Zhao, Bihuan Chen et al. **"From Component Manipulation to System Compromise: Understanding and Detecting Malicious MCP Servers."** arXiv preprint arXiv:2604.01905 (2026).[\[pdf\]](https://arxiv.org/abs/2604.01905)
6. 
Yi Ting Shen, Kentaroh Toyoda, Alex Leung. **"MCP-38: A Comprehensive Threat Taxonomy for Model Context Protocol Systems (v1.0)."** arXiv preprint arXiv:2603.18063 (2026).[\[pdf\]](https://arxiv.org/abs/2603.18063)
7. 
Yuepeng Hu, Yuqi Jia, Mengyuan Li et al. **"MalTool: Malicious Tool Attacks on LLM Agents."** arXiv preprint arXiv:2602.12194 (2026).[\[pdf\]](https://arxiv.org/abs/2602.12194)
8. 
Naen Xu, Jinghuai Zhang, Ping He et al. **"FraudShield: Knowledge Graph Empowered Defense for LLMs against Fraud Attacks."** arXiv preprint arXiv:2601.22485v1 (2026).[\[pdf\]](http://arxiv.org/abs/2601.22485v1)
9. 
Ruiqi Li, Zhiqiang Wang, Yunhao Yao et al. **"MCP-ITP: An Automated Framework for Implicit Tool Poisoning in MCP."** arXiv preprint arXiv:2601.07395v1 (2026).[\[pdf\]](http://arxiv.org/abs/2601.07395v1)
10. 
Jingxiao Yang, Ping He, Tianyu Du et al. **"HogVul: Black-box Adversarial Code Generation Framework Against LM-based Vulnerability Detectors."** arXiv preprint arXiv:2601.05587v1 (2026).[\[pdf\]](http://arxiv.org/abs/2601.05587v1)
11. 
Teofil Bodea, Masanori Misono, Julian Pritzi et al. **"Trusted AI Agents in the Cloud."** arXiv preprint arXiv:2512.05951v1 (2025).[\[pdf\]](http://arxiv.org/abs/2512.05951v1)
12. 
Yunyi Zhang, Shibo Cui, Baojun Liu et al. **"Beyond Jailbreak: Unveiling Risks in LLM Applications Arising from Blurred Capability Boundaries."** arXiv preprint arXiv:2511.17874v2 (2025).[\[pdf\]](http://arxiv.org/abs/2511.17874v2)
13. 
Bin Wang, Zexin Liu, Hao Yu et al. **"MCPGuard: Automatically Detecting Vulnerabilities in MCP Servers."** arXiv preprint arXiv:2510.23673v1 (2025).[\[pdf\]](http://arxiv.org/abs/2510.23673v1)
14. 
Weibo Zhao, Jiahao Liu, Bonan Ruan et al. **"When MCP Servers Attack: Taxonomy, Feasibility, and Mitigation."** arXiv preprint arXiv:2509.24272v1 (2025).[\[pdf\]](http://arxiv.org/abs/2509.24272v1)
15. 
Ping He, Changjiang Li, et al. **"Automatic Red Teaming LLM-based Agents with Model Context Protocol Tools."** arXiv preprint arXiv:2509.21011 (2025).[\[pdf\]](https://arxiv.org/abs/2509.21011)
16. 
Christian Coleman. **"Behavioral Detection Methods for Automated MCP Server Vulnerability Assessment."** (2025).[\[pdf\]](https://digitalcommons.odu.edu/cgi/viewcontent.cgi?article=1138&context=covacci-undergraduateresearch)
17. 
Yixuan Yang, Daoyuan Wu, Yufan Chen. **"MCPSecBench: A Systematic Security Benchmark and Playground for Testing Model Context Protocols."** arXiv preprint arXiv:2508.13220 (2025).[\[pdf\]](https://arxiv.org/abs/2508.13220)
18. 
Yongjian Guo, Puzhuo Liu, et al. **"Systematic Analysis of MCP Security."** arXiv preprint arXiv:2508.12538 (2025).[\[pdf\]](https://arxiv.org/abs/2508.12538)
19. 
Zexin Wang, Jingjing Li, et al. **"A Survey on AgentOps: Categorization, Challenges, and Future Directions."** arXiv preprint arXiv:2508.02121 (2025).[\[pdf\]](https://arxiv.org/abs/2508.02121)

📧 If you have used A.I.G in your research or product, or if we have inadvertently missed your publication, we would love to hear from you! [Contact us here](https://github.com#-join-the-community).


This project is open-sourced under the **Apache License 2.0**. We warmly welcome and encourage community contributions, integrations, and derivative works, subject to the following attribution requirements:

1. **Retain notices** : You must retain the`LICENSE` and`NOTICE` files from the original project in any distribution.
2. **Product attribution** : If you integrate AI-Infra-Guard's core code, components, or scanning engine into your open-source project, commercial product, or internal platform, you must clearly state the following in your**product documentation, usage guide, or UI "About" page** :"This project integrates [AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) , open-sourced by Tencent Zhuque Lab."
3. **Academic & article citation** : If you use this tool in vulnerability analysis reports, security research articles, or academic papers, please explicitly mention "Tencent Zhuque Lab AI-Infra-Guard" and include a link to the repository.

Repackaging this project as an original product without disclosing its origin is strictly prohibited.
