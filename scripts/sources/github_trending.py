"""GitHub Trending: 抓 trending 页 HTML，按 AI 关键词过滤。"""
from __future__ import annotations

from datetime import datetime, timezone

from bs4 import BeautifulSoup

from scripts.sources.base import Item, Source
from scripts.utils import http_client, log, stable_id, truncate


class GithubTrendingSource(Source):
    def fetch(self, since: datetime, until: datetime) -> list[Item]:
        langs = self.conf.get("languages", ["all"])
        ai_kw = [k.lower() for k in self.conf.get("ai_keywords", ["ai", "llm"])]

        items: list[Item] = []
        seen: set[str] = set()
        for lang in langs:
            url = "https://github.com/trending" if lang == "all" else f"https://github.com/trending/{lang}"
            url += "?since=daily"
            try:
                with http_client() as c:
                    r = c.get(url)
                    r.raise_for_status()
            except Exception as e:
                log.warning("[%s] %s failed: %s", self.id, url, e)
                continue
            soup = BeautifulSoup(r.text, "lxml")
            for art in soup.select("article.Box-row"):
                a = art.select_one("h2 a")
                if not a:
                    continue
                href = a.get("href", "").strip()
                if not href or href in seen:
                    continue
                repo_path = href.lstrip("/")
                full_url = f"https://github.com{href}"
                desc_el = art.select_one("p")
                desc = desc_el.get_text(" ", strip=True) if desc_el else ""

                blob = (repo_path + " " + desc).lower()
                if not any(kw in blob for kw in ai_kw):
                    continue
                seen.add(href)

                stars_today = ""
                star_el = art.select_one("span.d-inline-block.float-sm-right")
                if star_el:
                    stars_today = star_el.get_text(" ", strip=True)

                items.append(
                    Item(
                        source_id=self.id,
                        source_label=self.label,
                        title=repo_path,
                        url=full_url,
                        raw_excerpt=truncate(desc, 500),
                        published_at=datetime.now(tz=timezone.utc),
                        score_label=stars_today,
                        item_id=stable_id(self.id, repo_path),
                    )
                )
        log.info("[%s] fetched %d repos", self.id, len(items))
        return items
