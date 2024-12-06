#!/usr/bin/python3
"""
This module provides an asynchronous function to wait for a random delay.
"""

import asyncio
import random
"""Wait for a random delay up to max_delay seconds and return the delay."""

async def wait_random(max_delay: int = 10) -> float:
    sleep = random.uniform(0, max_delay)
    await asyncio.sleep(sleep)
    return sleep
