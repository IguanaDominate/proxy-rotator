from __future__ import annotations

import asyncio
import re
from typing import Iterable

import aiohttp

from proxy_rotator.adapters.filesystem_store import FilesystemStore
from proxy_rotator.models.proxy import Proxy
from proxy_rotator.models.source import ProxySource

PROXY_RE = re.compile(r"(?P<ip>\d{1,3}(?:\.\d{1,3}){3}):(?P<port>\d{1,5})")


class ScraperService:
    def __init__(self, sources: list[ProxySource], store: FilesystemStore) -> None:
        self._sources = {s.name: s for s in sources}
        self._store = store

    async def collect(self, names: list[str] | None = None) -> list[Proxy]:
        targets = [self._sources[n] for n in (names or self._sources.keys()) if n in self._sources]
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=20)) as session:
            batches = await asyncio.gather(
                *(self._fetch(session, src) for src in targets), return_exceptions=True
            )
        out: list[Proxy] = []
        for batch in batches:
            if isinstance(batch, list):
                out.extend(batch)
        return self._dedupe(out)

    async def _fetch(self, session: aiohttp.ClientSession, src: ProxySource) -> list[Proxy]:
        async with session.get(src.url, headers={"User-Agent": "proxy-rotator/2.4"}) as resp:
            text = await resp.text()
        found: list[Proxy] = []
        for m in PROXY_RE.finditer(text):
            found.append(
                Proxy(
                    host=m.group("ip"),
                    port=int(m.group("port")),
                    protocol=src.protocol,
                    source=src.name,
                )
            )
        return found

    @staticmethod
    def _dedupe(items: Iterable[Proxy]) -> list[Proxy]:
        seen: set[tuple[str, int, str]] = set()
        out: list[Proxy] = []
        for p in items:
            key = (p.host, p.port, p.protocol)
            if key in seen:
                continue
            seen.add(key)
            out.append(p)
        return out

    def persist_pool(self, proxies: list[Proxy], output: str) -> None:
        self._store.write_lines(output, [p.as_url() for p in proxies])