#!/usr/bin/env python3

"""
Ce module fournit une fonction  asynchrone pour attendre un délai aléatoire.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """attendre un delai aléatoire jusqu'au max_delay secondes et retourne le delai."""
    sleep = random.uniform(0, max_delay)
    await asyncio.sleep(sleep)
    return sleep
