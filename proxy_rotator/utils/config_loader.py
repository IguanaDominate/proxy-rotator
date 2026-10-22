from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

from proxy_rotator.models.source import ProxySource
from proxy_rotator.models.validation import ValidationConfig

DEFAULT_CONFIG = Path("config/sources.yaml")


@dataclass
class AppConfig:
    output_dir: str = "proxy_output"
    sources: list[ProxySource] = field(default_factory=list)
    validation: ValidationConfig = field(default_factory=ValidationConfig)


def load_config(path: Path | None = None) -> AppConfig:
    p = path or DEFAULT_CONFIG
    if not p.exists():
        return AppConfig(sources=_builtin_sources())
    data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    sources = [
        ProxySource(
            name=item["name"],
            url=item["url"],
            protocol=item.get("protocol", "http"),
            enabled=item.get("enabled", True),
        )
        for item in data.get("sources", [])
    ]
    validation = ValidationConfig(**(data.get("validation") or {}))
    return AppConfig(
        output_dir=data.get("output_dir", "proxy_output"),
        sources=sources or _builtin_sources(),
        validation=validation,
    )


def _builtin_sources() -> list[ProxySource]:
    return [
        ProxySource(name="free-proxy-list", url="https://free-proxy-list.net/"),
        ProxySource(name="proxy-list-download", url="https://www.proxy-list.download/api/v1/get?type=http"),
        ProxySource(name="openproxy-list", url="https://openproxy.space/list/http"),
    ]