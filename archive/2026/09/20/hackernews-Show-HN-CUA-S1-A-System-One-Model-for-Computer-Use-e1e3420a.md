---
title: "Show HN: CUA-S1 – A System One Model for Computer Use"
source: Hacker News
url: https://github.com/trycua/cua
date: 2026-09-20
published_at: 2026-09-19T15:52:51+00:00
tag: 工具开源
item_id: e1e3420a9dfafffc
---
**Give AI agents computers they can use.**

Cua provides open-source desktop automation, isolated cloud desktops, local macOS VMs, specialist decision models, and benchmarks for evaluating computer-use agents.

[Try Cua Fleets now at run.cua.ai](https://run.cua.ai/?utm_source=github&utm_medium=referral&utm_campaign=fleet_activation&content_id=repo_readme)

    
    
    

    

    


  

| ![Cua Fleets: isolated cloud desktops for your agents](https://github.com/trycua/cua/raw/main/img/card-cua-fleets-wide.gif)  |  | ![CUA-S1: small, specialized models for computer use.](https://github.com/trycua/cua/raw/main/img/card-cua-s1.gif)  | 
| ![Cua Driver: inspect and operate apps on macOS, Windows, and Linux](https://github.com/trycua/cua/raw/main/img/card-cua-driver.gif)  | ![Lume: local macOS and Linux VMs on Apple Silicon](https://github.com/trycua/cua/raw/main/img/card-cua-lume.gif)  | ![Cua Bench: create tasks, evaluate agents, and export trajectories](https://github.com/trycua/cua/raw/main/img/card-cua-bench.gif)  | 

- **Cua Fleets:**[Provision a Linux desktop, run a command, and save a screenshot](https://cua.ai/docs/tutorials/your-first-cloud-fleet) .
- **CUA-S1:**[Explore small, specialized models for computer-use decisions](https://github.com#cua-s1) .
- **Cua Driver:**[Operate Calculator and verify its result](https://cua.ai/docs/tutorials/drive-your-first-app) .
- **Lume:**[Create a Tahoe VM and connect over SSH](https://cua.ai/docs/tutorials/create-your-first-lume-vm) .
- **Cua Bench:**[Create and verify a simulated task](https://cua.ai/docs/tutorials/your-first-cua-bench-task) .

Bring your own agent and model, or explore CUA-S1 for specialized decisions. Cua provides the computer and automation tools. [Computer-Use 2.0](https://cua.ai/docs/concepts/what-is-computer-use) describes an agent moving between code, APIs, and graphical interfaces within the same task.

Two Cua Driver sessions select cells in LibreOffice Calc and objects in Inkscape on an Omarchy desktop while a terminal stays in the foreground. Watch the 50-second demo, then explore [Omarchy on Fleet](https://cua.ai/docs/how-to-guides/sandbox/run-omarchy-on-cloud-fleet).

## recording.mp4

Provision isolated cloud desktops at [run.cua.ai](https://run.cua.ai/?utm_source=github&utm_medium=referral&utm_campaign=fleet_activation&content_id=repo_readme). A Fleet maintains sandbox capacity; your code claims a desktop from a pool and uses the Sandbox SDK to run commands, capture screenshots, and interact with apps inside it.

**Your first result:** provision a Linux desktop, run `uname -a`, save a screenshot, and delete the cloud resources. The tutorial covers Fleet credentials, dependencies, and cleanup. Pools can retain paid capacity after a claim ends, so follow its cleanup steps.

Local sandboxes and Fleets share the Sandbox SDK, but credentials, images, operations, and runtime requirements differ. Use the [runtime support reference](https://cua.ai/docs/reference/sandbox-sdk/runtime-support) to choose an environment. For your own hardware, see [Manage local sandbox lifecycle](https://cua.ai/docs/how-to-guides/sandbox/manage-local-lifecycle).

**[Your first Cloud Fleet](https://cua.ai/docs/tutorials/your-first-cloud-fleet)** | **[Fleet overview](https://cua.ai/docs/cloud-fleets)** | [Sandbox SDK reference](https://cua.ai/docs/reference/sandbox-sdk)

Give your agent tools to inspect and operate native desktop apps and browsers on macOS, Windows, and Linux. Connect through the CLI, MCP, or typed SDKs. Background delivery lets agents work without moving your pointer or taking focus when the app and platform support it; see [platform support](https://cua.ai/docs/reference/cua-driver/platform-support) for the boundaries.

**macOS / Linux**

`/bin/bash -c "$(curl -fsSL https://cua.ai/driver/install.sh)"`
**Windows (PowerShell)**

`irm https://cua.ai/driver/install.ps1 | iex`
**Your first result:** connect your agent, ask it to compute 6 × 7 in Calculator, and have it verify that the app displays 42. The tutorial covers platform setup, permissions, and agent connection.

**[Drive your first app](https://cua.ai/docs/tutorials/drive-your-first-app)** | **[Installation](https://cua.ai/docs/how-to-guides/driver/install)** | [CLI Reference](https://cua.ai/docs/reference/cua-driver/cli-reference)

Using Claude Code, Codex, Cursor, OpenClaw, or another agent? [Find your integration](https://cua.ai/docs/how-to-guides/driver/connect-your-agent). Source documentation and architecture notes live in [`libs/cua-driver/README.md`](https://github.com/trycua/cua/blob/main/libs/cua-driver/README.md).

CUA-S1 is our family of small, specialized System 1 models for computer use. We use "System 1" as an engineering analogy for fast, bounded decisions, such as choosing which value belongs in a field or whether to leave an element alone. It is not a strict classification of model architectures or a replacement for a general-purpose agent's planning and reasoning.

The first research profile focuses on forms: scoring decisions from structured interface elements and document values rather than generating a response token by token. Application code orders the actions, and the optional Cua Driver integration handles execution with explicit action boundaries.

The project includes Python model code, synthetic-data generation, training, and evaluation. The GitHub component is an early, source-only research release; model weights are hosted separately on Hugging Face. The source is MIT-licensed. Check each model and dataset card for its scope, limitations, and artifact-specific license.

**[Explore CUA-S1](https://github.com/trycua/cua/blob/main/libs/cua-s1)** | **[Model card](https://github.com/trycua/cua/blob/main/libs/cua-s1/MODEL_CARD.md)** | [Safety and deployment guidance](https://github.com/trycua/cua/blob/main/libs/cua-s1/SECURITY.md)

**CUA-S1-FORMS on Hugging Face:** **[Model weights](https://huggingface.co/cua-ai/cua-s1-forms)** | [Dataset](https://huggingface.co/datasets/cua-ai/cua-s1-forms)

Create and manage local macOS and Linux VMs on Apple Silicon using Apple's Virtualization.Framework.

`/bin/bash -c "$(curl -fsSL https://cua.ai/lume/install.sh)"`
**Your first result:** create a vanilla macOS Tahoe VM from an Apple restore image, start it, and connect over SSH. The tutorial uses the Lume CLI directly and explains the unattended setup defaults.

**[Create your first Lume VM](https://cua.ai/docs/tutorials/create-your-first-lume-vm)** | **[Installation](https://cua.ai/docs/how-to-guides/lume/install-lume)** | [CLI reference](https://cua.ai/docs/reference/lume/cli-reference)

Build computer-use tasks, evaluate agents, and export trajectories for training. Start with a simulated task that requires no VM, Docker, or model API key.

With Python 3.12 or 3.13 and [uv](https://docs.astral.sh/uv/) installed:

```
uv tool install 'cua-bench[browser]'
uv tool run --from 'cua-bench[browser]' playwright install chromium
```
**Your first result:** create a small task, run its reference solution, and verify that its evaluator reports a reward of `1.0`. Then try the same task yourself.

**[Build your first task](https://cua.ai/docs/tutorials/your-first-cua-bench-task)** | **[What is Cua-Bench?](https://cua.ai/docs/concepts/what-is-cua-bench)** | **[CLI reference](https://cua.ai/docs/reference/cua-bench/cli-reference)** | [Partner with us](https://cuabench.ai/)

- [Documentation](https://cua.ai/docs) — Guides, examples, and API reference
- [Blog](https://cua.ai/blog) — Tutorials, updates, and research
- [Discord](https://discord.com/invite/mVnXXpdE85) — Community support and discussions
- [GitHub Issues](https://github.com/trycua/cua/issues) — Bug reports and feature requests
- [Security](https://github.com/trycua/cua/blob/main/SECURITY.md) — Private vulnerability reporting

If Cua supports your research, please cite the software:

```
@software{cua2025,
  author  = {{Cua AI, Inc.}},
  title   = {Cua},
  year    = {2025},
  url     = {https://github.com/trycua/cua},
  license = {MIT}
}
```
For reproducibility, include the Cua release or commit used in your experiments. Citation metadata is also available in [`CITATION.cff`](https://github.com/trycua/cua/blob/main/CITATION.cff).

We welcome contributions! See our [Contributing Guidelines](https://github.com/trycua/cua/blob/main/CONTRIBUTING.md) for details.

MIT License — see [LICENSE](https://github.com/trycua/cua/blob/main/LICENSE.md) for details.

Third-party components have their own licenses:

- [Kasm](https://github.com/trycua/cua/blob/main/libs/kasm/LICENSE) (MIT)
- [OmniParser](https://github.com/microsoft/OmniParser/blob/master/LICENSE) (CC-BY-4.0)
- Optional `cua-agent[omni]` includes ultralytics (AGPL-3.0)

Apple, macOS, Ubuntu, Canonical, and Microsoft are trademarks of their respective owners. This project is not affiliated with or endorsed by these companies.

Thank you to all our [GitHub Sponsors](https://github.com/sponsors/trycua)!

| [Adam Cohen Hillel](https://github.com/adamcohenhillel) | [CodeRabbit](https://github.com/coderabbitai) | [Zephyr Cloud IO](https://github.com/ZephyrCloudIO) | 
|---|---|---|
