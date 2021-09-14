"""Finding duplicate letters in a word."""

__author__ = "730225468"


word: str = input("Enter a word: ")
dup: bool = False

i: int = 0

while i < len(word) - 1:
    j: int = i + 1
    while j < len(word):
        if word[i] == word[j]:
            dup = True
        j = j + 1
    i = i + 1

print("Found duplicate: " + str(dup))