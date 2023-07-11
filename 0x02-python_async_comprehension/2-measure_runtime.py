#!/usr/bin/env python3
'''run time for parallel comprehension'''


import asyncio
import time
from typing import Iterator, Generator, Iterable


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''defining the function'''
    res = []
    for i in range(4):
        t1 = time.perf_counter()
        res.append(asyncio.create_task(async_comprehension()))
        li = await asyncio.gather(*res)
        t2 = time.perf_counter() - t1
    return(t2)
