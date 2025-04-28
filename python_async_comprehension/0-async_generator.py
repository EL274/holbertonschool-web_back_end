#!/usr/bin/env python3
"""Definie une coroutine asynchrone - async_generator"""


import asyncio
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Attendez 1 seconde, puis donne un nombre aléatoire entre 0 et 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0.0, 10.0)
