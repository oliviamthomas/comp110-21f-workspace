"""Unit tests for list utility functions."""


from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730225468"


def test_only_evens_edge() -> None:
    """Edge test for only evens."""
    list1: list[int] = []
    assert only_evens(list1) == []


def test_only_evens_use1() -> None:
    """Use test 1 for only evens."""
    list1: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(list1) == [2, 4]


def test_only_evens_use2() -> None:
    """Use test 2 for only evens."""
    list1: list[int] = [6, 7, 8, 9, 10]
    assert only_evens(list1) == [6, 8, 10]


def test_sub_edge() -> None:
    """Edge test for sub."""
    list1: list[int] = []
    i_start: int = 1
    i_end: int = 5
    assert sub(list1, i_start, i_end) == []


def test_sub_use1() -> None:
    """Use test 1 for sub."""
    list1: list[int] = [0, 2, 4, 6]
    i_start: int = 1
    i_end: int = 3
    assert sub(list1, i_start, i_end) == [2, 4]


def test_sub_use2() -> None:
    """Use test 2 for sub."""
    list1: list[int] = [1, 3, 5, 7, 9]
    i_start: int = 2
    i_end: int = 4
    assert sub(list1, i_start, i_end) == [5, 7]


def test_concat_edge() -> None:
    """Edge test for concat."""
    list1: list[int] = []
    list2: list[int] = []
    assert concat(list1, list2) == []


def test_concat_use1() -> None:
    """Use test 1 for concat."""
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [4, 5, 6]
    assert concat(list1, list2) == [1, 2, 3, 4, 5, 6]


def test_concat_use2() -> None:
    """Use test 2 for concat."""
    list1: list[int] = [10, 20, 30]
    list2: list[int] = [40, 50, 60]
    assert concat(list1, list2) == [10, 20, 30, 40, 50, 60]
