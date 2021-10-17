"""Practice with dictionaries."""

__author__ = "730225468"


def main() -> None:
    print(invert({"Olivia": "Colton", "Emily": "Bryan"}))
    print(favorite_color({"Olivia": "Blue", "Colton": "Blue", "Emily": "Pink", "Bryan": "Green"}))
    print(count(["Olivia", "Colton", "Olivia", "Bryan"]))


def invert(a: dict[str, str]) -> dict[str, str]:
    """Invert keys and values in a dictionary."""
    result: dict[str, str] = {}
    for key in a:
        value = a[key]
        if value in result:
            raise KeyError("The two keys cannot be the same")
        result[value] = key
    
    return result


def favorite_color(input: dict[str, str]) -> str:
    """Results in the color that appears most frequently."""
    color_counts: dict[str, int] = {}
    for person in input:
        color = input[person]
        if color not in color_counts:
            color_counts[color] = 1 
            # adding new row
        else: 
            color_counts[color] += 1 
            # adding one to the value of the row that is already there
    maximum: int = 0
    # lowest possible number 
    winning_color: str = ""
    for key in color_counts:
        if color_counts[key] > maximum:
            maximum = color_counts[key]
            winning_color = key

    return winning_color


def count(x: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    item: str = ""
    for item in x:
        if item not in result:
            result[item] = 1
        else:
            result[item] += 1

    return result


if __name__ == "__main__":
    main()