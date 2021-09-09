"""Counting letters in a string."""

__author__ = "730225468"

letter_choice: str = input("What letter do you want to search for?: ")
word_choice: str = input("Enter a word: ")
count: int = int(len(word_choice))

while len(letter_choice) == 1:
    count = count - 1
    print("Count: " + str(count))
    