"""ArXiv: 通过官方 API 拉指定时间窗内的 cs.AI / cs.LG / cs.CL 论文。"""
from __future__ import annotations

import urllib.parse as up
from datetime import datetime

import feedparser

from scripts.sources.base import Item, Source
from scripts.utils import http_client, log, parse_dt, stable_id, truncate


class ArxivSource(Source):
    supports_backfill = True
    API = "https://export.arxiv.org/api/query"

    def fetch(self, since: datetime, until: datetime) -> list[Item]:
        cats = self.conf.get("categories", ["cs.AI"])
        cat_query = " OR ".join(f"cat:{c}" for c in cats)
        # ArXiv submittedDate 格式: YYYYMMDDHHMM (UTC)
        s = since.strftime("%Y%m%d%H%M")
        u = until.strftime("%Y%m%d%H%M")
        query = f"({cat_query}) AND submittedDate:[{s} TO {u}]"
        # safe 保留 ArXiv 期望的字符；空格变 +
        encoded = up.quote_plus(query, safe=":[]")
        url = (
            f"{self.API}?search_query={encoded}"
            "&sortBy=submittedDate&sortOrder=descending&max_results=80"
        )

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
            # 二次过滤（API 偶尔会越界返回）
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
