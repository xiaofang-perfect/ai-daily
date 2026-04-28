"""LLM 筛选与分类：从所有候选中挑出 N 条，给中文摘要和分类。"""
from __future__ import annotations

import json
from typing import Any

from scripts.llm import LLMClient, parse_json_loose
from scripts.sources.base import Item
from scripts.utils import log, truncate


SYSTEM_PROMPT = """你是一位资深 AI 行业分析师，每天为读者精选当日全球 AI 圈最有价值的新闻。

筛选标准（按优先级）：
1. 信息增量：揭示新事实、新数据、新模型、新产品发布、新政策的优先
2. 影响力：来自一线公司/研究机构/知名研究员的优先
3. 技术深度：有具体方法、数据、benchmark 的优先于纯观点稿
4. 多样性：避免同一事件多条入选；不同分类要均衡
5. 视觉性：在质量相近时，**优先选择带图片的资讯**（候选项 has_image=true）

硬性约束：
- 入选 10 条中**必须有 2-4 条带图**（has_image=true 的）
- 如果带图候选不足，可以下调一些，但不能为 0；如果带图候选很多，也别全选带图的

剔除标准：
- 营销软文、个人观点博客、低质量重复内容
- 已经在更早日期报道过的旧闻（除非有重大新进展）

输出语言：中文摘要。"""


USER_TEMPLATE = """以下是过去 24 小时采集到的 {n_items} 条 AI 资讯候选。请：

1. 从中筛选最值得阅读的 {top_k} 条
2. 给每条写一段 80-150 字的中文摘要（说清"是什么、谁做的、为什么重要"）
3. 给每条打一个分类标签，必须从以下选项中选一个：{categories}

候选列表（JSON 数组）：
```json
{candidates_json}
```

请按以下 JSON 格式返回（只返回 JSON，不要其他文字）：
```json
{{
  "selected": [
    {{
      "item_id": "候选项的 item_id",
      "summary": "80-150 字中文摘要",
      "tag": "{first_tag}",
      "rank": 1
    }}
  ]
}}
```

注意：
- rank 从 1 开始，按重要性排序
- item_id 必须严格来自候选列表
- 严格输出 {top_k} 条
"""


def filter_and_classify(items: list[Item], llm: LLMClient, top_k: int, categories: list[str]) -> list[Item]:
    if not items:
        return []
    if not categories:
        categories = ["论文研究", "产品发布", "行业动态", "工具开源"]

    # 构造给 LLM 的精简候选（不要把全部 raw_excerpt 都喂进去，控制 token）
    candidates = []
    n_with_image = 0
    for it in items:
        has_image = bool(it.images)
        if has_image:
            n_with_image += 1
        candidates.append(
            {
                "item_id": it.item_id,
                "source": it.source_label,
                "title": it.title,
                "url": it.url,
                "excerpt": truncate(it.raw_excerpt, 600),
                "published_at": it.published_at.isoformat() if it.published_at else None,
                "score_label": it.score_label,
                "has_image": has_image,
            }
        )
    log.info("候选含图: %d / %d", n_with_image, len(items))

    user = USER_TEMPLATE.format(
        n_items=len(items),
        top_k=top_k,
        categories=", ".join(categories),
        first_tag=categories[0],
        candidates_json=json.dumps(candidates, ensure_ascii=False, indent=2),
    )

    log.info("LLM filter: %d candidates → top %d", len(items), top_k)
    raw = llm.complete(SYSTEM_PROMPT, user, json_mode=True)
    try:
        parsed = parse_json_loose(raw)
    except Exception as e:
        log.error("LLM JSON 解析失败: %s\n--- 原始 ---\n%s", e, raw[:1500])
        raise

    selected = parsed.get("selected") or []
    by_id = {it.item_id: it for it in items}
    out: list[Item] = []
    for picked in selected:
        iid = picked.get("item_id")
        it = by_id.get(iid)
        if not it:
            log.warning("LLM 返回了未知 item_id: %s", iid)
            continue
        it.summary = (picked.get("summary") or "").strip()
        tag = (picked.get("tag") or "").strip()
        it.tag = tag if tag in categories else categories[-1]
        it.rank = int(picked.get("rank") or (len(out) + 1))
        it.selected = True
        out.append(it)

    out.sort(key=lambda x: x.rank)
    log.info("LLM filter done: %d items selected", len(out))
    return out


def cap_image_count(items: list[Item], max_with_image: int = 4) -> None:
    """限制带图条数：超过 max_with_image 时按排名只保留前 max_with_image 条带图，其余清空。
    在 archive 之后调用（archive 会把全文里的图加回来，所以最后再 cap）。"""
    img_count = sum(1 for it in items if it.images)
    if img_count <= max_with_image:
        if img_count < 2:
            log.info("最终带图 %d 条（少于期望的 2 条，候选池图源不够）", img_count)
        else:
            log.info("最终带图 %d 条", img_count)
        return
    kept = 0
    for it in sorted(items, key=lambda x: x.rank):
        if it.images:
            if kept < max_with_image:
                kept += 1
            else:
                it.images = []
    log.info("图片后处理: %d → %d 条带图", img_count, max_with_image)
