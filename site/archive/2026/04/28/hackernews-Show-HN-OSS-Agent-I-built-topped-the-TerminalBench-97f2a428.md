---
title: "Show HN: OSS Agent I built topped the TerminalBench on Gemini-3-flash-preview"
source: Hacker News
url: https://github.com/dirac-run/dirac
date: 2026-04-28
published_at: 2026-04-27T12:35:55+00:00
tag: 工具开源
item_id: 97f2a4282915c5d6
---
Dirac topped the[Terminal-Bench-2 leaderboard]for`gemini-3-flash-preview`

with a 65.2% score!

It is a well studied phenomenon that any given model's reasoning ability degrades with the context length. If we can keep context tightly curated, we improve both accuracy and cost while making larger changes tractable in a single task.

Dirac is an open-source coding agent built with this in mind. It reduces API costs by **64.8%** on average while producing better and faster work. Using hash-anchored parallel edits, AST manipulation, and a suite of advanced optimizations. Oh, and no MCP.

Our goal: Optimize for bang-for-the-buck on tooling with bare minimum prompting instead of going blindly minimalistic.

Dirac is benchmarked against other leading open-source agents on complex, real-world refactoring tasks. Dirac consistently achieves 100% accuracy at a fraction of the cost. These evals are run on public github repos and should be reproducible by anyone.

🏆

TerminalBench 2.0 Leaderboard: Dirac recently topped the[Terminal-Bench-2 leaderboard]with a65.2%score using`gemini-3-flash-preview`

. This outperforms both Google's official baseline (47.6%) and the top closed-source agent Junie CLI (64.3%). This was achieved without any benchmark-specific info or any`AGENTS.md`

files being inserted.


