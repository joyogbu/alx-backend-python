#!/usr/bin/env python3
'''take a string and integer/float and return a tuple'''


from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    '''defining the function'''
    return (k, v*v)
