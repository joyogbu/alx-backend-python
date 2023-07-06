#!/usr/bin/env python3
'''mixed list annotations'''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''defining the function'''
    total = 0.0
    for num in mxd_lst:
        total += num
    return (total)
