"""
Define guardNone function to be used in polygon_api.py
"""


from typing import Optional, TypeVar


T = TypeVar("T")


def guardNone(input: Optional[T]) -> T:
    assert input is not None
    return input
