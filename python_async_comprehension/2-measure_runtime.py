#!/usr/bin/env python3
"""Module containing an asynchronous generator."""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """This function measure time it takes to excecute all async func"""
    start_time: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time: float = time.perf_counter()
    return end_time - start_time

if __name__ == "__main__":
    print(asyncio.run(measure_runtime()))
