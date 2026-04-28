"""采集源注册表。"""
from __future__ import annotations

from typing import Any

from scripts.sources.arxiv import ArxivSource
from scripts.sources.base import Item, Source
from scripts.sources.github_releases import GithubReleasesSource
from scripts.sources.github_trending import GithubTrendingSource
from scripts.sources.hackernews import HackerNewsSource
from scripts.sources.hf_papers_daily import HFPapersDailySource
from scripts.sources.kr36_search import Kr36SearchSource
from scripts.sources.reddit import RedditSource
from scripts.sources.rss import RSSSource
from scripts.sources.tldr_archive import TLDRArchiveSource
from scripts.sources.twitter_rsshub import TwitterRSSHubSource


REGISTRY: dict[str, type[Source]] = {
    "rss": RSSSource,
    "arxiv": ArxivSource,
    "hackernews": HackerNewsSource,
    "reddit": RedditSource,
    "github_trending": GithubTrendingSource,
    "github_releases": GithubReleasesSource,
    "tldr_archive": TLDRArchiveSource,
    "hf_papers_daily": HFPapersDailySource,
    "kr36_search": Kr36SearchSource,
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
