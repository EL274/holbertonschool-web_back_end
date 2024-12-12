#!/usr/bin/env python3
"""Define a asynchronous coroutine - measure_runtime"""


import asyncio
import time
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Return the execution time of async_comprehension 4 times"""
    t1 = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    t2 = time.time()

    return t2 - t1
