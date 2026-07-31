#!/usr/bin/env python3
"""Module that measures asynchronous comprehension runtime."""

import asyncio
import time

async_comprehension = __import__(
    '1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute four asynchronous comprehensions and return their runtime."""
    start_time = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    return time.time() - start_time
