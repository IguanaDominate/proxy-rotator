import pytest

from proxy_rotator.services.scraper_service import ScraperService
from proxy_rotator.adapters.filesystem_store import FilesystemStore
from proxy_rotator.models.proxy import Proxy


def test_dedupe_removes_duplicates() -> None:
    items = [
        Proxy("1.1.1.1", 80, "http", "a"),
        Proxy("1.1.1.1", 80, "http", "b"),
        Proxy("2.2.2.2", 8080, "http", "a"),
    ]
    out = ScraperService._dedupe(items)
    assert len(out) == 2


@pytest.mark.asyncio
async def test_persist_pool(tmp_path) -> None:
    store = FilesystemStore(str(tmp_path))
    svc = ScraperService([], store)
    svc.persist_pool([Proxy("1.1.1.1", 80)], "pool.txt")
    written = (tmp_path / "pool.txt").read_text(encoding="utf-8")
    assert "http://1.1.1.1:80" in written