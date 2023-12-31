#!/usr/bin/env python3
'''async comprehension'''


import asyncio
from typing import Generator, Iterator, Iterable, List, Awaitable


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''defining the function'''
    numbers = [i async for i in async_generator()]
    return (numbers)
