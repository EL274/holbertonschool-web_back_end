#!/usr/bin/env python3
"""Define a asynchronous coroutine - async_generator"""


import asyncio
from random import uniform
from typing import Async_Generator


async def async_generator() -> Async_Generator[float, None, None]:
    """Wait 1 second, then yield a random number between 0 and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0.0, 10.0)
