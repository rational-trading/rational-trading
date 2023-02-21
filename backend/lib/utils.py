
from typing import Optional, TypeVar


T = TypeVar("T")


def guardNone(input: Optional[T]) -> T:
    assert input is not None
    return input
