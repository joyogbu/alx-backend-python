#!/usr/bin/env python3
'''more annotations'''


from typing import Any, Mapping, TypeVar, Union


T = TypeVar("T")
def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> Union[Any, T]:
    '''defining the function'''
    if key in dct:
        return dct[key]
    else:
        return default
