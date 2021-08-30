"""A program about True and False!"""

__author__ = "730225468"

left: int = int(input("Left-hand side: "))
right: int = int(input("Right-hand side: "))

first_answer: bool = left < right
second_answer: bool = left >= right
third_answer: bool = left == right
fourth_answer: bool = left != right

print(str(left) + " < " + str(right) + " is " + str(first_answer))
print(str(left) + " >= " + str(right) + " is " + str(second_answer))
print(str(left) + " == " + str(right) + " is " + str(third_answer))
print(str(left) + " != " + str(right) + " is " + str(fourth_answer))