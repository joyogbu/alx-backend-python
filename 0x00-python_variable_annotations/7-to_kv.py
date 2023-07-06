#!/usr/bin/env python3
'''take a string and integer/float and return a tuple'''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''defining the function'''
    return (k, v*v)
