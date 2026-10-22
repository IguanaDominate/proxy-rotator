from __future__ import annotations

import asyncio
import click
from rich.console import Console

from proxy_rotator.bootstrap.container import build_container
from proxy_rotator.handlers.generate_handler import GenerateHandler
from proxy_rotator.handlers.validate_handler import ValidateHandler
from proxy_rotator.handlers.rotate_handler import RotateHandler

console = Console()


@click.group()
def main() -> None:
    """proxy-rotator — generate, validate, and rotate proxies."""


@main.command("generate")
@click.option("--sources", "-s", multiple=True, help="Source names to scrape")
@click.option("--limit", "-l", default=200, help="Max proxies to keep")
@click.option("--output", "-o", default="proxy_output/pool.txt")
def generate(sources: tuple[str, ...], limit: int, output: str) -> None:
    container = build_container()
    handler = GenerateHandler(container.scraper_service, container.validator_service)
    result = asyncio.run(handler.run(list(sources), limit, output))
    console.print(f"[green]wrote {result.written} proxies -> {output}[/green]")


@main.command("validate")
@click.argument("pool_file")
def validate(pool_file: str) -> None:
    container = build_container()
    handler = ValidateHandler(container.validator_service)
    result = asyncio.run(handler.run(pool_file))
    console.print(f"[cyan]alive={result.alive} dead={result.dead}[/cyan]")


@main.command("rotate")
@click.argument("pool_file")
@click.option("--count", "-n", default=1)
def rotate(pool_file: str, count: int) -> None:
    container = build_container()
    handler = RotateHandler(container.rotator_service)
    for proxy in handler.pull(pool_file, count):
        console.print(proxy.as_url())


if __name__ == "__main__":
    main()