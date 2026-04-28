"""ArXiv: 通过官方 API 拉 cs.AI / cs.LG / cs.CL 最新论文。"""
from __future__ import annotations

from datetime import datetime
from urllib.parse import urlencode

import feedparser

from scripts.sources.base import Item, Source
from scripts.utils import http_client, log, parse_dt, stable_id, truncate


class ArxivSource(Source):
    API = "https://export.arxiv.org/api/query"

    def fetch(self, since: datetime, until: datetime) -> list[Item]:
        cats = self.conf.get("categories", ["cs.AI"])
        query = "+OR+".join(f"cat:{c}" for c in cats)
        params = {
            "search_query": query,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "max_results": 80,
        }
        url = f"{self.API}?{urlencode(params, safe='+:')}"
        try:
            with http_client(timeout=45.0) as c:
                r = c.get(url)
                r.raise_for_status()
                feed = feedparser.parse(r.text)
        except Exception as e:
            log.warning("[%s] arxiv api failed: %s", self.id, e)
            return []

        items: list[Item] = []
        for e in feed.entries:
            pub = parse_dt(getattr(e, "published", None)) or parse_dt(getattr(e, "updated", None))
            if pub and (pub < since or pub > until):
                continue
            title = (getattr(e, "title", "") or "").replace("\n", " ").strip()
            link = (getattr(e, "link", "") or "").strip()
            summary = (getattr(e, "summary", "") or "").replace("\n", " ").strip()
            authors = ", ".join(getattr(a, "name", "") for a in getattr(e, "authors", []))
            excerpt = f"作者: {authors}\n摘要: {summary}" if authors else summary
            items.append(
                Item(
                    source_id=self.id,
                    source_label=self.label,
                    title=title,
                    url=link,
                    raw_excerpt=truncate(excerpt, 1500),
                    published_at=pub,
                    item_id=stable_id(self.id, link),
                )
            )
        log.info("[%s] fetched %d papers", self.id, len(items))
        return items
