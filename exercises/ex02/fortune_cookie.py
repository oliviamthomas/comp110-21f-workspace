"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730225468"

from random import randint
print(randint(1, 20))

answer: int = randint(1, 20)

print("Your fortune cookie says...")

if answer <= 5:
    print("Today will bring you joy and love!")
else:
    if answer <= 10: 
        print("You will soon have a new friend.")
    else:
        if answer <= 15:
            print("All your hard work will pay off soon!")
        else:
            print("Tomorrow will hold a fun surprise.")

print("Now, go spread positive vibes!")