"""Unit tests for dictionary functions."""

from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730225468"


def test_invert_edge() -> None:
    """Edge test for invert."""
    a: dict[str, str] = {}
    assert invert(a) == {}


def test_invert_use1() -> None:
    """Use test 1 for invert."""
    a: dict[str, str] = {"Olivia": "Colton", "Emily": "Bryan"}
    assert invert(a) == {"Colton": "Olivia", "Bryan": "Emily"}


def test_invert_use2() -> None:
    """Use test 2 for invert."""
    a: dict[str, str] = {"Pepperoni": "Pizza", "Peanut butter": "Jelly"}
    assert invert(a) == {"Pizza": "Pepperoni", "Jelly": "Peanut butter"}


def test_favorite_color_edge() -> None:
    """Edge test for favorite color."""
    input: dict[str, str] = {}
    assert favorite_color(input) == ""


def test_favorite_color_use1() -> None:
    """Use test 1 for favorite color."""
    input: dict[str, str] = {"Olivia": "Blue", "Colton": "Blue", "Emily": "Pink", "Bryan": "Green"}
    assert favorite_color(input) == "Blue"


def test_favorite_color_use2() -> None:
    """Use test 2 for favorite color."""
    input: dict[str, str] = {"Olivia": "Red", "Colton": "Yellow", "Emily": "Red", "Bryan": "Yellow"}
    assert favorite_color(input) == "Red"


def test_count_edge() -> None:
    """Edge test for count."""
    x: list[str] = []
    assert count(x) == {}


def test_count_use1() -> None:
    """Use test 1 for count."""
    x: list[str] = ["Olivia", "Colton", "Olivia", "Bryan"]
    assert count(x) == {"Olivia": 2, "Colton": 1, "Bryan": 1}


def test_count_use2() -> None:
    """Use test 2 for count."""
    x: list[str] = ["Emily", "Olivia", "Emily", "Emily"]
    assert count(x) == {"Emily": 3, "Olivia": 1}