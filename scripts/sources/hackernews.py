"""Hacker News: 通过 Algolia API 抓取 AI 相关热门故事。每个关键词分别查再合并。"""
from __future__ import annotations

from datetime import datetime, timezone

from scripts.sources.base import Item, Source
from scripts.utils import http_client, log, stable_id, truncate


class HackerNewsSource(Source):
    API = "https://hn.algolia.com/api/v1/search_by_date"

    def fetch(self, since: datetime, until: datetime) -> list[Item]:
        keywords = self.conf.get("keywords", ["AI", "LLM"])
        seen_ids: set[str] = set()
        items: list[Item] = []
        with http_client() as c:
            for kw in keywords:
                params = {
                    "query": kw,
                    "tags": "story",
                    "numericFilters": (
                        f"created_at_i>={int(since.timestamp())},"
                        f"created_at_i<={int(until.timestamp())}"
                    ),
                    "hitsPerPage": 30,
                }
                try:
                    r = c.get(self.API, params=params)
                    r.raise_for_status()
                    data = r.json()
                except Exception as e:
                    log.warning("[%s] kw=%s failed: %s", self.id, kw, e)
                    continue

                for hit in data.get("hits", []):
                    oid = str(hit.get("objectID"))
                    if oid in seen_ids:
                        continue
                    seen_ids.add(oid)
                    url = hit.get("url") or f"https://news.ycombinator.com/item?id={oid}"
                    title = (hit.get("title") or "").strip()
                    if not title:
                        continue
                    points = hit.get("points") or 0
                    comments = hit.get("num_comments") or 0
                    created_at = hit.get("created_at_i")
                    pub = (
                        datetime.fromtimestamp(created_at, tz=timezone.utc)
                        if created_at
                        else None
                    )
                    items.append(
                        Item(
                            source_id=self.id,
                            source_label=self.label,
                            title=title,
                            url=url,
                            raw_excerpt=truncate(hit.get("story_text") or "", 800),
                            published_at=pub,
                            score=float(points),
                            score_label=f"▲ {points}  💬 {comments}",
                            item_id=stable_id(self.id, oid),
                        )
                    )

        items.sort(key=lambda x: x.score or 0, reverse=True)
        items = items[:30]
        log.info("[%s] fetched %d stories (across %d keywords)", self.id, len(items), len(keywords))
        return items
