"""Practice functions for quiz 3."""


def main() -> None:
    """Entrypoint."""
    print(dict_transform({2: [1, 2], 5: [3, 4]}))
    print(average_grades({"Bill": [75, 94, 97], "Annie": [88, 93, 99]}))


def dict_transform(d: dict[int, list[int]]) -> dict[int, list[int]]:
    """Returns a dict with every value in a list multiplied by its corresponding key."""
    result: dict[int, list[int]] = {}
    for key in d:
        result[key] = [(d[key][0] * key), (d[key][1] * key)]
        
    return result


def average_grades(x: dict[str, list[int]]) -> dict[str, float]:
    """Map of each student's average grade."""
    result: dict[str, float] = {}
    for key in x:
        result[key] = ((x[key][0] + x[key][1] + x[key][2]) / 3)

    return result


if __name__ == "__main__":
    main()
