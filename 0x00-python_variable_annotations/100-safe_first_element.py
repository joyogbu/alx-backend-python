#!/usr/bin/env python3
'''sequence annotations'''


from typing import Optional, Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''defining the function'''
    if lst:
        return lst[0]
    else:
        return None
