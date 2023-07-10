#!/usr/bin/env python3
'''asynchronous routine that returns a list of all delays'''


import random
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    while True:
        for i in range(n):
            # await asyncio.sleep(max_delay)
            group = asyncio.create_task(wait_random(max_delay))
            #li = await asyncio.gather(wait_random(max_delay))
            li = await asyncio.gather(group)
        return (li)
