"""Source 基类与 Item 数据结构。"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class Item:
    """一条采集到的资讯。在 pipeline 各阶段被逐步丰富。"""
    source_id: str               # 来源唯一标识，如 "hackernews"
    source_label: str            # 显示名，如 "Hacker News"
    title: str
    url: str                     # 原始链接，必须为真，可点击
    raw_excerpt: str = ""        # 原始摘要/正文片段（喂给 LLM 用）
    published_at: datetime | None = None
    images: list[str] = field(default_factory=list)
    score: float | None = None   # 来源自带的热度（点赞/星数/评论数等，归一化前）
    score_label: str = ""        # 热度的人类可读说明，如 "★ 320"

    # ---- 后续 pipeline 阶段填充 ----
    item_id: str = ""            # stable_id, 用于去重和归档命名
    summary: str = ""            # LLM 生成的中文摘要 (1-3 句)
    tag: str = ""                # LLM 分配的分类标签
    full_text_md: str = ""       # archive 模块抓取的全文 markdown
    archive_path: str = ""       # archive markdown 的相对路径
    selected: bool = False       # filter 阶段标记是否入选
    rank: int = 0                # filter 排序后的位次

    def to_dict(self) -> dict[str, Any]:
        return {
            "source_id": self.source_id,
            "source_label": self.source_label,
            "title": self.title,
            "url": self.url,
            "raw_excerpt": self.raw_excerpt,
            "published_at": self.published_at.isoformat() if self.published_at else None,
            "images": self.images,
            "score": self.score,
            "score_label": self.score_label,
            "item_id": self.item_id,
            "summary": self.summary,
            "tag": self.tag,
            "archive_path": self.archive_path,
            "selected": self.selected,
            "rank": self.rank,
        }


class Source:
    """采集源接口。子类只需实现 fetch()。"""

    def __init__(self, conf: dict[str, Any]):
        self.conf = conf
        self.id: str = conf["id"]
        self.label: str = conf.get("label", self.id)
        self.enabled: bool = conf.get("enabled", True)

    def fetch(self, since: datetime, until: datetime) -> list[Item]:
        raise NotImplementedError
