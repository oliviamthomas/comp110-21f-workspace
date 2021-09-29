"""List utility functions."""

__author__ = "730225468"


def all(x: list[int], y: int) -> bool:
    """A list of ints that will return True if all int values are the same."""
    index: int = 0
    while index < len(x):
        if x[index] == y:
            index += 1
        if x[index] != y:
            return False
    return True    


print(all([1, 1, 2, 1], 1))


def is_equal(x: list[int], y: list[int]) -> bool:
    """Two lists of ints that will return True if both lists are the same."""
    index: int = 0
    while index < len(y):
        if x[index] != y[index]:
            return False
        if x[index] == y[index]:
            index += 1
    return True


print(is_equal([1, 1, 2], [1, 1, 2]))


def max(input: list[int]) -> int:
    """Return the largest integer in a list of int values."""
    i: int = 0
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    maximum: int = input[0]
    while i < len(input):
        if input[i] > maximum:
            maximum = input[i]
        i += 1
    return maximum


print(max([2, 3, 10]))