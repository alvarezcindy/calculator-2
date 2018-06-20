"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *
from functools import reduce

while True:
    input_string = input("> ")
    token = input_string.split(" ")

    if token[0] == "q":
        break

    operator = token[0]
    numbers = "".join(token[1:])

    if numbers.isdigit():
        float_list = [float(i) for i in token[1:]]
    else:
        print("Please input an operator and at least one number")
        continue

    if operator == "pow":
        answer = reduce(power, float_list)
    elif operator == '+':
        answer = reduce(add, float_list)
    elif operator == '-':
        answer = reduce(subtract, float_list)
    elif operator == '*':
        answer = reduce(multiply, float_list)
    elif operator == '/':
        answer = reduce(divide, float_list)
    elif operator == 'square':
        answer = reduce(square, float_list)
    elif operator == 'cube':
        answer = reduce(cube, float_list)
    elif operator == 'mod':
        answer = reduce(mod, float_list)
    else:
        print("Please input an operator and at least one number")
    print(round(answer, 2))
print("Quitting...")
