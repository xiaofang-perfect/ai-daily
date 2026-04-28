"""通用工具：日志、时间窗、HTTP、文本处理。"""
from __future__ import annotations

import hashlib
import logging
import os
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from datetime import datetime, time, timedelta, timezone
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import httpx


# ---------- 日志 ----------
def setup_logger(name: str = "ai-daily", level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
    logger.addHandler(h)
    logger.setLevel(level)
    return logger


log = setup_logger()


# ---------- 时间窗 ----------
def get_time_window(tz_name: str, cutoff_hour: int, now: datetime | None = None) -> tuple[datetime, datetime]:
    """返回 (since, until)，UTC aware。

    until = 今天 cutoff_hour:00 (本地时区)
    since = 昨天 cutoff_hour:00 (本地时区)
    """
    tz = ZoneInfo(tz_name)
    now_local = (now or datetime.now(tz)).astimezone(tz)
    until_local = datetime.combine(now_local.date(), time(cutoff_hour, 0), tzinfo=tz)
    if now_local < until_local:
        until_local -= timedelta(days=1)
    since_local = until_local - timedelta(days=1)
    return since_local.astimezone(timezone.utc), until_local.astimezone(timezone.utc)


def today_label(tz_name: str, cutoff_hour: int, now: datetime | None = None) -> str:
    """日报对应的日期标签 YYYY-MM-DD。即 until 那天。"""
    _, until = get_time_window(tz_name, cutoff_hour, now)
    return until.astimezone(ZoneInfo(tz_name)).strftime("%Y-%m-%d")


# ---------- HTTP ----------
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)


def http_client(timeout: float = 30.0) -> httpx.Client:
    return httpx.Client(
        timeout=timeout,
        follow_redirects=True,
        headers={"User-Agent": USER_AGENT, "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"},
    )


def safe_get(url: str, **kwargs) -> httpx.Response | None:
    try:
        with http_client() as c:
            r = c.get(url, **kwargs)
            r.raise_for_status()
            return r
    except Exception as e:
        log.warning("GET %s failed: %s", url, e)
        return None


# ---------- 文本 ----------
def slugify(text: str, max_len: int = 60) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text.strip())
    text = text[:max_len].strip("-")
    if not text:
        text = "untitled"
    return text


def stable_id(*parts: str) -> str:
    h = hashlib.sha1()
    for p in parts:
        h.update(p.encode("utf-8"))
        h.update(b"|")
    return h.hexdigest()[:16]


def truncate(text: str, max_chars: int) -> str:
    text = (text or "").strip()
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 1] + "…"


def parse_dt(value: Any) -> datetime | None:
    """尽量把任意常见时间格式解析为 UTC aware datetime。"""
    if value is None:
        return None
    if isinstance(value, datetime):
        return value if value.tzinfo else value.replace(tzinfo=timezone.utc)
    if isinstance(value, (int, float)):
        return datetime.fromtimestamp(value, tz=timezone.utc)
    if isinstance(value, str):
        # 优先 dateutil
        try:
            from dateutil import parser as du
            dt = du.parse(value)
            return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
        except Exception:
            return None
    if isinstance(value, tuple) and len(value) >= 6:
        # feedparser 的 struct_time 兼容
        try:
            return datetime(*value[:6], tzinfo=timezone.utc)
        except Exception:
            return None
    return None


# ---------- 路径 ----------
def project_root() -> Path:
    return Path(__file__).resolve().parent.parent


def env_get(key: str, default: str = "") -> str:
    return os.environ.get(key, default)


def expand_env(value: str) -> str:
    """把字符串中的 ${VAR} 替换成环境变量。"""
    if not isinstance(value, str):
        return value
    return re.sub(r"\$\{([A-Z_][A-Z0-9_]*)\}", lambda m: os.environ.get(m.group(1), ""), value)


# ---------- 图片提取 ----------
def first_images_from_html(html: str, max_n: int = 2) -> list[str]:
    if not html:
        return []
    out: list[str] = []
    for m in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', html, flags=re.IGNORECASE):
        u = m.group(1)
        if u.startswith("data:"):
            continue
        if u not in out:
            out.append(u)
        if len(out) >= max_n:
            break
    return out


def og_image(html: str) -> str | None:
    m = re.search(
        r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']',
        html or "",
        flags=re.IGNORECASE,
    )
    return m.group(1) if m else None
