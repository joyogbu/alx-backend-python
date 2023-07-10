#!/usr/bin/env python3
'''measure the execution time of an async function'''


import asyncio
import time
import tracemalloc


tracemalloc.start()
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    '''defining the function'''
    s = time.perf_counter()
    await wait_n(n, max_delay)
    t = time.perf_counter() - s
    return (t / n)