"""36氪搜索：按关键词搜索文章，按时间倒序。
适用于补历史日期（最近的内容用 RSS 即可）。
反爬较敏感，每页之间间隔 8-10 秒。"""
from __future__ import annotations

import re
import time
from datetime import datetime, timezone
from urllib.parse import quote

from bs4 import BeautifulSoup

from scripts.sources.base import Item, Source
from scripts.utils import http_client, log, parse_dt, stable_id, truncate


class Kr36SearchSource(Source):
    supports_backfill = True

    def fetch(self, since: datetime, until: datetime) -> list[Item]:
        query = self.conf.get("query", "AI")
        max_pages = int(self.conf.get("max_pages", 3))
        sleep_sec = float(self.conf.get("sleep_sec", 8.0))

        items: list[Item] = []
        with http_client(timeout=20.0) as c:
            for page in range(1, max_pages + 1):
                url = f"https://36kr.com/search/articles/{quote(query)}"
                if page > 1:
                    url += f"?page={page}"
                try:
                    r = c.get(url)
                    if r.status_code != 200:
                        log.warning("[%s] page %d status=%s", self.id, page, r.status_code)
                        break
                    page_items = self._parse(r.text, since, until)
                    items.extend(page_items)
                    # 如果整页都早于 since，说明不用再翻了
                    if page_items and all(
                        (it.published_at and it.published_at < since) for it in page_items
                    ):
                        break
                except Exception as e:
                    log.warning("[%s] page %d failed: %s", self.id, page, e)
                    break
                if page < max_pages:
                    time.sleep(sleep_sec)

        # 时间窗内
        items = [it for it in items if not it.published_at or (since <= it.published_at <= until)]
        log.info("[%s] fetched %d articles (query=%s)", self.id, len(items), query)
        return items

    def _parse(self, html: str, since: datetime, until: datetime) -> list[Item]:
        out: list[Item] = []
        soup = BeautifulSoup(html, "lxml")
        # 36kr 搜索结果项常见 class: .search-result-list .article-item-wrap, .common-list-article
        # 兜底：找所有带 /p/数字 链接的项
        seen: set[str] = set()
        for a in soup.find_all("a", href=re.compile(r"^/p/\d+")):
            href = a.get("href", "")
            if href in seen:
                continue
            seen.add(href)
            title = a.get_text(strip=True)
            if not title or len(title) < 6:
                continue
            url = f"https://36kr.com{href}"
            # 寻找该 a 周围的时间和摘要
            container = a.find_parent(["article", "div", "li"]) or a
            t_text = container.get_text(" ", strip=True)
            # 36kr 时间一般是 "X 小时前" / "X 分钟前" / "YYYY-MM-DD"
            pub = self._extract_time(t_text)
            # 摘要：title 之外的文字
            excerpt = t_text.replace(title, "").strip()[:600]

            out.append(
                Item(
                    source_id=self.id,
                    source_label=self.label,
                    title=title,
                    url=url,
                    raw_excerpt=truncate(excerpt, 800),
                    published_at=pub,
                    item_id=stable_id(self.id, href),
                )
            )
        return out

    def _extract_time(self, text: str) -> datetime | None:
        # 显式日期 YYYY-MM-DD
        m = re.search(r"(20\d{2})[-./](\d{1,2})[-./](\d{1,2})", text)
        if m:
            try:
                y, mo, d = map(int, m.groups())
                return datetime(y, mo, d, 12, tzinfo=timezone.utc)
            except Exception:
                pass
        # "X 小时前" / "X 分钟前" / "X 天前"
        m = re.search(r"(\d+)\s*(分钟|小时|天)前", text)
        if m:
            from datetime import timedelta
            now = datetime.now(tz=timezone.utc)
            n = int(m.group(1))
            unit = m.group(2)
            delta = {"分钟": timedelta(minutes=n), "小时": timedelta(hours=n), "天": timedelta(days=n)}.get(unit)
            if delta:
                return now - delta
        return None
