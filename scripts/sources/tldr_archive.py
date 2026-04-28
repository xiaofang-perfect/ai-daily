"""TLDR AI archive: 按日期 URL `tldr.tech/ai/YYYY-MM-DD` 抓每日精选。
每期里包含 15-20 条故事，每条提取为独立 Item。"""
from __future__ import annotations

import re
from datetime import datetime, timedelta, timezone
from html import unescape

from bs4 import BeautifulSoup

from scripts.sources.base import Item, Source
from scripts.utils import http_client, log, stable_id, truncate


class TLDRArchiveSource(Source):
    supports_backfill = True

    def fetch(self, since: datetime, until: datetime) -> list[Item]:
        items: list[Item] = []
        # 在 since~until 范围内每天试一次
        cur = since.replace(hour=12, minute=0, second=0, microsecond=0)
        end = until
        with http_client(timeout=20.0) as c:
            while cur <= end + timedelta(days=1):
                date_str = cur.strftime("%Y-%m-%d")
                url = f"https://tldr.tech/ai/{date_str}"
                try:
                    r = c.get(url)
                    if r.status_code == 200:
                        items.extend(self._parse(r.text, date_str))
                except Exception as e:
                    log.debug("[%s] %s failed: %s", self.id, date_str, e)
                cur += timedelta(days=1)
        log.info("[%s] fetched %d stories", self.id, len(items))
        return items

    def _parse(self, html: str, date_str: str) -> list[Item]:
        soup = BeautifulSoup(html, "lxml")
        out: list[Item] = []
        # TLDR 每条故事 = <article class="mt-3"><a><h3>title</h3></a><div>summary</div></article>
        for art in soup.select("article"):
            a = art.find("a")
            if not a:
                continue
            href = a.get("href", "").strip()
            h3 = a.find("h3")
            if not href or not h3:
                continue
            title = h3.get_text(strip=True)
            if not title:
                continue
            # 跳过广告
            if "(Sponsor)" in title or "utm_campaign" in href:
                continue
            # 跳过站内链接（订阅、自家产品等）
            if "tldr.tech" in href and "/ai/" not in href:
                continue
            summary_el = art.find("div", class_="newsletter-html")
            summary = summary_el.get_text(" ", strip=True) if summary_el else ""
            # TLDR 里时长标签（"5 minute read"）放在标题里 (XX minute read)，去掉
            title_clean = re.sub(r"\s*\(\d+\s*minute\s*read\)\s*$", "", title, flags=re.IGNORECASE).strip()

            # 用 date_str 当天 12:00 UTC 作为 published_at
            pub = datetime.strptime(date_str, "%Y-%m-%d").replace(hour=12, tzinfo=timezone.utc)
            out.append(
                Item(
                    source_id=self.id,
                    source_label=f"{self.label} · {date_str}",
                    title=title_clean,
                    url=unescape(href),
                    raw_excerpt=truncate(summary, 1200),
                    published_at=pub,
                    item_id=stable_id(self.id, href),
                )
            )
        return out
