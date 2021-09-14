"""Drawing forests in a loop."""

__author__ = "730225468"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

number: int = int(input("Depth: "))
space: str = "" + TREE


if number > 0:
    print(TREE)
    while number > 1:
        number = number - 1
        TREE = TREE + space
        print(TREE)
else:
    print(None)