"""HTML 渲染：每日页 + 首页（最新一期 + 日历侧栏）+ 静态资源。"""
from __future__ import annotations

import json
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, select_autoescape

from scripts.sources.base import Item
from scripts.utils import log, project_root


_TAG_CLASS = {
    "论文研究": "paper",
    "产品发布": "product",
    "行业动态": "industry",
    "工具开源": "tool",
}


def _tag_class(tag: str) -> str:
    return _TAG_CLASS.get(tag, "industry")


def _env() -> Environment:
    tpl_dir = project_root() / "templates"
    return Environment(
        loader=FileSystemLoader(str(tpl_dir)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=False,
        lstrip_blocks=False,
    )


def _scan_dates() -> list[str]:
    daily_dir = project_root() / "site" / "daily"
    daily_dir.mkdir(parents=True, exist_ok=True)
    return sorted(
        [
            p.stem
            for p in daily_dir.glob("*.html")
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.stem)
        ]
    )


def render_daily(date_label: str, items: list[Item], site_conf: dict[str, Any]) -> Path:
    env = _env()
    tpl = env.get_template("daily.html")
    source_summary = ", ".join(sorted({it.source_label.split(" · ")[0] for it in items})) or "—"

    # 渲染前需要扫一次 dates，并把今天加进去（因为 daily 文件还没写到磁盘）
    dates = _scan_dates()
    if date_label not in dates:
        dates.append(date_label)
    dates.sort()

    html = tpl.render(
        site=site_conf,
        date=date_label,
        items=items,
        rel_root="../",
        generated_at=datetime.now().strftime("%Y-%m-%d %H:%M"),
        source_summary=source_summary,
        tag_class=_tag_class,
        available_dates=dates,
        available_dates_json=json.dumps(dates),
    )
    out_dir = project_root() / "site" / "daily"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{date_label}.html"
    out_path.write_text(html, encoding="utf-8")
    log.info("rendered daily: %s", out_path.relative_to(project_root()))
    return out_path


def render_index(date_label: str, items: list[Item], site_conf: dict[str, Any]) -> Path:
    """首页 = 最新一期内容 + 左侧日历。"""
    env = _env()
    tpl = env.get_template("index.html")
    dates = _scan_dates()
    source_summary = ", ".join(sorted({it.source_label.split(" · ")[0] for it in items})) or "—"

    html = tpl.render(
        site=site_conf,
        date=date_label,
        items=items,
        rel_root="",
        generated_at=datetime.now().strftime("%Y-%m-%d %H:%M"),
        source_summary=source_summary,
        tag_class=_tag_class,
        available_dates=dates,
        available_dates_json=json.dumps(dates),
    )
    out_path = project_root() / "site" / "index.html"
    out_path.write_text(html, encoding="utf-8")
    log.info("rendered index with %d dates (latest: %s)", len(dates), date_label)
    return out_path


def copy_assets() -> None:
    src = project_root() / "templates" / "assets"
    dst = project_root() / "site" / "assets"
    if src.exists():
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        log.info("assets copied to site/assets")


def copy_archive_to_site(date_label: str) -> None:
    """把当天 archive/ 下的 markdown 也复制到 site/archive/，让 GitHub Pages 可访问。"""
    y, m, d = date_label.split("-")
    src = project_root() / "archive" / y / m / d
    if not src.exists():
        return
    dst = project_root() / "site" / "archive" / y / m / d
    dst.mkdir(parents=True, exist_ok=True)
    for f in src.glob("*.md"):
        shutil.copy2(f, dst / f.name)
