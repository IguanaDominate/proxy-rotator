from __future__ import annotations

from pathlib import Path


class FilesystemStore:
    def __init__(self, base_dir: str = "proxy_output") -> None:
        self._base = Path(base_dir)
        self._base.mkdir(parents=True, exist_ok=True)

    def path_for(self, relative: str) -> Path:
        p = self._base / relative
        p.parent.mkdir(parents=True, exist_ok=True)
        return p

    def write_lines(self, relative: str, lines: list[str]) -> None:
        self.path_for(relative).write_text("\n".join(lines) + "\n", encoding="utf-8")

    def read_lines(self, relative: str) -> list[str]:
        p = self.path_for(relative)
        if not p.exists():
            return []
        return [l.strip() for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]