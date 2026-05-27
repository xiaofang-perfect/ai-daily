---
title: "microsoft/agent-governance-toolkit"
source: GitHub Trending
url: https://github.com/microsoft/agent-governance-toolkit
date: 2026-05-27
published_at: 2026-05-27T06:22:37.267807+00:00
tag: 工具开源
item_id: 096a8e7ac09e34b9
---
**
🚀 Quick Start ·
📋 Specifications ·
📦 PyPI ·
📝 Changelog
**

Important

**Public Preview** -- production-quality, Microsoft-signed releases. May have breaking changes before GA.

Policy enforcement, identity, sandboxing, and SRE for autonomous AI agents. One `pip install`

, any framework.

Your AI agents call tools, browse the web, query databases, and delegate to other agents. Once deployed, they make decisions autonomously. You need answers to three questions:

**1. Is this action allowed?** An agent with access to `send_email`

and `query_database`

should not be able to `drop_table`

. OAuth scopes and IAM roles control which services an agent can reach, not what it does once connected.

**2. Which agent did this?** In a multi-agent system, five agents might share a single API key. When something goes wrong, "an agent did it" is not an incident response.

**3. Can you prove what happened?** Auditors and regulators need tamper-evident records of every decision: what policy was active, what the agent requested, and why it was allowed or denied.

