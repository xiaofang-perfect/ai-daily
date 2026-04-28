"""飞书群机器人通知。支持签名校验。"""
from __future__ import annotations

import base64
import hashlib
import hmac
import os
import time
from typing import Any

import httpx

from scripts.sources.base import Item
from scripts.utils import env_get, log, truncate


def _sign(secret: str, ts: int) -> str:
    """飞书自定义机器人签名：base64(hmac_sha256(timestamp + '\n' + secret, ''))"""
    string_to_sign = f"{ts}\n{secret}"
    h = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()
    return base64.b64encode(h).decode("utf-8")


def send_feishu(date_label: str, items: list[Item], site_url: str = "") -> bool:
    webhook = env_get("FEISHU_WEBHOOK_URL").strip()
    secret = env_get("FEISHU_WEBHOOK_SECRET").strip()
    if not webhook:
        log.info("FEISHU_WEBHOOK_URL not set, skipping notify")
        return False

    payload: dict[str, Any] = {
        "msg_type": "interactive",
        "card": _build_card(date_label, items, site_url),
    }
    if secret:
        ts = int(time.time())
        payload["timestamp"] = str(ts)
        payload["sign"] = _sign(secret, ts)

    try:
        with httpx.Client(timeout=15.0) as c:
            r = c.post(webhook, json=payload)
            data = r.json() if r.headers.get("content-type", "").startswith("application/json") else {}
            if data.get("StatusCode") == 0 or data.get("code") == 0 or r.status_code == 200 and not data.get("code"):
                log.info("feishu notify ok")
                return True
            log.warning("feishu notify failed: %s %s", r.status_code, r.text[:300])
            return False
    except Exception as e:
        log.warning("feishu notify exception: %s", e)
        return False


def _build_card(date_label: str, items: list[Item], site_url: str) -> dict[str, Any]:
    elements: list[dict[str, Any]] = [
        {
            "tag": "div",
            "text": {
                "tag": "lark_md",
                "content": f"**{date_label} · 共 {len(items)} 条精选**",
            },
        },
        {"tag": "hr"},
    ]

    for it in items:
        line = f"**#{it.rank} `{it.tag}`** {it.title}\n[{it.source_label}]({it.url})"
        if it.summary:
            line += f"\n{truncate(it.summary, 200)}"
        elements.append({"tag": "div", "text": {"tag": "lark_md", "content": line}})
        elements.append({"tag": "hr"})

    if site_url:
        elements.append(
            {
                "tag": "action",
                "actions": [
                    {
                        "tag": "button",
                        "text": {"tag": "plain_text", "content": "查看完整日报"},
                        "url": site_url,
                        "type": "primary",
                    }
                ],
            }
        )

    return {
        "config": {"wide_screen_mode": True},
        "header": {
            "title": {"tag": "plain_text", "content": f"📰 每日 AI 资讯 · {date_label}"},
            "template": "blue",
        },
        "elements": elements,
    }
