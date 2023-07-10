#!/usr/bin/env python3
'''asynchronous co routine that takes an integer,'''


import asyncio
import random


async def wait_random(max_delay: int = 10):
    '''defining the function'''
    # for i in range(0, max_delay):
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return (i)
