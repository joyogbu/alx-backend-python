#!/usr/bin/env python3
'''co-routine asynchronous generator that takes no argument'''


import asyncio
import random
from typing import Generator, Iterator


async def async_generator() -> Generator[float, float, None]:
    '''defining the function'''
    for i in range(10):
        i = random.uniform(0, 10)
        # for i in range(10):
        # yield i
        await asyncio.sleep(1)
        yield i
