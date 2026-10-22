from __future__ import annotations

from dataclasses import dataclass, field

from proxy_rotator.services.scraper_service import ScraperService
from proxy_rotator.services.validator_service import ValidatorService


@dataclass
class GenerateResult:
    written: int = 0
    alive: int = 0
    dead: int = 0
    by_source: dict[str, int] = field(default_factory=dict)


class GenerateHandler:
    def __init__(self, scraper: ScraperService, validator: ValidatorService) -> None:
        self._scraper = scraper
        self._validator = validator

    async def run(self, sources: list[str], limit: int, output: str) -> GenerateResult:
        raw = await self._scraper.collect(sources or None)
        candidates = raw[: max(limit * 3, limit)]
        validated = await self._validator.validate_batch(candidates)
        alive = [r.proxy for r in validated if r.alive][:limit]
        self._scraper.persist_pool(alive, output)
        return GenerateResult(
            written=len(alive),
            alive=len(alive),
            dead=len([r for r in validated if not r.alive]),
            by_source={s: len([p for p in alive if p.source == s]) for s in (sources or [])},
        )