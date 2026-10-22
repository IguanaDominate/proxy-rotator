from __future__ import annotations

from pathlib import Path

from proxy_rotator.models.proxy import Proxy


def read_pool(path: str) -> list[Proxy]:
    p = Path(path)
    if not p.exists():
        return []
    out: list[Proxy] = []
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            out.append(Proxy.parse(line))
        except ValueError:
            continue
    return out


def write_pool(path: str, proxies: list[Proxy]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("\n".join(x.as_url() for x in proxies) + "\n", encoding="utf-8")