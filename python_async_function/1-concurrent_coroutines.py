#!/usr/bin/env python3

"""
Ce module fournit une fonction qui  s'excute aléatoirement
et retourne les résultats
"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute wait_random n fois avec max_delay et retourne le resultat."""
    task = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(task):
        delay = await task
        for i, val in enumerate(delays):
            if delay < val:
                delays.insert(i, delay)
                break
        else:
            delays.append(delay)
    return delays
