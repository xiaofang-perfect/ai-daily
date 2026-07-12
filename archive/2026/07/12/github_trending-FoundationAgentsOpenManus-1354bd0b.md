---
title: "FoundationAgents/OpenManus"
source: GitHub Trending
url: https://github.com/FoundationAgents/OpenManus
date: 2026-07-12
published_at: 2026-07-12T05:23:52.404382+00:00
tag: 工具开源
item_id: 1354bd0be5de3453
---
![](https://github.com/FoundationAgents/OpenManus/raw/main/assets/logo.jpg)


 
  




Manus is incredible, but OpenManus can achieve any idea without an *Invite Code* 🛫!

Our team members [@Xinbin Liang](https://github.com/mannaandpoem) and [@Jinyu Xiang](https://github.com/XiangJinyu) (core authors), along with [@Zhaoyang Yu](https://github.com/MoshiQAQ), [@Jiayi Zhang](https://github.com/didiforgithub), and [@Sirui Hong](https://github.com/stellaHSR), we are from [@MetaGPT](https://github.com/geekan/MetaGPT). The prototype is launched within 3 hours and we are keeping building!

It's a simple implementation, so we welcome any suggestions, contributions, and feedback!

Enjoy your own agent with OpenManus!

We're also excited to introduce [OpenManus-RL](https://github.com/OpenManus/OpenManus-RL), an open-source project dedicated to reinforcement learning (RL)- based (such as GRPO) tuning methods for LLM agents, developed collaboratively by researchers from UIUC and OpenManus.

## seo_website.mp4

We provide two installation methods. Method 2 (using uv) is recommended for faster installation and better dependency management.

- Create a new conda environment:

```
conda create -n open_manus python=3.12
conda activate open_manus
```
- Clone the repository:

```
git clone https://github.com/FoundationAgents/OpenManus.git
cd OpenManus
```
- Install dependencies:

`pip install -r requirements.txt`- Install uv (A fast Python package installer and resolver):

`curl -LsSf https://astral.sh/uv/install.sh | sh`- Clone the repository:

```
git clone https://github.com/FoundationAgents/OpenManus.git
cd OpenManus
```
- Create a new virtual environment and activate it:

```
uv venv --python 3.12
source .venv/bin/activate  # On Unix/macOS
# Or on Windows:
# .venv\Scripts\activate
```
- Install dependencies:

`uv pip install -r requirements.txt``playwright install`OpenManus requires configuration for the LLM APIs it uses. Follow these steps to set up your configuration:

- Create a `config.toml`file in the`config`directory (you can copy from the example):

`cp config/config.example.toml config/config.toml`- Edit `config/config.toml`to add your API keys and customize settings:

```
# Global LLM configuration
[llm]
model = "gpt-4o"
base_url = "https://api.openai.com/v1"
api_key = "sk-..."  # Replace with your actual API key
max_tokens = 4096
temperature = 0.0
# Optional configuration for specific LLM models
[llm.vision]
model = "gpt-4o"
base_url = "https://api.openai.com/v1"
api_key = "sk-..."  # Replace with your actual API key
```
One line for run OpenManus:

`python main.py`Then input your idea via terminal!

For MCP tool version, you can run:

`python run_mcp.py`For unstable multi-agent version, you also can run:

`python run_flow.py`Currently, besides the general OpenManus Agent, we have also integrated the DataAnalysis Agent, which is suitable for data analysis and data visualization tasks. You can add this agent to `run_flow` in `config.toml`.

```
# Optional configuration for run-flow
[runflow]
use_data_analysis_agent = true     # Disabled by default, change to true to activate
```
In addition, you need to install the relevant dependencies to ensure the agent runs properly: [Detailed Installation Guide](https://github.com/FoundationAgents/OpenManus/blob/main/app/tool/chart_visualization/README.md##Installation)

We welcome any friendly suggestions and helpful contributions! Just create issues or submit pull requests.

Or contact @mannaandpoem via 📧email: [mannaandpoem@gmail.com](mailto:mannaandpoem@gmail.com)

**Note**: Before submitting a pull request, please use the pre-commit tool to check your changes. Run `pre-commit run --all-files` to execute the checks.

Join our networking group on Feishu and share your experience with other developers!

![OpenManus 交流群](https://github.com/FoundationAgents/OpenManus/raw/main/assets/community_group.jpg)

Thanks to [PPIO](https://ppinfra.com/user/register?invited_by=OCPKCN&utm_source=github_openmanus&utm_medium=github_readme&utm_campaign=link) for computing source support.

PPIO: The most affordable and easily-integrated MaaS and GPU cloud solution.


Thanks to [anthropic-computer-use](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo), [browser-use](https://github.com/browser-use/browser-use) and [crawl4ai](https://github.com/unclecode/crawl4ai) for providing basic support for this project!

Additionally, we are grateful to [AAAJ](https://github.com/metauto-ai/agent-as-a-judge), [MetaGPT](https://github.com/geekan/MetaGPT), [OpenHands](https://github.com/All-Hands-AI/OpenHands) and [SWE-agent](https://github.com/SWE-agent/SWE-agent).

We also thank stepfun(阶跃星辰) for supporting our Hugging Face demo space.

OpenManus is built by contributors from MetaGPT. Huge thanks to this agent community!

```
@misc{openmanus2025,
  author = {Xinbin Liang and Jinyu Xiang and Zhaoyang Yu and Jiayi Zhang and Sirui Hong and Sheng Fan and Xiao Tang and Bang Liu and Yuyu Luo and Chenglin Wu},
  title = {OpenManus: An open-source framework for building general AI agents},
  year = {2025},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.15186407},
  url = {https://doi.org/10.5281/zenodo.15186407},
}
```
