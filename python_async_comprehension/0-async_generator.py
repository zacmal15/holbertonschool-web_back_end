#!/usr/bin/env python3
"""This module defines an asynchronous generator."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield ten random numbers between zero and ten."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
