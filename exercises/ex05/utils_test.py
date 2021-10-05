"""Unit tests for list utility functions."""


from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730225468"


def test_only_evens() -> None:
    list1: list[int] = []
    assert only_evens(list1) == []


def test_sub() -> None:
    list1: list[int] = []
    assert sub(list1) == []


def test_concat() -> None:
    list1: list[int] = []
    list2: list[int] = []
    assert concat(list1, list2) == []