#!/usr/bin/env python3

import asyncio
from typing import List
async_generator = __import__('0-async_generator.py').async_generator


async def async_comprehension() -> List[float]:
    """Collecte 10 nombres aléatoires à l'aide d'une compréhension"""
    return [number async for number in async_generator()]
