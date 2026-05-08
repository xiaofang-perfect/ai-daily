---
title: "LearningCircuit/local-deep-research"
source: GitHub Trending
url: https://github.com/LearningCircuit/local-deep-research
date: 2026-05-08
published_at: 2026-05-08T04:51:58.907740+00:00
tag: 工具开源
item_id: 6e257ad3be07c835
---
**AI-powered research assistant for deep, agentic research**

*Performs deep, agentic research using multiple LLMs and search engines with proper citations*

▶️ Watch Review by The Art Of The Terminal

AI research assistant you control. Run locally for privacy, use any LLM and build your own searchable knowledge base. You own your data and see exactly how it works.

**Option 1: Docker Run (Linux)**

```
# Step 1: Pull and run Ollama
docker run -d -p 11434:11434 --name ollama ollama/ollama
docker exec ollama ollama pull gpt-oss:20b
# Step 2: Pull and run SearXNG for optimal search results
docker run -d -p 8080:8080 --name searxng searxng/searxng
# Step 3: Pull and run Local Deep Research
docker run -d -p 5000:5000 --network host \
--name local-deep-research \
--volume "deep-research:/data" \
-e LDR_DATA_DIR=/data \
localdeepresearch/local-deep-research
```

**Option 2: Docker Compose**

CPU-only (all platforms):

`curl -O https://raw.githubusercontent.com/LearningCircuit/local-deep-research/main/docker-compose.yml && docker compose up -d`

With NVIDIA GPU (Linux):

```
curl -O https://raw.githubusercontent.com/LearningCircuit/local-deep-research/main/docker-compose.yml && \
curl -O https://raw.githubusercontent.com/LearningCircuit/local-deep-research/main/docker-compose.gpu.override.yml && \
docker compose -f docker-compose.yml -f docker-compose.gpu.override.yml up -d
```

