#!/usr/bin/env python3
"""Measure the runtime of parallel asynchronous comprehensions."""

import asyncio
import time

async_comprehension = __import__(
    '1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run four asynchronous comprehensions and return the runtime."""
    start = time.time()

    await asyncio.gather(
        *(async_comprehension() for i in range(4))
    )

    return time.time() - start
