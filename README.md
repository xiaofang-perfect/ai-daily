# 每日 AI 资讯

每天早上 10:15 自动从 10+ 个来源采集前 24 小时的 AI 资讯，由 LLM 筛选 10 条，
推送到飞书 + 部署到 GitHub Pages，并把全文留痕到本地。

## 它做什么

1. **采集**：The Verge AI / MIT TR / ArXiv / Hacker News / Reddit / GitHub Trending / HuggingFace Papers / 机器之心 / 量子位 / TLDR AI / X（可选）
2. **筛选**：DeepSeek / OpenAI / Claude / 通义 等大模型筛 10 条最有价值的
3. **分类**：每条打 4 类标签之一（论文研究 / 产品发布 / 行业动态 / 工具开源）
4. **留痕**：每条原文清理广告后存为 markdown，按 `archive/年/月/日/` 归档
5. **推送**：发到飞书群机器人 + 部署到 GitHub Pages
6. **日历**：网站首页是日历，点任意日期看那天的日报

## 项目结构

```
.
├── config.yaml                # 全局配置：来源、模型、数量、分类
├── .env                       # 本地密钥（已 gitignore）
├── .env.example               # 密钥模板
├── requirements.txt           # Python 依赖
├── README.md
├── scripts/                   # 主程序
│   ├── main.py                # 入口：采集 → 筛选 → 留痕 → 渲染 → 通知
│   ├── llm.py                 # 多模型适配（OpenAI 兼容 + Anthropic）
│   ├── filter.py              # LLM 筛选 + 摘要 + 分类
│   ├── archive.py             # 全文抓取 + markdown 留痕
│   ├── render.py              # Jinja2 → HTML
│   ├── notify.py              # 飞书 webhook
│   ├── utils.py               # 时间窗、HTTP、slugify 等
│   └── sources/               # 各来源采集器
│       ├── base.py
│       ├── rss.py             # 通用 RSS（覆盖大多数源）
│       ├── arxiv.py           # ArXiv API
│       ├── hackernews.py      # Algolia API
│       ├── reddit.py          # 免登录 .json
│       ├── github_trending.py # HTML 抓取
│       └── twitter_rsshub.py  # 通过 RSSHub
├── templates/                 # Jinja2 模板 + CSS
│   ├── daily.html
│   ├── index.html
│   └── assets/style.css
├── archive/                   # 全文留痕（按 年/月/日 归档）
│   └── 2026/04/28/openai-xxx-abc12345.md
├── site/                      # 静态站点输出（GitHub Pages 发布的内容）
│   ├── index.html             # 日历首页
│   ├── daily/2026-04-28.html  # 每日详情页
│   └── assets/style.css
├── data/                      # 缓存与状态（运行时生成）
└── .github/workflows/daily.yml  # GitHub Actions 定时任务
```

## 本地运行

```bash
# 1. 装依赖
python3 -m pip install -r requirements.txt

# 2. 第一次只测采集（不调 LLM、不发通知）
python3 -m scripts.main --dry-run

# 3. 完整跑一次
python3 -m scripts.main

# 4. 跳过部分步骤（调试用）
python3 -m scripts.main --no-notify --no-archive
python3 -m scripts.main --limit-archive 3   # 只抓前 3 条全文
```

跑完会生成：
- `site/daily/YYYY-MM-DD.html` - 当日页
- `site/index.html` - 日历首页
- `archive/YYYY/MM/DD/*.md` - 全文留痕
- 飞书群消息（如配置了 webhook）

直接用浏览器打开 `site/index.html` 即可预览。

## 配置

### 改模型（最常用）

编辑 `config.yaml` 的 `llm:` 段。改 `provider`/`model`/`base_url` 即可：

```yaml
llm:
  provider: openai_compatible
  model: deepseek-chat
  base_url: https://api.deepseek.com/v1
```

切到 OpenAI / Claude / 通义 / Moonshot / 智谱：直接抄文件里的注释段。
API key 始终从环境变量 `LLM_API_KEY` 读，不要写在 yaml 里。

### 加/减/改采集源

编辑 `config.yaml` 的 `sources:` 段。每条加 `enabled: false` 即可临时关闭。
新增 RSS 源直接加一段：

