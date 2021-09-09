"""Repeating a beat in a loop."""

__author__ = "730225468"

beat: str = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want to repeat it? "))
space: str = " " + beat

if repeat > 0:
    while repeat > 1:
        repeat = repeat - 1
        beat = beat + space
        print(beat)
else:
    print("No beat...")
