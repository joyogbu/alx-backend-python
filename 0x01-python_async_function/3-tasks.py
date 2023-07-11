#!/usr/bin/env python3
'''funtion that takes an integer and return an ascencio.task'''


import asyncio
from typing import Awaitable, Any, Callable, Coroutine


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''defining the function'''
    return asyncio.ensure_future(wait_random(max_delay))