Note on the cost table below: A bug was discovered in Cline, the parent repo, after running these evals ([issue #10314]). We have submitted a[PR #10315]to fix this. This bug caused the evals for Dirac and Cline to slightly underreport the numbers ($0.03 vs $0.05 per million token cache read). Although there won't be a large difference, we will update the evals soon.

All tasks for all models used `gemini-3-flash-preview`

with thinking set to `high`


| Task (Repo) | Files* | Cline | Kilo | Ohmypi | Opencode | Pimono | Roo | Dirac |
|---|---|---|---|---|---|---|---|---|
| Task1 (
|

[(diff)](https://github.com/dirac-run/dirac/blob/master/evals/cline/cline_refactor_DynamicCache)[$0.37][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/kilo/kilo_code_refactor_DynamicCache_FAILURE)[N/A][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/ohmypi/ohmypi_refactor_DynamicCache)[$0.24][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/opencode/opencode_refactor_DynamicCache)[$0.20][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/pimono/pimono_refactor_DynamicCache)[$0.34][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/roo/roo_code_refactor_DynamicCache)[$0.49]**🟢**[(diff)](https://github.com/dirac-run/dirac/blob/master/evals/dirac/dirac_refactor_DynamicCache)[$0.13][vscode](https://github.com/microsoft/vscode))[(diff)](https://github.com/dirac-run/dirac/blob/master/evals/cline/cline_refactor_IOverlayWidget)[$0.67][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/kilo/kilo_code_refactor_IOverlayWidget)[$0.78][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/ohmypi/ohmypi_refactor_IOverlayWidget)[$0.63][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/opencode/opencode_refactor_IOverlayWidget)[$0.40][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/pimono/pimono_refactor_IOverlayWidget)[$0.48][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/roo/roo_code_refactor_IOverlayWidget)[$0.58]**🟢**[(diff)](https://github.com/dirac-run/dirac/blob/master/evals/dirac/dirac_refactor_IOverlayWidget)[$0.23][vscode](https://github.com/microsoft/vscode))[(diff)](https://github.com/dirac-run/dirac/blob/master/evals/cline/cline_refactor_addLogging)[$0.42][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/kilo/kilo_code_refactor_addLogging)[$0.70][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/ohmypi/ohmypi_refactor_addLogging)[$0.64][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/opencode/opencode_refactor_addLogging)[$0.32][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/pimono/pimono_refactor_addLogging)[$0.25][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/roo/roo_code_refactor_addLogging)[$0.45]**🟢**[(diff)](https://github.com/dirac-run/dirac/blob/master/evals/dirac/dirac_refactor_addLogging)[$0.16][django](https://github.com/django/django))[(diff)](https://github.com/dirac-run/dirac/blob/master/evals/cline/cline_refactor_datadict)[$0.36][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/kilo/kilo_code_refactor_datadict)[$0.42][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/ohmypi/ohmypi_refactor_datadict)[$0.32][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/opencode/opencode_refactor_datadict)[$0.24][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/pimono/pimono_refactor_datadict)[$0.24][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/roo/roo_code_refactor_datadict)[$0.17]**🟢**[(diff)](https://github.com/dirac-run/dirac/blob/master/evals/dirac/dirac_refactor_datadict)[$0.08][vscode](https://github.com/microsoft/vscode))[(diff)](https://github.com/dirac-run/dirac/blob/master/evals/cline/cline_refactor_extensionswb_service_FAILURE)[N/A][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/kilo/kilo_code_refactor_extensionswb_service)[$0.71][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/ohmypi/ohmypi_refactor_extensionswb_service)[$0.43][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/opencode/opencode_refactor_extensionswb_service)[$0.53][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/pimono/pimono_refactor_extensionswb_service)[$0.50][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/roo/roo_code_refactor_extensionswb_service)[$0.36]**🟢**[(diff)](https://github.com/dirac-run/dirac/blob/master/evals/dirac/dirac_refactor_extensionswb_service)[$0.17][transformers](https://github.com/huggingface/transformers))[(diff)](https://github.com/dirac-run/dirac/blob/master/evals/cline/cline_refactor_latency)[$0.87][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/kilo/kilo_code_refactor_latency_WRONG)[$1.51][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/ohmypi/ohmypi_refactor_latency)[$0.94][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/opencode/opencode_refactor_latency)[$0.90][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/pimono/pimono_refactor_latency)[$0.52][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/roo/roo_code_refactor_latency)[$1.44]**🟢**[(diff)](https://github.com/dirac-run/dirac/blob/master/evals/dirac/dirac_refactor_latency)[$0.34][vscode](https://github.com/microsoft/vscode))[(diff)](https://github.com/dirac-run/dirac/blob/master/evals/cline/cline_refactor_sendRequest_2missing)[$0.51][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/kilo/kilo_code_refactor_sendRequest)[$0.77][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/ohmypi/ohmypi_refactor_sendRequest)[$0.74][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/opencode/opencode_refactor_sendRequest)[$0.67][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/pimono/pimono_refactor_sendRequest)[$0.45][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/roo/roo_code_refactor_sendRequest)[$1.05]**🟢**[(diff)](https://github.com/dirac-run/dirac/blob/master/evals/dirac/dirac_refactor_sendRequest)[$0.25][transformers](https://github.com/huggingface/transformers))[(diff)](https://github.com/dirac-run/dirac/blob/master/evals/cline/cline_refactor_stoppingcriteria)[$0.25][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/kilo/kilo_code_refactor_stoppingcriteria)[$0.19][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/ohmypi/ohmypi_code_refactor_stoppingcriteria)[$0.17][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/opencode/opencode_refactor_stoppingcriteria)[$0.26][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/pimono/pimono_code_refactor_stoppingcriteria)[$0.23][(diff)](https://github.com/dirac-run/dirac/blob/master/evals/roo/roo_code_refactor_stoppingcriteria)[$0.29]**🟢**[(diff)](https://github.com/dirac-run/dirac/blob/master/evals/dirac/dirac_refactor_stoppingcriteria)[$0.12]**Total Correct****8/8****Avg Cost****$0.18**🟢 Success | 🟡 Incomplete | 🔴 Failure



Cost Comparison: Dirac is64.8% cheaperthan the competition (a2.8xcost reduction).* Expected number of files to be modified/created to complete the task.

See

[evals/README.md]for detailed task descriptions and methodology.

**Hash-Anchored Edits**: Dirac uses stable line hashes to target edits with extreme precision, avoiding the "lost in translation" issues of traditional line-number based editing.**AST-Native Precision**: Built-in understanding of language syntax (TypeScript, Python, C++, etc.) allows Dirac to perform structural manipulations like function extraction or class refactoring with 100% accuracy.**Multi-File Batching**: Dirac can process and edit multiple files in a single LLM roundtrip, significantly reducing latency and API costs.**High-Bandwidth Context**: Optimized context curation keeps the agent lean and fast, ensuring the LLM always has the most relevant information without wasting tokens.**Autonomous Tool Use**: Dirac can read/write files, execute terminal commands, use a headless browser, and more - all while keeping you in control with an approval-based workflow.**Skills & AGENTS.md**: Customize Dirac's behavior with project-specific instructions using`AGENTS.md`

files. It also seamlessly picks up Claude's skills by automatically reading from`.ai`

,`.claude`

, and`.agents`

directories.**Native Tool Calling Only**: To ensure maximum reliability and performance, Dirac exclusively supports models with native tool calling enabled. (Note: MCP is not supported).

Install Dirac from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=dirac-run.dirac).

Install the Dirac CLI globally using npm:

`npm install -g dirac-cli`

**Authenticate**:dirac auth

**Run your first task**:`dirac "Analyze the architecture of this project"`


You can provide API keys via environment variables to skip the `dirac auth`

step. This is ideal for CI/CD or non-persistent environments:

`ANTHROPIC_API_KEY`

`OPENAI_API_KEY`

`OPENROUTER_API_KEY`

`GEMINI_API_KEY`

`GROQ_API_KEY`

`MISTRAL_API_KEY`

`XAI_API_KEY`

(x.ai)`HF_TOKEN`

(HuggingFace)- ... and others (see
`src/shared/storage/env-config.ts`

for the full list).

Use Bedrock by setting AWS credentials and region. When any of these are present, Dirac automatically switches to the Bedrock provider:

`AWS_REGION`

— AWS region (e.g.`us-east-1`

)`AWS_ACCESS_KEY_ID`

— AWS access key`AWS_SECRET_ACCESS_KEY`

— AWS secret key`AWS_SESSION_TOKEN`

— session token (for temporary credentials)`AWS_BEDROCK_MODEL`

— model ID for both act and plan modes (e.g.`us.anthropic.claude-sonnet-4-6`

)`AWS_BEDROCK_MODEL_ACT`

— model ID for act mode only`AWS_BEDROCK_MODEL_PLAN`

— model ID for plan mode only

Works seamlessly with [aws-vault](https://github.com/99designs/aws-vault):

```
AWS_REGION=us-east-1 AWS_BEDROCK_MODEL=us.anthropic.claude-sonnet-4-6 \
aws-vault exec my-profile -- dirac "your task"
```


Note:Newer Claude models on Bedrock (Sonnet 4.6+) require a cross-region inference profile prefix (`us.`

,`eu.`

,`ap.`

). See the[AWS docs]for supported model IDs.

`dirac "prompt"`

: Start an interactive task.`dirac -p "prompt"`

: Run in**Plan Mode**to see the strategy before executing.`dirac -y "prompt"`

:**Yolo Mode**(auto-approve all actions, great for simple fixes).`git diff | dirac "Review these changes"`

: Pipe context directly into Dirac.`dirac history`

: View and resume previous tasks.

- Open the Dirac sidebar in VS Code.
- Configure your preferred AI provider (Anthropic, OpenAI, OpenRouter, etc.).
- Start a new task by describing what you want to build or fix.
- Watch Dirac go!



Dirac is **open source** and licensed under the [Apache License 2.0](https://github.com/dirac-run/dirac/blob/master/LICENSE).

Dirac is a fork of the excellent [Cline](https://github.com/cline/cline) project. We are grateful to the Cline team and contributors for their foundational work.

Built with ❤️ by [Max Trivedi](https://www.linkedin.com/in/max-trivedi-49993aab/) at [Dirac Delta Labs](https://dirac.run)
