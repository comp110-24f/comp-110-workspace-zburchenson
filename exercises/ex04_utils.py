"""List Utils"""

__author__ = "730753141"


def all(values: list[int], num1: int) -> bool:
    """return a bool"""

    idx: int = 0
    truevals: int = 0

    while idx < len(values):
        if values[idx] == num1:
            truevals += 1
        idx += 1

    if truevals == len(values):
        return True
    else:
        return False


def max(values: list[int]) -> int:
    """return largest int in list"""
    if len(values) == 0:
        raise ValueError("max() arg is an empty list")

    idx: int = 0
    max_int: int = 0

    while idx < len(values):
        if values[idx] > max_int:
            max_int = values[idx]
        idx += 1

    return max_int


def is_equal(values1: list[int], values2: list[int]) -> bool:
    """return true is every element is equal in both lists"""

    i: int = 0
    all_match: bool = True

    while i < len(values1) and i < len(values2):
        if values1[i] != values2[i]:
            all_match = False
        i += 1

    if all_match and len(values1) == len(values2):
        return True
    else:
        return False


def extend(values1: list[int], values2: list[int]) -> None:
    """append val2 to val1"""
    idx: int = 0

    while idx < len(values2):
        values1.append(values2[idx])
        idx += 1

    print(values1)


a: list[int] = [1, 2, 3]
b: list[int] = [4, 5, 6]
c: list[int] = [7, 8]

print(extend(c, b))
