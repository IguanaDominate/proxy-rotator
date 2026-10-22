from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProxySource:
    name: str
    url: str
    protocol: str = "http"
    enabled: bool = True
    weight: float = 1.0