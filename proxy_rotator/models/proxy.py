from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Proxy:
    host: str
    port: int
    protocol: str = "http"
    source: str = "unknown"

    def as_url(self) -> str:
        return f"{self.protocol}://{self.host}:{self.port}"

    def as_hostport(self) -> str:
        return f"{self.host}:{self.port}"

    @classmethod
    def parse(cls, line: str, source: str = "pool") -> "Proxy":
        raw = line.strip()
        if "://" in raw:
            proto, rest = raw.split("://", 1)
        else:
            proto, rest = "http", raw
        host, port = rest.rsplit(":", 1)
        return cls(host=host, port=int(port), protocol=proto, source=source)