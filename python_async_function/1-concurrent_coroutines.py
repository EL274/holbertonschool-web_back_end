#!/usr/bin/python3

import random
from typing import list 
import asyncio

async def wait_random(max_delay: int) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> list [float]:
     tasks = [wait_random(max_delay) for _ in range (n)]
     delays = []
     for task in asyncio.as_completed (tasks):
          delay = await task 
          delays.append(delay)
          return(delays)
     