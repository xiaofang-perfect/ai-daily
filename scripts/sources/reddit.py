"""Reddit: 抓 AI 相关 subreddit 当日热门。使用免登录 .json 接口。"""
from __future__ import annotations

from datetime import datetime, timezone

from scripts.sources.base import Item, Source
from scripts.utils import http_client, log, stable_id, truncate


class RedditSource(Source):
    def fetch(self, since: datetime, until: datetime) -> list[Item]:
        subs = self.conf.get("subreddits", [])
        items: list[Item] = []
        for sub in subs:
            url = f"https://www.reddit.com/r/{sub}/top.json?t=day&limit=25"
            try:
                with http_client() as c:
                    r = c.get(url, headers={"Accept": "application/json"})
                    if r.status_code != 200:
                        log.warning("[%s] r/%s status %s", self.id, sub, r.status_code)
                        continue
                    data = r.json()
            except Exception as e:
                log.warning("[%s] r/%s failed: %s", self.id, sub, e)
                continue

            for child in data.get("data", {}).get("children", []):
                d = child.get("data", {})
                created = d.get("created_utc")
                if not created:
                    continue
                pub = datetime.fromtimestamp(created, tz=timezone.utc)
                if pub < since or pub > until:
                    continue
                title = (d.get("title") or "").strip()
                permalink = d.get("permalink") or ""
                external = d.get("url_overridden_by_dest") or d.get("url") or ""
                # 偏向外链。但如果是自链 (selfpost) 用 reddit URL
                if d.get("is_self") or "reddit.com" in external:
                    final_url = f"https://www.reddit.com{permalink}"
                else:
                    final_url = external
                ups = d.get("ups") or 0
                num_comments = d.get("num_comments") or 0
                excerpt = (d.get("selftext") or "")[:1000]

                # 图片
                imgs: list[str] = []
                preview = d.get("preview", {}).get("images", []) if isinstance(d.get("preview"), dict) else []
                for p in preview[:2]:
                    src = p.get("source", {}).get("url")
                    if src:
                        imgs.append(src.replace("&amp;", "&"))
                if not imgs and external and any(external.lower().endswith(ext) for ext in (".jpg", ".png", ".jpeg", ".gif", ".webp")):
                    imgs = [external]

                items.append(
                    Item(
                        source_id=self.id,
                        source_label=f"{self.label} · r/{sub}",
                        title=title,
                        url=final_url,
                        raw_excerpt=truncate(excerpt, 1000),
                        published_at=pub,
                        images=imgs,
                        score=float(ups),
                        score_label=f"▲ {ups}  💬 {num_comments}",
                        item_id=stable_id(self.id, sub, d.get("id") or final_url),
                    )
                )
        items.sort(key=lambda x: x.score or 0, reverse=True)
        items = items[:30]
        log.info("[%s] fetched %d posts", self.id, len(items))
        return items
