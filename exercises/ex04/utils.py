"""List utility functions."""

__author__ = "730225468"


def all(x: list[int], y: int) -> bool:
    """A list of ints that will result in True if all int values are the same."""
    length: int = len(x)
    y: int = 1
    if length == y:
        return True
    else:
        return False


x: list[int] = [1, 5]
print(x)
