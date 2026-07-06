---
title: "alibaba/page-agent"
source: GitHub Trending
url: https://github.com/alibaba/page-agent
date: 2026-07-06
published_at: 2026-07-06T06:24:33.583374+00:00
tag: 工具开源
item_id: b9a82d497e2cecac
---
The GUI Agent Living in Your Webpage. Control web interfaces with natural language.

🌐 **English** | [中文](https://github.com/alibaba/page-agent/blob/main/docs/README-zh.md)

[ 🚀 Demo](https://alibaba.github.io/page-agent/) | 

[|](https://alibaba.github.io/page-agent/docs/introduction/overview)

**📖 Docs**[|](https://news.ycombinator.com/item?id=47264138)

**📢 HN Discussion**

**𝕏 Follow on X**## page-agent-demo-0227.mp4

- **🎯 Easy integration**- No need for `browser extension`/`python`/`headless browser`.
- Just in-page javascript. Everything happens in your web page.
 
- No need for 
- **📖 Text-based DOM manipulation**- No screenshots. No multi-modal LLMs or special permissions needed.
 
- **🧠 Bring your own LLMs**
- **🐙 Optional**- [chrome extension](https://alibaba.github.io/page-agent/docs/features/chrome-extension)for multi-page tasks.- And an [MCP Server (Beta)](https://alibaba.github.io/page-agent/docs/features/mcp-server)to control it from outside
 
- And an 

- **SaaS AI Copilot**— Ship an AI copilot in your product in lines of code. No backend rewrite.
- **Smart Form Filling**— Turn 20-click workflows into one sentence. Perfect for ERP, CRM, and admin systems.
- **Accessibility**— Make any web app accessible through natural language. Voice commands, screen readers, zero barrier.
- **Multi-page Agent**— Extend your own web agent's reach across browser tabs- [chrome extension](https://alibaba.github.io/page-agent/docs/features/chrome-extension).
- **MCP**- Allow your agent clients to control your browser.

Fastest way to try PageAgent with our free Demo LLM:

`<script src="{URL}" crossorigin="true"></script>`

This demo CDN uses our free⚠️ For technical evaluation only.[testing LLM API](https://alibaba.github.io/page-agent/docs/features/models#free-testing-api). By using it, you agree to its[terms](https://github.com/alibaba/page-agent/blob/main/docs/terms-and-privacy.md).

| Mirrors | URL | 
|---|---|
| Global | [https://cdn.jsdelivr.net/npm/page-agent@1.11.0/dist/iife/page-agent.demo.js](https://cdn.jsdelivr.net/npm/page-agent@1.11.0/dist/iife/page-agent.demo.js) | 
| China | [https://registry.npmmirror.com/page-agent/1.11.0/files/dist/iife/page-agent.demo.js](https://registry.npmmirror.com/page-agent/1.11.0/files/dist/iife/page-agent.demo.js) | 

Add `?autoInit=false` to load the script without creating the demo agent automatically. You can then instantiate it with `new window.PageAgent(...)`.

`npm install page-agent````
import { PageAgent } from 'page-agent'
const agent = new PageAgent({
    model: 'qwen3.5-plus',
    baseURL: 'https://dashscope.aliyuncs.com/compatible-mode/v1',
    apiKey: 'YOUR_API_KEY',
    language: 'en-US',
})
await agent.execute('Click the login button')
```
For more programmatic usage, see [📖 Documentations](https://alibaba.github.io/page-agent/docs/introduction/overview).

Built something cool with PageAgent? Add it here! Open a PR to share your project.

These are community projects — not maintained or endorsed by us. Use at your own discretion.


| Project | Description | 
|---|---|
| Yours? | [Open a PR](https://github.com/alibaba/page-agent/pulls)🙌 | 

We welcome contributions from the community! See [CONTRIBUTING.md](https://github.com/alibaba/page-agent/blob/main/CONTRIBUTING.md) for guidelines and [docs/developer-guide.md](https://github.com/alibaba/page-agent/blob/main/docs/developer-guide.md) for local development workflows.

Please read the [maintainer's note](https://github.com/alibaba/page-agent/issues/349) on principles and current state.

Contributions generated entirely by **bots or AI** without substantial human involvement will **not be accepted**.

This project builds upon the excellent work of 

`browser-use``PageAgent` is designed for **client-side web enhancement**, not server-side automation.

```
DOM processing components and prompt are derived from browser-use:
Browser Use <https://github.com/browser-use/browser-use>
Copyright (c) 2024 Gregor Zunic
Licensed under the MIT License
We gratefully acknowledge the browser-use project and its contributors for their
excellent work on web automation and DOM interaction patterns that helped make
this project possible.
```
**⭐ Star this repo if you find PageAgent helpful!**
