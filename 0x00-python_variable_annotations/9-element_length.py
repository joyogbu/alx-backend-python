#!/usr/bin/env python3
'''function return type annotations'''


from typing import List, Sequence, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''defining the function'''
    return [(i, len(i)) for i in lst]
