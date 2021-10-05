"""List utility functions part 2."""

__author__ = "730225468"


def main() -> None:
    """Start of the functions."""
    print(only_evens([1, 2, 3, 4, 5]))
    print(sub([1, 2, 4, 15], 1, 3))
    print(concat([1, 2, 3, 4], [5, 6, 7, 8]))


def only_evens(list1: list[int]) -> list[int]:
    """Find only the even elements within a list."""
    i: int = 0
    list2: list[int] = []
    while i < len(list1):
        if list1[i] % 2 == 0:
            list2.append(list1[i])
        i += 1
    return list2


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


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Two lists that will come together."""
    both_lists: list[int] = []
    i: int = 0
    j: int = 0
    if list1 and list2 == 0:
        return []
    while i < len(list1):
        both_lists.append(list1[i])
        i += 1
    while j < len(list2):
        both_lists.append(list2[j])
        j += 1
    return both_lists


if __name__ == "__main__":
    main()