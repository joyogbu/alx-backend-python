#!/usr/bin/env python3
'''alter a function to a new function'''

import random
import asyncio
from typing import List


task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''defining the function'''
    group = []
    for i in range(n):
        group.append(asyncio.create_task(task_wait_random(max_delay)))
        li = await asyncio.gather(*group)
        if li == 'None' or li == []:
            return []
    return (li)
