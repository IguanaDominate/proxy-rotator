from __future__ import annotations

from dataclasses import dataclass

from proxy_rotator.models.proxy import Proxy


@dataclass(frozen=True, slots=True)
class ValidationConfig:
    concurrency: int = 50
    timeout: float = 8.0
    check_url: str = "https://httpbin.org/ip"


@dataclass(frozen=True, slots=True)
class ValidationResult:
    proxy: Proxy
    alive: bool
    latency_ms: int = 0