Open [http://localhost:5000](http://localhost:5000) after ~30 seconds. For GPU setup, environment variables, and more, see the [Docker Compose Guide](https://github.com/LearningCircuit/local-deep-research/blob/main/docs/docker-compose-guide.md).

**Option 3: pip install**

`pip install local-deep-research`

Works on Windows, macOS, and Linux. SQLCipher encryption is included via pre-built wheels — no compilation needed. PDF export on Windows requires Pango (

[setup guide]). If you encounter issues with encryption, set`export LDR_BOOTSTRAP_ALLOW_UNENCRYPTED=true`

to use standard SQLite instead.

You ask a complex question. LDR:

- Does the research for you automatically
- Searches across web, academic papers, and your own documents
- Synthesizes everything into a report with proper citations

Choose from 20+ research strategies for quick facts, deep analysis, or academic research.

**New: LangGraph Agent Strategy** — An autonomous agentic research mode where the LLM decides what to search, which specialized engines to use (arXiv, PubMed, Semantic Scholar, etc.), and when to synthesize. Early results are promising — it adaptively switches between search engines based on what it finds and collects significantly more sources than pipeline-based strategies. Select `langgraph-agent`

in Settings to try it.

```
flowchart LR
R[Research] --> D[Download Sources]
D --> L[(Library)]
L --> I[Index & Embed]
I --> S[Search Your Docs]
S -.-> R
```

Every research session finds valuable sources. Download them directly into your encrypted library—academic papers from ArXiv, PubMed articles, web pages. LDR extracts text, indexes everything, and makes it searchable. Next time you research, ask questions across your own documents and the live web together. Your knowledge compounds over time.

```
flowchart LR
U1[User A] --> D1[(Encrypted DB)]
U2[User B] --> D2[(Encrypted DB)]
```

Your data stays yours. Each user gets their own isolated SQLCipher database encrypted with AES-256 (Signal-level security). No password recovery means true zero-knowledge—even server admins can't read your data. Run fully local with Ollama + SearXNG and nothing ever leaves your machine.

**In-memory credentials**: Like all applications that use secrets at runtime — including [password managers](https://www.ise.io/casestudies/password-manager-hacking/), browsers, and API clients — credentials are held in plain text in process memory during active sessions. This is an [industry-wide accepted reality](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html), not specific to LDR: if an attacker can read process memory, they can also read any in-process decryption key. We mitigate this with session-scoped credential lifetimes and core dump exclusion. Ideas for further improvements are always welcome via [GitHub Issues](https://github.com/LearningCircuit/local-deep-research/issues). See our [Security Policy](https://github.com/LearningCircuit/local-deep-research/blob/main/SECURITY.md) for details.

**Supply Chain Security**: Docker images are signed with [Cosign](https://github.com/sigstore/cosign), include SLSA provenance attestations, and attach SBOMs. Verify with:

`cosign verify localdeepresearch/local-deep-research:latest`

**Security Transparency**: Scanner suppressions are documented with justifications in [Security Alerts Assessment](https://github.com/LearningCircuit/local-deep-research/blob/main/.github/SECURITY_ALERTS.md), [Scorecard Compliance](https://github.com/LearningCircuit/local-deep-research/blob/main/.github/SECURITY_SCORECARD.md), [Container CVE Suppressions](https://github.com/LearningCircuit/local-deep-research/blob/main/.trivyignore), and [SAST Rule Rationale](https://github.com/LearningCircuit/local-deep-research/blob/main/bearer.yml). Some alerts (Dependabot, code scanning) can only be dismissed or are very difficult to suppress outside the [GitHub Security tab](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/viewing-and-updating-dependabot-alerts), so the files above do not cover every dismissed finding.

[Detailed Architecture →](https://github.com/LearningCircuit/local-deep-research/blob/main/docs/architecture.md) | [Security Policy →](https://github.com/LearningCircuit/local-deep-research/blob/main/SECURITY.md) | [Security Review Process →](https://github.com/LearningCircuit/local-deep-research/blob/main/docs/SECURITY_REVIEW_PROCESS.md)

Local Deep Research contains **no telemetry, no analytics, and no tracking**. We do not collect, transmit, or store any data about you or your usage. No analytics SDKs, no phone-home calls, no crash reporting, no external scripts. Usage metrics stay in your local encrypted database.

The only network calls LDR makes are ones **you** initiate: search queries (to engines you configure), LLM API calls (to your chosen provider), and notifications (only if you set up Apprise).

Since we don't collect any usage data, we rely on you to tell us what works, what's broken, and what you'd like to see next — [bug reports](https://github.com/LearningCircuit/local-deep-research/issues), feature ideas, and even which features you love or never use all help us improve LDR.

**~95% accuracy on SimpleQA benchmark** (preliminary results)

- Tested with GPT-4.1-mini + SearXNG + focused-iteration strategy
- Comparable to state-of-the-art AI research systems
- Local models can achieve similar performance with proper configuration

Not sure which local model to run with LDR? The community-maintained ** LDR Benchmarks dataset on Hugging Face** tracks accuracy across models, search engines, and research strategies — it's the fastest way to see which Ollama / LM Studio / llama.cpp models actually work well for deep research before you download multi-GB weights.

**Quick Summary**- Get answers in 30 seconds to 3 minutes with citations**Detailed Research**- Comprehensive analysis with structured findings**Report Generation**- Professional reports with sections and table of contents**Document Analysis**- Search your private documents with AI

- Use any vector store as a search engine[LangChain Integration](https://github.com/LearningCircuit/local-deep-research/blob/main/docs/LANGCHAIN_RETRIEVER_INTEGRATION.md)- Authenticated HTTP access with per-user databases[REST API](https://github.com/LearningCircuit/local-deep-research/blob/main/docs/api-quickstart.md)- Test and optimize your configuration[Benchmarking](https://github.com/LearningCircuit/local-deep-research/blob/main/docs/BENCHMARKING.md)- Track costs, performance, and usage metrics[Analytics Dashboard](https://github.com/LearningCircuit/local-deep-research/blob/main/docs/analytics-dashboard.md)- Automatic journal reputation scoring with 212K+ indexed sources, predatory detection, and quality dashboard. Powered by[Journal Quality System](https://github.com/LearningCircuit/local-deep-research/blob/main/docs/journal-quality.md)[OpenAlex](https://openalex.org)(CC0),[DOAJ](https://doaj.org)(CC0), and[Stop Predatory Journals](https://predatoryjournals.org)(MIT).**Real-time Updates**- WebSocket support for live research progress**Export Options**- Download results as PDF or Markdown**Research History**- Save, search, and revisit past research**Adaptive Rate Limiting**- Intelligent retry system that learns optimal wait times**Keyboard Shortcuts**- Navigate efficiently (ESC, Ctrl+Shift+1-5)**Per-User Encrypted Databases**- Secure, isolated data storage for each user

**Automated Research Digests**- Subscribe to topics and receive AI-powered research summaries**Customizable Frequency**- Daily, weekly, or custom schedules for research updates**Smart Filtering**- AI filters and summarizes only the most relevant developments**Multi-format Delivery**- Get updates as markdown reports or structured summaries**Topic & Query Support**- Track specific searches or broad research areas

**Academic**: arXiv, PubMed, Semantic Scholar**General**: Wikipedia, SearXNG**Technical**: GitHub, Elasticsearch**Historical**: Wayback Machine**News**: The Guardian, Wikinews

**Tavily**- AI-powered search**Google**- Via SerpAPI or Programmable Search Engine**Brave Search**- Privacy-focused web search

**Local Documents**- Search your files with AI**LangChain Retrievers**- Any vector store or database**Meta Search**- Combine multiple engines intelligently

LDR respects `robots.txt`

and identifies itself honestly when fetching web pages — no stealth or anti-detection techniques. In rare cases this means a page that blocks automated access won't be fetched, which we consider the right trade-off.

For most users, the [Quick Start](https://github.com#-quick-start) above is all you need.

| Method | Best for | Guide |
|---|---|---|
| Docker Compose | Most users (recommended) |
|

[Installation Guide](https://github.com/LearningCircuit/local-deep-research/blob/main/docs/installation.md#docker)[pip Guide](https://github.com/LearningCircuit/local-deep-research/blob/main/docs/install-pip.md)[Unraid Guide](https://github.com/LearningCircuit/local-deep-research/blob/main/docs/deployment/unraid.md)```
from local_deep_research.api import LDRClient, quick_query
# Option 1: Simplest - one line research
summary = quick_query("username", "password", "What is quantum computing?")
print(summary)
# Option 2: Client for multiple operations
client = LDRClient()
client.login("username", "password")
result = client.quick_research("What are the latest advances in quantum computing?")
print(result["summary"])
```

*The code example below shows the basic API structure - for working examples, see the link below*

```
import requests
from bs4 import BeautifulSoup
# Create session and authenticate
session = requests.Session()
login_page = session.get("http://localhost:5000/auth/login")
soup = BeautifulSoup(login_page.text, "html.parser")
login_csrf = soup.find("input", {"name": "csrf_token"}).get("value")
# Login and get API CSRF token
session.post("http://localhost:5000/auth/login",
data={"username": "user", "password": "pass", "csrf_token": login_csrf})
csrf = session.get("http://localhost:5000/auth/csrf-token").json()["csrf_token"]
# Make API request
response = session.post("http://localhost:5000/api/start_research",
json={"query": "Your research question"},
headers={"X-CSRF-Token": csrf})
```

🚀 [Ready-to-use HTTP API Examples → examples/api_usage/http/](https://github.com/LearningCircuit/local-deep-research/blob/main/examples/api_usage/http)

- ✅
**Automatic user creation**- works out of the box - ✅
**Complete authentication**with CSRF handling - ✅
**Result retry logic**- waits until research completes - ✅
**Progress monitoring**and error handling

```
# Run benchmarks from CLI
python -m local_deep_research.benchmarks --dataset simpleqa --examples 50
# Manage rate limiting
python -m local_deep_research.web_search_engines.rate_limiting status
python -m local_deep_research.web_search_engines.rate_limiting reset
```

Connect LDR to your existing knowledge base:

```
from local_deep_research.api import quick_summary
# Use your existing LangChain retriever
result = quick_summary(
query="What are our deployment procedures?",
retrievers={"company_kb": your_retriever},
search_tool="company_kb"
)
```

Works with: FAISS, Chroma, Pinecone, Weaviate, Elasticsearch, and any LangChain-compatible retriever.

LDR provides an MCP (Model Context Protocol) server that allows AI assistants like Claude Desktop and Claude Code to perform deep research.


⚠️ Security Note: This MCP server is designed forlocal use onlyvia STDIO transport (e.g., Claude Desktop). It has no built-in authentication or rate limiting. Do not expose over a network without implementing proper security controls. See the[MCP Security Guide]for network deployment requirements.

```
# Install with MCP extras
pip install "local-deep-research[mcp]"
```

Add to your `claude_desktop_config.json`

:

```
{
"mcpServers": {
"local-deep-research": {
"command": "ldr-mcp",
"env": {
"LDR_LLM_PROVIDER": "openai",
"LDR_LLM_OPENAI_API_KEY": "sk-..."
}
}
}
}
```

Add to your `.mcp.json`

(project-level) or `~/.claude/mcp.json`

(global):

```
{
"mcpServers": {
"local-deep-research": {
"command": "ldr-mcp",
"env": {
"LDR_LLM_PROVIDER": "ollama",
"LDR_LLM_OLLAMA_URL": "http://localhost:11434"
}
}
}
}
```

| Tool | Description | Duration | LLM Cost |
|---|---|---|---|
`search` |
Raw results from a specific engine (arxiv, pubmed, wikipedia, ...) | 5-30s | None |
`quick_research` |
Fast research summary | 1-5 min | Yes |
`detailed_research` |
Comprehensive analysis | 5-15 min | Yes |
`generate_report` |
Full markdown report | 10-30 min | Yes |
`analyze_documents` |
Search local collections | 30s-2 min | Yes |
`list_search_engines` |
List available search engines | instant | None |
`list_strategies` |
List research strategies | instant | None |
`get_configuration` |
Get current config | instant | None |

The `search`

tool lets you query specific search engines directly and get raw results (title, link, snippet) — no LLM processing, no cost, fast. This is especially useful for **monitoring and subscriptions** where you want to check for new content regularly without burning LLM tokens.

```
# Search arXiv for recent papers
search(query="transformer architecture improvements", engine="arxiv")
# Search PubMed for medical literature
search(query="CRISPR clinical trials 2024", engine="pubmed")
# Search Wikipedia for quick facts
search(query="quantum error correction", engine="wikipedia")
# Search OpenClaw for legal case law
search(query="copyright fair use precedents", engine="openclaw")
# Use list_search_engines() to see all available engines
```


```
"Use quick_research to find information about quantum computing applications"
"Search arxiv for recent papers on diffusion models"
"Generate a detailed research report on renewable energy trends"
```


Early experiments on small SimpleQA dataset samples:

| Configuration | Accuracy | Notes |
|---|---|---|
| gpt-4.1-mini + SearXNG + focused_iteration | 90-95% | Limited sample size |
| gpt-4.1-mini + Tavily + focused_iteration | 90-95% | Limited sample size |
| gemini-2.0-flash-001 + SearXNG | 82% | Single test run |

Note: These are preliminary results from initial testing. Performance varies significantly based on query types, model versions, and configurations. [Run your own benchmarks →](https://github.com/LearningCircuit/local-deep-research/blob/main/docs/BENCHMARKING.md)

**Full community leaderboard:** The community maintains a growing collection of benchmark results across models, strategies, and search engines in a dedicated repo with CI-validated submissions and auto-generated leaderboards:

— submit your results here[GitHub: LearningCircuit/ldr-benchmarks](https://github.com/LearningCircuit/ldr-benchmarks)— browse leaderboards and download CSVs[Hugging Face: local-deep-research/ldr-benchmarks](https://huggingface.co/datasets/local-deep-research/ldr-benchmarks)

Thanks to the community members who have contributed benchmark runs:

Track costs, performance, and usage with detailed metrics. [Learn more →](https://github.com/LearningCircuit/local-deep-research/blob/main/docs/analytics-dashboard.md)

**Ollama**— connect to its native API (default`http://localhost:11434`

)**LM Studio**— connect to its OpenAI-compatible server (default`http://localhost:1234/v1`

)**llama.cpp**— connect to`llama-server`

's OpenAI-compatible endpoint (default`http://localhost:8080/v1`

); start with`llama-server -m <model.gguf>`

- Common models: Llama 3, Mistral, Gemma, DeepSeek, Qwen
- LLM processing stays local (search queries still go to web). No API costs.

💡

Which local model should I pick?Check the— community-submitted accuracy numbers across local and cloud models, so you can compare before downloading. Also on[LDR Benchmarks dataset on Hugging Face][GitHub]if you want to submit your own runs.

- OpenAI (GPT-4, GPT-3.5)
- Anthropic (Claude 3)
- Google (Gemini)
- 100+ models via OpenRouter

Pre-1.7 installs auto-filled`llm.model`

no longer has a default.`gemma3:12b`

(Ollama) when no model was configured, which silently downloaded a multi-GB binary. The field is now empty by default — pick a model in Settings → LLM, or research will fail loudly with a clear error.**The**If you previously set`llamacpp`

provider now uses HTTP instead of in-process loading.`llm.llamacpp_model_path`

to a local`.gguf`

file, that setting is no longer read. Instead, run`llama-server -m <your-model.gguf>`

(it ships with every modern llama.cpp build) and the default`llm.llamacpp.url`

of`http://localhost:8080/v1`

will pick it up. Optional API key support is available via`llm.llamacpp.api_key`

if you put`llama-server`

behind an auth proxy.

[Installation Guide](https://github.com/LearningCircuit/local-deep-research/blob/main/docs/installation.md)[Frequently Asked Questions](https://github.com/LearningCircuit/local-deep-research/blob/main/docs/faq.md)[API Quickstart](https://github.com/LearningCircuit/local-deep-research/blob/main/docs/api-quickstart.md)[Configuration Guide](https://github.com/LearningCircuit/local-deep-research/blob/main/docs/env_configuration.md)[Full Configuration Reference](https://github.com/LearningCircuit/local-deep-research/blob/main/docs/CONFIGURATION.md)

"Local Deep Research

deserves special mentionfor those who prioritize privacy...tuned to use open-source LLMsthat can run on consumer GPUs or even CPUs. Journalists, researchers, or companies with sensitive topics can investigate informationwithout queries ever hitting an external server."

[Korben.info](https://korben.info/local-deep-research-alternative-gratuite-recherche-ia-sourcee.html)- French tech blog ("Sherlock Holmes numérique")[Roboto.fr](https://www.roboto.fr/blog/local-deep-research-l-alternative-open-source-gratuite-deep-research-d-openai)- "L'alternative open-source gratuite à Deep Research d'OpenAI"[KDJingPai AI Tools](https://www.kdjingpai.com/en/local-deep-research/)- AI productivity tools coverage[AI Sharing Circle](https://aisharenet.com/en/local-deep-research/)- AI resources coverage

[Hacker News](https://news.ycombinator.com/item?id=43330164)- 190+ points, community discussion[LangChain Twitter/X](https://x.com/LangChainAI/status/1901347759757902038)- Official LangChain promotion[LangChain LinkedIn](https://www.linkedin.com/posts/langchain_local-deep-research-an-ai-research-activity-7307113456095137792-cXRH)- 400+ likes

[Juejin (掘金)](https://juejin.cn/post/7481604667589885991)- Developer community[Cnblogs (博客园)](https://www.cnblogs.com/qife122/p/18955032)- Developer blogs[GitHubDaily (Twitter/X)](https://x.com/GitHub_Daily/status/1900169979313741846)- Influential tech account[Zhihu (知乎)](https://zhuanlan.zhihu.com/p/30886269290)- Tech community[A姐分享](https://www.ahhhhfs.com/68713/)- AI resources[CSDN](https://blog.csdn.net/gitblog_01198/article/details/147061415)- Installation guide[NetEase (网易)](https://www.163.com/dy/article/JQKAS50205567BLV.html)- Tech news portal

[note.com: 調査革命：Local Deep Research徹底活用法](https://note.com/r7038xx/n/nb3b74debbb30)- Comprehensive tutorial[Qiita: Local Deep Researchを試す](https://qiita.com/orca13/items/635f943287c45388d48f)- Docker setup guide[LangChainJP (Twitter/X)](https://x.com/LangChainJP/status/1902918110073807073)- Japanese LangChain community

[PyTorch Korea Forum](https://discuss.pytorch.kr/t/local-deep-research/6476)- Korean ML community[GeekNews (Hada.io)](https://news.hada.io/topic?id=19707)- Korean tech news

[BSAIL Lab: How useful is Deep Research in Academia?](https://uflbsail.net/uncategorized/how-useful-is-deep-research-in-academia/)- Academic review by contributor[@djpetti](https://github.com/djpetti)[The Art Of The Terminal: Use Local LLMs Already!](https://youtu.be/pfxgLX-MxMY?t=1999)- Comprehensive review of local AI tools, featuring LDR's research capabilities (embeddings now work!)

[SearXNG LDR-Academic](https://github.com/porespellar/searxng-LDR-academic)- Academic-focused SearXNG fork with 12 research engines (arXiv, Google Scholar, PubMed, etc.) designed for LDR[DeepWiki Documentation](https://deepwiki.com/LearningCircuit/local-deep-research)- Third-party documentation and guides


Note:Third-party projects and articles are independently maintained. We link to them as useful resources but cannot guarantee their code quality or security.

[Discord](https://discord.gg/ttcqQeFcJ3)- Get help and share research techniques[Reddit](https://www.reddit.com/r/LocalDeepResearch/)- Updates and showcases[GitHub Issues](https://github.com/LearningCircuit/local-deep-research/issues)- Bug reports

We welcome contributions of all sizes — from typo fixes to new features. The key rule: **keep PRs small and atomic** (one change per PR). For larger changes, please open an issue or start a discussion first — we want to protect your time and make sure your effort leads to a successful merge rather than a misaligned PR. See our [Contributing Guide](https://github.com/LearningCircuit/local-deep-research/blob/main/CONTRIBUTING.md) to get started.

Local Deep Research is built on the work of many open-access initiatives, academic databases, and open-source projects. We are grateful to:

| Source | What It Provides | License |
|---|---|---|
|

[DOAJ](https://doaj.org)[arXiv](https://arxiv.org)[PubMed / NCBI](https://pubmed.ncbi.nlm.nih.gov)[Semantic Scholar](https://www.semanticscholar.org)[Terms](https://www.semanticscholar.org/product/api/license)[NASA ADS](https://ui.adsabs.harvard.edu)[Terms](https://ui.adsabs.harvard.edu/help/terms/)[Zenodo](https://zenodo.org)[PubChem](https://pubchem.ncbi.nlm.nih.gov)[Stop Predatory Journals](https://predatoryjournals.org)[JabRef](https://github.com/JabRef/abbrv.jabref.org)[Wikipedia](https://www.wikipedia.org) • [OpenLibrary](https://openlibrary.org) • [Project Gutenberg](https://www.gutenberg.org) • [GitHub](https://github.com) • [Stack Exchange](https://stackexchange.com) • [The Guardian](https://www.theguardian.com) • [Wayback Machine](https://web.archive.org)

[LangChain](https://github.com/hwchase17/langchain) • [Ollama](https://ollama.ai) • [SearXNG](https://searxng.org/) • [FAISS](https://github.com/facebookresearch/faiss)

These projects run on donations and grants, not paywalls. If Local Deep Research is useful to you, consider giving back to the open-access ecosystem that makes it possible:

[arXiv](https://arxiv.org/about/give)— free preprints for physics, math, CS, and more[PubMed / NLM](https://www.nlm.nih.gov/pubs/donations/donations.html)— open biomedical literature[Wikipedia / Wikimedia](https://donate.wikimedia.org)— the free encyclopedia[Internet Archive](https://archive.org/donate)— the Wayback Machine and open digital library[DOAJ](https://doaj.org/support)— curating and verifying open-access journals worldwide[OpenAlex](https://openalex.org)— open scholarly metadata (sponsored by[OurResearch](https://ourresearch.org))[Project Gutenberg](https://www.gutenberg.org/donate/)— free ebooks since 1971

MIT License - see [LICENSE](https://github.com/LearningCircuit/local-deep-research/blob/main/LICENSE) file.

**Dependencies:** All third-party packages use permissive licenses (MIT, Apache-2.0, BSD, etc.) - see [allowlist](https://github.com/LearningCircuit/local-deep-research/blob/main/.github/workflows/dependency-review.yml#L50-L68)
