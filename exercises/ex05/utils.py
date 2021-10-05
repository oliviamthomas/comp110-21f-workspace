"""List utility functions part 2."""

__author__ = "730225468"


def only_evens(list1: list[int]) -> list[int]:
    """Find only the even elements within a list."""
    i: int = 0
    list2: list[int] = []

    while i < len(list1):
        if list1[i] % 2:
            list2.append(list1[i])
        i += 1
    return list2


print(only_evens([1, 2, 3, 4, 5]))


def sub(list1: list[int]) -> list[int]:
    """Subset of a given list."""
    i_start: int = 0
    i_end: int = 10

    while i_start < len(list1):
        if len(list1) < i_end:
            list1[i_start] += 1
            i_start += 2
        else:
            return list1
    return list1


print(sub([1, 2, 4, 15]))


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Two lists that will come together."""
    both_lists: list[int] = []
    i: int = 0
    i2: int = 0
    while i < 4:
        list1.append(i)
        i += 1
    while i2 < 4:
        list2.append(i2)
        i2 += 2
    return both_lists


print(concat([1, 2, 3, 4], [5, 6, 7, 8]))