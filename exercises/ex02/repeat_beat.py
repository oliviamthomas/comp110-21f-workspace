"""Repeating a beat in a loop."""

__author__ = "730225468"

beat: str = input("What beat do you want to repeat? ")
times: int = int(input("How many times do you want to repeat it? "))
space: str = " " + beat

if times > 0:
    while times > 1:
        times = times - 1
        beat = beat + space
        print(beat)
else:
    print("No beat...")
