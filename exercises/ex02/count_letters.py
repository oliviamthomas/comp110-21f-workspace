"""Counting letters in a string."""

__author__ = "730225468"

letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
count: int = int(len(word))

while len(letter) == 1:
    count = count - 1
    print("Count: " + str(count))
    