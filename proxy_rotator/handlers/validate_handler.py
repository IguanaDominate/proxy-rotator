from __future__ import annotations

from dataclasses import dataclass

from proxy_rotator.services.validator_service import ValidatorService


@dataclass
class ValidateResult:
    alive: int = 0
    dead: int = 0


class ValidateHandler:
    def __init__(self, validator: ValidatorService) -> None:
        self._validator = validator

    async def run(self, pool_file: str) -> ValidateResult:
        proxies = self._validator.load_pool(pool_file)
        results = await self._validator.validate_batch(proxies)
        alive = [r for r in results if r.alive]
        dead = [r for r in results if not r.alive]
        self._validator.rewrite_pool(pool_file, [r.proxy for r in alive])
        return ValidateResult(alive=len(alive), dead=len(dead))