"""An exercise in remainders and boolean logic."""

__author__ = "730225468"


prompt: int = int(input("Enter an int: "))


if ((prompt % 2) == 0) and ((prompt % 7) == 0):
    print("TAR HEELS")
else:
    if prompt % 7 == 0:
        print("HEELS")
    else: 
        if prompt % 2 == 0:
            print("TAR")
        else: 
            print("CAROLINA")