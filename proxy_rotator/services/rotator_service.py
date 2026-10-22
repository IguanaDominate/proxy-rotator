from __future__ import annotations

import random
import time

from proxy_rotator.adapters.filesystem_store import FilesystemStore
from proxy_rotator.models.proxy import Proxy
from proxy_rotator.utils.pool_io import read_pool


class RotatorService:
    def __init__(self, store: FilesystemStore, cooldown_s: float = 30.0) -> None:
        self._store = store
        self._cooldown_s = cooldown_s
        self._last_used: dict[tuple[str, int], float] = {}

    def next_batch(self, pool_file: str, count: int) -> list[Proxy]:
        pool = read_pool(pool_file)
        now = time.monotonic()
        ready = [p for p in pool if now - self._last_used.get((p.host, p.port), 0) > self._cooldown_s]
        if not ready:
            ready = pool
        random.shuffle(ready)
        picked = ready[:count]
        for p in picked:
            self._last_used[(p.host, p.port)] = now
        return picked