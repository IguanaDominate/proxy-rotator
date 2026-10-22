# Contributing to proxy-rotator

Thanks for wanting to help build proxy-rotator. This project is a Windows
desktop proxy generator + rotator, written in Python. It scrapes public
proxy sources, validates them concurrently, and exposes a rotator pool
for downstream tooling.

## Development setup

```powershell
git clone https://github.com/example/proxy-rotator
cd proxy-rotator
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Project layout

- `proxy_rotator/bootstrap/` — CLI entrypoint and app wiring
- `proxy_rotator/handlers/` — thin command handlers (no business logic)
- `proxy_rotator/services/` — scrapers, validators, rotator pool
- `proxy_rotator/models/` — dataclasses for proxies, sources, results
- `proxy_rotator/adapters/` — platform-specific IO (Windows registry, clipboard)
- `proxy_rotator/utils/` — parsing, logging, config helpers
- `tests/` — pytest suite

## Pull requests

- Keep handlers thin — push logic into `services/`.
- Add tests for any new scraper or validator.
- Run `pytest -q` before opening a PR.
- Use conventional commits (`feat:`, `fix:`, `chore:`).

## Reporting issues

Open a GitHub issue with the source URL, sample output, and Python version.
Never paste real proxy credentials from private pools.