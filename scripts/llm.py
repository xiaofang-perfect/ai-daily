"""LLM 多 provider 适配。OpenAI 兼容（DeepSeek/OpenAI/通义/Moonshot/智谱）+ Anthropic。"""
from __future__ import annotations

import json
import os
import re
from typing import Any

from scripts.utils import env_get, log


class LLMClient:
    def __init__(self, conf: dict[str, Any]):
        self.provider: str = conf.get("provider", "openai_compatible")
        self.model: str = conf.get("model", "deepseek-chat")
        self.base_url: str = conf.get("base_url", "")
        self.temperature: float = conf.get("temperature", 0.3)
        self.max_tokens: int = conf.get("max_tokens", 8000)
        self.api_key: str = env_get("LLM_API_KEY")
        if not self.api_key:
            raise RuntimeError("LLM_API_KEY 未设置")
        self._client = self._build_client()

    def _build_client(self):
        if self.provider in ("openai_compatible", "openai"):
            from openai import OpenAI
            kwargs: dict[str, Any] = {"api_key": self.api_key}
            if self.base_url:
                kwargs["base_url"] = self.base_url
            return OpenAI(**kwargs)
        if self.provider == "anthropic":
            import anthropic
            kwargs: dict[str, Any] = {"api_key": self.api_key}
            if self.base_url and self.base_url != "https://api.anthropic.com":
                kwargs["base_url"] = self.base_url
            return anthropic.Anthropic(**kwargs)
        raise ValueError(f"unknown provider: {self.provider}")

    # ------------------------------------------------------------------
    def complete(self, system: str, user: str, json_mode: bool = False) -> str:
        if self.provider in ("openai_compatible", "openai"):
            return self._openai_complete(system, user, json_mode)
        if self.provider == "anthropic":
            return self._anthropic_complete(system, user, json_mode)
        raise ValueError(self.provider)

    def _openai_complete(self, system: str, user: str, json_mode: bool) -> str:
        kwargs: dict[str, Any] = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }
        if json_mode:
            # DeepSeek/OpenAI 都支持 response_format
            kwargs["response_format"] = {"type": "json_object"}
        try:
            r = self._client.chat.completions.create(**kwargs)
            return r.choices[0].message.content or ""
        except Exception as e:
            # 某些 provider 不支持 response_format，降级
            if json_mode and ("response_format" in str(e) or "unsupported" in str(e).lower()):
                kwargs.pop("response_format", None)
                r = self._client.chat.completions.create(**kwargs)
                return r.choices[0].message.content or ""
            raise

    def _anthropic_complete(self, system: str, user: str, json_mode: bool) -> str:
        if json_mode:
            user = user + "\n\n请只输出合法 JSON，不要任何前后缀文字、不要 markdown 代码块。"
        r = self._client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        # 取所有 text block
        return "".join(b.text for b in r.content if getattr(b, "type", "") == "text")


# ---------------- JSON 解析 ----------------
def parse_json_loose(text: str) -> Any:
    """尽量解析模型输出的 JSON，容忍 markdown 代码块包裹。"""
    if not text:
        raise ValueError("empty LLM output")
    text = text.strip()
    # 去掉 ```json ... ``` 这种包裹
    fence = re.search(r"```(?:json)?\s*(.+?)```", text, flags=re.DOTALL | re.IGNORECASE)
    if fence:
        text = fence.group(1).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # 兜底：找首尾大括号
        s, e = text.find("{"), text.rfind("}")
        if s != -1 and e != -1 and e > s:
            return json.loads(text[s : e + 1])
        s, e = text.find("["), text.rfind("]")
        if s != -1 and e != -1 and e > s:
            return json.loads(text[s : e + 1])
        log.error("LLM output is not valid JSON: %s", text[:500])
        raise
