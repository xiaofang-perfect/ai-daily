"""全文留痕：抓原始页面，去广告，存为按年月日归档的 markdown。"""
from __future__ import annotations

from datetime import datetime
from pathlib import Path

from scripts.sources.base import Item
from scripts.utils import http_client, log, project_root, slugify, today_label


def _frontmatter(item: Item, date_label: str) -> str:
    lines = [
        "---",
        f'title: "{(item.title or "").replace(chr(34), chr(39))}"',
        f"source: {item.source_label}",
        f"url: {item.url}",
        f"date: {date_label}",
        f'published_at: {item.published_at.isoformat() if item.published_at else ""}',
        f'tag: {item.tag}',
        f'item_id: {item.item_id}',
        "---",
        "",
    ]
    return "\n".join(lines)


def _extract_main_text(html: str, url: str) -> tuple[str, list[str]]:
    """返回 (markdown 正文, 图片 URL 列表)。"""
    text_md = ""
    images: list[str] = []

    try:
        import trafilatura
        extracted = trafilatura.extract(
            html,
            url=url,
            output_format="markdown",
            include_images=True,
            include_links=True,
            include_tables=True,
            favor_recall=True,
        )
        if extracted:
            text_md = extracted
    except Exception as e:
        log.warning("trafilatura failed for %s: %s", url, e)

    # 提取图片：从 markdown 里再扫一遍（trafilatura 已嵌入 ![]() ）
    if text_md:
        import re as _re
        for m in _re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", text_md):
            u = m.group(1).strip()
            if u and not u.startswith("data:") and u not in images:
                images.append(u)

    return text_md, images


def archive_item(item: Item, date_label: str) -> str:
    """抓全文存 markdown，返回相对路径。失败返回空串。"""
    if not item.url or item.url.startswith("https://news.ycombinator.com/item?id="):
        # HN 的内部页没什么可存的
        return ""

    try:
        with http_client(timeout=25.0) as c:
            r = c.get(item.url)
            if r.status_code >= 400:
                log.info("archive %s: status %s", item.url, r.status_code)
                return ""
            html = r.text
    except Exception as e:
        log.info("archive %s failed: %s", item.url, e)
        return ""

    md, imgs = _extract_main_text(html, item.url)
    if not md or len(md) < 100:
        return ""

    # 合并图片到 item.images（去重）
    if imgs:
        for u in imgs:
            if u not in item.images:
                item.images.append(u)
        item.images = item.images[:5]

    # 写入 archive/YYYY/MM/DD/<source>-<slug>.md
    y, m, d = date_label.split("-")
    rel_dir = Path("archive") / y / m / d
    abs_dir = project_root() / rel_dir
    abs_dir.mkdir(parents=True, exist_ok=True)

    slug = slugify(item.title, max_len=50) or item.item_id
    fname = f"{item.source_id}-{slug}-{item.item_id[:8]}.md"
    fpath = abs_dir / fname
    rel_path = str(rel_dir / fname)

    full = _frontmatter(item, date_label) + md.strip() + "\n"
    fpath.write_text(full, encoding="utf-8")
    item.full_text_md = md
    item.archive_path = rel_path
    log.info("archived %s -> %s", item.title[:40], rel_path)
    return rel_path
