"""HTML 渲染：每日页 + 日历首页 + 静态资源。"""
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


def render_daily(date_label: str, items: list[Item], site_conf: dict[str, Any]) -> Path:
    env = _env()
    tpl = env.get_template("daily.html")
    source_summary = ", ".join(sorted({it.source_label.split(" · ")[0] for it in items})) or "—"
    html = tpl.render(
        site=site_conf,
        date=date_label,
        items=items,
        rel_root="../",
        generated_at=datetime.now().strftime("%Y-%m-%d %H:%M"),
        source_summary=source_summary,
        tag_class=_tag_class,
    )
    out_dir = project_root() / "site" / "daily"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{date_label}.html"
    out_path.write_text(html, encoding="utf-8")
    log.info("rendered daily: %s", out_path.relative_to(project_root()))
    return out_path


def render_index(site_conf: dict[str, Any]) -> Path:
    """扫描 site/daily/*.html 生成日历首页。"""
    site_dir = project_root() / "site"
    daily_dir = site_dir / "daily"
    daily_dir.mkdir(parents=True, exist_ok=True)
    dates = sorted(
        [
            p.stem
            for p in daily_dir.glob("*.html")
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.stem)
        ]
    )

    env = _env()
    tpl = env.get_template("index.html")
    html = tpl.render(
        site=site_conf,
        available_dates=dates,
        available_dates_json=json.dumps(dates),
        latest=dates[-1] if dates else "",
    )
    out_path = site_dir / "index.html"
    out_path.write_text(html, encoding="utf-8")
    log.info("rendered index with %d dates", len(dates))
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
