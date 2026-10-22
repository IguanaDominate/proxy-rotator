from __future__ import annotations

from dataclasses import dataclass

from proxy_rotator.adapters.filesystem_store import FilesystemStore
from proxy_rotator.adapters.windows_clipboard import WindowsClipboardAdapter
from proxy_rotator.services.scraper_service import ScraperService
from proxy_rotator.services.validator_service import ValidatorService
from proxy_rotator.services.rotator_service import RotatorService
from proxy_rotator.utils.config_loader import load_config


@dataclass
class Container:
    scraper_service: ScraperService
    validator_service: ValidatorService
    rotator_service: RotatorService
    clipboard: WindowsClipboardAdapter
    store: FilesystemStore


def build_container() -> Container:
    cfg = load_config()
    store = FilesystemStore(cfg.output_dir)
    scraper = ScraperService(cfg.sources, store)
    validator = ValidatorService(cfg.validation)
    rotator = RotatorService(store)
    clipboard = WindowsClipboardAdapter()
    return Container(scraper, validator, rotator, clipboard, store)