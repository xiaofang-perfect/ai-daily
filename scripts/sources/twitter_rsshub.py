"""X/Twitter via 自部署 RSSHub。需要先部署 RSSHub 并设置 RSSHUB_BASE_URL 和 TWITTER_AUTH_TOKEN。"""
from __future__ import annotations

import os
from datetime import datetime

import feedparser

from scripts.sources.base import Item, Source
from scripts.utils import (
    first_images_from_html,
    http_client,
    log,
    parse_dt,
    stable_id,
    truncate,
)


class TwitterRSSHubSource(Source):
    def fetch(self, since: datetime, until: datetime) -> list[Item]:
        base = os.environ.get("RSSHUB_BASE_URL", "").rstrip("/")
        if not base:
            log.info("[%s] RSSHUB_BASE_URL not set, skipping", self.id)
            return []

        handles = self.conf.get("handles", [])
        items: list[Item] = []
        for h in handles:
            url = f"{base}/twitter/user/{h}"
            try:
                with http_client() as c:
                    r = c.get(url)
                    if r.status_code != 200:
                        log.warning("[%s] @%s status %s", self.id, h, r.status_code)
                        continue
                    parsed = feedparser.parse(r.text)
            except Exception as e:
                log.warning("[%s] @%s failed: %s", self.id, h, e)
                continue

            for e in parsed.entries[:20]:
                pub = parse_dt(getattr(e, "published", None))
                if pub and (pub < since or pub > until):
                    continue
                title = (getattr(e, "title", "") or "").strip()
                link = (getattr(e, "link", "") or "").strip()
                if not title or not link:
                    continue
                content_html = getattr(e, "summary", "") or ""
                imgs = first_images_from_html(content_html, max_n=2)
                items.append(
                    Item(
                        source_id=self.id,
                        source_label=f"X · @{h}",
                        title=truncate(title, 120),
                        url=link,
                        raw_excerpt=truncate(_strip_html(content_html), 1000),
                        published_at=pub,
                        images=imgs,
                        item_id=stable_id(self.id, link),
                    )
                )
        log.info("[%s] fetched %d tweets", self.id, len(items))
        return items


def _strip_html(html: str) -> str:
    if not html:
        return ""
    try:
        from bs4 import BeautifulSoup
        return BeautifulSoup(html, "lxml").get_text(" ", strip=True)
    except Exception:
        import re
        return re.sub(r"<[^>]+>", " ", html)
