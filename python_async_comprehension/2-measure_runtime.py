#!/usr/bin/env python3
"""Module that measures the runtime of async comprehensions."""

import asyncio
import time

async_comprehension = __import__(
    "1-async_comprehension"
).async_comprehension


async def measure_runtime() -> float:
    """Execute four async comprehensions concurrently and return the runtime."""
    start = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end = time.perf_counter()

    return end - start
