#!/usr/bin/env python3
'''asynchronous routine that returns a list of all delays'''


import random
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''defining the function'''
    group = []
    for i in range(n):
        group.append(asyncio.create_task(wait_random(max_delay)))
        li = await asyncio.gather(*group)
        if li == 'None' or li == []:
            return []
    return (li)
