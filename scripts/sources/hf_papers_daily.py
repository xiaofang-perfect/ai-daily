"""HuggingFace Daily Papers: 按日期 URL `huggingface.co/papers?date=YYYY-MM-DD` 抓每日论文榜。"""
from __future__ import annotations

import json
import re
from datetime import datetime, timedelta, timezone

from bs4 import BeautifulSoup

from scripts.sources.base import Item, Source
from scripts.utils import http_client, log, stable_id, truncate


class HFPapersDailySource(Source):
    supports_backfill = True

    def fetch(self, since: datetime, until: datetime) -> list[Item]:
        items: list[Item] = []
        cur = since.replace(hour=12, minute=0, second=0, microsecond=0)
        end = until
        with http_client(timeout=25.0) as c:
            while cur <= end + timedelta(days=1):
                date_str = cur.strftime("%Y-%m-%d")
                url = f"https://huggingface.co/papers?date={date_str}"
                try:
                    r = c.get(url)
                    if r.status_code == 200:
                        items.extend(self._parse(r.text, date_str))
                except Exception as e:
                    log.debug("[%s] %s failed: %s", self.id, date_str, e)
                cur += timedelta(days=1)
        log.info("[%s] fetched %d papers", self.id, len(items))
        return items

    def _parse(self, html: str, date_str: str) -> list[Item]:
        out: list[Item] = []
        soup = BeautifulSoup(html, "lxml")

        # HF papers 用 SvelteKit；数据通常嵌在 <script> data-sveltekit-fetched 里
        # 兜底：直接抓 HTML 的 paper 卡片
        for art in soup.select("article"):
            link = art.find("a", href=re.compile(r"^/papers/"))
            if not link:
                continue
            paper_path = link.get("href", "")
            if not paper_path.startswith("/papers/"):
                continue
            arxiv_id = paper_path.split("/")[-1]
            title_el = art.find(["h3", "h2"])
            title = title_el.get_text(strip=True) if title_el else ""
            if not title:
                continue

            # 摘要
            summary = ""
            # HF 卡片里有 .text-gray-500 之类的描述，宽松匹配
            for sel in [".text-gray-700", ".text-gray-500", "p"]:
                el = art.select_one(sel)
                if el:
                    txt = el.get_text(" ", strip=True)
                    if len(txt) > 30:
                        summary = txt
                        break

            # 点赞数（如果能抓到，作为热度）
            score = None
            score_label = ""
            # HF 用 svg + 数字表示 upvotes，文本里寻找
            for txt in art.stripped_strings:
                if re.fullmatch(r"\d{1,4}", txt) and len(txt) <= 4:
                    try:
                        score = float(txt)
                        score_label = f"👍 {txt}"
                        break
                    except ValueError:
                        pass

            url = f"https://arxiv.org/abs/{arxiv_id}" if re.fullmatch(r"\d{4}\.\d{4,6}", arxiv_id) else f"https://huggingface.co{paper_path}"
            pub = datetime.strptime(date_str, "%Y-%m-%d").replace(hour=12, tzinfo=timezone.utc)
            out.append(
                Item(
                    source_id=self.id,
                    source_label=f"{self.label} · {date_str}",
                    title=title,
                    url=url,
                    raw_excerpt=truncate(summary, 1200),
                    published_at=pub,
                    score=score,
                    score_label=score_label,
                    item_id=stable_id(self.id, arxiv_id, date_str),
                )
            )
        return out
