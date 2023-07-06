#!/usr/bin/env python3
'''take a float and returns a function that multiplies the float'''



def func(x: float) -> float:
    return (x)
def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return (func(multiplier))
