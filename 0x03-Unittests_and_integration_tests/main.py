#!/usr/bin/env python3
'''main function'''


from utils import access_nested_map


print(access_nested_map({"a": 1}, ("a",)))
print(access_nested_map({"a": {"b": 2}}, ("a",)))
print(access_nested_map({"a": {"b": 2}}, ("a", "b")))
