"""通用 RSS 来源。覆盖：The Verge、MIT TR、机器之心、量子位、Anthropic/OpenAI 博客、TLDR AI、HF Papers 等。"""
from __future__ import annotations

from datetime import datetime
from typing import Any

import feedparser

from scripts.sources.base import Item, Source
from scripts.utils import (
    expand_env,
    first_images_from_html,
    log,
    parse_dt,
    stable_id,
    truncate,
)


class RSSSource(Source):
    # RSS feed 通常只保留最近一段时间的条目，对老日期几乎一定空。
    # 这里设 True 因为 fetch 会按 since/until 过滤，老日期会安全返回 0。
    supports_backfill = True

    def fetch(self, since: datetime, until: datetime) -> list[Item]:
        items: list[Item] = []
        feeds = [expand_env(u) for u in (self.conf.get("feeds") or []) if u]
        for url in feeds:
            if not url:
                continue
            try:
                parsed = feedparser.parse(url)
            except Exception as e:
                log.warning("[%s] parse %s failed: %s", self.id, url, e)
                continue

            for entry in parsed.entries[:60]:
                pub = parse_dt(getattr(entry, "published", None)) or parse_dt(
                    getattr(entry, "updated", None)
                ) or parse_dt(getattr(entry, "published_parsed", None))
                if pub and (pub < since or pub > until):
                    continue

                title = (getattr(entry, "title", "") or "").strip()
                link = (getattr(entry, "link", "") or "").strip()
                if not title or not link:
                    continue

                # summary 优先 content > summary > description
                content_html = ""
                if getattr(entry, "content", None):
                    try:
                        content_html = entry.content[0].value or ""
                    except Exception:
                        pass
                if not content_html:
                    content_html = getattr(entry, "summary", "") or getattr(entry, "description", "") or ""

                imgs = first_images_from_html(content_html, max_n=2)
                # 提取纯文本用于 LLM 上下文
                text = _strip_html(content_html)

                items.append(
                    Item(
                        source_id=self.id,
                        source_label=self.label,
                        title=title,
                        url=link,
                        raw_excerpt=truncate(text, 1500),
                        published_at=pub,
                        images=imgs,
                        item_id=stable_id(self.id, link),
                    )
                )
        log.info("[%s] fetched %d items", self.id, len(items))
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
