#!/usr/bin/env python3
"""Definie une coroutine asynchrone - async_comprehension"""


import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collecte 10 nombres utilisant une async comprehensing"""
    return [num async for num in async_generator()]