Prompt-level safety ("please follow the rules") is not a control surface. It is a polite request to a stochastic system. [OWASP LLM01:2025](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) states this explicitly: *"it is unclear if there are fool-proof methods of prevention for prompt injection."* The published numbers back this up. On [JailbreakBench (Chao et al., NeurIPS 2024)](https://arxiv.org/abs/2404.01318), the standard open robustness benchmark for LLM jailbreaks, adaptive attacks reach **near-100% attack success rates** against frontier safety-aligned models. [Andriushchenko et al., 2024](https://arxiv.org/abs/2404.02151) report 100% ASR on GPT-4, GPT-3.5, Claude 3, and Llama-3 using simple prompt-only attacks, and even the strongest published prompt-layer defenses leak double-digit residual ASR. Microsoft's own [AI Red Teaming Agent](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-red-teaming-agent) formalizes **Attack Success Rate (ASR)**, the rate of policy violations under adversarial input, as the canonical metric for this class of failure, and [ Lessons from Red Teaming 100 Generative AI Products](https://www.microsoft.com/en-us/security/blog/2025/01/13/3-takeaways-from-red-teaming-100-generative-ai-products/) concludes that

*"AI red teaming is never complete"*because model-layer defenses are probabilistic by construction.

AGT does not try to win that fight inside the prompt. Every tool call, message send, and delegation is intercepted in deterministic application code *before* the model's intent reaches the wire. Actions the AGT kernel denies are not "unlikely." They are **structurally impossible**. That is the difference between asking an agent to behave and making it incapable of misbehaving.

**Prerequisites:** Python 3.10+

`pip install agent-governance-toolkit[full]`

Govern any tool function in two lines:

```
from agentmesh.governance import govern
safe_tool = govern(my_tool, policy="policy.yaml") # every call checked, logged, enforced
```

That's it. `safe_tool`

evaluates your YAML policy on every call, logs the decision, and raises `GovernanceDenied`

if the action is blocked.

```
# policy.yaml
apiVersion: governance.toolkit/v1
name: production-policy
default_action: allow
rules:
- name: block-destructive
condition: "action.type in ['drop', 'delete', 'truncate']"
action: deny
description: "Destructive operations require human approval"
- name: require-approval-for-send
condition: "action.type == 'send_email'"
action: require_approval
approvers: ["security-team"]
```

```
>>> safe_tool(action="read", table="users")
{'table': 'users', 'rows': 42}
>>> safe_tool(action="drop", table="users")
GovernanceDenied: Action denied by policy rule 'block-destructive':
Destructive operations require human approval
```

Or use the full `PolicyEvaluator`

API for programmatic control:

**PolicyEvaluator example**

```
from agent_os.policies import (
PolicyEvaluator, PolicyDocument, PolicyRule,
PolicyCondition, PolicyAction, PolicyOperator, PolicyDefaults
)
evaluator = PolicyEvaluator(policies=[PolicyDocument(
name="my-policy", version="1.0",
defaults=PolicyDefaults(action=PolicyAction.ALLOW),
rules=[PolicyRule(
name="block-dangerous-tools",
condition=PolicyCondition(
field="tool_name",
operator=PolicyOperator.IN,
value=["execute_code", "delete_file"]
),
action=PolicyAction.DENY, priority=100,
)],
)])
result = evaluator.evaluate({"tool_name": "web_search"}) # Allowed
result = evaluator.evaluate({"tool_name": "delete_file"}) # Blocked
```

**TypeScript / .NET / Rust / Go examples**

**TypeScript**

```
import { PolicyEngine } from "@microsoft/agent-governance-sdk";
const engine = new PolicyEngine([
{ action: "web_search", effect: "allow" },
{ action: "shell_exec", effect: "deny" },
]);
engine.evaluate("web_search"); // "allow"
engine.evaluate("shell_exec"); // "deny"
```

**.NET**

```
using AgentGovernance;
using AgentGovernance.Extensions.ModelContextProtocol;
using AgentGovernance.Policy;
var kernel = new GovernanceKernel(new GovernanceOptions
{
PolicyPaths = new() { "policies/default.yaml" },
});
var result = kernel.EvaluateToolCall("did:mesh:agent-1", "web_search",
new() { ["query"] = "latest AI news" });
// MCP server integration
builder.Services.AddMcpServer()
.WithGovernance(options => options.PolicyPaths.Add("policies/mcp.yaml"));
```

**Rust**

```
use agent_governance::{AgentMeshClient, ClientOptions};
let client = AgentMeshClient::new("my-agent").unwrap();
let result = client.execute_with_governance("data.read", None);
assert!(result.allowed);
```

**Go**

```
import agentmesh "github.com/microsoft/agent-governance-toolkit/agent-governance-golang"
client, _ := agentmesh.NewClient("my-agent",
agentmesh.WithPolicyRules([]agentmesh.PolicyRule{
{Action: "data.read", Effect: agentmesh.Allow},
{Action: "*", Effect: agentmesh.Deny},
}),
)
result := client.ExecuteWithGovernance("data.read", nil)
```

CLI tools:

```
agt doctor # check installation
agt verify # OWASP compliance check
agt verify --evidence ./agt-evidence.json --strict # fail CI on weak evidence
agt red-team scan ./prompts/ --min-grade B # prompt injection audit
agt lint-policy policies/ # validate policy files
```

Full walkthrough: [quickstart.md](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/quickstart.md) -- zero to governed agents in 5 minutes.
🌍 Also in: [日本語](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/i18n/quickstart.ja.md) | [简体中文](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/i18n/quickstart.zh-CN.md) | [한국어](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/i18n/quickstart.ko.md)

```
Agent ──► Policy Engine ──► Identity ──► Audit Log
(YAML/OPA/Cedar) (SPIFFE/DID/mTLS) (Tamper-evident)
│ │
├── Allowed ──► Tool executes │
└── Denied ──► GovernanceDenied │
▼
Decision Record
```


Every layer is optional. Start with `govern()`

and add layers as your risk profile grows. Most teams run policy enforcement + audit logging and never need the full stack.

| Package | Description |
|---|---|
Agent OS |

**Agent Mesh****Agent Runtime****Agent SRE****Agent Compliance****Agent Marketplace****Agent Lightning****Agent Hypervisor**| Capability | Description |
|---|---|
MCP Security Gateway |
Tool poisoning detection, drift monitoring, typosquatting, hidden instruction scanning (
|

**Shadow AI Discovery**[Discovery](https://github.com/microsoft/agent-governance-toolkit/blob/main/agent-governance-python/agent-discovery))**Governance Dashboard**[Dashboard](https://github.com/microsoft/agent-governance-toolkit/blob/main/examples/demos/governance-dashboard))**PromptDefense Evaluator**[Evaluator](https://github.com/microsoft/agent-governance-toolkit/blob/main/agent-governance-python/agent-compliance/src/agent_compliance/prompt_defense.py))**Contributor Reputation**[Action](https://github.com/microsoft/agent-governance-toolkit/blob/main/.github/actions/contributor-check))| Language | Package | Command |
|---|---|---|
Python |
`agent-governance-toolkit` |

`pip install agent-governance-toolkit[full]`

**TypeScript**`@microsoft/agent-governance-sdk`

`npm install @microsoft/agent-governance-sdk`

**Copilot CLI**`@microsoft/agent-governance-copilot-cli`

`npx @microsoft/agent-governance-copilot-cli install`

**Claude Code**`@microsoft/agent-governance-claude-code`

`claude --plugin-dir ./agent-governance-claude-code`

**.NET**`Microsoft.AgentGovernance`

`dotnet add package Microsoft.AgentGovernance`

**.NET MCP**`Microsoft.AgentGovernance.Extensions.ModelContextProtocol`

`dotnet add package Microsoft.AgentGovernance.Extensions.ModelContextProtocol`

**Rust**`agent-governance`

`cargo add agent-governance`

**Go**`agent-governance-toolkit`

`go get github.com/microsoft/agent-governance-toolkit/agent-governance-golang`

All five language SDKs implement core governance (policy, identity, trust, audit). Python has the full stack. Copilot CLI and Claude Code are first-party developer surfaces built on the TypeScript SDK.
See ** Language Package Matrix** for detailed per-language coverage.

**Individual Python packages**

| Package | PyPI | Description |
|---|---|---|
| Agent OS |
`agent-os-kernel` |

`agentmesh-platform`

`agentmesh-runtime`

`agent-sre`

`agent-governance-toolkit`

`agent-discovery`

`agent-hypervisor`

`agentmesh-marketplace`

`agentmesh-lightning`

**Python**: 3.10+**Node.js**: 18+ / npm 9+ (TypeScript SDK)**.NET**: 8+**Go**: 1.25+**Rust**: 1.70+**Optional**:`AZURE_CLIENT_ID`

,`AZURE_TENANT_ID`

,`AZURE_CLIENT_SECRET`

for Azure-integrated features

| Framework | Integration |
|---|---|
Microsoft Agent Framework |

**Semantic Kernel**[AutoGen](https://github.com/microsoft/autogen)[LangGraph](https://github.com/langchain-ai/langgraph)/[LangChain](https://github.com/langchain-ai/langchain)[CrewAI](https://github.com/crewAIInc/crewAI)[OpenAI Agents SDK](https://github.com/openai/openai-agents-python)[Google ADK](https://github.com/google/adk-python)[LlamaIndex](https://github.com/run-llama/llama_index)[Haystack](https://github.com/deepset-ai/haystack)[Mastra](https://github.com/mastra-ai/mastra)[Dify](https://github.com/langgenius/dify)[Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/)Full list: [Framework Integrations](https://github.com/microsoft/agent-governance-toolkit/blob/main/agent-governance-python/agentmesh-integrations) · [Quickstart Examples](https://github.com/microsoft/agent-governance-toolkit/blob/main/examples/quickstart)

| Example | Framework | What it demonstrates |
|---|---|---|
|

[crewai-governed](https://github.com/microsoft/agent-governance-toolkit/blob/main/examples/crewai-governed)[smolagents-governed](https://github.com/microsoft/agent-governance-toolkit/blob/main/examples/smolagents-governed)[maf-integration](https://github.com/microsoft/agent-governance-toolkit/blob/main/examples/maf-integration)[mcp-trust-verified-server](https://github.com/microsoft/agent-governance-toolkit/blob/main/examples/mcp-trust-verified-server)[cedarling-governed](https://github.com/microsoft/agent-governance-toolkit/blob/main/examples/cedarling-governed)[governance-dashboard](https://github.com/microsoft/agent-governance-toolkit/blob/main/examples/demos/governance-dashboard)Every major component has a formal RFC 2119 specification with conformance tests. These specs define the behavioral contract: what implementations MUST, SHOULD, and MAY do.

| Specification | Scope | Tests |
|---|---|---|
|

[AgentMesh Identity and Trust](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/specs/AGENTMESH-IDENTITY-TRUST-1.0.md)[Agent Hypervisor Execution Control](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/specs/AGENT-HYPERVISOR-EXECUTION-CONTROL-1.0.md)[AgentMesh Trust and Coordination](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/specs/AGENTMESH-TRUST-COORDINATION-1.0.md)[Agent SRE Governance](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/specs/AGENT-SRE-GOVERNANCE-1.0.md)[MCP Security Gateway](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/specs/MCP-SECURITY-GATEWAY-1.0.md)[Agent Lightning Fast-Path](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/specs/AGENT-LIGHTNING-FAST-PATH-1.0.md)[Framework Adapter Contract](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/specs/FRAMEWORK-ADAPTER-CONTRACT-1.0.md)[Audit and Compliance](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/specs/AUDIT-COMPLIANCE-1.0.md)[AgentMesh Wire Protocol](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/specs/AGENTMESH-WIRE-1.0.md)**992 conformance tests** ensure code stays aligned to specs. [25 Architecture Decision Records](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/adr) document why.

| Standard | Coverage |
|---|---|
|

[NIST AI RMF 1.0](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/compliance/nist-ai-rmf-alignment.md)[EU AI Act](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/compliance)[SOC 2](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/compliance/soc2-mapping.md)AGT enforces governance at the application middleware layer, not at the OS kernel level. The policy engine and agents share the same process boundary.

**Production recommendation:** Run each agent in a separate container for OS-level isolation. See [Architecture: Security Boundaries](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/ARCHITECTURE.md).

| Tool | Coverage |
|---|---|
| CodeQL | Python + TypeScript SAST |
| Gitleaks | Secret scanning on PR/push/weekly |
| ClusterFuzzLite | 7 fuzz targets (policy, injection, MCP, sandbox, trust) |
| Dependabot | 13 ecosystems |
| OpenSSF Scorecard | Weekly scoring + SARIF upload |

See [Known Limitations](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/LIMITATIONS.md) for honest design boundaries and recommended layered defense.

| Category | Links |
|---|---|
Getting Started |
|

**Architecture**[System Design](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/ARCHITECTURE.md)·[Threat Model](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/security/threat-model.md)·[ADRs](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/adr)(25)**Specifications**[All Specs](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/specs)(10 formal specs, 992 conformance tests)**API Reference**[Agent OS](https://github.com/microsoft/agent-governance-toolkit/blob/main/agent-governance-python/agent-os/README.md)·[AgentMesh](https://github.com/microsoft/agent-governance-toolkit/blob/main/agent-governance-python/agent-mesh/README.md)·[Agent SRE](https://github.com/microsoft/agent-governance-toolkit/blob/main/agent-governance-python/agent-sre/README.md)**Compliance**[OWASP](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/compliance/owasp-agentic-top10-architecture.md)·[EU AI Act](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/compliance)·[NIST AI RMF](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/compliance/nist-ai-rmf-alignment.md)·[SOC 2](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/compliance/soc2-mapping.md)**Deployment**[Azure](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/deployment/README.md)·[AWS](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/deployment/README.md)·[GCP](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/deployment/README.md)·[Docker Compose](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/deployment/README.md)**Extensions**[VS Code](https://github.com/microsoft/agent-governance-toolkit/blob/main/agent-governance-typescript/agent-os-vscode)·[Framework Integrations](https://github.com/microsoft/agent-governance-toolkit/blob/main/agent-governance-python/agentmesh-integrations)[Contributing Guide](https://github.com/microsoft/agent-governance-toolkit/blob/main/CONTRIBUTING.md) · [Community](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/COMMUNITY.md) · [Security Policy](https://github.com/microsoft/agent-governance-toolkit/blob/main/SECURITY.md) · [Changelog](https://github.com/microsoft/agent-governance-toolkit/blob/main/CHANGELOG.md)

**Using AGT?** Add your organization to [ADOPTERS.md](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/ADOPTERS.md).

| Document | Purpose |
|---|---|
|

[CHARTER.md](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/CHARTER.md)[MAINTAINERS.md](https://github.com/microsoft/agent-governance-toolkit/blob/main/MAINTAINERS.md)[SECURITY.md](https://github.com/microsoft/agent-governance-toolkit/blob/main/SECURITY.md)[CODE_OF_CONDUCT.md](https://github.com/microsoft/agent-governance-toolkit/blob/main/CODE_OF_CONDUCT.md)[ANTITRUST.md](https://github.com/microsoft/agent-governance-toolkit/blob/main/ANTITRUST.md)[TRADEMARKS.md](https://github.com/microsoft/agent-governance-toolkit/blob/main/TRADEMARKS.md)If you use the Agent Governance Toolkit to build applications that operate with third-party agent frameworks or services, you do so at your own risk. We recommend reviewing all data being shared with third-party services and being cognizant of third-party practices for retention and location of data.

This project is licensed under the [MIT License](https://github.com/microsoft/agent-governance-toolkit/blob/main/LICENSE).

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
