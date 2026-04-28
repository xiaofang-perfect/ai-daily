"""主入口：采集 → 去重 → LLM 筛选 → 抓全文留痕 → 渲染 → 飞书通知。"""
from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, time, timedelta, timezone
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import yaml

# 让本模块既能 `python -m scripts.main` 也能 `python scripts/main.py` 跑
_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from scripts.archive import archive_item  # noqa: E402
from scripts.filter import filter_and_classify  # noqa: E402
from scripts.llm import LLMClient  # noqa: E402
from scripts.notify import send_feishu  # noqa: E402
from scripts.render import (  # noqa: E402
    copy_archive_to_site,
    copy_assets,
    re_render_all_dailies,
    render_daily,
    render_index,
)
from scripts.sources import build_source  # noqa: E402
from scripts.sources.base import Item  # noqa: E402
from scripts.utils import env_get, get_time_window, log, today_label  # noqa: E402


def load_dotenv() -> None:
    """简易 .env 加载（不依赖 python-dotenv）。"""
    p = _ROOT / ".env"
    if not p.exists():
        return
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        k, v = line.split("=", 1)
        k, v = k.strip(), v.strip().strip('"').strip("'")
        os.environ.setdefault(k, v)


def load_config() -> dict[str, Any]:
    p = _ROOT / "config.yaml"
    return yaml.safe_load(p.read_text(encoding="utf-8"))


def _backfill_window(date_label: str, tz_name: str, cutoff_hour: int) -> tuple[datetime, datetime]:
    """补跑模式的时间窗：返回 (since, until) UTC aware。
    until = date 当天 cutoff:00 (本地)，since = until - 24h。
    """
    tz = ZoneInfo(tz_name)
    until_local = datetime.combine(
        datetime.strptime(date_label, "%Y-%m-%d").date(),
        time(cutoff_hour, 0),
        tzinfo=tz,
    )
    since_local = until_local - timedelta(days=1)
    return since_local.astimezone(timezone.utc), until_local.astimezone(timezone.utc)


def collect_all(
    config: dict[str, Any],
    since: datetime | None = None,
    until: datetime | None = None,
    backfill: bool = False,
) -> list[Item]:
    site_conf = config.get("site", {})
    if since is None or until is None:
        tz = site_conf.get("timezone", "Asia/Shanghai")
        cutoff = int(site_conf.get("daily_cutoff_hour", 10))
        since, until = get_time_window(tz, cutoff)
    log.info("时间窗：%s ~ %s (UTC)", since.isoformat(), until.isoformat())

    per_source = int(config.get("output", {}).get("per_source_collect", 30))
    all_items: list[Item] = []
    for sconf in config.get("sources", []):
        if not sconf.get("enabled", True):
            continue
        src = build_source(sconf)
        if not src:
            continue
        if backfill and not getattr(src, "supports_backfill", False):
            log.info("[%s] 跳过（不支持 backfill）", sconf.get("id"))
            continue
        try:
            items = src.fetch(since, until)
        except Exception as e:
            log.exception("[%s] fetch failed: %s", sconf.get("id"), e)
            continue
        all_items.extend(items[:per_source])

    # 去重：按 URL
    seen: set[str] = set()
    deduped: list[Item] = []
    for it in all_items:
        key = it.url.split("?")[0].rstrip("/")
        if key in seen:
            continue
        seen.add(key)
        deduped.append(it)
    log.info("总计采集 %d → 去重 %d", len(all_items), len(deduped))
    return deduped


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="不调 LLM、不抓全文、不发通知，只测试采集")
    ap.add_argument("--no-archive", action="store_true", help="跳过全文抓取留痕")
    ap.add_argument("--no-notify", action="store_true", help="跳过飞书通知")
    ap.add_argument("--limit-archive", type=int, default=0, help="限制抓全文条数（0=不限）")
    ap.add_argument(
        "--backfill",
        type=str,
        metavar="YYYY-MM-DD",
        help="补跑指定日期的日报。仅 ArXiv/HackerNews 等支持历史查询的源会有数据；自动跳过通知。",
    )
    args = ap.parse_args()

    load_dotenv()
    config = load_config()
    site_conf = config.get("site", {})
    out_conf = config.get("output", {})
    tz_name = site_conf.get("timezone", "Asia/Shanghai")
    cutoff = int(site_conf.get("daily_cutoff_hour", 10))

    if args.backfill:
        date_label = args.backfill
        since, until = _backfill_window(date_label, tz_name, cutoff)
        log.info("=== 补跑模式: %s ===", date_label)
        # backfill 默认不发通知
        args.no_notify = True
    else:
        date_label = today_label(tz_name, cutoff)
        since = until = None
        log.info("=== 日报日期: %s ===", date_label)

    # 1. 采集
    items = collect_all(config, since=since, until=until, backfill=bool(args.backfill))
    if args.dry_run:
        for it in items[:20]:
            print(f"[{it.source_label}] {it.title}\n  {it.url}\n")
        log.info("dry-run 完成，共 %d 条", len(items))
        return 0

    if not items:
        log.warning("没有采集到任何资讯，退出")
        return 1

    # 2. LLM 筛选 + 摘要 + 分类
    llm = LLMClient(config.get("llm", {}))
    top_k = int(out_conf.get("daily_count", 10))
    selected = filter_and_classify(items, llm, top_k=top_k, categories=out_conf.get("categories"))
    if not selected:
        log.warning("LLM 筛选后为 0 条，退出")
        return 2

    # 3. 抓全文留痕
    if out_conf.get("archive_full_text", True) and not args.no_archive:
        n = 0
        for it in selected:
            if args.limit_archive and n >= args.limit_archive:
                break
            archive_item(it, date_label)
            n += 1

    # 4. 渲染 HTML
    render_daily(date_label, selected, site_conf)
    copy_archive_to_site(date_label)
    copy_assets()
    # 重新渲染所有 daily 页面，让每个页面的日历都拿到完整日期列表
    re_render_all_dailies(site_conf)
    render_index(site_conf)  # 始终从最新 daily JSON 重新渲染首页

    # 5. 飞书通知
    if not args.no_notify:
        site_url = env_get("SITE_BASE_URL").rstrip("/")
        page_url = f"{site_url}/daily/{date_label}.html" if site_url else ""
        send_feishu(date_label, selected, site_url=page_url)

    log.info("=== 完成 ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
