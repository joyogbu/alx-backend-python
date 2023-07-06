#!/usr/bin/env python3
'''take an input float list and return their float sum'''


from typing import List
def sum_list(input_list: List[float]) -> float:
    '''defining the function'''
    total = 0
    for x in input_list:
        total += x
    return (total)

