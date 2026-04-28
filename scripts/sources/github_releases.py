"""GitHub Releases: 拉指定 repo 列表的最近发布。
适用于 DeepSeek / Qwen / Mistral 等以 GitHub 为发布渠道的 AI 模型。
"""
from __future__ import annotations

import os
from datetime import datetime

from scripts.sources.base import Item, Source
from scripts.utils import http_client, log, parse_dt, stable_id, truncate


class GithubReleasesSource(Source):
    supports_backfill = True
    API = "https://api.github.com"

    def fetch(self, since: datetime, until: datetime) -> list[Item]:
        repos = self.conf.get("repos", [])
        token = os.environ.get("GITHUB_TOKEN", "")  # 可选，提高频次限制
        headers = {"Accept": "application/vnd.github+json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"

        items: list[Item] = []
        with http_client() as c:
            for repo in repos:
                url = f"{self.API}/repos/{repo}/releases?per_page=20"
                try:
                    r = c.get(url, headers=headers)
                    if r.status_code != 200:
                        log.warning("[%s] %s status=%s", self.id, repo, r.status_code)
                        continue
                    data = r.json()
                except Exception as e:
                    log.warning("[%s] %s failed: %s", self.id, repo, e)
                    continue

                for rel in data:
                    pub = parse_dt(rel.get("published_at") or rel.get("created_at"))
                    if pub and (pub < since or pub > until):
                        continue
                    if rel.get("draft") or rel.get("prerelease"):
                        continue
                    tag = rel.get("tag_name", "")
                    name = rel.get("name", tag)
                    title = f"{repo} 发布 {tag}" + (f"：{name}" if name and name != tag else "")
                    body = rel.get("body") or ""
                    items.append(
                        Item(
                            source_id=self.id,
                            source_label=f"{self.label} · {repo.split('/')[-1]}",
                            title=title,
                            url=rel.get("html_url", f"https://github.com/{repo}/releases/tag/{tag}"),
                            raw_excerpt=truncate(body, 1500),
                            published_at=pub,
                            item_id=stable_id(self.id, repo, tag),
                        )
                    )
        log.info("[%s] fetched %d releases", self.id, len(items))
        return items
