"""A program about numbers!"""

__author__ = "730225468"

left: int = int(input("Left-hand side: "))
right: int = int(input("Right-hand side: "))

first_answer: int = left ** right
second_answer: float = left / right
third_answer: int = left // right
fourth_answer: int = left % right

print(str(left) + " ** " + str(right) + " is " + str(first_answer))
print(str(left) + " / " + str(right) + " is " + str(second_answer))
print(str(left) + " // " + str(right) + " is " + str(third_answer))
print(str(left) + " % " + str(right) + " is " + str(fourth_answer))