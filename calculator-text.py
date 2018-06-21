"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *
from functools import reduce

math_file = open("inputs.txt")


def calculate(math_file):
    """
    Intake file with calculations and output results for each line as a list
    """
    ans_list = []

    for line in math_file:
        line = line.rstrip()
        token = line.split(" ")

        # takes out the operator, changes list of nums to a string
        operator = token[0]
        numbers = "".join(token[1:])

        # checks if the inputs are valid numbers

        if numbers.isdigit():
            float_list = [float(i) for i in token[1:]]
        else:
            continue

        # arithmetic calcs, calls functions

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
            continue

        ans_str = round(answer, 2)
        ans_list.append(ans_str)
    return ans_list


def calc_outputs(ans_list):
    """Intake list of results and output to file"""
    with open("outputs.txt", 'w') as f:
        for item in ans_list:
            f.write("{}\n".format(str(item)))


calc_list = calculate(math_file)
calc_outputs(calc_list)
