"""List utility functions part 2."""

__author__ = "730225468"


def only_evens(list1: list[int]) -> list[int]:
    """Find only the even elements within a list."""
    i: int = 0
    list2: list[int] = []

    while i < len(list1):
        if list1[i] % 2 == 0:
            list2.append(list1[i])
        i += 1
    return list2


print(only_evens([1, 2, 3, 4, 5]))


def sub(list1: list[int], i_start: int, i_end: int) -> list[int]:
    """Subset of a given list."""
    i_low = i_start
    i_high = i_end
    list2: list[int] = []
    if len(list1) == 0:
        return[]
    if i_high + 1 > len(list1):
        i_high = len(list1)
    if i_low < 0:
        i_low = 0
    while i_low < i_high:
        list2.append(list1[i_low])
        i_low += 1
    return list2
        

print(sub([1, 2, 4, 15], 1, 3))


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