"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    input_string = input("> ")
    token = input_string.split(" ")

    if len(token) > 3 or len(token) < 2:
        print("Please input an operator and at least one number")

    else:
        operator = token[0]
        num1 = float(token[1])
        num2 = float(token[2])

        if operator == "q":
            break
        elif operator == "pow":
            answer = power(num1, num2)
        elif operator == '+':
            answer = add(num1, num2)
        elif operator == '-':
            answer = subtract(num1, num2)
        elif operator == '*':
            answer = multiply(num1, num2)
        elif operator == '/':
            answer = divide(num1, num2)
        elif operator == 'square':
            answer = square(num1)
        elif operator == 'cube':
            answer = cube(num1)
        elif operator == 'mod':
            answer = mod(num1, num2)
        else:
            print("Please input an operator and at least one number")

        print(answer)

print("Quitting...")
