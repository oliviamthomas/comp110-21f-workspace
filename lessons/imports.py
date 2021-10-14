"""Examples of imports."""

from lessons import helpers

# Import using an alias
from lessons import helpers as hp

# Import names directly from gobals of a module
from lessons.helpers import THE_ANSWER, powerful


def main() -> None:
    # Acess the first import
    print(helpers.powerful(2, 4))

    # Access the aliased import
    print(hp.THE_ANSWER)

    # Call the imported function directly
    print(powerful(2, 10))
    print(THE_ANSWER)

    print(f"imports.py: {__name__}")


if __name__ == "__main__":
    main()