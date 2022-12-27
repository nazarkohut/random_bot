from typing import Tuple


def read_and_swap(data) -> Tuple[any, any, bool]:
    a, b = map(int, data) if len(data) == 2 else map(int, data[1:])
    swapped = False
    if a > b:
        swapped = True
        a, b = b, a
    return a, b, swapped
