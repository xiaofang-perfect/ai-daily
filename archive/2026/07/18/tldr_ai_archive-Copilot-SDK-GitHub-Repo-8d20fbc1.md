---
title: "Copilot SDK (GitHub Repo)"
source: TLDR AI · 2026-07-17
url: https://github.com/github/copilot-sdk?utm_source=tldrai
date: 2026-07-18
published_at: 2026-07-17T12:00:00+00:00
tag: 工具开源
item_id: 8d20fbc1d1af483b
---
![GitHub Copilot SDK](https://github.com/github/copilot-sdk/raw/main/assets/RepoHeader_01.png)







Agents for every app.

Embed Copilot's agentic workflows in your application with the GitHub Copilot SDK for Python, TypeScript, Go, .NET, Java, and Rust.

The GitHub Copilot SDK exposes the same engine behind Copilot CLI: a production-tested agent runtime you can invoke programmatically. No need to build your own orchestration—you define agent behavior, Copilot handles planning, tool invocation, file edits, and more.

| SDK | Location | Cookbook | Installation | API docs | 
|---|---|---|---|---|
| Node.js / TypeScript | `nodejs/` | [Cookbook](https://github.com/github/awesome-copilot/blob/main/cookbook/copilot-sdk/nodejs/README.md) | `npm install @github/copilot-sdk` | |
| Python | `python/` | [Cookbook](https://github.com/github/awesome-copilot/blob/main/cookbook/copilot-sdk/python/README.md) | `pip install github-copilot-sdk` | |
| Go | `go/` | [Cookbook](https://github.com/github/awesome-copilot/blob/main/cookbook/copilot-sdk/go/README.md) | `go get github.com/github/copilot-sdk/go` | [API docs](https://pkg.go.dev/github.com/github/copilot-sdk/go) | 
| .NET | `dotnet/` | [Cookbook](https://github.com/github/awesome-copilot/blob/main/cookbook/copilot-sdk/dotnet/README.md) | `dotnet add package GitHub.Copilot.SDK` | |
| Rust | `rust/` | — | `cargo add github-copilot-sdk` | [API docs](https://docs.rs/github-copilot-sdk/latest/github_copilot_sdk/) | 
| Java | `java/` | [Cookbook](https://github.com/github/awesome-copilot/blob/main/cookbook/copilot-sdk/java/README.md) | Maven coordinates `com.github:copilot-sdk-java`See instructions for [Maven](https://github.com/github/copilot-sdk/blob/main/java/README.md#maven)and[Gradle](https://github.com/github/copilot-sdk/blob/main/java/README.md#gradle) | [API docs](https://javadoc.io/doc/com.github/copilot-sdk-java/latest/) | 

See the individual SDK READMEs for installation, usage examples, and API reference.

For a complete walkthrough, see the ** Getting Started Guide**.

Quick steps:

- **(Optional) Install the Copilot CLI**

For Node.js, Python, and .NET SDKs, the Copilot CLI is bundled automatically and no separate installation is required.
For Go, Java, and Rust, [install the CLI manually](https://github.com/features/copilot/cli) or ensure `copilot` is available in your PATH. Go and Rust also expose application-level CLI bundling features.

- 
**Install your preferred SDK**using the commands above.
- 
**See the SDK README**for usage examples and API documentation.

All SDKs communicate with the Copilot CLI server via JSON-RPC:

```
Your Application
       ↓
  SDK Client
       ↓ JSON-RPC
  Copilot CLI (server mode)
```
The SDK manages the CLI process lifecycle automatically. You can also connect to an external CLI server—see the [Getting Started Guide](https://github.com/github/copilot-sdk/blob/main/docs/getting-started.md#connecting-to-an-external-cli-server) for details on running the CLI in server mode.

Yes, a GitHub Copilot subscription is required to use the GitHub Copilot SDK, **unless you are using BYOK (Bring Your Own Key)**. With BYOK, you can use the SDK without GitHub authentication by configuring your own API keys from supported LLM providers. For standard usage (non-BYOK), refer to the [GitHub Copilot pricing page](https://github.com/features/copilot#pricing), which includes a free tier with limited usage.

Billing for the GitHub Copilot SDK is based on the same model as the Copilot CLI, with each prompt being counted towards your usage allowance. For more information on Copilot usage billing, see [Usage in GitHub Copilot](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing).

Yes, the GitHub Copilot SDK supports BYOK (Bring Your Own Key). You can configure the SDK to use your own API keys from supported LLM providers (e.g. OpenAI, Azure AI Foundry, Anthropic) to access models through those providers. See the ** BYOK documentation** for setup instructions and examples.

**Note:** BYOK uses key-based authentication only. Microsoft Entra ID (Azure AD), managed identities, and third-party identity providers are not supported.

The SDK supports multiple authentication methods:

- **GitHub signed-in user**- Uses stored OAuth credentials from- `copilot`CLI login
- **OAuth GitHub App**- Pass user tokens from your GitHub OAuth app
- **Environment variables**-- `COPILOT_GITHUB_TOKEN`,- `GH_TOKEN`,- `GITHUB_TOKEN`
- **BYOK**- Use your own API keys (no GitHub auth required)

See the ** Authentication documentation** for details on each method.

No — for Node.js, Python, and .NET SDKs, the Copilot CLI is bundled automatically as a dependency. You do not need to install it separately.

For Go, Java, and Rust SDKs, the CLI is **not** bundled by default. Install the CLI manually or ensure `copilot` is available in your PATH. Go and Rust also expose application-level CLI bundling features.

Advanced: You can override the CLI binary or connect to an external server. See the individual SDK README for language-specific options.

By default, the SDK exposes the Copilot CLI's first-party tools, similar to running the CLI with `--allow-all`. Tool execution is still governed by each SDK's permission handler, so applications can approve, deny, or customize tool calls. You can customize tool availability by configuring the SDK client options to enable and disable specific tools. Refer to the individual SDK documentation for details on tool configuration and to the Copilot CLI documentation for the list of available tools.

Yes, the GitHub Copilot SDK allows you to define custom agents, skills, and tools. You can extend the functionality of the agents by implementing your own logic and integrating additional tools as needed. Refer to the SDK documentation of your preferred language for more details.

Yes, check out the custom instructions and SDK-specific guidance:

All models available via Copilot CLI are supported in the SDK. The SDK also exposes a method which will return the models available so they can be accessed at runtime.

The GitHub Copilot SDK is generally available and follows semantic versioning. See [CHANGELOG.md](https://github.com/github/copilot-sdk/blob/main/CHANGELOG.md) for release notes.

Please use the [GitHub Issues](https://github.com/github/copilot-sdk/issues) page to report bugs or request new features. We welcome your feedback to help improve the SDK.

- [Documentation](https://github.com/github/copilot-sdk/blob/main/docs/README.md)
- [Getting Started](https://github.com/github/copilot-sdk/blob/main/docs/getting-started.md)
- [Setup Guides](https://github.com/github/copilot-sdk/blob/main/docs/setup/README.md)
- [Authentication](https://github.com/github/copilot-sdk/blob/main/docs/auth/README.md)
- [Features](https://github.com/github/copilot-sdk/blob/main/docs/features/README.md)
- [Troubleshooting](https://github.com/github/copilot-sdk/blob/main/docs/troubleshooting/debugging.md)
- [Cookbook](https://github.com/github/awesome-copilot/blob/main/cookbook/copilot-sdk)
- [More Resources](https://github.com/github/awesome-copilot/blob/main/collections/copilot-sdk.md)

| SDK | Location | 
|---|---|
| Clojure | [copilot-community-sdk/copilot-sdk-clojure](https://github.com/copilot-community-sdk/copilot-sdk-clojure) | 
| C++ | [0xeb/copilot-sdk-cpp](https://github.com/0xeb/copilot-sdk-cpp) | 

See [CONTRIBUTING.md](https://github.com/github/copilot-sdk/blob/main/CONTRIBUTING.md) for contribution guidelines.

MIT
