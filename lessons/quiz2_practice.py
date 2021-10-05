"""Question 15 Function Writing Practice."""


def odd_and_even(list1: list[int]) -> list[int]:
    """Odd and even."""
    i: int = 0
    list2: list[int] = []

    while i < len(list1):
        if list1[i] % 2 == 1 and i % 2 == 0:
            list2.append(list1[i])
        i += 1
    
    return list2