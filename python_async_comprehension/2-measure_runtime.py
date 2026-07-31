#!/usr/bin/env python3
"""Measure the runtime of parallel asynchronous comprehensions."""

import asyncio
import time

async_comprehension = __import__(
    '1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run four async comprehensions in parallel and return the runtime."""
    start_time = time.time()

    await asyncio.gather(
        *[async_comprehension() for i in range(4)]
    )

    return time.time() - start_time
