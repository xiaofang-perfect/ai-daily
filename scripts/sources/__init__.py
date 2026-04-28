"""采集源注册表。"""
from __future__ import annotations

from typing import Any

from scripts.sources.arxiv import ArxivSource
from scripts.sources.base import Item, Source
from scripts.sources.github_trending import GithubTrendingSource
from scripts.sources.hackernews import HackerNewsSource
from scripts.sources.reddit import RedditSource
from scripts.sources.rss import RSSSource
from scripts.sources.twitter_rsshub import TwitterRSSHubSource


REGISTRY: dict[str, type[Source]] = {
    "rss": RSSSource,
    "arxiv": ArxivSource,
    "hackernews": HackerNewsSource,
    "reddit": RedditSource,
    "github_trending": GithubTrendingSource,
    "rsshub_twitter": TwitterRSSHubSource,
}


def build_source(conf: dict[str, Any]) -> Source | None:
    t = conf.get("type")
    cls = REGISTRY.get(t)
    if not cls:
        from scripts.utils import log
        log.warning("unknown source type: %s (id=%s)", t, conf.get("id"))
        return None
    return cls(conf)


__all__ = ["Item", "Source", "REGISTRY", "build_source"]
