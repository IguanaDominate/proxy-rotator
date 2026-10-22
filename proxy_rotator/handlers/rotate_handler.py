from __future__ import annotations

from proxy_rotator.services.rotator_service import RotatorService
from proxy_rotator.models.proxy import Proxy


class RotateHandler:
    def __init__(self, rotator: RotatorService) -> None:
        self._rotator = rotator

    def pull(self, pool_file: str, count: int) -> list[Proxy]:
        return self._rotator.next_batch(pool_file, count)