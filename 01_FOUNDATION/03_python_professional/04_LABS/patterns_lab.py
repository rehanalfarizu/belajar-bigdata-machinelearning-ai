"""Micro-lab standard-library untuk pola Python profesional."""

from __future__ import annotations

import asyncio
from collections.abc import Iterable, Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from time import perf_counter


@dataclass(frozen=True)
class Reading:
    sensor_id: str
    value: float

    def __post_init__(self) -> None:
        if not self.sensor_id:
            raise ValueError("sensor_id required")


def valid_numbers(lines: Iterable[str]) -> Iterator[float]:
    """Yield angka dari line nonempty; invalid text tetap failure yang terlihat."""
    for line in lines:
        text = line.strip()
        if text:
            yield float(text)


@contextmanager
def measured(label: str) -> Iterator[None]:
    started = perf_counter()
    print(f"start label={label}")
    try:
        yield
    finally:
        elapsed = perf_counter() - started
        print(f"finish label={label} elapsed={elapsed:.3f}s")


async def delayed_name(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return name


async def async_demo() -> list[str]:
    return list(
        await asyncio.gather(
            delayed_name("first", 0.02),
            delayed_name("second", 0.01),
        )
    )


def main() -> None:
    print(Reading(sensor_id="motor-1", value=27.5))
    stream = valid_numbers(["1", "", "2.5"])
    print("generator-created")
    print("values", list(stream))
    with measured("async-demo"):
        print("async-results", asyncio.run(async_demo()))


if __name__ == "__main__":
    main()
