"""Unit tests for list utility functions."""


from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730225468"


def test_only_evens() -> None:
    list1: list[int] = []
    assert only_evens(list1) == []


def test_sub_edge() -> None:
    list1: list[int] = []
    i_start: int = 1
    i_end: int = 5
    assert sub(list1, i_start, i_end) == [2, 4]


def test_sub_use1() -> None:
    list1: list[int] = []
    i_start: int = 1
    i_end: int = 3
    assert sub(list1, i_start, i_end) == [2, 4]


# def test_sub_use2() -> None:
    # list1: list[int] = []
    # i_start: int = 2
    # i_end: int = 4
    # assert sub(list1, i_start, i_end) == [3, 5]


def test_concat() -> None:
    list1: list[int] = []
    list2: list[int] = []
    assert concat(list1, list2) == []