from __future__ import annotations

import asyncio
from dataclasses import dataclass

import aiohttp

from proxy_rotator.models.proxy import Proxy
from proxy_rotator.models.validation import ValidationConfig, ValidationResult
from proxy_rotator.utils.pool_io import read_pool, write_pool

CHECK_URL = "https://httpbin.org/ip"


class ValidatorService:
    def __init__(self, config: ValidationConfig) -> None:
        self._cfg = config

    def load_pool(self, path: str) -> list[Proxy]:
        return read_pool(path)

    def rewrite_pool(self, path: str, proxies: list[Proxy]) -> None:
        write_pool(path, proxies)

    async def validate_batch(self, proxies: list[Proxy]) -> list[ValidationResult]:
        sem = asyncio.Semaphore(self._cfg.concurrency)

        async def one(proxy: Proxy) -> ValidationResult:
            async with sem:
                return await self._check(proxy)

        return await asyncio.gather(*(one(p) for p in proxies))

    async def _check(self, proxy: Proxy) -> ValidationResult:
        timeout = aiohttp.ClientTimeout(total=self._cfg.timeout)
        try:
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(CHECK_URL, proxy=proxy.as_url()) as resp:
                    alive = resp.status == 200
                    return ValidationResult(
                        proxy=proxy,
                        alive=alive,
                        latency_ms=0 if not alive else int(resp.headers.get("X-Latency", 0)),
                    )
        except (aiohttp.ClientError, asyncio.TimeoutError):
            return ValidationResult(proxy=proxy, alive=False, latency_ms=-1)