```yaml
- id: my_blog
  type: rss
  label: 某个博客
  enabled: true
  feeds:
    - https://example.com/feed
```

### 调整每日条数与分类

```yaml
output:
  daily_count: 10
  per_source_collect: 30
  archive_full_text: true
  categories:
    - 论文研究
    - 产品发布
    - 行业动态
    - 工具开源
```

## GitHub Actions（云端定时）

定时任务文件：`.github/workflows/daily.yml`

- 触发时间：每天 UTC 02:00 = 北京时间 10:00
- 实际可见时间：约 10:15（采集 + LLM 筛选 + 抓全文需要 5-15 分钟）
- 可手动触发：仓库 → Actions → Daily AI News → Run workflow

GitHub 仓库需要配置以下 **Secrets**（Settings → Secrets and variables → Actions）：

| Secret | 必须 | 说明 |
| ------ | ---- | ---- |
| `LLM_API_KEY` | ✅ | DeepSeek/OpenAI/Claude 等的 API key |
| `FEISHU_WEBHOOK_URL` | ✅ | 飞书自定义机器人 webhook |
| `FEISHU_WEBHOOK_SECRET` | 可选 | 启用飞书签名校验时填 |
| `SITE_BASE_URL` | 可选 | 例如 `https://用户名.github.io/ai-daily`，飞书消息里"查看完整日报"按钮会用 |
| `RSSHUB_BASE_URL` | 可选 | 自部署的 RSSHub 实例 URL |
| `TWITTER_AUTH_TOKEN` | 可选 | RSSHub 抓 X 用 |

## X / Twitter 配置

X 是付费墙 + 反爬，三种方案：

1. **RSSHub 自部署**（推荐，免费）
   - Vercel 一键部署：https://github.com/DIYgod/RSSHub
   - 部署后填 `RSSHUB_BASE_URL` 到 secrets
   - X 路由需要登录 cookie，按 RSSHub 文档填 `TWITTER_AUTH_TOKEN`
2. **公共 RSSHub 实例**：填 `https://rsshub.app`，但限流较重，不稳定
3. **跳过**：v1 不开 X，由 TLDR AI / Ben's Bites 等 newsletter 间接覆盖

`config.yaml` 里 `x_via_rsshub` 默认 `enabled: false`，部署完 RSSHub 再改 `true`。

## 全文留痕

每条入选资讯的全文存为 markdown，路径：
```
archive/2026/04/28/<source-id>-<slug>-<hash>.md
```

文件 frontmatter 含标题、来源、URL、发布时间、分类。正文经 trafilatura 提取，
去广告/导航/侧栏，保留正文 + 图片 markdown 链接。

`site/archive/...` 是同一份文件的副本，让 GitHub Pages 也能直链查看。

## 常见问题

**Q: GitHub Actions 海外 IP 抓 36氪/量子位失败怎么办？**
- 备选 1：把这些源单独跑在你本地或国内 VPS，用 git push 把结果合并
- 备选 2：用 RSSHub 中转（部分中文站有 RSSHub 路由）

**Q: 想换语言/Prompt 怎么办？**
- Prompt 在 `scripts/filter.py` 顶部 `SYSTEM_PROMPT` 和 `USER_TEMPLATE`
- 改完直接生效，不需要重新部署

**Q: 想加新分类标签？**
- 改 `config.yaml` 的 `output.categories`
- 同步在 `scripts/render.py` 的 `_TAG_CLASS` 加一个 CSS class 映射（可选，纯样式）
- `templates/assets/style.css` 加 `.tag-xxx` 样式（可选）

**Q: 历史数据要不要 commit 进仓库？**
- `archive/` 和 `site/` 都会被 GitHub Actions 自动 commit & push 回仓库
- 这样仓库本身就是完整历史归档

## 维护

- **看运行日志**：仓库 → Actions → 选某次运行
- **手动重跑**：仓库 → Actions → Daily AI News → Run workflow
- **改配置**：直接改 `config.yaml` 提交，下次运行生效
- **换 API key**：仓库 → Settings → Secrets → 改 `LLM_API_KEY`

## License

MIT
